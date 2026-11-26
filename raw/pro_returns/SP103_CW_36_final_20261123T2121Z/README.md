# SP103_CW_36 — Consolidated diplomatic transcription

Completed reading of archive cote 36, scans 016–027 (manuscript leaves 7–18), from the supplied images against witnesses C and H and the four relevant supplied sweep rows.

## Files

- `pages/`: twelve finished page fragments in scan order.
- `SP103_CW_36_transcription.tex`: their ordered concatenation, prefixed by `\cotefile{36}`, with no preamble.
- `SP103_CW_36_changes.md` and `SP103_CW_36_collation.tsv`: decisions, witness readings, confidence, crop evidence and blind adjudications.
- `SP103_CW_36_doubts.md`: reconciled notation, unresolved readings, abbreviations and legibility limits.
- `SP103_CW_36_inventory.csv`: all 515 recorded elements marked transcribed.
- `SP103_CW_36_notes.md` and `CHECK_EVENTS.tsv`: the source's claims and reservations, limited mathematical checks, and their actual check types.
- `SP103_CW_36_hand_log.md` and `SP103_CW_36_sheet_feedback.md`: local and cross-page observations for subsequent readers.
- `second/`: frozen first readings and boxes, independent second readings, literal token comparisons and main-reader adjudications.
- `crops/`: all first and second reading evidence crops.
- `reviews/`, `scripts/`, `work_scripts/` and `progress.log`: the work record and reproducibility materials.
- `history/`: two explicitly superseded early drafts recovered from checkpoint 01; finished readings are only in `pages/`.

## Counts and verification

There are 384 documented decision rows, with 127 substantive changes against C and 354 against H. The changes log separates confidence counts for each witness from all decision rows. Some retained doubts and sweep checks do not count as a change against either witness.

The independent second reading contains 324 original boxes, 257 raw token differences, and 87 changed boxes after main-reader adjudication. Whitespace alone is ignored by the comparison. Wrapper syntax and differing context can create a raw difference without a reading change. Five additional graphical corrections on scan026 concern originally equal boxes and are counted separately. Two changed scan027 boxes overlap the same uncertain prefix; box counts are not counts of unique lexical places.

The page and combined-file SHA-256 values are in `reviews/transcription_sha256.tsv` and `progress.log`; the final verification found them unchanged. Static checks verified structure and references. No OCR, external research, or TeX compilation was performed. The attached sources, witness copies, preamble and checkpoint ZIPs are excluded. To typeset later, use the supplied edition preamble and conventions; this archive contains fragments only.

The source's visible errors and incomplete text are preserved. Remaining alternatives are marked in place and explained in the doubts and changes files. Historical comparisons and patch records intentionally retain earlier readings as provenance, not competing final transcriptions.
