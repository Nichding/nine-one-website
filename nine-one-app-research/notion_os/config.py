from __future__ import annotations

from dataclasses import dataclass
import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


NOTION_VERSION = "2022-06-28"


@dataclass(frozen=True)
class Settings:
    notion_token: str
    notion_root_page_id: str
    openai_api_key: str | None = None
    openai_model: str = "gpt-4.1-mini"


def load_settings() -> Settings:
    if load_dotenv:
        load_dotenv()

    notion_token = os.getenv("NOTION_TOKEN", "").strip()
    notion_root_page_id = os.getenv("NOTION_ROOT_PAGE_ID", "").strip()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip() or None
    openai_model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()

    missing = []
    if not notion_token:
        missing.append("NOTION_TOKEN")
    if not notion_root_page_id:
        missing.append("NOTION_ROOT_PAGE_ID")
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")

    return Settings(
        notion_token=notion_token,
        notion_root_page_id=notion_root_page_id,
        openai_api_key=openai_api_key,
        openai_model=openai_model,
    )
