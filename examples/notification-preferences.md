# Example: a preference that does not stick

This fictional example follows **the same issue, #142**, from a rough report to a verified live change. Local Markdown is working material; the issue carries the accepted account. The amount of exploration here fits a behavior change with a real UX choice. A simpler fix could use much less.

## Rough problem → local draft

Request: “People keep getting weekly digest emails after turning them off. Add an unsubscribe button.”

The request already says what happens and proposes a fix, so the agent asks only for missing evidence: “What have you seen about when people turned it off and when the digest arrived?” The user cites three support reports this week, all involving a switch in Settings before the next delivery. That makes the timing matter. The agent reflects that the setting might fail to save or the send path might use an older value, and invites correction. The user confirms that stopping later sends matters more than the exact control used to turn them off. The agent stops interviewing and writes `work/digest-preferences.md` as an inspectable draft:

```markdown
# Weekly digest preference

Support has three reports this week of digests arriving after people switched
the digest off in Settings. We do not yet know whether the setting fails to
save, the sender ignores it, or scheduled mail is already queued.

Affected: people receiving the weekly digest; support handling repeat reports.
Desired outcome: switching it off prevents future digests, and the interface
accurately explains when that takes effect.
Proposed solution: add an unsubscribe button. It may help people reach the
preference, but we do not yet know whether it stops a queued send.
Open for exploration: Should the experience use a one-click button or a link
to Settings, and where must the preference be enforced? Observe whether either
approach stops a later digest after someone turns the setting off.
Questions: Where is the preference stored? When is the recipient list frozen?
```

The draft keeps the suggested button as a proposal. After reviewing it, the user chooses GitHub Issues as the shared destination. Issue **#142, first state**, carries the problem, evidence, desired outcome, proposal, and open exploration question in the same concise form. The local draft remains available for working notes.

## Map → revised issue

The agent reproduces the report and maps the current path in `work/digest-preferences.md`: Settings writes `digest_enabled` to the profile; the weekly job builds a recipient batch on Sunday; the mail worker sends that batch on Monday without rechecking the preference. The setting saves correctly. The map links the settings handler, batch builder, and mail worker and marks the mail provider's queued-message behavior as unknown.

Issue **#142, second state** now says:

```markdown
The setting persists, but the weekly job snapshots recipients before delivery.
The worker sends from that snapshot without checking the current preference.
An unsubscribe control could help access, but changing the stored preference
alone would not stop mail from an already-created batch. The one-click button
is still a proposal. Open for exploration: test the button alone, then both
controls with a send-time check. Observe what stops a send after batch creation
and what each interface can promise. The
provider's handling of accepted messages is still unknown.
```

## Explore → decision

The deciding questions are what stops a send from an existing batch and which control makes the preference's state clear. Three lightweight variants run against test accounts in the product after the Sunday batch is created:

| Option | Observed result |
| --- | --- |
| One-click unsubscribe button updates the preference; the worker uses the Sunday batch | The setting changes, but the account still receives Monday's mail. |
| One-click button plus a worker recheck before each send | The later send stops, but the email action gives no view of the current setting or when it takes effect. |
| Direct link to Settings plus the same worker recheck | The later send stops, and Settings shows the current state and its effect. The worker uses the existing profile lookup. |

The agent records the test setup, observations, and tradeoff in the local file. The team chooses the send-time check and a direct Settings link, revising the original button proposal. Issue **#142, third state** summarizes the variants, observed differences, and decision: the link shows the setting and its effect, while the recheck prevents the late send. It retains the question of whether messages already accepted by the provider can be recalled, and links the local findings rather than copying them.

## Build → implemented

The worker rechecks `digest_enabled` before sending, and the email links directly to the preference control. Settings copy says that disabling the digest stops future sends; it does not promise to recall mail already accepted by the provider. A test covers a preference change between batch creation and sending. The agent observes the change in a test account and updates issue #142 with the implementation and verification. Its status is **implemented**, not yet shipped.

## Integrate → PR → shipped issue

The review checks that the setting, link, worker, and copy tell the same story. After merge and deployment, a live test account is added to a batch, switches the digest off, and receives no digest. Issue **#142, final state** reads:

```markdown
# Turning off the weekly digest now prevents queued sends

Three support reports showed that people received a digest after disabling it.
The setting saved correctly, but recipients were selected on Sunday and the
Monday worker did not recheck the preference.

We tried a one-click button alone, then paired both the button and a Settings
link with a send-time check in test accounts. The button alone still allowed
mail from Sunday's batch; either recheck stopped the send. The link also showed
the current state and its effect, so we chose it with the send-time check. The
interface describes future sends without
promising recall of mail already accepted by the provider.

The worker now checks the latest preference before sending. The change was
tested across the batch/send boundary, reviewed in the running product, merged,
deployed, and verified live with a test account. See [the PR](PR_URL) for the
[worker change](CODE_URL) and checks, [the curated exploration note](EXPLORATION_URL)
for detailed observations, and [the mail delivery diagram](DIAGRAM_URL) for the current flow. The release is recorded at
[the deployment](RELEASE_URL). Watch support reports and send/skip counts in
the next weekly cycle; the provider recall question remains open.
```

The PR stays short:

```markdown
## Summary

The weekly digest worker now checks the current preference before sending, and
the email links directly to that setting. A batch/send boundary test and a
test-account walkthrough verified the behavior.

## Callouts

- **Provider boundary:** The new check prevents sends before provider acceptance;
  it cannot recall a message the provider already accepted.

## Context

[Source issue](ISSUE_URL) — problem, exploration, decisions, and full outcome.
```

The curated exploration note is a durable artifact made from the accepted findings in `work/digest-preferences.md`; the local scratch file is not assumed to be accessible from GitHub. For GitHub, the PR's `ISSUE_URL` would be replaced with #142's URL. Because this deployment and live check happen after merge, the PR does not close the issue on merge. The issue's live outcome is added only after live verification.
