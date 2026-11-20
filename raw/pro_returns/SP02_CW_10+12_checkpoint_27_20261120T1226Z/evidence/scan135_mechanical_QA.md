# Scan 135 mechanical QA

Checked: 2026-11-20 04:15:57 UTC  
Recorded finalization: 2026-11-20 04:13:23 UTC  
Page: `B10-10_10_scan135`

## Result

PASS for all performed checks.

The page is 5,427 bytes. All 15 actual root fields match the finalized record. The bounded in-memory builder exactly reproduces root JSON: True. The prepared fragment equals the final page byte-for-byte: True.

| Metadata | Count |
|---|---:|
| edits | 24 |
| asserted replacement occurrences | 24 |
| changes | 39 |
| against C | 25 |
| against H | 37 |
| confidence counted loci | {"high": 29, "medium": 9, "low": 1} |
| crop documents | {"crop_base": 83, "crop_extra": 13, "crop_extra2": 2} |
| crops | 98 |
| inventory | 48 |
| inventory all yes | True |
| remaining doubts | 9 |
| notation updates | 9 |
| abbreviations | 7 |
| inventory overrides | 9 |

## Checks

Imports/sys.path mutation removed from AST; observed pure builder calls restricted; recipe reads served only from three captured JSON streams; Record.save captured in memory without writes.

Schema and accepted values, stored identity/hash, exact inventory/collation/change/doubt projections, crop uniqueness/reference resolution, finite geometry/parameters and safe source paths passed. All 83+13+2 recipe entries match the final record by ID. Reading values were handled only as opaque data. Edit lists/counts agree across script reconstruction, root JSON and final record; no witness-based edit application was replayed.

AST: PASS. TeX lexical: PASS; {"brace_pairs": 121, "environment_pairs": 10, "math_pairs": 63}.

## Prior-file and input protection

All 162 prior finalized page/record files match their saved checkpoint16/QA134 hashes and stayed unchanged during this pass. All 21 other used input fingerprints also stayed unchanged: 183 protected files total. The full prior-file hash mapping is in the companion JSON.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan135.json` | 71930 | `9474d7970f770dd3554fba86e2e52010924aa8e78bdc5bb30ff0cef39a44e225` |
| `SP02_CW_10+12/pages/B10-10_10_scan135.tex` | 5427 | `af991e465a917cf0b08733fd7ce043e39815aa1faaa2687517ad240a0b3c3678` |
| `work/record135.json` | 58063 | `590ae6e707453a53ecc4ab3d7f9f7e7b535f489e7c3dcc15c3002ed907d28e39` |
| `work/record135.py` | 22221 | `214900271ec536a955e963e1d4f33257f96ab04a143c39ce5d433182cf78c1d8` |
| `work/prepared135.tex` | 5427 | `af991e465a917cf0b08733fd7ce043e39815aa1faaa2687517ad240a0b3c3678` |
| `work/crops135.json` | 15725 | `a222eef24d4de11e0c57685ecb0ec38aab3af4ec45b2d92dedda65e4e4f744b2` |
| `work/crops135_extra.json` | 2514 | `9d1becae10c5c66dbb565afddc3efd4631481b305571cc3243dbf10b2f289cfd` |
| `work/crops135_extra2.json` | 397 | `b45ef480872c797e200b67401cb9b0e89710e95b50b2252e25359ec2040c4b7a` |
| `SP02_CW_10+12/progress.log` | 13359 | `f935575f47fd1a82f60f0487e04a78674c0e8cdaa5be0c2796081dab4e66cfce` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |
| `SP02_CW_10+12/SP02_CW_10+12_inventory.csv` | 415173 | `5a3eba87ca94cbd70b473ad8ac01073756d41b88235fd4085ffe87c7433778f1` |
| `SP02_CW_10+12/SP02_CW_10+12_collation.tsv` | 731369 | `7c637e758d737f02f77ab67fc451aeefe32caffb7a5c3a80dfe571470f834517` |
| `SP02_CW_10+12/SP02_CW_10+12_changes.md` | 819375 | `354e44bbbf9528527542f6352579c7f01431f0d20f37090d79004fe565dfe912` |
| `SP02_CW_10+12/SP02_CW_10+12_doubts.md` | 128608 | `98d7987236c2695b2b9d734780929bad94b8816a7119496b616def8bbcd94ef8` |
| `SP02_CW_10+12/evidence/scan134_mechanical_QA.json` | 11309 | `07118a7ddea015b281db7f3fda5a395e8b758e272beed748884bca722c205f24` |
| `SP02_CW_10+12/evidence/checkpoint16_preparation_080.json` | 39043 | `fc5fcc5ebd560c519f0089ceb7383f7bc0aee7021d6712f79710fa8fff758233` |
| `SP02_CW_10+12/scripts/record_page.py` | 31648 | `ba5e962b8102702843b2a5228c0457bf0411c8e6e76149633b6c7e7a3f4a4a37` |
| `SP02_CW_10+12/scripts/validate_tex.py` | 10712 | `2a7ea5e1bd32176b7e6d286330c49dc79603e8feb009265dd41b0ee548cf0033` |
| `SP02_CW_10+12/scripts/render_crops.py` | 6848 | `d96eac6accd3a904de7c18b1ab29305636e883ca665a0521097e7a7c71781362` |
| `SP02_CW_10+12/scripts/crop_metadata.py` | 3431 | `2c1b67477e9aa43563cd714a2b7dfbc57c15299ee15f2d6935602833395add34` |
| `SP02_CW_10+12/scripts/root_record.py` | 1681 | `6ac1e9d42564fc6063349618c1c2945a562825df621975aa1d1f55e8a2441918` |

## Scope

Bounded metadata/schema, opaque projections/prepared-byte equality, AST/lexical and in-memory reconstruction of root-authored JSON only. Prior finalized pages/records accessed as raw hash bytes only. No images/headers, witness prose, source replay, context, reading decisions, next-page inspection, compilation, refresh, audit/freeze, staging/package/upload.

Actual image pixel extents were not checked. Only these bounded QA reports were written; checkpoint17 was not staged.
