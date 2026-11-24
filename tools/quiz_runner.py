#!/usr/bin/env python3
"""Interactive quiz runner for module quizzes and practice exams.

Examples:
    python3 tools/quiz_runner.py modules/05-switching
    python3 tools/quiz_runner.py cert/ccna-200-301/practice-exams/exam-1.md --shuffle --limit 20
    python3 tools/quiz_runner.py modules --all --limit 30      # random mix from every module
"""
from __future__ import annotations

import argparse
import random
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from quizlib import Question, parse_quiz  # noqa: E402


def collect(target: Path, all_modules: bool) -> list[tuple[str, Question]]:
    files: list[Path]
    if target.is_file():
        files = [target]
    elif all_modules:
        files = sorted(target.glob("*/quiz.md"))
    else:
        files = [target / "quiz.md"]
    out: list[tuple[str, Question]] = []
    for f in files:
        if not f.exists():
            sys.exit(f"not found: {f}")
        out.extend((f.parent.name if f.name == "quiz.md" else f.stem, q) for q in parse_quiz(f))
    return out


def ask(src: str, q: Question, idx: int, total: int) -> bool:
    print(f"\n[{idx}/{total}] ({src}) Q{q.number}")
    print(textwrap.fill(q.text.replace("\n", " "), width=100))
    for k, v in q.options.items():
        print(f"  {k}) {v}")
    need = len(q.answers)
    prompt = f"Your answer{' (' + str(need) + ' letters, e.g. B,D)' if need > 1 else ''}: "
    raw = input(prompt).upper().replace(" ", "")
    given = sorted(x for x in raw.split(",") if x)
    ok = given == sorted(q.answers)
    print("  Correct." if ok else f"  Wrong. Answer: {', '.join(q.answers)}")
    print(textwrap.fill("  " + q.explanation, width=100, subsequent_indent="  "))
    return ok


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("target", type=Path, help="module dir, quiz/exam file, or 'modules' with --all")
    p.add_argument("--all", action="store_true", help="pull questions from every module under target")
    p.add_argument("--shuffle", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()

    items = collect(args.target, args.all)
    rng = random.Random(args.seed)
    if args.shuffle or args.all:
        rng.shuffle(items)
    if args.limit:
        items = items[: args.limit]
    score = 0
    try:
        for i, (src, q) in enumerate(items, 1):
            score += ask(src, q, i, len(items))
    except (KeyboardInterrupt, EOFError):
        print("\nStopped.")
        items = items[: i - 1] if items else items
    if items:
        pct = 100 * score / len(items)
        print(f"\nScore: {score}/{len(items)} ({pct:.0f}%). Target: 85% or higher.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
