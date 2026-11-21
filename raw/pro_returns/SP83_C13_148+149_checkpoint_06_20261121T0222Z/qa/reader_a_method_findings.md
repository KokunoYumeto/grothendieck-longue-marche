# Method and documentation audit

Snapshot: 2026-11-21T02:12:54.387980+00:00

Read-only audit by reader_a. Accepted pages, records, assignments, first/second TSVs and aggregates were not edited or assembled.

## Coverage

- 23 page sets; 339 prescribed boxes; all first/second reading rows checked in order.
- 261 supplied C marks and 261 exported decisions checked.
- 339 canonical independent crop entries; 1116 accepted evidence references checked.
- 19 finalized audits at this snapshot; expected pending: 148_scan071, 148_scan072, 149_scan003, 149_scan004.

## Actionable findings

### A15: Four legacy retained intermediates lack locatable original-coordinate provenance

This is a provenance annotation gap for retained intermediates, not a missing mandatory citation or an ink-reading failure. Locate an existing original/parent box or generator if recoverable; otherwise document honestly that the historical coordinates were not retained. Preserve the images and existing view registry. Do not invent coordinates or change frozen readings.

Evidence:

```json
{
  "unlocated_provenance": [
    {
      "crop": "result/crops/148_scan051_r_arrow.png",
      "json_references": [],
      "main_reader_view_registry_contains_crop": true,
      "used_by_accepted_change_or_mark_evidence": false
    },
    {
      "crop": "result/crops/148_scan053_cela.png",
      "json_references": [],
      "main_reader_view_registry_contains_crop": true,
      "used_by_accepted_change_or_mark_evidence": false
    },
    {
      "crop": "result/crops/148_scan053_margin4.png",
      "json_references": [],
      "main_reader_view_registry_contains_crop": true,
      "used_by_accepted_change_or_mark_evidence": false
    },
    {
      "crop": "result/crops/148_scan053_margin3.png",
      "json_references": [],
      "main_reader_view_registry_contains_crop": true,
      "used_by_accepted_change_or_mark_evidence": false
    }
  ],
  "image_hash_issues": []
}
```

## Expected pending work

### P02: Root adjudication and final transcription freeze remain in progress

Finish the outstanding visual adjudications, refresh aggregate deliverables, freeze all 24 transcription hashes, verify them unchanged, then create the final ZIP.

```json
{
  "pending_at_snapshot": [
    "148_scan071",
    "148_scan072",
    "149_scan003",
    "149_scan004"
  ],
  "expected_pending_from_assignment": [
    "148_scan068",
    "148_scan069",
    "148_scan071",
    "148_scan072",
    "149_scan003",
    "149_scan004"
  ],
  "transcription_hashes_present": false,
  "transcription_frozen_log_line_present": false
}
```

## Resolved during this audit

- **R01: Reversed 149_scan004 assignment row corrected during audit.** No further action: the current ledger matches both reader records.

## Check results

| Check | Result |
|---|---|
| 23-page ordered scope | Pass |
| Assignment rows cover all pages once | Pass |
| Exact first/second box coverage, order and nonempty readings | Pass |
| First reading snapshots preserved in accepted metadata | Pass |
| Recorded second-reading hashes match frozen TSVs | Pass |
| Comparison preserves complete frozen readings | Pass |
| Finalized visual adjudication records complete | Pass |
| Different first and second readers, consistent assignments | Pass |
| Canonical crop existence, coordinates, hash and view documentation | Pass |
| First-reading decision/change crops exist with boxes and review registration | Pass |
| All 261 supplied C mark IDs occur once in original order | Pass |
| Required aggregate files and 23 accepted page files exist | Pass |
| Required table schemas, inventory confirmations and per-page sections | Pass |
| Progress and first/second phase chronology | Pass |
| Packaged result/work trees exclude attached texts, originals and prepared halves | Pass |
| Retained crop/helper provenance and stored image hashes | Review finding |
| Existing checkpoint ZIP central directories exclude inputs and nested ZIPs | Pass |
| Current package tree retains files documented by earlier checkpoints | Pass |
| Checkpoint durable-save receipts retained | Pass |
| All 46 frozen TSV files unchanged during this audit | Pass |

## Page ledger

| Page | First reader | Independent reader | Boxes | Audit state |
|---|---|---|---:|---|
| 148_scan048 | reader_a | reader_b | 18 | Finalized |
| 148_scan049 | reader_b | reader_c | 13 | Finalized |
| 148_scan050 | reader_c | reader_a | 21 | Finalized |
| 148_scan051 | reader_b | reader_c | 12 | Finalized |
| 148_scan052 | reader_c | reader_b | 17 | Finalized |
| 148_scan053 | reader_a | reader_c | 25 | Finalized |
| 148_scan055 | reader_b | reader_a | 12 | Finalized |
| 148_scan056 | reader_c | reader_b | 24 | Finalized |
| 148_scan057 | reader_b | reader_a | 11 | Finalized |
| 148_scan058 | reader_a | reader_c | 18 | Finalized |
| 148_scan059 | reader_c | reader_a | 15 | Finalized |
| 148_scan061 | reader_b | reader_c | 18 | Finalized |
| 148_scan062 | reader_a | reader_b | 21 | Finalized |
| 148_scan063 | reader_c | reader_a | 24 | Finalized |
| 148_scan064 | reader_a | reader_b | 19 | Finalized |
| 148_scan065 | reader_c | reader_a | 7 | Finalized |
| 148_scan067 | reader_b | reader_c | 17 | Finalized |
| 148_scan068 | reader_c | reader_a | 17 | Finalized |
| 148_scan069 | reader_a | reader_b | 2 | Finalized |
| 148_scan071 | reader_c | reader_b | 9 | Expected pending |
| 148_scan072 | reader_a | reader_c | 2 | Expected pending |
| 149_scan003 | reader_b | reader_a | 7 | Expected pending |
| 149_scan004 | reader_b | reader_a | 10 | Expected pending |

## Limits

- This is a metadata/process audit, not a fresh visual reading. View claims are checked against retained documentation; they are not re-enacted.
- Geometric box coverage alone cannot establish that every ink word or revision lies in an audit box; that semantic coverage belongs to the main reader and accepted inventories.
- Read-only checks are a timed snapshot while the root reader continues adjudication. Expected pending pages were supplied explicitly in the assignment.
- Filesystem write permission is not used as the definition of a frozen reading; unchanged content hashes and preserved comparison snapshots are the evidence.

The JSON companion retains per-page TSV hashes, all checked hash references, evidence for every check, and the timed input snapshot hashes.
