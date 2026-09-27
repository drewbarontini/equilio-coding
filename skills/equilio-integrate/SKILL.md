---
name: equilio-integrate
description: Review, verify, and hand off a software change; use when implementation needs product, code, and strategy coherence or a PR and shipped issue need finishing.
---

# Integrate

Start with the available issue, local Markdown, code, PR, or deployed result; the earlier skills need not have run. An ordinary change may use one issue; where a broader problem has an optional parent, use the linked delivery issue as the source of truth for this slice. Check the entire functioning slice for coherence across product experience, code structure, and strategic purpose. Run checks proportionate to the change and verify integrated behavior in the running product when feasible, not only its individual components. Record findings and any refinements in local Markdown.

Update diagrams and durable documentation when the system actually changed and those artifacts will help future work. Prepare a short PR that normally advances one delivery issue, using **Summary**, optional **Callouts**, and **Context** linking that issue. Summary should say what changed and how it was verified in two or three plain-language sentences; call out only decisions or behavior needing reviewer attention. The issue holds the full lifecycle, so do not copy a parent's narrative into the PR. Use issue-closing syntax only when merge also completes the team's live verification.

The delivery issue is the full lifecycle account, in GitHub, Linear, or local Markdown. Establish its destination before any remote update. Refine its narrative and link to code, diagrams, durable docs, PR, and release as available. Record what was released, to whom, what feedback or observation is available, and what remains unknown. When feasible, release to an appropriate audience and use feedback to shape the next slice. Mark the issue live only when the software is actually live; distinguish implemented, merged, deployed, and verified live. Keep planned feedback, observed feedback, and inferences distinct; never invent responses or claim a later state without evidence.
