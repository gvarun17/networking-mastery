"""Parse quiz Markdown files used in this repo.

Format (one block per question):

    ### Q1. Question text (may continue on following lines)
    - A) option
    - B) option
    - C) option
    - D) option

    <details><summary>Answer</summary>

    **Answer: B.** Explanation text.

    </details>

Multi-answer questions use "**Answer: B, D.**".
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

Q_RE = re.compile(r"^### Q(\d+)\.\s*(.*)$")
OPT_RE = re.compile(r"^- ([A-F])\) (.*)$")
ANS_RE = re.compile(r"\*\*Answer: ([A-F](?:, ?[A-F])*)\.\*\*\s*(.*)")


@dataclass
class Question:
    number: int
    text: str
    options: dict[str, str] = field(default_factory=dict)
    answers: list[str] = field(default_factory=list)
    explanation: str = ""


def parse_quiz(path: str | Path) -> list[Question]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    questions: list[Question] = []
    cur: Question | None = None
    in_details = False
    for line in lines:
        m = Q_RE.match(line)
        if m:
            cur = Question(int(m.group(1)), m.group(2).strip())
            questions.append(cur)
            in_details = False
            continue
        if cur is None:
            continue
        if line.startswith("<details"):
            in_details = True
            continue
        if line.startswith("</details>"):
            in_details = False
            continue
        if in_details:
            a = ANS_RE.search(line)
            if a:
                cur.answers = [x.strip() for x in a.group(1).split(",")]
                cur.explanation = a.group(2).strip()
            elif line.strip() and cur.answers:
                cur.explanation += " " + line.strip()
            continue
        o = OPT_RE.match(line)
        if o:
            cur.options[o.group(1)] = o.group(2).strip()
        elif line.strip() and not cur.options:
            cur.text += "\n" + line.strip()
    return questions


def validate(questions: list[Question], expected: int | None = None) -> list[str]:
    errors: list[str] = []
    if expected is not None and len(questions) != expected:
        errors.append(f"expected {expected} questions, found {len(questions)}")
    for i, q in enumerate(questions, 1):
        if q.number != i:
            errors.append(f"Q{q.number}: numbering out of order (expected Q{i})")
        if len(q.options) < 2:
            errors.append(f"Q{q.number}: fewer than 2 options")
        if not q.answers:
            errors.append(f"Q{q.number}: no answer found")
        for a in q.answers:
            if a not in q.options:
                errors.append(f"Q{q.number}: answer {a} is not an option")
        if not q.explanation:
            errors.append(f"Q{q.number}: no explanation")
    return errors
