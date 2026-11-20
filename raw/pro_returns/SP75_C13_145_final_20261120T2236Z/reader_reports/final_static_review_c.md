# Final static LaTeX compatibility review — reader C

## Scope and snapshot

Read-only review of the 24 page fragments under `/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/pages/` and `/workspace/scratch/937907bd75d7/SP75_C13_145_work/source/SP75_C13_145_texts/PREAMBLE.tex`. The page snapshot was acquired on **2026-11-20 from 21:56:25.866954 through 21:56:25.929651 UTC**. All line references and exact old-code blocks below refer to that snapshot. The last hash-only check was **2026-11-20T22:05:34.968362+00:00**.

No page, preamble, first reading, second reading, witness, or image was changed. No compilation, OCR, image rereading, or external research was performed. The four installed LaTeX package files cited in the font section were read only to answer the subsequent font-mapping question. This report is the only file written by this review.

**Result:** nine replacement loci contain cancelled display material serialized through the text branch of `\deleted`; these include fourteen display passages, one margin command, and one inline TikZ picture needing explicit boxing. A tenth replacement moves insertion brackets into a live display. These ten proposed replacements affect pages 012, 013, 014, 015, 018, and 019. A separate, material font-mapping defect affects the seven `\mathbb\Gamma` occurrences on page 024. No changes have been applied.

## Supplied macro behavior

The relevant definitions are at lines 18 and 22–27 of [PREAMBLE.tex](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/source/SP75_C13_145_texts/PREAMBLE.tex):

```tex
\newcommand{\unsure}[1]{\ifmmode{\color{orange}#1}^{?}\else{\color{orange}#1}\textsuperscript{?}\fi}
\newcommand{\deleted}[1]{\ifmmode\text{\sout{$#1$}}\else\sout{#1}\fi}
\newcommand{\inserted}[1]{\ifmmode\langle#1\rangle\else$\langle$#1$\rangle$\fi}
\newcommand{\margin}[1]{\marginpar{\footnotesize #1}}
\newcommand{\diagram}[1]{\par\begin{center}#1\end{center}\par}
\renewcommand{\figure}[1]{\par\begin{center}#1\end{center}\par}
```

When `\deleted` is called from prose, the entire argument is passed to `\sout`. A display boundary or `\marginpar` inside that text strikeout is a concrete structural risk. The narrow repair is to place the display or margin outside the text strikeout and retain the cancellation on every affected constituent. Inside a display, `\deleted` selects its math branch. Because that branch opens its own inline math within `\text`, the replacements include `\displaystyle` for formulas originally displayed.

An `aligned` environment must retain its alignment structure outside the per-cell strikeouts. Its mathematical cells, including each equals sign, retain their inherited cancellation. The proposals do not move alignment tabs into a boxed math argument.

The scope of cancellation is preserved from the supplied fragment: formerly cancelled prose remains cancelled; formerly cancelled formulas remain cancelled; existing nested `\deleted`, `\inserted`, and `\unsure` wrappers remain in the same semantic scope. The separate live insertion in I1 remains live. Existing insertion wrappers inside an already cancelled outer block are retained literally; the static review does not re-adjudicate the historical order of those nested revisions. No independent live insertion is newly struck.

## Exact serialization replacements

The following blocks are proposals for root to apply, not edits made by this review. Replace each exact old block once. D9 is a substring replacement within two longer prose lines; its live prefix and suffix must remain outside the replacement.

### D1 — 145_scan013.tex, snapshot lines 22–25

**Issue.** A display delimiter is inside the text-mode argument of deleted.

**Current code**

```tex
\deleted{\[
\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty
=l_0\sigma_\infty l_0\sigma_\infty^{-1}=l_0\sigma_\infty(l_0)
\]}
```

**Proposed serialization**

```tex
\[
\deleted{\displaystyle
\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty
=l_0\sigma_\infty l_0\sigma_\infty^{-1}=l_0\sigma_\infty(l_0)
}
\]
```

**Scope check.** The formula body, including any inner deletion or uncertainty, is unchanged. Displaystyle restores the display's intended math style inside deleted's boxed inline-math implementation.

