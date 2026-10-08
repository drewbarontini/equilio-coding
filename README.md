# Equilio Coding

**Core:** Frame → Map → Explore → Build → Integrate

**Supporting:** Loop — orchestrate · Explain — understand

Equilio Coding helps a person and an agent create coherent software while retaining what they learn. Three commitments distinguish the method:

1. **Continual Context.** Each Core Skill writes material learning back to the same issue as understanding changes, so the next person or agent can continue from current truth.
2. **Plain Language.** Issue and PR templates use strict word and section limits, concrete behavior, and clear reasons; the writing guide rules out filler, inflated claims, and patch narration.
3. **Working Prototypes.** Explore turns meaningful uncertainty into runnable software you can test before choosing a direction; writing and using it can reveal problems a proposal misses.

Two simple artifact shapes keep the work legible:

**Work: Problem → Solution → Decisions → Impact → Reality**

**PR: Summary → Changes → Callouts**

The work artifact preserves current understanding for the next human or agent. The PR gives a reviewer fast orientation around the implementation. [The work reference](references/work-artifact.md) defines the shared contract, information budgets, and adaptive routing; [the PR reference](references/pull-request.md) defines review prose.

The shared [writing style guidance](references/writing-style.md) makes both readable through technical precision in plain language: concrete behavior, clear cause and effect, and honest evidence within the existing limits.

Build small, atomic vertical slices through every product and technical layer their behavior needs. Each should let someone experience and evaluate functioning software. Prefer independent release to an appropriate audience when feasible, using feedback to shape the next slice. Foundational work may need its own issue; name its enabled capability, verification, and supported slice without claiming product feedback it cannot produce.

The five Core Skills apply [Equilio](https://equilio.dev), whose engine is **Intuition → Integration → Iteration** and whose Models are **Value Creation, Quality Refinement, and Strategic Momentum**. The skills are a coding method, not additional Models. Value Creation keeps the problem and purpose clear; Quality Refinement favors less but better; Strategic Momentum turns evidence into useful next steps while preserving what is learned. These concerns apply throughout the work rather than belonging to separate skills.

The shared [Development Principles](references/development-principles.md) guide judgment: **Understand First → Fewest Changes → Optimize for the Reader → Better Than Before → Close the Loop**. Fewest Changes means the smallest coherent functioning slice, including every layer it needs.

## Core Skills

**Follow the understanding, not the sequence.** Frame → Map → Explore → Build → Integrate is the canonical progression of concerns, not a mandatory pipeline. Enter anywhere appropriate, skip satisfied concerns, and revisit only when material evidence requires it. Honor explicit skill requests.

| Skill | Distinct job | Natural contribution to understanding |
| --- | --- | --- |
| [Frame](skills/equilio-frame/) | Interview until person and agent share the problem, purpose, and desired outcome. | Problem, with unknown direction or impact left provisional. |
| [Map](skills/equilio-map/) | Connect the affected product experience to actual code and system relationships. | Problem + Impact, correcting framing when needed. |
| [Explore](skills/equilio-explore/) | Build and test working prototypes where evidence could change the direction. | Solution + Decisions + Reality grounded in evidence. |
| [Build](skills/equilio-build/) | Execute the fewest changes needed for a coherent functioning solution. | Implemented Solution and Impact, consequential Decisions, and verification in Reality. |
| [Integrate](skills/equilio-integrate/) | Refine toward simpler solutions, verify coherence, and preserve system understanding. | All five coordinates reconciled with actual code and evidence. |

Every Core Skill stands alone and can rewrite all five coordinates. Start from a rough request, issue, local Markdown, prototype, or code. Each performs its job, reconciles the same work artifact when material understanding changes and before handoff, re-reads it, and gives one **Recommended next:** `<skill or action>` · **Why:** `<reason>`. The shared artifact and evidence must support continuation without hidden chat context; human judgment or stop / complete may be appropriate.

## Supporting Skills

Supporting Skills compose, inspect, or extend the workflow without adding stages or replacing Core Skill responsibilities.

**[Loop — orchestrate](skills/equilio-loop/)** adaptively follows **assess understanding → choose useful skill → run it → reconcile work artifact → reassess**. Install it with all five Core Skills. It routes from the five coordinates and current evidence, continuing until review-ready or a consequential unresolved choice needs human judgment. It may invoke Explain when meaningful maintainer understanding would benefit.

**[Explain — understand](skills/equilio-explain/)** teaches: **What should a maintainer understand differently because this changed?** Use it independently for AI-generated or human-written code, a branch, PR, completed work, or an unfamiliar implementation. Integrate checks coherence; Explain teaches the model. Durable insight missing from the work artifact belongs in Impact, Decisions, or Reality as appropriate. **Explain teaches the model. Impact preserves the model change.**

## Shared artifacts

Use **Problem → Solution → Decisions → Impact → Reality** for delivery issues, broader projects, and local Markdown work artifacts. **Same questions. Different resolution.** Projects preserve understanding of the coordinated effort; delivery issues preserve their own functioning slice. Link them without copying delivery-level detail into the parent. No hierarchy is required for ordinary work.

The same artifact gains fidelity throughout the lifecycle; replace provisional understanding with current truth rather than adding stage sections. Enforce a **250-word maximum** for the five coordinates and the [section limits](references/work-artifact.md#information-budget), with no minimum. Use natural language, preserve consequential reasoning and system meaning, and never invent validation, feedback, or delivery state. Reality records what the world has demonstrated and what remains uncertain; it is not a backlog.

When rewriting an existing issue, preserve its initial description verbatim beneath a horizontal line and **Original Request** heading, outside the word budget. Carry it forward unchanged on later updates and respect manual removal; the [preservation rule](references/work-artifact.md#preserve-the-original-request) governs write-back.

| Artifact | Purpose |
| --- | --- |
| Working Notes | Exhaustive temporary investigation and exploration. |
| Work Artifact | Canonical current understanding for humans and AI. |
| PR | Fast orientation for reviewing implementation; **100 words maximum**. |
| Code + tests | Implementation, behavior, contracts, and executable evidence. |
| Explain | Teaching that updates the human maintainer's mental model. |

Transform information between these artifacts rather than copying it blindly. The [canonical reconciliation contract](references/work-artifact.md#reconcile-current-understanding) governs write-back, including Explain's conditional updates. Use the project's destination in GitHub, Linear, or Markdown; draft locally when preparing remote work and reuse existing records. A skill invocation alone is no reason to create a remote issue.

Before PR creation, reconcile the work artifact against implemented behavior and evidence. Follow the [PR guidance](references/pull-request.md) and [template](.github/pull_request_template.md): put the issue link in Summary, use meaningful Changes, and omit unnecessary Callouts or Changes for a tiny PR. Keep implementation, merge, deployment, live verification, and observed feedback distinct.

[The notification-preferences example](examples/notification-preferences.md) shows successive rewrites of the same five-part artifact, two linked delivery slices, and a concise PR.

## Install

Choose Core Skills and optional Supporting Skills interactively:

```sh
npx skills add drewbarontini/equilio-coding
```

Install all skills non-interactively with `npx skills add drewbarontini/equilio-coding --skill '*' --yes`, select one with `--skill equilio-explore`, or list them with `--list`. Your agent's invocation syntax may vary; ask it to use a skill by name or describe the job. Invoke `equilio-loop` with a goal or work artifact, or `equilio-explain` for maintainer understanding.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). This repository contains skills and a few supporting references, with no required service or workflow engine.
