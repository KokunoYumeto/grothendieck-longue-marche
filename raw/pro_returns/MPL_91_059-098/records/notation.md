# Shared notation table

This table was begun during the first visual pass and expanded at the final comparison, before opening the context. Differences supported by the ink remain differences; unresolved differences carry `\unsure` rather than being forced into a uniform mathematical convention.

| Recurring ink / usage | LaTeX encoding | Comparison and decision |
|---|---|---|
| Underlined Hom versus plain Hom | `\underline{\mathrm{Hom}}`, `\mathrm{Hom}` | Scans 59, 63, 66, 69, 87–89, 97: retain each visible underline; no blanket replacement. |
| Local functor W; ring prescheme W; often omitted underline | `\underline W`, `W` | Scans 61–80 compared during audit. Underlines were removed where supplied without ink on 64, 65, 70, 71, and restored where visible on 67, 78. The manuscript itself varies; plain W is not automatically the ring object. |
| Adjoint exponent | `W^a`, `\underline W^a` | Small superscript a on 63–80; it is not a prime. The final expression on 70 has no visible a and remains W. |
| Primed functor, base, open | `W'`, `S'`, `\mathcal U'` | Especially 66–70, 75–79: prime kept separately from exponent a; doubtful final U decoration on 70 remains marked. |
| Star / prime ambiguity | `\unsure{S^*|S'}` | Scan 78: the mark is not resolved from the expected base. Cancelled star-like marks on 65–66 remain in deletions. No secure exclamation-mark exponent was identified in this package. |
| Calligraphic A versus underlined plain A | `\mathcal A`, `\underline A` | Scan 62 uses the first; scan 65 visibly uses the second. Checks/dual marks are `\check{...}` in both. |
| Underlined ordinary O | `\underline O` | Scans 62 and 65: the ink supports ordinary underlined O, not a supplied script O. |
| Gothic target letters versus ordinary representing letters | `\mathfrak X`, `\mathfrak Y`; `X`, `Y` | Scans 62–80 checked against each occurrence. Plain X in the final map on 70 and plain X_i at the end of the local chain on 73 were preserved. |
| Calligraphic opens versus ordinary opens | `\mathcal U`, `U` | Scans 70, 75–79: decorations retained; uncertainty about the prime on the last open of 70 is explicit. |
| Lambda and Gamma | `\Lambda`, `\Gamma`, `\underline\Gamma` | Scans 61–69: preserve the actual glyph and any underline; the reuse of Lambda for differently described objects is not normalized. |
| Algebra letter C / looped ell | `\unsure{C}`, `\unsure{\ell|C}` | Scan 68: overwritten C and looped corollary letter are kept distinct; no algebraic reconstruction settles the ink. |
| Barred geometric objects | `\overline T`, `\bar s`, `\overline{k(s)}`, `\bar x` | Scans 59 and 84; scope of bars checked locally. |
| Decorations on atomic source and target | `\unsure{\widetilde X|\bar X}`, similarly Y | Scan 87: heavy strokes do not securely decide tilde versus bar. |
| F / calligraphic T versus later plain T | `\unsure{F|\mathcal T}`, `T` | Scan 84: no uniformization of the initial letter from the following assertions. |
| Roman example labels | `\mathrm I`, `\mathrm I'`, `\mathrm{II}`, `\unsure{\mathrm{III}}`, `\unsure{\mathrm{III'}}` | Scans 61, 62, 71, 74, 75, 78: overwritten labels on 62 stay doubtful. |
| a-shaped mark on example II | `\unsure{\mathrm{II}^{a}|\mathrm{II}'}` | Scan 74 compared again with the labels on 62 and the clear I-prime on 74; the visible mark is a-shaped and is not silently changed to a prime. |
| Triple-overlap third index | `\unsure{h|k}` or `\unsure{k|h}` | Scans 71–72: first reading follows the local shape; the clear k occurrences are retained. They are not made identical merely for the cocycle argument. |
| Alpha/beta order | `Y_{\beta\alpha}`, later `Y_{\alpha\beta}` | Scan 93: order visibly changes; both retained. |
| Small partition-piece subscript | `T_{\unsure{i|\alpha}}^\beta` | Scan 97: first surviving piece has an i-like dot/stem, unlike later alpha; both readings remain possible. |
| Direct / inverse limits | `\varinjlim`, `\varprojlim` | Scans 69, 95, 97, 98: each arrow direction checked. The two differently ordered limits on 97 are intentional transcription. |
| Implication versus map | `\Longrightarrow`, `\longrightarrow`, `\to` | Scan 97 transition condition has a double arrow; the proposed cons comparison has a clear right arrow with a tilde. |
| Dash without secure arrowhead | `\unsure{-|\to}` or literal `-` | Scans 66, 69, 79, 87, 91: no mathematical arrowhead supplied. |
| Equality shorthand in prose | `$=$` | Scans 64, 71, 74, 75, 77, 79, 82: retained as ink, not expanded to a French word. |
| Inequalities | `\leq`, `\geq`, `<`, `\subset` | Especially 76–77, 85, 94, 97–98: first norm bound on 94 is strict, last weak; source inclusions are not silently strengthened or weakened. |
| Typed Lie algebra letter and names | `g`, `\mathrm{sl}(V)`, `\mathrm{gl}(V)` | Scans 88, 90, 92: ordinary printed g; sl on 90 versus gl on 92, checked at enlargement. |
| Typed dual stars and primes | `x_i^*`, `x'_i` | Scan 88: two primes are visibly printed in the pairing; no replacement by the mathematically expected unprimed argument. |
| Round typed subscript | `\unsure{o|0}` | Scan 96, every x/H occurrence: primary o follows its round type; 0 remains an alternative. |
| Script L in typed exercises | `\mathcal L` | Scans 83, 88, 90, 92; not substituted for plain L in the normed-map text on 94. |
| Double quotation marks / ditto marks | two backticks and two apostrophes | Scans 61, 63, 68, 79, 87, 96: one convention throughout. No guillemets supplied. |
| Circled 1, 2, 3 and alpha/beta | `\textcircled{...}` | Scans 61, 67, 70–71 are section or condition markers. They are not `\mspage`. |
| Later corner numerals | `% archive foliation: ...` | Kept apart from scan identifiers. No secure author page number was identified. Printed headings remain ordinary text. |
| Graphical enclosures and strokes | `\figure{\begin{tikzpicture}...}` | Ovals, boxes, small correction strokes and connecting curves are reproduced, not replaced with descriptions. Their geometry is approximate; uncertain labels stay marked. |
| Diagrams in macro arguments | `\diagram{\begin{tikzcd}[ampersand replacement=\&]...}` | Escaped cell separators are a TeX requirement, not a change of diagram. Cancelled nodes/labels retain `\deleted`. |

