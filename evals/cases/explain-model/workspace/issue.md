# Respect digest opt-outs after batching

## Problem

**Current:** People can receive a digest after opting out because the batch captured their earlier preference.

**Expected:** Opting out before sending should prevent the digest.

## Solution

Proposed: check the current preference before each send.

## Decisions

Check at send time because the saved preference can change after batching.

## Impact

The batch owns final send eligibility.

## Reality

Not yet verified.

---

## Original Request

Please stop sending queued digests to people who have since opted out.
