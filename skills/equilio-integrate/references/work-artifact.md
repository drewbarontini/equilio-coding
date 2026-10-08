<!-- Generated from references/work-artifact.md; edit the source and run scripts/sync-references.py. -->

# Work as current understanding

**Problem → Solution → Decisions → Impact → Reality**

The shared work artifact preserves the **current understanding of the work** for humans and AI agents. Use the same shape for delivery issues, broader projects, and local Markdown work artifacts, whether the destination is GitHub, Linear, or the project's Markdown files.

For delivery work, the issue is the core artifact: continually rewrite its current understanding as material learning emerges. Use a local Markdown equivalent when no issue owns the work; the PR and chat are not substitutes for the owning artifact.

> After any Equilio operation, a fresh human or AI agent should be able to read the shared work artifact and responsibly continue without needing prior conversation or hidden agent context.

## The shared shape

```markdown
<!-- Maximum 250 rendered words across the five coordinates; Original Request is excluded. Follow the section limits and writing-style.md: concrete behavior, clear reasons, honest evidence, no filler or patch narration. -->

# [Work title]

## Problem

**Current:** What is happening now?

**Expected:** What should happen instead?

## Solution

How are we addressing the gap?

## Decisions

What consequential choices shaped the approach, and why?

## Impact

What responsibilities, relationships, boundaries, flows, behaviors, or assumptions change because of this work?

## Reality

What remains uncertain? What has actually been verified or observed? What errors, feedback, trade-offs, limitations, or new opportunities should shape what happens next?

---

## Original Request

[Existing issue description, preserved verbatim when present before the first rewrite.]
```

These are stable coordinates, not fields to fill mechanically. Keep the five coordinate headings throughout the lifecycle; use brief provisional language where understanding is missing, such as “Direction not chosen,” “System impact is not yet understood,” or “Not yet verified.” Do not manufacture information or pad sections.

