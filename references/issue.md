# The issue as current understanding

**Shared problem, functioning slices, connected memory.**

The shared issue is the **canonical current understanding** of a change, whether it lives in GitHub Issues, Linear, or a local Markdown file. It should always be the best current summary of understanding, readable and useful to both humans and AI. At any point in the workflow, a human or AI should be able to read the issue and understand the current state of the work without needing the prior conversation. Start with what is known and refine it as evidence grows. Use the project's conventions where they exist; a small fix can use one issue with little ceremony.

## Issue write-back contract

For work tracked in GitHub, the GitHub issue is the canonical account of the work. The same contract applies to the project's shared issue in Linear or local Markdown. Each Core Skill and Loop must re-read and rewrite the issue body (or local issue file) to reflect its latest understanding before it finishes, even when its work began in conversation, code, a prototype, or local notes. A new comment or stage note alone does not satisfy this contract.

Explain is a Supporting Skill whose response is a teaching artifact. Read an associated issue when available and reconcile only durable new understanding discovered during explanation into its current narrative. Remove stale or contradictory understanding as needed; do not copy the entire Explain output. If no durable insight is missing, leave the issue unchanged. Standalone Explain does not require creating an issue or another permanent artifact. **Explain output = teaching; issue = durable understanding.**

Write-back means **synthesis, not append-only logging**. When writing back, reconcile all material learning from conversation, inspection, prototyping, testing, implementation, review, and explanation into the issue's current narrative. Rewrite, consolidate, simplify, reorder, and replace stale assumptions. Remove superseded or disproven claims, duplicates, and incidental detail; promote important discoveries. Preserve meaningful decisions, their reasons, and unresolved or intentionally deferred questions without retaining a chronological record of how they arose. Each update should leave the issue more accurate, more complete, and easier to understand than it found it.

The target is **completeness of understanding, not completeness of implementation detail**. No material understanding should remain only in conversation, temporary agent context, scratch notes, or local investigation artifacts. Link to durable detail where useful; do not copy working notes wholesale. Check that a fresh human or AI can resume from the issue alone. If the conversation and working notes disappeared, the issue should still explain what matters now.

Establish the project's issue destination before a remote update. If no shared issue exists yet, use a local Markdown issue while preparing one; for GitHub-tracked work, local notes alone do not satisfy the write-back once a GitHub issue exists. If a required write-back is blocked, preserve the issue-ready update and report that the skill remains incomplete.

## Choose the next useful operation

**Follow the understanding, not the sequence.** **Frame → Map → Explore → Build → Integrate** is the canonical progression of concerns, not a mandatory pipeline. Work may enter at any appropriate skill, skip work whose purpose is already satisfied, or revisit an earlier concern when material evidence requires it. Do not repeat work merely because a skill exists or has not run.

Each Core Skill performs its job, reconciles the shared issue, then re-reads the resulting issue before recommending what is useful next. Base that judgment primarily on the reconciled issue, relevant repository evidence, current implementation, verification results, and the Development Principles. The issue is both shared memory and the state from which the next operation can be selected: a future human or AI should reach approximately the same recommendation without hidden chat context. Put material reasons, unresolved questions, and evidence in its current narrative, without adding a routing report or required fields.

Use these as judgment guides, not gates:

| Next operation | When it is useful |
| --- | --- |
| `equilio-frame` | The actual problem, desired outcome, scope, boundaries, intent, or important constraints are unclear; a proposed solution lacks enough problem understanding. Skip it when the issue already expresses a strong problem, outcome, evidence, and boundaries. |
| `equilio-map` | The problem is understood, but relevant behavior, code paths, data flow, state, boundaries, dependencies, or conventions remain assumptions that affect implementation decisions. Do not repeat mapping already sufficient for this change. |
| `equilio-explore` | Meaningful approaches remain, interaction or behavior is uncertain, or a cheap test or prototype could resolve an important assumption and change the decision. **Do not explore merely because Explore exists.** Skip it when evidence and conventions sufficiently support one direction. |
| `equilio-build` | The problem, relevant system, and implementation direction are understood enough for a responsible, coherent change; more framing, mapping, or prototyping is unlikely to materially improve the decision. Build requires sufficient understanding, not certainty. |
| `equilio-integrate` | Functioning implementation exists and intended behavior has been built; coherence review, verification, issue reconciliation, and preparation for review are the primary remaining needs. Return to an earlier skill if review reveals material problems. |
| `equilio-explain` | The implementation is coherent and review-ready, and the change meaningfully alters the maintainer's mental model. This Supporting Skill is optional; skip trivial changes where explanation adds no useful understanding. |
| Human review or stop / complete | Implementation is coherent, verification is sufficient, the issue reflects reality, and no further Core Skill is needed. Recommend human judgment sooner when a consequential unresolved choice needs it; state that choice without claiming review readiness. |

