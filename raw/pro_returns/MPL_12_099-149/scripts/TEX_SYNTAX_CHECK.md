# Optional TeX syntax validation

## Availability in this execution environment

The administrative probe found working pdfLaTeX, XeLaTeX and LuaLaTeX binaries
from TeX Live 2025/dev. `kpsewhich` could not locate even `article.cls`, or `tikz-cd.sty`, `tikz.sty`,
`amsmath.sty`, `amssymb.sty`, `fontspec.sty` or `ulem.sty`. Therefore the available
binaries do not currently provide a usable environment for compiling this
fragment with its diagrams. Nothing was installed or downloaded, and no
manuscript fragment was compiled during preparation of this wrapper.

## Probe without opening manuscript files

```bash
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/tex_syntax_check.py --probe
```

The probe only checks executable and package locations. It does not open the
combined transcription, page files, doubts, inventory or context. Exit status 2
means mandatory tooling is unavailable. Missing packages are reported by name.

## Optional compilation in an adequately provisioned environment

```bash
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/tex_syntax_check.py
```

The default input is `MPL_12_099-149_transcription.tex` in the work bundle. Use
`--fragment /absolute/path/to/fragment.tex` to select a different fragment.
`--engine` accepts `xelatex`, `lualatex` or `pdflatex`; the default prefers
XeLaTeX. All mandatory packages are checked before TeX can open the input. The
script never installs packages, invokes an auto-downloading distribution,
changes the fragment, or rewrites any deliverable.

The generated wrapper and compiler outputs go into a fresh scratch directory
outside the bundle, unless another external `--output-directory` is supplied.
The engine runs once with shell escape disabled and reports a pass/fail result
plus log paths. It does not print manuscript excerpts from diagnostics. The
primary reader must inspect reported errors. A successful exit does not make
overfull boxes, layout warnings or undefined references into reading evidence.

## Macro definitions and limits

The wrapper defines all user-specified editorial macros. `deleted`, `inserted`,
`margin`, `uline`, `uuline` and `unsure` pass their full arguments through, in
either text or math mode. This neutral treatment checks their contents without
claiming to reproduce editorial styling. The alternatives inside `unsure` are
not selected or interpreted.

`diagram` places its argument in display math only when outside math mode, so
both `tikzcd` and mathematical `array` contents can be checked; nested uses
already in math mode pass through. `figure` passes through its TikZ argument and
replaces the class's float-opening command. `illegible` renders its word count
using a mode-aware text label. Page and cote markers receive simple headings.
The wrapper loads AMS mathematics, TikZ and tikz-cd, with common arrow, position
and decoration libraries; `mathrsfs` and `bm` are loaded only if available.

This is an optional syntax aid, not a publishable diplomatic rendering or a
test of manuscript accuracy. The actual delivered transcription remains a
fragment without a preamble or document class. Compilation cannot verify
omitted text, misread symbols, misplaced insertions, diagram geometry, or the
appropriateness of a doubt mark. No manuscript contents were read in preparing
this administrative script and documentation.
