# AI Usage Policy

> **Template.** Replace every `TODO(org)`, delete the *Why* lines before publishing (or keep them — they help people follow the rules), and have your legal/security teams review it. This is a starting point, not legal advice.

**Applies to:** all engineers, contractors and anyone using AI coding tools on company systems.
**Owner:** TODO(org) — e.g. VP Engineering · **Last reviewed:** TODO(org) · **Review cadence:** every 6 months

## 1. Purpose

Use AI to build better software faster, without leaking data, shipping code nobody understands, or creating legal exposure. This policy is deliberately short so people read it.

## 2. Approved tools

- Approved: TODO(org) — e.g. Claude Code (company account), GitHub Copilot (Business).
- Use **company-managed accounts**, not personal ones, for any work involving company code or data.
- Want a new tool? Request it from TODO(org) — security reviews data handling and retention first.

*Why:* The tool's terms decide where your code and data go. Personal accounts often allow training on inputs and have no audit trail.

## 3. What you may share with AI tools

| Data class | Examples | Allowed in approved tools? |
| --- | --- | --- |
| **Public** | Open-source code, published docs | Yes |
| **Internal** | Company source code, internal docs, architecture | Yes — approved tools only |
| **Confidential** | Unreleased product plans, security configs, customer-identifiable metadata | Only if TODO(org) has approved the tool for it |
| **Restricted** | Credentials and keys, customer personal data, health/payment data, regulated data | **Never** |

*Why:* A mistake with a secret or personal data is expensive and hard to undo. Making "never" absolute for the top tier means nobody has to make a judgement call under pressure.

## 4. You own what you ship

- You are fully responsible for any code you commit, whether you wrote it or an AI did.
- If you cannot explain a change in your PR, it does not go in the PR.
- AI output is a draft. Read it, run it, and test it.

*Why:* Reviewers can't tell good AI output from plausible-looking wrong output. The only reliable defence is an author who understands the change.

## 5. Disclose AI assistance

Mark AI-assisted PRs using the PR template ([`03-ai-pr-review-checklist.md`](03-ai-pr-review-checklist.md)). Disclosure tells reviewers where to look harder; it is never a penalty.

*Why:* If people fear disclosure, they hide it, and reviewers lose the signal.

## 6. Security and IP

- Never put secrets in prompts, files or commands. Use environment variables and the secrets manager.
- Do not paste proprietary code into unapproved tools or public chat services.
- Check generated code that resembles third-party code for license compatibility. When unsure, rewrite it or ask TODO(org).
- Review new dependencies the AI suggests: does the package exist, is it maintained, is the license acceptable? (AI sometimes invents package names.)

*Why:* Hallucinated dependencies are a real supply-chain attack route; secrets in prompts leave your control.

## 7. Autonomy limits

- Don't run AI tools with permission checks disabled in shared repositories.
- AI may not push to protected branches, deploy, run production migrations, or change access controls without a human approving that specific action.
- Follow the project's `CLAUDE.md` and `.claude/settings.json` ([`02-claude-md-standards.md`](02-claude-md-standards.md)).

*Why:* The cheapest safety control is requiring human approval for actions that are hard to reverse.

## 8. Incidents

If AI exposed data, introduced a vulnerability, or did something destructive: stop, tell TODO(org) within TODO(org) hours, preserve the session log, and don't try to quietly fix it. Blameless review follows.

*Why:* Fast reporting matters far more than who made the mistake.

## 9. Exceptions and questions

Request an exception from TODO(org) in writing; exceptions are time-limited and recorded. Questions are welcome — ask before you guess.
