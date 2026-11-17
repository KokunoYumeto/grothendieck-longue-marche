# TeX environment check

2026-11-17 16:55:14 UTC

The executables `lualatex`, `xelatex`, `pdflatex`, and `latex` are present. `xelatex --version` reports XeTeX from TeX Live 2025/dev/Debian. However, `kpsewhich` resolves none of `article.cls`, `amsmath.sty`, `amssymb.sty`, `tikz.sty`, `tikz-cd.sty`, or `ulem.sty`.

A temporary QA wrapper was created outside the deliverable, in `../tex_qa/qa_wrapper.tex`, with identity definitions for the diplomatic macros and inputs for the 33 page files then present. It was run with shell escape and format generation disabled.

Exit status: 1

```text
This is XeTeX, Version 3.141592653-2.6-0.999996 (TeX Live 2025/dev/Debian) (preloaded format=xelatex)
I can't find the format file `xelatex.fmt'!
```

This environment-level failure prevents a TeX compilation check. It is not evidence of malformed page content. No page text was modified; no package installation or network download was attempted.
