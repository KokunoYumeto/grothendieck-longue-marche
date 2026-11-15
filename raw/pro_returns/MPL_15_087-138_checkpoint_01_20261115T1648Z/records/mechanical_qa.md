# Mechanical QA record

Recorded 2026-11-15 16:13:45 UTC.

## Scope

The ancillary check covered completed scans 087–102: 16 page files and 231 inventory rows. The partial validator reported zero structural errors and seven review flags for ellipses or “etc.” These checks establish neither transcription accuracy nor visual completeness; no manuscript images or research-context contents were inspected by the mechanical-checking worker.

A subsequent diagram syntax check found one terminal backslash at scan 102, line 15, where the matrix row continued onto the next source line. This was reported to the primary reader, who confirmed that the image has two rows and is handling the correction. The validator now flags a single backslash at a line end within `tikz-cd` for human review. A suspected `\de` occurrence in scan 100 was a tokenization false positive: the source contains a node line break followed by `de`.

## Compilation attempt and environment limit

The combined transcription was rebuilt with `workflow.combined()`. A temporary snapshot and wrapper were used outside the package directory. LuaLaTeX stopped before parsing the document with:

```text
I can't find the format file `lualatex.fmt'!
```

`kpsewhich` found none of `lualatex.fmt`, `xelatex.fmt`, `pdflatex.fmt`, `lualatex.ini`, `xelatex.ini`, `latex.ltx`, `tikz.sty`, `tikz-cd.sty`, `fontspec.sty`, or `ulem.sty`. The engine executables are present; the required TeX distribution files are unavailable. Consequently, no successful compilation or rendered-document verification is claimed. No dependency installation was attempted.

## Reusable harness

`records/compile_wrapper.tex` contains the macro definitions and package imports for a future syntax check. Run it from the package root with an existing temporary output directory, as its header describes. It inputs the current combined transcription directly; no duplicate transcription snapshot is included in the package. The editorial macros retain their arguments with minimal presentation. This harness is for mechanical compilation checks only.

## Follow-up mechanical check: scans 087–120

Recorded 2026-11-15 16:34:49 UTC. The combined transcription was rebuilt with `workflow.combined()` before validation. The checked set comprised 33 page files and 484 inventory rows, excluding the omitted scan 116. The package remains unfrozen.

The partial validator reported zero structural errors: page markers and ordering, combined-file correspondence, inventory structure, completion-log events, brace balance, and environment balance passed. No single-backslash row-separator warning remained, including the previously reported scan 102 location. All authorized state-macro occurrences had braced arguments. Additional syntax counts found an even number of unescaped dollar signs on every page, matching opening/closing display and inline math delimiters, and matching `\left`/`\right` counts. These are syntax checks, not a substitute for compilation or visual reading.

The 12 remaining review flags concern explicit ellipsis syntax or “etc.” at scans 092, 094 (two), 097, 099, 100, 101, 105 (two), 106, 110, and 120. They are review candidates only; they do not establish omissions. No other concrete defect was found in this pass.

### Authorized state-macro counts

| Macro | Count |
|---|---:|
| `\cotefile` | 1 |
| `\scanpage` | 33 |
| `\mspage` | 28 |
| `\deleted` | 149 |
| `\inserted` | 75 |
| `\margin` | 49 |
| `\uline` | 116 |
| `\uuline` | 0 |
| `\diagram` | 22 |
| `\figure` | 4 |
| `\unsure` | 277 |
| `\illegible` | 3 |

Every page containing `\unsure` or `\illegible` had at least one registered doubt row. The exported doubt register contains 151 rows for scans through 120. This page-level presence check does not establish that each individual doubtful reading is covered: a register row may group several occurrences, and numerical counts alone cannot resolve that relationship. The validator now offers `--macro-report` to print macro counts and scan-level exported register-row counts.

No manuscript images or context-archive contents were inspected during this pass. No page transcription was changed. No new compilation attempt or dependency installation was made; the previously documented TeX distribution limitation still governs the available verification.
