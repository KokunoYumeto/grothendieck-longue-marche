# MPL 133 — delivery guide

## Principal files

- `MPL_133_transcription.tex`: the complete, frozen LaTeX fragment, containing all 50 supplied scans in order; no preamble or embedded source images.
- `pages/`: one fragment for each supplied scan, with the same bytes used in the combined transcription.
- `MPL_133_doubts.md`: the shared notation table, individual reading doubts, abbreviation list, and legibility assessment.
- `MPL_133_inventory.csv`: 809 inventoried elements across 50 scans; every element is marked `yes`.
- `MPL_133_notes.md`: 76 research notes, answers to the planning questions, both standing registers, results-state reconciliation, and APA references.
- `research/`: longer mathematical proofs, source-access qualifications, and contextual comparison records supporting the main notes.
- `progress.log` and `records/`: completion and audit times, the pre-context freeze, SHA-256 hashes, visual-audit records, context searches, and mechanical validation.
- `scripts/`: the work's recording and integration scripts, retained as provenance.

## Scope and numbering

The supplied sequence is scans 002–054 of cote 133, excluding 005, 010, and 041, which the prompt identified as blank. Archive scan numbers, visible manuscript foliation, the internal numbering of the group-cohomology leaves, and printed offprint pagination remain separate. The inventory has three cover/title sheets, ten reused printed/typed sheets, and 37 text sheets; a partial cancellation is recorded as an element rather than reclassifying an entire otherwise live sheet.

## Frozen text and verification

The transcription was frozen before the context was opened. The final verification compares all 50 page files and the combined fragment with those frozen hashes. Mathematical counterexamples and reading questions discovered during research occur only in the notes; they do not correct the transcription.

The combined fragment was compiled unchanged with a temporary test preamble using the installed mathematical and diagram packages. Editorial styling was suppressed in that test; it checks syntax and integration, not the final appearance of a styled edition. Full details and the eight nonfatal layout notices are in `records/mechanical_validation.md`. The fragment expects the editorial macros named in the task and standard LaTeX, TikZ, and tikz-cd support in its eventual edition preamble.

Only `python3 scripts/validate_package.py` is intended as a safe final read-only check. Page-writing, audit-update, syntax-repair, and one-time integration scripts record earlier work and must not be rerun on the frozen delivery. The first-pass observations are explicitly historical; the frozen fragments and final doubt table take precedence over preliminary readings recorded there.

The supplied source archives, extracted scans and context, downloaded literature, and temporary compilation outputs are excluded. The context-search ledger records paths, hashes, query execution, and precise locations without copying the supplied source texts.
