# MPL_83_178-222

Complete diplomatic transcription and separate research notes for the 43 supplied scans of Montpellier cote 83, scans 178–222, excluding the blank scans 182 and 206.

## Main files

- `MPL_83_178-222_transcription.tex`: the combined LaTeX fragment in scan order, with no preamble.
- `pages/`: one authoritative LaTeX fragment for each of the 43 supplied scans.
- `MPL_83_178-222_doubts.md`: the recurring-notation table, manual reading judgments, exhaustive uncertainty concordance, abbreviation glossary, and legibility assessment.
- `MPL_83_178-222_inventory.csv`: 1,025 element rows, all marked transcribed.
- `MPL_83_178-222_notes.md`: 111 indexed research items, including the standing registers of author-marked unfinished steps and titles/page counts.
- `progress.log`: page completion, second visual audit, checkpoint, freeze, context-opening, and final verification records in UTC.

## Source boundary

The primary reader alone read and transcribed every full-page image and both halves, in ascending order, without OCR. All 43 pages received a second visual audit before the transcription was frozen at **2026-11-17 17:10:31 UTC**. Context contents were first opened at **17:10:36 UTC** and used only for research notes; a preliminary listing of the context ZIP's filenames and sizes, before the instruction file had finished being read, is disclosed in `records/work_method.md` and the progress log.

The 43 page files and combined transcription are identified by `records/frozen_hashes.json`. No frozen reading has been changed because of the context, a mathematical calculation, or a subsequent comparison. The final hash comparison is recorded in `records/final_verification.json` and `progress.log`.

## Reading and rendering

The transcription deliberately retains uncertain readings, deletions, insertions, anomalies, unfinished expressions, and inconsistent working formulas. It contains 331 `\unsure` occurrences and one `\illegible{5}` occurrence inside a heavily blackened cancellation. The uncertainty register explains confidence and the limits of the drawings' typographic approximation.

Use the requested editorial macros in your own document setup, or use `scripts/compile_fragment.py` as a separate validation wrapper. The combined source itself remains a fragment. The recorded validation build has no TeX errors or overfull-box diagnostics; its 44 rendered pages reflect wrapper pagination and are not an authorial page count. No rendered PDF or source image is included.

## Research and working records

The research notes distinguish current manuscript evidence, supplied contextual interpretations, earlier-run claims, reviewed statuses reported in the results digest, independently checked calculations, and open proposals. They credit Hua's modernised reading for corrections and models already present there. The supplied context and original scans are not duplicated in this ZIP.

`records/` and `scripts/` preserve the work's evidence and reproduction tools. The three research contribution memos are working records; the main notes incorporate their review and qualifications and are the authoritative synthesis. Historical `recordNNN.py` and page-record scripts are retained as records of initial construction and **must not be used to regenerate the audited transcription**, because later visual corrections are authoritative in `pages/`.

The exact algebra checks require Python and SymPy:

```bash
python records/verify_algebra.py
```

The finite contextual bi-icosahedron enumeration uses the Python standard library:

```bash
python scripts/check_biicosahedron.py
```

Mechanical validation of the source fragments and inventory is available with:

```bash
python scripts/validate_package.py
```

Successful syntax checks and exact algebra calculations do not certify the reading of a handwritten stroke. The notes preserve that distinction throughout.
