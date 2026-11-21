# SP78_C13_147 diplomatic collation

The authoritative text is in `pages/`, one LaTeX fragment for each requested scan, and in the combined `SP78_C13_147_transcription.tex`. The combined file has no preamble and uses the conventions of the supplied `PREAMBLE.tex`.

## Reading and evidence

Each page is read visually against witnesses C and H by one assigned reader, then its disputed or differing places are reviewed by the main reader on saved enlarged crops. The scan number is the filename number; H's page number is one less. Source slips, abbreviations, deletions and insertions are preserved. Uncertainty is retained in the text when the ink does not decide. The mathematical notes do not silently repair the transcription.

After all24 first readings were approved, three fresh readers wrote independent blind readings of all372 prescribed boxes, before comparison. Root personally examined every differing box. The frozen box lists, separately written first and second readings, token comparisons and explicit root adjudications are preserved in `second/`. A token comparison ignores whitespace only; differences caused solely by equivalent TeX encoding are still presented to the main reader for adjudication. Counts of second-reading differences refer to boxes with at least one differing token. Changes of certainty alone are recorded in the doubts, rather than counted as substantive witness corrections.

The source images are examined visually. No OCR, internet research, TeX compilation or rendering is used. Pillow is used to crop, enlarge, rotate and adjust contrast. Crop boxes in the logs refer to pixels in the original scan, before rotation or enlargement. The original source attachments and reproducible native-resolution halves are omitted from the archive as requested.

## Files

- `SP78_C13_147_changes.md`: substantive differences against either witness, evidence and confidence.
- `SP78_C13_147_collation.tsv`: differences against H, excluding macro-only differences.
- `decisions.tsv`: the indexed marks in the supplied order; unindexed doubts are recorded separately.
- `SP78_C13_147_doubts.md`: notation, unresolved readings, abbreviations and legibility assessment.
- `SP78_C13_147_inventory.csv`: page elements and transcription coverage.
- `SP78_C13_147_notes.md` and `CHECK_EVENTS.tsv`: manuscript claims, reading-related mathematics, and the exact scope of any checks actually performed.
- `SP78_C13_147_sheet_feedback.md` and `SP78_C13_147_hand_log.md`: error categories and observed handwriting habits.
- `crops/`: first-reading, review and independent-reading image evidence.
- `reader_returns/`: original proposals and reader reports. These are working records, not the authoritative final transcription.
- `reviewed/`: main-reader decisions used to assemble the logs; completed audit decisions are incorporated in these records.
- `second/`: box lists, independently written readings, token comparisons and adjudications.
- `scripts/`: reproducible assembly, comparison, structural validation and packaging tools.
- `progress.log`: UTC page completion, audit, checkpoint and final hash records.

The cross-page notation review is complete; its source resolutions and preserved historical snapshots are in `workflow/`. The final freeze records SHA-256 hashes of all page fragments and the combined transcription. Structural validation checks files, indices, marks, braces, evidence and audit coverage; it is not a mathematical proof or a compiled-typesetting check.
