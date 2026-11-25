# CLAUDE.md Standards

> **Template.** Standards for how your organization writes and maintains `CLAUDE.md` files (and `AGENTS.md`, if you use it). For a ready-to-copy file, use the annotated template in [`claude-code-org-setup`](https://github.com/ivandir/claude-code-org-setup).

**Owner:** TODO(org) · **Applies to:** every repository where AI coding tools are used

## 1. Every AI-enabled repo has a project `CLAUDE.md`

Committed at the repo root, reviewed like code. *Why:* Without it, output quality depends on whoever happens to be prompting.

## 2. Required content

A project `CLAUDE.md` must contain:

1. **What the service does** and where it runs — one paragraph.
2. **Data sensitivity** — what classes of data it touches (see the policy's data classes).
3. **Commands** — build, test, lint, run. Copy-pasteable.
4. **Conventions that differ from defaults** — only things the model gets wrong without instruction.
5. **Do-not-do-without-approval list** — migrations, public API contracts, deletions, CI/CD, dependencies.

*Why:* These five items remove most wrong guesses. The sensitivity line changes the security decisions the model makes.

## 3. Keep it small

- Target **under 150 lines**. Move subsystem rules into a local `CLAUDE.md` in that directory.
- Don't paste the style guide. If a linter enforces it, leave it out.
- No secrets, internal hostnames, customer names, or credentials. Ever.

*Why:* The file is loaded into every session. Length costs attention and money, and a bloated file gets ignored — by the model and by humans.

## 4. The three levels

| Level | Location | Owned by |
| --- | --- | --- |
| Global | `~/.claude/CLAUDE.md` | The individual. **Never distributed as a team standard.** |
| Project | `CLAUDE.md` in the repo | The team, via PR |
| Local | `<subdir>/CLAUDE.md` | The subsystem owners |

*Why:* Pushing one global file to everyone overrides legitimate personal differences and breeds resistance. Local files must not be used to dodge project rules.

## 5. Permissions match the file

The do-not-do list in `CLAUDE.md` is advisory; `.claude/settings.json` **enforces** it. When one changes, change the other. Choose a preset per [`claude-code-org-setup`](https://github.com/ivandir/claude-code-org-setup) and disable bypass mode.

*Why:* A rule that is only written down is a suggestion. A rule that is enforced is a control.

## 6. Ownership and review

- Each `CLAUDE.md` has a named owner (the team champion). No owner, no file.
- Changes need a PR and one reviewer — a one-line edit can change every AI session in the repo.
- **Review quarterly.** Delete rules the model now follows by default; add the mistakes you keep seeing in code review.

*Why:* Files rot. Review keeps them short and keeps them true.

## 7. Don't copy blindly

A `CLAUDE.md` copied from another repo is wrong in ways that are hard to see. Start from the template; edit every section.
