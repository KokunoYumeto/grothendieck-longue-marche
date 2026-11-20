# SP56_CW_63 consolidated reading

This archive contains the primary reader’s manually checked page fragments and the accompanying change, doubt, inventory, notation, mathematical-check and audit records. The source is the supplied set of 25 images; C and H are earlier AI drafts, not authorities.

## Method and status

All image reading and all reading decisions are performed sequentially by the same primary reader. A separate helper supplies only generic structural validation and packaging scripts and does not inspect scans or source readings. No OCR, external research or TeX compilation is used.

Completion and second-reading status are recorded per scan in progress.log and SP56_CW_63_audit.md. Checkpoints may be incomplete; only the final archive is the completed deliverable.

## Contents

- pages/: consolidated page fragments, named as in witness C.
- SP56_CW_63_transcription.tex: combined fragment, with one initial cotefile marker.
- SP56_CW_63_changes.md: actual reading differences, counts and crop decisions.
- SP56_CW_63_collation.tsv: differences against H’s source transcription only.
- SP56_CW_63_doubts.md: notation, remaining doubts and certainty-only decisions.
- SP56_CW_63_inventory.csv: page elements checked against the transcription.
- SP56_CW_63_notes.md and CHECK_EVENTS.tsv: observations and explicitly delimited mathematical checks.
- SP56_CW_63_hand_log.md and SP56_CW_63_sheet_feedback.md: recurring notation/hand habits and primary error counts.
- records/: manually entered structured decisions from which the reports are built.
- scripts/: report maintenance, documented reading edits, selected reproducible algebraic checks, syntax/schema validator and ZIP packager.

The LaTeX is a fragment using the supplied PREAMBLE conventions, standard LaTeX and TikZ. It is not compiled. Source slips and odd spellings remain in the transcription; interpretations and mathematical qualifications are confined to the notes.

## Rebuilding and checking

The report builder scripts/record.py expects the originally supplied witnesses at ../input/SP56_CW_63_witnesses relative to this archive’s extracted root. It uses the page map only; image reading is not automated. Do not rerun a read_NNN.py edit script against an already edited page: its guarded replacements intentionally require the original local text at each edit. The saved page files and records are the deliverables.

Use scripts/validate_deliverable.py OUT_DIR [--zip ZIP_PATH] --format text for structural checks after completion. These checks do not establish palaeographic or mathematical correctness. scripts/package_deliverable.py OUT_DIR ZIP_PATH packages eligible files and refuses overwrite.

Scans, original witnesses, crop images and earlier checkpoint ZIPs are intentionally excluded. Crop boxes in the changes log use the original whole image’s pixel coordinates.
