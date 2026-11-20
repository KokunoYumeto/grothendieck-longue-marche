# Final static recheck of pages 021–027 — reader C

## Outcome and scope

**The final page sources introduce one additional structural error: a second superscript after the supplied `\unsure` macro on page 027.** Root has approved the narrow grouping correction S1 described below. The previously identified page 024 Gamma font mapping remains covered by the separate F1 stage. Root's page 026 prime-positioning correction P1 is staged using the required literal apostrophe.

The drawn mark above `des` on page 025, the new alternatives on page 026, the dotless barred `j` on page 027, and the raised abbreviation letters on page 027 are otherwise structurally compatible with the supplied macros and packages. No additional command-availability or grouping/environment issue was identified in these seven final page fragments.

Snapshot: **2026-11-20T22:22:09.631410+00:00 through 2026-11-20T22:22:09.633969+00:00**. The sources were `edition/pages/145_scan021.tex` through `145_scan027.tex` and the supplied `source/SP75_C13_145_texts/PREAMBLE.tex`. Root's final page 027 ink decisions were treated as fixed. No images, OCR, first/second readings, or comparison files were consulted; no TeX compilation was performed. No page or accepted reading was edited.

The initial [final_static_review_c.md](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/reader_reports/final_static_review_c.md) remains unchanged. This supplementary report records the later final-page snapshot and root-requested corrections; the exact executable staging data is maintained separately in [staged_serialization_plan_c.json](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_plan_c.json).

## S1 — page 027, line 9: group an uncertain base before its additional superscript

The second cancellation-scope alternative currently contains:

```tex
\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}
```

The supplied preamble defines the math branch of `\unsure` as an argument group followed by `^{?}`. Appending another superscript immediately to that expansion therefore produces two superscripts on the same atom. In simplified expanded form, the problematic sequence is:

```tex
{\color{orange}\dot\rho|\rho}^{?}^{\deleted{\unsure{2}}}
```

The narrowly scoped serialization correction is:

```tex
{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}
```

The entire accepted uncertainty, with that correction, is:

```tex
\unsure{\deleted{\unsure{\dot\rho^2}}|{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}}
```

Only the uncertain base receives an additional grouping pair. The first alternative still cancels the whole uncertain dotted-rho-squared expression. The second alternative still leaves the uncertain rho base live and cancels its uncertain exponent 2. Both uncertainty levels remain. This is the grouping fix approved by root, not a new decision about either deletion scope.

The direct-macro scan found exactly one `\unsure{...}` immediately followed by an additional `^` or prime in the seven current page sources: this locus. No other such occurrence was found.

### Current-quotation synchronization handed off by reader A

Reader A and root assigned C the single current-report field `c_markup_audit.items[1].reading` on page 027. It still contains the stale quotation:

```tex
\deleted{\unsure{\dot\rho}}
```

The S1 stage explicitly synchronizes that field to the accepted full grouped rho expression above, matching current decision U027-02 and the accepted page. This is listed separately from the brace-only operations because its old quotation lacks the later accepted exponent and scope alternatives. The associated `source_span` remains untouched as the historical C quotation; every prior instruction payload and independent reading is preserved.

## P1 — page 026, line 2: literal prime convention

The current opening is:

```tex
en associant à $(g,(\unsure{\alpha^i|\alpha_i|\alpha\prime})_{i\in\{0,1,\infty\}})$ le système
```

Root requested correction of the prime's serialization and then specified the user convention: an existing prime is encoded as a literal apostrophe. The proposed opening is therefore:

```tex
en associant à $(g,(\unsure{\alpha^i|\alpha_i|\alpha'})_{i\in\{0,1,\infty\}})$ le système
```

The alternatives `\alpha^i`, `\alpha_i`, and alpha-prime all remain present. The correction introduces no new mark and resolves no uncertainty. It changes only `\alpha\prime` to `\alpha'` in the page and the explicitly listed current quotations, including the current notation entry. The command `\prime` itself exists; the defect is the absent superscript/prime syntax in this mathematical position, rather than an unavailable control sequence.

