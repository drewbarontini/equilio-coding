<!-- Generated from references/development-principles.md; edit the source and run scripts/sync-references.py. -->

# Development Principles

**Understand First → Fewest Changes → Optimize for the Reader → Better Than Before → Close the Loop**

These principles guide judgment throughout the five Core Skills: **Frame → Map → Explore → Build → Integrate**. Supporting Skills also apply them in proportion to their job: Loop orchestrates the core workflow; Explain helps a maintainer understand meaningful system changes. They are shared development doctrine, not additional workflow stages, Equilio Models, mandatory printed checklists, or gates. Explicit repository-specific requirements take precedence.

## Equilio in practice

**Intuition → Integration → Iteration** connects an initial sense of value to shared understanding, working software, and refinement through evidence. Apply all three Equilio Models throughout the work:

- **Value Creation — Build the right things.** Establish whose problem matters, why it matters, and what improvement would mean; connect product experience and system behavior before choosing a solution.
- **Quality Refinement — Elevate what exists.** Test the experience, question unnecessary complexity, and refine toward less but better while preserving the intended behavior.
- **Strategic Momentum — Sustain forward movement.** Take the next useful step, learn from functioning software, and preserve current understanding in the owning issue so progress does not depend on one conversation.

Use these to change decisions, not decorate output. Frame builds shared problem understanding; Map connects experience and implementation; Explore tests working possibilities; Build makes the fewest coherent changes; Integrate actively refines the result and preserves what changed in the system. Each concern can reveal evidence that sends the work back to an earlier question.

## Understand First

Understand the problem and existing system before prescribing or changing a solution. Inspect the product's actual behavior and relevant code paths. Understand the state, data, interfaces, dependencies, tests, and conventions that matter to the change. Distinguish verified facts from assumptions. Follow existing patterns unless there is a meaningful reason to change them; do not redesign surrounding systems merely because another design appears cleaner.

## Fewest Changes

Make the smallest coherent change that solves the problem. This does not mean minimizing lines, files, or layers. A functioning vertical slice may cross UI, backend, persistence, infrastructure, or other boundaries. Prefer the minimum connected set of changes needed to create functioning software someone can evaluate.

Avoid unrelated cleanup, speculative features, premature abstractions, and “while we’re here” expansion. Apply YAGNI where useful. Use the [delivery-slicing guidance](delivery-slices.md#shape-delivery-slices) when broader work needs decomposition; separate build tasks do not necessarily provide separate useful outcomes. Separate genuinely independent prerequisite work when it creates a useful, verifiable change. Favor changes that can be independently understood, reviewed, reverted, released, and learned from.

## Optimize for the Reader

Use American English spelling in newly written prose, including product copy, comments, documentation, work artifacts, and PRs: **favorite**, **color**, **behavior**, and **organize**. Preserve exact quotations, proper names, and existing code identifiers or external contracts.

For work artifacts and PRs, apply the shared [writing style guidance](writing-style.md): technical precision in plain language, with concrete behavior, connected reasoning, and claims supported by evidence. Keep the existing artifact budgets; remove repetition before compressing sentences.

**Prefer self-explanatory code over explanatory comments.** Improve names, control flow, and responsibilities before adding explanation; use abstractions when they reduce complexity. Follow local conventions without imposing rigid rules for line counts, function sizes, or paradigms.

**Comments should add understanding, not narration.** Preserve non-obvious reasons, invariants, constraints, compatibility requirements, and subtle external behavior near the code. “Explain why, not what” is a shorthand, not an absolute rule; explain what comprehension requires. Avoid routine branch or function narration, restated types or tests, and temporary implementation notes. Correct stale comments when behavior changes; false context is a correctness problem.

## Better Than Before

Leave the affected system at least as understandable and maintainable as before, without pursuing perfection or broad cleanup. Remove accidental complexity introduced by the change and refine rough prototype code before treating it as production code. Fix nearby problems when they directly interfere with the change or its comprehensibility; leave unrelated debt for separate work. Favor incremental improvement over idealized redesign.

## Close the Loop

**Tests should add confidence, not count.** Inspect existing coverage and run appropriate checks; add tests where evidence is weak for behavior, contracts, boundaries, regressions, failures, or integration. Code changing does not automatically require another test. Honor repository requirements without mechanically chasing coverage percentages.

Ask **what behavior must remain true** and **what is the smallest useful evidence?** Choose focused, integration, or end-to-end checks for the actual risk. Prefer tests that survive reasonable refactoring; avoid redundant layers, incidental private structure, uncertain requirements, or tests that exercise mocks more than real behavior. A misleading test creates false confidence.

When a check fails, reconcile both implementation and test with intended behavior: the code, requirement, or test assumption may be wrong. Do not blindly change or delete failing tests to make the suite pass, or preserve stale behavior solely because a test expects it.

Verify integrated behavior in the running product when feasible, including relevant failure cases. Use manual or other evidence when automation adds little confidence; record what was checked and its limits. Distinguish implementation, verification, deployment, and live validation, and reconcile material learning into the [work artifact](work-artifact.md). Comments and tests do not replace work-level reasoning; the PR follows its [own guidance](pull-request.md).
