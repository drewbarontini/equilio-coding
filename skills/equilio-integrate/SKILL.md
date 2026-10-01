---
name: equilio-integrate
description: Review, verify, and hand off a software change; use when implementation needs product, code, and strategy coherence or a PR and work artifact need reconciliation.
---

# Integrate

Start from the work artifact, local Markdown, code, PR, or deployed result; earlier skills need not have run. Review the entire functioning slice through the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md): does it solve the actual gap, use the smallest coherent change, read clearly, leave touched areas healthy, and have sufficient integrated verification? Use judgment proportionate to the change. Check useful comments and meaningful tests without producing a separate audit or requiring artificial coverage.

Run appropriate checks and verify integrated product behavior when feasible. Update diagrams or durable documentation only when the system changed and they will help future work. If review exposes a material problem in framing, system understanding, direction, or behavior, reconcile it and return to the appropriate earlier concern before claiming readiness.

Reconcile **all five sections** against actual code and verified behavior under the [work-artifact contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#reconcile-current-understanding). Compress for handoff: current Problem, supported Solution, consequential Decisions, system-level Impact, and honest Reality. Replace disproven claims rather than retaining a workflow history.

Before preparing a PR, ensure the artifact reflects the implemented and verified work. Follow the [PR guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/pull-request.md): **Summary → Changes → Callouts**, with the issue link in Summary. Callouts is optional; Changes can be omitted for a genuinely tiny change. Orient the reviewer without duplicating the work artifact.

Merge, release, or deploy only when explicitly authorized. When they occur, update Reality with actual state, audience, live verification, and meaningful observations. Prefer independent release and feedback where useful; distinguish planned observation, observed feedback, and inference. Deployment alone does not prove live behavior, and a live test does not prove customer outcomes.

Before finishing, reconcile any further material findings and re-read the artifact. Apply the [next-operation guidance](https://github.com/drewbarontini/equilio-coding/blob/main/references/work-artifact.md#choose-the-next-useful-operation) and finish with **Recommended next:** `<skill or action>` · **Why:** `<reason>`. Recommend human review or stop / complete when appropriate to the actual state; Explain is useful when coherent work meaningfully changes the maintainer's model.
