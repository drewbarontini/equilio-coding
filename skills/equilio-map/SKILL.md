---
name: equilio-map
description: Map existing product behavior and code paths for a software change; use when implementation boundaries, dependencies, or architectural questions are unclear.
---

# Map

Start from the request, work artifact, local Markdown, prototype, or code. Apply the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md): observe relevant product behavior and inspect the actual code before describing it. Trace entry points, state, data flow, interfaces, dependencies, tests, conventions, and affected surfaces only as deeply as the change requires. Do not repeat sufficient investigation.

Keep a local Markdown map as working notes, with precise references for revisiting relevant code and relationships. Separate verified facts from inference and unresolved choices. Trace the product and technical paths a functioning change must connect, including dependencies that affect independent release or evaluation. Technical-layer boundaries alone do not justify splitting delivery issues.

Primarily strengthen **Problem + Impact**. Mapping may correct the gap; Impact can explain the relevant current system model before any change is implemented. Synthesize responsibilities, relationships, boundaries, and constraints that affect judgment. Keep detailed code maps in working notes, linking durable detail only when needed. Do not copy file or function inventories into the shared artifact or imply architectural facts settle a product decision.

Before finishing, reconcile and re-read the same artifact under the [work-artifact contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#reconcile-current-understanding); all five coordinates are available for revision. Apply the [next-operation guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#choose-the-next-useful-operation) and finish with **Recommended next:** `<skill or action>` · **Why:** `<reason>`. Build when the direction is supported, Explore when a focused test could change it, or Frame when mapping reveals the wrong problem.
