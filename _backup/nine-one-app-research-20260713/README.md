# Nine One Notion Operating System

This repository contains a production-ready sync layer for building the Nine One Notion workspace from markdown strategy, research, product, moat, philosophy, and AI output files.

## What It Creates

Top-level Notion pages:

- `01 — Mission Control`
- `02 — Philosophy`
- `03 — Intelligence`
- `04 — Strategy`
- `05 — Product System`
- `06 — AI Studio`
- `07 — Knowledge Graph`
- `08 — Investor Room`
- `09 — Archive`

Databases:

- `Intelligence Vault`
- `Strategic Decisions`
- `Feature Graph`
- `Philosophy Library`
- `AI Output Library`
- `Moat Map`

Each database includes review state, source tracking, timestamps, select fields, status fields, and relation fields.

## Safety Rules

The sync is intentionally calm and idempotent.

- It never deletes Notion pages.
- It uses `Source Path` as the unique ID.
- It does not create duplicate imported records for the same markdown file path.
- It defaults imported records to `Status = Needs Review`.
- It defaults `Human Reviewed = false` and `Accepted Into System = false` on first import.
- It does not overwrite reviewed status once `Human Reviewed` or `Accepted Into System` has been checked in Notion.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set environment variables:

```bash
export NOTION_TOKEN="secret_xxx"
export NOTION_ROOT_PAGE_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export OPENAI_API_KEY="sk-..."
```

Run a local classification preview:

```bash
python scripts/notion_sync.py --root . --dry-run
```

Create or update the Notion workspace:

```bash
python scripts/notion_sync.py --root .
```

## GitHub Actions

The workflow at `.github/workflows/notion-sync.yml` runs on pushes to `main` when markdown files or sync code changes.

Add these repository secrets:

- `NOTION_TOKEN`
- `NOTION_ROOT_PAGE_ID`
- `OPENAI_API_KEY`

## Architecture

The system is split into small modules:

- `notion_os/config.py` loads environment configuration.
- `notion_os/schema.py` defines database schemas and relation fields.
- `notion_os/taxonomy.py` classifies markdown into the right workspace destination.
- `notion_os/markdown.py` scans files, hashes content, extracts titles, and converts markdown into Notion blocks.
- `notion_os/notion_api.py` creates pages/databases and upserts records through the Notion API.
- `notion_os/relation_mapper.py` creates cross-database links from shared tags and areas.
- `notion_os/sync.py` orchestrates the full sync.

## Operating Model

Markdown remains the durable source of truth. Notion becomes the operating surface:

- research goes into `Intelligence Vault`
- choices go into `Strategic Decisions`
- product surfaces go into `Feature Graph`
- principles go into `Philosophy Library`
- generated work goes into `AI Output Library`
- defensibility logic goes into `Moat Map`

The result is a minimal, AI-native workspace where human review remains explicit and high-signal.
