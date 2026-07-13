from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable


TOP_LEVEL_PAGES = [
    "01 — Mission Control",
    "02 — Philosophy",
    "03 — Intelligence",
    "04 — Strategy",
    "05 — Product System",
    "06 — AI Studio",
    "07 — Knowledge Graph",
    "08 — Investor Room",
    "09 — Archive",
]


DATABASE_PARENT_PAGE = {
    "Intelligence Vault": "03 — Intelligence",
    "Strategic Decisions": "04 — Strategy",
    "Feature Graph": "05 — Product System",
    "Philosophy Library": "02 — Philosophy",
    "AI Output Library": "06 — AI Studio",
    "Moat Map": "07 — Knowledge Graph",
}


STRATEGIC_AREAS = [
    "Ecosystem",
    "Moat",
    "Network Effects",
    "Market",
    "Competition",
    "Investor Narrative",
    "Product Strategy",
    "Operations",
    "Partnerships",
    "Brand",
]


PRODUCT_AREAS = [
    "Padel",
    "Smart Infrastructure",
    "AI Coaching",
    "Venue Intelligence",
    "Player Identity",
    "Data Platform",
    "MVP",
    "Hardware",
    "Software",
    "Community",
]


SOURCE_TYPES = ["Markdown", "Research", "AI Output", "Decision", "Product Spec", "Philosophy", "Archive"]


STATUS_VALUES = ["Needs Review", "In Review", "Accepted", "Archived"]


TAG_KEYWORDS = {
    "padel": ["padel", "court", "match", "coach", "racket", "club"],
    "smart infrastructure": ["camera", "sensor", "infrastructure", "hardware", "computer vision", "iot"],
    "ai coaching": ["coaching", "coach", "feedback", "training", "skill", "performance"],
    "venue intelligence": ["venue", "operator", "utilization", "booking", "revenue", "occupancy"],
    "player identity": ["identity", "profile", "player", "reputation", "progress", "passport"],
    "data network effects": ["network effect", "data network", "flywheel", "defensibility", "moat"],
    "mvp": ["mvp", "prototype", "pilot", "launch", "roadmap"],
    "investor": ["investor", "fundraising", "deck", "venture", "market size"],
    "competitor": ["competitor", "competition", "benchmark", "rival", "comparison"],
    "strategy": ["strategy", "strategic", "positioning", "thesis"],
    "philosophy": ["philosophy", "principle", "belief", "manifesto", "doctrine"],
}


DESTINATION_RULES = [
    ("Philosophy Library", ["philosophy", "principle", "manifesto", "belief", "doctrine"]),
    ("Moat Map", ["moat", "defensibility", "network effect", "flywheel", "lock-in"]),
    ("Feature Graph", ["feature", "product definition", "prd", "mvp", "roadmap", "user story"]),
    ("Strategic Decisions", ["decision", "strategy", "positioning", "thesis", "choice"]),
    ("AI Output Library", ["ai output", "generated", "prompt", "llm", "gpt"]),
    ("Intelligence Vault", ["research", "competitor", "analysis", "market", "intelligence"]),
]


@dataclass(frozen=True)
class Classification:
    destination: str
    tags: list[str]
    strategic_area: str
    product_area: str
    source_type: str
    summary: str


def normalize_text(*parts: str) -> str:
    return " ".join(parts).lower()


def compact_summary(markdown: str, max_chars: int = 650) -> str:
    text = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text).strip()
    return text[: max_chars - 1] + "…" if len(text) > max_chars else text


def contains_any(text: str, keywords: Iterable[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def pick_first(text: str, options: list[str], fallback: str) -> str:
    for option in options:
        if option.lower() in text:
            return option
    return fallback


def classify_markdown(path: str, markdown: str) -> Classification:
    text = normalize_text(path, markdown[:6000])
    tags = [tag.title() for tag, keywords in TAG_KEYWORDS.items() if contains_any(text, keywords)]

    destination = "Intelligence Vault"
    for database, keywords in DESTINATION_RULES:
        if contains_any(text, keywords):
            destination = database
            break

    source_type = "Markdown"
    if destination == "AI Output Library":
        source_type = "AI Output"
    elif destination == "Strategic Decisions":
        source_type = "Decision"
    elif destination == "Feature Graph":
        source_type = "Product Spec"
    elif destination == "Philosophy Library":
        source_type = "Philosophy"
    elif "research" in text or "competitor" in text:
        source_type = "Research"

    strategic_area = pick_first(text, STRATEGIC_AREAS, "Ecosystem")
    product_area = pick_first(text, PRODUCT_AREAS, "Data Platform")

    return Classification(
        destination=destination,
        tags=sorted(set(tags)) or ["Unclassified"],
        strategic_area=strategic_area,
        product_area=product_area,
        source_type=source_type,
        summary=compact_summary(markdown),
    )
