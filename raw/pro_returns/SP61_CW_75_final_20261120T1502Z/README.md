# SP61_CW_75 — Consolidated diplomatic transcription

## Scope

Montpellier cote 75, archive scans 16–25. The ten supplied sheets were read in order by the root reader against witnesses C and H, then read against their images a second time in the same order. H’s page numbers are one less than the scan numbers. The pencilled archive numerals 15–24 are retained in fragment comments and separately inventoried; no authorial date or page count was found on these sheets.

## Files

- `pages/`: one LaTeX fragment per scan, named as in C.
- `SP61_CW_75_transcription.tex`: the ordered combined fragment, with no preamble.
- `SP61_CW_75_changes.md`: differences from either witness, counts, consequences, unresolved places and every crop box.
- `SP61_CW_75_collation.tsv`: only the differences from H, in the requested schema.
- `SP61_CW_75_doubts.md`: notation table, remaining doubts, abbreviations, certainty decisions and trust limits.
- `SP61_CW_75_inventory.csv`: all recorded page elements, including the pencilled numerals.
- `SP61_CW_75_notes.md` and `CHECK_EVENTS.tsv`: page notes and the actual mathematical checks performed.
- `SP61_CW_75_hand_log.md` and `SP61_CW_75_sheet_feedback.md`: observed handwriting habits and error-sheet feedback.
- `SP61_CW_75_audit.md`, `progress.log`, `checkpoint_history.md`: the two-reading and checkpoint record.
- `reading_decisions.tsv`, `remaining_doubts.tsv`, `crop_register.tsv`: canonical supporting tables.
- `scripts/`: the actual recording, report-building, validation and packaging code. Per-page recording scripts document the first pass and must not be rerun over the finalized tables.
- `transcription_hashes.sha256`: the frozen page/combined hashes; the completion log records their final verification.
- `package_file_list.txt`: every file included in this archive.

## Editorial limits

Uncertain readings remain marked in place; spelling, abbreviations, contradictory direction words, incomplete sentences and possible mathematical slips are not silently corrected. Mathematical comments do not alter the transcription. Low-confidence differences are not presented as established errors. The final reports supersede first-pass choices where the audit records a revision.

The fragments use the supplied C macro vocabulary with standard LaTeX, TikZ and tikz-cd. No new preamble is supplied and no TeX compilation was performed. Mechanical checks verify file structure and internal records, not fidelity to the handwriting or rendered layout. The mechanical helper did not read images or witnesses. No OCR or outside research was used. This remains an AI reading with disclosed uncertainties.

No source scans, crops, witness files, input archives, earlier checkpoint ZIPs or generated caches are included.

Reports consolidated 2026-11-20 15:00:08 UTC.