### D2 — 145_scan013.tex, snapshot lines 45–47

**Issue.** A display delimiter is inside the text-mode argument of deleted.

**Current code**

```tex
\deleted{\[
l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1
\]}
```

**Proposed serialization**

```tex
\[
\deleted{\displaystyle
l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1
}
\]
```

**Scope check.** The formula body, including any inner deletion or uncertainty, is unchanged. Displaystyle restores the display's intended math style inside deleted's boxed inline-math implementation.

### D3 — 145_scan013.tex, snapshot lines 49–51

**Issue.** A display delimiter is inside the text-mode argument of deleted.

**Current code**

```tex
\deleted{\[
\deleted{\unsure{l_\infty^{-1}l_1|l_\infty^{-1}l_\infty|l_0^{-1}l_1}}l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1
\]}
```

**Proposed serialization**

```tex
\[
\deleted{\displaystyle
\deleted{\unsure{l_\infty^{-1}l_1|l_\infty^{-1}l_\infty|l_0^{-1}l_1}}l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1
}
\]
```

**Scope check.** The formula body, including any inner deletion or uncertainty, is unchanged. Displaystyle restores the display's intended math style inside deleted's boxed inline-math implementation.

### D4 — 145_scan013.tex, snapshot lines 56–58

**Issue.** A display delimiter is inside the text-mode argument of deleted.

**Current code**

```tex
\deleted{\[
l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}
\]}
```

**Proposed serialization**

```tex
\[
\deleted{\displaystyle
l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}
}
\]
```

**Scope check.** The formula body, including any inner deletion or uncertainty, is unchanged. Displaystyle restores the display's intended math style inside deleted's boxed inline-math implementation.

### D5 — 145_scan019.tex, snapshot lines 32–34

**Issue.** A display delimiter is inside the text-mode argument of deleted.

**Current code**

```tex
\deleted{\[
\varepsilon_0\varepsilon_1=l_0\sigma_1l_1
\]}
```

**Proposed serialization**

```tex
\[
\deleted{\displaystyle
\varepsilon_0\varepsilon_1=l_0\sigma_1l_1
}
\]
```

**Scope check.** The formula body, including any inner deletion or uncertainty, is unchanged. Displaystyle restores the display's intended math style inside deleted's boxed inline-math implementation.

### D6 — 145_scan012.tex, snapshot lines 7–15

**Issue.** The text-mode strikeout contains two displays.

**Current code**

```tex
\deleted{\unsure{Appliquant|Appliquons} la relation fondamentale
\[
u\unsure{g|\rho}=\operatorname{int}(g)\rho u
\]
à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$
\[
u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})
\]
et ceci détermine déjà \deleted{\unsure{$\operatorname{int}(g)$}} \unsure{$g$|\deleted{$g$}} modulo multiplication à droite par un élt de $L_1$, \unsure{par|près|puis} le donnée de $u$}
```

**Proposed serialization**

```tex
\deleted{\unsure{Appliquant|Appliquons} la relation fondamentale}
\[
\deleted{\displaystyle u\unsure{g|\rho}=\operatorname{int}(g)\rho u}
\]
\deleted{à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$}
\[
\deleted{\displaystyle u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})}
\]
\deleted{et ceci détermine déjà \deleted{\unsure{$\operatorname{int}(g)$}} \unsure{$g$|\deleted{$g$}} modulo multiplication à droite par un élt de $L_1$, \unsure{par|près|puis} le donnée de $u$}
```

**Scope check.** Each original prose segment remains cancelled; the two display bodies receive the inherited outer cancellation. Existing inner deleted/unsure wrappers are retained verbatim.

### D7 — 145_scan015.tex, snapshot lines 2–26

**Issue.** A mixed strikeout contains five displays and a margin command.

**Current code**

