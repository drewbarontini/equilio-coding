# Webhook retries

## Problem

**Current:** Duplicate provider events send duplicate notifications.
**Expected:** Successful delivery suppresses duplicates while failed delivery can be retried.

## Solution

Deduplicate using the provider event identifier.

## Decisions

Only successful notification delivery may mark an event completed; durable cross-worker deduplication is outside this single-worker change.

## Impact

The webhook handler owns the local completed-event set and calls the notification boundary.

## Reality

Local happy-path tests were reported passing; provider failure and live retries remain unverified.
