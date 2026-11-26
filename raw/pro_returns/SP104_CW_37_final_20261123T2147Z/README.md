# SP104_CW_37 — consolidated diplomatic transcription

The final reading is in `SP104_CW_37_transcription.tex` and the thirteen files in `pages/`. They are LaTeX fragments, without a preamble. The supplied preamble remains the external convention source.

Scans: 031, 034, 035, 039, 040, 041, 042, 043, 044, 045, 066, 067, 068. All thirteen pages have completed independent second-reading audits.

## Reports

- `SP104_CW_37_changes.md`: per-witness counts, consequential readings, source evidence, changed second-reading boxes and the complete saved-crop register.
- `SP104_CW_37_collation.tsv`: H differences on the seven pages with an H transcription; no rows for description-only pages.
- `SP104_CW_37_doubts.md`: notation, remaining alternatives, abbreviations and legibility assessment.
- `SP104_CW_37_inventory.csv`: every recorded element, in page order.
- `SP104_CW_37_notes.md`, `CHECK_EVENTS.tsv`: source claims and the limited mathematical checks actually performed.
- `SP104_CW_37_sheet_feedback.md`, `SP104_CW_37_hand_log.md`: error categories and observed notation/hand habits.

## Evidence and audit trail

The final counts are 82 definite correction places against C and 120 against H, covering 160 distinct places; overlap between witnesses is counted once in that last total. There are 28 separately classified certainty decisions. The independent reading covers 265 boxes, with 64 changed box readings after adjudication.

`second/` preserves the box lists, immutable first and independent readings, token comparisons and adjudications. `crops/` holds the saved image evidence; `records/crop_register.json` records the original source box and rotation of every saved crop. `records/`, `drafts/`, working notation and `scripts/` document the work; historical drafts and scripts do not supersede the final page files. Many adjudication scripts deliberately refuse a second run.

`progress.log` records completion, audits, checkpoints and the final hash verification. `TRANSCRIPTION_SHA256SUMS.txt` and `records/frozen_transcription.json` identify the frozen pages and combined file. No OCR, PDF text recognition, external research or TeX compilation was used. Attached sources and previous checkpoint ZIPs are excluded from this archive.
