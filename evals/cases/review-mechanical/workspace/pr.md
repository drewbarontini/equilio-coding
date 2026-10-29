# PR #52 — Cache release metadata

Offline snapshot. The complete changed files are in `base/` and `head/`; `change.patch` is their diff. Source revision IDs, CI results, linked issue, and thread export are unavailable.

Allow shared caches to retain public release metadata for one minute. The response body and status should stay the same. Regenerated catalog entries use the current generator version; the generator changes only the generator field in each entry.

Author reports `python3 -m unittest discover -v` passes. No live cache has been exercised.
