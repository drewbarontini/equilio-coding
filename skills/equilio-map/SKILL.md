---
name: equilio-map
description: Map existing product behavior and code paths for a software change; use when implementation boundaries, dependencies, or architectural questions are unclear.
---

# Map

Use the [work-artifact contract](references/work-artifact.md) throughout; keep the owning issue current as understanding changes. Reuse current guidance already in context, but read the latest artifact at the start.

Start from the request, work artifact, local Markdown, prototype, or code. Apply the [Development Principles](references/development-principles.md): observe relevant product behavior and inspect the actual code before describing it. Trace entry points, state, data flow, interfaces, dependencies, tests, conventions, and affected surfaces only as deeply as the change requires. Do not repeat sufficient investigation.

Connect the affected person's journey to the surfaces, actions, and state changes they encounter, then trace how actual code and system boundaries produce that behavior. Explain where the problem enters this path, what a solution must connect, and which constraints could change the direction. Use the browser for relevant UI behavior when available; code inspection alone cannot establish the experience. For work without a UI, trace the corresponding caller or operational flow.

Keep a local Markdown map as working notes, with precise references for revisiting relevant code and relationships. Separate verified facts from inference and unresolved choices. When work needs decomposition, use the [delivery-slicing guidance](references/delivery-slices.md#shape-delivery-slices) to connect outcomes and dependencies before separating issues. Identify what each candidate slice needs from the existing product or earlier releases; keep mutually dependent layers together.

Primarily strengthen **Problem + Impact**. Mapping may correct the gap; Impact can explain the relevant current system model before any change is implemented. Synthesize responsibilities, relationships, boundaries, and constraints that affect judgment. Keep detailed code maps in working notes, linking durable detail only when needed. Do not copy file or function inventories into the shared artifact or imply architectural facts settle a product decision.
