# Scan 131 mechanical QA

Checked: 2026-11-20 03:24:22 UTC  
Recorded finalization: 2026-11-20 03:23:29 UTC  
Page: `B10-10_10_scan131`

## Result

PASS for all performed checks.

The page is 3,244 bytes. All 15 actual root JSON fields match the finalized record after existing cote/scan normalization. Stored page hash and record/map identity agree.

| Metadata | Count |
|---|---:|
| edits | 18 |
| asserted replacement occurrences | 18 |
| changes | 31 |
| against C | 20 |
| against H | 29 |
| confidence counted loci | {"high": 15, "medium": 11, "low": 5} |
| crops | 64 |
| inventory | 29 |
| inventory extra rows | 6 |
| inventory other resolved rows | 23 |
| inventory all yes | True |
| remaining doubts | 15 |

## Inventory and projections

All resolved element IDs are nonempty and unique. The six explicit extra-row IDs occur exactly once; 23 other resolved IDs remain, matching the root-reported 23+6 partition. This partition was checked from output/root metadata only; C inventory was not reopened. Inventory/collation schemas and exact page rows, change flags/counts/full section, and page doubt rows match the finalized record projections. Reading strings were compared as opaque data.

## Crop and syntax checks

All crop references resolve. Recipe coordinate/parameter validation and safe existing source-path resolution passed without image or header access. Actual source pixel bounds were not checked.

Root script AST: PASS. TeX lexical: PASS; {"brace_pairs": 74, "environment_pairs": 1, "math_pairs": 39}. Edit counts reflect explicit metadata only; no edits were replayed.

## Protected inputs

All 6 protected byte streams were identical before/after. Changes: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-10_10_scan131.json` | 52181 | `daf3f93e7cd1abd28327e2e98b86c1b4bcc37def4e23a52f32f857deb7a369f5` |
| `SP02_CW_10+12/pages/B10-10_10_scan131.tex` | 3244 | `5c14e58981df1431f052a63064d3c90f6dc05a89e1864ce7dc6139632fea3938` |
| `work/record131.json` | 43366 | `9037ddd30b641f8c7fb39c2b3f2529e12cf7cd71b87e6a31f32f23ed230c669e` |
| `work/record131.py` | 17623 | `445f38163ea76375004f2d62b195491b5d758ae6276f63ab91516cd546e2eeb3` |
| `SP02_CW_10+12/progress.log` | 12660 | `f731351d256582fe4a89ba099eff972a68505b5e443d8805703bc488eb32cc71` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |

## Scope

Bounded metadata/schema, opaque projections, AST and lexical TeX only. No image/header, witness prose, context, source replay, reading decisions, next-page inspection, compilation, output refresh, audit/freeze, package or upload.

Only the requested scan131_mechanical_QA Markdown/JSON reports were written.
