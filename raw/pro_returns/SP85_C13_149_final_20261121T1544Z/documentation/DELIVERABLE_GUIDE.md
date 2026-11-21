# Guide to the transcription and its records

## Which text to use

The current consolidated reading is in `pages/149_scanNNN.tex`. The combined fragment, `SP85_C13_149_transcription.tex`, contains those same pages in the supplied order after `\cotefile{149}`. Use the separately supplied original `PREAMBLE.tex` for the edition's macros. No preamble or original scan has been copied into this archive.

The supplied scans are 028, 029, 030, 031, 033, 035, 036, 037, 038, 039, 040, 041, 042, 043, 045, 046, 047, 048, 049, 050, 051, 052 and 053. Gaps in the supplied sequence have not been filled or reconstructed. H's page number is the scan number minus one. Authorial page numbers and thin secondary foliation are distinguished in the transcription and inventory.

## How to read the evidence

- `SP85_C13_149_changes.md` gives material differences from C or H, counts, confidence and consequential corrections. Its per-page second-reading tables also retain changed uncertainty and formatting decisions that are not new material C corrections.
- `SP85_C13_149_collation.tsv` contains the differences from H in the requested column order. Macro syntax alone is not a material difference.
- `decisions.tsv` follows the original MARKS order. A resolved mark has its crop and stroke evidence; an undecided mark retains the surviving reading or alternatives.
- `SP85_C13_149_doubts.md` begins with the notation table, then gives remaining local doubts, the abbreviations and the legibility assessment. An expansion in the abbreviations list is not part of the transcription.
- `SP85_C13_149_inventory.csv` records the page elements and their presence. `SP85_C13_149_notes.md` summarizes the pages and distinguishes written slips from mathematical expectations. `CHECK_EVENTS.tsv` records only checks actually performed, not ordinary transcription or image comparison.
- The hand log and sheet feedback identify local habits, exceptions and the witness errors associated with them. They are not universal replacement rules.

Every crop is derived from the original scan. Its filename and original-pixel box are retained in the associated records. The full-resolution halves were working aids and are deliberately omitted, as are the original scans and witness texts.

## Independent second readings

For each page, `second/*_boxes.tsv` gives the exact requested boxes and `*_first.tsv` gives the root reading frozen before assignment. The assigned agent received only the original image, box list and blind-reading instructions. It saved `*_second.tsv` before comparison. The comparison script tokenizes the two written readings without recognizing any image text. The root reader then viewed every differing crop and recorded its adjudication.

The frozen first TSVs are historical evidence. They deliberately retain readings that were later corrected; they must not be used as the current transcription. Their original hashes are checked against the assignment records. The final adjudication is in `*_adjudication.tsv`, with supporting JSON and a separate blind-reader report. Earlier `reader_returns/` likewise records first-stage proposals, including proposals the root rejected. Approved per-page `records/149_scanNNN.json` is the current source for the generated logs, notes and counts; the page TeX files hold the current text itself.

## Reproducibility and limits

The scripts are included as documentation of the work. The `adjudicate_*.py` files are one-shot mutation records, not scripts to rerun against the final archive. The comparison, bookkeeping, packaging and validation scripts do not perform OCR or make reading decisions. Some bookkeeping checks expect the original attachments to be unpacked beside this directory under `source/`; that dependency is intentional because the source attachments are excluded from deliverables.

The final validation checks coverage, ordering, referenced files, frozen blind inputs, literal TeX delimiter balance, prohibited illegibility in mathematical contexts, and agreement between the combined fragment and page files. It is not TeX compilation and does not claim to prove typesetting or mathematical correctness. The final freeze record and `progress.log` give SHA-256 hashes of all 23 page files and the combined fragment, followed by verification that those 24 files remained unchanged.

Periodic checkpoint archives were saved under new sequential names; their scheduled and actual times are recorded in `progress.log`. No checkpoint archive is nested inside another or inside the final archive. The final archive contains the deliverables, crops, second readings and documentation themselves.
