# PR Review Checklist for AI-Assisted Code

> **Template.** Two parts: what authors add to the PR, and what reviewers check. Same standard for all code — this just points reviewers at where AI-assisted changes tend to fail.

## Part 1 — Author: PR template section

Paste into your PR template:

```markdown
## AI assistance
- [ ] None
- [ ] AI-assisted (I wrote or heavily edited the result)
- [ ] Mostly AI-generated (I reviewed every line)

**What I verified myself:** <e.g. traced the main path, ran tests, checked error handling>
**What I'm unsure about:** <anything you want looked at harder — "nothing" is fine if true>

- [ ] I can explain every change in this PR
```

*Why:* "What I verified" makes authors verify. "What I'm unsure about" is the most useful line a reviewer can get.

## Part 2 — Reviewer checklist

Ordered by how often AI-assisted code fails, not by how easy the check is.

1. **Intent** — Does the change do what the description says? Is the *why* stated? *(AI-written descriptions often miss the why.)*
2. **Correctness** — Trace one non-trivial path by hand. Plausible-looking code that passes shallow tests is the typical failure.
3. **Fit** — Does it follow our existing patterns and architecture, or invent a parallel one?
4. **Security** — Input validation, authn/authz, injection, secrets, PII in logs. See [`security-review-additions.md`](security-review-additions.md) for features that add AI behavior.
5. **Dependencies** — Any new package: does it exist, is it maintained, is the license OK? (Hallucinated package names are a supply-chain risk.)
6. **Tests** — Do they assert *behavior* and cover failure paths, or just mirror the implementation? Would they fail without the change?
7. **Scope** — Reformatting, renames, unrelated "improvements", extra abstractions. Ask for a smaller diff.
8. **Understanding** — For anything non-obvious ask: *"Do you understand why this works?"*

## Reviewer rules

- "Claude suggested it" is never an answer to a design question.
- Hold AI-assisted code to the **same bar** as any other — no lower, no higher.
- Large AI-generated diffs are hard to review: ask the author to split them. Over about 800 changed lines, don't approve a skim.
- If one author repeatedly ships correct-looking but naive code, coach and pair; don't respond with more tooling restrictions.

*Why:* The failure mode isn't syntax or style — those are cheap to catch. It's code that looks right, passes tests, and is wrong for your system.
