# Notation concordance and reading doubts

## Notation concordance

The table records graphic choices made from the scans, before the context archive was opened. It does not impose a mathematically uniform notation on passages where the written forms differ. Cote 154, scans 046–076, is the entire retained input; the cote 81 pages named in the package prefix were explicitly omitted from the supplied scan archive.

| Recurring manuscript form | Diplomatic LaTeX | Comparison and limits |
|---|---|---|
| Ordinary Latin capitals and lower-case letters | `X,Y,K,L,F,D,a,b,s,t,u,v,n,p` | Capitals, subscripts, and changes of letter are retained locally; an apparent mathematical mismatch does not license changing a letter. |
| More elaborate X used for the reconstructed surface | `\mathcal X` | Distinguished from the base `X`, especially scans 065–076. A large cursive ordinary X is not automatically made calligraphic. |
| Tilde above X, I, or D | `\widetilde X`, `\widetilde I`, `\widetilde D` | Single versus double tilde above X remains explicitly doubtful in scans 059–060. |
| Underlined Sigma | `\uline{\Sigma}` | The underline is retained, including in discussion of vertices and configurations. It is not converted into an unrelated alphabet. |
| Double-stroked number-system letters | `\mathbb N`, `\mathbb Z` | Scan 047 was compared with later occurrences; the half-integer group there retains an alternative bold-Z reading. |
| Double-stroked dihedral-group letter | `\mathbb D_{2n}` | Kept apart from ordinary D for a position or line. Indices and a plus superscript are transcribed only where written. |
| Map letter with small loop and descending stem | `\varphi` | Used for the recurring map in the early pages and later local constructions; no switch to `\phi` based on mathematical function. |
| Boundary mark with delta-shaped loop and top stroke | `\delta` | Typical in scans 046–054, including `\delta F` and `\delta'F`; also the named critical line in later drawings. |
| Curved partial-shaped boundary mark | `\partial` | Retained in such places as scan 051 and the boundaries of disks in scans 066, 068, 076. The `\partial F`/`\delta F` ambiguity in scan 049 remains marked. |
| Triangle-shaped capital delta | `\Delta_D`, `\Delta_{D'}^*` | Not confused with the preceding boundary marks. Stars, primes, and their attachment are kept. |
| Nu, lower-case v, and n | `\nu`, `v`, `n` | Vertex/edge indices use nu where the ink supports it; very faint pencil nu/mu labels on scan 073 remain alternatives. |
| Loop or path ell | `\ell`, `\ell_i`, `\ell_0` | Distinguished from numeral 1; uncertain labels in the scan 056 transport computation are individually recorded below. |
| Rho and sigma | `\rho`, `\sigma`, `\rho_i`, `\sigma_a^F` | The resemblance of a quick rho to sigma is not silently resolved in the transition triple on scan 065. |
| Epsilon sign on an edge or face | `\varepsilon_F(a)`, `\varepsilon_a(F)` | The local order of argument and index is retained, including the apparently reversed convention in scan 048. |
| Chi and ordinary X | `\chi`, `X` | The character in formulas is chi where visibly drawn; an ambiguous boxed subscript on scan 063 is `\unsure{o\|X}`. |
| Subscripted characters | `\chi_s`, `\chi_a`, `\chi_X`, `\chi_{\mathcal X}` | Kept as written at each stage. The manuscript's subsequent comparison of these characters does not change earlier symbols. |
| Orientation symbol, plain or underlined | `\omega`, `\underline\omega` | The local underline is preserved; plain omega in several orientation diagrams is not normalized to the underlined form elsewhere. |
| Vertex sets with primes | `S_K`, `S'_K`, `S''_K` | Single and double primes distinguish sets in the early polygon calculations. |
| Primes on positions and arcs | `D'`, `F'`, `F''`, `a'`, `b'` | Recurring marks have been compared across pages. No clear exclamation-mark exponent was identified in this retained set; none was supplied by analogy with other packages. |
| Stars and overwritten endpoint labels | `a^*`, `b^*`, `u^*`, `v^*` | The attachment is retained locally; uncertain small stars are marked in place, notably scans 052, 069, 072. |
| Bar over tubular-neighborhood T | `\overline T`, `\overline T_a` | Distinguished from a prime; the object of the involution in scan 047 remains `a`/`\overline T_a` doubtful. |
| Hat or arch over a side or string of points | `\widehat a`, `\widehat{usv}`, `\overbrace{...}` | Long drawn arches are retained as arches, not made into straight bars. Labels and starred endpoints are not completed from symmetry. |
| Polygon functor and shorter P | `\operatorname{Pol}(D)`, `P(F_n)` | A shorter written P is retained, with a doubt alternative where needed, rather than expanded into Pol throughout. |
| Aut, image, identity, and connected-component notation | `\operatorname{Aut}`, `\operatorname{Im}`, `\mathrm{id}`, `\Pi_0`/`\pi_0` | The capital/lower-case pi question on scan 061 is left open. |
| Equality, inequality, inclusion, and non-equality | `=`, `\leq`, `\geq`, `\subset`, `\supset`, `\ne` | Ambiguous inequality/equality strokes remain marked, notably scan 047. A displayed expression is never corrected to fit its surrounding argument. |
| Equality-like shorthand in prose | `$=$`, occasionally `\unsure{$=$s\|$=$}` | The visible two-stroke sign is transcribed as a sign, including in `lui-$=$`, `elle-$=$`, and before *indice* or *signe*. Its probable expansion is listed only in the abbreviation glossary below. |
| Actual written word *même* | `même` | Retained where letters are visible, for example *même en choisissant* and *quand même* in scan 066; the prose shorthand is not substituted globally. |
| Arrow with visible head | `\longrightarrow`, `\longleftrightarrow`, TikZ/TikZ-cd arrows | Direction follows the ink. The curved transport link in scan 068 is bidirectional; very small figure heads may remain less certain than the main geometry. |
| Plain connecting dash or headless isomorphism link | `\mathbin{-}` or a headless TikZ-cd link | Kept headless in the orientation and polygon diagrams when no arrowhead is visible. An isomorphism label does not manufacture an arrowhead. |
| Double quotation marks | <code>``...''</code> | Used for the drawn double quotes, including nested quotation in scan 047. No guillemets were supplied merely because the prose is French. |
| Written ellipsis and unfinished expressions | `\dots`, `\ldots`, or a terminal relation exactly as written | These transcribe visible dots or an unfinished written formula; none substitutes for omitted content. |
| Single and double underlining | `\uline{...}`, `\uuline{...}` | Preserved separately; e.g. the emphatic *opposée* in scan 067. |
| Cancellations, insertions, and independent marginal notes | `\deleted`, `\inserted`, `\margin` | Content remains present. Large cancellation boundaries on scans 054 and 058 are separately discussed because their extent is less certain than the words within them. |
| Curves, colored strokes, hatching, and regions | `\figure{\begin{tikzpicture}...}` | Manually drawn vector transcriptions, with written labels included. Color is approximated to distinguish the visible ink groups, not sampled as an exact colorimetric measurement. |
| Object-and-map diagrams | `\diagram{\begin{tikzcd}...}` | Objects, directions, and labels are transcribed. Layout is adjusted for typesetting without completing a missing arrow or unfinished row. |
| Printed listing-paper text | `\texttt{...}` with literal visible characters | Banner digits, job lines, masking asterisks, times, and notices are included on reused sheets; these are not treated as irrelevant background. |

## How to use the doubt register

Every literal `\unsure` occurrence in the frozen page files has one row below, including repeated readings and doubt macros nested inside another doubt or a deletion. The identifier `154-NNN-Uxx` is local to this package; the file column and TeX line locate the exact occurrence, while the position column identifies its approximate place on the manuscript sheet. TeX line numbers are locators in the diplomatic source, not claims to reproduce the manuscript's original line breaks.

**High** means a strong graphic reading with a residual local reservation; **medium** means a plausible reading supported by part of the visible letter or symbol structure; **low** means heavily overwritten, cramped, faint, or speculative, or that the alternatives cannot be separated. These are qualitative editorial judgments, not calibrated error probabilities. A dash in the alternatives column means no defensible second reading is proposed, not that the preferred reading is secure.

