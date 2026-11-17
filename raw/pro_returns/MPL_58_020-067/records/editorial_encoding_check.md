# Mechanical inventory and macro encoding check

Checked 2026-11-17 13:29:36 UTC. No images, crops, attachments, or context were opened. This report describes file encoding only and makes no inference about ink or attribution. Neither page files nor inventory rows were edited.

## Requested inventory checks

- **Scan 032:** Both matching inventory labels already say **Fermés**. Element 4 (CSV line 211, kind `deletion`) is `Fermés de Lefschetz-Grauert`; element 15 (CSV line 222, kind `text`) is `Fermés de Lefschetz-Grauert. Remarques, exemples`. There are no `Faisceaux` occurrences in this scan's inventory labels.
- **Scan 041:** Element 18 (CSV line 411, position `bottom revised proposition`) still has kind `text`. In the fragment, `Pr. 2` at line 39 occurs under the nested wrappers `\unsure{\deleted{\uline{...}}...}`. To match that existing encoding, the corresponding inventory row should have kind **`deletion`**. This is a metadata consistency recommendation, not a reading judgment; the outer doubt wrapper remains relevant.

## Corner numerals and `\mspage`

Every retained scan N has exactly one inventory `margin note` row with numeral N−1, and the matching fragment uses `\margin`, not `\mspage`, for that numeral. Forty fragments use `\margin{N−1}` directly. Scans **051, 053, 061, and 063** instead use `\margin{\rotatebox{180}{N−1}}`, giving 50, 52, 60, and 62 respectively. This describes the encoding and does not identify whose numerals they are.

There are nine separate `\mspage` calls:

| Scan | Literal argument of `\mspage` |
|---|---|
| 020 | `- 2 -` |
| 022 | `- 3 -` |
| 024 | `- 2 -` |
| 030 | `\uline{III} \unsure{0}` |
| 047 | `- 11 -` |
| 049 | `- 10 -` |
| 051 | `- 134 -` |
| 053 | `- 133 -` |
| 063 | `- 7 -` |

## Control sequences outside the editorial list

No additional custom macro was found. The following 103 control words are standard LaTeX, AMS mathematics, TikZ/tikz-cd, or graphics commands. `\rotatebox` is supplied by `graphicx` (also loaded by TikZ). A lexical scan treats `\\` as one control symbol, so ordinary words following a row break are not misreported as commands.

```latex
\Downarrow \Gamma \Lambda \Longleftrightarrow \Longrightarrow \Phi \Rightarrow \S \Updownarrow
\Vert \alpha \arrow \ast \bar \begin \beta \bigcap \bigcup
\bigl \bigoplus \bigr \bullet \cap \cdots \check \chi \circ
\coprod \cup \det \dim \displaystyle \div \downarrow \draw \ell
\end \eta \exists \fbox \fill \forall \ge \geq \gg
\hat \hfill \in \lambda \ldots \left \leq \linewidth \longleftarrow
\longmapsto \longrightarrow \mathbin \mathcal \mathfrak \mathop \mathrm \mu \ne
\newline \ni \node \notin \nu \omega \operatorname \otimes \overline
\overset \pi \prod \qquad \quad \rho \right \rotatebox \sigma
\sim \simeq \subset \substack \sum \supset \text \textcircled \texttt
\times \underbrace \underline \underset \varnothing \varphi \varprojlim \wedge \widehat
\widetilde \xi \xrightarrow \zeta
```

Standard control symbols present: `\ ` (control space), `\!`, `\&`, `\,`, `\[`, `\\`, `\]`, `\{`, `\}`; a backslash followed by a physical newline also occurs (TeX treats it as a control space).
