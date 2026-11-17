# Mechanical syntax support report

Generated: 2026-11-17 22:08:22 UTC

## Scope

The support agent examined only saved deliverable text. No scan images or research
context files were opened, and no transcription readings or production records
were changed. This report cannot establish visual completeness or manuscript
accuracy.

## Available compilation infrastructure

`pdflatex`, `lualatex`, `xelatex`, `latex`, and `kpsewhich` binaries are present.
The detected engine is pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian).
However, `kpsewhich` found none of `article.cls`, `amsmath.sty`, `amssymb.sty`,
`tikz.sty`, `tikz-cd.sty`, `pgf.sty`, `ulem.sty`, `fontspec.sty`, `geometry.sty`,
or `xcolor.sty`. An actual compile attempt stopped before reading any page with
`I can't find the format file pdflatex.fmt!`. Full compilation and visual layout
verification therefore did not occur.

`compile_harness.tex` is a separate validation harness, not a transcription
preamble. It contains input commands for the 17 pages saved at harness creation;
regenerate its input list before checking later pages. Its apparatus definitions
pass arguments through and accept both braced and single-token arguments. The
exact failed attempt is saved in `compile_attempt.txt`. The command was:

```sh
pdflatex -no-mktex=fmt -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory records/compile_build records/compile_harness.tex
```

Run from the package root. Automatic format generation was disabled. No TeX
packages were installed and no external resources were fetched.

## Static checks

At this report's creation, the package validator examined 18
saved page fragments and found 0 mechanical errors
and 0 warnings. Missing later work remains
informational in partial mode. The validator was updated to recognize legal
unbraced single-token apparatus arguments; focused parser assertions passed.

A separate conservative scan found no unmatched math delimiters and no unequal
per-page `\left`/`\right` counts. Ten initial nested-dollar warnings were manually
reviewed and resolved: they are five ordinary inline-math pairs inside
`\text{...}` on scan 090 line 28, scan 094 lines 17 and 24, and scan 095 line 31.
These are valid LaTeX uses and are not outstanding structural findings.

These lexical checks do not replace compilation. They do not validate TikZ option
names, arrow destinations, macro expansion, math/text compatibility, or rendering.

To refresh the separate harness with later saved pages, run:

```sh
python records/update_compile_harness.py
```
