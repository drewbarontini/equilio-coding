# Correct the file-count label

## Problem

**Current:** The label says "0 file" and "2 file" because it always uses the singular noun.

**Expected:** Use "1 file" for one file and the plural noun for other counts.

## Solution

Correct the noun selection in the existing label function.

## Decisions

Keep the public function and English wording because callers already use them.

## Impact

The label's public input and output type stay the same.

## Reality

The existing tests cover zero, one, and multiple files; the fix has not been verified.

---

## Original Request

The file-count label needs to say "2 files", not "2 file". Keep "1 file" and fix zero too.
