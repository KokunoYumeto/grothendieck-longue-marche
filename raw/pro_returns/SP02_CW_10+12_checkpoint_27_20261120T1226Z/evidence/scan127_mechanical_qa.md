# Scan 127 mechanical QA

Checked: 2026-11-20 02:20:07 UTC  
Recorded finalization: 2026-11-20 01:58:11 UTC  
Page: `B10-09_10_scan127`

## Result

PASS for all performed checks.

The finalized page is 7,611 bytes. All 15 actual root JSON fields match the finalized record after the existing cote/scan normalization. The record/page identity and stored page hash agree. The source-C hash field has valid SHA-256 syntax; its source was not reopened.

| Metadata | Count |
|---|---:|
| edits | 32 |
| changes | 83 |
| against C | 39 |
| against H | 80 |
| crops | 101 |
| inventory | 113 |
| inventory all yes | True |
| remaining doubts | 22 |

## Performed checks

The metadata validator accepted the record. Crop IDs, finite integral box geometry, transformation parameters, safe existing source paths, and all change-row crop references passed. Paths were resolved without opening images or image headers. Inventory and collation headers and exact page projections agree; the change count row, complete change/doubt page section, and remaining-doubt rows also agree. Reading strings were processed only as opaque values and were neither displayed nor adjudicated.

Root script AST: PASS. Page TeX lexical validation: PASS; {"brace_pairs": 224, "environment_pairs": 12, "math_pairs": 75}. No TeX compilation or edit replay occurred.

## Root-reported padding

Root reports that the summaryl recipe may extend one pixel beyond the source right edge and that this is documented viewing padding. No image or header was opened, so the source extent and padding claim were not independently verified. Recipe unchanged.

- Recipe `summaryl`: source `SP02_CW_10+12_scans/B10-09_10_scan127.jpg`, box `[744, 1443, 1684, 1513]`, rotation `0`, scale `6`.

The box passed coordinate/parameter checks. Actual source pixel bounds were not checked in this task.

## Protected inputs

All 6 protected input byte streams were identical before and after the checks. No page, record, root script, progress log or CHECK_EVENTS mutation occurred.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-09_10_scan127.json` | 128152 | `2a7959be936bef2c50da12f81410ae3f52eda6e44d8d4de99a62a25c38fa57ca` |
| `SP02_CW_10+12/pages/B10-09_10_scan127.tex` | 7611 | `68d39ceb7c2bad934f497a6ed9592af2ffe08f9f21a4fa85dd764862bbabffc7` |
| `work/record127.json` | 93104 | `416d455e9685863e49cc674574714835e16adba2f2ce7e9cb37908df329f5a7a` |
| `work/record127.py` | 37723 | `a3cf9375d6c4c14d10e64a1a154f882453e2c7e7bc5afdd1c9977de6666d8c68` |
| `SP02_CW_10+12/progress.log` | 11702 | `85b4a27f9c0fe1557ad52f393a2e08454ad46f5486de2ea7788390be7e8e3e8f` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |

## Scope

Bounded metadata/schema, opaque report projections, path metadata, AST and lexical TeX only. No source-edit replay, image/header access, witness prose/context inspection, reading decision, compilation, live audit/freeze, assembly, packaging or upload.

Only this Markdown report and its companion JSON report were written. No assembly, checkpoint preparation, archive creation or upload was performed.
