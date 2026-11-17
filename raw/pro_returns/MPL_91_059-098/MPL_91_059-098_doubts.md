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


## Doubt register

The table below enumerates every uncertainty or unreadable-word macro in the frozen page text. Locations are line numbers in the individual page fragment (not the combined file); they locate the corresponding manuscript passage approximately. Confidence describes the reading, not its mathematical plausibility. `low` also covers highly compressed words and overwritten phrases for which an alternative cannot responsibly be invented.

| File | Scan | Approximate location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|---|
| 91.pdf | 59 | 4 | comme pour | No second reading securely proposed. | low |
| 91.pdf | 59 | 8 | tel | No second reading securely proposed. | low |
| 91.pdf | 59 | 13 | raison | No second reading securely proposed. | low |
| 91.pdf | 59 | 13 | $S'\to S$ | No second reading securely proposed. | low |
| 91.pdf | 59 | 15 | p. ex. | No second reading securely proposed. | low |
| 91.pdf | 59 | 16 | a | No second reading securely proposed. | low |
| 91.pdf | 59 | 16 | un fini | No second reading securely proposed. | low |
| 91.pdf | 59 | 18 | regarder | No second reading securely proposed. | low |
| 91.pdf | 59 | 18 | un | No second reading securely proposed. | low |
| 91.pdf | 59 | 18 | ch. | No second reading securely proposed. | low |
| 91.pdf | 59 | 20 | sch. | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | enfin | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | f | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | comme | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | le | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | dessus | No second reading securely proposed. | low |
| 91.pdf | 59 | 24 | chgt. | No second reading securely proposed. | low |
| 91.pdf | 59 | 25 | encore | No second reading securely proposed. | low |
| 91.pdf | 59 | 25 | $\mathrm{H}$ | No second reading securely proposed. | low |
| 91.pdf | 59 | 27 | isom. | No second reading securely proposed. | low |
| 91.pdf | 59 | 27 | T--- | No second reading securely proposed. | low |
| 91.pdf | 61 | 4 | Set up | No second reading securely proposed. | medium |
| 91.pdf | 61 | 6 | Algèbre | No second reading securely proposed. | medium |
| 91.pdf | 61 | 6 | 2 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 61 | 8 | $S$ | No second reading securely proposed. | medium |
| 91.pdf | 61 | 13 | on fera | No second reading securely proposed. | medium |
| 91.pdf | 61 | 13 | de suite | No second reading securely proposed. | medium |
| 91.pdf | 61 | 13 | tt | No second reading securely proposed. | medium |
| 91.pdf | 61 | 19 | quelc. | No second reading securely proposed. | medium |
| 91.pdf | 61 | 30 | $S$ | No second reading securely proposed. | medium |
| 91.pdf | 61 | 30 | préschéma | No second reading securely proposed. | medium |
| 91.pdf | 61 | 30 | le | No second reading securely proposed. | medium |
| 91.pdf | 61 | 30 | 1 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 61 | 30 | ainsi | No second reading securely proposed. | medium |
| 91.pdf | 61 | 31 | associé aux | No second reading securely proposed. | medium |
| 91.pdf | 61 | 31 | anneaux locaux | No second reading securely proposed. | medium |
| 91.pdf | 62 | 3 | un foncteur | No second reading securely proposed. | medium |
| 91.pdf | 62 | 4 | défini | No second reading securely proposed. | medium |
| 91.pdf | 62 | 4 | covar. | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | Nous donnerons des | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | préschémas | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | puis que | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | 2 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 62 | 8 | conditions | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | prop. | No second reading securely proposed. | medium |
| 91.pdf | 62 | 8 | voulues | No second reading securely proposed. | medium |
| 91.pdf | 62 | 10 | III | No second reading securely proposed. | medium |
| 91.pdf | 62 | 10 | algèbres | No second reading securely proposed. | medium |
| 91.pdf | 62 | 11 | W | No second reading securely proposed. | medium |
| 91.pdf | 62 | 15 | III' | No second reading securely proposed. | medium |
| 91.pdf | 62 | 16 | blague sur | No second reading securely proposed. | medium |
| 91.pdf | 63 | 3 | veut | No second reading securely proposed. | medium |
| 91.pdf | 63 | 3 | T | No second reading securely proposed. | medium |
| 91.pdf | 63 | 3 | T | No second reading securely proposed. | medium |
| 91.pdf | 63 | 11 | factorisation | No second reading securely proposed. | medium |
| 91.pdf | 63 | 15 | à | No second reading securely proposed. | medium |
| 91.pdf | 63 | 17 | T | No second reading securely proposed. | medium |
| 91.pdf | 64 | 8 | pour | No second reading securely proposed. | medium |
| 91.pdf | 64 | 14 | existence | No second reading securely proposed. | medium |
| 91.pdf | 65 | 5 | faisc. | No second reading securely proposed. | medium |
| 91.pdf | 65 | 7 | un | No second reading securely proposed. | medium |
| 91.pdf | 65 | 7 | de | No second reading securely proposed. | medium |
| 91.pdf | 65 | 7 | * | No second reading securely proposed. | medium |
| 91.pdf | 66 | 3 | avec | No second reading securely proposed. | medium |
| 91.pdf | 66 | 3 | donc | No second reading securely proposed. | medium |
| 91.pdf | 66 | 5 | \mathfrak Y_r | No second reading securely proposed. | medium |
| 91.pdf | 66 | 7 | \alpha(T) | No second reading securely proposed. | medium |
| 91.pdf | 66 | 7 | * | No second reading securely proposed. | medium |
| 91.pdf | 66 | 9 | - | \to | medium |
| 91.pdf | 66 | 16 | qui est d'ailleurs | No second reading securely proposed. | medium |
| 91.pdf | 66 | 21 | - | \to | medium |
| 91.pdf | 66 | 27 | - | \to | medium |
| 91.pdf | 66 | 27 | W | No second reading securely proposed. | medium |
| 91.pdf | 66 | 30 | ) | No second reading securely proposed. | medium |
| 91.pdf | 66 | 32 | hom | No second reading securely proposed. | medium |
| 91.pdf | 66 | 38 | ') | ) | medium |
| 91.pdf | 67 | 3 | $\mathfrak X$ fixé | No second reading securely proposed. | low |
| 91.pdf | 67 | 3 | fixé | No second reading securely proposed. | low |
| 91.pdf | 67 | 10 | en plus | No second reading securely proposed. | low |
| 91.pdf | 67 | 10 | sur un | No second reading securely proposed. | low |
| 91.pdf | 67 | 11 | associé à un | No second reading securely proposed. | low |
| 91.pdf | 67 | 11 | d' | No second reading securely proposed. | low |
| 91.pdf | 67 | 13 | fais. | No second reading securely proposed. | low |
| 91.pdf | 67 | 13 | Avec | No second reading securely proposed. | low |
| 91.pdf | 67 | 13 | caractère local | No second reading securely proposed. | low |
| 91.pdf | 68 | 3 | est | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | Soit | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | C | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | C | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | \S\ N° 1 | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | W^r | No second reading securely proposed. | low |
| 91.pdf | 68 | 7 | cqf | No second reading securely proposed. | low |
| 91.pdf | 68 | 9 | S aff. | No second reading securely proposed. | low |
| 91.pdf | 68 | 9 | l\textquotesingle anneau de | No second reading securely proposed. | low |
| 91.pdf | 68 | 9 | \ell | C | low |
| 91.pdf | 68 | 9 | v | No second reading securely proposed. | low |
| 91.pdf | 69 | 3 | v | No second reading securely proposed. | medium |
| 91.pdf | 69 | 13 | W(B) | No second reading securely proposed. | medium |
| 91.pdf | 69 | 21 | W^a | No second reading securely proposed. | medium |
| 91.pdf | 69 | 21 | \longrightarrow | No second reading securely proposed. | medium |
| 91.pdf | 69 | 30 | soit | No second reading securely proposed. | medium |
| 91.pdf | 69 | 32 | S | No second reading securely proposed. | medium |
| 91.pdf | 69 | 32 | - | \to | medium |
| 91.pdf | 70 | 21 | \mathcal U' | \mathcal U | low |
| 91.pdf | 71 | 5 | \mathrm I' | No second reading securely proposed. | low |
| 91.pdf | 71 | 5 | \mathrm{II}'' | No second reading securely proposed. | medium |
| 91.pdf | 71 | 7 | vérifient | No second reading securely proposed. | medium |
| 91.pdf | 71 | 7 | \} | No second reading securely proposed. | medium |
| 91.pdf | 71 | 7 | bis-bis | bis-idem | medium |
| 91.pdf | 71 | 7 | h | k | medium |
| 91.pdf | 72 | 3 | un ouvert | No second reading securely proposed. | low |
| 91.pdf | 72 | 3 | à l'ouvert | No second reading securely proposed. | low |
| 91.pdf | 72 | 3 | \varphi_{ki}=\varphi_{kj}\varphi_{ji} | No second reading securely proposed. | low |
| 91.pdf | 72 | 5 | k | h | low |
| 91.pdf | 72 | 6 | k | h | low |
| 91.pdf | 72 | 7 | k | h | low |
| 91.pdf | 72 | 7 | k | h | low |
| 91.pdf | 72 | 11 | k | h | low |
| 91.pdf | 72 | 13 | la flèche | No second reading securely proposed. | low |
| 91.pdf | 72 | 19 | et | No second reading securely proposed. | low |
| 91.pdf | 72 | 19 | hom | No second reading securely proposed. | low |
| 91.pdf | 73 | 19 | considérons | No second reading securely proposed. | medium |
| 91.pdf | 73 | 19 | les | No second reading securely proposed. | medium |
| 91.pdf | 73 | 19 | images | No second reading securely proposed. | medium |
| 91.pdf | 73 | 20 | supposons | No second reading securely proposed. | medium |
| 91.pdf | 73 | 20 | qu'il | No second reading securely proposed. | medium |
| 91.pdf | 73 | 20 | se | No second reading securely proposed. | medium |
| 91.pdf | 73 | 20 | peut factoriser | No second reading securely proposed. | low |
| 91.pdf | 73 | 20 | et | No second reading securely proposed. | medium |
| 91.pdf | 73 | 20 | soit | No second reading securely proposed. | medium |
| 91.pdf | 73 | 21 | inverse | No second reading securely proposed. | medium |
| 91.pdf | 73 | 24 | ) | No second reading securely proposed. | medium |
| 91.pdf | 74 | 5 | tt | No second reading securely proposed. | medium |
| 91.pdf | 74 | 7 | pour | No second reading securely proposed. | medium |
| 91.pdf | 74 | 7 | liés | No second reading securely proposed. | medium |
| 91.pdf | 74 | 17 | \mathrm{I} | No second reading securely proposed. | medium |
| 91.pdf | 74 | 23 | \mathrm{II}^{a} | \mathrm{II}' | medium |
| 91.pdf | 74 | 25 | \mathrm{II}^{a} | \mathrm{II}' | medium |
| 91.pdf | 74 | 27 | la hyp. utile | No second reading securely proposed. | medium |
| 91.pdf | 75 | 13 | par | No second reading securely proposed. | low |
| 91.pdf | 75 | 13 | radiciel | No second reading securely proposed. | low |
| 91.pdf | 75 | 14 | tout | No second reading securely proposed. | low |
| 91.pdf | 75 | 15 | Soit | No second reading securely proposed. | low |
| 91.pdf | 75 | 18 | supposé | No second reading securely proposed. | low |
| 91.pdf | 75 | 18 | que | W | low |
| 91.pdf | 75 | 19 | de type | No second reading securely proposed. | low |
| 91.pdf | 75 | 20 | fini | No second reading securely proposed. | low |
| 91.pdf | 75 | 25 | \mathrm{II} | No second reading securely proposed. | low |
| 91.pdf | 75 | 25 | ou | No second reading securely proposed. | low |
| 91.pdf | 75 | 25 | \mathrm I | No second reading securely proposed. | low |
| 91.pdf | 75 | 27 | \mathfrak X | No second reading securely proposed. | low |
| 91.pdf | 75 | 35 | fibre | No second reading securely proposed. | low |
| 91.pdf | 76 | 8 | - | No second reading securely proposed. | low |
| 91.pdf | 76 | 14 | v | \varphi | low |
| 91.pdf | 76 | 21 | v | u | low |
| 91.pdf | 76 | 28 | si on décompose | No second reading securely proposed. | low |
| 91.pdf | 76 | 30 | suivant les comp. connexes | No second reading securely proposed. | low |
| 91.pdf | 76 | 32 | on est ramené à | No second reading securely proposed. | low |
| 91.pdf | 76 | 32 | ce que chaque | No second reading securely proposed. | low |
| 91.pdf | 76 | 33 | une section de | No second reading securely proposed. | low |
| 91.pdf | 76 | 33 | sur | No second reading securely proposed. | low |
| 91.pdf | 76 | 35 | tt | No second reading securely proposed. | low |
| 91.pdf | 76 | 40 | 2 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 76 | 40 | nombre | No second reading securely proposed. | low |
| 91.pdf | 76 | 41 | géom. | No second reading securely proposed. | low |
| 91.pdf | 76 | 41 | de points | No second reading securely proposed. | low |
| 91.pdf | 77 | 15 | les | No second reading securely proposed. | low |
| 91.pdf | 77 | 18 | affine | No second reading securely proposed. | low |
| 91.pdf | 77 | 26 | - | No second reading securely proposed. | low |
| 91.pdf | 77 | 29 | 2 | \mathcal Z | low |
| 91.pdf | 77 | 30 | cas. Car | No second reading securely proposed. | low |
| 91.pdf | 77 | 30 | 1 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 77 | 30 | 1 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 78 | 6 | affine | No second reading securely proposed. | medium |
| 91.pdf | 78 | 6 | spécial | No second reading securely proposed. | medium |
| 91.pdf | 78 | 6 | de type | No second reading securely proposed. | medium |
| 91.pdf | 78 | 6 | \mathrm{II} | No second reading securely proposed. | medium |
| 91.pdf | 78 | 9 | ouv. | No second reading securely proposed. | medium |
| 91.pdf | 78 | 11 | en de | No second reading securely proposed. | medium |
| 91.pdf | 78 | 11 | que | No second reading securely proposed. | medium |
| 91.pdf | 78 | 23 | S^* | S' | medium |
| 91.pdf | 78 | 31 | imm. | No second reading securely proposed. | medium |
| 91.pdf | 78 | 32 | sur | No second reading securely proposed. | medium |
| 91.pdf | 79 | 5 | Prop | No second reading securely proposed. | low |
| 91.pdf | 79 | 7 | et | No second reading securely proposed. | low |
| 91.pdf | 79 | 8 | \times | No second reading securely proposed. | low |
| 91.pdf | 79 | 14 | - | \to | low |
| 91.pdf | 79 | 18 | \mathfrak X | No second reading securely proposed. | low |
| 91.pdf | 79 | 18 | quasi | No second reading securely proposed. | low |
| 91.pdf | 79 | 19 | tout | No second reading securely proposed. | low |
| 91.pdf | 79 | 22 | réunion | No second reading securely proposed. | low |
| 91.pdf | 79 | 25 | resp. affine | No second reading securely proposed. | low |
| 91.pdf | 79 | 27 | quasi-affine | No second reading securely proposed. | low |
| 91.pdf | 79 | 28 | inquiétude | No second reading securely proposed. | low |
| 91.pdf | 79 | 29 | l'énoncé est | No second reading securely proposed. | low |
| 91.pdf | 79 | 29 | valable | No second reading securely proposed. | low |
| 91.pdf | 79 | 29 | compte tenu | No second reading securely proposed. | low |
| 91.pdf | 79 | 30 | de la propriété | No second reading securely proposed. | low |
| 91.pdf | 79 | 30 | projectif | No second reading securely proposed. | low |
| 91.pdf | 81 | 3 | Notions d'algèbre | Morph. d'algèbres | low |
| 91.pdf | 81 | 4 | multilinéaire | multilinéaires | low |
| 91.pdf | 82 | 4 | ou | No second reading securely proposed. | low |
| 91.pdf | 82 | 5 | tt pt | No second reading securely proposed. | low |
| 91.pdf | 82 | 5 | a | $\in$ | low |
| 91.pdf | 82 | 5 | un | une | low |
| 91.pdf | 82 | 5 | syst. fond. | pet. fam. | low |
| 91.pdf | 82 | 5 | voisinages rétrocompacts dans | No second reading securely proposed. | low |
| 91.pdf | 82 | 14 | U | No second reading securely proposed. | low |
| 91.pdf | 82 | 16 | dans | No second reading securely proposed. | low |
| 91.pdf | 82 | 17 | et | No second reading securely proposed. | low |
| 91.pdf | 82 | 24 | loc. | No second reading securely proposed. | low |
| 91.pdf | 82 | 30 | suppose que dans | No second reading securely proposed. | low |
| 91.pdf | 82 | 34 | donc | No second reading securely proposed. | low |
| 91.pdf | 84 | 12 | qu. cpt | No second reading securely proposed. | low |
| 91.pdf | 84 | 23 | tte partie ouverte | tt quasi-ouvert | low |
| 91.pdf | 84 | 23 | quasi-cpt. | No second reading securely proposed. | medium |
| 91.pdf | 84 | 23 | rétrocompacte | rétrocompact | medium |
| 91.pdf | 84 | 26 | F | \mathcal T | low |
| 91.pdf | 84 | 29 | E | No second reading securely proposed. | medium |
| 91.pdf | 84 | 29 | U | No second reading securely proposed. | medium |
| 91.pdf | 87 | 4 | spectres | schémas | medium |
| 91.pdf | 87 | 6 | - | \to | medium |
| 91.pdf | 87 | 9 | - | \to | medium |
| 91.pdf | 87 | 14 | - | \to | medium |
| 91.pdf | 87 | 17 | - | \to | medium |
| 91.pdf | 87 | 23 | est | No second reading securely proposed. | medium |
| 91.pdf | 87 | 23 | représente | No second reading securely proposed. | medium |
| 91.pdf | 87 | 25 | - | \to | medium |
| 91.pdf | 87 | 26 | aux schémas ponctuels | No second reading securely proposed. | low |
| 91.pdf | 87 | 29 | pleinement | No second reading securely proposed. | medium |
| 91.pdf | 87 | 33 | \widetilde X | \bar X | low |
| 91.pdf | 87 | 33 | \widetilde Y | \bar Y | low |
| 91.pdf | 87 | 35 | ouvert affine | No second reading securely proposed. | low |
| 91.pdf | 89 | 3 | Transitivité | No second reading securely proposed. | low |
| 91.pdf | 89 | 4 | aff. | No second reading securely proposed. | low |
| 91.pdf | 89 | 4 | trouver | No second reading securely proposed. | low |
| 91.pdf | 89 | 4 | aff. | No second reading securely proposed. | low |
| 91.pdf | 89 | 5 | \varphi | No second reading securely proposed. | low |
| 91.pdf | 89 | 8 | algébrique | No second reading securely proposed. | low |
| 91.pdf | 89 | 8 | 1 unreadable word(s) | No secure reading after magnification; see page and audit. | low |
| 91.pdf | 89 | 11 | \text{réd} | No second reading securely proposed. | low |
| 91.pdf | 89 | 12 | \text{n'd} | No second reading securely proposed. | low |
| 91.pdf | 89 | 12 | \text{fidèle} | No second reading securely proposed. | low |
| 91.pdf | 89 | 19 | Tous | No second reading securely proposed. | low |
| 91.pdf | 89 | 19 | lim. | No second reading securely proposed. | low |
| 91.pdf | 89 | 23 | donc | No second reading securely proposed. | low |
| 91.pdf | 89 | 25 | \mathfrak S | \mathsection | low |
| 91.pdf | 89 | 25 | comme | No second reading securely proposed. | low |
| 91.pdf | 89 | 25 | l.c.q. | l.c.p. | low |
| 91.pdf | 89 | 34 | quelconque | No second reading securely proposed. | low |
| 91.pdf | 89 | 34 | plus fine qu'un recouvrement de $X$ par des ens. constructibles | No second reading securely proposed. | low |
| 91.pdf | 89 | 38 | a) | i) | low |
| 91.pdf | 89 | 40 | iii) | ii) | low |
| 91.pdf | 89 | 42 | iii) | No second reading securely proposed. | low |
| 91.pdf | 89 | 42 | morphisme | No second reading securely proposed. | low |
| 91.pdf | 91 | 10 | E_f | E_i | medium |
| 91.pdf | 91 | 10 | induite | No second reading securely proposed. | medium |
| 91.pdf | 91 | 14 | topologique | No second reading securely proposed. | medium |
| 91.pdf | 91 | 14 | l'argument | No second reading securely proposed. | medium |
| 91.pdf | 91 | 14 | ! | No second reading securely proposed. | medium |
| 91.pdf | 91 | 18 | un | No second reading securely proposed. | medium |
| 91.pdf | 91 | 18 | Affines si on veut | No second reading securely proposed. | low |
| 91.pdf | 91 | 20 | Évidem. | No second reading securely proposed. | medium |
| 91.pdf | 91 | 20 | inv. | No second reading securely proposed. | medium |
| 91.pdf | 93 | 5 | Prenons | No second reading securely proposed. | low |
| 91.pdf | 93 | 5 | en une réunion finie | No second reading securely proposed. | low |
| 91.pdf | 93 | 5 | et de $X_\alpha$ | No second reading securely proposed. | low |
| 91.pdf | 93 | 12 | Donc il est | No second reading securely proposed. | low |
| 91.pdf | 93 | 14 | morph. | No second reading securely proposed. | low |
| 91.pdf | 93 | 20 | ens | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | schématique | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | défini par | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | un | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | noethérien | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | quasi-séparé | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | pour | No second reading securely proposed. | low |
| 91.pdf | 93 | 25 | fini | No second reading securely proposed. | low |
| 91.pdf | 95 | 3 | prés. finie | quasi-fini | low |
| 91.pdf | 95 | 3 | prés. finie | quasi-fini | low |
| 91.pdf | 95 | 5 | cela implique | No second reading securely proposed. | low |
| 91.pdf | 95 | 5 | la définition | No second reading securely proposed. | low |
| 91.pdf | 95 | 5 | présentation finie | No second reading securely proposed. | low |
| 91.pdf | 95 | 9 | \mathbf Z | Z | low |
| 91.pdf | 96 | 17 | o | 0 | medium |
| 91.pdf | 96 | 17 | o | 0 | medium |
| 91.pdf | 96 | 17 | o | 0 | medium |
| 91.pdf | 96 | 17 | o | 0 | medium |
| 91.pdf | 96 | 17 | o | 0 | medium |
| 91.pdf | 96 | 19 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 96 | 21 | o | 0 | medium |
| 91.pdf | 97 | 19 | T_1 | T_i | medium |
| 91.pdf | 97 | 19 | i | \alpha | medium |
| 91.pdf | 97 | 25 | \operatorname{cons}X | No second reading securely proposed. | medium |
| 91.pdf | 97 | 37 | \coprod_\beta | \sum_\beta | medium |

