#!/usr/bin/env python3
"""Validate an anti-churn-audit.json report against schemas/audit-report.schema.json.

Usage:
    python3 scripts/validate_report.py <path-to-anti-churn-audit.json> [more paths...]

Exits non-zero if any file fails validation or fails to parse.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _minischema import validate_file  # noqa: E402

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "audit-report.schema.json"


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: validate_report.py <path-to-anti-churn-audit.json> [more paths...]")
        return 2

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    exit_code = 0
    for arg in argv:
        path = Path(arg)
        if not path.exists():
            print(f"[FAIL] {path}: file not found")
            exit_code = 1
            continue
        try:
            instance = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"[FAIL] {path}: invalid JSON ({exc})")
            exit_code = 1
            continue

        errors = validate_file(instance, schema)
        if errors:
            print(f"[FAIL] {path}: {len(errors)} error(s)")
            for err in errors:
                print(f"  - {err}")
            exit_code = 1
        else:
            print(f"[OK]   {path}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