```tex
\deleted{d'ordre fini dans le groupe envisagé \inserted{\deleted{\unsure{stable|stables}} fixé par $\rho$}, il faudrait donc avoir
\[
\varepsilon_0\varepsilon_1\varepsilon_\infty=1
\]
i.e. en termes des $l_i,\sigma_i$
\[
\unsure{l_1|l_1'}\underbrace{\sigma_0l_0}_{\substack{\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}\\\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}}}l_\infty\underbrace{\sigma_1l_1}_{l_\infty^{-1}l_0^{-1}}l_0\underbrace{\sigma_\infty l_\infty}_{l_0^{-1}l_1^{-1}}=1
\]
\margin{i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$\quad OK}
On a donc
\[
\boxed{\varepsilon_0\varepsilon_1\varepsilon_\infty=1}
\]
on peut en tirer de plus jolies expressions pour les $\sigma_i$
\[
\begin{aligned}
\sigma_0&=\varepsilon_\infty^{-1}\varepsilon_1\\
\sigma_1&=\varepsilon_0^{-1}\varepsilon_\infty\\
\sigma_\infty&=\varepsilon_1^{-1}\varepsilon_0
\end{aligned}
\]
donc \unsure{aussi|on a} la relation inattendue
\[
\sigma_\infty\sigma_1\sigma_0=1
\]}
```

**Proposed serialization**

```tex
\deleted{d'ordre fini dans le groupe envisagé \inserted{\deleted{\unsure{stable|stables}} fixé par $\rho$}, il faudrait donc avoir}
\[
\deleted{\displaystyle \varepsilon_0\varepsilon_1\varepsilon_\infty=1}
\]
\deleted{i.e. en termes des $l_i,\sigma_i$}
\[
\deleted{\displaystyle \unsure{l_1|l_1'}\underbrace{\sigma_0l_0}_{\substack{\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}\\\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}}}l_\infty\underbrace{\sigma_1l_1}_{l_\infty^{-1}l_0^{-1}}l_0\underbrace{\sigma_\infty l_\infty}_{l_0^{-1}l_1^{-1}}=1}
\]
\margin{\deleted{i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$\quad OK}}
\deleted{On a donc}
\[
\deleted{\displaystyle \boxed{\varepsilon_0\varepsilon_1\varepsilon_\infty=1}}
\]
\deleted{on peut en tirer de plus jolies expressions pour les $\sigma_i$}
\[
\begin{aligned}
\deleted{\displaystyle \sigma_0}&\deleted{\displaystyle =\varepsilon_\infty^{-1}\varepsilon_1}\\
\deleted{\displaystyle \sigma_1}&\deleted{\displaystyle =\varepsilon_0^{-1}\varepsilon_\infty}\\
\deleted{\displaystyle \sigma_\infty}&\deleted{\displaystyle =\varepsilon_1^{-1}\varepsilon_0}
\end{aligned}
\]
\deleted{donc \unsure{aussi|on a} la relation inattendue}
\[
\deleted{\displaystyle \sigma_\infty\sigma_1\sigma_0=1}
\]
```

**Scope check.** The margin command is lifted out of sout; its text retains the cancellation inherited from the old outer wrapper. The aligned environment stays outside deleted, with both sides of every row, including each equals sign, cancelled. The existing inserted/deleted nest in the first prose segment and the underbrace annotation is unchanged. No cancellation is added to an independently live insertion outside this original outer scope.

### D8 — 145_scan018.tex, snapshot lines 11–17

**Issue.** The margin strikeout wraps an aligned display.

**Current code**

```tex
\deleted{\[
\begin{aligned}
l_0&=(\sigma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\sigma_0\rho^{-1}|\rho\sigma_0\rho^{-1}})\\
l_1&=(\sigma_1\rho)^2\unsure{\sigma_1}\qquad&\unsure{l_0}&=\unsure{\rho^{-1}\sigma_0}\\
l_\infty&=(\sigma_\infty\rho)^2\unsure{\sigma_\infty}
\end{aligned}
\]}
```

**Proposed serialization**

```tex
\[
\begin{aligned}
\deleted{\displaystyle l_0}&\deleted{\displaystyle =(\sigma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\sigma_0\rho^{-1}|\rho\sigma_0\rho^{-1}})}\\
\deleted{\displaystyle l_1}&\deleted{\displaystyle =(\sigma_1\rho)^2\unsure{\sigma_1}\qquad}&\deleted{\displaystyle \unsure{l_0}}&\deleted{\displaystyle =\unsure{\rho^{-1}\sigma_0}}\\
\deleted{\displaystyle l_\infty}&\deleted{\displaystyle =(\sigma_\infty\rho)^2\unsure{\sigma_\infty}}
\end{aligned}
\]
```

