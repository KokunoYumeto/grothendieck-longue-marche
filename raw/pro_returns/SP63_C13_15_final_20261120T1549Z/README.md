# SP63_C13_15 — consolidated diplomatic transcription

This package contains all 25 supplied scan pages, read in the requested order by one reader and then audited again in that order. The reading decisions are based on the supplied images and the two supplied draft witnesses. No OCR, outside source, or TeX compilation was used. A separate mechanical checker inspected files, records, delimiters, tables, and hashes without reading the scans or adjudicating the mathematics.

## Principal files

| File or directory | Contents |
|---|---|
| pages/ | One consolidated LaTeX fragment for each scan, named as in C. |
| SP63_C13_15_transcription.tex | Exact concatenation of the 25 page fragments, separated by one additional newline; no preamble. |
| SP63_C13_15_changes.md | Per-page and total counts, confidence counts, consequential corrections, every substantive differing place, image evidence, crop boxes, and remaining uncertainties. |
| SP63_C13_15_collation.tsv | The 410 places differing from H; no rows on its five absent pages. |
| decisions.tsv | All 77 supplied marks in their original order. |
| SP63_C13_15_doubts.md | Recurring notation, 75 remaining-doubt entries, decisions, abbreviations, and legibility assessment. |
| SP63_C13_15_inventory.csv | The 593 inventoried elements, with sheet and hand classifications. |
| SP63_C13_15_notes.md and CHECK_EVENTS.tsv | Page reports and the 14 recorded mathematical check/background events, with their precise scope. |
| SP63_C13_15_hand_log.md | Observations made while reading and the final review of their checked extent. |
| SP63_C13_15_sheet_feedback.md | Counts for all ten error kinds and recurring subcases for future passes. |
| progress.log | Actual UTC completion and audit entries, checkpoint history, freeze hashes, and final verification. |
| audit_notes.md | The root reader's second image audit, page by page. |
| STRUCTURAL_REPAIRS.md | Syntax-only boxing of cancelled blocks and small drawings; no changes of reading. |

## Supporting documentation

The records directory preserves the structured evidence behind the tables. The scripts directory preserves the page-recording, image-view preparation, assembly, final corrections, validation, hashing, and packaging code used in the work. The image-preparation script performs geometric Pillow operations only; no image is included in this package. The assessment and final-feedback text files are assembly inputs retained as documentation.

Page-recording scripts represent the first-pass recording stage. Do not rerun them over the delivered pages: they would append new completion entries and restore readings later changed by the documented final-review scripts. The delivered page files and records are the final state. The assembly script can rebuild the tables from that state. The supplied PREAMBLE.tex remains in the original attachment and is not duplicated here.

Two scheduled checkpoint archives were saved during the run under their own names. Neither is nested here. This archive includes all current deliverables and documentation from those checkpoints, with the final corrections and verification added. The original attachments, scans, halves, crops, compiled files, and nested archives are excluded.

All counts describe the recorded places or entries, not numbers of characters or a claim that the remaining doubtful strokes have become legible. The in-place uncertainty marks and corresponding evidence remain part of the transcription.
