# Optional syntax compile harness

This scratch folder contains a stable snapshot of the first 30 page files available when the harness was prepared (097–127 except 123). The source page files were not modified. A later static check of 31 pages (through 128) found no brace, environment, display-delimiter, left/right-count, or dollar-parity problems.

Compilation is BLOCKED BY THE ENVIRONMENT, before any page is read. Executable launchers exist, but kpsewhich cannot locate lualatex.fmt, pdflatex.fmt, xelatex.fmt, latex.ltx, article.cls, mathtools.sty, tikz-cd.sty, ulem.sty, or fontspec.sty. Every initial FAIL in compile_report.txt therefore means an environment failure, not a page-source error.

Dependencies in preamble.tex: LaTeX article, geometry, fontspec (LuaLaTeX), amsmath, amssymb, mathtools, tikz-cd, and ulem. The manuscript bracket commands use mathtools. The harness makes editorial-state macros transparent, except for printed scan/page identifiers and illegibility markers, because its purpose is syntax checking. It redefines the existing article figure command for the requested one-argument drawing macro. It reads diagram arguments with active ampersands so tikz-cd matrices can be wrapped in the requested diagram macro; the array case receives ordinary alignment tabs by expansion. This wrapper is prepared but cannot be runtime-validated without LaTeX dependencies.

To try one snapshot when a complete LaTeX installation is available, change into its directory and run:

```bash
lualatex -interaction=nonstopmode -halt-on-error -file-line-error check.tex
```

Do not present these scratch compile files or any generated PDF as the requested transcription. No image or context was examined during this QA.
