# Scan102 bounded mechanical QA

Checked: 2026-11-19 21:30:21 UTC  
Page: `B10-07_10_scan102`  
Result: **PASS — no structural issues found.**

## Scope

One bounded metadata/lexical pass checked root-authored record metadata and Python syntax, finalized record metadata, generated report projections, page hashes and TeX lexical structure. No witness prose, scan/image files or context were opened. No live events, audit/freeze state, assembly, archive or upload were accessed or changed. Transcription and page records were not edited.

No source-C edit replay or image pixel-extent bounds check was performed. The source-C hash field was checked for format only. Crop geometry, IDs, references and safe path resolution were checked without opening images or reading headers.

## Counts

| Item | Result |
| --- | ---: |
| Page bytes | 2598 |
| Asserted edit entries (not replayed) | 8 |
| Changes | 26 |
| Against C | 7 |
| Against H | 23 |
| Crop recipes | 35 |
| Inventory rows | 24, all transcribed |
| Root JSON fields compared | 14 |

The expected byte/change/inventory/crop counts agree. Metadata schema, root/final-record correspondence, page hash, inventory/report projections, crop metadata and references, Python AST and TeX lexical checks passed. The lexical check found 45 brace pairs, 48 math pairs and 1 environment pairs; no TeX compilation was performed. All four protected input hashes were unchanged during the check.

The companion JSON records precise input/helper hashes, scope limitations and machine-readable results.
