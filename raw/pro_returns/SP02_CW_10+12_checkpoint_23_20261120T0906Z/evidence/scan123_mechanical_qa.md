# Scan123 bounded mechanical QA

Checked: 2026-11-20 00:30:12 UTC  
Page: `B10-09_10_scan123`  
Finalized record timestamp: 2026-11-20 00:29:52 UTC  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual root JSON fields against the finalized record, root Python AST, finalized schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No fixed field count was assumed. No witness prose, C notes, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation or compilation occurred. Only this evidence and its companion JSON were written by the page check; separately authorized checkpoint preparation is documented separately.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted or changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 4501 |
| Asserted edit entries (not replayed) | 31 |
| Changes | 63 |
| Against C | 33 |
| Against H | 62 |
| Crop recipes | 82 |
| Inventory rows | 61 |
| All inventory rows transcribed | true |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 4,501 bytes, 63 changes, 61 inventory rows, 82 crop recipes. Findings: none. Root/final field differences: none.

Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks were included. Lexical result: PASS, with 120 brace pairs, 46 math pairs and 5 environment pairs. No macro expansion, compilation or reading assessment was performed.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were compared byte-for-byte before/after the check. Changed inputs: none. Exact hashes, actual field-name sets and helper hashes are recorded in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without source access or edit replay. No protected input was edited.
