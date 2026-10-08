---
name: equilio-build
description: Implement a chosen software direction in the existing codebase; use when a problem and approach are clear enough to build and refine working behavior.
---

# Build

Read the [work-artifact contract](references/work-artifact.md#reconcile-current-understanding) at the start; keep the owning issue current as material understanding changes, before acting on it and before handoff.

Establish the current problem, system, and direction from the request, work artifact, prototype, and actual code. Earlier skills are optional; enough understanding for a responsible change is required, not certainty. Apply the [Development Principles](references/development-principles.md) throughout.

Build the smallest coherent functioning delivery slice through every product and technical layer needed for someone to experience and evaluate it. Use the shared problem and evidence from exploration to choose the fewest changes that solve the gap; reuse existing behavior and remove unnecessary prototype machinery rather than carrying every explored option forward. Iterate in the running product when feasible so behavior, design, and UX work together. Prefer independent release where useful. Separate genuinely independent follow-ups; include work this slice needs to function. Avoid unrelated cleanup and speculative abstractions.

Follow local conventions, refine prototype shortcuts, and improve names and structure before compensating with comments. Preserve non-obvious reasoning, constraints, and invariants near the code; correct stale comments and avoid routine narration.

Inspect existing coverage and run appropriate checks. Add or update tests when they increase confidence in behavior or contracts, using the smallest useful evidence and avoiding redundancy or brittle implementation coupling. Reconcile failures with intended behavior rather than blindly changing code or tests. Verify integrated behavior when feasible; record the limits of manual or other evidence honestly.

Turn **Solution + Impact** from prospective understanding into implemented behavior. Preserve consequential **Decisions** and verification or remaining uncertainty in **Reality**. If implementation disproves the framing or direction, rewrite the issue before continuing on the revised basis and surface consequential changes to the user; return to Frame, Map, or Explore when the new evidence requires it. Describe resulting behavior and system meaning rather than narrating the patch; implementation alone does not establish merge, deployment, or live outcomes.

Before finishing, reconcile and re-read the same artifact under the [work-artifact contract](references/work-artifact.md#reconcile-current-understanding); all five coordinates are available for revision. Apply the [next-operation guidance](references/work-artifact.md#choose-the-next-useful-operation) and finish with **Recommended next:** `<skill or action>` · **Why:** `<reason>`. Integrate when review and handoff remain; return to earlier concerns for material gaps rather than silently diverging.
