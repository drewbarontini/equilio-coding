# Example: reliable, understandable digest control

This fictional example uses illustrative issue numbers and observations. It shows successive rewrites of **the same #143 artifact**, with its Original Request preserved verbatim beneath the five coordinates. The stage labels belong to this teaching example only. All five concerns are useful here; other work may skip satisfied concerns.

## Frame

Existing issue #143 says: “People keep getting weekly digests after turning them off. Add an unsubscribe button.” One substantive question establishes three support reports. The agent reflects that preventing later sends matters more than the exact control, and the person agrees; the shared problem is reliable stopping, while the solution remains open. The local draft updates #143 while preserving its existing description outside the word budget:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** Three people report receiving digests after disabling them in Settings; the cause is unknown.

**Expected:** People can stop future digests and understand when their choice takes effect.

## Solution

Direction not chosen. An unsubscribe button is proposed, but easier access may not solve unwanted sends.

## Decisions

No implementation direction chosen yet.

## Impact

The relationship between the saved preference and queued sends is not yet understood.

## Reality

- **Evidence:** Support reports establish the symptom.
- **Unknown:** Preference persistence, send eligibility, and the provider's recall boundary remain unverified.

---

## Original Request

People keep getting weekly digests after turning them off. Add an unsubscribe button.
```

## Map

Inspection and reproduction show that Settings saves correctly. The batch snapshots recipients on Sunday, and the worker sends Monday without checking the latest preference. Detailed code paths stay in working notes. The agent replaces #143's body:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** Reproduction confirms the worker sends from a Sunday recipient snapshot despite later opt-outs; saving the preference works.

**Expected:** Disabling the digest should prevent sends we still control, with understandable timing.

## Solution

Proposed: recheck the saved preference before sending and clarify Settings copy. This direction still needs a focused test.

## Decisions

No final solution choice yet.

## Impact

The batch currently determines final send eligibility; Settings changes cannot affect its queued recipients. A functioning fix must connect the preference, worker, and timing explanation.

## Reality

- **Verified:** Preference persistence and stale batch behavior were reproduced in the test product.
- **Unknown:** Provider behavior after acceptance and customer outcomes remain unverified.

---

## Original Request

People keep getting weekly digests after turning them off. Add an unsubscribe button.
```

## Explore

The uncertainty is whether a different control is needed to stop queued sends. The working belief is that a send-time preference check can make existing Settings reliable; if the trial still sends after opt-out, that belief needs revision. If the check skips the send through existing Settings, an additional control is unnecessary for this outcome.

The agent builds reversible prototypes in the test product and exercises the Settings flow in the browser. Each test-account trial queues a digest, saves an opt-out, and runs the worker. Changing the control alone leaves the send intact; a send-time check skips it, and a direct email-to-Settings route also works with that check. The observed skip supports the check and retaining the existing control; the working email route establishes feasibility while leaving its customer need unresolved.

The person receives the runnable test product and the same short trial, with the worker's send or skip as the result to inspect. Provider recall is outside this prototype. These are agent prototype observations, not human testing or customer feedback; #143 is rewritten before proceeding on the supported direction:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** A saved opt-out does not stop a digest already in the recipient batch, undermining trust in Settings.

**Expected:** Opting out should stop future sends before provider acceptance and explain the remaining boundary.

## Solution

Chosen direction: check the current preference before each send and update Settings copy. Production implementation is not complete.

## Decisions

- **Check at send time:** This is the last boundary we control before provider acceptance; changing the control alone did not stop queued sends.
- **Keep the existing control:** The check stopped queued sends through Settings, so an additional control is unnecessary for reliable stopping.
- **Separate direct access:** An email-to-Settings route is a candidate slice whose need depends on real-use feedback.

## Impact

Final eligibility would move from the batch snapshot to the worker. The snapshot would select candidates; the current preference would authorize each send.

## Reality