## Checked readings that remain surprising

These are additional checks, not proposed repairs.

| File | Scan | Location | Reading | Alternative deliberately not supplied | Confidence |
|---|---|---|---|---|---|
| 91.pdf | 69 | First Hom computation | `(\mathfrak X,\underline W(T))`, with a transposition stroke | Reading only the inferred transposed order | high |
| 91.pdf | 70 | Last line | plain X; W without superscript a | Expected Gothic X or W^a | medium |
| 91.pdf | 73 | Local factorisation chain | plain X_i | Gothic target inferred from the argument | medium |
| 91.pdf | 87 | Final partition condition | no visible word finie | Adding finiteness from later criteria | high |
| 91.pdf | 88 | Exercise 5b | pour tout z in U; pi(z) nonzero | Adding z nonzero | high |
| 91.pdf | 88 | Exercise 6b pairing | primes on both arguments | Removing one prime to give a dual-basis formula | high |
| 91.pdf | 90 / 92 | Exercise 5 / exercise 3 | sl(V) / gl(V), respectively | Making the Lie-algebra names uniform | high |
| 91.pdf | 93 | Definition and later proof | Y_beta-alpha, later Y_alpha-beta | Uniformizing the index order | high |
| 91.pdf | 94 | Norm display | first bound <1; last bound ≤1 | Equalizing the two signs | high |
| 91.pdf | 97 | Transition condition and comparison | double implication; u_ij; right arrow with tilde | Reversing indices or replacing the clear arrow by an equality | high |
| 91.pdf | 98 | Proposition 25 | base de filtre sur E | Replacing E by the expected G | high |

