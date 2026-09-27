# Example: reliable, understandable digest control

This fictional example starts with one broad problem, then creates two linked functioning delivery issues after mapping and prototyping. The issue numbers and observations are illustrative. The first slice reaches a live test and becomes available to customers; the second remains open. No customer response is assumed.

## Frame → a local draft and a parent

Request: “People keep getting weekly digests after turning them off. Add an unsubscribe button.”

The agent asks one question at a time, starting with what has been seen. The user cites three support reports this week, each after someone turned the digest off in Settings. The agent reflects two possible causes: the setting may fail to save, or a queued send may ignore it. The user confirms that preventing later sends matters more than the exact control. The agent stops interviewing and writes a local Markdown draft:

> **Problem:** People report receiving a weekly digest after disabling it in Settings. Three support reports are known; the cause is not.
>
> **Desired outcome:** People can reliably stop future digests and understand when their choice takes effect.
>
> **Proposal to test:** An unsubscribe button may make the choice easier to reach, but it might not stop a queued send.
>
> **Open questions:** Does the setting persist? When is the recipient list frozen? Can the mail provider recall an accepted message?

After reviewing the draft, the team chooses GitHub Issues as its shared destination and creates parent **#142, Reliable digest control**. It holds the broader problem, evidence, desired outcome, and open exploration. No delivery breakdown is fixed yet. The local draft and later prototype notes remain working material.

## Map → the system boundary

The agent reproduces the report and inspects the running product and code. Settings saves the digest preference to the profile. The weekly job snapshots eligible recipients on Sunday. The worker sends the batch on Monday without checking the latest preference. The setting persists correctly; the send path is the gap. The mail provider's behavior after accepting a message remains unknown.

The local map links the Settings control and save handler, profile data, batch builder, mail worker, and email template. Parent #142 gains the verified finding and the unresolved provider question. Mapping shows that a functioning stop action must connect the preference, worker, and customer-facing explanation. A worker-only or UI-only issue would leave the experience incomplete.

## Explore → choose a direction and two slices

The agent tries three reversible variants with test accounts after the Sunday batch has been created:

| Variant | Observed in the test product |
| --- | --- |
| A one-click email button updates the preference; the worker uses the Sunday batch | The preference changes, but Monday's mail still sends. |
| The existing Settings control saves the preference; the worker rechecks it before sending | The queued send is skipped. Settings needs clear timing copy. |
| A direct email link opens the specific Settings control, with the same send-time check | The queued send is skipped, and the test account can see the current state before changing it. |

These are test-account observations, not customer feedback. The team chooses a send-time check with accurate Settings copy first. The direct email path is a candidate follow-up whose need still requires feedback from real use. The provider recall question remains open. The parent records the decision and links to the curated exploration note.

The team now links two delivery issues to parent #142:

| Delivery issue | Functioning outcome | Evaluation and remaining question |
| --- | --- | --- |
| **#143, Turning the digest off stops future sends** | A person turns the digest off in Settings; the saved preference is rechecked before each send, and Settings explains the effect. This crosses the UI, profile, batch/worker, and copy boundaries. | Release independently to an appropriate audience. Verify the batch-to-send boundary with a live test account, then watch send/skip counts and support reports. Will real use confirm the reports stop? |
| **#144, Open the digest setting from an email** | A person follows a link in the email, signs in if needed, lands on the exact preference, sees its current state, and can change it. This crosses email, routing/authentication, Settings, and profile update behavior. | Keep this proposed slice open while #143 gathers feedback. If access remains a problem, release it after #143 and test the full journey. Does direct access reduce confusion? |

Each issue has an experience someone can evaluate. #144 has a named dependency on the verified behavior of #143, yet it can be deployed as its own release if feedback warrants it. Neither issue is a frontend or backend task disguised as a slice. Parent #142 keeps the broader aim; each delivery issue owns its own lifecycle and links back to #142 without repeating it.

## Build → #143 implemented

The worker now reads the current preference before each send. Settings copy says disabling the digest stops future sends; it does not promise recall after provider acceptance. The team tests a preference change between batch creation and sending and walks through the experience with a test account. Issue #143 records the behavior, verification, code links, and remaining provider boundary as **implemented**. It does not claim a release or feedback yet. Issue #144 remains open as a proposed slice with an intended experience and test plan.

## Integrate → #143 live, #144 open

The review checks the Settings control, saved state, worker decision, and copy together in the running product. The PR advances #143 and stays concise:

```markdown
## Summary

Turning off the weekly digest now prevents future sends, including sends from
an existing batch. A batch-to-send test and a product walkthrough verified the
integrated behavior.

## Callouts

- **Provider boundary:** The worker can stop a send before provider acceptance;
  it cannot recall mail already accepted by the provider.

## Context

[Delivery issue #143](ISSUE_URL) — problem, exploration, decisions, and outcome.
```

After merge and deployment, a live test account in a batch disables the digest and receives no digest. The team confirms the worker skipped that send. Issue #143 is marked **verified live** and links the PR, release, and durable exploration note. The change is available to customers, so feedback can now arrive. The issue distinguishes the verified test from **planned feedback**: watching the next weekly cycle's send/skip counts and support reports. It records **observed feedback: none yet** and avoids inferring that the broader problem is solved from one test.

The completed #143 issue gives a newcomer the account in one place:

> **#143 — Verified live.** Three reports of unwanted digests led us to inspect the save and send paths. The preference saved, but the worker used a Sunday recipient snapshot without rechecking it. In test accounts, changing the preference alone did not stop the queued send; rechecking it did. We added that check and clear Settings copy, tested the batch-to-send boundary, and verified a skipped send with a live test account after deployment. The change is available to customers. See the linked PR, release, and curated exploration note. Planned feedback: review send/skip counts and support reports after the next weekly cycle. Observed customer feedback: none yet. We still do not know whether the provider can recall accepted mail.

Parent #142 notes that the first slice is live and #144 remains open. If the next cycle shows people still struggle to find or change the setting, the team can build and evaluate #144's email-to-Settings journey. If it does not, the team can reshape or close #144. The completed #143 issue remains the useful record for that slice, while the parent connects it to the broader problem.
