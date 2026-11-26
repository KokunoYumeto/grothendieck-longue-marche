# SP105_CW_37 — consolidated diplomatic transcription

This edition covers all eleven supplied scans: 87–94 and 96–98. Scan 95 is not part of the assignment. The operative instructions are identified in `provenance.md`.

## Reading the deliverables

- `SP105_CW_37_transcription.tex` is the combined LaTeX fragment, in scan order, without a preamble. `pages/` contains one finished fragment per scan. Use the supplied source preamble when building an edition; this task did not compile TeX.
- `SP105_CW_37_changes.md` gives the witness comparisons, counts, image evidence and remaining questions. `SP105_CW_37_collation.tsv` isolates differences from actual text in H.
- `SP105_CW_37_doubts.md` contains the notation table, residual doubts, abbreviation suggestions and legibility assessment. `SP105_CW_37_inventory.csv` records the page elements.
- `SP105_CW_37_notes.md` separates the pages' claims and questions from checks performed here. `CHECK_EVENTS.tsv` records only actual mathematical check events.
- `SP105_CW_37_hand_log.md` and `SP105_CW_37_sheet_feedback.md` record local habits and error patterns for later readers.

## Evidence and reproducibility

`notation_working.md` is the preserved historical first-phase notebook; its provisional readings may be superseded. The notation table in `SP105_CW_37_doubts.md`, the current `decisions/` records and `notation_consistency.md` give the final readings.

`readers/` preserves first-reader returns. `decisions/` records the main reader's settlements. `drafts/` retains work products; the finished text is in `pages/`. `crops/` holds every saved first- and second-reading crop. Coordinates refer to the full-resolution supplied images.

For each page, `second/` contains the geometric box list, first reading, independently written second reading, reader attestation, raw token comparison and adjudication. The second reading remains unchanged after comparison. Raw differences may include context or macro choices; each is adjudicated separately from the count of changed readings.

The canonical second readings were made by fresh agents with no earlier page-reading context. `second/preliminary_exposed/` preserves the initial attempts that were superseded after a reader flagged possible exposure through the first phase's shared notation table. Their raw files remain unchanged and are not counted as the final blind audit.

`progress.log` records completion, audit and freezing events. `transcription_sha256.json` and the final verification record establish the frozen text. `scripts/` contains the assembly, comparison, audit, validation, hashing and packaging programs; none recognizes text from images. `method/` contains the run's own reader protocols. `source_manifest.tsv` identifies the supplied sources by hash without redistributing them.

The archive intentionally contains no original scans, unchanged witness files, source prompts, supplied preamble, or earlier checkpoint ZIPs. It includes the edition's own evidence, drafts, logs and programs.
