from __future__ import annotations

from notion_os.schema import RELATIONS


def overlap_score(source: dict, target: dict) -> int:
    source_class = source["classification"]
    target_class = target["classification"]
    source_tags = set(source_class["tags"])
    target_tags = set(target_class["tags"])

    score = len(source_tags & target_tags) * 3
    if source_class["strategic_area"] == target_class["strategic_area"]:
        score += 2
    if source_class["product_area"] == target_class["product_area"]:
        score += 2
    return score


def build_relation_updates(records: list[dict]) -> dict[str, dict[str, list[str]]]:
    by_destination: dict[str, list[dict]] = {}
    for record in records:
        if "notion_page_id" not in record:
            continue
        destination = record["classification"]["destination"]
        by_destination.setdefault(destination, []).append(record)

    updates: dict[str, dict[str, list[str]]] = {}
    for record in records:
        if "notion_page_id" not in record:
            continue

        source_db = record["classification"]["destination"]
        source_relations = RELATIONS.get(source_db, {})
        page_updates: dict[str, list[str]] = {}

        for relation_name, target_db in source_relations.items():
            candidates = []
            for target in by_destination.get(target_db, []):
                score = overlap_score(record, target)
                if score > 0:
                    candidates.append((score, target["notion_page_id"]))
            candidates.sort(reverse=True)
            if candidates:
                page_updates[relation_name] = [page_id for _, page_id in candidates[:12]]

        if page_updates:
            updates[record["notion_page_id"]] = page_updates

    return updates
