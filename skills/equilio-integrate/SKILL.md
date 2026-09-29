---
name: equilio-integrate
description: Review, verify, and hand off a software change; use when implementation needs product, code, and strategy coherence or a PR and shipped issue need finishing.
---

# Integrate

Start with the available issue, local Markdown, code, PR, or deployed result; the earlier skills need not have run. An ordinary change may use one issue; where a broader problem has an optional parent, use the linked delivery issue as the source of truth for this slice. Check the entire functioning slice for coherence across product experience, code structure, and strategic purpose. Run checks proportionate to the change and verify integrated behavior in the running product when feasible, not only its individual components. Record findings and any refinements in local Markdown.

Update diagrams and durable documentation when the system actually changed and those artifacts will help future work. Before creating a PR, re-read and reconcile the delivery issue under the [issue write-back contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#issue-write-back-contract). Ensure it is fully formed through the implemented and verified state: what mattered, what was learned and decided, what changed, what was checked, and what remains open. Prepare a short PR that normally advances one delivery issue, using **Summary**, optional **Callouts**, and **Context** linking that issue. Its summary should reflect implemented reality and verification in two or three plain-language sentences; call out only decisions or behavior needing reviewer attention. The issue holds the full lifecycle and reasoning, so the PR links to it rather than reconstructing that history or copying a parent's narrative. Use issue-closing syntax only when merge also completes the team's live verification.

The delivery issue is the full lifecycle account, in GitHub, Linear, or local Markdown. Establish its destination before any remote update. Refine its narrative and link to code, diagrams, durable docs, PR, and release as available. Record what was released, to whom, what feedback or observation is available, and what remains unknown. When feasible, release to an appropriate audience and use feedback to shape the next slice. Mark the issue live only when the software is actually live; distinguish implemented, merged, deployed, and verified live. Keep planned feedback, observed feedback, and inferences distinct; never invent responses or claim a later state without evidence.

Before finishing, re-read and write any PR, release, review, or feedback learning back to the delivery issue. Reconcile stale claims and preserve decisions and deferred questions so subsequent work can continue from the issue.
