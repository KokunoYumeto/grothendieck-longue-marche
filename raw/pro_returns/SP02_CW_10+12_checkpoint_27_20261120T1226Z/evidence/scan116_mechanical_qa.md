# Scan116 bounded mechanical QA

Checked: 2026-11-19 22:47:20 UTC  
Page: `B10-08_10_scan116`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, root Python AST, finalized record schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No fixed root-field count was assumed. No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

The progress log and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted and neither file was changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 5414 |
| Asserted edit entries (not replayed) | 33 |
| Changes | 73 |
| Against C | 34 |
| Against H | 69 |
| Crop recipes | 94 |
| Inventory rows | 96, all transcribed |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

All supplied expected counts agree: 5,414 bytes, 73 changes, 96 inventory rows and 94 crop recipes. All actual root fields agree with the finalized record. Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks passed.

The lexical checker reported 181 brace pairs, 22 math pairs and 6 environment pairs, with no issues. It does not expand macros, compile TeX or judge readings.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were unchanged byte-for-byte before/after the check. Their exact hashes, the actual field-name sets and helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because this pass opens no images or headers. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record or log changes were made.
