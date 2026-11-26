# SP108_CW_109 — consolidated transcription

This package covers Montpellier cote 109, scans 033–038. The six finished page fragments are in `pages/`; `SP108_CW_109_transcription.tex` combines them in scan order with one cote marker and no preamble. The macros are those of the supplied preamble. That source file, the original images, and both witnesses are deliberately left out of this generated package.

The page fragments preserve handwriting states, local spelling, punctuation, notation, and unresolved readings. In a multi-alternative `\unsure` the first alternative is the reading used in the text. The archive foliation appears only in the permitted page comments.

## Completed results

All six pages received a first reading, primary crop adjudication, and an independent blind reading of their listed difficult places. The blind tables contain 385 boxes; the literal comparison produced 117 differences, each individually adjudicated. Thirty-eight boxes received a page amendment, including changes of uncertainty. The changes log records 37 final reading-change places against C: 22 with high, 7 with medium, and 8 with low confidence. These counts describe different stages of the recorded work and are not additive.

The transcription retains 82 in-place doubt marks. All 149 inventory elements are marked transcribed. H supplies descriptions only on these six pages, so its collation has a header and no data rows. Structural LaTeX and record checks passed without TeX compilation. The six page files and combined transcription were frozen by SHA-256 and subsequently verified unchanged.

## Editorial records

- `SP108_CW_109_changes.md`: changes against witness C, including resolved C doubts, with exact readings, crop boxes, visible evidence, confidence, and consequential corrections.
- `SP108_CW_109_collation.tsv`: H collation header. H supplies descriptions only for all six pages, so there are no data rows.
- `SP108_CW_109_doubts.md`: verified notation, all remaining in-place doubts, abbreviations, and assessment of legibility and witnesses.
- `SP108_CW_109_inventory.csv`: text blocks and individual handwriting states, ordered on each sheet.
- `SP108_CW_109_notes.md`: the writer’s statements and questions, and reading decisions involving mathematics or notation.
- `SP108_CW_109_sheet_feedback.md` and `SP108_CW_109_hand_log.md`: correction categories and observed handwriting habits.
- `CHECK_EVENTS.tsv`: header only. No mathematical proof, re-proof, computation, or formal certificate was carried out.

## Reading and audit trail

`progress.log` records page completion, blind audits, packaging, and the final transcription freeze. `reports/` contains first-reader material, primary decisions, and cumulative final records. Reports used to prepare the first committed pages can include primary amendments; the `_final.json` records track the consolidated decisions.

For every page, `second/` contains the coordinate box list, the primary reading written before comparison, the independent second reading, literal token comparison, and primary adjudication of every difference. Token comparison preserves characters and macros and ignores whitespace only. An adjudication may retain a reading while explaining a macro difference or the treatment of neighboring ink at a crop boundary.

All saved first-pass and second-pass detail crops are in `crops/`. Coordinates are always in pixels of the supplied whole scan. No OCR, text-recognition library, external source reconstruction, or TeX compilation was used.

`scripts/` contains the programs used for recording, literal comparisons, structural LaTeX checks, assembly, and packaging. These programs do not decide handwriting. `file_list.tsv` lists the generated files in the current package with byte sizes and SHA-256 hashes; it excludes its own row.
