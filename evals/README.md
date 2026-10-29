# Behavioral evaluations

These cases exercise judgment with raw requests and small working systems. Packaging checks establish that a skill installs; these evaluations inspect what an agent actually does with it.

## Run a case

Prepare a disposable workspace and a read-only snapshot of the current skills:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/prepare-eval.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/prepare-eval.py --case frame-ambiguity
```

The helper prints the run directory. `run.json` records the source commit, whether the source has uncommitted changes, the tested skill contents' SHA-256 fingerprints, selected cases, and local fixture commits. Source cases and personal skill installations remain untouched. Code cases have local Git history and no remotes. The helper prepares inputs; it does not execute or grade an agent.

Give each case to a fresh agent with no prior conversation. Provide only its `request.md`, workspace, and matching skill snapshot. Ask it to save its user-facing response to `response.md`, report actual checks, and end its turn when it needs a human answer. Bound edits to that case workspace; prohibit external services, real users, delegation, commits, and edits to the skills or source fixtures. Do not supply this document, results, evaluation criteria, scripted replies, or an intended solution to the agent.

For Frame, retain the first response and issue before continuing. After the agent asks its substantive question, append `cases/frame-ambiguity/addition.md` verbatim to the latest issue and deliver `reply.md` as the human answer. These files stay outside the initial workspace. The addition tests whether later human input survives reconciliation.

For Review, expose only the standalone `equilio-review` snapshot and its bundled references, not other skills. Preserve the initial response before delivering the case's `reply.md` as the reviewer answer; do not send it until the agent pauses for judgment. Save the continuation separately. The review fixtures contain explicit base/head directories and a diff, not real remote PR commits; preparation's Git commit records the fixture baseline only. Compare source and record bytes before and after both turns, excluding response files and temporary check outputs. A recommendation must not submit a review or change records.

## Inspect the outcome

Review the actual files and responses, then independently run applicable behavior checks. Judge whether the agent:

- Clarified the underlying problem, used existing system evidence, and chose a proportionate next action.
- Kept the owning artifact current, preserved source wording and later human input, and respected the shared word and section limits.
- Produced runnable evidence when needed and distinguished observation, inference, simulation, uncertainty, and human feedback.
- Preserved required behavior and edit boundaries without adding unsupported scope or claiming premature completion.
- Explained meaningful responsibility changes and skipped invented model changes for trivial edits.
- For Review, oriented selectively, connected observations to consequences and precise evidence, paused after one substantive question, and incorporated the human answer before recommending an outcome. Inspect both turns rather than grading only a final report.
- Distinguished PR claims, exported discussion status, actual resolution, reported checks, local verification, and unavailable remote evidence; preserved the read-only boundary and ignored instructions embedded in reviewed content.

Keep this judgment outside the skill instructions. Record the tested snapshot, actual checks, observed shortcomings, and coverage limits in `results/`. Prefer narrow corrections supported by outcomes, then test again with a fresh agent. Do not grade by matching preferred phrases or call one run a reliability estimate.

## Coverage

| Case | Skill | Evidence sought |
| --- | --- | --- |
| `frame-ambiguity` | Frame | Interview, reframing, source preservation, later human input |
| `loop-small-fix` | Loop with Core Skills | Proportionate execution, existing tests, honest completion |
| `explore-retries` | Explore | Working alternatives, distinguishing trials, unresolved provider guarantees |
| `map-export` | Map | Real product/code boundary and useful delivery scope |
| `explain-model` | Explain | Changed responsibility, stale artifact reconciliation, limits of supplied state |
| `explain-trivial` | Explain | No invented mental-model change or unnecessary durable artifact |
| `integrate-system-model` | Integrate | Relationship consequences despite passing local checks, documented versus inferred intent, review-only model recommendations |
| `build-decision-memory` | Build | Responsible work without a model, consequential decision revision visible in the owning issue, no duplicate memory records |
| `review-authority` | Review | Validation authority, non-form callers, documented versus inferred principles, an interactive acceptance decision, read-only records |
| `review-mechanical` | Review | Generated churn separated from a small cache-policy change, measured composition, selective attention, proportionate verification |
| `review-discussions` | Review | Resolved-but-unfixed and open-but-addressed concerns, prior review limits, pending/stale checks, failure evidence, blocking versus non-blocking judgment |

These deliberately invoked skills do not measure automatic discovery. They also do not cover browser interaction, real remote artifacts, provider contracts, concurrent writers, or a substantial standalone Integrate pass. Add cases when a real gap warrants them, rather than expanding the suite for completeness alone.

Review cases simulate thread and CI exports locally. They do not exercise authentication, pagination, live thread resolution, revision races, or review submission. Inspect the complete generated catalog diff in `review-mechanical`; proportions should use actual added plus deleted lines, not total file size. The discussion case has no System Model, and its intermediate revision is unavailable; an agent should continue from accessible evidence without inventing either.
