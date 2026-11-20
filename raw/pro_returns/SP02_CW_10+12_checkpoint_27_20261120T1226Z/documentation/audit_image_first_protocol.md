# Image-first audit receipt protocol

This helper supplements the existing ordered audit workflow. It does not begin,
complete, revise or freeze an audit; it never opens page text, scan images,
witnesses or context. Root remains responsible for all visual observations.
No live receipt has been created as part of implementing this helper.

## Root sequence

1. Begin the next audit with the existing `record_audit.py --begin PAGE_KEY`.
2. Personally view the whole scan and both actual halves.
3. Write root-authored observations, including unusual words, accents and other
   matters noticed before reopening the consolidated transcription. Explicitly
   state none if there is nothing to record; do not leave observations blank.
4. Commit those declarations with `record_audit_image_first.py --record INPUT.json`.
5. Invoke `--mark-text-open PAGE_KEY` immediately before reopening the consolidated
   page text. Proceed to the text only after the helper succeeds.
6. Conduct the comparison and complete the audit using the existing audit helper.

Example input structure (replace the identity/hash placeholders with the actual
values returned by `--begin`; the observation is authored by root):

```json
{
  "page_key": "B10-01_10_scan033",
  "audit_id": "B10-01_10_scan033_audit001",
  "baseline_page_sha256": "ACTUAL_64_HEX_BASELINE_HASH",
  "viewed": {"whole": true, "half_a": true, "half_b": true},
  "observations": {"unusual_words": [], "accents": [], "other": "ROOT_OBSERVATIONS"}
}
```

Observations may be a nonempty string, list or JSON object. Their internal
structure is not prescribed. The example does not constitute observations or
claim that any scan was viewed. Client-supplied observation/text-opening times
are rejected; the helper records the actual UTC clock at each successful phase.

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_audit_image_first.py \
  --record work/ROOT_IMAGE_FIRST_DECLARATION.json

PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_audit_image_first.py \
  --mark-text-open B10-01_10_scan033
```

## Files and guarantees

For each existing audit ID, the helper exclusively publishes:

- `documentation/audit_image_first/AUDIT_ID/image_first.json`: immutable first
  observations, view declarations, identity, baseline, schema version 1, actual
  `image_first_observed_utc`, and a null `transcription_opened_utc`.
- `documentation/audit_image_first/AUDIT_ID/receipt.json`: the same immutable
  fields, actual `transcription_opened_utc`, and `image_first_sha256` binding the
  exact initial receipt bytes.

No file is overwritten. Identical retries return the existing timestamp and hash;
attempts to replace observations are rejected. Each write requires exactly one
matching `started` audit, its matching start event, and the same baseline hash.
`commit_pending`, frozen and context-opened state prohibit receipt writes.
Neither existing session JSON nor progress.log is changed.

Receipt times use actual UTC with microseconds. Existing audit sessions record
seconds. The completed-receipt validator conservatively requires:

`audit began <= image-first observed < text opened < audit completed`.

If audit completion is recorded in the same second as text opening, that strict
order cannot be established and validation fails. Root should complete the real
comparison before finalizing; the helper never fabricates a later time.

These are root declarations and a temporal record of helper calls. They cannot
prove human visual attention or that a viewer was actually opened. The text-open
marker records intent immediately before opening; it does not open the page.

## Read-only validation

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_audit_image_first.py \
  --validate --require-no-active --require-completed-pages 106
```

API:

```python
validate_receipts(output, expected_page_keys=canonical_keys, require_no_active=True)
```

The API returns a metadata-only report and raises `ReceiptError` or an I/O error
on invalid/missing evidence. It checks every completed audit, including repeat
audits keyed by their distinct audit IDs; 106 distinct pages may have more than
106 completed audit sessions. It verifies immutable-field equality, binding
hashes, baseline/session identity and strict timestamp order. Optional canonical
keys enforce exact page coverage. Without coverage arguments, zero completed
audits is a valid empty set, not a claim that the final audit is complete.

This validator remains read-only after freeze/context opening. It supplements
the existing map-order, event/history and 107-hash checks; it does not replace
them. No existing audit/freeze/package script has been wired to require it yet.

The synthetic checks under `evidence/audit_image_first_synthetic_checks.py` use
temporary, artificial sessions without any manuscript or image files. They do
not invoke a real audit, receipt, freeze or context event.
