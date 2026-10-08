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

Avoid unrelated cleanup, speculative features, premature abstractions, and “while we’re here” expansion. Apply YAGNI where useful. Separate genuinely independent prerequisite work when it creates a useful, verifiable change. Favor changes that can be independently understood, reviewed, reverted, released, and learned from.

## Optimize for the Reader

Use American English spelling in newly written prose, including product copy, comments, documentation, work artifacts, and PRs: **favorite**, **color**, **behavior**, and **organize**. Preserve exact quotations, proper names, and existing code identifiers or external contracts.

For work artifacts and PRs, apply the shared [writing style guidance](writing-style.md): technical precision in plain language, with concrete behavior, connected reasoning, and claims supported by evidence. Keep the existing artifact budgets; remove repetition before compressing sentences.

Make code's intent easy for the next human or AI to understand. **Prefer self-explanatory code over explanatory comments.** Clear names, straightforward control flow, focused responsibilities, and local conventions should communicate what the code does, how it is structured, and its important concepts. Use abstractions when they meaningfully reduce complexity. Prefer explicit code over clever code and reduce cognitive load. Do not impose rigid rules for line counts, function sizes, class structures, or programming paradigms.

Before adding a comment, ask: **Can the code itself be made clearer?** Prefer better naming, structure, or decomposition when it removes the need for explanation. **Comments explain why, not what** is a useful shorthand, not an absolute rule: explain more when comprehension genuinely requires it. Preserve non-obvious reasoning, important invariants, constraints a maintainer could accidentally violate, why an obvious implementation is intentionally avoided, or subtle external behavior, compatibility requirements, and system limitations. Keep context near the code when it would otherwise be lost.

Do not add comments by default merely because code changed. Avoid comments above every function or obvious branch, restatements of names or types, narration of straightforward steps, repetition of clearly expressed tests, verbose documentation of already-clear private details, and temporary implementation notes left after completion. **Comments should add understanding, not narration.**

Treat comments as maintained code. Inspect relevant comments when changing nearby behavior; correct stale claims and remove context that is no longer useful. A stale comment is worse than no comment because it creates false understanding; treat it as a correctness problem.

## Better Than Before

Leave the affected system at least as understandable and maintainable as before, without pursuing perfection or broad cleanup. Remove accidental complexity introduced by the change and refine rough prototype code before treating it as production code. Fix nearby problems when they directly interfere with the change or its comprehensibility; leave unrelated debt for separate work. Favor incremental improvement over idealized redesign.

## Close the Loop

Verify the change as an integrated piece of software rather than stopping at generated code. **Tests should increase confidence, not merely increase coverage.** Run appropriate existing checks and inspect existing coverage before adding or updating tests. Add or update tests when they provide trustworthy evidence for observable behavior, important contracts, regression-prone logic, boundaries, meaningful edge cases, failure behavior, invariants, or integration points where confidence is weak. Code changing does not automatically require another test. **Tests should add confidence, not count.** Do not optimize for test count or mechanically pursue coverage percentages unless the repository explicitly requires them.

**A misleading test can be worse than no test because it creates false confidence.** Avoid tests based on uncertain or incorrect interpretations of intended behavior, unnecessary coupling to private implementation, brittleness under reasonable refactoring, redundancy with stronger coverage, exercising mocks more than real behavior, or incidental details rather than the contract. Do not preserve stale behavior because an old test expects it, or add tests so broad or indirect that failures offer little useful information.

Ask: **What behavior must remain true?** Prefer tests that survive reasonable internal refactoring while external behavior and contracts stay unchanged. Unit and implementation-level tests remain useful when justified; avoid coupling to incidental structure. In keeping with **Fewest Changes**, ask: **What is the smallest useful evidence that this behavior is correct?** Choose focused tests for isolated behavior, integration tests for risks between components, or higher-level tests for an end-to-end contract. Avoid overlapping tests at several layers without a reason.

When an existing test fails, reconcile both implementation and test with the work artifact and current understanding of intended behavior. Determine whether the implementation violated the contract, requirements changed, the test reflects an outdated assumption, or the test is brittle or incorrectly specified. Do not blindly change tests until they pass, preserve them solely because they exist, or delete failures to make the suite green. Both should converge on the intended behavior.

Verify integrated behavior in the running product when feasible, inspecting failure and edge cases in proportion to the change. Automated tests are one form of verification. When automation is impractical or adds little confidence, use manual verification or another appropriate method; record what was checked and what remains unverified. Prefer honest evidence over artificial tests. Distinguish implementation, verification, deployment, and live validation, and incorporate meaningful learning into the current understanding of the work.

Keep artifact responsibilities distinct: code communicates intent; comments preserve reasoning, constraints, and invariants that belong nearby; tests provide evidence for behavior and contracts; the [work artifact](work-artifact.md) preserves current understanding; the PR gives a quick review synopsis under the [PR guidance](pull-request.md). Comments and tests do not replace work-level decision reasoning, and the PR need not duplicate all comments or tests.
