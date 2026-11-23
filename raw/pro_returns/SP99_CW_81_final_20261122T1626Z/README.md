# SP99_CW_81 — consolidated diplomatic transcription

Scans 012–026 of cote 81: 15 pages accepted; 15 independent second readings adjudicated. The prescribed box lists contain 342 regions. Completed comparisons contain 324 token-different boxes, of which 27 led to an amended reading. Overlapping boxes are not distinct correction places. Macro syntax, different amounts of adjacent context, and independently drawn TikZ coordinates can produce token differences without a textual change.

## Reading the deliverable

- `pages/` contains the current consolidated page fragments. `SP99_CW_81_transcription.tex` concatenates them in scan order under one cote marker. `PREAMBLE.tex` supplies the conventions; the combined file itself has no preamble.
- `SP99_CW_81_changes.md` gives witness readings, decisions, crop coordinates, confidence levels, counts and consequential corrections. Resolving a C doubt counts as a change; adding uncertainty to an unchanged primary reading does not. Macro-only differences do not count.
- `SP99_CW_81_collation.tsv` contains the differences from H. H's page number is our scan number minus one; scans013 and014 have no H text and therefore no H collation rows.
- `SP99_CW_81_doubts.md` contains the notation review, unresolved readings, abbreviations and legibility assessment. A primary reading inside an uncertainty marker is not a certified correction.
- `SP99_CW_81_inventory.csv` records all inventoried page elements; every entry is transcribed. The notes separately identify excluded incidental or non-authorial material.
- `SP99_CW_81_notes.md` and `CHECK_EVENTS.tsv` distinguish the manuscript's claims from the mathematical checks actually performed. Clear slips and unfinished expressions remain in the transcription.
- `SP99_CW_81_hand_log.md` and `SP99_CW_81_sheet_feedback.md` record observed handwriting habits and local refinements of the supplied error sheet.

## Audit trail

`second/` retains each neutral coordinate list, the first reading, the independently committed second reading, literal token comparison and root adjudication. Neither independent TSV is rewritten to conceal disagreement. `records/` contains the structured first, accepted and audit records used to build the reports. `drafts/` preserves the historical first-stage page snapshots; the final authority is `pages/`. Saved crops accompany the evidence. Scripts perform cropping, packaging, literal collation or structural checks; they do not recognize handwriting or decide readings.

The handwritten text and drawings were inspected visually; no OCR or external mathematical research was used. Genuine drawings were reconstructed manually in TikZ, and running text was retained as text. No TeX compilation was performed, as requested. `progress.log` records page acceptance, independent commitments, audits, scheduled checkpoints and the final transcription freeze. `TRANSCRIPTION_SHA256.tsv`, when present, fixes the fifteen final page files and combined fragment. `FILE_MANIFEST.tsv` lists the archive's other member hashes; it excludes itself to avoid a circular hash.

The original scans, witness files, attached prompts and previous checkpoint archives are deliberately absent; they remain in the supplied source package. Earlier checkpoint ZIPs were never overwritten or nested.
