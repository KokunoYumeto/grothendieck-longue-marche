# Scan 129 mechanical QA

Checked: 2026-11-20 02:51:16 UTC  
Recorded finalization: 2026-11-20 02:49:51 UTC  
Page: `B10-09_10_scan129`

## Result

PASS for all performed checks.

Page bytes: 6,661. All 15 actual root JSON fields match the finalized record. Final page bytes exactly match root's prepared fragment, and the final recipe list exactly matches all 98 entries in root's crops129.json. No source replay was needed.

| Metadata | Count |
|---|---:|
| edits | 37 |
| changes | 75 |
| against C | 38 |
| against H | 71 |
| crops | 98 |
| inventory | 71 |
| inventory all yes | True |
| remaining doubts | 14 |

## Checks

Record/map identity, stored page hash, shared metadata schema and accepted values passed. Inventory/collation headers and exact rows, the complete changes section/count row, and the page doubt rows agree with their generated projections. Reading fields were handled as opaque values only. Every crop reference resolved; recipe geometry, transformation parameters and safe source paths passed without opening images or headers. Actual pixel extent bounds were not checked.

Root script AST: PASS. TeX lexical: PASS; {"brace_pairs": 145, "environment_pairs": 7, "math_pairs": 65}.

## Protected inputs

All 8 protected byte streams were identical before and after. Changes: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-09_10_scan129.json` | 102657 | `3c5f6fb7cb3675cd961a061bcd00239532295886a2acc37a5f3ef4b491131c8d` |
| `SP02_CW_10+12/pages/B10-09_10_scan129.tex` | 6661 | `fd479600361be875e9488bb6d3f9e2876c9a543bca48d31452bdd9bcaa8e7205` |
| `work/record129.json` | 79541 | `7092a6cac8e0ec5dceb38ed8bfa12ba05d4b530c84c3678afdf059857376ed5e` |
| `work/record129.py` | 29811 | `df427419c7e5728387994ac1668ad25679001e9f8d7915e383c582144d439537` |
| `work/prepared129.tex` | 6661 | `fd479600361be875e9488bb6d3f9e2876c9a543bca48d31452bdd9bcaa8e7205` |
| `work/crops129.json` | 18485 | `b4c8d7bc83fb75869923f31902b20a09f86aa7042198d09c6791212b3484f18f` |
| `SP02_CW_10+12/progress.log` | 12130 | `c983f91b569dbf16ad61624e88a26a492266340eb7f1d1eec407637ae2a2dc30` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |

## Scope

One bounded finalized metadata/projection/AST/lexical check. Preparation equality means direct byte equality of root-supplied prepared129.tex and the finalized page; no witness/source-edit replay. No image/header, witness prose, context, reading judgment, compilation, audit/freeze, staging/package/upload.

Only this report and its companion JSON were written. Checkpoint 15 was neither staged nor packaged by this QA.