Original Request preserves source wording beneath the five coordinates; it is not a sixth coordinate. Include it only when preserving an existing issue description under the [preservation rule](#preserve-the-original-request).

| Coordinate | What belongs here |
| --- | --- |
| **Problem** | The actual gap: what happens, what should happen, and why it matters. State Current and Expected in one sentence each. Rewrite the framing when evidence corrects it. |
| **Solution** | The high-level approach and resulting behavior. Distinguish a proposal from a chosen direction; describe the mechanism rather than the patch. |
| **Decisions** | Consequential choices and their reasons that could matter to a future change. Combine choice and reason, for example: **Check preference at send time:** This is the last boundary we control before provider acceptance. |
| **Impact** | System meaning: changed responsibilities, relationships, boundaries, flows, contracts, behaviors, invariants, or assumptions. Before implementation, it can explain the relevant current system model. Preserve what a maintainer should understand differently, without file, function, class, or component inventories. |
| **Reality** | The gap between what we believe and what the world has demonstrated: verification, observations, errors, feedback, unknowns, accepted trade-offs, limitations, and opportunities that affect judgment. |

Reality acknowledges that implementation is not completion. Distinguish planned testing or observation, verified behavior, observed use, inference, unknowns, and accepted trade-offs when material. Record implementation, merge, deployment, live verification, and observed feedback as separate facts only when they occur. Reality is not a backlog, and it need not imply more work always exists.

## Information budget

The five-coordinate body of an issue, project, or local work artifact must be **250 words or fewer**. There is no minimum. These are hard limits, not targets:

| Section | Maximum shape |
| --- | --- |
| **Problem** | Two sentences: one **Current**, one **Expected**. |
| **Solution** | One paragraph of two sentences. |
| **Decisions** | Three bullets, one sentence each; or one short sentence. |
| **Impact** | One paragraph of two sentences. |
| **Reality** | Three bullets, one sentence each; or one short sentence. |

Keep only the five headings within the current understanding. No nested bullets, subheadings, tables, code blocks, appendices, or collapsed detail. The preserved Original Request section is the sole structural exception and retains its original formatting. Give each synthesized fact one home: Solution describes behavior, Decisions explains consequential choices, Impact preserves the changed system model, and Reality records evidence and limits.

Count rendered body text, including headings and link labels; exclude the separate title, link destinations, template comments, and the entire Original Request section. Before writing or updating the destination, count words and check the section limits; revise until both pass. Only an explicit user instruction or a mandatory destination requirement can override these limits; complexity alone cannot.

Before keeping a sentence, ask: **If I remove this sentence, would a fresh human or agent make a materially worse decision about the work?** If not, remove it. Prefer meaning over activity.

When oversized, remove duplication and compress first, then link necessary durable detail with a label that explains its relevance. Keep the gap, chosen direction, consequential reasoning, changed system model, and material evidence or uncertainty understandable in the body. Do not hide overflow in comments or move it into the PR. Split only when the work contains multiple coherent problems or outcomes, never just to meet a word limit. Exclude chronological logs, transcripts, raw exploration history, exhaustive alternatives or tests, commands, code inventories, generic “implemented / updated / tested” narration, and prose that restates code or diffs.

## Reconcile current understanding

Read this reference, the [writing style guidance](writing-style.md), and the existing artifact before modifying it. Apply the writing guidance within the information budget: make behavior, reasons, system meaning, and evidence easy to follow. Establish the destination and preserve records, relationships, and useful links; prefer updating over creating a duplicate. Use a local Markdown artifact while preparing a remote one. Do not create a remote issue merely because a skill ran; use the user's existing authorization and request human judgment only for consequential unresolved choices.

Every Core Skill can rewrite all five coordinates while preserving the Original Request unchanged. Read this contract at the start of the operation. Reconcile when material learning changes the problem, approach, consequential reasoning, system understanding, or evidence, before acting on that changed understanding and before handoff. Batch closely related findings into one coherent rewrite; routine tool calls and unchanged understanding need no write. Replace stale guesses with current truth, retain consequential reasoning, synthesize material learning, and remove contradictions and duplication.

Enforce the [information budget](#information-budget) before each update, then re-read the result to ensure the invariant holds. Comments, appended stage notes, and working notes alone do not satisfy reconciliation. Once a remote artifact owns the work, a local draft cannot replace its update; if blocked, preserve a destination-ready synthesis and report the incomplete reconciliation. Continue independent work where useful, but do not claim the owning issue is current until its update is verified.

**Frame → Map → Explore → Build → Integrate** is a progression of concerns, not a mandatory pipeline or a set of artifact sections. Fidelity increases within the same five coordinates:

| Skill | Natural emphasis, without exclusive ownership |
| --- | --- |
| Frame | Strengthen Problem; leave unknown direction, impact, or verification provisional. |
| Map | Strengthen Problem and Impact through actual product and system understanding; mapping may correct the gap. |
| Explore | Strengthen Solution, Decisions, and Reality through discriminating evidence; separate observations from hypotheses. |
| Build | Turn prospective Solution and Impact into implemented behavior; preserve consequential decisions, verification, and remaining uncertainty. |
| Integrate | Reconcile all five coordinates against actual code and verified behavior, compressing them for handoff. |

Loop uses the same reconciliation contract for orchestration learning. Explain conditionally reconciles durable insight into an existing artifact: mental-model changes generally belong in Impact, reasoning in Decisions, and unresolved invariants, trade-offs, limits, or observation needs in Reality. Leave it unchanged if nothing durable is missing; do not copy the teaching response or require a new artifact for standalone Explain. **Explain teaches the model. Impact preserves the model change.**

### Preserve the original request

Before first rewriting an existing issue into the shared shape, preserve its nonempty description verbatim beneath Reality, separated by `---` and headed `## Original Request`. Retain wording, links, and formatting without correcting, summarizing, or truncating them. Reflect relevant intent and constraints in the five coordinates as well; preserving the source does not replace understanding it. Omit this section for an empty description or a newly created issue with no existing source description.

On later updates, carry the same Original Request forward unchanged; do not duplicate it or replace it with a previous synthesis. Read the latest issue before writing and preserve any later human additions verbatim rather than silently overwriting them. Respect manual removal of Original Request; do not restore it from past drafts or history, or treat an already structured artifact as a new original request. After writing, re-read the issue to verify both the current understanding and preserved source.

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

## Artifact responsibilities

| Artifact | Responsibility |
| --- | --- |
| **Working Notes** | Exhaustive temporary investigation and exploration, including detailed code maps and raw trials. |
| **Work Artifact** | Problem → Solution → Decisions → Impact → Reality: canonical current understanding for humans and AI. |
| **PR** | [Summary → Changes → Callouts](pull-request.md): fast orientation for implementation review. |
| **Code + tests** | Implementation, behavior, contracts, and executable evidence. |
| **Explain** | Teaching that updates the human maintainer's mental model. |

Transform information between these artifacts instead of copying it blindly. Link durable detail when it matters; temporary notes must not be the only home of understanding needed to continue.

## Choose the next useful operation

**Follow the understanding, not the sequence.** Read the reconciled artifact with relevant repository, implementation, verification evidence, and the [Development Principles](development-principles.md). Honor an explicitly requested skill first. Skip satisfied concerns and revisit only when new evidence materially requires it.

Use the five coordinates as judgment lenses: Is the **Problem** understood enough? Is there a supported **Solution**? Are consequential **Decisions** resolved enough? Is the relevant system **Impact** understood? What uncertainty or evidence in **Reality** should determine the next move? These are not gates, scores, maturity levels, or required checklists.

| Useful operation | Reason to choose it |
| --- | --- |
| Frame | The actual gap, outcome, or important boundaries remain unclear. |
| Map | Relevant behavior, flow, contracts, or dependencies remain assumptions that affect the change. |
| Explore | A focused test or prototype could resolve meaningful uncertainty and change the decision. |
| Build | The problem, system, and direction are understood enough for a responsible change; certainty is unnecessary. |
| Integrate | Functioning implementation needs coherence review, verification, and handoff. Return to earlier concerns if material problems emerge. |
| Explain | Coherent work meaningfully changes the maintainer's mental model; skip it for trivial changes. |
| Human judgment or stop / complete | A consequential unresolved choice needs a human, or no further operation is useful given the requested scope and actual state. |

After reconciliation, each Core Skill and Loop finishes with one concise **Recommended next:** `<skill or action>` and **Why:** `<reason>`. Keep material reasons and evidence in the artifact, so routing does not depend on hidden conversation state. A recommendation neither requires an installed skill nor invokes it automatically; Loop owns adaptive orchestration.
