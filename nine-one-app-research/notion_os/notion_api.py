from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from notion_client import Client

from notion_os.config import Settings
from notion_os.schema import DATABASES, RELATIONS, database_properties
from notion_os.taxonomy import DATABASE_PARENT_PAGE, TOP_LEVEL_PAGES


def rich_text(value: str | None) -> list[dict]:
    if not value:
        return []
    return [{"type": "text", "text": {"content": value[:1900]}}]


def title(value: str) -> list[dict]:
    return [{"type": "text", "text": {"content": value[:1900]}}]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class WorkspaceState:
    pages: dict[str, str]
    databases: dict[str, str]


class NotionOS:
    def __init__(self, settings: Settings) -> None:
        self.client = Client(auth=settings.notion_token)
        self.root_page_id = settings.notion_root_page_id

    def list_child_pages(self, page_id: str) -> dict[str, str]:
        pages: dict[str, str] = {}
        cursor = None
        while True:
            response = self.client.blocks.children.list(block_id=page_id, start_cursor=cursor)
            for block in response.get("results", []):
                if block.get("type") == "child_page":
                    pages[block["child_page"]["title"]] = block["id"]
            if not response.get("has_more"):
                break
            cursor = response.get("next_cursor")
        return pages

    def ensure_top_pages(self) -> dict[str, str]:
        existing = self.list_child_pages(self.root_page_id)
        pages: dict[str, str] = {}
        for page_title in TOP_LEVEL_PAGES:
            if page_title in existing:
                pages[page_title] = existing[page_title]
                continue
            created = self.client.pages.create(
                parent={"page_id": self.root_page_id},
                properties={"title": {"title": title(page_title)}},
                children=[
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": rich_text("Nine One operating system surface.")},
                    }
                ],
            )
            pages[page_title] = created["id"]
        return pages

    def discover_databases(self) -> dict[str, str]:
        found: dict[str, str] = {}
        for name in DATABASES:
            response = self.client.search(
                query=name,
                filter={"property": "object", "value": "database"},
                sort={"direction": "descending", "timestamp": "last_edited_time"},
            )
            for item in response.get("results", []):
                title_text = "".join(part.get("plain_text", "") for part in item.get("title", []))
                if title_text == name:
                    found[name] = item["id"]
                    break
        return found

    def ensure_databases(self, pages: dict[str, str]) -> dict[str, str]:
        existing = self.discover_databases()
        database_ids: dict[str, str] = {}

        for name, config in DATABASES.items():
            if name in existing:
                database_ids[name] = existing[name]
                continue
            parent_page_id = pages[DATABASE_PARENT_PAGE[name]]
            created = self.client.databases.create(
                parent={"type": "page_id", "page_id": parent_page_id},
                title=title(name),
                description=rich_text(config["description"]),
                properties=database_properties(name),
            )
            database_ids[name] = created["id"]

        for source_name, relations in RELATIONS.items():
            relation_props: dict[str, Any] = {}
            for prop_name, target_name in relations.items():
                relation_props[prop_name] = {
                    "relation": {
                        "database_id": database_ids[target_name],
                        "type": "dual_property",
                        "dual_property": {},
                    }
                }
            self.client.databases.update(database_id=database_ids[source_name], properties=relation_props)

        return database_ids

    def ensure_workspace(self) -> WorkspaceState:
        pages = self.ensure_top_pages()
        databases = self.ensure_databases(pages)
        return WorkspaceState(pages=pages, databases=databases)

    def find_page_by_source_path(self, database_id: str, source_path: str) -> dict | None:
        response = self.client.databases.query(
            database_id=database_id,
            filter={"property": "Source Path", "rich_text": {"equals": source_path}},
            page_size=1,
        )
        results = response.get("results", [])
        return results[0] if results else None

    def build_import_properties(self, *, name: str, source_path: str, source_hash: str, classification: Any) -> dict:
        return {
            "Name": {"title": title(name)},
            "Status": {"status": {"name": "Needs Review"}},
            "Source Type": {"select": {"name": classification.source_type}},
            "Source Path": {"rich_text": rich_text(source_path)},
            "Source Hash": {"rich_text": rich_text(source_hash)},
            "Strategic Area": {"select": {"name": classification.strategic_area}},
            "Product Area": {"select": {"name": classification.product_area}},
            "Tags": {"multi_select": [{"name": tag} for tag in classification.tags]},
            "Summary": {"rich_text": rich_text(classification.summary)},
            "Last Synced": {"date": {"start": now_iso()}},
        }

    def create_import_page(self, database_id: str, properties: dict, children: list[dict]) -> str:
        properties["Human Reviewed"] = {"checkbox": False}
        properties["Accepted Into System"] = {"checkbox": False}
        created = self.client.pages.create(
            parent={"database_id": database_id},
            properties=properties,
            children=children[:100],
        )
        return created["id"]

    def update_import_page(self, page: dict, properties: dict) -> str:
        current = page.get("properties", {})
        source_hash = current.get("Source Hash", {}).get("rich_text", [])
        current_hash = source_hash[0].get("plain_text", "") if source_hash else ""
        incoming_hash = properties["Source Hash"]["rich_text"][0]["text"]["content"]

        if current_hash == incoming_hash:
            properties = {"Last Synced": properties["Last Synced"]}

        reviewed = current.get("Human Reviewed", {}).get("checkbox")
        accepted = current.get("Accepted Into System", {}).get("checkbox")
        if reviewed:
            properties.pop("Human Reviewed", None)
            properties.pop("Status", None)
        if accepted:
            properties.pop("Accepted Into System", None)

        self.client.pages.update(page_id=page["id"], properties=properties)
        return page["id"]

    def update_relations(self, page_id: str, relation_updates: dict[str, list[str]]) -> None:
        properties = {
            prop_name: {"relation": [{"id": target_id} for target_id in page_ids]}
            for prop_name, page_ids in relation_updates.items()
            if page_ids
        }
        if properties:
            self.client.pages.update(page_id=page_id, properties=properties)
