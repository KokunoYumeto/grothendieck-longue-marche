# Mechanical notation and syntax report

Generated: 2026-11-15 20:33:40 UTC

Scope: lexical checks of the 48 TeX fragments only. No manuscript images or context were opened; no page file was edited.

Checked 48 fragments, 48 scan markers, 74 tikz-cd environments and 265 diagram arrow commands.

Structural issues: 0; additional row-separator issues: 0; literal Unicode Greek characters: 0.

Brace balance, environment nesting, math delimiters, macro-name allowlist and explicit matrix arrow targets passed when the issue count is zero. This does not establish visual fidelity or mathematical correctness. Full TeX compilation was unavailable because the installed engine lacks pdflatex.fmt; it was not repeated for this report.

## Token-count conventions

Counts are lexical. Prime marks count apostrophes in mathematical regions, excluding text/typographic-text/operator-name groups; prime commands are listed separately. Script counts recognize direct forms such as `^!` and `^{!}`. They do not normalize compound superscripts or infer a sign hidden inside an annotation. Arrow/no-head counts distinguish explicit `no head` options; drawing counts report whether a local option explicitly supplies arrowheads, without inferring inherited TikZ styles.

Complete page-by-page counts are in `mechanical_notation_counts.csv`; the JSON report includes command counts and the scans using each command.

## Aggregate construction counts

| Construction | Count |
|---|---:|
| `prime_marks_in_math` | 222 |
| `prime_runs_in_math` | 221 |
| `prime_command` | 1 |
| `sup_bang` | 0 |
| `sub_bang` | 1 |
| `sup_star` | 41 |
| `sub_star` | 42 |
| `overline` | 44 |
| `bar` | 0 |
| `widetilde` | 28 |
| `tilde` | 0 |
| `mathcal` | 56 |
| `mathfrak` | 0 |
| `mathbb` | 0 |
| `underline` | 142 |
| `uline` | 125 |
| `uuline` | 7 |
| `arrow_commands_all` | 395 |
| `tikz_arrow_commands` | 265 |
| `tikz_arrow_no_head` | 42 |
| `draw_commands_with_explicit_heads` | 0 |
| `draw_commands_without_explicit_heads` | 9 |
| `greek_commands` | 383 |

## Command-name inventory

120 distinct alphabetic command names; all are in the technical checker's standard-math/TikZ or permitted-state macro allowlist.

`\Delta`, `\Downarrow`, `\Lambda`, `\Leftarrow`, `\Leftrightarrow`, `\Longleftrightarrow`, `\Longrightarrow`, `\Omega`, `\Phi`, `\Pi`, `\Psi`, `\Rightarrow`, `\Sigma`, `\Updownarrow`, `\Vert`, `\alpha`, `\arrow`, `\begin`, `\beta`, `\big`, `\boxed`, `\boxtimes`, `\bullet`, `\cap`, `\cdot`, `\cdots`, `\circ`, `\colon`, `\cotefile`, `\cup`, `\deleted`, `\diagram`, `\draw`, `\end`, `\eta`, `\exists`, `\figure`, `\forall`, `\gamma`, `\geq`, `\hline`, `\hookrightarrow`, `\hspace`, `\illegible`, `\in`, `\infty`, `\inserted`, `\int`, `\joinrel`, `\ldots`, `\left`, `\leftarrow`, `\leq`, `\lhook`, `\linewidth`, `\longrightarrow`, `\mapsto`, `\margin`, `\mathbf`, `\mathbin`, `\mathcal`, `\mathrm`, `\mathtt`, `\mid`, `\mspage`, `\multicolumn`, `\ne`, `\operatorname`, `\otimes`, `\overbrace`, `\overline`, `\overset`, `\partial`, `\phantom`, `\pi`, `\pounds`, `\prime`, `\psi`, `\qquad`, `\quad`, `\rho`, `\right`, `\rightarrow`, `\rule`, `\scanpage`, `\setminus`, `\sigma`, `\sim`, `\simeq`, `\stackrel`, `\subset`, `\substack`, `\sup`, `\supset`, `\text`, `\textcircled`, `\textit`, `\textnormal`, `\textsf`, `\texttt`, `\theta`, `\tikzcdmatrixname`, `\times`, `\to`, `\uline`, `\underbrace`, `\underline`, `\underset`, `\unsure`, `\uuline`, `\varinjlim`, `\varnothing`, `\varphi`, `\varprojlim`, `\vert`, `\wedge`, `\widehat`, `\widetilde`, `\xi`, `\xrightarrow`

## Mechanical issues

None detected.
