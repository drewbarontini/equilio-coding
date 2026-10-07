# Contributing

Keep Equilio Coding small and usable across projects and work systems. Consolidate overlapping guidance before adding concepts or files.

- Preserve exactly five standalone **Core Skills**: **Frame → Map → Explore → Build → Integrate**. This is a progression of concerns, not a mandatory pipeline. Each needs valid `name` and `description` frontmatter, a distinct job and method, and useful output when entered from a request, issue, local file, prototype, or code. Honor explicit skill requests.
- Keep **Loop** and **Explain** as optional **Supporting Skills**. Loop owns adaptive orchestration using the Core Skills' current instructions; Explain owns maintainer comprehension. Neither adds a stage or duplicates a Core Skill's job. Add supporting skills only for a genuine recurring, independently invokable need.
- Use the [canonical work artifact](references/work-artifact.md): **Problem → Solution → Decisions → Impact → Reality** for issues, projects, and local Markdown. Keep its meaning, hard 250-word maximum, section limits, reconciliation contract, and routing guidance in that reference. Skills should retain their distinct method, natural contribution to understanding, shared reconciliation requirement, and next-operation judgment without maintaining separate schemas or shipped-state checklists.
- Every Core Skill can rewrite every section and must reconcile and re-read the artifact before recommending one useful next action with a brief reason. Loop does so at each transition and for orchestration learning. Routing must work from the artifact and relevant evidence without hidden conversation state. Skip satisfied concerns; revisit only when material evidence requires it. Do not add scores, maturity levels, required checklists, gates, or service dependencies.
- Preserve **Same questions. Different resolution.** Projects hold broader understanding; delivery issues hold their own functioning slices. Link rather than aggregate detail. Keep slices atomic and vertical, independently releasable and evaluable when feasible. Distinguish foundational capability verification from product feedback.
- Preserve the five [Development Principles](references/development-principles.md). Link rather than repeat their doctrine. Favor clear code, comments that preserve meaningful reasoning or constraints, and verification that adds confidence. Do not narrate straightforward code or require redundant or misleading tests for every edit; honor repository-specific checks.
- Treat Explain's response as teaching. Reconcile missing durable insight into Impact, Decisions, or Reality as appropriate, without copying its response or creating a competing artifact by default. **Explain teaches the model. Impact preserves the model change.** Integrate retains coherence review.
- Keep [artifact responsibilities](references/work-artifact.md#artifact-responsibilities) distinct and transform information between them. Prefer updating existing records; establish remote destinations and preserve relationships. Human judgment is appropriate for consequential unresolved choices, not routine edits. Merge, release, and deployment require explicit authorization.
- Accurately distinguish proposed, decided, implemented, merged, deployed, verified live, and observed feedback. Reality may contain uncertainty, errors, limits, or opportunities without implying a mandatory backlog.

Follow [PR guidance](references/pull-request.md) and [the template](.github/pull_request_template.md) exactly: **Summary → Changes → Callouts**. Place the issue link in Summary. Callouts is optional; Changes may be omitted for a genuinely tiny PR. Enforce the **100-word maximum** and section limits before creating or updating a PR. Avoid patch narration, inventories, duplicate work-artifact content, and generated-by footers or agent signatures.

## Validation

Validate new or modified skills with the available skill validator (`quick_validate.py <skill-directory>`). Check that Explain's `agents/openai.yaml` remains consistent with its instructions.

When the skills CLI is available, list the repository and confirm installation selection for a single Core Skill, Loop, and standalone Explain:

```sh
npx skills add <local-path> --list
npx skills add <local-path> --skill equilio-frame --yes
npx skills add <local-path> --skill equilio-loop --yes
npx skills add <local-path> --skill equilio-explain --yes
```

Run installation checks in a disposable project so they do not change personal skill installations. Confirm every skill can access canonical references, including when installed alone. Compare the README, references, template, and example against the actual skill instructions; search for superseded schemas and broken links. Review the final diff for unnecessary prose and prefer deleting obsolete guidance over preserving it alongside the new model.
