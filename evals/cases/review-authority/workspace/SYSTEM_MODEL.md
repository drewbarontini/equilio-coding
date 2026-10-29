# Tasks System Model

Components: Form collects task input; API owns valid persisted tasks; Importer creates tasks from CSV.
Relationships: Form → API and Importer → API both create tasks.
P1 — Documented: API rejects blank task titles regardless of caller; task lists assume stored titles are nonempty. Basis: product requirement in issue.md.
P2 — Inferred: all imports run through the same API adapter; production import scheduling is not included in this snapshot.
Scope: local code snapshot only; no live environment inspected.
