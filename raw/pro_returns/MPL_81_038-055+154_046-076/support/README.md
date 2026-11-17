# Structural validation support

**Historical work record.** The opening preparation statements below describe the initial preflight phase. Later authorized compilation, uncertainty extraction, and post-freeze research are documented in the appended sections, `research/`, and the final `records/method.md`. Original manuscript images were read only by the primary transcription reader. The current final source checks are in `records/final_validation.json`; the latest prefreeze compile is `validation/compile_07_final_prefreeze.json`.

This support work did not open any scan, page transcription, context document,
or prior package. The validator is non-mutating; its results are structural and
cannot establish transcription accuracy or completeness against the images.

## Validate the completed deliverable

```bash
python /workspace/scratch/89f8415d3ab0/support/validate_package.py /workspace/scratch/89f8415d3ab0/deliver
```

For machine-readable output, append `--json` and redirect stdout if a persistent
report is wanted. Exit code 0 means the specified checks passed; 1 means at least
one check failed.

The combined transcription is required to equal the exact ordered concatenation
of all 31 page files, with no additional separators. End each page file with the
desired newline(s) before concatenating it. The first page must begin with
`\cotefile{154}` and `\scanpage{46}`; subsequent pages begin with their own scan
marker and do not repeat the cote marker. Inventory element identifiers must be
unique within each scan. Text, notes, and doubts are not semantically inspected.

Synthetic verification covered a complete 31-page fixture, escaped braces and
percent signs, comments containing braces, an unclosed group, and a combined-file
mismatch. No real page content was opened during that verification.

## Extract uncertainty occurrences

```bash
python /workspace/scratch/89f8415d3ab0/support/extract_uncertainties.py \
  /workspace/scratch/89f8415d3ab0/deliver/pages
```

The command emits JSON to stdout and does not modify any page or doubts file.
It finds every literal `\unsure{...}` and `\illegible{...}`, including nested
occurrences and figure labels. Each occurrence includes cote, scan, source file,
one-based source line and column, global ordinal, per-page ordinal, macro name,
the nearest preceding `% E: kind|position|first words` marker, the exact raw
argument, its first reading, and an array of alternatives.

Only unescaped pipes at brace depth zero divide alternatives. Whitespace and
source spelling are retained. Pipes inside nested groups, comments, escaped
`\|`, and verbatim material do not divide alternatives. The parser skips
uncertainty-like strings inside comments or verbatim content. It does not expand
TeX or infer the mathematical meaning of literal top-level pipes. Missing or
unclosed arguments appear in the JSON `errors` array and cause exit status 1.
No confidence or reading judgment is supplied.

## Refresh an audited page's inventory

```bash
python /workspace/scratch/89f8415d3ab0/support/record_page.py 46 --inventory-only
```

This replaces that scan's inventory rows using the current page file, without
appending a `done` timestamp to `progress.log`. When the optional positional
sheet kind is omitted, the existing sheet kind is retained. An explicit kind
may still be given, for example `46 text --inventory-only`. If existing rows
disagree on the sheet kind, the script stops before writing and requests an
explicit kind. The original `record_page.py SCAN [SHEET_KIND]` invocation retains
its behavior of updating inventory and appending one `done` timestamp.

The `--root` option supports a different deliverable directory and was used only
with synthetic fixtures during verification. Page bytes and progress-log bytes
were checked unchanged in the inventory-only fixture. Nested parsing, source
locations, ordinals, error reporting, JSON output, sheet-kind retention, and
ordinary completion logging were also checked. The result is recorded in
`mechanical_tools_verification.json`. No real page files were opened or modified
by the support agent.

## Current Library transfer helpers

The files in `library_helpers/` were obtained from the currently advertised
`c0/library` skill resources during this task. They have not been used to upload
or download any artifact. The two files are colocated so the optional hosted-app
companion can be imported when needed.

After a successful direct create of one ZIP, the parent should run
`library_file_transfer.py apply-xattrs ABSOLUTE_ZIP_PATH EXACT_LIBRARY_FILE_ID`
with the complete returned xattrs array (or `[]`) as JSON on stdin, in the same
code-mode invocation as the successful create call. Do not include credentials
or returned private URLs in the deliverable.

## Create an external compilation wrapper

The wrapper generator reads page filenames and filesystem metadata only. It
does not read or modify any source page, and it refuses to place the wrapper
inside the source pages directory.

From the task directory, create the wrapper with:

```bash
python support/create_validation_wrapper.py deliver/pages \
  --output support/validation/manuscript_validation.tex --landscape
```

Only when manuscript compilation is authorized, compile it with:

```bash
python support/run_xelatex.py \
  -output-directory=/workspace/scratch/89f8415d3ab0/support/validation \
  /workspace/scratch/89f8415d3ab0/support/validation/manuscript_validation.tex
```

