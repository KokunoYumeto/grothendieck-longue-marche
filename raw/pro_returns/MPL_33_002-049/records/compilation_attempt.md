# Compilation attempt

A separate 48-page source snapshot and a temporary LaTeX harness were prepared. No manuscript source was changed.

The executable `/usr/bin/lualatex` exists, but execution stopped before reading the harness because `lualatex.fmt` is absent. `kpsewhich` also found none of `latex.ltx`, `pdflatex.fmt`, `xelatex.fmt`, `article.cls`, `amsmath.sty`, `tikz.sty`, `tikz-cd.sty`, or `ulem.sty`. Thus actual TeX compilation was unavailable; this is an environment limitation, not a diagnosed manuscript-source error.

The harness uses identity definitions for deletion, insertion, marginal, figure, and doubt wrappers, and an ampersand-aware diagram wrapper so TikZ-CD matrices can be read as macro arguments. It is only a syntactic check harness, not a proposed presentation of the diplomatic transcription. It requires ordinary LaTeX, AMS, fontspec, ulem, TikZ, and TikZ-CD packages. Its copied page inputs remain in the temporary scratch directory, outside the deliverable package; the source snapshot hashes are retained in `compile_snapshot_hashes.tsv`.

`compile_stdout.txt` preserves the failed invocation's diagnostic. `compile_harness.tex` preserves the exact harness used. No compilation-success claim is made.
