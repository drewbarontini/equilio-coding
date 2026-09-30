# Development Principles

**Understand First → Fewest Changes → Optimize for the Reader → Better Than Before → Close the Loop**

These principles guide judgment throughout **Frame → Map → Explore → Build → Integrate**. They are shared development doctrine, not additional workflow stages, Equilio Models, mandatory printed checklists, or gates. Apply them in proportion to the work.

## Understand First

Understand the problem and existing system before prescribing or changing a solution. Inspect the product's actual behavior and relevant code paths. Understand the state, data, interfaces, dependencies, tests, and conventions that matter to the change. Distinguish verified facts from assumptions. Follow existing patterns unless there is a meaningful reason to change them; do not redesign surrounding systems merely because another design appears cleaner.

## Fewest Changes

Make the smallest coherent change that solves the problem. This does not mean minimizing lines, files, or layers. A functioning vertical slice may cross UI, backend, persistence, infrastructure, or other boundaries. Prefer the minimum connected set of changes needed to create functioning software someone can evaluate.

Avoid unrelated cleanup, speculative features, premature abstractions, and “while we’re here” expansion. Apply YAGNI where useful. Separate genuinely independent prerequisite work when it creates a useful, verifiable change. Favor changes that can be independently understood, reviewed, reverted, released, and learned from.

## Optimize for the Reader

Make code's intent easy for the next human or AI to understand. Prefer clear names, straightforward control flow, focused responsibilities, and local conventions. Use abstractions when they meaningfully reduce complexity. Explain why when the code alone cannot. Prefer explicit code over clever code and reduce cognitive load. Do not impose rigid rules for line counts, function sizes, class structures, or programming paradigms.

## Better Than Before

Leave the affected system at least as understandable and maintainable as before, without pursuing perfection or broad cleanup. Remove accidental complexity introduced by the change and refine rough prototype code before treating it as production code. Fix nearby problems when they directly interfere with the change or its comprehensibility; leave unrelated debt for separate work. Favor incremental improvement over idealized redesign.

## Close the Loop

Verify the change as an integrated piece of software rather than stopping at generated code. Run appropriate automated checks; add or update tests when they meaningfully protect behavior. Verify integrated behavior in the running product when feasible, and inspect important failure and edge cases in proportion to the change. Distinguish implementation, verification, deployment, and live validation. Incorporate meaningful learning into the current understanding of the work.
