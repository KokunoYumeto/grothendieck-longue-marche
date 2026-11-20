# Scan109 bounded mechanical QA

Checked: 2026-11-19 22:18:48 UTC  
Page: `B10-07_10_scan109`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked root-authored JSON/final-record consistency, root Python AST, finalized record schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

The progress log and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted and neither file was changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 2520 |
| Asserted edit entries (not replayed) | 9 |
| Changes | 20 |
| Against C | 8 |
| Against H | 19 |
| Crop recipes | 34 |
| Inventory rows | 18, all transcribed |
| Root JSON fields compared | 15 |

All supplied expected counts agree: 2,520 bytes, 20 changes, 18 inventory rows, 34 crop recipes and 9 edits. Schema/accepted values, identity, root/final-record correspondence, page hash, inventory/report projections, crop IDs/references/geometry/parameters/safe paths, Python AST and TeX lexical checks passed.

The lexical checker reported 33 brace pairs, 25 math pairs and 2 environment pairs, with no issues. It does not expand macros, compile TeX or judge readings.

All six protected inputs (finalized page, finalized record, root script, root JSON, progress log and CHECK_EVENTS) were unchanged byte-for-byte before/after the checks. Their exact hashes and the helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because this pass opens no images or headers. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record, progress or CHECK_EVENTS changes were made.
