<!-- Generated from references/agent-handoffs.md; edit the source and run scripts/sync-references.py. -->

# Agent handoffs

Read for a handoff to another agent or authorized multi-agent work; apply the shared [work-artifact contract](work-artifact.md) throughout.

Before handing work to another agent, reconcile the owning artifact and make the relevant code, prototype, and evidence accessible. Give the receiving agent the artifact location, intended outcome, scope boundaries, relevant branch or checkout, and the next useful action with its reason. Identify unresolved decisions and verification limits where they affect that action. Use existing task context and links; no separate handoff document or issue section is required.

The receiving agent reads the latest artifact and inspects relevant actual state before continuing. A prior summary is an orientation aid, not proof that the issue, code, or verification still matches. Preserve the user's scope and authorization; a handoff does not grant additional permissions.

When multiple agents are authorized and useful, agree on one active writer for each shared artifact. Other agents return findings and proposed revisions to that writer, who owns synthesis and verified write-back before work proceeds on changed understanding. Give each assignment a bounded outcome, relevant dependencies, and clear edit ownership; serialize overlapping edits unless the agents have explicitly coordinated them. Separate assignments need not create separate delivery issues.

Returned work should identify what changed in understanding, the evidence and code state supporting it, and what remains unresolved. The coordinating agent inspects the returned artifacts and resolves contradictions against evidence. For implementation work, verify the combined behavior; passing isolated checks does not establish integration. Preserve material unresolved disagreements in Reality and seek human judgment when evidence cannot settle a consequential choice.

Immediately before writing, re-read the destination and incorporate intervening human or agent edits, preserving source wording under the [original-request rule](work-artifact.md#preserve-the-original-request). Use revision checks when available; if the destination changed or an update conflicts, reconcile against its latest version instead of overwriting from a stale draft. Keep consequential meaning in the five coordinates within their budget, with durable links for supporting evidence; do not append agent reports or a coordination log.
