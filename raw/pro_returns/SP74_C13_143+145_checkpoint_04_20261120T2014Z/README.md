# SP74 C13: cotes 143 and 145

This package contains the consolidated diplomatic LaTeX fragments and the evidence and decision records for the requested 24 scans. The fragments use the supplied PREAMBLE.tex conventions; the original preamble, scans and witnesses remain in the input attachment and are deliberately not duplicated here. No OCR, text-recognition library, external research or TeX compilation is used.

## Contents

- `pages/`: accepted page fragments, one per scan.
- `SP74_C13_143+145_transcription.tex`: the same fragments combined in the prescribed order, with cote markers.
- Changes, collation, inventory, decisions, doubts, notes, hand log, error-sheet feedback and CHECK_EVENTS: the requested editorial records.
- `reviews/`: first-reader candidates and reports, main-reader adjudications, accepted structured records, and second-reading reports when completed.
- `crops/`: evidence crops from the native scans. Coordinate boxes refer to the original scan, before resizing or rotation.
- `progress.log`, `reader_schedule.tsv`, `validation.json` and final hash records: work status and structural verification.
- `scripts/` and `workflow/`: the processing code and reader contracts used in the work.

Original scans, original texts, disposable full-resolution halves, attached prompts and prior checkpoint ZIP files are excluded. A checkpoint is an in-progress snapshot and does not imply completion; the final package's progress log and validation record identify the completed readings.

## Rebuilding expendable inputs after restoration

Place the restored working package in its own directory. Extract the original attachment once into its sibling directory `source/`; the attachment already contains expanded scans/texts folders. Run `python3 scripts/prepare_inputs.py` from the restored working directory to recreate missing native halves and page-only packets in sibling directories. Existing halves are retained. The input files and regenerated halves are not part of subsequent output archives.

`build_deliverables.py` rebuilds aggregate editorial files from accepted structured records and current page fragments. Per-page reader/adjudication scripts are historical processing records and should not be rerun indiscriminately. `validate_deliverables.py --final` checks structural completeness without compiling TeX. `manage.py freeze` records page and combined-text hashes; `manage.py verify` verifies those hashes.

Confidence describes a visible reading, not a certification of the mathematics. A retained unsure mark remains unresolved even where its first alternative agrees with a witness. CHECK_EVENTS distinguishes actual limited mathematical checks from claims merely carried from the source.
