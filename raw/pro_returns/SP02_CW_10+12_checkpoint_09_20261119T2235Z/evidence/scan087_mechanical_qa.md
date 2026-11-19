# Scan087 bounded mechanical QA

Checked: 2026-11-19 21:21:28 UTC  
Page: `B10-06_10_scan087`  
Result: **PASS — no structural issues found.**

## Scope

Only root-authored record metadata, Python syntax, finalized record metadata, generated report projections, page hashes and TeX lexical structure were checked. No witness prose, scan/image files or context were opened. No live events, audit/freeze state, assembly, archive or upload were accessed or changed. Page records and transcription were not edited.

Source-C edit replay and image pixel-extent bounds were not repeated. The source-C hash field was checked for format only. Crop geometry, IDs, references and safe path resolution were checked without opening images or reading their headers.

## Counts

| Item | Result |
| --- | ---: |
| Page bytes | 2400 |
| Asserted edit entries (not replayed) | 6 |
| Changes | 28 |
| Against C | 13 |
| Against H | 26 |
| Crop recipes | 34 |
| Inventory rows | 30, all transcribed |
| Root JSON fields compared | 15 |

Metadata schema, root/final-record correspondence, page hash, inventory/report projections, counts, crop metadata and references, Python AST and TeX lexical checks passed. The lexical check found 75 brace pairs, 14 math pairs and 4 environment pairs; no TeX compilation was performed. All four protected input hashes were unchanged during the check.

The companion JSON records precise input/helper hashes, scope limitations and machine-readable results.
