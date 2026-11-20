# Scan106 bounded mechanical QA

Checked: 2026-11-19 21:59:51 UTC  
Page: `B10-07_10_scan106`  
Result: **PASS — no structural issues found.**

## Scope

One bounded pass checked root-authored JSON/final-record consistency, root Python AST, finalized record schema, generated inventory/collation/count projections, page hash, crop metadata and TeX lexical structure. No witness prose, scan/image files, image headers or context were opened. No source edit replay, live-event access, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 4493 |
| Asserted edit entries (not replayed) | 16 |
| Changes | 49 |
| Against C | 15 |
| Against H | 47 |
| Crop recipes | 55 |
| Inventory rows | 45, all transcribed |
| Root JSON fields compared | 15 |

Schema/accepted values, identity, all supplied root fields, page hash, inventory/report projections, crop IDs/references/geometry/parameters/safe paths, Python AST and TeX lexical checks passed. The counts above are derived from finalized metadata and agree with their projections; no independent expected count list was supplied.

The lexical checker reported 112 brace pairs, 30 math pairs and 7 environment pairs, with no issues. It does not expand macros, compile TeX or judge readings.

All four protected inputs (finalized page, finalized record, root script and root JSON) were unchanged byte-for-byte before/after the checks. Their exact hashes and the helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because this pass opens no images or headers. Source-C hash format was checked, but its source bytes were not reopened and edits were not replayed. No transcription or record was edited.
