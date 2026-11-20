# Scan107 bounded mechanical QA

Checked: 2026-11-19 22:07:43 UTC  
Page: `B10-07_10_scan107`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked root-authored JSON/final-record consistency, root Python AST, finalized metadata schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No witness prose, scan/image files, image headers or context were opened. No source edit replay, live-event access, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 5285 |
| Asserted edit entries (not replayed) | 24 |
| Changes | 55 |
| Against C | 22 |
| Against H | 52 |
| Crop recipes | 62 |
| Inventory rows | 55, all transcribed |
| Root JSON fields compared | 15 |

The supplied expected counts (55 changes, 55 inventory rows, 62 crop recipes) agree. Schema/accepted values, identity, root/final-record correspondence, page hash, inventory/report projections, crop IDs/references/geometry/parameters/safe paths, Python AST and TeX lexical checks passed.

The lexical checker reported 138 brace pairs, 32 math pairs and 6 environment pairs, with no issues. It does not expand macros, compile TeX or judge readings.

All four protected inputs (finalized page, finalized record, root script and root JSON) were unchanged byte-for-byte before/after the checks. Their exact hashes and the helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because this pass opens no images or headers. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record or transcription was edited.
