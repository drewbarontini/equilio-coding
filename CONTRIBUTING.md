# Contributing

Keep Equilio Coding small and usable across projects and issue systems.

- Each `skills/<name>/SKILL.md` must have valid `name` and `description` frontmatter, a distinct trigger, one primary job, and a useful output. It must work when installed alone and entered from a rough request, an issue, a local file, a prototype, or code.
- Keep local Markdown available as inspectable working space at every step. Treat the shared issue as the concise current account, whether GitHub, Linear, or local Markdown. Establish a remote destination before changing it and carry accepted conclusions forward without copying scratch material.
- Keep issue and PR conventions consistent with [the issue reference](references/issue.md) and [PR template](.github/pull_request_template.md). Do not add a stage gate, service dependency, or automation without a demonstrated need.
- State what is observed, decided, implemented, merged, deployed, and verified live accurately. Keep the five steps distinct from Equilio's three Models.

Before proposing a change, validate modified skills with the skill validator, list the repository through `npx skills add <local-path> --list` when the CLI is available, and confirm that a single skill can be selected with `--skill <name>`. Read the README and example against the actual skill instructions.
