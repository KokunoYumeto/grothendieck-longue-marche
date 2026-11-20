# Scan 132 mechanical QA

Checked: 2026-11-20 03:33:25 UTC  
Recorded finalization: 2026-11-20 03:31:42 UTC  
Page: `B10-10_10_scan132`

## Result

PASS for all performed checks.

Page size is 2,368 bytes. All 15 actual root JSON fields match the finalized record. Stored page hash and record/map identity agree.

| Metadata | Count |
|---|---:|
| edits | 11 |
| asserted replacement occurrences | 11 |
| changes | 23 |
| against C | 12 |
| against H | 22 |
| confidence counted loci | {"high": 12, "medium": 8, "low": 3} |
| crops | 48 |
| inventory | 18 |
| inventory extra rows | 5 |
| inventory other resolved rows | 13 |
| inventory all yes | True |
| remaining doubts | 10 |

## Checks

Record schema/accepted flags, inventory IDs/state, exact inventory and collation rows/headers, the changes count row/full page section and doubt rows passed. The five explicit extras occur once each, leaving 13 other resolved inventory IDs. This partition was checked solely from finalized/root metadata. Reading fields were processed only as opaque values.

All 48 crop recipes passed geometry/parameter and safe source-path checks, and all change-row references resolve. Images and headers were not opened; actual source pixel extents were not checked.

Root-script AST: PASS. TeX lexical: PASS; {"brace_pairs": 36, "environment_pairs": 1, "math_pairs": 16}. Declared edits were counted but never replayed.

## Input protection

All 14 input fingerprints were unchanged: the four root/page/record inputs, progress/CHECK_EVENTS, four generated reports, and four helper code files. Changes: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan132.json` | 35678 | `2c6007ffa3b88bddf5982e6d7f992ed6c8ae1c191f45e2126377820fda5de01b` |
| `SP02_CW_10+12/pages/B10-10_10_scan132.tex` | 2368 | `87d3fa6d5225be6390bdce2b7bcd7a9c3042586586ec3cc8840299d38e01cc46` |
| `work/record132.json` | 29901 | `2cee952f24e0cfd0463dfbd434c048c050e0f548033e080429c3f1fd49994596` |
| `work/record132.py` | 11196 | `8c375b4865b85fb366e87299f60364f75f317a8f4f93d494bc281ffddb1e34e0` |
| `SP02_CW_10+12/progress.log` | 12720 | `a7c19814ff052413ed81b754953175619da21e26a6675ae4f82308c8c5be5985` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |
| `SP02_CW_10+12/SP02_CW_10+12_inventory.csv` | 403711 | `e56c3cbf08d031f931ac86aab2f7928bc68a24c5e9babd40d838272c6a60225a` |
| `SP02_CW_10+12/SP02_CW_10+12_collation.tsv` | 700936 | `de8d957dc4071ce7833e5ec03e91cbfd8078fb8a4aed8f3fcfa9140e83c3f5db` |
| `SP02_CW_10+12/SP02_CW_10+12_changes.md` | 784082 | `808d836f853a7863cfc1859a1689c70ba3b5bd9a2196c09bac5e947a358ac514` |
| `SP02_CW_10+12/SP02_CW_10+12_doubts.md` | 119935 | `c0f984e174f62610d9adc3ba103406677f4c8a778c9bcb07883f2d8f4907cccb` |
| `SP02_CW_10+12/scripts/record_page.py` | 31648 | `ba5e962b8102702843b2a5228c0457bf0411c8e6e76149633b6c7e7a3f4a4a37` |
| `SP02_CW_10+12/scripts/validate_tex.py` | 10712 | `2a7ea5e1bd32176b7e6d286330c49dc79603e8feb009265dd41b0ee548cf0033` |
| `SP02_CW_10+12/scripts/render_crops.py` | 6848 | `d96eac6accd3a904de7c18b1ab29305636e883ca665a0521097e7a7c71781362` |
| `SP02_CW_10+12/scripts/crop_metadata.py` | 3431 | `2c1b67477e9aa43563cd714a2b7dfbc57c15299ee15f2d6935602833395add34` |

## Scope

Bounded finalized metadata/schema, opaque report projections, AST and lexical TeX only. No source replay, image/header, witness prose, context, reading decisions, next-page inspection, compilation, refresh, audit/freeze, checkpoint staging/package or upload.

Only these scan132 QA Markdown/JSON evidence files were written.
