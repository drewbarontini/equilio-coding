---
name: equilio-map
description: Map existing product behavior and code paths for a software change; use when implementation boundaries, dependencies, or architectural questions are unclear.
---

# Map

Start from the current request, issue, local Markdown, prototype, or code. Apply **Understand First** from the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md): observe the relevant product behavior and inspect the actual code before describing how it works. Follow the paths that matter to the change: files, functions, entry points, state, data flow, interfaces, dependencies, tests, conventions, and affected surfaces. Scale the map to the task.

Create a local Markdown map that lets another person find the important code and understand the current behavior. **Optimize for the Reader**: show the paths and relationships needed for an intentional change without burying them in an exhaustive inventory. Resolve architectural facts where the evidence allows; identify boundaries, constraints, and choices that depend on seeing an option work in the product. Separate verified facts from inferences, proposals, and decisions when it matters; use file links or paths precise enough to revisit.

Trace the product and technical paths a functioning change must connect. Identify dependencies, necessary coupling, and what can safely be released and evaluated independently. A frontend, backend, or infrastructure boundary alone is not a reason to split delivery issues. If foundational work needs a separate issue, describe the capability it enables, how to verify it, and the functioning slice it supports.

Find the project's shared issue in GitHub, Linear, or local Markdown and carry the map's accepted conclusions into it when ready. Keep detailed files, functions, flows, dependencies, and tests in working notes where useful. Synthesize what they mean for current behavior, system boundaries, constraints, and decisions in the issue, linking durable detail where needed. Establish the remote destination before changing it. Leave enough context for a fresh session to investigate without treating uncertainties as resolved.

An ordinary change may use one issue. For a larger problem, an optional parent can retain overall intent while each linked delivery issue owns its own lifecycle. Do not turn a tentative map into a fixed issue breakdown before the relevant behavior has been tested.

Before finishing, re-read and rewrite the shared issue body to reflect all material system learning. Replace stale assumptions and code inventories with a concise, accurate account of behavior and implications; preserve meaningful decisions and open choices. Leave it understandable to a human or AI without the map or prior conversation. Follow the [issue write-back contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#issue-write-back-contract).
