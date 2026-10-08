---
name: equilio-loop
description: Adaptively orchestrate Equilio Coding from a goal or work artifact to coherent, verified, review-ready work. Use this Supporting Skill to choose and coordinate the next useful Core Skill based on current understanding.
---

# Equilio Loop

Use Loop as a **Supporting Skill** for adaptive orchestration. Preserve **Frame → Map → Explore → Build → Integrate** as the progression of concerns, not a required pipeline. Apply the [Development Principles](references/development-principles.md). Install Loop with all five Core Skills; invoke the selected skill or read and follow its current instructions: [Frame](../equilio-frame/SKILL.md), [Map](../equilio-map/SKILL.md), [Explore](../equilio-explore/SKILL.md), [Build](../equilio-build/SKILL.md), [Integrate](../equilio-integrate/SKILL.md). Keep Loop and its dependencies from the same source revision. Report a missing dependency rather than substituting remembered instructions or fetching an unrelated latest version.

## Establish current understanding

Use the [work-artifact contract](references/work-artifact.md) throughout, reusing current guidance already in context. Read the latest owning artifact at the start; it holds discoveries within a skill as well as between skills.

Inspect the goal, branch, project conventions, and existing work before creating anything. Reuse the artifact that owns the goal, or prepare a local Markdown artifact while establishing the project's shared destination. For broader work, use the [delivery-slicing guidance](references/delivery-slices.md#shape-delivery-slices) to select a useful outcome linked to project-level understanding. Sequence by value and release dependencies, not merely by build-task order; revisit boundaries when mapping or prototype evidence changes them. Avoid duplicates and speculative delivery breakdowns.

Assess the five coordinates and relevant evidence under the shared [routing guidance](references/work-artifact.md#choose-the-next-useful-operation). Treat them as judgment lenses, not gates or scores; routing must work without hidden conversation state.

## Choose, run, and reassess

**Assess understanding → choose useful skill → run it → reconcile work artifact → reassess.**

Use the [next-operation guidance](references/work-artifact.md#choose-the-next-useful-operation). Honor an explicitly requested skill first, skip satisfied concerns, and revisit only when new evidence materially requires it. Give the selected skill the goal, shared artifact, and relevant evidence; let its current instructions determine method and depth.

For a handoff to another agent or authorized multi-agent work, follow the [agent-continuation guidance](references/agent-handoffs.md). Keep assignments bounded and artifact write-back owned by one active writer; inspect returned evidence and reconcile contradictions before routing from it. Parallel assignments do not redefine delivery boundaries; readiness depends on verifying the functioning slice.

Each skill owns reconciliation as material understanding changes; in delegated work, the coordinating agent verifies that the shared writer completes it. Reconcile additional orchestration learning, then independently re-read the artifact at every transition and reassess against actual evidence. Preserve shared problem understanding, working prototypes, and opportunities to simplify; a plausible proposal or passing tests may leave these unresolved. If repetition produces no learning, identify the evidence or judgment needed rather than cycling mechanically.

Continue through reasonable choices supported by evidence and conventions. Request human judgment when a consequential unresolved choice materially changes intent, scope, security or privacy expectations, compatibility, architecture, external commitments, or irreversible behavior, or when evidence gives no sound basis for choosing. Continue independent work while judgment is pending; avoid routine approval gates.

Use the [scope and completion guidance](references/work-artifact.md#judge-scope-and-completion) to distinguish required work from optional improvements and judge when another operation would add value. Stop by default at review-ready: coherent implementation, appropriate verification, a reconciled artifact, and a coherent branch and working tree. Prepare a PR synopsis or draft PR when the normal workflow and request support it, using the [PR guidance](references/pull-request.md): **Summary → Changes → Callouts**; count words and enforce its section limits before creating or updating the PR. Continue further slices needed for the authorized goal without treating possible improvements as automatic follow-ups. Merge, release, deployment, and live observation remain separate and require explicit authorization where applicable.

## Support human understanding

Use optional [Explain](../equilio-explain/SKILL.md) when coherent work meaningfully changes the maintainer's model; skip trivial changes. Re-read the artifact after any durable insight is reconciled. Do not copy its teaching response. If explanation exposes a material contradiction, return to the appropriate Core Skill before claiming convergence; Integrate retains coherence review.

Finish under the shared reconciliation and routing contract, usually with human review, stop / complete, or a specific judgment needed.
