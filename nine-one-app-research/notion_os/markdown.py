from __future__ import annotations

import hashlib
from pathlib import Path
import re


IGNORED_DIRS = {".git", ".venv", "venv", "node_modules", ".next", "dist", "build", "__pycache__"}


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def file_hash(markdown: str) -> str:
    return hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def title_from_markdown(path: Path, markdown: str) -> str:
    heading = re.search(r"^\s*#\s+(.+?)\s*$", markdown, re.MULTILINE)
    if heading:
        return heading.group(1).strip()[:120]
    return path.stem.replace("-", " ").replace("_", " ").strip().title()[:120]


def markdown_to_blocks(markdown: str, max_blocks: int = 80) -> list[dict]:
    blocks: list[dict] = []
    code_language = "plain text"
    in_code = False
    code_lines: list[str] = []

    def append_paragraph(text: str) -> None:
        text = text.strip()
        if text:
            blocks.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": text[:1900]}}]},
                }
            )

    for raw_line in markdown.splitlines():
        if len(blocks) >= max_blocks:
            break
        line = raw_line.rstrip()

        if line.startswith("```"):
            if in_code:
                content = "\n".join(code_lines).strip()
                if content:
                    blocks.append(
                        {
                            "object": "block",
                            "type": "code",
                            "code": {
                                "language": code_language,
                                "rich_text": [{"type": "text", "text": {"content": content[:1900]}}],
                            },
                        }
                    )
                in_code = False
                code_lines = []
                code_language = "plain text"
            else:
                in_code = True
                code_language = line.removeprefix("```").strip() or "plain text"
            continue

        if in_code:
            code_lines.append(line)
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            block_type = {1: "heading_1", 2: "heading_2", 3: "heading_3"}[level]
            blocks.append(
                {
                    "object": "block",
                    "type": block_type,
                    block_type: {"rich_text": [{"type": "text", "text": {"content": heading.group(2)[:1900]}}]},
                }
            )
            continue

        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        if bullet:
            blocks.append(
                {
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": bullet.group(1)[:1900]}}]},
                }
            )
            continue

        numbered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if numbered:
            blocks.append(
                {
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": numbered.group(1)[:1900]}}]},
                }
            )
            continue

        append_paragraph(line)

    if len(blocks) >= max_blocks:
        blocks.append(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": "Import truncated. Full source remains in repository."}}]
                },
            }
        )

    return blocks
