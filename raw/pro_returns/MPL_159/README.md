# MPL 159 — Diplomatic transcription package

This package concerns **cote 159**, *Connexions projectives et uniformisation*,
and contains a diplomatic LaTeX transcription with separate reading doubts,
an element inventory, research notes, and a record of the work.

## Numbering and references

There are **32 retained scans**, numbered **1–34, excluding 14 and 24**. The
omitted scans were identified as blank in the supplied instructions. Scan
numbers are the page numbers of the source PDF, not a new consecutive sequence.

Use cote and scan number as the primary references. `\scanpage{N}` records the
source scan; `\mspage{n}`, when present, records the author's own manuscript
number. Archive foliation is separate and may be recorded in a TeX comment.

“TeX line” references in the doubts table refer to the **individual page file**,
not to the combined transcription and not necessarily to one handwritten line.
Physical line references in research notes are approximate. The combined file
is an ordered concatenation of the page fragments; its line numbers therefore
differ from those of individual files.

## Frozen transcription status

All **32 page completions and 32 personal audits** are recorded. The inventory
contains **761 elements**, all marked `yes`. The doubts register has **441
occurrences: 435 `\unsure` and 6 `\illegible`**.

The transcription was frozen at **2026-11-18 01:04:49 UTC**; the context-opening
event follows at **01:04:50 UTC**. `TRANSCRIPTION_SHA256SUMS` contains **33
hashes**, one for every page and one for the combined fragment. An independent
byte-level comparison verified all 33 against the files and the matching
records in `progress.log`. These are integrity and workflow checks, not
certifications of visual accuracy. Research-note completion is recorded
separately from this transcription freeze.

The completed research apparatus contains **82 individually numbered notes**,
**82 per-note searches of the supplied context**, and **403 check events**.
The notes include dedicated indexes of authorial verification flags and of
title sheets/page counts. Their comparisons distinguish confirmed claims,
counterexamples, unresolved questions, and reading alternatives suggested by
the context; none of those comparisons changes the frozen transcription.

## Contents

| File or directory | Purpose |
|---|---|
| `MPL_159_transcription.tex` | Combined transcription, with no document class or preamble. |
| `pages/MPL_159_159_scanNNN.tex` | One transcription fragment for each retained scan. |
| `MPL_159_doubts.md` | Recurring notation table, occurrence-level reading doubts, abbreviations, and legibility assessment. |
| `MPL_159_inventory.csv` | Page elements and their transcription status, including insertions, deletions, marginalia, diagrams, and drawings. |
| `MPL_159_notes.md` | Research notes prepared after the transcription is frozen; manuscript claims and the reader's ideas remain distinguishable. |
| `CHECK_EVENTS.tsv` | Events recording what was actually checked, used, or refuted during the research stage. Transcription alone is not a mathematical check. |
| `context_searches.tsv` | The 82 actual per-note `rg` searches, retained match locations, and stated context comparisons. |
| `research_checks/` | Detailed post-freeze proofs, counterexamples, exact algebra scripts/certificates, and delegated source event proposals. The main ledger normalizes those proposals to the requested event categories. |
| `progress.log` | UTC completion, audit, freezing, context-opening, and hash-verification records. |
| `TRANSCRIPTION_SHA256SUMS` | The 33 SHA-256 digests defining the frozen transcription bytes. |
| `reading_observations.md`, `audit_changes.md` | Working observations and the record of changes made during the visual audit. |
| `scripts/` | Page-recording, audit-recording, table rebuilding, structural validation, and ZIP-packaging utilities. |
| `scripts/first_pass/` | The original page-commit scripts that existed as saved files; retained as documentation and not rerun during auditing. |
| `scripts/pre_freeze/` | Archived doubt-register preparation script; retained as documentation, not a command to rerun against the final register. |
| `diagnostics/MPL_159_diagnostic.tex` | Optional compilation wrapper, separate from the transcription. |

Research-stage files are produced after the frozen combined transcription.
Their completion status is established by `progress.log`, not by this contents
list. Input scans, supplied context sources,
previous checkpoint ZIPs, and caches are excluded from packaged deliverables.

