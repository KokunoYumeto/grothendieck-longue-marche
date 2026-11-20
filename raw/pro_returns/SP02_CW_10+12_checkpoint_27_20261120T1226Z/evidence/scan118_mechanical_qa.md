# Scan118 bounded mechanical QA

Checked: 2026-11-19 23:09:37 UTC  
Page: `B10-08_10_scan118`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, root Python AST, finalized schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No field count was assumed. No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation or compilation occurred. Only this evidence and its companion JSON were written by the page check; the separately authorized checkpoint preparation is documented separately.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted or changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 5342 |
| Asserted edit entries (not replayed) | 25 |
| Changes | 54 |
| Against C | 24 |
| Against H | 49 |
| Crop recipes | 81 |
| Inventory rows | 66 |
| All inventory rows transcribed | true |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected crop count: 81. Findings: none. Root/final field differences: none.

Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks were included. Lexical result: PASS, with 152 brace pairs, 41 math pairs and 9 environment pairs. This does not expand macros, compile TeX or judge readings.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were compared byte-for-byte before/after the check. Changed inputs: none. Exact hashes, actual field-name sets and helper hashes are recorded in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. No page, record or log was edited.
