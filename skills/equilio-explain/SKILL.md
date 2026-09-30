---
name: equilio-explain
description: Explain the meaningful system changes a human should understand to maintain software coherence. Use this Supporting Skill for maintainer understanding and mental-model change in a branch, PR, issue and associated changes, completed work, or unfamiliar implementation, including requests like "Explain what changed", "What should I understand about this implementation?", "Teach me what changed in this PR", "What changed in the system model?", "What do I need to know to maintain this?", or "Explain the important changes in this branch". Do not use for ordinary code summaries or diff recaps.
---

# Equilio Explain

Help a human understand what changed in their mental model of the software. Treat Explain as an independently invokable **Supporting Skill**, not a stage in the five Core Skills: **Frame → Map → Explore → Build → Integrate**. Work with AI-generated or human-written code whether or not that workflow produced it.

Ask: **What changed that a maintainer needs to understand to keep the software coherent?** Then ask: **If a human reviewed only the normal diff and PR, what important change in their mental model of the system might they miss?**

## Establish the conceptual change

Read the supplied branch, PR, issue, implementation, and relevant repository context. Establish the comparison baseline from the request and available history; inspect the actual code and relevant callers or tests rather than inferring system behavior from a diff alone. When only a diff or partial context is available, explain what the evidence supports and name what could not be checked. For an unfamiliar implementation without a clear before-state, teach the current model and name the limits of the comparison instead of inventing an old model. Distinguish verified behavior, inferred intent, and documented reasoning; do not manufacture a rationale or imply verification that did not occur.

Read the shared [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md) and apply them proportionately to comprehension. In particular, expose concepts, boundaries, or assumptions the reader must now understand, using evidence before explanation and the smallest useful account.

Look selectively for shifts that affect future reasoning:

- **New concepts:** Domain concepts, state, persistence models, responsibilities, or abstractions that did not exist before; explain what each means in this system.
- **Changed boundaries:** Responsibility moving between components, services, layers, modules, client/server, persistence, or owners; explain who now owns what and why that matters.
- **New invariants:** What must remain true, why the constraint exists, and where it matters for correct behavior.
- **Changed flows:** How important data, state, control, events, or user behavior now move; describe the conceptual path and its consequences.
- **Important decisions:** Design choices with durable consequences that future maintainers need to respect; omit incidental implementation choices.
- **Removed assumptions:** Beliefs that used to be valid and now mislead; explicitly replace the old model with the supported one.
- **Meaningful dependencies or coupling:** Relationships that constrain future changes; explain the consequence rather than listing imports.
- **Extension points:** Where future work should extend the behavior and which boundaries or constraints it must preserve, when useful.

Use these as inspection lenses, not a mandatory output checklist. **Explain the change in the maintainer's model of the system, not the diff.** Exclude variable renames, formatting, obvious helper extraction, simple movement, and mechanical refactors unless they actually change that model. Do not produce a file-by-file walkthrough, function inventory, generated code documentation, generic code review, verbose architecture document, or tutorial on obvious mechanics.

Do not teach routine comment or test mechanics or summarize ordinary test additions. Call out a comment's subtle constraint, an invariant encoded in code and tests, a test representing an important system contract, or a changed behavioral guarantee only when it materially affects the maintainer's mental model.

## Teach the updated model

Produce a concise, human-readable response. Start with concepts before implementation; explain relationships, cause and effect, and responsibility boundaries. Distinguish intentional design from incidental mechanics, and explain necessary technical terms in this system. Include only enough context for someone who did not write the code to reason accurately about future changes.

Use sections only when they help, and omit empty ones:

- **What changed conceptually?** The most important shift from the previous model.
- **What should I understand now?** The updated model to carry forward.
- **Why is it this way?** Durable reasoning supported by evidence, when relevant.
- **What should I be careful about?** Invariants, constraints, coupling, outdated assumptions, or future coherence risks.
- **Where should I look?** A few precise code or system references that anchor the concepts, not an exhaustive file list.

If the change does not materially alter maintainer understanding, say so plainly and briefly. Do not manufacture insights to fill the structure.

Use the PR and diff as evidence without repeating them. **PR: How did the code change? Explain: What should I understand differently because it changed?** Keep the PR as the implementation-review artifact.

Keep [Integrate](../equilio-integrate/SKILL.md) responsible for checking coherence of the current change before review. **Integrate: Is this change coherent? Explain: What should a human understand about the coherent system that now exists?** Call out surprising or contradictory findings and their evidence without claiming the system is coherent merely because it was explained. Leave implementation and review to the appropriate Core Skill; do not turn Explain into another implementation or review stage.

## Reconcile durable understanding

Treat the response as a teaching artifact for the human. **Explain output = teaching. Issue = durable understanding.** Do not create a competing permanent artifact by default or require a new issue for standalone use.

Read an associated issue when available and determine whether explanation uncovered durable understanding missing from, or contradicting, its current account. If so, re-read and reconcile that insight at the conceptual level under the [issue write-back contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#issue-write-back-contract). Preserve the existing issue and relationships, establish the destination before a remote update, and remove stale or contradictory claims while retaining meaningful decisions, reasons, and open questions. Do not copy the entire Explain response or append a teaching transcript. If a needed update is blocked, preserve an issue-ready synthesis and report the limitation.

If no durable new understanding needs reconciliation, leave the issue unchanged. Keep it the canonical current understanding: a human or AI should be able to read it and understand the work's current state without prior conversation. When no associated issue exists, deliver the explanation and identify any durable insight worth retaining without creating a new artifact by default.
