# MPL_67_002-052 — technical file record

## Contents

The transcription contains all 46 supplied nonblank scan pages of cote 67, in order from 002 to 051. Scans 015, 022, 023, 047 and 052 were omitted as blank in the supplied selection. The root transcribed and audited the images in one stream; research agents worked only on contextual and technical support.

| File or directory | Contents |
|---|---|
| `MPL_67_002-052_transcription.tex` | Ordered combined LaTeX fragment, without a document preamble |
| `pages/` | One LaTeX fragment for each of the 46 scans |
| `MPL_67_002-052_doubts.md` | Notation table, 333 uncertainty occurrences, abbreviation glossary and legibility assessment |
| `MPL_67_002-052_inventory.csv` | 741 element records; every row has `transcribed=yes` |
| `MPL_67_002-052_notes.md` | 76 research items, including six title/page-count items, plus the standing section on the manuscript’s own unverified steps |
| `CHECK_EVENTS.tsv` | 242 events, with the statement, date, actor, actual kind of check or use, and outcome |
| `progress.log` | Page completion and audit records, transcription hashes, context-opening time and subsequent package events |
| `records/` | Verification reports, research evidence and calculations, independent reviews, checkpoint receipt and procedural scripts |

## Transcription identity and mechanical verification

The transcription was frozen at **2026-11-18 00:48:20 UTC**, before the context was opened at **00:48:27 UTC**. The manifest `records/transcription.sha256` records the 46 page files and their combined fragment. The combined fragment’s SHA-256 is:

```
f8fe3b2a869c9ad4aefaa16d86352cc163d53be440181995ff69d34b2cc6daa0
```

The final structural report, `records/final_technical_validation.json`, was produced at **2026-11-18 01:27:47 UTC**. It records the following results:

| Check | Result |
|---|---|
| Required page files | All 46 present, with the required scan markers |
| Recorded completion and audit events | 46 completion events and 46 audit events |
| Combined fragment | Byte-for-byte equality with the ordered concatenation of the page files |
| Inventory | Required schema; 741 rows, all marked `yes` |
| Doubts | Notation precedes the doubts table; 333 recognized rows corresponding to 333 uncertainty macros |
| Syntax report identity | Every per-page report matches its delivered source hash |
| Frozen files | All 47 SHA-256 values unchanged |
| Errors in this structural check | None |

The remaining annotation-count warnings concern the grouping of drawings on scans 004 and 010 and the address margin on scan 013. Their element-to-wrapper correspondence is documented in `records/inventory_grouping_resolution.md`; the inventory records 218 deletions, 138 insertions and 18 diagrams. The compiler and structural checks establish file properties and recorded-event coverage. The reading assessments remain those of the image transcription and audit, with their doubts retained in place.

## Typesetting and compilation scope

The requested transcription is a fragment: its editorial macros, standard LaTeX and TikZ/TikZ-CD support must be supplied by a document wrapper. `records/compile_qa.py` preserves the optional syntax-check harness. That harness treats editorial wrappers transparently and supports arrays and TikZ-CD within the diagram wrapper.

The recorded XeLaTeX checks used `--no-pdf`. All 46 page checks succeeded; the consolidated report is dated 2026-11-18 00:45:18 UTC. The combined-fragment check succeeded at 00:46:21 UTC. Neither check reported missing characters. Scans 011 and 013 each generated two font-substitution warnings. The combined check recorded two font warnings, nine overfull boxes and two underfull boxes.

An earlier PDF-output attempt encountered an `xdvipdfmx` assertion. No PDF or PDF-layout verification is delivered. A historical `pdf_exists` field in the syntax reports records filesystem presence from earlier attempts; the same reports explicitly record `pdf_generation_requested=false`. It must not be read as successful PDF production or inspection.

## Research evidence and preserved work records

Each research item names its source scan and brief source wording, records the comparison with the supplied context, and identifies relevant research-register entries with their stated status. `records/context_search_ledger.tsv` preserves 10,673 search-hit records. The three context evidence ledgers preserve the agents’ locators and scope qualifications. Explicit calculations and proof checks are in `records/research_checks.md`, `records/check_calculations.py` and `records/calculation_results.json`; the independent reviews are in `records/orange_obstruction_review.md` and `records/coordinate_checks_review.md`. Their scope is also recorded in `CHECK_EVENTS.tsv`. Reading alternatives suggested after the freeze appear only in the notes.

The earlier `records/pre_freeze_validation.json` and `records/technical_validation_after_freeze.json` are dated snapshots; the final report above records the delivered inventory. `records/research_leads.md` preserves provisional leads from the transcription stage. The developed notes and check events record their later treatment.

`records/scripts/` preserves 12 historical page-save scripts, with a provenance README and manifest. They may contain earlier readings and must never be rerun over the frozen page files. Other save, audit, assembly and inventory scripts are retained as procedural records; their presence does not authorize altering the delivered transcription. Scripts that search the supplied context require those input sources at the workspace paths used during this run.

The archive excludes the supplied scans and context sources, earlier ZIP archives, and Python cache files. The ZIP contains the deliverables and their work records directly at its root.
