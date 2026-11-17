# MPL_84_097–145

This package contains the diplomatic transcription and separate research notes for cote 84, scans 097–145, with blank scan 123 omitted as in the supplied attachment. The archive order is retained, including the reused typed page numbered 480 at scan 143.

## Authoritative deliverables

- `MPL_84_097-145_transcription.tex`: the complete ordered LaTeX fragment, without a document preamble.
- `pages/`: the 48 individual frozen page fragments.
- `MPL_84_097-145_doubts.md`: the package notation table, 475 doubt occurrences, abbreviation glossary and legibility account.
- `MPL_84_097-145_inventory.csv`: 1,001 recorded elements, all marked `yes`, using the requested eight columns.
- `MPL_84_097-145_notes.md`: the integrated research notes, including context comparisons, the two standing questions, and tables and enumerations.
- `progress.log` and `freeze.sha256`: the completion and second-audit records, transcription hashes, context-opening record and final verification.

The sheet categories are 36 mathematical text faces, one cancelled draft, and 11 reused typed faces; no cover is present. The one `\illegible{1}` marks a cancelled word on scan 097; the other 474 registered uncertainties are `\unsure` occurrences, including repeated doubts and uncertainty in cancelled material. A count of inventory elements is not a word count or a guarantee of error-free handwriting recognition.

## Reading and freeze protocol

The root transcriber alone read the whole-page images and overlapping halves in scan order, saved each page before proceeding, and then visually audited every page again. No OCR was used, and handwriting transcription or visual audit was not split among agents. The notation comparison included exclamation exponents versus primes, the scope of bars, alphabets, quotation marks, uncertain arrowheads, cancellations, insertions and folio placement.

The 48 page files and combined transcription were frozen at **2026-11-17 00:13:12 UTC**. The context contents were opened at **00:13:19 UTC**, and the README and results register were read before research-note writing began. An initial listing of the context ZIP's directory metadata had occurred before the freeze; that procedural deviation is explicitly recorded in the first protocol line of `progress.log`. No context file contents were read or extracted at that earlier stage.

After the freeze, text-only work on context comparison, calculations, enumeration and packaging was delegated. The root reviewed and integrated those outputs. Context-suggested changes appear only as reading questions in the notes; none changes the 49 frozen transcription files. The final hash verification is recorded in the log.

## Research records and reproducibility

`research/` retains the component note drafts, per-item context searches, calculation reports and enumeration records used to assemble the integrated notes. `research_leads.md` is the source-only first-pass lead log, with its audit corrections appended; it is a historical working record, not the final research assessment. The integrated notes are the primary research deliverable when wording differs from an earlier draft.

The scripts below can be run with Python 3 from the package directory. The symbolic calculation and enumeration scripts require SymPy; the finite-ring and package checks use the Python standard library.

```sh
python3 scripts/package_tools.py check
python3 scripts/package_tools.py verify-frozen
python3 scripts/check_tex_structure.py
python3 scripts/research_algebra_checks.py
python3 scripts/research_relative_norm.py
python3 scripts/research_extensions_checks.py
python3 scripts/recompute_enumerations.py
```

The algebra scripts print reports to standard output, and the saved results are in `research/`. They test explicitly stated finite-ring examples or universal polynomial identities; they do not infer a reading from mathematics and do not modify the transcription. The enumeration script uses `research/earlier_typed_pagination.json` as a provenance-labelled, derived input for the neighbouring packet’s reported pagination. Context-search scripts require the four supplied Markdown context files at the relative location documented in those scripts; the context attachment itself is intentionally not duplicated in this archive.

The `scripts/pageNNN.py` and `scripts/finishNNN.py` files preserve the actual first-pass write operations for recovery. **Do not rerun these historical scripts over the frozen page files:** they predate the final visual audit and can overwrite audited readings. The authoritative version is the page fragment matching `freeze.sha256`. The package tool refuses to recombine or refreeze a transcription once its freeze is recorded.

## Mechanical checks and their limits

The package was checked for the exact 48-file scan set, individual scan markers, combined-file order and agreement, inventory schema and coverage, all-`yes` entries, balanced TeX structure and preservation of all 49 hashes. The mechanical reports are under `scripts/mechanical_qa/`; records labelled as candidates or generated before the audit are historical checks, not alternative transcription files.

A full TeX compilation was attempted but could not be completed because the available TeX installation lacks the required formats/packages; `scripts/mechanical_qa/compile_report.txt` records that limit. The requested deliverable is a fragment using the supplied editorial macros, standard mathematical LaTeX, TikZ and `tikz-cd`; the receiving document must define the editorial macros. No claim of successful rendered-page compilation is made.

The source scans and input ZIPs are excluded. The only archive to use as the final deliverable is `MPL_84_097-145.zip`; earlier hourly checkpoints preserve earlier stages and are not substitutes for the final frozen transcription and integrated notes.
