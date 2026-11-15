---
name: equilio-retro
description: Inspect evidence from a completed coding session to recommend small, high-leverage improvements to the agent's working environment. Use after real work reveals navigation, context, tooling, or verification friction; not for evaluating the product change.
---

# Retro

Use Retro as an independently invokable **Supporting Skill** after a coding session or meaningful work interval. Ask: **What about the working environment made this task harder than necessary, and what small change would help the next session?** This is not a code review, delivery retrospective, or another implementation stage. Integrate judges the product change; Review supports a PR acceptance decision; Retro improves the environment in which agents and people work.

## Inspect actual session evidence

Establish the session goal and inspect accessible evidence: commands and tool results, navigation/search detours, repeated context requests, instructions consulted or missed, setup failures, verification friction, handoffs, and work-artifact continuity. Use only records actually available; distinguish observed events from inference and user-reported friction. Do not claim access to hidden agent reasoning, missing logs, or past sessions. If evidence is too thin, ask for one concrete example or report that no supported recommendation is available.

Look for recurring or consequential friction across five lenses, only where relevant:

- **Navigation:** missing or misleading pointers to entry points, ownership, or important code paths.
- **Context:** inaccessible decisions, stale references, duplicated or contradictory instructions, and lost handoff knowledge.
- **Tooling:** unnecessary calls, manual repetition, slow or unreliable setup, and missing capabilities.
- **Checks:** avoidable regressions or uncertainty that a fast, deterministic test, linter, formatter, or preflight could catch.
- **Instruction economy:** rules that are redundant, overly broad, unenforceable, or costly to maintain.

Distinguish environment friction from a one-off difficult problem, code quality issue, or individual agent mistake. A single observation may justify a small change when its consequence is substantial; repetition alone does not establish priority.

## Recommend fewer, better changes

For each worthwhile candidate, connect **evidence → friction → proposed intervention → expected benefit → cost or trade-off**. Rank at most three by likely future leverage, confidence, and implementation effort; fewer or none is acceptable. Prefer repairing existing entry points, references, automation, and guidance over adding files, templates, or process. For mechanical mistakes, prefer a deterministic check over another prose rule. Remove obsolete or conflicting instructions before adding more. Identify the repository-owned destination and owner where known; do not impose a universal standards document or new schema.

Present proposals separately from changes actually made. Do not automatically edit shared instructions, standards, CI, scripts, repository settings, or other durable environment configuration. Obtain explicit authorization for the proposed change and its scope before applying it, especially for consequential or shared changes. Inspect the current destination and reconcile concurrent edits before any authorized modification. Do not expose secrets, credentials, or private logs in a retrospective.

## Close with a useful handoff

Report the strongest observed friction, up to three ranked recommendations with evidence and confidence, and the single best next action (or no action). Describe how a future session could verify that the intervention helped, without claiming improvement before it is observed. Keep temporary session details in working notes; avoid creating a separate retrospective database, work artifact, or issue by default. If an existing work artifact already owns an authorized environment improvement, follow the [work-artifact contract](references/work-artifact.md) and [Development Principles](references/development-principles.md) for material updates, without rewriting the product-delivery artifact merely to record session commentary.
