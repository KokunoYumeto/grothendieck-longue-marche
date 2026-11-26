# SP111: diplomatic transcription and reading record

This edition covers cotes156-4, scans074–089, and156-6, scans002–005. The scan is the authority. Spelling, abbreviations, cancellation layers, insertions, marginal writing, mathematical notation and authorial slips are preserved; unresolved readings remain marked in place.

## Files

- `pages/`: one LaTeX fragment per scan, named as in witnessC.
- `SP111_CW_156-4+156-6_transcription.tex`: the fragments in scan order, without a preamble. Use the preamble supplied with the original witnesses. No TeX compilation was performed in this run.
- `SP111_CW_156-4+156-6_changes.md`: page counts, consequential readings, every difference fromC orH, decisions on prior doubts, theS decision, and the independent-reading adjudications.
- `SP111_CW_156-4+156-6_collation.tsv`: the locations where the consolidated reading differs fromH.
- `SP111_CW_156-4+156-6_doubts.md`: the notation table, remaining doubts, abbreviations and legibility assessment.
- `SP111_CW_156-4+156-6_inventory.csv`: all inventoried manuscript elements and their transcription status.
- `SP111_CW_156-4+156-6_notes.md` and `CHECK_EVENTS.tsv`: page contents, ink-versus-intention distinctions, and mathematical checks actually performed. Visual collation is not counted as a proof check.
- `SP111_CW_156-4+156-6_hand_log.md` and `SP111_CW_156-4+156-6_sheet_feedback.md`: local writing habits, their scope, witness effects and counts by error category.
- `second/`: original coordinate boxes, first readings, independently written readings, token comparisons, crop manifests and root adjudications. First and independent readings are retained as written before comparison.
- `crops/`: enlarged deciding crops. `crops/second/` contains the independent readers’ new crops. Coordinates refer to the original scan pixels.
- `records/`: the structured page records from which the registers are generated.
- `documentation/`: root adjudication notes, reading manifests and work provenance.
- `scripts/`: the preparation, register, comparison, structural-validation, audit, freeze and packaging programs used in this run.
- `progress.log`: page completion, audit, checkpoint and freeze events. `transcription_frozen.json` records the final21 hashes when all audits are complete.

## Counting and interpretation

A correction row is one located reading decision. It may differ fromC, fromH, or from both. Consequently, the two witness counts overlap. Pure macro syntax, agreement with both witnesses and a change of certainty alone are excluded from correction totals. Confidence describes the final ink reading; low confidence remains explicit in the transcription.

The historical page-completion lines report counts at their respective completion times. A later reconciliation records certainty-only rows removed from correction totals; the current changes table supplies the final counts. An audit difference is a box whose token sequence differs, including differences of extent or encoding. The adjudication states whether the actual page reading changed.

The notes distinguish literal ink from an intended mathematical correction. In particular, witnessS’s proposed reading of156-6/005 is assessed separately from its explanation of the author’s apparent slip.

The archive contains the work products and deciding crops. The supplied scans, unchanged witnesses, attached prompts and earlier checkpoint ZIPs are excluded.

## Extracting the ZIP

The lossless transfer archive uses standard ZIP method 14 (LZMA) for some PNG entries. Python 3 with its standard `lzma` support can extract these entries; this run used Python's `zipfile` reader to decode and CRC-check every archived entry. From the directory containing the final ZIP, run:

```bash
python3 -m zipfile -e SP111_CW_156-4+156-6.zip extracted
```

Use an extractor with ZIP-LZMA support. The legacy Info-ZIP installed in the working environment could not read these method-14 entries. The extraction creates ordinary PNG files without changing their dimensions, image modes or decoded pixels. Encoding details and the measured compatibility results are recorded in `documentation/compression_research/README.md`; the transfer archive's per-image verification record is `documentation/lossless_archive_encoding.json`.
