# SP62_CW_162-1+162-6 — consolidated diplomatic second pass

## Scope and authority

Eleven supplied scan pages: cote 162-1, scans 005–010 (folder H162-01), then cote 162-6, scans 002–006 (folder H162-02). H’s page is always the scan number minus one. The ink is the authority; C and H are unverified witnesses used for collation. No outside source or publication was consulted.

The sole manuscript reader was `/root`, GPT-6 Astra Pro; the runtime did not expose a reasoning-effort label, so none is invented. All first readings were completed before the second complete visual reading began. The reading and audit times are in `progress.log`. An auxiliary worker wrote and ran mechanical validation code only, without inspecting scans, witnesses or making reading decisions.

## Contents

- `pages/`: eleven consolidated fragments, named exactly as C’s page files.
- `SP62_CW_162-1+162-6_transcription.tex`: all eleven fragments in order, with cote markers and no preamble.
- `PREAMBLE.tex`: the supplied macro definitions. No new manuscript-transcription macros were introduced.
- `SP62_CW_162-1+162-6_changes.md`: per-page C/H/final readings, ink evidence, confidence, unresolved places, all crop boxes, and counts including witness-specific confidence totals.
- `SP62_CW_162-1+162-6_collation.tsv`: substantive differences from H only. Certainty-only and equivalent macro-syntax differences are excluded.
- `SP62_CW_162-1+162-6_doubts.md`: notation table, remaining doubts, dispositions of C’s doubts, abbreviation expansions, and an honest legibility assessment.
- `SP62_CW_162-1+162-6_inventory.csv`: every inventoried block, formula, drawing, diagram, margin note, insertion and cancellation, marked transcribed.
- `SP62_CW_162-1+162-6_notes.md`: brief per-page documentary notes and conditional mathematical checks, without emending the source.
- `CHECK_EVENTS.tsv`: the kind of check actually performed. Documentary reading is carried as background, never represented as a proof. Where a note and a source formula both identify one calculation, their events cross-reference the same check rather than claim independent repetitions.
- `SP62_CW_162-1+162-6_hand_log.md` and `SP62_CW_162-1+162-6_sheet_feedback.md`: observed handwriting habits and localized error-class counts.
- `SP62_CW_162-1+162-6_audit.md`, `progress.log`, `transcription_sha256.tsv`, `validation_report.json`: visual audit, real times, frozen transcription hashes and mechanical validation.
- `crop_register.tsv`: all crops by original-image coordinates and rotation. The images themselves are deliberately excluded.
- `records/`: explicit documentary decision ledgers used to assemble the apparatus; these are not checkpoint substitutes and contain no OCR output.
- `scripts/`: crop production, first-reading record-writing scripts, apparatus assembly, hash freezing/verification, packaging and mechanical validation. `consequential.txt` and `readability.txt` are apparatus source text.

## Reading and notation policy

Every page was inspected as a whole and through both supplied full-resolution halves. One tight enhanced crop was made for each remaining open place. No OCR or recognition library was used. During the second reading, an existing crop could be re-viewed; no decided place was cropped again. Source spelling, accents, abbreviated forms, questionable mathematics and cancellation state remain diplomatic. The three surviving `illegible{1}` regions are physically overstruck word-sized regions, never missing mathematical symbols. Archive corner numbers are comments, following C’s conventions, not invented manuscript pagination.

A substantive row is a localized reading, state or placement difference. It can differ from both witnesses and can encompass a connected multiword passage. Certainty-only choices are not counted as substantive changes. A preference reversal inside `unsure{a|b}` is substantive when it changes the primary reading; simply adding or removing an uncertainty wrapper is not. Roman numeral cap/foot glyphs are preserved; a purely typographic encoding difference is not counted unless it changes the numeral, underline or deletion state.

## Rebuilding and validation

The final page files and current `records/*.json` are authoritative. `record_*.py` scripts preserve the initial first-reading stage and must not be rerun over the final package: later audit decisions are in the current ledgers and page fragments. `python scripts/records.py` rebuilds apparatus and combines the current pages without making reading decisions. It does not replace page files. The original scans and witnesses remain in the user’s supplied attachment and are not redistributed here.

`python scripts/validate_package.py . --format json` checks expected files, order, agreement of combined text with page fragments, TeX delimiter/environment balance, table schemas/categories and forbidden-file exclusions. With `--zip PATH`, it also checks archive integrity and packaged bytes. This is lexical/structural validation, not a TeX compilation or a proof of typesetting. No TeX engine was run, as instructed.

`python scripts/freeze_transcription.py freeze` creates the twelve-file SHA-256 manifest and logs the freeze; it refuses to overwrite an existing freeze. `python scripts/freeze_transcription.py verify` checks every digest and logs an unchanged result only if all twelve match. Later apparatus edits do not change these twelve transcription files.

Checkpoints are due only after each full 45-minute interval from the first timestamp, never at page or cote boundaries. Any checkpoint and the final archive contain all deliverables and work documentation then available, without source images, witnesses, attached archives, crops or earlier checkpoint ZIPs. If the final package is completed before the first interval elapses, no checkpoint is created.
