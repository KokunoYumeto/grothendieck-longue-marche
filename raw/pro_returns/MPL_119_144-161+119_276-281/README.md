# MPL_119_144-161+119_276-281

This package separates the diplomatic transcription, its reading apparatus, and the subsequent research notes. The required scan order is **144, 145, 146, 148–153, 155–161, 276–281** in cote 119: 22 pages. Scans 147 and 154 were omitted as blank in the supplied input set.

## Contents

| File or directory | Purpose |
|---|---|
| `MPL_119_144-161+119_276-281_transcription.tex` | Combined LaTeX fragment, in scan order, without a document preamble. |
| `pages/` | One LaTeX fragment per scan, named `MPL_119_144-161+119_276-281_119_scanNNN.tex`. |
| `MPL_119_144-161+119_276-281_doubts.md` | Recurring-notation table, individual reading doubts, abbreviations, and legibility assessment. |
| `MPL_119_144-161+119_276-281_inventory.csv` | Page-element inventory with the specified eight columns and explicit transcription status. |
| `MPL_119_144-161+119_276-281_notes.md` | Research notes written after the transcription freeze and context opening. |
| `CHECK_EVENTS.tsv` | Statement-by-statement event accounting: `statement_id`, `date`, `who`, `type`, `outcome`. |
| `progress.log` | UTC work records, page completions and second readings, frozen SHA-256 hashes, context opening, checkpoints, and final integrity verification. |
| `scripts/record_page.py` | Page-saving support used during the sequential transcription workflow. |
| `scripts/package_transcription.py` | Mechanical validation, assembly, hash freeze/verification, and archive creation. |
| `scripts/compile_wrapper.tex` | Optional support preamble for local TeX compilation; its labels and colors are editorial display conventions. |
| `scripts/search_note_context.py` and `research/context_queries.tsv` | The actual per-note context searches, with their results in `research/context_searches.tsv`. |
| `scripts/assemble_check_events.py` | Explicit mapping of support-note identifiers into the final note identifiers; consolidates the actual event ledgers without inferring proof events. |
| `research/topology_research.md` | Detailed hypotheses and direct proofs behind the short topology notes. |
| `research/finite_research.md`, `research/finite_checks.py`, `research/finite_checks.json` | Finite-geometry proof details, executable exact computations, and their recorded output. |
| `research/report_research.md` | Detailed comparison of the report with Hua's neighbouring institutional exposition, including voting denominators. |
| `research/*_check_events.tsv` and `research/*_context_search.tsv` | Research-support provenance; the canonical event table is the top-level `CHECK_EVENTS.tsv`. |

The supplied scan and context archives are not redistributed here. In an interim checkpoint, files for work not yet performed may be absent; `progress.log` records the completed work.

## Completed scope and research status

The final package contains 22 per-scan fragments, their combined fragment, an inventory of 428 elements marked `yes`, and 80 numbered research notes. Every numbered note has a recorded context query and at least one corresponding check/use event; the canonical event table contains 176 records, distinguishing textual comparisons, targeted proof checks, independent short re-proofs, ordinary exact computations, background uses, and specifically scoped refutations. A computation event is not a proof-assistant certificate. The original support ledgers retain their local F/T/R identifiers; the consolidation script supplies the explicit mapping to the final N identifiers, with the originating event retained in each outcome.

One transcriber read and audited the scans in the prescribed order, without OCR or delegated image reading. Research assistants worked only after the transcription freeze, using the frozen text and supplied context; an infrastructure assistant also prepared packaging support without reading the scans. The 22 page fragments and their combined transcription were frozen at **2026-11-18 01:39:27 UTC**, and the context file contents were first opened at **01:39:35 UTC**. **Protocol deviation:** the context ZIP's central-directory member names and sizes had been listed during initial archive inventory, before the freeze; no member contents were read then. That early metadata access is recorded in the first entries of `progress.log` rather than represented as a fully closed archive.

The main notes distinguish manuscript wording, Hua's supplied modernised interpretation, earlier result-register claims, and this run's limited checks. In particular, a note marked “unproved claim” identifies the manuscript's initial status; a later event may establish a precisely stated special case or refinement, and its outcome specifies that scope. An earlier register's “Proved,” “Known,” or “Refuted” is carried with its supplied review qualification, without automatically certifying its proof. No uncertainty or mathematically motivated correction from the research phase was imported into the frozen transcription.

## TeX requirements and editorial macros

The transcription is a fragment intended to be included in a document that supplies these macros:

| Macro | Meaning in the transcription |
|---|---|
| `\cotefile{...}`, `\scanpage{...}`, `\mspage{...}` | Archive file, PDF scan number, and a visible authorial page number. |
| `\deleted{...}`, `\inserted{...}`, `\margin{...}` | Deletion, insertion at its intended textual position, and an independent marginal note. |
| `\uline{...}`, `\uuline{...}` | Single and double underlining. |
| `\unsure{...}`, `\illegible{...}` | Explicit reading doubt and an estimated unreadable word count. |
| `\diagram{...}`, `\figure{...}` | Typeset diagrams/tables and TikZ reconstructions of drawings. |