The other newly accepted page 026 alternatives remain well grouped: the cancelled initial wording, inverse-exponent alternatives, upper-mark alternatives including infinity, deleted preposition alternatives, and the accent alternatives on the final cancelled `u`. Their nested `\unsure`, `\deleted`, `\text`, and inline math uses do not create another display-in-strikeout or direct double-superscript case.

## F1 — page 024: confirmed font issue, updated short right return

The final audited page retains seven `\mathbb\Gamma` tokens. The initial review's local package evidence still applies: `\Gamma` is an alphabetic symbol at slot 00, whereas the AMSb alphabet selected by `\mathbb` uses that slot for `\lvertneqq`, not the accepted double-stroke Gamma.

The separate Gamma stage uses only existing preamble dependencies. Its nonzero coordinate scales and stroke width use `em`/`ex`, and it introduces no macro. Following root's explicit instruction about the already adjudicated shape, the outer upper arm now has the short return from `(.58,1.60)` to `(.58,1.40)`: a vertical extent of 0.20 ex. The left strokes span approximately 1.4–1.6 ex.

```tex
\mathord{\text{\begin{tikzpicture}[
  x=1em,y=1ex,baseline=0pt,
  line width=.045em,line cap=butt,line join=miter]
  \draw (.04,0)--(.04,1.60)--(.58,1.60)--(.58,1.40);
  \draw (.16,0)--(.16,1.40)--(.58,1.40);
\end{tikzpicture}}}
```

`\mathord` preserves ordinary math-atom behavior. The supplied amsmath `\text` wrapper selects the appropriate text-font size for the current math style, so the `em`/`ex` drawing dimensions respond to scripted use. The zero baseline value introduces no fixed glyph-size requirement. The newly audited undersets, the NB inside the lower TikZCD row, and the final word uncertainty remain outside the replacement token and are retained verbatim.

## Requested constructs requiring no further correction

### Page 025, lines 21–23: tiny drawn mark above `des`

The new construction is a mathematical `\overset` whose upper argument is `\text{\begin{tikzpicture}...\end{tikzpicture}}` and whose lower argument is `\text{des}`. The entire overset is within one inline math pair. `\overset` and `\text` are supplied by amsmath; TikZ is explicitly loaded. The graphic is consequently boxed in the text argument of a math construction, without a `\figure`/`\diagram` paragraph wrapper or an outer text-mode strikeout.

The path has a terminating semicolon, valid coordinate/control-point syntax, and balanced environment/group boundaries. The new graphic is not a missing command or illegal nested-dollar case. Its displayed scale and exact visual spacing have not been rendered.

### Page 027, line 7: dotless barred `j`

The current expression includes:

```tex
-\bar{\jmath}\}.
```

`\jmath` is a standard available math symbol. The installed [fontmath.ltx](sandbox:/usr/share/texlive/texmf-dist/tex/latex/base/fontmath.ltx), line 217, declares:

```tex
\DeclareMathSymbol{\jmath}{\mathord}{letters}{"7C}
```

`\bar{\jmath}` is therefore valid with the supplied setup and applies the bar to the dotless math-j glyph. The literal closing escaped brace after it is an accepted manuscript delimiter, not an unmatched TeX grouping brace. It is retained.

### Page 027, lines 9 and 11: raised abbreviation letters and a cancelled raised `s`

The two constructions are:

```tex
p\textsuperscript{ts}
p\textsuperscript{t\deleted{\unsure{s}}}
```

`\textsuperscript` is available from the LaTeX kernel. The installed [latex.ltx](sandbox:/usr/share/texlive/texmf-dist/tex/latex/base/latex.ltx), lines 16009–16012, defines it through an `\ensuremath` superscript containing an `\mbox` with the selected smaller text font:

```tex
\DeclareRobustCommand*\textsuperscript[1]{%
  \@textsuperscript{\selectfont#1}}
\def\@textsuperscript#1{%
  {\m@th\ensuremath{^{\mbox{\fontsize\sf@size\sf@size#1}}}}}
```

The abbreviation letters are inside that text box. Accordingly, the supplied `\deleted` selects its text branch and applies `\sout` only to the uncertain `s`; the `t` remains live. The inner `\unsure` also runs in text mode, so its question marker is produced through a separate text-superscript box. This nesting is structurally valid and does not create the direct math-atom double superscript identified in S1.

### Page 021: newly encountered equivalence command