**Scope check.** The two alignment pairs on the middle row remain two pairs. All original mathematical material is still cancelled. The enclosing margin is unchanged.

### D9 — 145_scan018.tex, snapshot lines 51–66

**Issue.** A mixed outer strikeout contains another deleted display; its inline TikZ environment also needs an indivisible box for text strikeout.

**Current code**

```tex
\deleted{on voit par contre (utilisant le fait que $l_0,l_1,l_\infty$ avec \begin{tikzpicture}[baseline=(relation.base)]
\node[inner sep=0pt,outer sep=0pt] (relation) {la relation};
\draw ([xshift=0.05em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.77em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=1.49em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.21em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.93em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.40em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.12em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.84em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=2.56em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\end{tikzpicture} fondamentale (1) est une présentation de $\unsure{\Pi|\pi}$, que \deleted{$\rho$} \inserted{$(\sigma_0\sigma_1)^3$ (p.ex)} doit s'exprimer en fonction des $l_i$; \unsure{puisque} en outre
\deleted{\[
\rho=l_0l_1l_\infty
\]}
des \unsure{relations|rel.} $\sigma_i^2=1$}
```

**Proposed serialization**

```tex
\deleted{on voit par contre (utilisant le fait que $l_0,l_1,l_\infty$ avec \mbox{\begin{tikzpicture}[baseline=(relation.base)]
\node[inner sep=0pt,outer sep=0pt] (relation) {la relation};
\draw ([xshift=0.05em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.77em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=1.49em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.21em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.93em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.40em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.12em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.84em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=2.56em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\end{tikzpicture}} fondamentale (1) est une présentation de $\unsure{\Pi|\pi}$, que \deleted{$\rho$} \inserted{$(\sigma_0\sigma_1)^3$ (p.ex)} doit s'exprimer en fonction des $l_i$; \unsure{puisque} en outre}
\[
\deleted{\displaystyle\deleted{\rho=l_0l_1l_\infty}}
\]
\deleted{des \unsure{relations|rel.} $\sigma_i^2=1$}
```

**Scope check.** Replace only this outer deleted call, leaving the live prefix/suffix on lines 51 and 66 untouched. Both existing deletion layers on rho=l_0l_1l_infinity are preserved. Mbox groups the unchanged inline TikZ picture as one object for sout; no node text, path, or coordinate is changed. The inserted live text already nested in the old cancelled prose remains in the identical nested wrapper; this is not a new independent deletion of that insertion.

### I1 — 145_scan014.tex, snapshot lines 35–37

**Issue.** The text-mode insertion prints its angle markers outside the display rather than around its formula.

**Current code**

```tex
\inserted{\[
\sigma_0\sigma_1=l_1^{-1}\rho
\]}
```

**Proposed serialization**

```tex
\[
\inserted{\sigma_0\sigma_1=l_1^{-1}\rho}
\]
```

**Scope check.** This is a placement repair, not a newly added cancellation. The formula remains inserted and live. The old code is not the same hard display-in-sout failure; it puts separate inline angle runs before and after the display.

### Payload and scope validation

All ten old/new pairs were checked as TeX-like token streams after removing only the moved serialization wrappers (`\deleted`, `\inserted`, `\mbox`) and the added `\displaystyle`. Every remaining text, mathematical, punctuation, environment, and TikZ-coordinate token is unchanged. This token check was supplemented by the explicit scope review above; token equality by itself would not establish cancellation scope.

| Replacement | Payload tokens before / after | Result |
|---|---:|---|
| D1 | 50 / 50 | Unchanged |
| D2 | 80 / 80 | Unchanged |
| D3 | 65 / 65 | Unchanged |
| D4 | 89 / 89 | Unchanged |
| D5 | 18 / 18 | Unchanged |
| D6 | 260 / 260 | Unchanged |
| D7 | 468 / 468 | Unchanged |
| D8 | 134 / 134 | Unchanged |
| D9 | 905 / 905 | Unchanged |
| I1 | 18 / 18 | Unchanged |

