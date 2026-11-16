# Mechanical preflight report

## Scope and timing

This report records mechanical checks of the first-pass LaTeX files before the
primary transcriber completed the second visual reading and before the
transcription was frozen. It is not a final validation report. No scan image or
context document was read for these checks, and no page, inventory, combined
transcription, or existing record was modified by the mechanical checker.

These checks do not establish paleographic accuracy, completeness against the
images, or fidelity of diagram geometry. Those matters remain the responsibility
of the primary transcriber's visual audits. Counts below describe the preflight
snapshot; in particular, the inventory row count may increase during auditing.

## Checks passed at preflight

- All 34 expected page filenames, scans 002–035, were present.
- Each page had its correct `\scanpage` header, and the first began with
  `\cotefile{60}`.
- The combined transcription equalled the literal bytewise concatenation of the
  ordered page files.
- Grouping braces balanced after excluding TeX comments and escaped literal
  braces.
- Environment openings and closings were correctly nested and matched.
- Inline dollar signs and display delimiters balanced on every page.
- Counts of `\left` and `\right` matched on every page.
- The token scan found no stray alignment characters outside applicable
  environments, unescaped parameter characters, obvious doubled subscripts or
  superscripts, or math-script characters outside mathematical contexts.
- The inventory contained 543 rows, all with valid fields and `transcribed=yes`,
  covering all 34 pages.
- The command inventory contained standard LaTeX, AMS, and TikZ commands and the
  requested transcription macros. No accidental additional nonstandard command
  names were found.
- Inspected TikZ paths had terminating semicolons and balanced syntax. The
  diagram-arrow destinations inspected remained within their displayed grids.

## Expected prefreeze omissions

The validation script had no separate prefreeze mode. At the time it was run,
its only error was the absence of the research-notes file,
`MPL_60_002-035_notes.md`. It also warned that
`records/frozen_hashes.json` did not yet exist. These were expected omissions
at that stage, not findings about transcription content. Final validation must
be rerun after those files exist.

## TikZ encoding issue reported to the primary transcriber

Multi-column `tikzcd` environments were enclosed in `\diagram{...}` macro
arguments. With a conventional one-argument wrapper, literal ampersands can
produce TikZ matrix catcode errors. The recommended mechanically equivalent
encoding is `ampersand replacement=\&` in the environment options and `\&`
as the cell separator. The affected environments were on scans 013, 025, 026,
and 035. Single-column `tikzcd` environments and ordinary `tabular` tables do
not require this change for that reason.

The primary transcriber stated that these encoding changes would be applied
while auditing the affected pages. This preflight report does not assert that
the subsequent changes were completed; final checks should establish that.

## TeX compiler and package availability

| Component | Preflight observation |
| --- | --- |
| `pdflatex` | Executable present and version command ran; pdfTeX 1.40.26 |
| `lualatex` | Executable present and version command ran; LuaHBTeX 1.18.0 |
| `xelatex` | Executable present |
| `latex` | Executable present |
| `kpsewhich` | Executable present |
| `tectonic` | Not installed |
| `article.cls` | Not found by the active `kpsewhich` lookup |
| `amsmath.sty` | Not found by the active `kpsewhich` lookup |
| `amssymb.sty` | Not found by the active `kpsewhich` lookup |
| `tikz.sty` | Not found by the active `kpsewhich` lookup |
| `tikz-cd.sty` | Not found by the active `kpsewhich` lookup |
| `ulem.sty` | Not found by the active `kpsewhich` lookup |
| `fontspec.sty` | Not found by the active `kpsewhich` lookup |

The engine executables were available, but the active configuration did not
provide a usable standard LaTeX/AMS/TikZ package installation. **No document
compilation succeeded, and no successful compilation is claimed.** The results
above come from structural inspection, not from a compiler run.

For any later rendering harness, `\figure` is already a LaTeX environment
command. Implementing the requested one-argument transcription wrapper therefore
requires an intentional redefinition rather than an ordinary `\newcommand`.
This is a harness consideration, not a defect in the required LaTeX fragment.

## Final-validation requirements

After visual audits, recombine the page files and rerun the structural validator.
After freezing and completing the research notes, verify every recorded SHA-256
again and rerun the required-file and inventory checks. Treat any final compiler
claim separately from these preflight checks and make it only if an actual
compilation succeeds.
