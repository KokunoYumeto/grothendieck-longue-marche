# Private TeX runtime

## Finding

The normal `/usr/share/texlive/texmf-dist` and `/usr/share/texmf` trees contain
LaTeX, AMS packages, TikZ, tikz-cd, fontspec, and babel. Their `ls-R` links point
into absent `/var/lib/texmf` files, while the default `TEXMF` configuration uses
database-only `!!` search paths. Consequently the original package probes
reported no files even though the packages were installed.

No system TeX configuration was modified. `environment.json` removes the
database-only restriction and points writable TeX directories into this private
runtime. A private XeLaTeX format was built successfully from the installed
`xelatex.ini`. Its format-build transcript is retained here.

The missing standard `ulem.sty` was downloaded from CTAN's mirror selector:

- Request: `https://mirrors.ctan.org/macros/latex/contrib/ulem/ulem.sty`
- Selected mirror: `https://latex.us/macros/latex/contrib/ulem/ulem.sty`
- Local file: `texmf/tex/generic/ulem/ulem.sty` (15,682 bytes).

French babel support was absent and was not installed; a UTF-8 French text can
be compiled by XeLaTeX without loading babel. The private format uses the
installed default English hyphenation file because `language.dat` is absent.
This affects typesetting hyphenation, not stored transcription characters.

## Invocation

From the directory containing the temporary validation wrapper:

```bash
python /workspace/scratch/89f8415d3ab0/support/run_xelatex.py wrapper.tex
```

Standard XeLaTeX options, including `-output-directory=...`, can be supplied.
The helper does not alter the source. The TeX engine writes ordinary compilation
outputs to the current directory or the requested output directory.

Use a separate wrapper to define the user's diplomatic macros and input the
fragment. Do not insert a preamble or macro definitions into the deliverable
fragment merely to make it compile.

## Verification

A synthetic, one-page document containing French Unicode characters, AMS math,
a tikz-cd diagram, and a TikZ curve compiled successfully to `smoke.pdf`.
Those logs and source are synthetic; the initial setup verification did not
read or compile manuscript pages.

## Private PDF font-map repair

An explicitly authorized later compilation of all manuscript pages exposed a
second missing generated TeX file: `pdftex.map`. Without it, the PDF backend used
the wrong built-in encoding for `lmsy10` and aborted while embedding the Latin
Modern math-symbol font. A private `pdftex.map` was assembled from the installed
Latin Modern, AMS/Computer Modern, and RSFS map files. The original map lines are
retained, with duplicate font entries omitted; no system files were changed.
`font_map_provenance.json` records the standard source maps and 777 entries.

The private map is at `texmf/fonts/map/pdftex/private/pdftex.map` and resolves
through the existing private `TEXMF` configuration. With this environment repair,
the complete combined document compiled successfully to a 40-page PDF. No
transcription source change was needed for the font-map issue.
