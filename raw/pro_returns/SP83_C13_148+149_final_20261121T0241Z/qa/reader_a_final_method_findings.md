# Final method and documentation audit

Snapshot: 2026-11-21T02:34:39.279972+00:00

Read-only audit by reader_a. Accepted pages, records, assignments, first/second TSVs and aggregates were not edited or assembled.

## Coverage

- 23 page sets; 339 prescribed boxes; all first/second reading rows checked in order.
- 261 supplied C marks and 261 exported decisions checked.
- 339 canonical independent crop entries; 1119 accepted evidence references checked.
- 23 finalized audits at this snapshot; expected pending: none.

## Actionable findings

No open structural defect found in the checks below.

## Final post-documentation gates

## Resolved prior findings

- **R01: Reversed 149_scan004 assignment row corrected before final audit.** No further action: the current ledger matches both reader records.
- **R02: A15 four early intermediate crop rectangles recovered exactly.** No action; retain the standalone recovery report and unchanged crops.

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
| All23 independent audits finalized | Pass |
| Packaged result/work trees exclude attached texts, originals and prepared halves | Pass |
| Retained crop/helper provenance and stored image hashes | Pass |
| Existing checkpoint ZIP central directories exclude inputs and nested ZIPs | Pass |
| Current package tree retains files documented by earlier checkpoints | Pass |
| Checkpoint durable-save receipts retained | Pass |
| All 46 frozen TSV files unchanged during this audit | Pass |
| Historical 19-audit snapshot preserved; all 46 frozen TSV hashes remain identical | Pass |
| All 339 full token comparisons and edit sequences recomputed | Pass |
| All 23 audit B/D/K counts, accepted audit_changes and progress entries agree | Pass |
| Frozen box kinds and original coordinates agree with accepted prescriptions | Pass |
| A15 exact geometry recovery remains valid for all four retained intermediates | Pass |
| All24 frozen transcription hashes and progress hash entries match current files | Pass |
| Final aggregate counts agree with current accepted records | Pass |

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
| 148_scan071 | reader_c | reader_b | 9 | Finalized |
| 148_scan072 | reader_a | reader_c | 2 | Finalized |
| 149_scan003 | reader_b | reader_a | 7 | Finalized |
| 149_scan004 | reader_b | reader_a | 10 | Finalized |

## Final method metrics

```json
{
  "historical_snapshot_preserved": true,
  "historical_frozen_tsv_hashes_unchanged": true,
  "independent_boxes": 339,
  "different_boxes": 288,
  "changed_boxes": 126,
  "final_aggregate_counts": {
    "places": 715,
    "against_C": 276,
    "against_H": 640,
    "inventory_elements": 520,
    "remaining_doubts": 275
  },
  "transcription_hashes": 24,
  "transcription_hashes_match": true,
  "final_unchanged_verification_log_present": true,
  "complementary_scope": "Reader_b final static QA owns byte-exact aggregate consistency, remaining-doubt mappings and accepted TeX static structure. This report checks method/identity/freeze/provenance and export counts.",
  "post_package_gate": "The final ZIP does not yet exist at this method snapshot. Its exact contents, restoration and durable save receipt require root post-package verification."
}
```

## Limits

- This is a metadata/process audit, not a fresh visual reading. View claims are checked against retained documentation; they are not re-enacted.
- Geometric box coverage alone cannot establish that every ink word or revision lies in an audit box; that semantic coverage belongs to the main reader and accepted inventories.
- All23 adjudications were completed before this final run. Later root documentation synchronization is permitted; current hashes and report timestamps define this snapshot. The final ZIP and its restoration/save receipts require a separate post-package gate.
- Filesystem write permission is not used as the definition of a frozen reading; unchanged content hashes and preserved comparison snapshots are the evidence.

The JSON companion retains per-page TSV hashes, all checked hash references, evidence for every check, and the timed input snapshot hashes.
