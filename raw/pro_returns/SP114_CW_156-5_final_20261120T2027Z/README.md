# SP114_CW_156-5 — consolidated diplomatic transcription

This package concerns archive scans 26–33 of cote 156-5, handwritten pages 25–32. The supplied whole-page and half-page images are the primary evidence. Witnesses C and H, and the one in-range row of witness S, are comparison witnesses. No external research, OCR, text-recognition library, PDF text layer, or TeX compilation is used.

## Deliverables

- `pages/`: one diplomatic LaTeX fragment per scan, using the supplied edition's macros.
- `SP114_CW_156-5_transcription.tex`: the page fragments in archive order, without a preamble.
- `SP114_CW_156-5_changes.md`: substantive differences from C or H, crop evidence and confidence; separate certainty decisions; retained doubts; second-reading corrections.
- `SP114_CW_156-5_collation.tsv`: only substantive differences from H, in the requested column schema.
- `SP114_CW_156-5_inventory.csv`: page elements and their transcription status.
- `SP114_CW_156-5_doubts.md`: shared notation, unresolved readings, abbreviations and legibility assessment.
- `SP114_CW_156-5_notes.md`: brief English notes, including the distinction between visible authorial slips and mathematical repairs.
- `CHECK_EVENTS.tsv`: actual mathematical checks and uses, with no claim that transcribing a statement proves it.
- `SP114_CW_156-5_sheet_feedback.md` and `SP114_CW_156-5_hand_log.md`: error-category feedback and observations of this hand.
- `progress.log`: start, assignments, completion/audit events, checkpoints and final transcription hashes.
- `second/`: precommitted box coordinates and first readings, independent blind readings, literal token comparisons and final adjudications.
- `crops/`: image evidence, in original whole-page coordinates as documented in the reports.
- `review/`: reader returns, main-reader decisions, coverage records and structural validation.
- `scripts/`: reproducible packet preparation, documentation assembly, literal token comparison, structural checking and packaging.

The original input scans, witnesses and context are deliberately not copied into this archive. The attached source ZIP remains necessary to reproduce crops or reconstruct packets. Paths beginning `source/` refer to that ZIP extracted once in the task workspace; `deliverable/` is this package's working root. Some independent reader records retain those working paths. The final changes and collation files use package-relative crop paths.

## Reading and counting conventions

A substantive locus is counted once in the total, and can count against both C and H. Macro-only differences are excluded. Changes of certainty alone are documented separately and do not inflate substantive totals. When a preferred reading remains uncertain, the change count compares that preferred reading with the witness; alternatives and confidence remain explicit. The requested LaTeX `\unsure{...}` marks describe uncertainty in the ink, not a mathematical objection.

A broad cancellation is represented as a deleted passage even when its crossing strokes do not physically touch every letter; small local deletions are scoped to the visible strike. Surviving punctuation and interlinear additions are distinguished. The inventory records the spatial elements separately, including insertions inside cancelled material.

Confidence is a qualitative judgment of legibility, not a statistical probability. A formula's expected mathematical form is recorded only in the notes when it differs from clear ink. The meaning assigned to an ambiguous recurring sign is reviewed across these eight pages; no conclusion from another cote is imported without checking the present images.

## Reproduction and verification

`python3 scripts/assemble.py` assembles the human-readable logs and combined fragment from the main-reader adjudicated records. `python3 scripts/metadata.py` assembles the hand log and check-event table. `python3 scripts/compare_second.py` compares already-written first and blind second readings token by token; it chooses no reading. `python3 scripts/validate.py` checks structure and coverage without invoking a TeX engine. The edition's `PREAMBLE.tex` is supplied in the original source package and is not duplicated here.

The blind readers receive only the assigned page images and box-coordinate list, plus procedural instructions to use the edition's macros. They do not receive the first-reading file, C, H, the main page, or its notes. Each blind reader is different from that page's first reader. The comparison files retain raw token differences, including harmless formatting differences; the main reader records their adjudication.

The final `progress.log` is authoritative for which stages are complete and for the frozen hashes. Reader drafts in `review/` preserve the history; the delivered transcription is `pages/` and the combined fragment.


## Final audit and evidence provenance

All eight blind audits are complete in the current records:224 precommitted boxes,196 boxes with raw token differences, and71 adjudicated changes of physical loci. Raw token differences include formatting and excerpt-boundary differences; changed physical loci also include revised certainty or alternative readings. Those counts are distinct from the300 substantive comparison loci. The per-page records preserve their separate definitions and decisions.

Fresh blind readers completed030 and031 after earlier reader work was interrupted. They received only their permitted image/box inputs and procedural instructions. Both earlier and fresh crop sets remain in the package. The seal verification report distinguishes16 unchanged first-reading/box TSV files from8 verified pre-audit page hashes; the current pages appropriately incorporate later adjudications. Checkpoint02's617 paths and checkpoint01's274 paths all remain present. See `review/seal_and_checkpoint_path_verification.json` for the verification method and exact hashes.

The saved crops underwent lossless PNG recompression only. All561 files retained their filenames, dimensions, image mode, decoded-pixel SHA-256 and non-IDAT chunks;487 smaller encodings saved33,532,926 bytes. `review/lossless_png_recompression_01.json` records per-file byte counts and verification hashes. Historical checkpoint ZIPs were not altered. The reproducible compressor is `scripts/lossless_png_recompress.py`.
