# Scan117 bounded mechanical QA

Checked: 2026-11-19 22:52:14 UTC  
Page: `B10-08_10_scan117`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, root Python AST, finalized metadata schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No fixed field count was assumed. No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

The progress log and CHECK_EVENTS were accessed as raw bytes solely for before/after protection hashes; their contents were not interpreted or changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 1140 |
| Asserted edit entries (not replayed) | 7 |
| Changes | 19 |
| Against C | 7 |
| Against H | 19 |
| Crop recipes | 26 |
| Inventory rows | 23 |
| All inventory rows transcribed | true |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 1,140 bytes, 19 changes, 23 inventory rows, 26 crop recipes. Findings: none. Root/final field differences: none.

Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks were included. Lexical result: PASS, with 39 brace pairs, 4 math pairs and 1 environment pairs. This does not expand macros, compile TeX or judge readings.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were compared byte-for-byte before/after the check. Changed inputs: none. Exact hashes, actual field-name sets and helper hashes are recorded in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record or log was edited.
