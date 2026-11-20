# Scan121 bounded mechanical QA

Checked: 2026-11-19 23:53:37 UTC  
Page: `B10-08_10_scan121`  
Finalized record timestamp: 2026-11-19 23:53:18 UTC  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual root JSON fields against the finalized record, root Python AST, finalized metadata schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No fixed field count was assumed. No witness prose, C notes, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation or compilation occurred. Only this evidence and its companion JSON were written by the page check; separately authorized checkpoint preparation is documented separately.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted or changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 6178 |
| Asserted edit entries (not replayed) | 24 |
| Changes | 64 |
| Against C | 24 |
| Against H | 61 |
| Crop recipes | 89 |
| Inventory rows | 57 |
| All inventory rows transcribed | true |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 6,178 bytes, 64 changes, 57 inventory rows, 89 crop recipes. Findings: none. Root/final field differences: none.

Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks were included. Lexical result: PASS, with 121 brace pairs, 64 math pairs and 11 environment pairs. No macro expansion, compilation or reading assessment was performed.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were compared byte-for-byte before/after the check. Changed inputs: none. Exact hashes, actual field-name sets and helper hashes are recorded in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without source access or edit replay. No protected input was edited.
