# Review at r2

- T1: Payload logging includes customer email; redact it.
- T2: Ensure retries after notifier failure can deliver; do not mark completion before success.
- T3: Missing event identifiers must be rejected rather than deduplicated as None.
- T4: Successful duplicate requests must not call notify twice.

This document records requests, not proof they were addressed. r2 code was not included in the export.
