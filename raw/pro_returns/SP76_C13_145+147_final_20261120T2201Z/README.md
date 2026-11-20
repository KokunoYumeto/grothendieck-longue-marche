# SP76_C13_145+147 — diplomatic consolidation

## Completion

All 24 pages have a completed first reading, main-reader image adjudication and independent second reading by a different reader. The second pass contains 332 boxes. Its token comparison produced 241 mismatches, all decided on crops; 54 boxes changed in reading, placement or uncertainty.

The final log contains 466 local rows: 118 substantive differences against C and 395 against H, with overlaps between the witness counts. Fourteen rows record cropped certainty resolutions without a substantive difference from either witness. All 72 original marks have decisions: 27 first readings, 8 listed alternatives, 4 other readings and 33 left undecided. The doubts register contains 145 entries covering 147 active uncertainty marks; two entries each cover a paired occurrence. The inventory has 371 elements. Two targeted mathematical checks are recorded in `CHECK_EVENTS.tsv`.

The final cross-page notation review, static LaTeX review, doubt-coverage mapping and packaging checks are in `reports/`. The 24 page files and combined fragment are frozen together; their SHA-256 values and final verification are recorded in `reports/frozen_hashes.json` and `progress.log`.

## Reading the deliverable

The authoritative transcription is in `pages/`, one LaTeX fragment per scan, and in `SP76_C13_145+147_transcription.tex`, the same pages combined in the supplied order. These fragments use the supplied witness C preamble conventions. The original scans, witnesses and preamble are not duplicated here; they remain in the user's input archive. No TeX compilation has been performed.

The changes log records local differences from C and H, the observed ink, crop coordinates and confidence. Its independent-audit sections preserve the first reading, the blind reading and the main reader's decision. The collation TSV contains the substantive differences from H. `decisions.tsv` follows the original order of all 72 marked doubts. The doubts file begins with the notation table, lists remaining uncertainties, and gives abbreviation expansions separately from the transcription. The inventory, notes, hand log and error-sheet feedback are companion records.

`CHECK_EVENTS.tsv` records only mathematical checks that actually occurred. Summarizing a manuscript assertion or reading its formula is not represented as a proof check.

## Evidence and history

`crops/` contains the saved first-pass and independent-reading crops. Coordinates refer to the original scan pixels. In the independent audit, the target box and actual crop bounds are recorded separately; the manifest also gives rotation in degrees. No OCR or other text-recognition software was used.

For each scan, `second/` contains its neutral box list, the first reading written before the blind pass, the independent reading, the token comparison, and the main reader's adjudications. The first-reading manifest fixes all 48 box-list and first-reading-table hashes. Those historical tables are never rewritten after an audit correction.

`reports/` and `docs/` preserve the work record. In particular, `reports/*_draft.tex` are historical first-pass submissions, **not the final transcription**. Page report JSON files drive the consolidated logs; date-stamped review statements describe their snapshot at that time. `progress.log` is the chronological record of page completions, independent audits, checkpoints and final hash verification.

## Counting conventions

Counts are local decision places, not changed tokens. A primary reading changed within an uncertainty still counts as a substantive difference. Adding an uncertainty without changing its preferred reading does not create a C/H error row. Resolving a C doubt in favor of its existing first reading is recorded as a certainty resolution and excluded from substantive C corrections. Purely equivalent macro syntax, spacing commands and editorial wrappers are excluded from substantive counts. H's editorial recognition of a cancellation or insertion is considered together with its displayed text. A box may contain more than one local decision, so changed-box counts and C/H place counts measure different things.

## Scripts

The scripts document preparation, aggregation, token comparison, explicit main-reader decisions, validation, checkpoint packaging and freezing. Scripts named `adjudicate_*` are historical, page-specific applications of already made visual decisions; they are not general recognition software and should not be rerun on a completed deliverable. `start_audit.py` and `prepare_blind_lists.py` likewise belong to the completed preparation history and must not be used to rewrite the frozen first-reading tables.

The package deliberately retains the observations, low-confidence alternatives and rejected proposals needed to review difficult passages. Confidence labels describe local visual judgment, not a calibrated error probability.
