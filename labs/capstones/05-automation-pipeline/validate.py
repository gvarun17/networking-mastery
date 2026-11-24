#!/usr/bin/env python3
"""Validate the source of truth. Exit 1 on any error (fails the CI job)."""
from __future__ import annotations

import sys

import netintent


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else None
    intent = netintent.load(path) if path else netintent.load()
    errors = netintent.validate(intent)
    for e in errors:
        print(f"ERROR: {e}")
    print(f"{len(intent.get('routers', {}))} routers, {len(intent.get('links', []))} links, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
