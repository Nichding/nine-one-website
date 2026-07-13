from __future__ import annotations

from copy import deepcopy

from notion_os.taxonomy import PRODUCT_AREAS, SOURCE_TYPES, STATUS_VALUES, STRATEGIC_AREAS


def select_options(values: list[str], color: str = "gray") -> list[dict]:
    return [{"name": value, "color": color} for value in values]


COMMON_PROPERTIES = {
    "Name": {"title": {}},
    "Status": {"status": {"options": select_options(STATUS_VALUES)}},
    "Human Reviewed": {"checkbox": {}},
    "Accepted Into System": {"checkbox": {}},
    "Source Type": {"select": {"options": select_options(SOURCE_TYPES, "blue")}},
    "Source Path": {"rich_text": {}},
    "Source Hash": {"rich_text": {}},
    "Source URL": {"url": {}},
    "Strategic Area": {"select": {"options": select_options(STRATEGIC_AREAS, "purple")}},
    "Product Area": {"select": {"options": select_options(PRODUCT_AREAS, "green")}},
    "Tags": {"multi_select": {"options": []}},
    "Summary": {"rich_text": {}},
    "Last Synced": {"date": {}},
    "Created": {"created_time": {}},
    "Updated": {"last_edited_time": {}},
}


DATABASES = {
    "Intelligence Vault": {
        "description": "Research, analysis, competitor notes, market observations, and raw strategic intelligence.",
        "extra": {
            "Signal Strength": {"select": {"options": select_options(["Weak", "Medium", "Strong"], "yellow")}},
            "Confidence": {"select": {"options": select_options(["Low", "Medium", "High"], "orange")}},
        },
    },
    "Strategic Decisions": {
        "description": "Clear strategic choices, open questions, decisions, and rationale.",
        "extra": {
            "Decision Type": {"select": {"options": select_options(["Principle", "Product", "Market", "Moat", "Operating"], "red")}},
            "Decision Date": {"date": {}},
        },
    },
    "Feature Graph": {
        "description": "Product capabilities, MVP scope, feature dependencies, and ecosystem surfaces.",
        "extra": {
            "Feature Stage": {"select": {"options": select_options(["Concept", "MVP", "Pilot", "Scaled"], "green")}},
            "User Surface": {"select": {"options": select_options(["Player", "Coach", "Venue", "Operator", "Investor", "Internal"], "blue")}},
        },
    },
    "Philosophy Library": {
        "description": "Principles, beliefs, operating philosophy, and long-term product doctrine.",
        "extra": {
            "Principle Type": {"select": {"options": select_options(["Product", "Brand", "AI", "Ecosystem", "Operating"], "purple")}},
        },
    },
    "AI Output Library": {
        "description": "AI-generated analyses, drafts, prompts, and model-assisted synthesis.",
        "extra": {
            "AI Role": {"select": {"options": select_options(["Researcher", "Strategist", "Product", "Investor", "Operator"], "pink")}},
            "Model": {"rich_text": {}},
            "Prompt Source": {"rich_text": {}},
        },
    },
    "Moat Map": {
        "description": "Defensibility assets, compounding advantages, data loops, and strategic moats.",
        "extra": {
            "Moat Type": {"select": {"options": select_options(["Data", "Network", "Brand", "Distribution", "Infrastructure", "Workflow"], "orange")}},
            "Compounding Strength": {"select": {"options": select_options(["Early", "Emerging", "Durable", "Dominant"], "yellow")}},
        },
    },
}


RELATIONS = {
    "Intelligence Vault": {
        "Related Decisions": "Strategic Decisions",
        "Related Features": "Feature Graph",
        "Related Philosophy": "Philosophy Library",
        "Related AI Outputs": "AI Output Library",
        "Related Moats": "Moat Map",
    },
    "Strategic Decisions": {
        "Supporting Intelligence": "Intelligence Vault",
        "Related Features": "Feature Graph",
        "Related Moats": "Moat Map",
    },
    "Feature Graph": {
        "Supporting Intelligence": "Intelligence Vault",
        "Strategic Decisions": "Strategic Decisions",
        "Related AI Outputs": "AI Output Library",
        "Related Moats": "Moat Map",
    },
    "Philosophy Library": {
        "Related Intelligence": "Intelligence Vault",
        "Related AI Outputs": "AI Output Library",
        "Related Moats": "Moat Map",
    },
    "AI Output Library": {
        "Source Intelligence": "Intelligence Vault",
        "Related Features": "Feature Graph",
        "Related Philosophy": "Philosophy Library",
    },
    "Moat Map": {
        "Supporting Intelligence": "Intelligence Vault",
        "Strategic Decisions": "Strategic Decisions",
        "Related Features": "Feature Graph",
        "Related Philosophy": "Philosophy Library",
    },
}


def database_properties(name: str) -> dict:
    properties = deepcopy(COMMON_PROPERTIES)
    properties.update(DATABASES[name]["extra"])
    return properties