## Abbreviations encountered

Expansions below are editorial suggestions in this register only. They do not expand the transcription.

| Written form | Suggested expansion / meaning |
|---|---|
| tt, tte, ttes | tout, toute, toutes, according to the actual form |
| pt | point |
| ens, ens., Ens | ensemble(s); category of sets when capitalized in a formula |
| Sch, Schs, sch., schém. | schéma(s), or schématique(s), according to context |
| présch | préschéma(s) |
| loc., loc. libre, loc. fermé | localement; localement libre; localement fermé |
| qu., qu-, quasi-cpt., qu. cpt, qu compt | quasi; quasi-compact |
| qu sép, quasi-sép. | quasi-séparé |
| géom. | géométriquement / géométrique |
| aff., affines | affine(s), where abbreviated |
| ss-, ss, ss-catégorie, s.-famille | sous-, sous-catégorie, sous-famille |
| ss-jacents | sous-jacents |
| covar. | covariant(e) |
| Hom, hom | homomorphisme(s), set/functor of morphisms |
| App cons, appl. constructibles, cons | applications constructibles; constructible-set functor notation |
| isom., isom | isomorphisme |
| imm., immers. | immersion |
| morph., morphisme | morphisme where abbreviated |
| Prop., prop., prop | proposition |
| Cor., Cor, cor. | corollaire |
| Th., th. | théorème |
| Pb | problème |
| N.B. | nota bene |
| i.e. | id est / c'est-à-dire |
| p. ex. | par exemple |
| resp. | respectivement |
| cf. | confer / voir |
| etc | et cetera; retained only where written |
| hyp. | hypothèse |
| tq. | tel que |
| ssi | si et seulement si |
| il faut et s. | il faut et il suffit |
| génér. | générateur(s) |
| coeffs. | coefficients |
| syst., syst. fond. | système, système fondamental |
| pet. fam. | petite famille (only an alternative reading on 82) |
| nb | nombre |
| noeth. | noethérien(ne) |
| rec. | recouvrement |
| quelc. | quelconque |
| ouv. | ouverte (cancelled on 78) |
| constr. | constructible(s) |
| prés. finie | présentation finie (uncertain cancelled reading on 95) |
| lim. | limite(s) |
| ét. | étale |
| Esp. vect. top. | espace vectoriel topologique |
| fini / finie in abbreviations | finite; ending is not standardized |
| comp. connexes | composantes connexes |
| mb | membre |
| chgt. | changement |
| ch. | unresolved abbreviation on 59; possibly champ/changement, no confident expansion |
| fais. / faisc. | faisceau(x), tentative on 67 / cancelled on 65 |
| comm. | commutatif / commutative |
| alg. | algèbre / algébrique; category suffix when used in Hom |
| Alg. | reference to Algèbre in the printed report |
| Chap., chap. | chapitre |
| exerc. | exercice |
| éd. | édition |
| mod. | modulo |
| pl. fid. | pleinement fidèle |
| inv. | inverse(s) |
| Évidem. | évidemment, tentative on 91 |
| cqf | likely cqfd / ce qu'il fallait démontrer; the final d was not supplied |
| n°, nᵒˢ | numéro, numéros |
| E.V.T. | Espaces vectoriels topologiques (suggested title abbreviation in the printed text) |
| l.c.q. / l.c.p. | unresolved abbreviation after Notons on 89; no responsible expansion |
| bis-bis / bis-idem | uncertain repetition shorthand on 71, not expanded |
| M with an overbar; = in prose | shorthand for même / même chose, depending on the phrase |

