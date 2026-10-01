---
name: equilio-loop
description: Adaptively orchestrate Equilio Coding from a goal or work artifact to coherent, verified, review-ready work. Use this Supporting Skill to choose and coordinate the next useful Core Skill based on current understanding.
---

# Equilio Loop

Use Loop as a **Supporting Skill** for adaptive orchestration. Preserve **Frame → Map → Explore → Build → Integrate** as the progression of concerns, not a required pipeline. Apply the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md). Install Loop with all five Core Skills; invoke the selected skill or read and follow its current instructions: [Frame](../equilio-frame/SKILL.md), [Map](../equilio-map/SKILL.md), [Explore](../equilio-explore/SKILL.md), [Build](../equilio-build/SKILL.md), [Integrate](../equilio-integrate/SKILL.md). If a dependency is unavailable, obtain its current repository version; report an inaccessible dependency rather than substituting remembered instructions.

## Establish current understanding

Inspect the goal, branch, project conventions, and existing work before creating anything. Reuse the artifact that owns the goal, or prepare a local Markdown artifact while establishing the project's shared destination. For broader work, select a functioning delivery slice linked to project-level understanding under the [issues and projects guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#issues-and-projects). Avoid duplicates and speculative delivery breakdowns.

Use **Problem → Solution → Decisions → Impact → Reality** as the orientation surface:

- **Problem:** Is the gap understood enough?
- **Solution:** Is there a supported way forward?
- **Decisions:** Are consequential choices sufficiently resolved?
- **Impact:** Is the relevant system understood enough to proceed?
- **Reality:** What uncertainty or evidence should determine the next move?

Treat these as judgment lenses, never gates, scores, maturity levels, or required checklists. Read the artifact and relevant evidence so a fresh human or agent can route without hidden conversation state.

## Choose, run, and reassess

**Assess understanding → choose useful skill → run it → reconcile work artifact → reassess.**

Use the [next-operation guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#choose-the-next-useful-operation). Honor an explicitly requested skill first, skip satisfied concerns, and revisit only when new evidence materially requires it. Give the selected skill the goal, shared artifact, and relevant evidence; let its current instructions determine method and depth.

Each skill owns reconciliation under the [work-artifact contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#reconcile-current-understanding). Reconcile additional orchestration learning, then independently re-read the artifact at every transition and reassess the recommendation against actual evidence. Keep material reasons there instead of producing a routing log. If repetition produces no learning, identify the evidence or judgment needed rather than cycling mechanically.

Continue through reasonable choices supported by evidence and conventions. Request human judgment when a consequential unresolved choice materially changes intent, scope, security or privacy expectations, compatibility, architecture, external commitments, or irreversible behavior, or when evidence gives no sound basis for choosing. Continue independent work while judgment is pending; avoid routine approval gates.

Stop by default at review-ready: coherent implementation, appropriate verification, a reconciled artifact, and a coherent branch and working tree. Prepare a PR synopsis or draft PR when the normal workflow and request support it, using the [PR guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/pull-request.md): **Summary → Changes → Callouts**. Check whether more functioning slices are needed for the goal. Merge, release, deployment, and live observation remain separate and require explicit authorization where applicable.

## Support human understanding

Use optional [Explain](../equilio-explain/SKILL.md) when coherent work meaningfully changes the maintainer's model; skip trivial changes. Re-read the artifact after any durable insight is reconciled. Do not copy its teaching response. If explanation exposes a material contradiction, return to the appropriate Core Skill before claiming convergence; Integrate retains coherence review.

Before finishing, reconcile remaining material understanding and re-read the artifact. Give **Recommended next:** `<skill or action>` · **Why:** `<brief reason>`, usually human review, stop / complete, or a specific judgment needed.
