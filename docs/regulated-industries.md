# Heavier alternatives for regulated industries

The three core documents are deliberately light so teams read them. If you work under HIPAA, PCI DSS, SOC 2, GDPR, financial-services supervision, or similar, you will likely need more. This page lists what to **add or tighten**, document by document. It is a checklist for your compliance and legal teams, not legal advice, and following it does not make you compliant.

## AI Usage Policy — add or tighten

| Light version says | Regulated version adds |
| --- | --- |
| "Use approved tools" | A maintained **approved-tool register**: owner, purpose, data classes allowed, contract/BAA/DPA status, data residency, retention and training terms, last vendor-risk review date |
| "Use company-managed accounts" | SSO-only access, enterprise plan with zero-retention / no-training terms confirmed in the contract, and logging enabled |
| Data classes table | Map classes to your regulatory categories (e.g. PHI, cardholder data, personal data). Treat the **Restricted** tier as hard-blocked *technically* (network egress rules, DLP), not only by policy |
| "You own what you ship" | Named accountable owner per AI-assisted change; segregation of duties — the author of an AI-assisted change cannot be its sole approver |
| "Report incidents" | Defined regulatory notification clocks, a named incident commander, and a path to legal/privacy; retain the session logs as evidence |
| Review every 6 months | Review on every material tool, model, or vendor change; record the review |
| *(none)* | **Training** requirement before access; periodic attestation; defined consequences |
| *(none)* | **Impact assessment** (privacy/DPIA or equivalent) for any AI feature that touches personal data or affects individuals |

## CLAUDE.md Standards — add or tighten

- Deploy `.claude/settings.json` and hooks through **managed settings** so engineers cannot override them. See [`claude-code-security`](https://github.com/ivandir/claude-code-security).
- Put `CLAUDE.md`, `.claude/` and `AGENTS.md` under **CODEOWNERS** requiring security-team approval for changes.
- Require the *data sensitivity* line to use your regulatory categories and to drive which permission preset applies.
- Forbid `--dangerously-skip-permissions` and set it as disabled at the managed level.
- Run Claude Code in a **sandboxed environment** with no production credentials and restricted egress.

## PR Review Checklist — add or tighten

- Two-person review for AI-assisted changes touching regulated data, authentication, authorization, payments, or audit logging.
- Make the "AI assistance" PR section a **required** field enforced by a CI check.
- Retain review evidence (who reviewed, what was checked, outcome) for your required retention period.
- Add the [security review additions](security-review-additions.md) as a mandatory gate for any feature that uses AI at runtime.
- Run secret scanning and dependency/license checks as blocking CI jobs, not advisory ones.

## Audit and evidence

- Capture tool-call audit logs off-host to write-once storage ([`claude-code-security`](https://github.com/ivandir/claude-code-security) provides the hooks and format).
- Keep an inventory of AI systems and the models/versions in use, and when they changed.
- Decide retention by regime — confirm with counsel; don't copy numbers from a blog post.

## Questions to take to counsel

1. Does our contract with the AI vendor cover the data classes engineers will actually send?
2. Do any of our regulatory regimes treat AI-assisted code as a change requiring additional approval?
3. If we operate in the EU, do any of our AI features fall under the EU AI Act's risk categories?
4. What are our notification obligations if AI tooling exposes regulated data?