- **Observed:** The check skipped queued sends through existing Settings; the email route also worked with a test account.
- **Unknown:** Provider recall remains unverified and customer feedback is unavailable.
- **Related work:** Project #142 coordinates this slice and proposed #144.

---

## Original Request

People keep getting weekly digests after turning them off. Add an unsubscribe button.
```

The team shapes the work using [Surface → Structure → Slice → Simplify → Sequence](../references/delivery-slices.md#shape-delivery-slices), keeping the detailed map in working notes:

- **Surface:** Preference persistence, queued sends, provider acceptance, timing copy, and direct access are the relevant concerns.
- **Structure:** Reliable stopping connects the saved preference, worker eligibility, and the explanation people see.
- **Slice:** #143 lets someone stop future digests using existing Settings even if no further work follows; worker and copy changes belong together.
- **Simplify:** Keep the existing control and defer the email-to-Settings route; provider recall is outside the prevention boundary.
- **Sequence:** Release reliable stopping first; evaluate direct access only if later evidence supports it.

The team links #143 to [project #142](#project-142) and an illustrative [proposed delivery #144](#proposed-delivery-144). #144 would depend on #143 being released, but could then provide useful access without another future slice. Worker and copy tasks can be implemented separately within #143; deploying the worker behind a disabled flag would be preparation, with no change to the experience yet.

## Agent handoff

If the team authorizes two build agents, one can implement the worker check and regression test while the other refines Settings copy. Their assignments point to #143 and the relevant checkout, name the prevention boundary, and avoid overlapping edits; both are build units within #143. The coordinating agent is the only writer of #143 while they work.

Suppose the copy agent proposes “stops all queued emails,” while the worker agent reports that provider-accepted emails cannot be prevented by this check. The coordinator inspects the evidence and reconciles the wording to promise prevention before acceptance, leaving recall unverified in Reality. Separate successful checks do not resolve this contract mismatch.

The next agent reads the reconciled #143, inspects the assembled code, and uses linked test and prototype evidence to choose the next action. It does not need either agent's full conversation or a new handoff artifact; the integrated walkthrough still needs to establish that behavior and copy agree.

## Build

The worker and Settings now work together. A regression test changes the preference between batch creation and sending; a product walkthrough checks saved state and copy. #143's body is replaced again:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** Queued digests previously ignored opt-outs saved after batch creation, causing the reported unwanted sends.

**Expected:** Disabling the digest should stop sends before provider acceptance, with clear timing in Settings.

## Solution

The worker now reads the current preference before each send and skips disabled recipients. Settings explains that disabling stops future sends.

## Decisions

- **Check at send time:** Eligibility must reflect current intent at the last boundary we control.
- **Keep the existing control:** Prototype opt-outs through Settings stopped queued sends with the check.
- **Keep direct access separate:** #144's email-to-Settings journey can be evaluated independently after reliability improves.

## Impact

The batch selects candidates; the worker owns final eligibility. Settings promises prevention before acceptance rather than recall afterward.

## Reality

- **Verified:** The batch-to-send regression test and integrated walkthrough passed.
- **State:** Implemented; not merged, deployed, or verified live.
- **Limit:** Provider recall remains unknown and customer feedback is unavailable; #142 retains the broader effort.

---

## Original Request

People keep getting weekly digests after turning them off. Add an unsubscribe button.
```

## Integrate

Review checks the whole slice and asks whether it can solve the same problem more simply. A redundant eligibility wrapper left from the prototype is removed; the worker retains the send-time check, and the regression test still passes. Impact preserves the distinction between batch candidates and the worker's final eligibility decision.

The requested outcome is reliable stopping before provider acceptance with understandable timing; it does not require the unproven email route or provider recall. The regression test and integrated walkthrough support review readiness, and no concrete gap justifies another refinement pass. Delivery and live verification remain separate work under the team's authorization. All five sections are reconciled against the refined behavior before the PR follows [the canonical guidance](../references/pull-request.md):

