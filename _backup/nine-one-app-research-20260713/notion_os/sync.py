from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from notion_os.config import load_settings
from notion_os.markdown import file_hash, iter_markdown_files, markdown_to_blocks, read_markdown, title_from_markdown
from notion_os.relation_mapper import build_relation_updates
from notion_os.taxonomy import classify_markdown


def sync_workspace(root: Path, dry_run: bool = False) -> dict:
    files = iter_markdown_files(root)

    results = {
        "root": str(root),
        "dry_run": dry_run,
        "markdown_files": len(files),
        "created": 0,
        "updated": 0,
        "skipped": 0,
        "records": [],
    }

    notion = None
    if dry_run:
        database_ids = {}
    else:
        from notion_os.notion_api import NotionOS

        settings = load_settings()
        notion = NotionOS(settings)
        state = notion.ensure_workspace()
        database_ids = state.databases

    for path in files:
        markdown = read_markdown(path)
        relative_path = str(path.relative_to(root))
        source_hash = file_hash(markdown)
        name = title_from_markdown(path, markdown)
        classification = classify_markdown(relative_path, markdown)

        record = {
            "path": relative_path,
            "name": name,
            "hash": source_hash,
            "classification": asdict(classification),
        }

        if dry_run:
            results["records"].append(record)
            continue

        assert notion is not None
        database_id = database_ids[classification.destination]
        properties = notion.build_import_properties(
            name=name,
            source_path=relative_path,
            source_hash=source_hash,
            classification=classification,
        )
        existing = notion.find_page_by_source_path(database_id, relative_path)
        if existing:
            page_id = notion.update_import_page(existing, properties)
            results["updated"] += 1
        else:
            page_id = notion.create_import_page(database_id, properties, markdown_to_blocks(markdown))
            results["created"] += 1
        record["notion_page_id"] = page_id
        results["records"].append(record)

    if not dry_run:
        assert notion is not None
        relation_updates = build_relation_updates(results["records"])
        for page_id, updates in relation_updates.items():
            notion.update_relations(page_id, updates)
        results["relation_updates"] = len(relation_updates)

    return results
