# Example: reliable, understandable digest control

This fictional example uses illustrative issue numbers and observations. It shows successive replacements of **the same #143 artifact**, not sections appended to an issue. The stage labels belong to this teaching example only. All five concerns are useful here; other work may skip satisfied concerns.

## Frame

Request: “People keep getting weekly digests after turning them off. Add an unsubscribe button.” One substantive question establishes three support reports. Preventing later sends matters more than the exact control. The local draft becomes delivery issue #143 in the team's chosen destination:

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

Support reports establish the symptom. Preference persistence, send eligibility, and the provider's recall boundary remain unverified.
```

## Map

Inspection and reproduction show that Settings saves correctly. The batch snapshots recipients on Sunday, and the worker sends Monday without checking the latest preference. Detailed code paths stay in working notes. The agent replaces #143's body:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** The worker sends from a Sunday recipient snapshot even when someone disables the digest before Monday's send. Reproduction confirms the reported gap; saving the preference works.

**Expected:** Disabling the digest should prevent sends we still control, with understandable timing.

## Solution

Proposed: recheck the saved preference before sending and clarify Settings copy. This direction still needs a focused test.

## Decisions

No final solution choice yet.

## Impact

The batch currently determines final send eligibility; Settings changes cannot affect its queued recipients. A functioning fix must connect the preference, worker, and timing explanation.

## Reality

Persistence and the stale batch behavior are verified in the test product. Provider behavior after message acceptance remains unknown; no customer outcome is established.
```

## Explore

Reversible test-account trials show that changing the control alone leaves queued sends intact. A send-time check skips the queued send; a direct email-to-Settings route also works with that check. These are prototype observations, not customer feedback. #143 is rewritten:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** A saved opt-out does not stop a digest already in the recipient batch, undermining trust in Settings.

**Expected:** Opting out should stop future sends before provider acceptance and explain the remaining boundary.

## Solution

Chosen direction: check the current preference before each send and update Settings copy. Production implementation is not complete.

## Decisions

- **Check at send time:** This is the last boundary we control before provider acceptance; changing the control alone did not stop queued sends.
- **Separate direct access:** An email-to-Settings route is a candidate slice whose need depends on real-use feedback.

## Impact

Final eligibility would move from the batch snapshot to the worker. The snapshot would select candidates; the current preference would authorize each send.

## Reality

Test-account prototypes skipped queued sends with the check. Provider recall remains unverified. Customer feedback is unavailable. Project #142 coordinates this slice and proposed #144.
```

The team links #143 to [project #142](#project-142) and [proposed delivery #144](#proposed-delivery-144). Each slice crosses the layers needed for a functioning experience. #144 depends on #143's reliable send behavior but can release separately if evidence supports it; neither is merely a frontend or backend task.

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
- **Keep direct access separate:** #144's email-to-Settings journey can be evaluated independently after reliability improves.

## Impact

The batch selects candidates; the worker owns final eligibility. Settings promises prevention before acceptance rather than recall afterward.

## Reality

The batch-to-send regression test and integrated walkthrough passed. Implemented; not merged, deployed, or verified live. Provider recall remains unknown and is not promised. No customer feedback yet; #142 retains the broader effort.
```

## Integrate

Review reconciles all five sections against actual behavior and checks the whole slice. The PR follows [the canonical guidance](../references/pull-request.md):

```markdown
## Summary

Turning off the weekly digest now prevents future sends, including sends from an existing batch. Settings explains when the choice takes effect.

[Delivery issue #143](#integrate)

## Changes

- **Send eligibility:** The worker uses current preference state rather than treating the batch snapshot as final authorization.
- **Settings:** Preference copy reflects the send-time boundary and avoids promising recall.

## Callouts

- **Provider boundary:** No recall capability has been verified after provider acceptance; review the prevention promise against that limit.
```

The plain link in Summary keeps #143 open for delivery and live verification. It points to this illustrative record rather than a fictional remote issue. Review-ready does not mean deployed.

Later, the team explicitly authorizes merge and deployment. A live test account opts out after entering the batch, receives no digest, and has a confirmed worker skip. Only then is Reality updated and #143 closed. The final artifact is about 330 words:

```markdown
# #143 — Turning the digest off stops future sends

## Problem

**Current:** Three support reports described unwanted digests after people disabled them in Settings. The preference saved correctly, but queued sends used an earlier recipient snapshot and ignored subsequent opt-outs. This made the control unreliable at the moment people expected it to stop mail.

**Expected:** Disabling the digest should prevent future sends while they remain under our control, and Settings should explain when the choice takes effect.

## Solution

The worker reads the current saved preference immediately before each send and skips recipients who have disabled the digest, including those already in the batch. Settings explains that disabling stops future sends without promising recall of messages already accepted by the provider. The slice is deployed and available to customers.

## Decisions

- **Check preference at send time:** This is the last boundary we control before provider acceptance; changing the control alone left queued sends intact in prototypes.
- **Keep direct access separate:** #144's email-to-Settings journey addresses discoverability and can be released independently if real-use feedback supports it.

## Impact

The batch now selects candidates rather than granting final send eligibility. The worker owns that decision using current preference state. Future changes to batching or Settings must preserve this boundary: an earlier eligibility snapshot cannot override a later saved opt-out. Settings copy must match what the send path can actually prevent.

## Reality

- **Verified:** The batch-to-send regression test and integrated Settings walkthrough passed; review checked persistence, worker eligibility, and copy together.
- **Live:** After merge and deployment, a test account opted out from an existing batch; no digest arrived and the worker skip was confirmed.
- **Limit:** Provider recall remains unverified and is not promised. Prevention before acceptance is the supported behavior.
- **Planned observation:** Review send/skip counts and support reports after the next weekly cycle.
- **Feedback:** No customer feedback yet. The live test establishes this case, not resolution of every concern in project #142.
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

#143 is verified live. Broader customer outcomes remain unknown. The next weekly cycle's operational signals and support reports can inform whether direct access warrants delivery.
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

A prototype reached the setting with a test account. Customer need and reduced confusion remain unverified; project #142 coordinates evaluation.
```

If feedback supports direct access, the team can build and evaluate #144 independently. Otherwise it can reshape or close the proposal with appropriate authorization. These records replace earlier understanding; they do not retain the teaching example's workflow history.
