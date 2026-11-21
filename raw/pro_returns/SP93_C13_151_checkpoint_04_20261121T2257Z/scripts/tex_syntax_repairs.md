# Static TeX syntax repair proposals: scans 018 and 020

These proposals preserve the source readings. They do not modify the committed report TeX, JSON, first-reading TSVs, final pages, or commits. No TeX compilation was run.

## Scan 018: one global handwritten cancellation

The preamble defines `\deleted` using `\sout`, so its argument cannot contain the existing paragraph breaks, display mathematics, `\figure`, `\diagram`, or floating `\margin` calls. The proposal removes that **one outer wrapper only** and retains its entire body in one saved minipage. It draws the source's two long crossing courses over the saved block. The opposing course has the visible short pen gap. These are global cancellation strokes; no new local deletion is applied to a word, formula, or diagram.

The original scan 018 was viewed only for the global X's extent and shape. No new reading or crop was made. The strokes use normalized coordinates relative to the saved block, so their geometry is an approximation over typeset content rather than a letter-by-letter facsimile. All existing text, formula, enclosure, and diagram tokens are retained. The printed heading, initial sketch, outer `p>=`/278 notes, and final foliation 17 remain outside the replaced block.

The exact replacement is the former argument of `\deleted{...}`, with the following opening and closing code:

### New opening

```tex
% Global cancellation is the manuscript's X, not a linewise sout.
\begingroup
\newsavebox{\SPXCIIICancelledXVIII}
\begin{lrbox}{\SPXCIIICancelledXVIII}
\begin{minipage}{\linewidth}
```

### New closing

```tex

\end{minipage}
\end{lrbox}
\begin{center}
\begin{tikzpicture}
\node[anchor=south west,inner sep=0pt,outer sep=0pt] (spCancelledXVIII) at (0,0)
  {\usebox{\SPXCIIICancelledXVIII}};
% The unit vectors are the saved block's width and height.
\begin{scope}[x={(spCancelledXVIII.south east)},y={(spCancelledXVIII.north west)}]
% Descending course: upper left to lower right.
\draw[line width=.45pt] (.09,1.035)
 .. controls (.14,.96) and (.17,.84) .. (.26,.70)
 .. controls (.42,.49) and (.68,.15) .. (.81,.01);
% Opposing course, with the source's short upper pen gap.
\draw[line width=.45pt] (.50,1.00)
 .. controls (.50,.96) and (.44,.87) .. (.42,.835);
\draw[line width=.45pt] (.41,.812)
 .. controls (.36,.65) and (.21,.28) .. (.15,.13)
 .. controls (.145,.10) and (.14,.09) .. (.13,.08);
\end{scope}
\end{tikzpicture}
\end{center}
\endgroup
```

### Internal margin calls

A floating `\marginpar` is not placed inside the minipage. The two internal `\margin` calls are replaced at their existing source-order call sites by nonfloating text boxes. Their mathematical and textual content is identical. The first is a left overhang and the second is right aligned. The `\smash` only suppresses their layout height; it does not suppress their visible ink.

First old call:

```tex
\margin{$\alpha\unsure{-|\longrightarrow}F$\\$\beta\unsure{-|\longrightarrow}G$}
```

Exact replacement:

```tex
\par\noindent
\makebox[0pt][r]{%
  \smash{\begin{tabular}[t]{@{}l@{}}
  $\alpha\unsure{-|\longrightarrow}F$\\$\beta\unsure{-|\longrightarrow}G$
  \end{tabular}}\hspace{.75em}%
}\par
```

Second old call:

```tex
\margin{$u$ continu\\$v$ cocontinu}
```

Exact replacement:

```tex
\par\noindent
\makebox[\linewidth][r]{%
  \smash{\begin{tabular}[t]{@{}l@{}}
  $u$ continu\\$v$ cocontinu
  \end{tabular}}%
}\par
```

The body is typeset into the savebox before the outer TikZ picture is opened. The original inner figures are therefore already boxed when the global cancellation overlay is drawn.

## Scan 020: two block wrappers and two superscript groups

### First cancelled point drawing

Replace the structural shell

```tex
\deleted{\figure{<unchanged tikzpicture>}}
```

with

```tex
\figure{<unchanged tikzpicture>}
```

The inner picture already contains the heavy zigzag cancellation paths. The complete inner figure substring, including every path and point, is retained verbatim. Removing the outer `\deleted` prevents a block paragraph from entering `\sout`; the source cancellation remains drawn.

### Drawing whose deletion is doubtful

Replace the structural shell

```tex
\unsure{\deleted{\figure{<unchanged tikzpicture>}}}
```

with

```tex
\figure{\unsure{\deleted{\mbox{<unchanged tikzpicture>}}}}
```

Here the block-level `\figure` is outside the wrappers. `\deleted` receives one unbreakable inline `\mbox`, and the existing `\unsure` still marks the deletion state as uncertain. The TikZ picture substring is retained verbatim, including its existing strokes and points. No additional source letter, symbol, or local cancellation is inferred.

### Starred doubtful bases

The math-mode definition of `\unsure` appends `^{?}`. An immediately following `^*` on the same nucleus would be a second superscript. The exact two replacements are:

```tex
\unsure{\delta|\partial}_1^*
\unsure{\delta|\partial}_2^*
```

becoming:

```tex
{\unsure{\delta|\partial}}_1^*
{\unsure{\delta|\partial}}_2^*
```

Only an outer grouping pair is added around each uncertain base. Both alternative glyphs, the subscripts 1/2, and the stars are unchanged.

## Static verification

- Brace, dollar-delimiter, and environment counts balance in both proposals.
- No remaining `\deleted` argument contains block `\figure`, `\diagram`, `\margin`, display math, or paragraph breaks.
- The saved scan 018 minipage contains no floating `\margin`/`\marginpar` call; both note texts survive exactly.
- Reversing the listed scan 020 replacements reproduces its original report TeX exactly.
- Reversing scan 018's two internal margin replacements reproduces the original outer deletion's entire argument exactly; the prefix and suffix outside that argument are unchanged.
- Original report files were checked unchanged after writing the proposals.
- No compiler, renderer, OCR, or outside research was used.

## Files

- `reports/151_scan018.syntax.tex`
- `reports/151_scan020.syntax.tex`
- `scripts/tex_syntax_repairs.md`

## Root application

Root reviewed the proposals, rechecked the global cancellation against original018, and applied them to the report TeX and final pages with `--preserve-first`. The final-reading snippets of the affected020 change records were synchronized. The frozen first/box TSVs remain unchanged. No compilation was performed.
