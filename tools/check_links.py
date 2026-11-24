#!/usr/bin/env python3
"""Check that every relative Markdown link points to a file or directory that exists.

External links (http/https/mailto) are checked in CI by lychee, not here.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def main() -> int:
    bad = 0
    count = 0
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in {"node_modules", ".git"} for part in md.parts):
            continue
        text = FENCE_RE.sub("", md.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            count += 1
            path_part = unquote(target.split("#", 1)[0])
            dest = (md.parent / path_part).resolve()
            if not dest.exists():
                bad += 1
                print(f"{md.relative_to(ROOT)}: broken link -> {target}")
    print(f"checked {count} internal links, {bad} broken")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
