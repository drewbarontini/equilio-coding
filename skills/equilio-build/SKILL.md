---
name: equilio-build
description: Implement a chosen software direction in the existing codebase; use when a problem and approach are clear enough to build and refine working behavior.
---

# Build

Use the [work-artifact contract](references/work-artifact.md) throughout; keep the owning issue current as understanding changes. Reuse current guidance already in context, but read the latest artifact at the start.

Establish the current problem, system, and direction from the request, work artifact, prototype, and actual code. Earlier skills are optional; enough understanding for a responsible change is required, not certainty. Apply the [Development Principles](references/development-principles.md) throughout.

Judge the change against the [requested scope and sufficient evidence](references/work-artifact.md#judge-scope-and-completion). Respect known time or effort limits while preserving the functioning outcome and required contracts; surface a concrete trade-off when they cannot fit rather than silently dropping necessary work.

Build the smallest coherent functioning delivery slice through every product and technical layer needed for someone to experience and evaluate it. Use the shared problem and exploration evidence to choose the fewest changes; reuse existing behavior and remove unnecessary prototype machinery. Iterate in the running product when feasible so behavior, design, and UX work together. Basic usefulness must not need future follow-ups; build tasks can be staged separately within the slice. Read the [delivery-slicing guidance](references/delivery-slices.md) when broader work needs decomposition. Avoid unrelated cleanup and speculative abstractions.

Follow local conventions, refine prototype shortcuts, and improve names and structure before compensating with comments. Preserve non-obvious reasoning, constraints, and invariants near the code; correct stale comments and avoid routine narration.

Inspect existing coverage and run appropriate checks. Add or update tests when they increase confidence in behavior or contracts, using the smallest useful evidence and avoiding redundancy or brittle implementation coupling. Reconcile failures with intended behavior rather than blindly changing code or tests. Verify integrated behavior when feasible; record the limits of manual or other evidence honestly.

Turn **Solution + Impact** from prospective understanding into implemented behavior. Preserve consequential **Decisions** and verification or remaining uncertainty in **Reality**. If implementation disproves the framing or direction, rewrite the issue before continuing on the revised basis and surface consequential changes to the user; return to Frame, Map, or Explore when the new evidence requires it. Describe resulting behavior and system meaning rather than narrating the patch; implementation alone does not establish merge, deployment, or live outcomes.
