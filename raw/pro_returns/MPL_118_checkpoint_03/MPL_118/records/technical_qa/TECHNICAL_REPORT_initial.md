# MPL_118 technical LaTeX QA

Scope: technical syntax of the 38 saved page fragments only. No scan image or
context source was opened for this check, and no page fragment was modified.
The primary reader retains all decisions about readings and geometry.

## Static checks

The current machine-readable snapshot is `static_report.json`; it records the
UTC check time and SHA-256 of every page inspected. The checks are reproducible
with `python3 MPL_118/records/technical_qa/static_checks.py` from the workspace.

| Check | Result at this report |
| --- | --- |
| Page fragments found | 38 |
| Unescaped brace balance | No imbalance found |
| Begin/end environment nesting | No mismatch found |
| Unescaped dollar parity | Even on every page |
| Display/inline command delimiters | Balanced |
| Left/right delimiters and enclosing brace depth | Balanced |
| Unknown custom command candidates | None outside the permitted diplomatic macros and the reviewed standard/package command list |
| TikZ-CD matrices inspected | 86 |
| TikZ-CD arrows inspected | 429 |
| Arrow endpoints outside matrix bounds | One remaining occurrence, scan 034 below |

The command whitelist is a syntax aid, not a substitute for TeX compilation.
The checks do not decide whether an arrow points to the object shown in the
manuscript, or whether a label is correctly read. They also do not certify the
layout or renderability of arbitrary macro definitions.

## Actionable remaining error

`pages/MPL_118_118_scan034.tex`, line 21, contains:

```tex
\margin{\diagram{\begin{tikzcd}(iii)\arrow[u,Rightarrow]\\{}\end{tikzcd}}}
```

The arrow starts at row 1, column 1 and targets row 0, column 1 in a two-row,
one-column matrix. A syntactically valid upward arrow from the lower blank
cell to the upper `(iii)` would be:

```tex
\margin{\diagram{\begin{tikzcd}(iii)\\{}\arrow[u,Rightarrow]\end{tikzcd}}}
```

If the ink instead shows an arrow rising from `(iii)` toward a blank space,
put the blank row above `(iii)` and retain the arrow on its source cell. The
primary reader must choose by the scan; this report makes no reading decision.

## Earlier finding already resolved by the primary reader

An initial look found `F\cap S\arrow[ddll]` at scan 005, line 41, targeting
column zero. The primary reader reported checking the scan and removing that
redundant direct arrow and its symmetric counterpart because the same paths
were already represented by two segments. The static snapshot has no
remaining off-grid arrow on scan 005. The support agent made no page edit.

## Compilation limitation

The `pdflatex`, `lualatex`, and `xelatex` engine binaries exist, but the runtime
cannot locate the LaTeX formats or package tree. In particular, `kpsewhich`
failed to locate `article.cls`, `latex.ltx`, `pdflatex.fmt`, `lualatex.fmt`,
`tikz-cd.sty`, `tikz.sty`, `amsmath.sty`, `amssymb.sty`, `ulem.sty`, and
`cmr10.tfm`. Full lookup evidence is in `runtime_manifest.json`.

An actual `pdflatex -no-mktex=fmt` attempt stopped before reading the document:

```text
I can't find the format file `pdflatex.fmt'!
```

The command, exit status, and output are saved in `compile_attempt.txt`.
No packages were installed and no network access was used. Therefore **no
successful compile or visual layout verification is claimed**.

`validation_wrapper.tex` is a diagnostic wrapper only, outside `pages/`.
Its long, neutral pass-through definitions accept multi-paragraph deletion,
insertion, and margin arguments without switching math/text mode. It is not a
publication style or a deliverable transcription. Since format loading failed,
neither its macro-rendering choices nor TikZ ampersand handling could be tested.

## Final rerun

After the primary reader completes all page corrections, rerun the static
script and retain its new per-page hashes. This technical snapshot is separate
from the primary reader's required final visual audit and freeze hashes.