In D7, the margin already lay inside the original outer deletion. Its explicit `\deleted` after extraction preserves that inherited cancellation. In D9, both original deletion layers around the rho formula remain present; the inline TikZ picture is boxed without changing its node text, paths, or coordinates. I1 receives no deletion wrapper.

## F1 — the double-stroke Gamma font mapping

### Concrete defect and local evidence

`\mathbb\Gamma` is syntactically defined under the supplied packages, but it does **not** select a supported double-stroke Gamma. In the standard LaTeX/AMS math setup used by this preamble, `\Gamma` is an alphabetic math symbol at slot hexadecimal 00. `\mathbb` switches the alphabet to AMSb, whose slot 00 is the unrelated relation glyph named `\lvertneqq`. The defect is therefore an unintended font-slot selection, rather than an undefined command or a missing closing delimiter.

The installed definitions are:

| Local source | Lines | Definition |
|---|---:|---|
| [fontmath.ltx](sandbox:/usr/share/texlive/texmf-dist/tex/latex/base/fontmath.ltx) | 204 | `\DeclareMathSymbol{\Gamma}{\mathalpha}{operators}{"00}` |
| [amsfonts.sty](sandbox:/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty) | 60 | `\DeclareSymbolFont{AMSb}{U}{msb}{m}{n}` |
| [amsfonts.sty](sandbox:/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty) | 107–109 | `\DeclareSymbolFontAlphabet{\mathbb}{AMSb}` |
| [amssymb.sty](sandbox:/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty) | 171 | `\DeclareMathSymbol{\lvertneqq}{\mathrel}{AMSb}{"00}` |

Adding braces, as in `\mathbb{\Gamma}`, does not repair this mapping. The supplied preamble does not load a separate double-stroke Greek alphabet. No claim about the manuscript glyph has been inferred from expected mathematics: the following proposal serializes the already accepted double-stroke Gamma appearance.

### Exact affected occurrences

| Page fragment | Snapshot line | Occurrences on line |
|---|---:|---:|
| 145_scan024.tex | 2 | 2 |
| 145_scan024.tex | 5 | 2 |
| 145_scan024.tex | 6 | 1 |
| 145_scan024.tex | 13 | 1 |
| 145_scan024.tex | 15 | 1 |

The seven occurrences above are the complete set in the reviewed snapshot. In particular, the second occurrence on line 5 is one alternative inside `\unsure`; its surrounding uncertainty must remain intact.

### Inline replacement with existing packages

Replace only the token sequence below at each occurrence; retain every surrounding group, uncertainty, subscript, superscript, and diagram cell.

**Current code**

```tex
\mathbb\Gamma
```

**Proposed inline serialization**

```tex
\mathord{\text{\begin{tikzpicture}[
  x=1em,y=1ex,baseline=0pt,
  line width=.045em,line cap=butt,line join=miter]
  \draw (.04,0)--(.04,1.60)--(.58,1.60);
  \draw (.16,0)--(.16,1.40)--(.58,1.40);
\end{tikzpicture}}}
```

This uses only standard math grouping, the supplied `\text` command, and the already loaded TikZ package. It introduces no macro and requires no preamble edit. The two paths draw the two vertical strokes and their upper arms explicitly. `\mathord` preserves ordinary math-atom behavior, so surrounding products, indices, and superscripts continue to attach normally.

The `\text` wrapper makes the dimensions reasonably responsive to math style. In the installed [amstext.sty](sandbox:/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty), lines 31–41 select the normal, script, or scriptscript text-font size through `\mathchoice` and `\textdef@`. The drawing uses `em` and `ex` dimensions, including its stroke width, so it scales within that selected font size. This also avoids a fixed-size graphic in scripted occurrences. The supplied snapshot has no scripted `\mathbb\Gamma` occurrence; the proposal nevertheless handles that use without adding a new command.

The geometry is a typographic serialization of the accepted double-stroke capital, not a fresh ink adjudication. Its exact printed spacing and stroke weight have not been rendered or compiled. The literal linework can be adjusted by root for typography while retaining the same accepted two-stroke Gamma and ordinary math-atom wrapper.

