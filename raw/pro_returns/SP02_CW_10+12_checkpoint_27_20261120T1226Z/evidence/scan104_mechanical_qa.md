# Scan104 bounded mechanical QA

Checked: 2026-11-19 21:41:30 UTC  
Page: `B10-07_10_scan104`  
Result: **PASS — no structural issues found.**

## Scope and limits

One bounded pass checked root-authored record metadata and Python syntax, finalized record metadata, generated report projections, page hashes and TeX lexical structure. No source witness prose, scan/image files, image headers or context were opened. No source edit replay, live events, audit/freeze operation, completion-log change, compilation, packaging or upload occurred. Only this Markdown evidence and its companion JSON were written.

No source dimensions are recorded in the finalized record, root JSON or map metadata. Crop geometry, IDs, references, parameters and safe source paths passed; pixel-extent bounds could not be checked from the permitted metadata. The source-C hash field was checked for format only.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 4910 |
| Asserted edit entries (not replayed) | 23 |
| Changes | 52 |
| Against C | 27 |
| Against H | 51 |
| Crop recipes | 63 |
| Inventory rows | 62, all transcribed |
| Root JSON fields compared | 15 |

Required metadata fields and accepted values, page/record identity, root/final-record correspondence, page hash, inventory and collation projections, change-count report projection, crop metadata and references, Python AST and TeX lexical checks passed. No independent expected counts were supplied for this page; the counts above come from the checked finalized inputs and agree with their generated projections.

The lexical check found 114 brace pairs, 46 math pairs and 4 environment pairs. It does not compile or assess textual/mathematical readings.

The page, finalized record, root script and root JSON were captured before the checks and compared byte-for-byte afterwards; all four were unchanged. Exact SHA256 values and machine-readable results are retained in the companion JSON.
