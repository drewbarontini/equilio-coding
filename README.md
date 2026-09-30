# Equilio Coding

**Core:** Frame → Map → Explore → Build → Integrate

**Supporting:** Loop — orchestrate · Explain — understand

Equilio Coding helps a person and an agent move from a problem to coherent software while retaining what they learn. Get to reality early by testing meaningful uncertainty in the running product when it could change a decision. Carry context forward in an issue that explains the work clearly to the next person or agent.

**Shared problem, functioning slices, connected memory.** Break delivery work into the smallest software changes that someone can experience and evaluate. Build each slice through the product and technical layers its behavior needs. Prefer independent release to an appropriate audience when feasible: it is a way to reach reality, observe what happens, and let feedback guide the next slice. A slice can teach something useful before the broader vision is complete. Some foundational work needs its own issue; name the capability, verification, and functioning slice it supports rather than claiming product feedback it cannot produce.

The five Core Skills are a practical application of [Equilio](https://equilio.dev), whose engine is **Intuition → Integration → Iteration** and whose Models are **Value Creation, Quality Refinement, and Strategic Momentum**. The skills are a coding method, not additional Equilio Models. Match the depth to the work; a small fix may need only a few lines of context.

The shared [Development Principles](references/development-principles.md) guide how those skills operate: **Understand First → Fewest Changes → Optimize for the Reader → Better Than Before → Close the Loop**. They are judgment guides beneath the workflow, not new stages or Equilio Models. “Fewest Changes” means the smallest coherent functioning slice, including every layer it needs, rather than the smallest diff.

## Core Skills

**Frame → Map → Explore → Build → Integrate**

These are the only five Core Skills: the canonical progression of concerns, not a mandatory pipeline or required checklist. **Follow the understanding, not the sequence.** Enter at any appropriate skill, skip work already satisfied, and revisit earlier concerns only when new evidence materially requires it.

| Skill | When to use it | Useful result |
| --- | --- | --- |
| [`equilio-frame`](skills/equilio-frame/) | A problem or proposed solution needs clearer definition. | A conversationally framed problem and local issue draft. |
| [`equilio-map`](skills/equilio-map/) | Relevant behavior and code are insufficiently understood for the change. | Verified system facts, boundaries, and remaining uncertainty. |
| [`equilio-explore`](skills/equilio-explore/) | Resolving meaningful product or implementation uncertainty could change the decision. | Test or prototype observations and a reasoned direction, when evidence supports one. |
| [`equilio-build`](skills/equilio-build/) | A direction is ready to implement. | Working, understandable software and updated decisions. |
| [`equilio-integrate`](skills/equilio-integrate/) | A change needs coherent review, verification, and handoff. | A fully formed issue before PR creation, then a reviewable PR and later live updates. |

Each Core Skill stands alone. Start with a rough request, an issue, a local Markdown file, a prototype, or working code. An explicit skill request takes precedence over automatic routing. Each skill performs its job, reconciles the shared issue, re-reads the result, and recommends one useful next skill or action with a brief reason: **Recommended next:** `<skill or action>` · **Why:** `<reason>`. Use the [reconciled issue and current evidence](references/issue.md#choose-the-next-useful-operation) to choose; hidden chat context should not be needed. Human review, optional Explain, or stop / complete may be the right next action.

## Supporting Skills

**Core skills define the workflow. Supporting skills compose, inspect, or extend the workflow without redefining it.**

Supporting Skills are optional and independently invokable for a distinct atomic job. They do not add workflow stages or change the core skills' responsibilities or canonical conceptual progression. Create another only when a recurring, independently invokable job emerges that is not already owned by a Core Skill.

**[Loop — orchestrate](skills/equilio-loop/)**

Adaptively orchestrate work from a goal or issue: **assess current understanding → choose next skill → run skill → reconcile issue → reassess → repeat**. Loop reuses the Core Skills' current instructions and routes from the issue and evidence until work is review-ready or meaningful human judgment is required. It may skip or revisit skills; a well-understood small change might use **Build → Integrate**, without making that another required sequence. Install Loop with all five Core Skills. When work is coherent and review-ready, Loop may invoke Explain if it adds meaningful maintainer understanding.

**[Explain — understand](skills/equilio-explain/)**

Surface the meaningful changes a human should understand to maintain a coherent mental model of the software. Explain teaches what concepts, boundaries, invariants, flows, or assumptions changed, filtering routine implementation detail. Use it independently for an AI-generated change, a human-written branch, a PR, completed work, or an unfamiliar implementation; the core workflow need not have produced the code. Ask “Explain what changed,” “Teach me what changed in this PR,” or “What do I need to know to maintain this?” when the intent is maintainer understanding rather than an ordinary code summary.

**Integrate:** Is this change coherent? **Explain:** What should a human understand about the coherent system that now exists? Integrate retains coherence review; Explain is a teaching skill, not another review or implementation stage.

## Install

Run the interactive command and choose the Core Skills and optional Supporting Skills you need:

```sh
npx skills add drewbarontini/equilio-coding
```

For a non-interactive install of all skills, use `npx skills add drewbarontini/equilio-coding --skill '*' --yes`. Select any Core or Supporting Skill with the CLI's skill filter:

```sh
npx skills add drewbarontini/equilio-coding --skill equilio-explore
```

The CLI can list the repository's skills with `npx skills add drewbarontini/equilio-coding --list`. Your agent's invocation syntax may vary; ask it to use a skill by name or describe the job in ordinary language. Invoke `equilio-loop` with a goal or issue for adaptive orchestration, or select `equilio-explain` on its own for maintainer understanding.

## Local work and the issue

Use local Markdown at any step for drafts, maps, experiments, observations, decisions, and reviews. **Working Notes → Issue → PR:** working notes hold exhaustive, temporary detail; the shared issue holds the canonical current understanding; the PR holds implementation detail for code review. Transform information between these layers instead of copying it. The shared issue is the GitHub issue for GitHub-tracked work, or the issue in Linear or local Markdown according to the project.

Each Core Skill and Loop re-reads and rewrites the issue body before finishing, leaving it as the best current summary of understanding for humans and AI. Explain reconciles only durable new understanding into an existing issue; otherwise it leaves the issue unchanged and does not create a competing permanent artifact. **Explain output = teaching. Issue = durable understanding.** Write-back means synthesizing material learning: replace stale assumptions, consolidate duplicates, preserve decisions and deferred questions, and remove incidental code detail. A comment, stage note, or appended work log is insufficient. A new reader should understand the current state without prior conversation or working notes. When the team works entirely in Markdown, the local issue file can be that shared account.

**PR:** How did the code change? **Explain:** What should I understand differently because it changed? Explain uses the PR and diff as evidence without duplicating them or copying its entire teaching output into the issue.

The issue gains fidelity as the work progresses. Frame can leave a proposed solution open; Map can settle system facts while naming what a prototype must reveal; Explore can choose a direction from observed behavior. At the start, the issue may contain only a problem and questions. When the change is live, its completed account should explain why it mattered, what was learned and tried, what was decided and changed, how it was verified, who could use it, what feedback is available, and where the durable artifacts are.

An ordinary change can use one issue. A broader problem may use an optional parent issue for shared intent, exploration, and overall outcome, with linked delivery issues for functioning changes. Each delivery issue owns its lifecycle and links to the parent without repeating it. A PR normally advances one delivery issue and links to that issue for full context. [The issue reference](references/issue.md) gives practical slice questions and a completed-state check. [The example](examples/notification-preferences.md) shows a broader problem becoming two linked delivery slices after mapping and prototyping, with one live and one still open.

Do not create a remote issue just because a skill was invoked. Draft framing in local Markdown for review before creating or materially updating a shared issue. Loop checks for an existing owner and establishes a delivery issue when needed; it requests human judgment for consequential framing or decisions. Once work proceeds, follow the [issue write-back contract](references/issue.md#issue-write-back-contract), including Explain's conditional reconciliation. Before PR creation, the delivery issue should reflect the implemented and verified work; the PR explains how the code implements that understanding and links to the issue. Keep planned feedback, observed feedback, and inference distinct. Use [the PR template](.github/pull_request_template.md) to guide a human reviewer.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). This repository contains skills and a small number of supporting references, with no required service or workflow engine.
