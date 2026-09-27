# The evolving issue

The issue is the current shared account of a change, whether it lives in GitHub Issues, Linear, or a local Markdown file. Start with what is known; add and edit as evidence grows. These headings are prompts, not fields that must be filled before work can begin. Use the project's conventions where they exist.

## Small starting issue

```markdown
# [Problem in plain language]

[Who is affected, what happens, and why it matters. State the evidence available now.]

**Desired outcome:** [Observable improvement.]

**Open questions:** [Only questions that could change the next move.]
```

Add the proposed direction if there is one, clearly marked as a proposal. A small fix may need nothing more. Local drafts, maps, and prototype notes can precede any shared issue.

## As the work gains fidelity

Keep a readable narrative, adding only relevant parts:

- **Current behavior and system:** What the product does and where the important code or dependencies live.
- **Exploration:** Meaningful options, prototypes or other evidence, observations, and tradeoffs.
- **Decision:** Chosen direction, reasons, and remaining uncertainty.
- **Result:** What changed in the experience and implementation.
- **Verification and status:** What was checked; distinguish implemented, merged, deployed, and verified live.
- **Links and signals:** Code, PR, diagrams, durable documentation, release, and what to watch next.

Record observations and decisions when they happen, then edit the issue for clarity. Link to detailed local or durable artifacts rather than copying transcripts, scratch files, or exhaustive code inventories. If local Markdown is the team's issue system, the local issue file itself serves as this account.

## Shipped-state check

A newcomer should understand why the change mattered and whom it affected; what was learned about the product and existing system; which meaningful options were tried and what happened; what was decided and why; what changed; how it was verified and whether it is live; and where to find code, diagrams, durable documentation, release details, and remaining signals. If a category was irrelevant, do not add an empty section to prove it was considered. Mark the result shipped only after live verification.
