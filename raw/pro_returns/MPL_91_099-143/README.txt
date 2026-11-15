MPL_91_099-143 — complete return

Main files
- MPL_91_099-143_transcription.tex: complete diplomatic fragment, no preamble.
- pages/: the 38 individual scan-page fragments in archive order.
- MPL_91_099-143_doubts.md: notation table, 448 doubt occurrences, abbreviations and legibility statement.
- MPL_91_099-143_inventory.csv: 666 elements, all marked transcribed=yes.
- MPL_91_099-143_notes.md: 56 research notes, standing questions and context/status comparisons.
- progress.log: sequential completion, second audits, freeze and final hash verification.

Records
The records directory holds the visual-audit record, historical working notes,
notation/line-location support, context searches, exact example calculations,
SHA-256 manifest, structural validation and the temporary typesetting harness.

The transcription uses the page-state macros specified in the task. Supply
definitions suitable for the intended edition. records/qa_wrapper.tex provides
a checking harness, including TikZ/tikz-cd and a first-reading display for
uncertainties. Its colours and wide pages are verification conventions.
The full alternatives and deletions remain in the diplomatic source.

The frozen transcription predates access to the research context.
Historical scripts are retained as a work record; do not run transcription-
building scripts over the frozen sources. records/verify_package.py is a
read-only structural and hash check.

The original input scans, supplied context files and temporary QA PDF are
excluded, as requested. Source references in the notes name the supplied
context files and their entry IDs; underlying external reports were not
included in that input.
