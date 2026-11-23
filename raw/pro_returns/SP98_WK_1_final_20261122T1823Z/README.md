# SP98_WK_1 — consolidated diplomatic transcription

Completed 2026-11-22 18:23:46 UTC.

All 23 supplied scan pages have a consolidated reading, a recorded first-pass approval, and a blind second reading by a different reader. The blind readings were saved with UTC receipts and SHA-256 hashes before comparison. Root adjudication records every comparison difference and its crop evidence.

## Contents

| File or directory | Purpose |
| --- | --- |
| pages/ | One finished LaTeX fragment per scan, in the original filenames. |
| SP98_WK_1_transcription.tex | All 23 fragments in scan order, preceded by the cote marker. No preamble or document wrapper. |
| SP98_WK_1_changes.md | Witness-difference tables, counts by witness and confidence, consequential readings, unresolved places, and every blind-reading adjudication. |
| SP98_WK_1_collation.tsv | The 636 recorded places differing substantively from witness H. |
| decisions.tsv | All 148 original MARKS decisions in their original order. |
| SP98_WK_1_doubts.md | Shared notation, remaining local doubts, abbreviations, and the legibility assessment. |
| SP98_WK_1_inventory.csv | 577 inventoried elements, all marked transcribed. |
| SP98_WK_1_notes.md and CHECK_EVENTS.tsv | Source descriptions and scoped mathematical checks, with 77 actual check events. |
| SP98_WK_1_hand_log.md | Page-local letter, sign and notation observations. |
| SP98_WK_1_sheet_feedback.md | Error-category counts and refinements for subsequent runs. |
| crops/ | 1350 saved first-pass and fresh blind-audit evidence crops. |
| second/ | Neutral boxes, immutable first and second readings, save/comparison receipts and token comparisons. |
| progress.log | Actual UTC approvals, audits, checkpoint records, and the24 transcription hashes with unchanged verification. |
| review/, records/, scripts/ | Working provenance, final validation, notation comparisons and the explicit adjudication scripts. |

## Reading and count conventions

The 684 substantive places comprise 181 differences against C and 636 against H; the two witness counts overlap. Macro syntax and certainty alone do not add substantive differences. Unresolved alternatives remain qualified in the text and are not reported as certain corrections. Blind-audit rows document the second reading without counting a witness difference twice.

The blind stage contains 754 targets, 591 comparison differences, and 150 changed targets. A target can cover several local readings; these figures are not token counts or error rates.

Use the supplied PREAMBLE.tex with the fragments. Original attachments, native halves and earlier checkpoint ZIPs are intentionally excluded. No OCR, external edition or literature, or TeX compilation was used. The final validation checks structure and record consistency; it does not claim typeset rendering verification.

Clear slips, short forms, cancellation/insertion layers, unusual punctuation and incomplete delimiters remain diplomatic source readings. Mathematical repairs are confined to explicitly scoped notes and check events. The final_manifest.json and frozen_hashes.json files under review record the final counts and SHA-256 values.

Scripts are records of this run. In particular, adjudicateNNN.py files have already been applied and must not be rerun on the completed archive. Historical first-reader counts remain provenance; final_counts in approved records and the exported summary tables are authoritative for the finished reading.

The records/ directory preserves immutable first-reader submissions. The review/1_scanNNN_approved.json records contain the current adjudicated readings and metadata. Their retained coverage, difference_rows, reading_checks, legacy counts and first_pass_status fields are explicitly scoped as historical first-pass provenance; status, audit_complete, final_counts and the exported deliverables describe the completed result. The saved second/*_first.tsv and second/*_second.tsv files retain the readings made before comparison and are not rewritten to match the final adjudication.