The `\equiv` in relation (15) is available from base math definitions. The same [fontmath.ltx](sandbox:/usr/share/texlive/texmf-dist/tex/latex/base/fontmath.ltx), line 345, declares `\equiv` as a relation in the symbols font at slot 11. It requires no new package.

## Structural check results

| Page | Display openings / closings | Left / right pairs | Group/environment findings |
|---|---:|---:|---|
| 145_scan021.tex | 5 / 5 | 4 / 4 | Balanced |
| 145_scan022.tex | 5 / 5 | 2 / 2 | Balanced |
| 145_scan023.tex | 1 / 1 | 1 / 1 | Balanced |
| 145_scan024.tex | 5 / 5 | 1 / 1 | Balanced |
| 145_scan025.tex | 7 / 7 | 1 / 1 | Balanced |
| 145_scan026.tex | 2 / 2 | 0 / 0 | Balanced |
| 145_scan027.tex | 1 / 1 | 0 / 0 | Balanced |

The actual control-token scan distinguishes a row-spacing option such as `\\[2ex]` from a display opening. Literal grouping braces and environment names match in all seven fragments. All 26 display pairs and all nine left/right pairs match. No display, margin, figure, or diagram command was found inside a new `\deleted` or `\inserted` argument. The page 023 figure and the pages 023/024 diagram wrappers remain outside math.

The only page command names newly encountered relative to the original complete review were `\equiv` and `\jmath`; their installed definitions are cited above. Ordinary written parentheses, separators, indices, word choices, and cancellation alternatives were not normalized.

These are static source findings. They do not certify rendered margins, page breaks, line width, graphic placement, or the visual appearance of nested strikeouts. No optional compilation or image rereading was performed.

## Snapshot hashes

| Source | Bytes | SHA-256 |
|---|---:|---|
| 145_scan021.tex | 3336 | `a1263cc8f4f15b4746736f2d1a239e7edfa20da74496c4794b232e6b79c0a1b8` |
| 145_scan022.tex | 3088 | `fa497256e0b8b80061e3d28773d8848fad9ff80072b14dcc8c64a52e2ef9a105` |
| 145_scan023.tex | 1969 | `ece030772e561b0dcbd55a59590df9286f4a78ae9423e07deb85ab05ace4ed9e` |
| 145_scan024.tex | 2049 | `6c3df672a4036dd92bb200d68332b7b21720bc0693bb20739dde34bbb4fa4ae8` |
| 145_scan025.tex | 3758 | `c67f85179618c5f98d2419945dffc66c588d8e2c383219cccf85756ed066ceef` |
| 145_scan026.tex | 1311 | `6274529774467672879b1fa78b398733ce2b8987fcbcac44791f63e6e5ff4175` |
| 145_scan027.tex | 2241 | `6005f8f6ab5c5b4495c0b8d256f4783535b4dba504d64a5be87998a61206a8a6` |
| PREAMBLE.tex | 1607 | `aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf` |

Root's completed page 027 adjudication had SHA-256 `8f778d391e72405d990565cc01e471aac413de0a4ef451bad144fdd8e3a254c5`, and its `main_reader_viewed_all_differing_crops` value was true.

### Local definition evidence

Checked at 2026-11-20T22:29:34.635097+00:00.

| Source | SHA-256 |
|---|---|
| /usr/share/texlive/texmf-dist/tex/latex/base/fontmath.ltx | `d7368515628e9e6e4ede13eb985e6ad3dccab6976c023a1bef45e60acf0dc4cc` |
| /usr/share/texlive/texmf-dist/tex/latex/base/latex.ltx | `8420904f06764a8cc2ec81e13215c22fec8e599c269160dcc02ad84507851f32` |

## Disposition

The final recheck of 021–027 is complete. F1, P1, and S1 are staged serialization changes; the original D1–D9/I1 page operations remain as approved by root. D7 moves the margin command outside the outer `\sout` while retaining the note's cancellation through `\margin{\deleted{...}}`; it does not make the margin note live.

The separate P1 release can now be opened against the pinned completed page 027 audit. Root will review the final script and exact-field plan before applying any stage. All first/second readings, comparisons, initial reports, and historical instruction payloads remain unchanged.