## Legibility and limits of trust

The typed faces are substantially more legible than the handwriting, but include torn edges, incomplete continuations and literal apparent errors. The handwritten main arguments are usually readable; dense cancellations, tiny additions, compressed word endings and sloping marginal notes are much less secure. The least trustworthy passages are the opening and final sentences of 59; cancelled text on 61–62; compressed wording on 67–68; the final expression on 70; the overwritten opening and third indices on 71–72; the boxed note on 75; the n(s) note and deleted text on 76; the clipped footnote on 77; the Greenberg margin on 79; the cancelled title on 81; the opening of 82; the boxed qualification on 84; and the heavily revised/angled text on 89, 93 and 95.

Every supplied whole image and both supplied halves were inspected in the first pass. All 38 retained pages were reread in the audit, with further crops, rotations or magnification for difficult passages. No OCR was used, and no page was delegated. Seven `\illegible` occurrences (ten estimated words in total) remain where the ink is obliterated or clipped after magnification; mathematical symbols instead receive tentative readings. The seven occurrences include the clipped final footnote on 77; their counts are estimates, not inferred missing sentences.

Drawings, boxes and connecting strokes are TikZ reconstructions. Their shape and relative arrangement are approximate, especially the overlapping cancelled arrows on 89 and the long marginal connection on 93; they should not be mistaken for facsimiles. Display spacing follows typesetting needs, and line breaks within prose paragraphs need not match the scan. The final inventory locates each text paragraph, displayed formula and markup element by its individual-fragment line, including nested insertions/deletions.

`records/doubts.jsonl`, `records/precontext_observations.md` and the earlier inventory are working history. They are superseded where this register or `records/visual_audit.md` records a changed reading. In particular, early guesses at reverse-side typewriting on 82 were removed once the actual printed face on 83 was read; printed material is transcribed once, on its supplied printed face. Those earlier guesses must not be treated as a second transcription.
