# SP117_CW_97+123+162-1

This working edition covers the fifteen supplied scans in the order recorded in `work/page_order.json`: 97/019; 123/002,003,016,017,018,019,020,022,023,028,040; and 162-1/002,003,004.

The scan images are the authority. The two supplied AI transcriptions are witnesses, not verified editions. No OCR, text-recognition library, external source research, or TeX compilation is used in this run. The supplied sweep has no correction row explicitly naming one of these fifteen scans.

## Contents

- `pages/`: one diplomatic LaTeX fragment per scan, with the original filenames.
- `SP117_CW_97+123+162-1_transcription.tex`: the page fragments joined in the prescribed order, without a preamble.
- `PREAMBLE.tex`: supplied macro definitions used by the transcription.
- `SP117_CW_97+123+162-1_changes.md`: readings against both witnesses, source evidence, confidence, unresolved places, and changes made after the blind reading.
- `SP117_CW_97+123+162-1_collation.tsv`: the specified eleven-column collation against H; macro-only differences are excluded.
- `SP117_CW_97+123+162-1_doubts.md`: notation, unresolved readings, abbreviations and legibility assessment.
- `SP117_CW_97+123+162-1_inventory.csv`: the page elements and their transcription status.
- `SP117_CW_97+123+162-1_notes.md`: brief English notes on what each source page says, with actual mathematical observations distinguished from transcription.
- `CHECK_EVENTS.tsv`: mathematical check events, not visual inspection events.
- `SP117_CW_97+123+162-1_sheet_feedback.md` and `SP117_CW_97+123+162-1_hand_log.md`: recurring error categories and scoped handwriting observations.
- `second/`: neutral boxes, the first and independent second readings, token comparisons, crop decisions and page audits. The written readings are preserved unchanged after comparison.
- `crops/`: saved evidence, including the independent second-reading crops. All coordinates refer to the original whole-page images.
- `progress.log`: page commits, audit counts, checkpoint records and final transcription hashes.
- `transcription_audit.md`, `notation.md`, `work/`, `scripts/`: working reports, original first-reader returns, root decisions, manifests and the scripts documenting the process.

## How to interpret the record

The LaTeX preserves spelling, abbreviations, canceled material, insertions, punctuation, symbols and graphic marks. `unsure` is a reader's uncertainty, not source punctuation. Source question marks remain ordinary question marks. The first alternative is the preferred visible reading; it is not a reconstruction of the expected mathematics. Archival corner numbers are comments; the author's own foliation uses `mspage`.

Counts in the changes log describe adjudicated places, not tokens or independent error-rate estimates. A place may differ from both witnesses. Resolving a C doubt is recorded with its evidence; an added doubt that changes no reading is listed as uncertainty. The independent token comparison deliberately retains TeX tokens: equivalent macro spelling, differing context inside a box and actual source differences all reach the root for a crop decision. They must not be read as counts of transcription errors.

Three first readers work on different pages in parallel. A first reader receives a new page only after the root has adjudicated and committed its previous return. All fifteen first passes must be committed before the blind stage begins. Each blind page goes to a different reader, who receives only the image, neutral coordinates and transcription conventions. Root decisions retain both written readings and identify the saved crop. No witness reading or expected mathematical statement overrides the ink.

The supplied scans, witness folders and context files are not copied into this archive; they remain the original attachments. Earlier checkpoint ZIPs are also excluded. Checkpoint receipts and documentation remain in `work/`.

## Reproducibility and limits

The scripts perform crop preparation, bookkeeping, token comparison, structural validation, hashing and packaging. They do not recognize text or adjudicate handwriting. The final validation checks completeness, file identities, evidence paths, coordinate bounds, audit coverage and LaTeX brace structure; no compilation is performed. The mathematical notes have only the scope stated in their corresponding check events. Difficult canceled words and tightly overtyped symbols remain explicitly doubtful.

This README is finalized with the audit and freeze record at completion.
