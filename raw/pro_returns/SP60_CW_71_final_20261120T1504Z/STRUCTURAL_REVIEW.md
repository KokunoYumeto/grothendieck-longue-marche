# SP60_CW_71 — Structural metadata review

Generated 2026-11-20 15:04:08 UTC. Scope: final package structure.

This report is generated from deliverable structure and bookkeeping metadata. It does not inspect source scans or witnesses, judge readings, interpret mathematics, certify inventory completeness, or compile TeX. Approximate doubt matches are string candidates, not confirmed identification of manuscript places.

Result: **PASS**, 3949 structural checks, 0 warning(s). Present scans: 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48.

## Decision bookkeeping

150 decision rows: 67 changes and 83 retained-reading rows. Changes against C: 32; against H: 41; against both: 6. Exact unique scan/place labels: 67. H collation projection exact: True.

The counts below use one recorded primary category per change row. They do not establish that differently worded place labels are distinct manuscript locations. Category typography is normalized for counting.

| Error-sheet category | Change rows | Against C | Against H |
|---|---:|---:|---:|
| Symbols and indices | 7 | 6 | 1 |
| Words | 5 | 5 | 0 |
| Omissions | 40 | 12 | 31 |
| Drawings and diagrams | 1 | 1 | 1 |
| Readable ink left as illegible | 7 | 1 | 7 |
| Insertion or placement | 0 | 0 | 0 |
| Deletion state | 1 | 1 | 0 |
| Abbreviation or spelling normalization | 4 | 4 | 1 |
| Text not on the page | 1 | 1 | 0 |
| Other | 1 | 1 | 0 |

## Approximate uncertainty coverage

Each in-place marker is compared with reading/alternative fields on the same scan. Recurring notation permits several markers to share a doubt row. A primary-reader acknowledgement can resolve a failed approximate match only while its recorded page SHA-256 is current. Remaining missing candidates and matches only to resolved rows are warnings; they do not establish a transcription defect.

| Scan | Unsure | Illegible | Active doubt rows | Active candidate | Manual acknowledgement | Resolved only | No candidate |
|---|---:|---:|---:|---:|---:|---:|---:|
| 38 | 6 | 1 | 7 | 7 | 0 | 0 | 0 |
| 39 | 5 | 0 | 5 | 4 | 1 | 0 | 0 |
| 40 | 7 | 0 | 7 | 7 | 0 | 0 | 0 |
| 41 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 42 | 9 | 0 | 8 | 6 | 3 | 0 | 0 |
| 43 | 12 | 1 | 12 | 12 | 1 | 0 | 0 |
| 44 | 9 | 0 | 9 | 9 | 0 | 0 | 0 |
| 45 | 9 | 0 | 9 | 7 | 2 | 0 | 0 |
| 46 | 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 47 | 6 | 1 | 7 | 6 | 1 | 0 | 0 |
| 48 | 17 | 0 | 17 | 15 | 2 | 0 | 0 |

### Primary-reader manual mappings

These are the primary reader's supplied mappings to existing active doubt records, not additional manuscript judgments by the validator. They are bound to the full page-file hashes stored in `UNCERTAINTY_ACKNOWLEDGEMENTS.tsv`; a later page edit makes a mapping stale until deliberately reviewed.

| Scan | TeX line | Hash current | Primary-reader acknowledgement |
|---|---:|---|---|
| 39 | 4 | yes | Mapped by the primary reader to existing active records for the dark subtraction and opening parenthesis. |
| 42 | 16 | yes | Mapped by the primary reader to the existing active record for cancelled r/e. |
| 42 | 29 | yes | Mapped by the primary reader to the existing active record for the asterisk-like blot. |
| 42 | 32 | yes | Mapped by the primary reader to the existing active record for cancelled Γ. |
| 43 | 29 | yes | Mapped by the primary reader to existing active records for −{z}, q, and quén. |
| 45 | 7 | yes | Mapped by the primary reader to the existing active record for the underlying superset. |
| 45 | 19 | yes | Mapped by the primary reader to the existing active record for cancelled cap. The approximate match to a resolved ext record elsewhere on the page is accidental. |
| 46 | 38 | yes | Mapped by the primary reader to the existing active record for the overwritten opening ]. |
| 47 | 16 | yes | Mapped by the primary reader to existing active records for overwritten [ and the first dotted Λ. |
| 48 | 2 | yes | Mapped by the primary reader to existing active records for so, the dot, and R. |
| 48 | 16 | yes | Mapped by the primary reader to existing active records for numèro and the pencil words. |

## Progress and freeze

Done entries: 11. Audited entries: 11. Freeze recorded: True.

Current frozen hashes verified: 12/12. Final unchanged confirmation: True.

## Errors

None.

## Warnings

None.

## Final bookkeeping procedure

1. Complete all second readings; consolidate superseded place decisions and doubt statuses while preserving the audit history.
2. Generate every required final document and the combined fragment. Recheck the H projection and category counts.
3. Append `transcription frozen <UTC time>` to `progress.log`, followed by one `sha256 <64-hex digest> <relative path>` line for each page and the combined fragment. Hash only finalized UTF-8 bytes.
4. Recompute those hashes before packaging. If any differ, investigate and deliberately establish a new freeze after the change; do not silently replace the recorded values.
5. After successful comparison, append `frozen hashes unchanged <UTC time>`. Run the validator in final mode and then with `--zip` against the final archive.

`record.py` is append-only: it does not automatically supersede doubts, deduplicate places, or rebuild the H collation after an existing decision row is edited. Its `render()` also rewrites the combined transcription, so finish rendering before freezing.