## Other static checks

- The 24 page fragments have balanced literal grouping braces and matched `\begin`/`\end` environment names. There are 70 begin/end pairs.
- Actual display tokens are balanced: 134 `\[` openings and 134 `\]` closings. The optional spacing in `\\[4pt]`, `\\[-2pt]`, and `\\[2ex]` is a row/line-break option, not a display opening.
- All 24 `\left`/`\right` pairs are balanced. Ordinary written parentheses and brackets are not required to be balanced by TeX and were not normalized. The accepted missing ordinary close on page 025 and the literal closing delimiter on page 027 are not structural TeX brace errors.
- No `\figure` or `\diagram` call is in math mode. The five `\figure` calls occur on pages 003, 008, 013, 015, and 023; the two `\diagram` calls occur on pages 023 and 024. Their supplied paragraph/center implementations therefore do not create a current figure-within-math failure.
- TikZ node formula content is locally delimited in the node's text context. Inline TikZ pictures inside mathematical expressions are not, by themselves, an invalid paragraph wrapper. No unsupported node-math dollar nesting was identified.
- No direct `\unsure{...}` followed by an additional superscript was found; such a form would be a separate risk because the supplied math branch already adds `^{?}`. Current occurrences do not require that repair.
- No unavailable control sequence was identified among the 102 distinct page command names. They belong to base LaTeX, amsmath/amssymb, ulem, TikZ/tikz-cd, or the supplied preamble. This command-availability result does not excuse the distinct Gamma font-slot defect described in F1.
- Inline math nested in prose-mode `\deleted`, `\inserted`, or `\unsure` is not automatically an error. The identified repairs concern block displays or margin construction inside text strikeout, rather than removing valid inline dollar pairs.

These are static source checks, not a compilation or rendered-layout certificate. Margin overflow, page breaks, graphic placement, line lengths, and the visual interaction of nested strikeouts remain outside the observed result.

## Snapshot drift and required short recheck

At the final hash-only check, these page files had changed since the reviewed snapshot:

| File | Current hash at 2026-11-20T22:05:34.968362+00:00 |
|---|---|
| 145_scan021.tex | `a1263cc8f4f15b4746736f2d1a239e7edfa20da74496c4794b232e6b79c0a1b8` |
| 145_scan022.tex | `fa497256e0b8b80061e3d28773d8848fad9ff80072b14dcc8c64a52e2ef9a105` |
| 145_scan023.tex | `ece030772e561b0dcbd55a59590df9286f4a78ae9423e07deb85ab05ace4ed9e` |

Those changed contents were not substituted into this review. Root was still auditing pages 021–027, so all seven of those pages require a short final static recheck after their accepted edits settle, even if a particular page had not changed at this hash check. The exact replacement proposals D1–D9 and I1 still matched the unchanged snapshot files at that check.

After root applies any proposals, recheck pages 012, 013, 014, 015, 018, and 019 for the split cancellation structure, and page 024 for every Gamma replacement and preserved uncertainty context. Recheck any later preamble change against all fragments. The recheck should remain structural; it must not normalize manuscript punctuation, notation, formulas, or revision states.

## Snapshot SHA-256 hashes

These hashes identify the actual sources read for the review, rather than the later changed page versions listed above.

