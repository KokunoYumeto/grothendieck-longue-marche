# Mechanical QA records

## Final structural checks

`latest_structure_report.txt` and the final validation summary record checks of the completed 48-page set. The checker examines braces, environments, display/inline delimiters, left/right delimiter counts and dollar parity. It does not certify successful compilation, visual accuracy or completeness of the transcription.

The inventory proposal files, row map, doubt-register components and notation inventory preserve work leading to the final audit. The authoritative text is in `../../pages/` and matches `../../freeze.sha256`; the final assembled doubts file is at the package root. Older candidate files can contain superseded suggestions.

## Historical compilation attempt

The initial compile attempt used the first 30 available page fragments (097–127 except 123). It failed before reading their TeX: the launcher could not find `lualatex.fmt`. Additional environment checks could not locate `pdflatex.fmt`, `xelatex.fmt`, `latex.ltx`, `article.cls`, `mathtools.sty`, `tikz-cd.sty`, `ulem.sty` or `fontspec.sty`. The raw launcher outputs are retained in `compile_outputs/`, and every historical FAIL in `compile_report.txt` refers to this environment block.

`preamble.tex` is the provisional syntax-check preamble from that attempt. Its temporary snapshot wrappers are not final deliverables and are not included here. During the later visual/notation audit, the manuscript grouping brackets were redrawn with TikZ, removing the provisional mathtools-only bracket commands from the frozen transcription. A receiving LaTeX document still needs definitions of the user-requested editorial macros and the required mathematical/TikZ packages.

No full rendered-page compilation was achieved. Re-running the structure checker is supported; a real compilation should use the final frozen fragments in a complete LaTeX environment, rather than treating the historical attempted wrappers as a verified reader edition.
