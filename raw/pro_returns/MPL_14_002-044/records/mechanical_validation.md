# Mechanical LaTeX validation

Checked at 2026-11-15 00:19:11 UTC. This record concerns LaTeX structure and packaging syntax.
The primary transcriber retains responsibility for all manuscript readings and
visual auditing. No scan images or context archive were accessed during this
mechanical check.

## Structural checks

All 40 expected page files were present: scans 002–044, omitting 018, 023, and
043. Each file passed the utility's checks for its matching scan marker,
balanced braces, properly nested LaTeX environments, and the absence of document
preambles, image inclusion, or external input commands. Counts of `\(` / `\)`
and `\[` / `\]` matched on every page. These checks establish structural lint
results; the TeX engine did not reach document parsing, as recorded below.

No combined transcription was assembled and no hashes were frozen by this
check.

## Applied syntax repairs

The 19 `tikzcd` blocks in the table below now use
`\begin{tikzcd}[ampersand replacement=\&]`. Their 33 top-level cell separators
were changed from `&` to `\&`. These changes address TikZ's documented
category-code issue for a diagram captured as a macro argument, here the
required `\diagram{...}` wrapper. Array environments and separators nested in
groups or other environments were left intact. Reversing the recorded token
substitutions reproduced each original page file exactly.

| Scan | Diagram option additions | Cell separator replacements |
|---|---:|---:|
| 009 | 1 | 1 |
| 010 | 2 | 7 |
| 011 | 1 | 1 |
| 015 | 1 | 1 |
| 019 | 2 | 5 |
| 021 | 2 | 2 |
| 026 | 1 | 2 |
| 027 | 2 | 5 |
| 035 | 3 | 4 |
| 036 | 1 | 1 |
| 037 | 1 | 2 |
| 038 | 2 | 2 |

On scan 035, the second diagram's node options occurred after an initial
`\varphi:\,`. TikZ recognizes the `|[options]|` form at the start of a cell.
The cell was rewritten with the same formula tokens, keeping `\varphi:\,`
as a label outside the ellipse on its left:

```latex
|[draw,ellipse,label={left:$\varphi:\,$}]|A_Y^{\unsure{*|0}}(k)\arrow[r]\&A^i_{\mathrm{alb}}(X)
```

The rotation option on scan 037, `"\simeq" rotate=90`, follows the documented
quoted-label syntax and was retained. No reading, doubt mark, arrow direction,
formula, or manuscript wording was changed.

## Consumer dependencies and compilation limitation

The fragment requires consumer definitions for the requested diplomatic macros,
LaTeX mathematics support such as `amsmath` and `amssymb`, `tikz-cd`, and TikZ's
`shapes.geometric` library for the ellipse node shape. Underlining can be
implemented with `ulem`; its consumer definitions need to accommodate both text
and mathematics. The requested transcription remains a fragment without a
preamble.

A scratch compilation wrapper was created at
`/workspace/scratch/ff2fe622ef15/latex_syntax_qa/syntax_check.tex`. It provides
minimal macro definitions and inputs scratch snapshots of the page files. Its
state has been refreshed to include all 40 pages after the syntax repairs. The
wrapper is a syntax-check harness; its deletion, insertion, and doubt macros
pass through their arguments and do not implement a final diplomatic layout.

An attempted invocation was:

```sh
xelatex -interaction=nonstopmode -file-line-error -halt-on-error syntax_check.tex
```

The executable was available at `/usr/bin/xelatex`, but the process exited with
status 1 before reading the document because the TeX installation lacked an
accessible XeLaTeX format. Its final diagnostic was:

```text
I can't find the format file `xelatex.fmt'!
```

`kpsewhich` also returned no path for `tikz-cd.sty`, `amsmath.sty`,
`amssymb.sty`, `ulem.sty`, or `fontspec.sty`. Consequently, this check claims no
successful compilation or rendered output. The established result is the
structural validation and the documented syntax repairs above.

## Syntax documentation consulted

- [tikz-cd manual, §§1.2 and 3.4](https://tug.ctan.org/graphics/pgf/contrib/tikz-cd/tikz-cd-doc.pdf): quoted-label options and macro-argument ampersand handling.
- [PGF/TikZ matrix library, §59.1](https://tikz.dev/library-matrix): node options at the beginning of a cell.
- [PGF/TikZ shape library, §71.3](https://tikz.dev/library-shapes): the ellipse node shape in `shapes.geometric`.


## Read-only recheck after the second visual audit — 2026-11-15 00:40:51 UTC

After the primary transcriber reported completion of all 40 second visual
audits, the current fragments were checked again without changing any page
file. All 40 passed the scan/cote marker, brace, environment, prohibited-command,
and paired math-delimiter count checks. All 20 `tikzcd` blocks declare
`ampersand replacement=\&`; scanning their contents found no remaining raw
top-level cell separators.

Static inspection of the revised TikZ found no concrete syntax error requiring
a repair:

| Scan | Revised constructs inspected | Result |
|---|---|---|
| 031 | Alias `ay`, left node label, shifted anchor coordinates, end-of-picture ellipse and annotation | Balanced options and terminated paths; references use the declared alias. |
| 032 | Marginal path; inline ellipse node with baseline `(cycle.base)` | Balanced environments, label math delimiters, and terminated paths. |
| 035 | Cell-initial ellipse options and left label; inline ellipse node with baseline `(sy.base)` | Cell options remain at the beginning; label groups and paths are balanced. |
| 036 | Inline ellipse node with baseline `(target.base)` inside surrounding mathematics | Balanced math delimiters and picture environment; the node supplies its referenced baseline. |
| 038 | Alias `hyp`, end-of-picture annotation, quoted question-mark arrow label | Balanced option groups and terminated node command; the alias is declared in the diagram. |

The TikZ documentation defines baseline coordinates, node aliases, and the
end-of-picture hook used here. The `tikz-cd` implementation passes its diagram
options to the underlying `tikzpicture`, so the hook is supplied at the documented
picture-option location. This records a source-based syntax inspection; the
previously documented missing TeX format and packages still preclude a successful
compilation or rendering claim.

The updated `records/inventory_macro_audit.md` captures the separate inventory
comparison. It reports no page/category deficits. Its totals (macro occurrences
/ inventory rows) are deletion 155/155, insertion 74/74, margin note 36/37,
diagram 20/20, and drawing 11/12. Scan 031 contains one `\draw` command directly
inside its diagram and outside a figure macro; the corresponding drawing row is
therefore recorded separately from figure-macro counts. Annotation placement
within diagrams was retained. The inventory was being finalized, so these remain
snapshot counts.

Additional syntax references:

- [PGF/TikZ picture options](https://tikz.dev/tikz-scopes), §12.2: baseline coordinates and `execute at end picture`.
- [PGF/TikZ node options](https://tikz.dev/tikz-shapes), §17: `alias`.
- [tikz-cd maintained source](https://github.com/astoff/tikz-cd/blob/master/tikzlibrarycd.code.tex): `\tikzcd@` forwards diagram options to `\tikzpicture`.
