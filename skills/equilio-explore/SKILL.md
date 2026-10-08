---
name: equilio-explore
description: Build and test working software prototypes; use when behavior, design, UX, or technical tradeoffs need evidence before choosing a product or implementation direction.
---

# Explore

Read the [work-artifact contract](references/work-artifact.md#reconcile-current-understanding) at the start; keep the owning issue current as material understanding changes, before acting on it and before handoff.

Establish the current problem from the work artifact, local Markdown, prototype, or code. Name uncertainty whose resolution could change the decision. If evidence and conventions already support a direction, reconcile that judgment without manufacturing alternatives or a prototype. Otherwise choose a few meaningfully different options or one focused discriminating test.

Apply the [Development Principles](references/development-principles.md): build lightweight, reversible working prototypes in the actual product when feasible. Run them and exercise the uncertain behavior; for UI work, use the browser to experience the flow, state changes, and relevant failure cases. Writing and running code can expose constraints the proposal missed; reconcile discoveries before choosing the direction. Screenshots and static mockups can supplement a working prototype but cannot establish its behavior.

Make the prototype available for the person to test: provide a working preview or runnable entry point, the short interaction that tests the uncertainty, and material shortcuts or limitations. Invite their observations when experience or preference could determine the choice; leave that choice open when their judgment is needed. Do not claim human testing occurred because the agent exercised the prototype. For work without a UI, provide the equivalent runnable operation and observable result. If a running prototype is impractical, state the constraint and use the closest useful evidence. Keep raw trials in working notes and name shortcuts that need refinement before production.

Choose a direction when evidence supports one; otherwise leave the choice open and identify the next useful evidence. Use observations to refine [delivery slices](references/work-artifact.md#shape-delivery-slices): combine pieces the prototype shows must work together, remove options unnecessary to the outcome, and name dependencies on earlier releases. Preserve uncertainties that affect boundaries without fixing speculative follow-ups.

Primarily strengthen **Solution + Decisions + Reality**. Preserve the supported approach and consequential reasons. Distinguish actual observations from hypotheses, planned tests, or planned feedback; test accounts are not customer feedback. Retain only alternatives whose reasoning still affects judgment.

Before finishing, reconcile and re-read the same artifact under the [work-artifact contract](references/work-artifact.md#reconcile-current-understanding); all five coordinates are available for revision. Apply the [next-operation guidance](references/work-artifact.md#choose-the-next-useful-operation) and finish with **Recommended next:** `<skill or action>` · **Why:** `<reason>`. Build when evidence supports a direction, Map for an unknown system constraint, or Frame for changed intent.
