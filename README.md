# ai-team-guidelines

Opinionated, ready-to-adopt templates for governing how an engineering team uses AI coding tools. Most organizations have no written AI policy; CTOs and VPs of Engineering are being asked for one right now and want a starting point, not a blank page.

Three short documents — light enough that people read them — each annotated with the reasoning behind every rule, plus optional add-ons for security review and regulated industries.

> Companion to [How I Set Up Claude Code for a Team of 25](https://ivandir.com/blog/claude-code-team-case-study.html). Written from running AI adoption across an engineering organization.

## The core three

Together about **1,400 words — roughly three pages**. CI enforces a five-page (2,500-word) budget so they stay readable as they grow.

| Document | Answers | Audience |
| --- | --- | --- |
| [`docs/01-ai-usage-policy.md`](docs/01-ai-usage-policy.md) | Which tools, what data may go in, who is accountable, what to do when it goes wrong | Everyone |
| [`docs/02-claude-md-standards.md`](docs/02-claude-md-standards.md) | How we write, own and review `CLAUDE.md` so output quality is a team property | Engineers, tech leads |
| [`docs/03-ai-pr-review-checklist.md`](docs/03-ai-pr-review-checklist.md) | What authors disclose and what reviewers check on AI-assisted changes | Authors, reviewers |

## Add-ons

| Document | Use when |
| --- | --- |
| [`docs/security-review-additions.md`](docs/security-review-additions.md) | A feature *uses* AI at runtime (LLM calls, agents, RAG): data flow, prompt injection, tool permissions, output handling |
| [`docs/regulated-industries.md`](docs/regulated-industries.md) | You are in fintech, healthtech or another regulated space and need heavier alternatives to each core document |

## How to adopt (an afternoon)

1. Copy the three core documents into your handbook or an internal repo.
2. Search for `TODO(org)` and fill in tool names, owners, contacts and timelines.
3. Have **legal and security review** it. These are templates, not legal advice.
4. Decide what to cut. A rule nobody will follow is worse than no rule.
5. Announce it, run one 30-minute walkthrough, and put the PR-template section in place.
6. Put a six-month review date on the calendar.

Rule of thumb: keep the *Why* lines. People follow rules they understand.

## Design principles

- **Short enough to read.** If it needs a training course to understand, it won't be followed.
- **Absolute where it matters, flexible elsewhere.** Restricted data and irreversible actions get hard lines; everything else is judgement.
- **Accountability stays with the human.** AI is a tool; the engineer owns the change.
- **Disclosure is a signal, not a penalty.**
- **Enforce what you can.** Pair these documents with enforced settings: see [`claude-code-org-setup`](https://github.com/ivandir/claude-code-org-setup) (permission presets) and [`claude-code-security`](https://github.com/ivandir/claude-code-security) (hooks and audit logging).

## Validate

```bash
python scripts/validate.py
```

## License

[MIT](LICENSE). Not legal advice — have counsel review before adopting.
