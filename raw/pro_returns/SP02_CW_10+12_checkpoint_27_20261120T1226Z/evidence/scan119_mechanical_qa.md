# Scan119 bounded mechanical QA

Checked: 2026-11-19 23:25:30 UTC  
Page: `B10-08_10_scan119`  
Finalized record timestamp: 2026-11-19 23:25:06 UTC  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, root Python AST, finalized metadata schema, inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No field or count assumption was imposed. The supplied finalization timestamp was checked. No witness prose, scan/image files, image headers or context were opened. No source edit replay, transcription decisions, audit/freeze operation, compilation, checkpoint preparation, packaging or upload occurred. Only this evidence and its companion JSON were written.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes; their contents were not interpreted or changed.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 4427 |
| Asserted edit entries (not replayed) | 23 |
| Changes | 50 |
| Against C | 22 |
| Against H | 48 |
| Crop recipes | 81 |
| Inventory rows | 80 |
| All inventory rows transcribed | true |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Findings: none. Root/final field differences: none.

Schema/accepted values, identity, page hash, inventory/report projections, crop IDs/references/finite geometry/parameters/safe paths, Python AST and TeX lexical checks were included. Lexical result: PASS, with 113 brace pairs, 43 math pairs and 9 environment pairs. This does not expand macros, compile TeX or judge readings.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were compared byte-for-byte before/after the check. Changed inputs: none. Exact SHA256 fingerprints, actual field-name sets and helper hashes are recorded in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. No protected input was edited.