The resulting external PDF is
`support/validation/manuscript_validation.pdf`; source page files are untouched.
Keep the generated preamble and macro definitions in this external wrapper.
The user's deliverable remains a LaTeX fragment without a preamble.

The wrapper supports text and math uncertainties, uncertainties in TikZ nodes
and tikz-cd labels, single and double underlining, long editorial macros with
multiple paragraphs, and deleted blocks containing formulas, diagrams, or
drawings. The `diagram` and `figure` wrappers retokenize their arguments so an
ordinary `&` in a tikz-cd or TikZ matrix works even inside nested editorial
macros. Explicit `ampersand replacement=\&` also works. Arrays are supported
inside their normal surrounding math delimiters.

Validation styling uses orange for uncertainty, red for deletion, blue for
insertion, and violet for margin notes. These are unboxed groups, allowing whole
paragraphs and graphics to compile. Deletions are distinguished by color rather
than a strikeout across whole blocks; this PDF is a compilation aid. Each source
scan starts on a fresh PDF page with its cote and scan header.

The `--landscape` option uses A4 landscape with 14 mm margins. It removed the
overfull boxes reported in the initial portrait validation layout. The default
without this option remains portrait. The wrapper emits a `PDFPAGE` marker for
each scan to support exact PDF-page mapping.

The synthetic two-page fixture in `compile_fixture/` compiled successfully. It
exercised all these contexts, including raw and escaped matrix separators,
nested editorial macros, paragraphs inside underlining, and deletion of a
whole drawing and diagram. Its source hashes remained unchanged. The source,
wrapper, PDF, log, standard output, and `verification.json` there are entirely
synthetic. No manuscript compilation was run during that preparation.

Later, explicitly authorized mechanical compilation of the manuscript was run.
The combined run recorded as `validation/compile_05.json` succeeded for all 31
scans and produced 40 PDF pages, with no source errors, no overfull boxes, and no
missing-character warnings. No source page was modified by this support work.
The transcription owner alone made the two reported source syntax corrections.

## Render validation pages for the owner's visual check

```bash
python support/render_validation.py \
  support/validation/manuscript_validation.pdf \
  support/validation/manuscript_validation.stdout \
  --output support/validation/renders
```

This reads the compiled PDF and scan markers in the compilation output, without
reading manuscript source files or scan images. It writes `scan_pdf_mapping.csv`,
`pdf_page_geometry.csv`, and `render_manifest.json`. The default full-page sample
contains 12 PNGs at 150 dpi, selected by vector-path count, curve count, and area.
Two contact sheets cover all 23 PDF pages detected as containing substantial
vector drawing geometry in the current compiled version. Selection is mechanical
and supplies no judgment about the drawing content. The owner performs the visual
comparison. Re-run this command after a later combined compilation if page
boundaries change.

For the complete post-audit review set, render every PDF page onto individual
150 dpi PNGs and distribute all pages over three contact sheets:

```bash
python support/render_validation.py \
  support/validation/manuscript_validation.pdf \
  support/validation/manuscript_validation.stdout \
  --output support/validation/audited_renders --all-pages --contact-sheets 3
```

This was run after `compile_06_audited`, which successfully compiled all 31 scans
to 40 PDF pages after the owner's second visual audit. The current complete
review set and refreshed mapping are under `validation/audited_renders/`.
The three contact sheets cover PDF pages 1–14, 15–28, and 29–40. No review or
interpretation of their content was performed by the support agent.

After the owner's notation concordance, `compile_07_final_prefreeze` succeeded
again for all 31 scans (40 PDF pages). The corresponding complete review set is
under `validation/prefreeze_renders/`, with all 40 pages at 150 dpi and three
contact sheets. The current source hashes still matched those recorded by that
compilation after rendering and uncertainty extraction.

The current literal uncertainty snapshot is
`validation/uncertainties_prefreeze.json`; the current working extraction is also
written to `validation/uncertainties_full.json`. A grouped plain-text review can
be reproduced without reading source pages:

```bash
python support/format_uncertainty_review.py \
  support/validation/uncertainties_prefreeze.json \
  --output support/validation/uncertainties_review.txt
```

The review preserves the exact readings and alternatives using JSON string
escaping, grouped by scan with page ordinal, source line, and nearest element
position. It does not assign confidence or interpret any reading.

## LaTeX environment

`latex_environment.json` records executable discovery and `kpsewhich` results.
The engine executables exist. The initial default configuration resolved none
of the queried packages because its database links were dangling. The follow-up
investigation repaired the search configuration privately, without altering the
system trees, and compiled a synthetic document successfully. See
`tex_runtime/README.md` and use `run_xelatex.py` for compilation.
