# Scan 134 mechanical QA

Checked: 2026-11-20 03:58:20 UTC  
Recorded finalization: 2026-11-20 03:56:13 UTC  
Page: `B10-10_10_scan134`

## Result

PASS for all performed checks.

Page bytes: 3,094. All 15 actual root fields match the final record. The bounded in-memory root builder exactly reproduces the saved JSON: True. Root's prepared fragment exactly equals the final page: True.

| Metadata | Count |
|---|---:|
| edits | 15 |
| asserted replacement occurrences | 15 |
| changes | 25 |
| against C | 15 |
| against H | 25 |
| confidence counted loci | {"high": 17, "medium": 7, "low": 1} |
| crop base | 62 |
| crop extra | 10 |
| crops | 72 |
| inventory | 34 |
| inventory all yes | True |
| remaining doubts | 8 |
| notation updates | 9 |
| abbreviations | 5 |
| inventory overrides | 9 |

## Script, edits and projections

Imports/sys.path mutation removed from AST; observed call forms restricted; json.loads supplied as an in-memory decoder; recipe reads limited to two captured JSON streams; Record.save captured without writes.

Exact script/JSON/final-record edit-list agreement and exact root-prepared/final-page byte equality. The witness-based application was not independently replayed.

Schema, inventory state and exact inventory/collation/change/doubt projections passed. Reading strings were handled only as opaque data. All 62 base plus 10 extra recipes agree with the finalized recipe mapping. IDs are unique and every reference resolves. Coordinates/parameters and safe paths passed; no image/header was opened and actual source pixel extents were not checked.

AST: PASS. TeX lexical: PASS; {"brace_pairs": 75, "environment_pairs": 2, "math_pairs": 37}. Prior finalized133 page/record match saved QA hashes: {"page": true, "record": true}.

## Input protection

All 21 used input byte streams were unchanged. Changes: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan134.json` | 49274 | `deef44d5eda30e6488ee08c8ea16909d747efdaf7e04e65475ff884656ccc264` |
| `SP02_CW_10+12/pages/B10-10_10_scan134.tex` | 3094 | `dfaf63d33a9c2e9f37e764744096589c89043ef5efa694b76b441341f0c34193` |
| `work/record134.json` | 39229 | `9bcb1190302a2325d55bfb9808c87c3eed9d4bdb48d1f135fc300fb353618017` |
| `work/record134.py` | 13908 | `078098f67eddd68d4a576df255bd402519dcb5b2ec77465b80e7f81bb9680186` |
| `work/prepared134.tex` | 3094 | `dfaf63d33a9c2e9f37e764744096589c89043ef5efa694b76b441341f0c34193` |
| `work/crops134.json` | 11714 | `6d4149762bfe407b77f0c4a9ea721e2d93adf3bcd3fe141e92077208dbdab42e` |
| `work/crops134_extra.json` | 1928 | `da9fcb8e049d87a5b040ad87fcc6ebd9bef327a5dc2a6a73cad21f84e7681cbe` |
| `SP02_CW_10+12/progress.log` | 13299 | `f8987304fd361d9231f65bec3d424cfefa86684e096f87c11569870a112e0326` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |
| `SP02_CW_10+12/SP02_CW_10+12_inventory.csv` | 410723 | `09782bc991d14c58c2bdb028af99ba6663ce333ed740f1992d8ae8b577d1aaa0` |
| `SP02_CW_10+12/SP02_CW_10+12_collation.tsv` | 718985 | `528d86d18927981d7a6f29120e7077fd7afadfb0a5a32e9d84e9d1407dc70757` |
| `SP02_CW_10+12/SP02_CW_10+12_changes.md` | 805045 | `41b459f97e35dd1568bcabcc241daf312ee0deda6df626c11453722fe839ea25` |
| `SP02_CW_10+12/SP02_CW_10+12_doubts.md` | 125366 | `e50cb952b0ea5616becf949cb71a739ec1d9d7ceb39d25add767eaf51acd7f7e` |
| `SP02_CW_10+12/pages/B10-10_10_scan133.tex` | 3930 | `63b54770dec12fd2f11187ffe9827e9e99c90668ae2e2d2f14ca7dbb5677f7c6` |
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan133.json` | 63075 | `a5881e314d3c21c8e08491b5faab5edac31061206f1222a7e0bb304d86af5c88` |
| `SP02_CW_10+12/evidence/scan133_mechanical_QA.json` | 11299 | `b594ece6188ede70717972f27f015125c02ba49be478a264c73c66c726613303` |
| `SP02_CW_10+12/scripts/record_page.py` | 31648 | `ba5e962b8102702843b2a5228c0457bf0411c8e6e76149633b6c7e7a3f4a4a37` |
| `SP02_CW_10+12/scripts/validate_tex.py` | 10712 | `2a7ea5e1bd32176b7e6d286330c49dc79603e8feb009265dd41b0ee548cf0033` |
| `SP02_CW_10+12/scripts/render_crops.py` | 6848 | `d96eac6accd3a904de7c18b1ab29305636e883ca665a0521097e7a7c71781362` |
| `SP02_CW_10+12/scripts/crop_metadata.py` | 3431 | `2c1b67477e9aa43563cd714a2b7dfbc57c15299ee15f2d6935602833395add34` |
| `SP02_CW_10+12/scripts/root_record.py` | 1681 | `6ac1e9d42564fc6063349618c1c2945a562825df621975aa1d1f55e8a2441918` |

## Scope

Bounded metadata, opaque report/prepared-byte comparisons, AST/lexical and in-memory reconstruction of the root-authored JSON dictionary. No images/headers, witness prose, context, source-edit replay, transcription judgments, next-page inspection, TeX compilation, refresh, audit/freeze, checkpoint staging/package or upload.

Only these bounded QA Markdown/JSON files were written.