Movement may go backward: Map can expose the wrong problem and recommend Frame; Explore can discover an unknown system constraint and recommend Map; Build can invalidate a decision and recommend Explore; Integrate can discover a missed outcome and recommend whichever earlier skill addresses the gap. Re-enter only when current understanding materially requires it, and converge through evidence rather than creating loops for their own sake.

Finish with one useful skill or action and a brief reason, for example:

**Recommended next:** `equilio-build`

**Why:** The problem and relevant system behavior are understood, and prototyping is unlikely to change the supported direction.

Keep this recommendation concise; do not introduce completion scores, maturity levels, routing percentages, mandatory checklists, formal gates, or a requirement to pass every skill. If the user explicitly invokes a particular skill, perform its job and reconcile the issue before recommending continuation; routing must not override deliberate use. Recommending a skill does not require it to be installed or invoke it automatically. Loop owns orchestration; individual Core Skills own their specific judgment.

## What the issue should explain

Use clear headings, concise prose, meaningful bullets, explicit decisions, and links to durable artifacts. Include only what is relevant at the current stage:

- **Problem and outcome:** What problem are we solving, who or what is affected, why it matters, and what outcome are we trying to create?
- **Evidence and learning:** What do we know, what evidence matters, what have we learned, and which claims remain assumptions?
- **Constraints and decisions:** What constraints matter, what was decided and why, and which meaningful alternatives were considered or rejected?
- **System and result:** What behavior exists now, what has been implemented, and what high-level system understanding matters?
- **Verification and state:** What has been checked, what risks or important callouts remain, what is unresolved or intentionally deferred, and is the work proposed, implemented, merged, deployed, or verified live?

Keep facts, assumptions, decisions, verification, and open questions distinct when that distinction changes the next move. The issue represents **current truth**, not the history of discovering it. It is not a chronological work log, transcript, scratchpad, dump of code details, or duplicate PR description. Remove stale claims and repeated observations rather than leaving them phrased as current truth.

## Working Notes → Issue → PR

- **Working notes** hold exhaustive exploration and temporary detail: raw investigation, detailed code maps, debugging notes, discarded hypotheses, prototype mechanics, and scratch analysis.
- **Issue** holds the best current synthesis of understanding. It is canonical memory for the work.
- **Pull request** gives a quick review synopsis: the outcome, meaningful reviewer callouts, and the issue link.
- **Code** explains the implementation.

Transform information between these layers instead of copying it blindly. Technical detail belongs in the issue when it materially affects understanding, a decision, a constraint, a risk, system behavior, or future work. Let the code explain how the solution works; do not move incidental implementation detail into PR prose.

Read the canonical [PR guidance](pull-request.md) when preparing a description. The issue explains the understanding; the code explains the implementation; the PR explains the change. Keep deeper framing, evidence, decisions, and verification in the reconciled issue before PR creation.

Explain uses the issue, PR, and code as evidence for human comprehension, without duplicating them: **PR: What changed and what deserves review attention? Explain: What should I understand differently because it changed?** Keep the issue canonical and the PR a quick review synopsis.

## One issue or linked issues

Use one issue when a change has one coherent functioning outcome. For a larger problem, an optional parent issue can hold overall intent, exploration, and outcome. Link delivery issues for the changes that address it. The parent helps people see the shared problem; it is not a required hierarchy or a substitute for delivery issues. Each delivery issue remains the source of truth for its own decisions, implemented outcome, verification, release, and feedback. Link to the parent without copying its entire narrative.

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

Refine the existing narrative, adding only relevant parts:

- **Current behavior and system:** What the product does and which system relationships matter. Resolve architectural facts without implying a design choice is settled.
- **Exploration:** Meaningful alternatives, evidence, learning, and tradeoffs that still explain the direction.
- **Decision:** Chosen direction, reasons, and remaining uncertainty.
- **Result:** What behavior now exists and which implementation outcomes matter beyond review of the patch.
- **Verification and status:** What was checked; distinguish implemented, merged, deployed, and verified live.
- **Release and learning:** Who can use or evaluate the slice, what was actually observed, what is inferred, and what remains to learn.
- **Links and signals:** Parent if one exists, code, PR, diagrams, durable documentation, release, and what to watch next.

Distinguish **planned feedback**, **observed feedback**, and **inferences**. Record observations, assumptions, proposals, and decisions distinctly when the difference affects the next move. Edit the same delivery issue for clarity as learning and decisions change; do not append a section for every workflow step. Link to detailed durable artifacts rather than copying transcripts, scratch files, or exhaustive code inventories. If local Markdown is the team's issue system, the local issue file itself serves as this account. A PR normally advances one delivery issue and links to it for current understanding.

## Shipped-state check

A newcomer should understand why the change mattered and whom it affected; what was learned about the product and existing system; which meaningful options shaped the decision; what was decided and why; what behavior now exists; how it was verified and whether it is live; who could evaluate it and what feedback is available; and where to find code, diagrams, durable documentation, release details, and remaining signals. If a category was irrelevant, do not add an empty section to prove it was considered. Mark the result live only when the software is actually live, and record live verification separately from deployment.
