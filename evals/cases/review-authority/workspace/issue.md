# Blank task titles

## Problem

**Current:** Blank titles cause a generic save error in the task form.
**Expected:** People see a clear error beside the title field.

## Solution

Show an inline error before sending blank titles. The existing API should continue to reject invalid titles.

## Decisions

No change to API validation responsibility was requested.

## Impact

The form adds feedback; API callers retain the same contract.

## Reality

Author reports one form test passes; API caller behavior has not been checked.
