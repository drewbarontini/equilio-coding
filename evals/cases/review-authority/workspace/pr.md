# PR #41 — Show clearer title errors

Local review snapshot, no remote access. `base/` and `head/` contain the supplied comparison states; the original Git object IDs and live thread state were not exported. `change.patch` contains the full changed-file diff; other supplied files provide surrounding context.

## Summary

Prevent people from submitting empty task titles and show the error next to the field.

## Changes

- Move the blank-title check to the form so invalid requests are caught before sending.

Linked work: issue.md. Existing architecture: SYSTEM_MODEL.md.

The author reports that the form test passes. CI and review conversations were not exported.
