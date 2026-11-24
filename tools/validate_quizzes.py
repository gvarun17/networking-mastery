#!/usr/bin/env python3
"""Check every module quiz and practice exam for structure errors.

- Module quizzes must have exactly 15 questions.
- Practice exams must have exactly 100 questions.
- Every answer letter must exist in the options, and every question needs an explanation.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from quizlib import parse_quiz, validate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    failures = 0
    checked = 0
    targets = [(p, 15) for p in sorted(ROOT.glob("modules/*/quiz.md"))]
    targets += [(p, 100) for p in sorted(ROOT.glob("cert/*/practice-exams/exam-*.md"))]
    for path, expected in targets:
        errs = validate(parse_quiz(path), expected)
        checked += 1
        for e in errs:
            failures += 1
            print(f"{path.relative_to(ROOT)}: {e}")
    print(f"checked {checked} files, {failures} problems")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