| Source | Bytes | SHA-256 |
|---|---:|---|
| edition/pages/145_scan003.tex | 2254 | `e5a220cbd46c2cb4787ec04e686cd7ae04b16d279f5adf5d284d0747cb378ec4` |
| edition/pages/145_scan005.tex | 1834 | `106e7ec9e7298793eb67e2a0159881a8de9bcf80d949549d1f9a2fe66b8afa3a` |
| edition/pages/145_scan006.tex | 2110 | `ee6b9ac302e0406d7579f1a8d0b99df3548ce68f347d6ab9d6533602512ccb2a` |
| edition/pages/145_scan007.tex | 1231 | `e6c4c93bac400ed96686c9be35964019909c3c5666603c3d0346e81835787c0f` |
| edition/pages/145_scan008.tex | 2124 | `1ac7d9b09e9f0006d0f0ec2f569339eb869ee40622bf08d9094e85fe3bd49104` |
| edition/pages/145_scan009.tex | 1837 | `3ed1fc580820ddf57f99549587c0e387983d143e5afe22d97179bff514a1aa2c` |
| edition/pages/145_scan010.tex | 1374 | `608e3b9bcc47000d28181527ae0ee9a5b6bc83c869d39289dd929ef574cafabd` |
| edition/pages/145_scan011.tex | 1846 | `63f8ac9ec03be53c428d4ba19283885f6604426261cae99ae255688b2cc57c8c` |
| edition/pages/145_scan012.tex | 1584 | `09207aeeedb709e590754c3d57e27888de8b02a864e9d3216140cdb91d39b64a` |
| edition/pages/145_scan013.tex | 4331 | `2310034831c3c556b6d3e73a4705a09dea3ed2ec1c5186b385b9f82165c69ca5` |
| edition/pages/145_scan014.tex | 1933 | `1ebf61d87d5442562d84bfd712e1d17e5c4cb72d4cab9c0afe9d507c61ba42f9` |
| edition/pages/145_scan015.tex | 1674 | `aa4f0dd4382ffccdf0f898c84c1aee7fcf11ba2acb7a325a452dd64dbb115f0b` |
| edition/pages/145_scan016.tex | 2279 | `7e51d0bc45126f55282c8416628bbf7b9dc6b38ce450a18685d61cd70d1d0fe5` |
| edition/pages/145_scan017.tex | 1802 | `b04169751ca8e8b038b0de2139d37403add4ce03982e9f49f47a6bfec3c9e3ff` |
| edition/pages/145_scan018.tex | 4048 | `8922fd22e4007f3734f3b75182f244b313d725abae9ffd1dfe1b610789a4709a` |
| edition/pages/145_scan019.tex | 2907 | `115c6c2ae5ed7157dc64843715a6d5b1287638c4beec932ceae9a29f59224582` |
| edition/pages/145_scan020.tex | 4836 | `057b03f845870506456d9ed18797c802c943da52baf9850099fda98af9cf5fe0` |
| edition/pages/145_scan021.tex | 3305 | `6bd4572d3efddc800aa217d7d7d3aed848e7c96fed024e6e3e5e52dba43f75d6` |
| edition/pages/145_scan022.tex | 3027 | `fc88b73360e6da880d6cdcf51565053791c07cfa36186ebf6b5e1efa4f6e522e` |
| edition/pages/145_scan023.tex | 1972 | `e5c636be02fc429ce608ed553a23c12dcad9366df18534ed32529b1f489cbc30` |
| edition/pages/145_scan024.tex | 1954 | `9cb52898adf7a1b059a2fec41919b207d48d9ed7e5d5fdbaf3b372b531cafb69` |
| edition/pages/145_scan025.tex | 3428 | `f1323c16148e2dfa3625f7902f6d23c67829f9a6b89b1802413917da929012ee` |
| edition/pages/145_scan026.tex | 1202 | `4845f86d465dbdbaeb82e331334591dc6b52c821b898c9fae0d35e0fd49c6d9c` |
| edition/pages/145_scan027.tex | 2114 | `140111e87e545638e33bfae4c20036bfef5b1c4f169f493c17e674bacd56c56f` |
| source/SP75_C13_145_texts/PREAMBLE.tex | 1607 | `aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf` |

### Installed package-definition evidence

Hashes checked at 2026-11-20T22:05:34.968362+00:00. These files were read only for the supplementary Gamma assessment.

| Source | SHA-256 |
|---|---|
| /usr/share/texlive/texmf-dist/tex/latex/base/fontmath.ltx | `d7368515628e9e6e4ede13eb985e6ad3dccab6976c023a1bef45e60acf0dc4cc` |
| /usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty | `dab8b0e621267acfd89736cf97bdcc02647c545c0719c4997be8a7d1bf98f9c3` |
| /usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| /usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty | `75fb45a2bc94a2f383abd95220465053f0693b9331854680079a6eb015f328dc` |

## Disposition

The report is complete for its stated snapshot. All proposed page changes remain with root. No first or second reading has been reopened or modified.

