# Equilio Coding

**Frame → Map → Explore → Build → Integrate**

Equilio Coding helps a person and an agent move from a problem to coherent, shipped software while retaining what they learn. Get to reality early by trying meaningful options in the running product. Carry context forward in an issue that explains the work clearly to the next person or agent.

**Shared problem, functioning slices, connected memory.** Break delivery work into the smallest software changes that someone can experience and evaluate. Build each slice through the product and technical layers its behavior needs. Prefer independent release to an appropriate audience when feasible: it is a way to reach reality, observe what happens, and let feedback guide the next slice. A slice can teach something useful before the broader vision is complete. Some foundational work needs its own issue; name the capability, verification, and functioning slice it supports rather than claiming product feedback it cannot produce.

The five steps are a practical application of [Equilio](https://equilio.dev), whose engine is **Intuition → Integration → Iteration** and whose Models are **Value Creation, Quality Refinement, and Strategic Momentum**. The steps are a coding method, not additional Equilio Models. Use as much of each step as the work warrants; a small fix may need only a few lines of context.

## The skills

| Skill | When to use it | Useful result |
| --- | --- | --- |
| [`equilio-frame`](skills/equilio-frame/) | A problem or proposed solution needs clearer definition. | A conversationally framed problem and local issue draft. |
| [`equilio-map`](skills/equilio-map/) | Existing behavior and code need to be understood before choosing a change. | Verified system facts and choices to test. |
| [`equilio-explore`](skills/equilio-explore/) | Product or implementation options need contact with reality. | Prototype observations and a reasoned direction, when evidence supports one. |
| [`equilio-build`](skills/equilio-build/) | A direction is ready to implement. | Working, understandable software and updated decisions. |
| [`equilio-integrate`](skills/equilio-integrate/) | A change needs coherent review, verification, and handoff. | A fully formed issue before PR creation, then a reviewable PR and later live updates. |

Each skill stands alone. Start with a rough request, an issue, a local Markdown file, a prototype, or working code. Invoke only the skill that helps with the current job; the others need not have run.

## Install

Run the interactive command and choose all five skills:

```sh
npx skills add drewbarontini/equilio-coding
```

For a non-interactive install of the set, use `npx skills add drewbarontini/equilio-coding --skill '*' --yes`. Select one skill with the CLI's skill filter:

```sh
npx skills add drewbarontini/equilio-coding --skill equilio-explore
```

The CLI can list the repository's skills with `npx skills add drewbarontini/equilio-coding --list`. Your agent's invocation syntax may vary; ask it to use a skill by name or describe the job in ordinary language.

## Local work and the issue

Use local Markdown at any step for drafts, maps, experiments, observations, decisions, and reviews. It is inspectable working material. The **shared issue** is the canonical, evolving account of the work: the GitHub issue for GitHub-tracked work, or the issue in Linear or local Markdown according to the project. Every skill re-reads and reconciles its material learning into that issue before finishing. Replace stale assumptions, preserve decisions and deferred questions, and leave enough context for the next skill to continue. Link to detailed artifacts instead of pasting scratch files or transcripts. When the team works entirely in Markdown, that local issue file can be the shared account.

The issue gains fidelity as the work progresses. Frame can leave a proposed solution open; Map can settle system facts while naming what a prototype must reveal; Explore can choose a direction from observed behavior. At the start, the issue may contain only a problem and questions. When the change is live, its completed account should explain why it mattered, what was learned and tried, what was decided and changed, how it was verified, who could use it, what feedback is available, and where the durable artifacts are.

An ordinary change can use one issue. A broader problem may use an optional parent issue for shared intent, exploration, and overall outcome, with linked delivery issues for functioning changes. Each delivery issue owns its lifecycle and links to the parent without repeating it. A PR normally advances one delivery issue and links to that issue for full context. [The issue reference](references/issue.md) gives practical slice questions and a completed-state check. [The example](examples/notification-preferences.md) shows a broader problem becoming two linked delivery slices after mapping and prototyping, with one live and one still open.

Do not create a remote issue just because a skill was invoked. Draft framing in local Markdown for review before creating or materially updating a shared issue. Establish the project's destination and review consequential framing or decisions with the user when appropriate. Once work proceeds, complete the [issue write-back contract](references/issue.md#issue-write-back-contract) before each skill finishes. Before PR creation, the delivery issue should fully reflect the implemented and verified work; the PR summarizes that reality and links to the issue for its reasoning. Keep planned feedback, observed feedback, and inference distinct. Use [the PR template](.github/pull_request_template.md) to guide a human reviewer.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). This repository contains skills and a small number of supporting references, with no required service or workflow engine.
