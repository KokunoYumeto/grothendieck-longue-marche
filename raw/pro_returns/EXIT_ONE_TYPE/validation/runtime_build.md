# Verified LuaLaTeX runtime

The existing LuaHBTeX executable is usable with the locally generated
`lualatex.fmt` and the local TDS dependency tree. A fontspec smoke document
successfully compiled on 13 November 2026 UTC as `font-smoke.pdf`.

The absolute `TEXMFCACHE` setting failed during luaotfload initialization
because TeX's existing `openout_any=p` policy rejects absolute output
filenames. The normal-TeX diagnostic logged `kpse.out_name_ok=false` and
`io.open=nil` for the absolute test filename, while a relative test file
opened successfully. Using the relative path `.` for both `TEXMFCACHE`
and `TEXMFVAR` resolves the failure within that existing restriction.
No permission settings were changed.

The next missing dependency was `lua-uni-case`; ten upstream Lua modules
from lua-uni-algos v0.5 were installed without modification under
`build/texmf/tex/luatex/lua-uni-algos`. Source archive:
https://ctan.math.illinois.edu/macros/luatex/generic/lua-uni-algos.zip

Verified command, run in the directory containing the input document:

```sh
env TEXMF='{/workspace/scratch/4b304a8756d2/build/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}' \
  TEXMFVAR=. TEXMFCACHE=. \
  TEXMFCONFIG=/workspace/scratch/4b304a8756d2/build/tex-runtime/config \
  luahbtex \
  --fmt=/workspace/scratch/4b304a8756d2/build/tex-runtime/lualatex.fmt \
  --progname=lualatex --interaction=nonstopmode --halt-on-error \
  font-smoke.tex
```

For the paper, run in `output/EXIT_ONE_TYPE` and substitute
`EXIT_ONE_TYPE_paper.tex`. The generated `luatex-cache` directory is a
build cache and should be excluded from the final deliverable archive.

## Vector mathematics fonts

The installed CM and AMS Type1 fonts were present, but the restricted
TEXMF tree above contained no default `pdftex.map`. Therefore TeX fell
back to bitmap font generation and failed on `msbm10`.

A local default map was assembled without changing any font entry:
`build/texmf/fonts/map/pdftex/exit-one-type/pdftex.map`. It contains the
156 distinct entries from the installed `cm.map`, `cmextra.map`,
`symbols.map`, `euler.map`, and `latxfont.map` files under
`/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/`.
The existing build command finds this local map automatically.

`ams-smoke.tex` compiled successfully with the same command.
`pdffonts ams-smoke.pdf` verified embedded Type1 MSBM10, CMSY10, CMMI10,
EUFM10, CMR7, CMR10, CMMI7, and CMEX10, together with embedded Latin
Modern OpenType text. No Type3 bitmap font remains in that test.
No mathematical source, main preamble, or permission setting was changed.

## Optional APA citation style, verified

Official CTAN apacite 6.03 was downloaded from
https://ctan.math.illinois.edu/biblio/bibtex/contrib/apacite.zip and
its supplied `apacite.ins` was run without modification. Generated
`.sty` and `.apc` files were installed under
`build/texmf/tex/latex/apacite`, and `.bst` files under
`build/texmf/bibtex/bst/apacite`.

The isolated `apa-smoke.tex` uses an unchanged copy of the complete
35-entry bibliography. LaTeX, BibTeX, LaTeX, LaTeX all returned zero;
the final log and BibTeX log contain no warnings or undefined references.
The rendered first page was inspected. The four-page PDF verifies
narrative and parenthetical theorem citations, the APA6 first/repeated
multiple-author behavior, and all35 bibliography entries.

The exact optional source switch is:

```tex
% Replace the separate natbib package line; do not load both separately.
\usepackage[natbibapa]{apacite}
% Load hyperref after this line.
...
\bibliographystyle{apacite}
```

This is APA6, as stated by CTAN, not APA7. Apacite prints both the
URL and DOI fields when both are present: the smoke bibliography has
32 URL blocks and26 DOI blocks. Therefore the assembler's mechanically
appended `DOI:` and `Source:` note suffixes would duplicate those fields.
The exact inspected preprint URL remains visible in the URL block.
Specific source-note URLs can be retained where they convey additional
information. Protect proper names in sentence-case titles with braces:
Hodge, Betti, Rham, Fano, and Seattle are examples in the current bib.
