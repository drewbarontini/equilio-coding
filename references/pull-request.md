# Pull Request Guidance

**Summary → Changes → Callouts**

The work artifact preserves understanding; the PR orients a human reviewing the implementation. Reconcile the [work artifact](work-artifact.md) before preparing a PR. Use [the template](../.github/pull_request_template.md), omitting Callouts when unnecessary and Changes for a genuinely tiny change.

Target **75–150 words** for a normal description. At roughly **200 words**, reconsider what belongs in code, the work artifact, or a durable linked artifact. Do not repeat the full Problem, Decisions, Impact, or Reality, narrate development, or add default sections.

Do not add generated-by footers, agent signatures, model names, or tool branding to the editable PR body. Leave platform-generated metadata alone.

## Summary

**What does this change accomplish?** Use approximately 1–3 sentences about resulting behavior or outcome. Put the issue link directly after the prose:

```markdown
## Summary

Fixes keyboard navigation so focus follows the highlighted command-menu result.

Closes #123
```

This is a complete PR for a tiny change. Use closing syntax only when merge should close the issue; otherwise use a plain issue link, including when release or live verification must still occur. A PR normally advances one delivery issue.

## Changes

**What meaningfully changed in the implementation or code system?** Usually use **2–5 bullets**, one sentence each, orienting reviewers around behavior, responsibility, flow, boundary, contract, or meaningful implementation changes:

```markdown
## Changes

- **Send eligibility:** The worker now uses current preference state rather than treating the earlier batch snapshot as final eligibility.
- **Settings:** Preference copy now reflects the actual send-time boundary.
```

Omit this section for a genuinely tiny change. Avoid file, function, class, or component inventories, mechanical diff summaries, “added tests,” “updated component,” and narration of obvious code. The diff already shows mechanics.

## Callouts

Optional; usually **0–3 bullets**. Include only something deserving disproportionate reviewer attention: risk, an important trade-off, compatibility concern, intentional limitation, unusual verification, surprising behavior, or an area for focused review. Never manufacture callouts.

Ordinary checks need no prose unless the repository requires it. Mention verification when noteworthy, for example manual keyboard-focus verification that covers behavior the automated suite cannot represent. Keep broader evidence and limitations in Reality.
