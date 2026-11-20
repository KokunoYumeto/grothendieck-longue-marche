# Scan108 bounded mechanical QA

Checked: 2026-11-19 22:14:27 UTC  
Page: `B10-07_10_scan108`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked root-authored JSON/final-record consistency, root Python AST, finalized record schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

The progress log and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted and neither file was changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 3391 |
| Asserted edit entries (not replayed) | 11 |
| Changes | 38 |
| Against C | 10 |
| Against H | 37 |
| Crop recipes | 40 |
| Inventory rows | 28, all transcribed |
| Root JSON fields compared | 15 |

All supplied expected counts agree: 3,391 bytes, 38 changes, 28 inventory rows, 40 crop recipes and 11 edits. Schema/accepted values, identity, root/final-record correspondence, page hash, inventory/report projections, crop IDs/references/geometry/parameters/safe paths, Python AST and TeX lexical checks passed.

The lexical checker reported 55 brace pairs, 24 math pairs and 3 environment pairs, with no issues. It does not expand macros, compile TeX or judge readings.

All six protected inputs (finalized page, finalized record, root script, root JSON, progress log and CHECK_EVENTS) were unchanged byte-for-byte before/after the checks. Their exact hashes and the helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because this pass opens no images or headers. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record, progress or CHECK_EVENTS changes were made.
