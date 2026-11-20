# Scan105 bounded mechanical QA

Checked: 2026-11-19 21:50:51 UTC  
Page: `B10-07_10_scan105`  
Result: **PASS — no structural issues found.**

## Scope and limits

One bounded pass checked root-authored record metadata and Python AST, finalized record metadata, generated report projections, page hashes and TeX lexical structure. No witness prose, scan/image files, image headers or context were opened. No source edit replay, live-event access, audit/freeze operation, compilation, packaging or upload occurred. Only this evidence and its companion JSON were written; transcription and page records were unchanged.

Crop geometry, IDs, references, parameters and safe source paths were checked without image dimensions. Pixel-extent bounds were not checked. The source-C hash field was checked for format only.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 2626 |
| Asserted edit entries (not replayed) | 17 |
| Changes | 36 |
| Against C | 16 |
| Against H | 36 |
| Crop recipes | 52 |
| Inventory rows | 39, all transcribed |
| Root JSON fields compared | 15 |

The supplied expected byte/change/inventory/crop counts agree. Metadata schema, root/final-record correspondence, page identity and hash, inventory identity/accepted columns and values, inventory and collation projections, change-count report projection, crop metadata and references, Python AST and TeX lexical checks passed.

Root reported placing `mathbb` in inline math inside `unsure` before finalization. The finalized page passes lexical checks with 49 brace pairs, 30 math pairs and 1 environment pairs. This is not macro expansion, compilation or a transcription judgment.

The finalized page, finalized record, root script and root JSON were captured before the checks and compared byte-for-byte afterwards; all four were unchanged. The companion JSON records precise input/helper hashes and machine-readable results.
