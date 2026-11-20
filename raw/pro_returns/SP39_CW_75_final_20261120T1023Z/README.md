# SP39_CW_75 — consolidated second pass

The transcription covers archive scans **26, 27, 28, 30, 31, 32, 33**, in that order. Scan 29 is outside the supplied task. Witness H has no text for scan 30.

## Reading the return

- `pages/` contains the seven diplomatic LaTeX fragments under witness C's original filenames. `SP39_CW_75_transcription.tex` concatenates them in scan order, with one opening `\cotefile{75}` and no preamble.
- Use these fragments with `PREAMBLE.tex` from the supplied witness package. No new notation macros are defined. The diplomatic text preserves the observed mathematics and French.
- `SP39_CW_75_changes.md` gives counted changes, per-locus ink evidence, the three independent alternatives where they differed, and unresolved readings.
- `SP39_CW_75_collation.tsv` gives every substantive difference from H; purely equivalent macro syntax is excluded. No rows are assigned to the absent H page.
- `SP39_CW_75_doubts.md` starts with the evolving notation table, then remaining doubts, abbreviation interpretations, and legibility assessment.
- `SP39_CW_75_inventory.csv` records every inventoried text block, formula, diagram, insertion, deletion and note.
- `SP39_CW_75_notes.md` describes what each page states, the mathematical checks actually made while reading, its explicit qualifications, titles and dates. `CHECK_EVENTS.tsv` distinguishes actual verification from merely transcribing a claim.
- `SP39_CW_75_workflow.md`, `briefs/`, `readers/` and `decisions/` preserve the reading process. Reader A, reader B and reader C are the fresh readers for one scan, and are distinct from the historical source called witness C.
- `progress.log`, `frozen_hashes.json` and `validation.json` document completion, syntax checks and the frozen transcription hashes. The final consolidated source is checked statically. A preliminary compile attempt by scan-026 reader A did not reach typesetting because pdflatex.fmt was unavailable; the workflow records that deviation, and later readers were explicitly instructed to use static checks only. No rendered-layout validation is claimed.

## Reproducing inspection crops

Source images, supplied witness files and full-page/half-page image copies are excluded from this return. Each reader's `crops.tsv` and the main reader's crop manifests give exact bounds in whole-page pixels, output width, rotation, processing and creation time. Their named crops can be reproduced from the attached source archive with `scripts/crop.py`:

```text
python scripts/crop.py SOURCE_IMAGE OUTPUT_IMAGE MANIFEST X0 Y0 X1 Y1 WIDTH ROTATION
```

Coordinates are `(left, top, right, bottom)` measured from the upper-left of the named supplied whole-page JPEG. The script uses Pillow only for crop, rotation, contrast and enlargement; it contains no text recognition. Reader records identify whether the half-page image or a particular crop settled each reading. The main reader's decisions cite the chosen crop and the observed strokes.

`SOURCE_INPUTS.tsv` identifies the two user-supplied attachments by filename, size and SHA-256. `PACKAGE_CONTENTS.tsv` lists the files in this archive except itself. Timed checkpoint archives, when made, are separate files and never embedded in later archives.

The auxiliary JSON files are editable structured records used to produce the readable logs. `scripts/build_records.py` renders those logs without choosing readings. The diplomatic page fragments themselves are explicitly decided and frozen before final packaging.
