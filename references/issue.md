# The evolving issue

**Shared problem, functioning slices, connected memory.**

The issue is the current shared account of a change, whether it lives in GitHub Issues, Linear, or a local Markdown file. Start with what is known; add and edit as evidence grows. Use the project's conventions where they exist. A small fix can use one issue with little ceremony.

## Issue write-back contract

For work tracked in GitHub, the GitHub issue is the canonical, evolving account of the work. The same contract applies to the project's shared issue in Linear or local Markdown. Every skill must write its latest understanding back to that issue before it finishes, even when its work began in conversation, code, a prototype, or local notes.

Before completing a skill, re-read the current issue and reconcile all material learning from conversation, inspection, prototyping, testing, implementation, and review into its current narrative. Replace or update stale assumptions instead of appending contradictory history. Preserve meaningful decisions, their reasons, and deferred questions; link to detailed artifacts without copying working notes wholesale. Check that the issue now gives the next skill enough context to continue without reconstructing the work elsewhere. No material understanding should remain only in a conversation or working artifact.

Establish the project's issue destination before a remote update. If no shared issue exists yet, use a local Markdown issue while preparing one; for GitHub-tracked work, local notes alone do not satisfy the write-back once a GitHub issue exists. If a required write-back is blocked, preserve the issue-ready update and report that the skill remains incomplete.

## One issue or linked issues

Use one issue when a change has one coherent functioning outcome. For a larger problem, an optional parent issue can hold overall intent, exploration, and outcome. Link delivery issues for the changes that address it. The parent helps people see the shared problem; it is not a required hierarchy or a substitute for delivery issues. Each delivery issue remains the source of truth for its own decisions, implementation, verification, release, and feedback. Link to the parent without copying its entire narrative.

Each delivery issue should produce the smallest **functioning software** that someone can experience and evaluate. Connect the necessary product and technical parts so the behavior works in the running product. A slice need not complete the broader vision. It should create a real opportunity to learn through user feedback, observed behavior, or a meaningful product demonstration. Prefer slices that can go live independently, release to an appropriate audience when feasible, observe what happens, and use that feedback to shape the next slice. Do not divide issues solely into frontend, backend, or infrastructure work that cannot be experienced or evaluated on its own.

Use these questions as judgment prompts for a proposed delivery issue, not mandatory fields or rigid gates:

1. What can someone actually do or experience when this slice works?
2. Which product and technical parts must be connected for it to function?
3. Who can evaluate it, and how will we observe or gather feedback?
4. Can it go live independently? If not, what dependency remains?
5. What question will this release help answer?

Foundational work sometimes needs its own issue. Explain the capability it enables, how it can be verified, and which functioning slice it supports. Do not present a technical separation as a product learning opportunity when it is not one.

## Small starting issue

```markdown
# [Problem in plain language]

[Who is affected, what happens, and why it matters. State the evidence available now.]

**Desired outcome:** [Observable improvement.]

**Open questions:** [Only questions that could change the next move.]
```

Add a proposed direction if there is one, clearly marked as a proposal. When a solution choice needs evidence, an optional note can say: **Open for exploration:** what choice remains, what needs to be observed, and what would help decide. Write it as natural language, not a required field. Local drafts, maps, and prototype notes can precede any shared issue. Draft in local Markdown for review before consequential shared issue updates.

## As the work gains fidelity

Keep a readable narrative, adding only relevant parts:

- **Current behavior and system:** What the product does and where the important code or dependencies live. Resolve architectural facts without implying a design choice is settled.
- **Exploration:** Meaningful options, prototypes or other evidence, observations, and tradeoffs.
- **Decision:** Chosen direction, reasons, and remaining uncertainty.
- **Result:** What changed in the experience and implementation.
- **Verification and status:** What was checked; distinguish implemented, merged, deployed, and verified live.
- **Release and learning:** Who can use or evaluate the slice, what was actually observed, what is inferred, and what remains to learn.
- **Links and signals:** Parent if one exists, code, PR, diagrams, durable documentation, release, and what to watch next.

Distinguish **planned feedback**, **observed feedback**, and **inferences**. Record observations, assumptions, proposals, and decisions distinctly when the difference affects the next move. Record learning and decisions when they happen, then edit the same delivery issue for clarity. Link to detailed local or durable artifacts rather than copying transcripts, scratch files, or exhaustive code inventories. If local Markdown is the team's issue system, the local issue file itself serves as this account. A PR normally advances one delivery issue and links to it for the full lifecycle.

## Shipped-state check

A newcomer should understand why the change mattered and whom it affected; what was learned about the product and existing system; which meaningful options were tried and what happened; what was decided and why; what changed; how it was verified and whether it is live; who could evaluate it and what feedback is available; and where to find code, diagrams, durable documentation, release details, and remaining signals. If a category was irrelevant, do not add an empty section to prove it was considered. Mark the result live only when the software is actually live, and record live verification separately from deployment.
