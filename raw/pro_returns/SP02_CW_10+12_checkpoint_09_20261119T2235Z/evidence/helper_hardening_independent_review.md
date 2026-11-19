# Independent helper hardening review

Reviewed: 2026-11-19 21:07:13 UTC. This was a separate static code/evidence review followed by a parent check of the cited branches. No optional tests were rerun.

## Finding: freeze event-parser consistency

**One concrete remaining gap:** `freeze_transcription.progress_evidence()` silently skips lines that fail `EVENT.fullmatch`. `collect_ready_state()` fingerprints only lines matching that same grammar. Consequently, when all recognized evidence remains valid, appending an additional malformed audit-looking line after interrupted preparation can leave readiness and the retry fingerprint unchanged.

For example, this **unexecuted synthetic example** is skipped:

```text
scan 001 audited INVALID_TIMESTAMP cote=10 audit_id=synthetic
```

The relevant branches are `freeze_transcription.py` lines 129–131 and 268. By contrast, `record_audit.require_order()` rejects malformed completion/audit-looking lines.

A related inconsistency is duplicate identity fields: freeze parsing constructs a dictionary directly from the fields and takes the last duplicate value, whereas audit parsing rejects duplicates. A recognized duplicate-field line does enter the fingerprint; this is a parsing ambiguity, not the unchanged-fingerprint example above.

**Narrow follow-up:** apply the audit parser's malformed-event and duplicate-field rejection to freeze parsing before readiness/fingerprinting. A focused synthetic test should append a malformed event after preparation and require refusal without writes. The existing test changes a valid recognized event and does not cover this case.

No live event log or audit/freeze state was inspected. This finding does not imply that any actual task event is malformed. No helper was changed in this review.

## Otherwise consistent

The independent review found the inventory identity/field checks, shared preview/final validation, complete audit gates, honest freeze phase reporting, and changed-recognized-evidence retry checks consistent with their documented behavior.

All six code/test/documentation hashes match `helper_hardening.json`. The saved output records **28 passing tests**, consistent with the test source; they were not rerun. The companion JSON records exact code hashes and the finding.

Only this new review evidence was written. No existing report, page, record or helper was modified. No witness prose, image, context or live completion state was inspected. No packaging or upload occurred.


## Resolution — FREEZE-PARSER-1

2026-11-19 21:12:23 UTC: the reported parser inconsistency is fixed. Freeze rejects malformed completion/audit-looking lines and duplicate identity fields before readiness/fingerprinting. Three focused synthetic checks pass, covering both rejections and unchanged retry/verification. No live state was accessed. Current code hashes and results are in `helper_hardening.json`; the original review above remains historical evidence.
