---
name: equilio-explain
description: Explain the meaningful system changes a human should understand to maintain software coherence. Use this Supporting Skill for maintainer understanding and mental-model change in a branch, PR, issue and associated changes, completed work, or unfamiliar implementation, including requests like "Explain what changed", "What should I understand about this implementation?", "Teach me what changed in this PR", "What changed in the system model?", "What do I need to know to maintain this?", or "Explain the important changes in this branch". Do not use for ordinary code summaries or diff recaps.
---

# Equilio Explain

Use Explain as an independently invokable **Supporting Skill** for human comprehension, whether the code came from a human, AI, or the Core Skills. Ask: **What should a maintainer understand differently because this changed?**

## Establish the model change

When an associated work artifact is available, read it and the [work-artifact contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#reconcile-current-understanding) at the start; keep the owning issue current when explanation reveals missing durable understanding.

Read the supplied branch, PR, work artifact, implementation, and relevant repository context. Establish a comparison baseline from available history; inspect actual code, callers, and tests rather than inferring behavior from the diff alone. With partial evidence, name what could not be checked. For unfamiliar code without a before-state, teach the current model and its comparison limits instead of inventing an old model.

Apply the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md) proportionately. Distinguish verified behavior, inferred intent, and documented reasoning; do not manufacture rationale or validation.

Look selectively for concepts and relationships that change future reasoning: responsibilities moving across boundaries, new invariants, changed data or user flows, removed assumptions, durable decisions, meaningful coupling, or extension points. Explain what must now be understood and why it matters. These are inspection lenses, not required output sections. Omit mechanical refactors, file or function inventories, routine test additions, and obvious code narration unless they alter the system model.

## Teach the updated model

Lead with the conceptual shift, then explain relationships, cause and effect, and responsibility boundaries. Include supported reasoning, constraints a maintainer must preserve, and a few precise references when useful. Use technical terms only with enough context to make them understandable. Match depth to the change and omit empty sections; say briefly when no material mental-model change exists.

Use the PR and diff as evidence without repeating them. Keep the PR under the [PR guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/pull-request.md). Integrate asks whether the change is coherent; Explain teaches what a maintainer should understand. Surface contradictory findings with evidence and recommend the relevant Core Skill rather than turning explanation into implementation or review.

## Reconcile durable understanding

**Explain teaches the model. Impact preserves the model change.**

If explanation uncovers missing or contradictory durable understanding, reconcile it under the work-artifact contract as that understanding changes:

- Put conceptual or mental-model changes generally in **Impact**.
- Put consequential reasoning in **Decisions**.
- Put unresolved invariants, trade-offs, limits, or observation needs in **Reality**.

Every section remains available if the insight corrects it. Preserve existing records and relationships, remove stale claims, and keep the information budget. Synthesize the durable insight; do not copy the teaching response or append a transcript.

Leave the artifact unchanged when no durable understanding is missing. Without an associated artifact, deliver the teaching and identify worthwhile insight without creating a competing permanent artifact by default. If a required update is blocked, preserve a destination-ready synthesis and report the limitation. Recommend further action only when the explanation reveals a meaningful need.