The optional wrapper uses standard LaTeX together with `fontenc`, `inputenc`, `textcomp`, `geometry`, `amsmath`, `amssymb`, `mathtools`, `mathrsfs`, `xcolor`, `ulem`, and `tikz-cd`. TikZ libraries include `arrows.meta`, `calc`, `decorations.pathmorphing`, and `shapes.geometric`; the latter supplies elliptical node shapes such as `|[draw,ellipse]|`. `amssymb` supplies `\approxeq`. The wrapper gives `\textcircled` a math-mode branch for TikZ-cd cells while preserving its text behavior. Its other math/text branches display deleted, inserted, and uncertain material visibly, including arrow labels. Its `\figure` macro supplies the task's content wrapper and replaces the article class's figure-float opening command; do not also use a `figure` environment with this wrapper.

Because TikZ-cd blocks occur inside `\diagram` arguments, including two nested inside `\margin`, the wrapper scopes the active-ampersand workaround from the [TikZ-cd manual, §3.4](https://tikz.dev/tikz-cd/advanced-usage) to its input group. This preserves the transcription's plain `&` tokens and addresses the documented argument-tokenization conflict without editing the manuscript files. The manual notes that this workaround can interact with other packages; the current wrapper and its nested labels still require a successful compilation before their rendering can be certified.

From the package root, a suitable local compilation command is:

```sh
mkdir -p tex_build
pdflatex -no-mktex=fmt -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=tex_build scripts/compile_wrapper.tex
```

**Recorded compilation limitation:** on 18 November 2026, TeX engine executables were available in the execution environment, but `kpsewhich` could not resolve `article.cls` or the requested packages. An entirely fabricated smoke sample failed before the wrapper was parsed, with ``I can't find the format file `pdflatex.fmt'!``. Accordingly, that test did not establish that the wrapper or manuscript fragments compile. No manuscript content was read or compiled by the infrastructure assistant. The fabricated sample is not included in this package. The `-no-mktex=fmt` flag prevents automatic format-generation attempts.

## Mechanical verification and packaging

Run support commands from the package root:

```sh
python scripts/package_transcription.py validate --partial
python scripts/package_transcription.py validate
python scripts/package_transcription.py assemble
python scripts/package_transcription.py freeze
python scripts/package_transcription.py verify-frozen
python scripts/package_transcription.py verify-frozen --record
python scripts/package_transcription.py checkpoint
python scripts/package_transcription.py final-zip
```

These commands are alternatives for the relevant stage, not a sequence to rerun indiscriminately. `assemble` and `freeze` refuse to operate after the recorded freeze. `freeze` requires completed page and second-reading log records; it hashes the 22 page files in scan order and then the combined fragment, and appends `transcription frozen` with its UTC time. `verify-frozen` checks those bytes and the hash/event ordering without editing the transcription. Its optional `--record` flag writes the successful verification to the log.

`checkpoint` is restricted to the hourly schedule measured from the log's starting time and uses a new numbered filename. Its `saved` record denotes successful local ZIP creation; durable upload is a separate operation recorded by the main worker. `final-zip` requires the complete expected page set, inventory, additional deliverable files, a populated check-event table, and a post-freeze context-opening record. It verifies the frozen hashes and records their unchanged status before packaging. Both archive commands refuse to overwrite an existing ZIP and accept `--output-dir PATH`.

The archive excludes supplied-input directories, scan images, previous ZIPs, bytecode/cache directories, and optional TeX build directories. Symlinks are rejected. Included support scripts and this README are documentation; they are not part of the manuscript transcription.

## Limits of automated checks

The packaging utility checks filenames, scan markers, inventory fields and statuses, unescaped brace balance, literal `\begin`/`\end` environment balance and nesting, the prescribed concatenation, exact inventory/check-event table headers, event-table shape, log protocol, and SHA-256 integrity. Its lexical pass ignores ordinary comments and inline `\verb` spans, and distinguishes a double-backslash line break from a control word. It is not a TeX expansion engine: macro-generated environment names, verbatim environments, math-mode correctness, TikZ option validity, and layout still require a working compiler and review. It cannot establish whether every visible word, symbol, deletion, insertion, or drawing was transcribed, whether readings are accurate, or whether mathematical claims are true.

The support-code review passed Python syntax parsing and seven checks using fabricated log strings: acceptance of an ordered completion/audit sequence; rejection of premature audits, reversed timestamps, reordered hashes, hashes after the freeze, context opening before the freeze, and a context timestamp before the freeze timestamp. These checks did not access manuscript text or modify the work log.

A later lexical pass extracted command/environment names and counts only. It found 61 balanced and correctly nested environments across the 22 page files and verified both required table headers. The environment checker was also exercised on fabricated balanced, missing, extra, and crossed delimiters, with comment, inline-verbatim, and double-backslash cases. These are structural checks, not readings of the manuscript or compilation results.

Visual coverage, insertion placement, sign consistency, the recurring-notation comparison, and the second reading must be performed against the images. The doubts file must be checked for its notation table, abbreviations, and legibility assessment; the notes must address the requested research categories and both standing questions. Check-event types must describe the work actually performed. These substantive checks remain the main transcriber's responsibility and cannot be inferred from a successful packaging command.
