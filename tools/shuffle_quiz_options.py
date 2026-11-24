#!/usr/bin/env python3
"""Deterministically shuffle answer options in quiz Markdown files and fix the answer letters.

Why: hand-written questions tend to put the right answer in the same position.
Shuffling with a fixed seed per question removes that pattern and stays stable across runs.

Usage: python3 tools/shuffle_quiz_options.py modules/*/quiz.md
Options whose text refers to other letters ("Both A and B") or to position ("All of the above")
keep their order.
"""
from __future__ import annotations

import hashlib
import random
import re
import sys
from pathlib import Path

LETTERS = "ABCDEF"
POSITIONAL = re.compile(r"\b[A-F] and [A-F]\b|of the above|None of these|All of these")


def shuffle_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    i = 0
    changed = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith("### Q"):
            out.append(line)
            i += 1
            continue
        # collect the question block up to </details>
        j = i
        while j < len(lines) and not lines[j].startswith("</details>"):
            j += 1
        block = lines[i : j + 1]
        opt_idx = [k for k, l in enumerate(block) if re.match(r"^- [A-F]\) ", l)]
        opts = [re.sub(r"^- [A-F]\) ", "", block[k]) for k in opt_idx]
        ans_k = next(k for k, l in enumerate(block) if l.startswith("**Answer: "))
        m = re.match(r"^\*\*Answer: ([A-F](?:, ?[A-F])*)\.\*\*(.*)$", block[ans_k])
        if not opts or not m or any(POSITIONAL.search(o) for o in opts):
            out.extend(block)
            i = j + 1
            continue
        answers = [a.strip() for a in m.group(1).split(",")]
        seed = int(hashlib.sha256(block[0].encode()).hexdigest(), 16) % (2**32)
        # Start from a canonical (sorted) order so running the tool twice gives the same result.
        order = sorted(range(len(opts)), key=lambda k: opts[k])
        random.Random(seed).shuffle(order)
        new_opts = [opts[o] for o in order]
        mapping = {LETTERS[o]: LETTERS[n] for n, o in enumerate(order)}
        new_answers = sorted(mapping[a] for a in answers)
        for n, k in enumerate(opt_idx):
            block[k] = f"- {LETTERS[n]}) {new_opts[n]}"
        block[ans_k] = f"**Answer: {', '.join(new_answers)}.**{m.group(2)}"
        changed += 1
        out.extend(block)
        i = j + 1
    path.write_text("\n".join(out), encoding="utf-8")
    return changed


def main() -> int:
    total = 0
    for p in sys.argv[1:]:
        n = shuffle_file(Path(p))
        total += n
        print(f"{p}: shuffled {n} questions")
    print(f"total {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
