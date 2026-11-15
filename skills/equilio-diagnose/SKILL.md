---
name: equilio-diagnose
description: Reproduce, isolate, and explain a difficult software bug or regression with evidence before choosing a fix. Use when the failure mechanism is uncertain; Build implements the chosen correction.
---

# Diagnose

Use Diagnose as a standalone **Supporting Skill** when a bug or regression cannot yet be explained confidently. Its job is to establish **what fails, under which conditions, and why**—not to implement the final fix. A straightforward, already-understood defect can go directly to Build. Map traces the affected system; Explore tests uncertain product directions; Diagnose tests competing explanations of an observed failure.

Read the current owning work artifact when available, following the [work-artifact contract](references/work-artifact.md) and [Development Principles](references/development-principles.md). Use the existing issue or local Markdown; do not create a second bug artifact or require a new issue. Preserve observed symptoms, affected behavior, and available evidence separately from assumptions.

## Establish a trustworthy failing signal

Identify the expected behavior, actual symptom, environment, relevant versions or inputs, and the smallest reliable observation that distinguishes failure from success. Inspect existing tests, logs, traces, reports, and code paths before adding instrumentation. Prefer a safe, fast, repeatable failing test or minimal reproduction. Record exact setup, command or interaction, expected and actual result, and repeatability. Use a controlled environment and synthetic or sanitized data where possible; do not expose secrets or alter production data to reproduce a bug. Inspect commands before executing them, avoid destructive operations, and obtain approval for consequential external actions.

If the failure is intermittent, characterize frequency and relevant timing, concurrency, or environment variables instead of calling a single pass a fix. If it cannot be reproduced, preserve the strongest observable signal and missing conditions; do not manufacture a failing test.

## Isolate and challenge explanations

Trace the symptom backward through affected responsibilities, boundaries, state, inputs, and dependencies. Use Map when the system path itself is unclear. Form a small set of competing causal hypotheses with a predicted observation that would distinguish each one. Change one meaningful condition at a time where feasible; use targeted tests, instrumentation, logs, history, or controlled comparisons to eliminate alternatives. Keep a clear boundary between observation, inference, and established cause. Do not patch around the symptom or modify tests to force a passing result.

Stop when evidence sufficiently identifies the mechanism and scope for a responsible fix, or when the next discriminating observation is blocked. Avoid indefinite investigation and speculative rewrites.

## Verify and hand off

Recommend the smallest coherent correction and the relevant Core Skill—usually Build—for implementation. A diagnosis may include a temporary probe or reproduction test, but must not silently ship a speculative production fix. After a fix is made, rerun the original failing signal and relevant regression or integration checks; distinguish an observed pass from proof of root cause, and investigate contradictory results. If asked to implement as well, invoke or follow Build and Integrate rather than duplicating their responsibilities.

Provide a compact handoff: **symptom and conditions → reproduction or evidence → causal explanation and alternatives ruled out → proposed correction → verification and remaining uncertainty**. Reconcile material learning into the existing Problem, Decisions, Impact, and Reality coordinates within their limits; keep exhaustive logs in temporary working notes. Without an owning artifact, return the handoff without creating a new permanent record by default. Never claim a fix is verified before running its checks.
