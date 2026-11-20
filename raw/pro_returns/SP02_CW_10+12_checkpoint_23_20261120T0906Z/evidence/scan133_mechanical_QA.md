# Scan 133 mechanical QA

Checked: 2026-11-20 03:49:24 UTC  
Recorded finalization: 2026-11-20 03:44:18 UTC  
Page: `B10-10_10_scan133`

## Result

PASS for all performed checks.

The page is 3,930 bytes. All 15 actual root JSON fields match the finalized record. The bounded in-memory root builder reproduces the saved root JSON exactly.

| Metadata | Count |
|---|---:|
| edits | 23 |
| asserted replacement occurrences | 23 |
| changes | 41 |
| against C | 23 |
| against H | 39 |
| confidence counted loci | {"high": 28, "medium": 10, "low": 3} |
| crop base | 69 |
| crop extra | 15 |
| crops | 84 |
| inventory | 40 |
| inventory all yes | True |
| remaining doubts | 11 |
| notation updates | 9 |
| abbreviations | 4 |
| inventory overrides | 8 |

## Checks and protection

Imports and sys.path mutation removed from parsed AST; calls restricted to observed pure builder forms; Record.save captured in memory; Path.read_text allowed only for two pre-captured recipe JSON byte streams. No builder filesystem write or source-C access.

All 69 base plus 15 extra recipe entries match finalized recipes by ID; IDs are unique and every reference resolves. Geometry/parameters and safe paths passed without images or headers. Actual pixel extents were not checked. Schema, inventory and exact report projections passed. Script AST and page lexical structure passed. The prior finalized132 page and record match their saved QA hashes.

All 20 input byte streams remained unchanged. Reading values were handled only as opaque data; source edits were not replayed.

## Isolated QA retry

The initial wrapper omitted `json.loads` from its allowed call names, despite supplying the safe decoder. That checker-only omission was corrected. The script-to-JSON comparison then passed; the initial attempt is retained in the JSON history. No root file was corrected.

Only the in-memory root-script dictionary reconstruction was retried after adding json.loads to the QA allow-list. All 20 original input fingerprints were checked before and after; other successful checks were not repeated.

## Input fingerprints

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan133.json` | 63075 | `a5881e314d3c21c8e08491b5faab5edac31061206f1222a7e0bb304d86af5c88` |
| `SP02_CW_10+12/pages/B10-10_10_scan133.tex` | 3930 | `63b54770dec12fd2f11187ffe9827e9e99c90668ae2e2d2f14ca7dbb5677f7c6` |
| `work/record133.json` | 51382 | `fb0b1f21a6ecf3f4aa813f2922f591be42c7060b0b14da0254984e7faa42c691` |
| `work/record133.py` | 17897 | `1aa17b432b114892a3c2d01211de855e72cc23dc815ba382b430a619f057d942` |
| `work/crops133.json` | 12978 | `5497f477db5ca8421cbb4381369f401cd546d6798b146e2339603375097abb0c` |
| `work/crops133_extra.json` | 2872 | `eb0c21d1057e6d4ac89f2d2fe2271a9c1ff0f6263d2f01888823df7174d3d724` |
| `SP02_CW_10+12/progress.log` | 12780 | `612bb4ca15f58894c428f1d4d812fd3c939ddf94c76772849c6013a7ca6359f7` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |
| `SP02_CW_10+12/SP02_CW_10+12_inventory.csv` | 407495 | `c158a282b85e72b8bfe2743538102e10d352ec8b71a05e05bca44244afcc9c77` |
| `SP02_CW_10+12/SP02_CW_10+12_collation.tsv` | 711415 | `fe5bfa112a4a13e8a0993593e51894339f20003ea104b7dcadcbb3a91b5f72f2` |
| `SP02_CW_10+12/SP02_CW_10+12_changes.md` | 796313 | `2118cbd5ae86c792c3b859199e41970e4e42c6593922b0987a92f05bf3c7df92` |
| `SP02_CW_10+12/SP02_CW_10+12_doubts.md` | 122691 | `bb65aec289b381c6a166bbc1e23ba888a54f55d35c8109f51dbe110f9ed18101` |
| `SP02_CW_10+12/pages/B10-10_10_scan132.tex` | 2368 | `87d3fa6d5225be6390bdce2b7bcd7a9c3042586586ec3cc8840299d38e01cc46` |
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan132.json` | 35678 | `2c6007ffa3b88bddf5982e6d7f992ed6c8ae1c191f45e2126377820fda5de01b` |
| `SP02_CW_10+12/evidence/scan132_mechanical_QA.json` | 8864 | `2fa46ee75bab637f2488da6f7c8f842a47b9a42f74dce8d7124a6bf92a559214` |
| `SP02_CW_10+12/scripts/record_page.py` | 31648 | `ba5e962b8102702843b2a5228c0457bf0411c8e6e76149633b6c7e7a3f4a4a37` |
| `SP02_CW_10+12/scripts/validate_tex.py` | 10712 | `2a7ea5e1bd32176b7e6d286330c49dc79603e8feb009265dd41b0ee548cf0033` |
| `SP02_CW_10+12/scripts/render_crops.py` | 6848 | `d96eac6accd3a904de7c18b1ab29305636e883ca665a0521097e7a7c71781362` |
| `SP02_CW_10+12/scripts/crop_metadata.py` | 3431 | `2c1b67477e9aa43563cd714a2b7dfbc57c15299ee15f2d6935602833395add34` |
| `SP02_CW_10+12/scripts/root_record.py` | 1681 | `6ac1e9d42564fc6063349618c1c2945a562825df621975aa1d1f55e8a2441918` |

## Scope

Bounded metadata, exact opaque projections, AST/lexical and in-memory reconstruction of the root-authored JSON dictionary only. No images/headers, witness prose, context, source-edit replay, transcription judgments, next-page inspection, compilation, refresh, audit/freeze, checkpoint staging/package or upload.

Only the requested QA evidence was written.