## Transcription conventions

The fragments use standard LaTeX, TikZ and `tikz-cd`, together with these
editorial macros:

| Macro | Meaning |
|---|---|
| `\cotefile{C}`, `\scanpage{N}`, `\mspage{n}` | Archive file, source scan, and author's manuscript numbering. |
| `\deleted{...}` | Legible struck-through material; unreadable deleted words retain an illegibility marker. |
| `\inserted{...}` | An insertion placed where its attachment indicates. |
| `\margin{...}` | A marginal note that is not an insertion. |
| `\uline{...}`, `\uuline{...}` | Single and double underlining. |
| `\diagram{...}` | A diagram or table reproduced as LaTeX structure. |
| `\figure{...}` | A drawing reproduced with TikZ. |
| `\unsure{reading}` | An uncertain reading. |
| `\illegible{n}` | An estimated number of physically unreadable words. |

The two-reading form `\unsure{reading|alternative}` records two candidates;
the first is the preferred ink reading.

The transcription is not a corrected or modernized mathematical edition.
Notation, spellings, abbreviations, cancellations, and uncertainty belong to
the transcription itself; proposed interpretations belong to the notes.

## Reading, audit, and freezing protocol

All image reading and transcription were performed by the primary reader in
one sequential stream, without OCR or division of pages among readers.
Before freezing, delegated assistance was restricted to scripts, packaging,
and mechanical checks. After freezing, research agents checked selected
mathematical claims against the frozen text and supplied context; they did
not read manuscript images or edit page files. The page-completion and
personal-audit events for all 32 scans are recorded in the log.

The required sequence is: read and save each page with its inventory; reread
every page against the images; reconcile recurring notation; assemble the
combined fragment; record each page's and the combined file's SHA-256 hash;
then log `transcription frozen`. Only after freezing may the context be opened
for the separate research notes. Later context suggestions are reading
questions in the notes, not changes to the frozen transcription. The final
hash check records whether the frozen bytes remain unchanged. Consult the log
for which of these stages have occurred.

## Mechanical checks and optional rendering

The static page checks passed after all 32 personal audits; the final
structural validator also checks the research apparatus and frozen manifest.
These checks cover file and scan coverage, inventory structure,
delimiters, known macros, mathematical mode where detectable, and empty or
phantom-only doubt arguments. These checks do not certify an ink reading or
prove a mathematical statement.

**An actual TeX compilation was unavailable in this environment.** Engine
binaries were present, but the supporting LaTeX files and packages—including
`latex.ltx`, `article.cls`, `amsmath`, `amssymb`, `tikz-cd`, `xcolor`, and
`ulem`—were not available to `kpsewhich`.

With a complete TeX installation, regenerate the wrapper after moving or
extracting the package, then optionally compile it:

```bash
python scripts/check_tex_structure.py --write-wrapper
python scripts/check_tex_structure.py --compile
```

The wrapper is a diagnostic rendering, not an edition of the page layout.
It colors deletion content gray instead of processing it through `ulem`;
this permits deleted paragraphs, displays, and diagrams without forcing them
into a text box. The original editorial macros remain intact in the fragments.
The wrapper's paths are regenerated for the current package location.

For final structural and frozen-byte checks, run:

```bash
python scripts/validate_package.py --json
```

Before the research and freezing stages are complete, use `--partial` for
the appropriate intermediate check. Neither validator changes transcription
files or writes completion, audit, freezing, or research-check events.

To reproduce the small mathematical certificates, run
`python research_checks/basic_checks.py` (requires SymPy) and
`python research_checks/formal_group_checks.py` (standard library only).
Their output certifies the explicit models and finite computations stated
in the reports; the all-orders arguments are written separately.

`scripts/build_research_notes.py` regenerates the research notes and ledger
only when the original supplied context has been extracted beside the package
as `context/`; those input files are intentionally not included here. It does
not modify frozen page files. The original delegated event proposal files are
documentation; `CHECK_EVENTS.tsv` is the authoritative consolidated event log.