```markdown
## Summary

Turning off the weekly digest now prevents future sends, including sends from an existing batch. Settings explains when the choice takes effect.

[Delivery issue #143](#integrate)

## Changes

- **Send eligibility:** The worker checks the saved preference before each send, including recipients already in a batch.
- **Settings:** The copy promises to stop digests only before the email provider accepts them.

## Callouts

- **Provider limit:** Recalling accepted emails remains unverified; check that Settings promises only to prevent sends before acceptance.
```

The plain link in Summary keeps #143 open for delivery and live verification. It points to this illustrative record rather than a fictional remote issue. Review-ready does not mean deployed.

Later, the team explicitly authorizes merge and deployment. A live test account opts out after entering the batch, receives no digest, and has a confirmed worker skip. Only then is Reality updated and #143 closed. The final five coordinates stay within the 250-word maximum and section limits; Original Request remains unchanged:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** Three support reports described unwanted digests after opt-out because queued sends used an earlier recipient snapshot despite correctly saved preferences.

**Expected:** Disabling the digest should prevent sends before provider acceptance, with clear timing in Settings.

## Solution

The worker checks the current preference before each send and skips disabled recipients, including those already batched. Settings explains the prevention boundary.

## Decisions

- **Check preference at send time:** Changing the control alone left queued sends intact in prototypes.
- **Keep the existing control:** Prototype opt-outs through Settings stopped queued sends with the check.
- **Keep direct access separate:** #144's email-to-Settings journey can be evaluated independently if customer feedback supports it.

## Impact

The batch selects candidates; the worker owns final eligibility using current intent. Future batching changes must preserve that boundary, and Settings copy must match it.

## Reality

- **Verified:** Regression coverage and the integrated walkthrough passed; after merge and customer deployment, a live account opted out from an existing batch with a confirmed skip.
- **Limit:** Provider recall remains unverified and is not promised.
- **Observation:** No customer feedback yet; next-cycle send/skip counts and support reports can inform #142 and proposed #144.

---

## Original Request

People keep getting weekly digests after turning them off. Add an unsubscribe button.
```

Explain could teach the changed eligibility model. The final Impact already preserves that durable change, so teaching it again would not require another write-back.

## Project #142

**Same questions. Different resolution.** The project's current artifact retains the broader coordinated effort without aggregating #143's implementation reasoning:

```markdown
# #142 — Reliable digest control

## Problem

**Current:** People reported unwanted digests after opting out; difficulty reaching the control may also contribute, but that is not established.

**Expected:** People can reliably stop digests and find the control when needed.

## Solution

#143 delivers reliable stopping. Proposed #144 adds direct access from an email only if real-use evidence supports it.

## Decisions

- **Reliability first:** Easier access cannot compensate for an opt-out that queued sends ignore.

## Impact

Digest control connects saved intent, delivery eligibility, and understandable access. The linked delivery issues retain their own system details.

## Reality

- **Verified:** #143 is verified live; broader customer outcomes remain unknown.
- **Observation:** The next weekly cycle's operational signals and support reports can inform whether direct access warrants delivery.
```

## Proposed delivery #144

This artifact stays open while evidence develops; Reality does not require a new backlog by default:

```markdown
# #144 — Open the digest setting from an email

## Problem

**Current:** Whether people struggle to find the control remains an assumption.

**Expected:** If access is a meaningful gap, an email should lead people to the exact setting and its current state.

## Solution

Proposed: a direct route through sign-in to the digest preference. Not implemented.

## Decisions

No delivery commitment; wait for evidence from #143's real use.

## Impact

The email-to-Settings journey would connect authentication, navigation, and preference state. Reliable stopping depends on #143.

## Reality

- **Observed:** A prototype reached the setting with a test account.
- **Unknown:** Customer need and reduced confusion remain unverified; project #142 coordinates evaluation.
```

If feedback supports direct access, the team can build and evaluate #144 independently. Otherwise it can reshape or close the proposal with appropriate authorization. These records replace earlier understanding; they do not retain the teaching example's workflow history.
