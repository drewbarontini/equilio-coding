# Respect digest opt-outs after batching

## Problem

**Current:** Digests still reach people who disable them after entering the recipient batch.

**Expected:** Disabling digests should stop sends that have not reached the provider.

## Solution

Proposed: rebuild queued recipient lists whenever preferences change. No fix has been implemented.

## Decisions

Rebuilding the batch on preference changes is a candidate approach; the choice remains open pending code inspection.

## Impact

The queue selects recipients from saved preferences; delivery currently trusts that earlier selection.

## Reality

Existing tests cover initial selection and successful sending; changes after batching are not covered.

---

## Original Request

Please stop sending queued digests to people who have since opted out.
