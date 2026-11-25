#!/usr/bin/env python3
"""Validate the guidelines. No third-party dependencies.

Checks:
  1. The three core documents together stay under CORE_WORD_BUDGET words (about 5 pages).
  2. Each core document has an owner line and uses TODO(org) placeholders (so it is a template, not a finished policy).
  3. Relative Markdown links resolve; the README lists every document in docs/.
  4. No credential patterns.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CORE = ["01-ai-usage-policy.md", "02-claude-md-standards.md", "03-ai-pr-review-checklist.md"]
CORE_WORD_BUDGET = 2500  # roughly five printed pages
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def words(text: str) -> int:
    return len(re.findall(r"\S+", re.sub(r"```.*?```", "", text, flags=re.DOTALL)))


def check_core() -> int:
    total = 0
    for name in CORE:
        p = DOCS / name
        if not p.exists():
            err(f"docs/{name}: missing")
            continue
        text = p.read_text(encoding="utf-8")
        total += words(text)
        if "TODO(org)" not in text and name != "03-ai-pr-review-checklist.md":
            err(f"docs/{name}: expected TODO(org) placeholders")
    if total > CORE_WORD_BUDGET:
        err(f"core documents total {total} words; budget is {CORE_WORD_BUDGET} (about 5 pages)")
    return total


def check_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for p in sorted(DOCS.glob("*.md")):
        if f"docs/{p.name}" not in readme:
            err(f"README.md: docs/{p.name} is not linked")


SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
]
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")


def check_files() -> None:
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts or p.suffix not in {".md", ".py", ".yml"}:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                err(f"{p.relative_to(ROOT)}: matches credential pattern {pat.pattern!r}")
        if p.suffix != ".md":
            continue
        in_fence = False
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"[a-z]+:", target):
                    continue
                if not (p.parent / target).resolve().exists():
                    err(f"{p.relative_to(ROOT)}:{n}: broken link {target}")


def main() -> int:
    total = check_core()
    check_readme()
    check_files()
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: core documents total {total} words (budget {CORE_WORD_BUDGET}); links and credential checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
