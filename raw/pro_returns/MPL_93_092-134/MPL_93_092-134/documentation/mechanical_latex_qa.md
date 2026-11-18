# Mechanical LaTeX and doubts QA

Checked 2026-11-18 00:52:32 UTC. This is an independent mechanical pass on a snapshot of the 42 saved page files while the root continues the visual audit. No images, context-archive contents, mathematical interpretation, or page edits were involved.

## Macro inventory

No remaining potentially undefined command was identified outside the allowed annotation macros and the usual LaTeX, AMS math, TikZ and TikZ-CD commands. The previously reported `\longdash` is absent. The array on scan 105 now has explicit math delimiters, resolving the earlier wrapper dependency.

| Allowed custom macro | Occurrences |
| --- | ---: |
| `\cotefile` | 1 |
| `\scanpage` | 42 |
| `\mspage` | 6 |
| `\deleted` | 265 |
| `\inserted` | 146 |
| `\margin` | 44 |
| `\uline` | 99 |
| `\uuline` | 0 |
| `\diagram` | 14 |
| `\figure` | 2 |
| `\unsure` | 447 |
| `\illegible` | 1 |

Annotation commands are intentionally not defined by the transcription fragment. A consuming document must supply them. The temporary test wrapper used neutral markers leaving the following brace groups intact, so it introduces no annotation-specific math mode or TikZ argument-capture behavior.

## Actual compilation attempt

- `pdflatex`, `xelatex` and `lualatex` binaries are installed. A temporary XeLaTeX wrapper and the current ordered concatenation were created under `../qa_syntax/` outside the package.
- The exact wrapper, process output, and run metadata are preserved under `documentation/latex_compile_attempt/`. Its `qa_current_pages.tex` input was an ordered snapshot of the page files; that redundant snapshot remains temporary.
- The attempted command was `xelatex -interaction=nonstopmode -file-line-error -no-shell-escape qa_wrapper.tex`.
- The process returned exit code 1 **before reading the manuscript**: `I can't find the format file xelatex.fmt!`.
- `kpsewhich` could locate none of `xelatex.fmt`, `pdflatex.fmt`, `lualatex.fmt`, `latex.ltx`, `article.cls`, `amsmath.sty`, `amssymb.sty`, `tikz-cd.sty`, `fontspec.sty`, or `geometry.sty`.
- Therefore this environment has TeX executables but lacks the formats and packages needed for a genuine LaTeX syntax compilation. **Compilation success is not claimed, and actual compiler-level syntax validation remains unperformed.** No system installation or source substitution was attempted.

## Doubt markers

- `\unsure`: **447** occurrences in page files, excluding comments.
- `\illegible`: **1** occurrence.
- `MPL_93_092-134_93_scan117.tex`, line 13: `\illegible{2}` is in prose, outside explicit math, math environments and diagram wrappers (math=false, diagram=false).

## Doubts-table confidence values

- The confidence table begins on line 19 of `MPL_93_092-134_doubts.md` and contains **272** rows.
- Values: high **4**, medium **83**, low **185**.
- Invalid confidence values or malformed Markdown column counts: **0**.

## Actionable outcome and limits

- No remaining actionable source-syntax or doubt-confidence fault was identified by this pass. Compiler-level confirmation requires a working TeX installation with the listed packages.
- Counts are occurrences, not claims that every ambiguity has its own table row; the table groups some readings. Neither marker counts nor confidence labels establish visual accuracy.
- Neutral annotation wrappers are a syntax-check device, not an approved diplomatic rendering style.
- Files detected changing during this snapshot check: none. Later root edits may supersede counts and line numbers.
