# MPL_93_002-046 — package guide

This archive contains the diplomatic transcription and post-freeze research commentary for the **42 supplied scans of cote 93**: 003–046, excluding 026 and 035. Scan 002 was also omitted as blank by the input package.

## Main deliverables

- **MPL_93_002-046_transcription.tex** — the combined LaTeX fragment, with no preamble, in scan order.
- **pages/** — 42 individual page fragments; their exact byte concatenation is the combined transcription.
- **MPL_93_002-046_doubts.md** — the notation table first, an abbreviation list, 124 registered doubts or visually clear anomalies, and a legibility statement.
- **MPL_93_002-046_inventory.csv** — 693 element rows with the requested columns, all marked transcribed=yes.
- **MPL_93_002-046_notes.md** — 82 labelled research notes, the complete 33-sheet typed/printed census, title and pagination evidence, a register of the manuscript's explicit questions and deferred steps, context comparisons, and a bibliography.
- **progress.log** — UTC page-completion, second-audit, freeze, checkpoint, and final-validation records.

## Reading and freeze

The primary transcriber read all 42 whole-page images and all 84 supplied half-page images directly, in one stream, then performed a second image audit of every retained page. No OCR was used, and no target-image reading or transcription was delegated. Research assistance after the freeze was confined to source research, mathematical checks, and review of the frozen text/records.

The transcription was frozen at **2026-11-15 11:03:40 UTC** and the context was opened at **11:03:56 UTC**. The final unchanged-hash check is recorded in progress.log and final_validation_report.md. The canonical frozen hashes are in frozen_sha256.json; post-freeze editorial suggestions occur only in the research notes.

## Research scope

The supplied context consists only of README.md and notes/RESULTS_STATE.md from the context attachment. The latter has no matching open or settled result rows and contains three abbreviated, unreviewed first-pass leads. No unprovided earlier transcription or content of cotes 159 and 64 was accessed.

The notes give partial support to S20 as a thematic grouping, while keeping the projective, elliptic, and crystalline constructions distinct where the scans do not provide a comparison. The English analysis pages remain unidentified, with the Huff chapter recorded only as a tentative bibliographical candidate.

The per-note literal searches are recorded in research/context_search_by_note.json and summarized in research/context_search_coverage.md. Literal hits can be incidental; the prose of each note states the substantive comparison and the status of any relevant supplied ID.

## Verification and reuse

Mechanical validation checks the scan set and order, macro classification, braced macro arguments, balanced braces and environments, inventory schema and coverage, exact concatenation, and frozen hashes. It cannot certify a palaeographic reading. The independent research-note review checks references, classifications, hypotheses, and the 1–4 sentence structure.

The LaTeX fragment requires a host document defining the diplomatic macros specified in the task and loading the relevant standard mathematics and TikZ/tikz-cd packages. Full TeX compilation was unavailable because the installed binaries lacked the required format and package data; no compiled or rendered typesetting proof is claimed. Diagrams and drawings should be checked in the eventual host edition.

Supporting files preserve the notation and doubt records, calculation scripts/results, source-verification registers, and the writing/audit tools. Scripts under tools/session_scripts record earlier writing stages; the page files named in frozen_sha256.json are the final transcription, and earlier script strings are not an alternative final text.

To run the mechanical page validation after extraction:

    python tools/validate_package.py

To reproduce the mathematical calculations, a Python environment with SymPy is needed:

    python research/check_calculations.py

The per-note context-search script additionally needs the two original context files in the supplied relative workspace location. The original scans, image crops, attached ZIPs, context-source files, and external research PDFs are not included in this archive.

