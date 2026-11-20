# Scan 130 mechanical QA

Checked: 2026-11-20 03:14:42 UTC  
Recorded finalization: 2026-11-20 03:13:52 UTC  
Page: `B10-09_10_scan130`

## Result

PASS for all performed checks.

The page is 3,893 bytes. All 15 actual root JSON fields agree with the finalized record after the existing cote/scan normalization. The record/map identity and stored page hash agree.

| Metadata | Count |
|---|---:|
| edits | 22 |
| asserted replacement occurrences | 24 |
| changes | 53 |
| against C | 20 |
| against H | 50 |
| confidence counted loci | {"high": 41, "medium": 11, "low": 1} |
| crops | 95 |
| inventory | 65 |
| inventory all yes | True |
| remaining doubts | 11 |

## Checks

Shared record schema, accepted change flags/kinds/confidences, inventory identity/state and crop references passed. Inventory/collation headers and exact page rows, the changes count row and complete page section, and all page doubt rows agree with record projections. Reading values were processed only as opaque data. Every crop reference resolves; recipe geometry/parameters and safe existing source paths passed without image/header access. Source pixel bounds and source-C hash contents were not independently checked.

Root script AST: PASS. TeX lexical: PASS; {"brace_pairs": 91, "environment_pairs": 2, "math_pairs": 68}. Edit counts are declared metadata only; no edits were replayed.

## Protected inputs

All 6 protected byte streams were identical before and after. Changed inputs: [].

| Input | Bytes | SHA-256 |
|---|---:|---|
| `SP02_CW_10+12/documentation/page_records/B10-09_10_scan130.json` | 82331 | `fb6efeb51fd2a0fdb454f35be7d7035b4c057cc3b6b4b27b9af272a320ea8247` |
| `SP02_CW_10+12/pages/B10-09_10_scan130.tex` | 3893 | `02b8a762d958031af521804eb576ea331d73ffe40ce2c723d6249c4986ad4322` |
| `work/record130.json` | 61238 | `9cad8363932092c1c4f5e34ab5665c618b3c638f322cec666e033e9edb6a2897` |
| `work/record130.py` | 21701 | `613b0a6727c1747b9be99ce4193563d5de5c33f62aad2f5a33382539ec420eb4` |
| `SP02_CW_10+12/progress.log` | 12600 | `2914a0cfc8556bdcfc682a79a2929138c6303305d4381e01af04c4bec7af0e60` |
| `SP02_CW_10+12/CHECK_EVENTS.tsv` | 35 | `dd24c34e0a87d344d18048d222591ae12e50f7db7f224d9deaebf0243bc1241d` |

## Scope

Bounded metadata, exact opaque report projections, AST and lexical structure only. No images/headers, witness prose, research/context, source-edit replay, reading judgments, next-page inspection, compilation, output refresh, audit/freeze, packaging or upload.

Only the requested scan130_mechanical_QA Markdown and JSON reports were written. No helper or finalized output was changed.
