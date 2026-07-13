#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from notion_os.sync import sync_workspace


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Nine One markdown knowledge into the Notion Operating System.")
    parser.add_argument("--root", default=".", help="Repository root to scan for markdown files.")
    parser.add_argument("--dry-run", action="store_true", help="Classify files without writing to Notion.")
    args = parser.parse_args()

    result = sync_workspace(Path(args.root).resolve(), dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
