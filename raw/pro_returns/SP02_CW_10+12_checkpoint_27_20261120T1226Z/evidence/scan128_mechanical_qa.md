# Scan 128 mechanical QA

Checked: 2026-11-20 02:29:45 UTC  
Recorded finalization: 2026-11-20 02:24:35 UTC  
Page: `B10-09_10_scan128`

## Result

PASS for all performed checks.

Page bytes: 5,892. All 15 actual root JSON fields agree with the finalized record after the existing cote/scan normalization. Record/map identity and page SHA-256 agree. The source-C hash field is well formed; the source was not reopened.

| Metadata | Count |
|---|---:|
| edits | 27 |
| changes | 49 |
| against C | 36 |
| against H | 45 |
| crops | 69 |
| inventory | 67 |
| inventory all yes | True |
| remaining doubts | 12 |

## Checks

The strengthened shared validator accepted the metadata, inventory IDs and crop references. Inventory/collation headers and exact page rows, the complete changes page section/count row, and all page doubt rows match their record projections. Reading strings were processed as opaque values only. Crop metadata passed finite integral geometry, supported transformation parameters and safe existing source-path resolution. No image or image header was opened; source pixel bounds were not independently checked.

Root script AST: PASS. TeX lexical: PASS, with {"brace_pairs": 143, "environment_pairs": 14, "math_pairs": 60}. No compilation or edit replay occurred.

## Protected inputs

All six protected byte streams were identical before and after the QA. Changes: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-09_10_scan128.json` | 81056 | `2d455ca31ac3cd333c3bb9873545477db0647c166105a0d99304872311d99d62` |
| `SP02_CW_10+12/pages/B10-09_10_scan128.tex` | 5892 | `8f8e2e3350a01e9acbdc95d246ae1f4a3b1ddfd6e2591a575887ad32725abd84` |
| `work/record128.json` | 60511 | `4d718f09978c5b0f86723343cf14f70607ef4c6261d52ec97da98a3dbbc1b188` |
| `work/record128.py` | 25532 | `90fe4f48eb2aee41a1b106d31e3dd5801e2dd01208e1b12f6e9e56047d28ccbd` |
| `SP02_CW_10+12/progress.log` | 12070 | `73e5c07a82dbbc5e82799c30f65a074fa330302a1f762e74b491383877a0dcb9` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |

## Scope

One bounded metadata/projection/AST/lexical pass under the strengthened shared validators. No image or header access, witness prose/context inspection, source-edit replay, reading judgment, TeX compilation, audit/freeze, assembly, packaging or upload.

Only this report and its companion JSON were written. No checkpoint refresh was performed after scan 128 finalization.
