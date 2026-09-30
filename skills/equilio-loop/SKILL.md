---
name: equilio-loop
description: Orchestrate the Equilio Coding core workflow from a goal to coherent, verified, review-ready work. Use this Supporting Skill when a goal calls for autonomous coordination of Frame, Map, Explore, Build, and Integrate.
---

# Equilio Loop

Start from the user's goal or desired outcome. Treat Loop as a **Supporting Skill**, not a core stage. **Loop owns orchestration. The five Core Skills own judgment.** Preserve their responsibilities and order: **Frame → Map → Explore → Build → Integrate**. Use [Frame](../equilio-frame/SKILL.md), [Map](../equilio-map/SKILL.md), [Explore](../equilio-explore/SKILL.md), [Build](../equilio-build/SKILL.md), and [Integrate](../equilio-integrate/SKILL.md) as their current canonical instructions, invoking each skill directly when supported or reading and following its `SKILL.md` otherwise. Read the [Development Principles](https://github.com/drewbarontini/equilio-coding/blob/main/references/development-principles.md) and apply them throughout. If a required skill or reference is unavailable in the installation, obtain its current repository version before proceeding. If it cannot be obtained, report the missing dependency; do not substitute a remembered or abbreviated workflow.

## Establish the shared issue

Inspect the current branch, request, project issue conventions, and relevant existing issues before creating anything. Reuse an issue that clearly owns the goal. Otherwise establish the appropriate delivery issue in the project's issue system; use local Markdown as the issue when that is the project's system or as a draft while preparing a remote issue. An ordinary change can use one issue. For broader work, follow the [parent and delivery issue model](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#one-issue-or-linked-issues) and choose the smallest coherent functioning slice that advances the goal. Do not create a duplicate issue or a large speculative delivery issue.

The issue is the canonical shared memory between skills. At every transition, re-read the issue and relevant current artifacts, then reconcile material learning into the issue body under the [issue write-back contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#issue-write-back-contract). Replace stale claims and preserve decisions, reasons, constraints, verification, and open questions. Keep it a concise account of current truth, not a stage log or a substitute for working notes. Do not rely on conversation state alone to carry context forward.

## Run the workflow

Default progression: **Goal → Frame → Map → Explore → Build → Integrate → Review-ready**. Give each skill the current goal, issue, and relevant artifacts; let that skill's instructions determine the depth and methods its work needs.

1. **Frame** the problem and desired outcome. Bring the issue into line with that understanding.
2. **Map** existing behavior and the system paths that matter. Add material system learning to the issue.
3. **Explore** meaningful alternatives in proportion to the uncertainty. Use evidence and the Development Principles to choose a direction when possible; record the decision and why it fits the goal.
4. **Build** the smallest coherent functioning vertical slice. Verify it appropriately and update the issue to describe implemented reality, not a plan or a live result.
5. **Integrate** the product, code, verification, and issue. Resolve material gaps and leave a coherent, verified implementation ready for human review, with review details in the PR or prepared for it. In Loop, stop before Integrate's optional release and live feedback work unless explicitly requested.

After each skill, read the rewritten issue before deciding the next move. Re-enter an earlier skill only when material evidence changes its judgment: for example, Map changes the problem, Explore exposes a system constraint, Build invalidates the chosen direction, or Integrate reveals that the result misses the goal. Update the issue when returning, then continue toward convergence rather than repeating phases mechanically.

Make reasonable decisions from repository evidence, the issue, conventions, tests, observed behavior, and the Development Principles. Compare options proportionally, record consequential reasoning, and continue without routine approval gates. Ask for human judgment when an unresolved decision would materially change the goal, product behavior beyond the stated intent, fundamental scope, security or privacy expectations, compatibility guarantees, major architecture, an external commitment, or destructive or irreversible behavior, or when evidence provides no reasonable basis for choosing. Continue independent work while that judgment is pending.

Stop by default at **review-ready**: implementation and appropriate verification complete, the delivery issue reconciled with reality, and the branch and working tree coherent. Commit changes when appropriate for the environment and prepare PR review detail or a draft PR when the normal workflow supports it and the request implies it. Check whether another functioning slice is required to satisfy the goal; use linked delivery issues when broader work remains. Do not merge, release, deploy, or claim live validation unless explicitly requested and supported by evidence.

## Support human understanding

After the five Core Skills converge, use the Supporting Skill [Explain](../equilio-explain/SKILL.md) when the implementation meaningfully changes the maintainer's model of the system. Follow its current instructions using the same invocation or reading approach as above. Explain is optional, not a sixth core stage or another coherence review; skip it for trivial changes where it adds no value. If used and it finds no meaningful mental-model change, report that concisely.

Leave the human with coherent, verified, review-ready work, a reconciled issue containing the current understanding, and, when useful, a concise Explain response before human review. Re-read the issue after Explain reconciles any durable new understanding; its teaching output should not be copied wholesale into the issue or PR. If explanation exposes a material contradiction, call it out and return to the appropriate Core Skill to resolve it before claiming convergence. Keep Integrate responsible for coherence and verification.
