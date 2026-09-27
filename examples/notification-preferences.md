# Example: a preference that does not stick

This fictional example follows **the same issue, #142**, from a rough report to a verified live change. Local Markdown is working material; the issue carries the accepted account. The amount of exploration here fits a behavior change with a real UX choice. A simpler fix could use much less.

## Rough problem → local draft

Request: “People keep getting weekly digest emails after turning them off. Add an unsubscribe button.”

`work/digest-preferences.md` begins as an inspectable draft:

```markdown
# Weekly digest preference

Support has three reports this week of digests arriving after people switched
the digest off in Settings. We do not yet know whether the setting fails to
save, the sender ignores it, or scheduled mail is already queued.

Affected: people receiving the weekly digest; support handling repeat reports.
Desired outcome: switching it off prevents future digests, and the interface
accurately explains when that takes effect.
Proposed solution: add an unsubscribe link, but first check the send path.
Questions: Where is the preference stored? When is the recipient list frozen?
```

The draft challenges the request's solution without discarding it. The user chooses GitHub Issues as the shared destination. Issue **#142, first state**, carries the problem, evidence, desired outcome, and open questions in the same concise form. The local draft remains available for working notes.

## Map → revised issue

The agent reproduces the report and maps the current path in `work/digest-preferences.md`: Settings writes `digest_enabled` to the profile; the weekly job builds a recipient batch on Sunday; the mail worker sends that batch on Monday without rechecking the preference. The setting saves correctly. The map links the settings handler, batch builder, and mail worker and marks the mail provider's queued-message behavior as unknown.

Issue **#142, second state** now says:

```markdown
The setting persists, but the weekly job snapshots recipients before delivery.
The worker sends from that snapshot without checking the current preference.
An unsubscribe link would help access, but alone would not prevent mail from
an already-created batch. We need to decide where to enforce the preference
and what the interface should promise about queued mail.
```

## Explore → decision

Two lightweight variants run against test accounts in the product:

| Option | Observed result |
| --- | --- |
| Filter only when creating the Sunday batch | People who turn the digest off after the batch is made still receive Monday's mail. |
| Recheck immediately before each send | Turning it off after batch creation prevents a later send. The worker can use the existing profile lookup. |

The agent records the test setup, observations, and tradeoff in the local file. The team chooses a send-time check and an unsubscribe link that opens the same preference control. Issue **#142, third state** summarizes both options, the observed difference, the chosen path, and a remaining question: whether messages already accepted by the provider can be recalled. It links the local findings rather than copying them.

## Build → implemented

The worker rechecks `digest_enabled` before sending, and the email links directly to the preference control. Settings copy says that disabling the digest stops future sends; it does not promise to recall mail already accepted by the provider. A test covers a preference change between batch creation and sending. The agent observes the change in a test account and updates issue #142 with the implementation and verification. Its status is **implemented**, not yet shipped.

## Integrate → PR → shipped issue

The review checks that the setting, link, worker, and copy tell the same story. After merge and deployment, a live test account is added to a batch, switches the digest off, and receives no digest. Issue **#142, final state** reads:

```markdown
# Turning off the weekly digest now prevents queued sends

Three support reports showed that people received a digest after disabling it.
The setting saved correctly, but recipients were selected on Sunday and the
Monday worker did not recheck the preference.

We tried filtering only during batch creation and rechecking at send time in
test accounts. The first still sent to people who opted out after Sunday; the
second stopped the send. We chose the send-time check and added a direct
preference link in the email. The interface describes future sends without
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

The curated exploration note is a durable artifact made from the accepted findings in `work/digest-preferences.md`; the local scratch file is not assumed to be accessible from GitHub. For GitHub, the PR's `ISSUE_URL` would be replaced with #142's URL, and issue-closing syntax can be used if closing on merge fits the team's release flow. The issue's live outcome is added only after live verification.
