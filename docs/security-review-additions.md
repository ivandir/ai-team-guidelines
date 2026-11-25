# Security Review Additions for AI-Assisted Features

> **Optional add-on.** For features that *use* AI at runtime (calling an LLM, running agents, RAG) — not for code that was merely *written* with AI help (that's covered by the PR checklist). Add these questions to your existing security review; they don't replace it.

## 1. Data flow

- [ ] What data goes into the model (prompts, retrieved documents, tool results)? Classified using the policy's data classes?
- [ ] Is any Restricted data sent to the model provider? (If yes: is that approved, contractual, and minimized?)
- [ ] Where are prompts, responses and logs stored, for how long, and who can read them?
- [ ] Does the provider retain or train on our data? Is that setting confirmed and documented?

## 2. Prompt injection and untrusted input

- [ ] Can untrusted content (user input, web pages, emails, tickets, documents, third-party repos) reach the model's context?
- [ ] If so, what is the **worst thing the model can do** with the tools it has? Design for that outcome, not for "the model will behave".
- [ ] Is untrusted content clearly separated from instructions? (Helpful, but never sufficient on its own.)

## 3. Tools and autonomy

- [ ] Are the model's tools least-privilege (read-only where possible, scoped credentials, no ambient admin)?
- [ ] Which actions are irreversible or high-impact? Do they require **human approval** of that specific action?
- [ ] Are there rate limits and cost caps to bound a runaway loop?

## 4. Output handling

- [ ] Is model output treated as **untrusted input** by everything downstream (SQL, shell, HTML, file paths, other services)?
- [ ] Is output validated against a schema before use?
- [ ] Can the model leak data it was given (other users' data, system prompt, secrets in context) to the wrong audience?

## 5. Reliability and misuse

- [ ] What happens when the model is wrong, unavailable, or slow? Is there a safe fallback?
- [ ] For decisions affecting people (eligibility, pricing, moderation): is there human review and a way to contest?
- [ ] Abuse cases considered: cost abuse, jailbreaks, scraping via the feature?

## 6. Evidence

- [ ] Security-relevant AI events are logged (tool calls, denials, approvals) without logging sensitive content.
- [ ] A named owner and an incident path exist for the feature.

*Why this list exists:* The model is a component that can be steered by its inputs. Classic reviews miss that "input" now includes any text the model reads and "authorization" now includes what the model is allowed to do on someone's behalf.
