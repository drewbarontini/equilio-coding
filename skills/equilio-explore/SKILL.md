---
name: equilio-explore
description: Test meaningful software product or implementation options in a running product; use when behavior, design, UX, or technical tradeoffs need evidence before choosing a direction.
---

# Explore

Establish the current problem and available context from the issue, local Markdown, prototype, or code. Name the question whose answer would distinguish viable options. Choose a small number of meaningfully different options; do not produce variations merely for volume.

Prototype in the running product when feasible, using the lightest reversible change that exposes actual behavior and experience. Observe rather than infer how each option affects users, design, UX, and implementation. When a running prototype is impractical, state the constraint and use the closest useful evidence. Keep observations, tradeoffs, and decisions in local Markdown so the user can inspect them.

Choose a direction when evidence supports one; otherwise identify the next discriminating test and leave the choice open. Update the project's GitHub, Linear, or local Markdown issue with observations, the decision and its reason, or the remaining open question, after establishing its destination. Summarize; do not paste a transcript or the entire working file. Leave enough context for a teammate or a new agent session to continue.

Use what the prototypes show to identify the smallest functioning delivery slices. For each proposed slice, say what people can do or experience, which parts must work together, who can evaluate it, how feedback can be gathered, and what remains to learn. Prefer a slice that can go live independently; name any dependency that prevents this. A slice need not fulfill the broader vision, but it should create a real opportunity for user feedback, observed behavior, or a meaningful product demonstration. Keep choices open where the needed evidence is still missing.

A single issue can carry an ordinary change. For a broader problem, an optional parent can hold shared intent and exploration while linked delivery issues each carry their own outcome. Treat planned feedback as a plan, not an observation.

Before finishing, re-read the shared issue and write all material observations, tradeoffs, decisions, and next tests back into its current account. Update superseded assumptions, preserve deferred questions, and leave enough context for Build or another exploration pass to continue from the issue. Follow the [issue write-back contract](https://github.com/drewbarontini/equilio-coding/blob/main/references/issue.md#issue-write-back-contract).
