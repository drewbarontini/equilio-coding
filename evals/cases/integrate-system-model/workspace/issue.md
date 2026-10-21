# Faster task notifications

## Problem

**Current:** Notifications are processed after task updates, which may delay when collaborators see changes.

**Expected:** Collaborators should see task notifications sooner.

## Solution

Proposed: call notification delivery during the task update. The implementation in after.py is ready for assessment.

## Decisions

No architecture change has been chosen; immediate delivery is a proposal.

## Impact

Registry records activity for Relay; notification delivery currently happens outside the task update.

## Reality

The supplied successful-notification test passes; no deployment or real provider has been checked.
