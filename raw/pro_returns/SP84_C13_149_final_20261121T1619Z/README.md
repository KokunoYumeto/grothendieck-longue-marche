# SP84_C13_149 — diplomatic second pass

The authoritative current transcription is in `pages/`. Completion times, independent-audit status, checkpoints and any recorded final freeze are documented in `progress.log` and the per-page JSON records. Historical drafts are retained separately as evidence of the reading process.

This completed edition covers all 23 scans, 005–027. All 99 supplied doubt marks have a recorded decision, and all 23 pages have completed the independent audit and main-reader adjudication. The final changes log records 462 substantive places: 156 differ from C and 412 from H, with overlap. The independent phase covered 460 boxes, of which 351 produced differences and 95 changed in adjudication; these are selected-box and representation counts, not accuracy rates. Remaining local uncertainties are marked in the transcription and documented in the doubts report.

Final structural, accounting and provenance checks passed. The 23 page files and combined fragment were frozen and all 24 SHA-256 hashes verified unchanged. The records are `documentation/final_validation.json`, `documentation/frozen_sha256.json`, `documentation/final_accounting.json` and the closing entries of `progress.log`.

The consolidated fragments are in `pages/`, in scan order 005–027. `SP84_C13_149_transcription.tex` combines them without a preamble. The original supplied `PREAMBLE.tex` defines the edition's macros; it is not duplicated here. No LaTeX compilation was requested or performed.

The supplied scans were read visually. Neither OCR nor outside editions, published texts, or external research was used. Witness C and witness H are comparison drafts. The adopted reading follows visible ink, and unresolved readings remain marked in the text.

Three readers each received one page at a time, with only that page's witnesses, listed disagreements, marks, and the current notation cautions. The main reader reviewed the reported disagreements on saved crops and finalized each page. A different reader then received only the images and box coordinates for the independent second reading. The first and second box readings are preserved separately, with a scripted token comparison and adjudications.

## Finding the evidence

- `SP84_C13_149_changes.md`: substantive differences against either witness, counts, evidence and unresolved places.
- `SP84_C13_149_collation.tsv`: differences against H alone; H's page number is our scan minus one.
- `decisions.tsv`: every supplied doubt mark, in the original order.
- `SP84_C13_149_doubts.md`: notation, remaining uncertainty, abbreviations and legibility limits.
- `SP84_C13_149_inventory.csv`: every identified manuscript element.
- `SP84_C13_149_notes.md` and `CHECK_EVENTS.tsv`: what the pages say and what mathematical checking actually occurred.
- `SP84_C13_149_hand_log.md` and `SP84_C13_149_sheet_feedback.md`: local handwriting observations and feedback on the supplied error sheet.
- `crops/`: enlarged image evidence; coordinates always refer to the original scan pixels.
- `second/`: frozen box lists, first readings, independent readings, token differences and adjudications.
- `reviews/*.json`: current structured readings, decisions, doubts, metadata and accounting, together with identified historical first-pass evidence and approval/audit records.
- `reviews/*.tex`: archived first-reader proposals; these are historical working texts and are not the current transcription or either supplied witness.
- `progress.log`: completion/audit times, checkpoints and frozen transcription hashes.
- `source_manifest.json`: hashes of the supplied inputs; the source scans and witness files themselves are excluded.
- `scripts/`: preparation, assembly, comparison, packaging and validation scripts used in this run.

## Current text and historical records

`pages/149_scanNNN.tex` is the authority for the adopted page text. The combined transcription is generated from those page files in ascending scan order. Current report fields such as final readings, decisions, doubts, notes, inventory and witness-accounting flags are synchronized with the adopted text. Fields that preserve the first-pass audit targets, and the separate first/second TSVs, retain their original historical readings; adjudications and correction logs explain subsequent changes. Adjudication final-reading strings and changed-box counts describe the audit-time decisions. Later documented presentation amendments can update current page/report rendering without changing those historical strings or counts; the amendment logs identify their exact scope.

The archived `reviews/*.tex` proposals may differ from both the current pages and the supplied C/H comparison drafts. They must not be substituted for `pages/` or treated as a new witness. `documentation/first_reader_working_files/` preserves earlier scripts and coordinate metadata for provenance; these are historical working files, not a recipe to overwrite frozen readings. The active duplicate `scripts/write_reader_c_scan012.py` is deliberately disabled before its historical body can run or be imported; its byte-original source is preserved at `documentation/first_reader_working_files/write_reader_c_scan012.py`. The supplied source scans and witness texts remain outside this edition archive and are identified by `source_manifest.json`.

`notation_current.md`, `legibility_note.md`, and `feedback_addendum.md` support the assembled reports. Cross-page notation review is documented separately in `documentation/notation_review.md`; repeated forms do not by themselves remove a local doubt. The full-size halves are reproducible and are excluded, as are original attachments and previous checkpoint ZIPs.
