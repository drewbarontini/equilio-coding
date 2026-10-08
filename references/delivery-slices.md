# Delivery slices

Read when broader work needs decomposition or coordinated project and delivery issues; apply the shared [work-artifact contract](work-artifact.md) throughout.

## Issues and projects

**Same questions. Different resolution.** A delivery issue preserves understanding of its own functioning slice. A broader project or optional parent issue preserves the coordinated effort at project resolution; link delivery issues without aggregating their detailed decisions or implementation information. An ordinary change can use one artifact without a hierarchy.

### Shape delivery slices

For work that needs decomposition, use **Surface → Structure → Slice → Simplify → Sequence**. These are reasoning concerns, not required rounds, artifact sections, or another workflow; skip what is already understood and revisit when evidence changes it.

- **Surface:** Make relevant actions, decisions, questions, risks, and unknowns visible in working notes.
- **Structure:** Connect the affected experience, system responsibilities, and dependencies; group what belongs together rather than by implementation layer.
- **Slice:** Ask **if this shipped and work stopped here, could someone complete something useful?** Include every layer needed for that outcome. A slice may rely on already available behavior or an earlier released slice, but cannot need future work for basic usefulness; combine interdependent pieces.
- **Simplify:** Remove or defer states, controls, variants, and other scope while preserving the useful outcome. Easy implementation alone does not justify added scope.
- **Sequence:** Order releases by value and dependencies, identifying who can evaluate each slice and what the observation could change.

Database, API, and interface tasks can be separate build units within one delivery slice. Technical staging, including preparatory deployments or work behind a flag, does not establish delivery of the slice's value. Keep necessary sequencing detail in linked working notes; preserve consequential boundaries, dependencies, and evidence in the existing five coordinates without adding a planning schema or creating speculative issues.

When foundational work needs its own issue, name the enabled capability, verification, and functioning slice it supports. Its evidence is capability verification; do not claim end-user value or feedback it cannot produce.
