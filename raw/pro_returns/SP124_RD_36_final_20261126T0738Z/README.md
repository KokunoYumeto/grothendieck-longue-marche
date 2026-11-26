# SP124_RD_36 diplomatic transcription and visual apparatus

Scope: cote 36, supplied scans 044–064. This edition follows the supplied scan order. The combined TeX is a fragment intended for the supplied PREAMBLE.tex; the original preamble and source witnesses are not duplicated in this package.

## Files and evidence

- `pages/`: finished page fragments; completion events are in `progress.log`.
- `SP124_RD_36_transcription.tex`: the finished page fragments in scan order.
- Changes, collation, mark decisions, inventory, doubts/notation, notes, hand log and error-sheet feedback form the apparatus.
- `records/36_scanNNN.json`: per-page reading records, reader assignment, source-line estimate, decisions and visual review evidence.
- `second/`: neutral box lists, preserved first readings, independently written second readings, exact token comparisons and main-reader adjudications.
- `crops/CROPS.tsv`: crop filenames and original-scan pixel coordinates. The separate crop ZIP contains the image evidence once.
- `CHECK_EVENTS.tsv`: actual mathematical checking events. Reading a source assertion is not recorded as a proof check.

## Reproduction and integrity

All crop work uses Pillow without text recognition. The source scans are read at native resolution; enlarged crops use grayscale, autocontrast, LANCZOS and unsharp masking. The manifest distinguishes wide context views from small decisive details. Source text was not researched externally and no TeX compilation was used.

`scripts/crop.py` documents the crop transformation. `scripts/assemble.py` builds the apparatus from visually reviewed records. `scripts/audit_compare.py` compares exact TeX/word/punctuation tokens, ignoring whitespace only; it does not decide reading differences. `scripts/package.py` creates unique packages without the source scans, witnesses, overlapping halves, earlier ZIPs, or repeated crop images.

For reconstruction, put the original archive contents under `source/` beside a directory named `work/` containing this package. The per-page record paths and crop manifest preserve the original coordinates. First-pass packets and overlapping halves can be recreated from the supplied source files; they contain no unique deliverable. The first progress-log line establishes the checkpoint interval. Checkpoint ZIPs are saved at 45-minute intervals and are not nested in later packages.

After visual review and blind comparison, SHA-256 digests of all page fragments and the combined fragment are written to `progress.log` and checked again before delivery.

## Completed audit

All 21 page audits are closed. The independent image-only readings cover 421 boxes; root adjudications address all 377 exact-token differences. The approved transcription changes in 167 boxes after that comparison, including local uncertainty and encoding refinements. All 168 supplied witness-C doubt marks have a decision record.

The final witness-attribution review records 686 correction loci: 399 against C and 496 against H. A locus may affect both witnesses. The 286 remaining doubt entries and 728 inventory elements are recorded in the apparatus. Seven wrapper-only or already represented observations were removed from correction counts and preserved in the per-page records. `records/final_count_review.json` documents that metadata review and the unchanged page hashes.

The dated QA reports and implementation scripts document successive states of the work. Their earlier counts and proposed fixes are historical. The current `pages/`, assembled apparatus, per-page records and adjudications contain the approved result. `records/final_validation.json` records the final consistency checks; `records/frozen_hashes.json` and `progress.log` record the 21 page hashes and combined-transcription hash.
