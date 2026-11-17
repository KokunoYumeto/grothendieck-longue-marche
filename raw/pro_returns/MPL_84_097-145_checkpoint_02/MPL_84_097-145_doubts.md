# Notation table

This table records the reading conventions used by the single transcriber. It is not a mathematical identification of differently written objects. Recurring signs were compared again after the second page-by-page reading and before the context archive was opened; differences that the ink does not settle remain in `\unsure`.

| Sign / use | LaTeX | Evidence / caution |
|---|---|---|
| Double quotation marks, including nested quotations | Two backticks and two apostrophes | Consistent throughout; a missing closing mark at a clipped edge is not supplied. Literal double quotes inside `\arrow` are TikZ syntax, not manuscript quotation marks. |
| Scalar sheaf, with underline when drawn | `\underline{\mathcal O}`, `\underline O`, `\mathcal O`, `O` | 97–107, 124, 134, 136; the different visible alphabets and underlining are retained, not globally normalized. |
| Cursive algebra and extension letters | `\mathcal A`, `\mathcal E`, `\mathcal H`, `\mathcal X` | Distinguished from plain `A`, `E`, `H`, `X`; especially 97–104, 121–122, 126–136. |
| Plain capital modules/algebras | `E,L,M,A,B,X,P,U,T,N` | The same letter can have different roles on different sheets; no role-based substitution was made. |
| Lowercase scalar ring and variables | `k`, `u`, `x`, `b`, `c`, `p`, `q`, `f` | Crowded `u/f`, `u/x`, and subscript `1/2/3` readings remain locally marked. |
| Gothic ideal | `\mathfrak a` | 120–121; the small ideal letter itself is doubtful at several occurrences. |
| Doubled-stem finite-field letter | `\mathbb F_2` | 116–117; the raised 3 denotes the three-coordinate group. |
| Phi and psi families | `\varphi`, `\phi` where present, `\psi`, `\Phi`, `\Psi` | Lowercase/uppercase distinction retained; 136–138 contain especially compressed capital Psi forms. |
| Splitting coefficient versus auxiliary scalar | `\chi` versus `\gamma` | Compared across 100, 126, 128–144; the relation `\gamma\chi=2` on 142 has two different glyphs. |
| Group letter | `\unsure{\gamma|\Gamma}` or the local first reading | 116–121; small/capital gamma cannot always be distinguished securely. |
| Projection and bent companion | `\pi`, `\varpi` | 99, 124, 128: `\overline T` and `\overline\omega` alternatives are retained where the strokes do not decide. |
| Involution/bar | `\sigma`, `\bar x`, `\bar\xi`, `\overline{...}` | Bar scope follows the drawn stroke. A doubtful bar scope is explicitly marked, notably 108. |
| Bent superscript on the invariant/trace construction | `^{\unsure{\natural}}`; first occurrence has `\natural|\flat` | 102–104; this is a doubtful glyph, not an imported conventional notation. |
| Trace letters | `t`, `T`, `\operatorname{Tr}` | Kept distinct, including the changes within 114–115. `T_i` is not silently changed to `\sigma_i`. |
| Norm letters | `n`, `N` | Case retained; overwritten capitalization in 108 is marked. |
| Dual marker | `^\vee` | V-shaped superscript, beginning 97; separate from the binary `\vee` construction. |
| Contracted product / alternative construction | `*`, `\wedge`, `\vee` | Kept distinct when visible. Doubt between wedge and vee remains on 134 and 144. |
| Tensor kernel and quotient | `\otimes_0`, `\otimes^0` | Subscript/superscript placement preserved, especially 99–101 and 142. |
| Amalgamated sum | `\amalg_{\underline{\mathcal O}}` | Clear standalone symbol on 101; overwritten sum/coproduct readings elsewhere remain `\unsure{\oplus|\amalg}` in their observed order. |
| Exclamation exponent | `^!` or `^{!}` | Dotted marks confirmed individually in `Hom` on 134 and 136 and in the restriction symbols on 144. The late `x_1` mark on 144 remains `\unsure{x^!_1|x'_1}`. |
| Prime, double prime, triple prime | `'`, `''`, `^{\prime\prime\prime}` | Splitting changes on 124–134 and partial maps on 142; enlarged bracket expressions on 136 show primes without dots, including the prime outside each bracket. |
| Exclamation attached to a claim | `\overset{!}{=}`, literal `!`, or the locally written form | Kept separate from exclamation exponents; examples on 115, 128, 138 and degree labels on 122. |
| Headless connecting stroke | `\mathrel{-\!\!-\!\!-}` or TikZ `no head` | Used wherever no head is visible; not upgraded to an arrow because a map would be expected. Ambiguous heads are marked locally. |
| Arrow direction / double arrow | TikZ directions and `leftrightarrow`, `Rightarrow`, `hook`, `mapsto` | 101 central direction remains doubtful; 115 has asymmetric drawn permutation arrows; 142's enlarged dashed diagonal has heads at both ends. |
| Equality, equivalence and inclusion | `=`, `\equiv`, `\subset`, `\simeq`, `\sim` | No mathematical normalization; on 124 the three-stroke relation is first read as `\equiv`, with `=` as alternative. |
| Underlining | `\uline`, `\uuline`; mathematical underlines where the notation itself uses them | Single/double strokes and their extent are retained, including the minus sign in the double-underlined `-b_i` on 128. |
| Square grouping strokes and small pointers | TikZ in `\figure` or `\diagram` | 97, 106, 113, 140 and 144; square arches are drawn as square strokes rather than changed to curly braces. |
| Raised typed note references | `({}^{106}1)`, `({}^{107})`, `({}^{108})`, `({}^{108}1)` | 129, 131, 139, 145; the trailing 1 on 129 and 145 is on the baseline, not a subscript. |
| Printed and handwritten page numbers | Separate `\mspage{...}` markers | Typed 465–474 and 480 coexist with handwritten foliation; markers stay where visible on the page. |
| Abbreviations | Literal manuscript forms | See the glossary below; proposed expansions never enter the transcription. |

# Doubts

Every `\unsure` and `\illegible` occurrence in the audited page files is listed below, including repeated occurrences and uncertainty inside cancelled material. Line numbers refer to the individual `.tex` fragment, not to manuscript lineation; the file column makes each occurrence findable. “Medium” means a tentative single reading; “low” means unresolved alternatives or unreadable ink, and is not a measured probability. The register does not convert a missing right-edge letter into a confident reconstructed word.


| File | Cote | Scan | Approximate TeX line / occurrence | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|---|
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 7; occurrence 1 | `signe` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 17; occurrence 1 | `1 unreadable word(s)` | No secure reading after enlargement | low |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 28; occurrence 1 | `x` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 29; occurrence 1 | `l'on a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 30; occurrence 1 | `quo` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 31; occurrence 1 | `signe` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 43; occurrence 1 | `\operatorname{Quad}(E)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 43; occurrence 2 | `\simeq` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 43; occurrence 3 | `\mathcal A^{\otimes2}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 45; occurrence 1 | `\varphi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 45; occurrence 2 | `correspondent` | `correspondant` | low |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 46; occurrence 1 | `lorsque` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 46; occurrence 2 | `truc du type` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 46; occurrence 3 | `dans` | No secure alternative | medium |
| `MPL_84_097-145_84_scan097.tex` | 84 | 97 | TeX line 47; occurrence 1 | `OS` | `on` | low |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 9; occurrence 1 | `x` | No secure alternative | medium |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 13; occurrence 1 | `\lambda^2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 13; occurrence 2 | `+` | No secure alternative | medium |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 13; occurrence 3 | `-` | No secure alternative | medium |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 19; occurrence 1 | `On donne un sens aux deux symboles pour : l'argument $N$ variable` | No secure alternative | medium |
| `MPL_84_097-145_84_scan098.tex` | 84 | 98 | TeX line 19; occurrence 2 | `inut.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 2; occurrence 1 | `\otimes` | `\simeq` | low |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 17; occurrence 1 | `\mathrm{proj}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 20; occurrence 1 | `hom` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 22; occurrence 1 | `L_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 22; occurrence 2 | `E_1\otimes L_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 23; occurrence 1 | `\cap` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 25; occurrence 1 | `\chi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 26; occurrence 1 | `E` | No secure alternative | medium |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 34; occurrence 1 | `\overline T_1` | `\varpi_1` | low |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 34; occurrence 2 | `\overline T_2` | `\varpi_2` | low |
| `MPL_84_097-145_84_scan099.tex` | 84 | 99 | TeX line 39; occurrence 1 | `\overline T_2` | `\varpi_2` | low |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 2; occurrence 1 | `\chi` | `\gamma` | low |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 2; occurrence 2 | `P` | No secure alternative | medium |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 4; occurrence 1 | `*` | `\wedge` | low |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 16; occurrence 1 | `P_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 16; occurrence 2 | `type` | No secure alternative | medium |
| `MPL_84_097-145_84_scan100.tex` | 84 | 100 | TeX line 32; occurrence 1 | `les conditions` | `la condition` | low |
| `MPL_84_097-145_84_scan101.tex` | 84 | 101 | TeX line 5; occurrence 1 | `\oplus` | `\amalg` | low |
| `MPL_84_097-145_84_scan101.tex` | 84 | 101 | TeX line 5; occurrence 2 | `\uparrow` | `\downarrow` | low |
| `MPL_84_097-145_84_scan101.tex` | 84 | 101 | TeX line 24; occurrence 1 | `\varphi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 3; occurrence 1 | `\natural` | `\flat` | low |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 3; occurrence 2 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 6; occurrence 1 | `supposant` | `supprimant` | low |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 6; occurrence 2 | `\chi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 9; occurrence 1 | `\overline T_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 10; occurrence 1 | `\overline T_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 19; occurrence 1 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 19; occurrence 2 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 19; occurrence 3 | `^{\natural}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 23; occurrence 1 | `la structure` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 25; occurrence 1 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 35; occurrence 1 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 36; occurrence 1 | `En tant que telle` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 36; occurrence 2 | `définie` | No secure alternative | medium |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 38; occurrence 1 | `rev. quad.` | `rev. qu. ét.` | low |
| `MPL_84_097-145_84_scan102.tex` | 84 | 102 | TeX line 39; occurrence 1 | `etc.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 2; occurrence 1 | `vaut` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 4; occurrence 1 | `e` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 6; occurrence 1 | `chute` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 6; occurrence 2 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 8; occurrence 1 | `-` | `+` | low |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 10; occurrence 1 | `donc` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 16; occurrence 1 | `\mathrel{-\!\!-\!\!-}` | `\longrightarrow` | low |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 18; occurrence 1 | `remonté` | `remontée` | low |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 25; occurrence 1 | `autres` | No secure alternative | medium |
| `MPL_84_097-145_84_scan103.tex` | 84 | 103 | TeX line 35; occurrence 1 | `peut écrire` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 2; occurrence 1 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 2; occurrence 2 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 4; occurrence 1 | `\natural` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 7; occurrence 1 | `U_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 36; occurrence 1 | `\otimes U_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 37; occurrence 1 | `joue` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 37; occurrence 2 | `rôle` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 37; occurrence 3 | `trace` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 37; occurrence 4 | `en disposant des` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 40; occurrence 1 | `x_1*` | No secure alternative | medium |
| `MPL_84_097-145_84_scan104.tex` | 84 | 104 | TeX line 43; occurrence 1 | `\oplus` | `\amalg` | low |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 4; occurrence 1 | `alors` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 6; occurrence 1 | `\tau` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 8; occurrence 1 | `\oplus_{\underline O}` | `\amalg_{\underline O}` | low |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 13; occurrence 1 | `\overline{\operatorname{Tr}(\xi)}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 14; occurrence 1 | `\sigma_A` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 15; occurrence 1 | `_{A_1\otimes_{\underline O}A_2}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 16; occurrence 1 | ``` ``un hom. trace''``` | `un hom. trace` | low |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 21; occurrence 1 | `tendance` | No secure alternative | medium |
| `MPL_84_097-145_84_scan105.tex` | 84 | 105 | TeX line 21; occurrence 2 | `est` | No secure alternative | medium |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 13; occurrence 1 | `\varphi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 21; occurrence 1 | `A_2` | `A_1` | low |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 25; occurrence 1 | `Noter` | No secure alternative | medium |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 41; occurrence 1 | `\xi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 43; occurrence 1 | `constate` | No secure alternative | medium |
| `MPL_84_097-145_84_scan106.tex` | 84 | 106 | TeX line 43; occurrence 2 | `ait` | `a` | low |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 4; occurrence 1 | `!` | No secure alternative | medium |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 10; occurrence 1 | `soit` | No secure alternative | medium |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 16; occurrence 1 | `A_1\ A_1,O` | No secure alternative | medium |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 16; occurrence 2 | `en oubliant la` | No secure alternative | medium |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 16; occurrence 3 | `sur` | No secure alternative | medium |
| `MPL_84_097-145_84_scan107.tex` | 84 | 107 | TeX line 32; occurrence 1 | `c'est` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 2; occurrence 1 | `en termes de $t$ par $\tau$` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 6; occurrence 1 | `N` | `n` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 10; occurrence 1 | `Posons` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 10; occurrence 2 | `Posons` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 12; occurrence 1 | `c` | `b` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 17; occurrence 1 | `On veut que cette application soit` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 26; occurrence 1 | `on a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 41; occurrence 1 | `comb. lin.` | `cond. lin.` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 42; occurrence 1 | `en car.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 46; occurrence 1 | `ci-dessous` | `ci-dessus` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 46; occurrence 2 | `(de $2^\circ$)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 46; occurrence 3 | `ci-dessus` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 46; occurrence 4 | `qui` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 50; occurrence 1 | `N` | `n` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 54; occurrence 1 | `\overline{n(x)}` | `n(\bar x)` | low |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 57; occurrence 1 | `mais en` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 57; occurrence 2 | `voudra que` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 59; occurrence 1 | `3^\circ)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 63; occurrence 1 | `t(x)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan108.tex` | 84 | 108 | TeX line 65; occurrence 1 | `t(x)^2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan109.tex` | 84 | 109 | TeX line 4; occurrence 1 | `d'où` | No secure alternative | medium |
| `MPL_84_097-145_84_scan109.tex` | 84 | 109 | TeX line 10; occurrence 1 | `\alpha(x\bar x)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan109.tex` | 84 | 109 | TeX line 18; occurrence 1 | `\alpha t` | No secure alternative | medium |
| `MPL_84_097-145_84_scan109.tex` | 84 | 109 | TeX line 34; occurrence 1 | `2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan109.tex` | 84 | 109 | TeX line 34; occurrence 2 | `alors on supposera` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 4; occurrence 1 | `\alpha` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 7; occurrence 1 | `\nu` | `\gamma` | low |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 9; occurrence 1 | `est` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 24; occurrence 1 | `ici` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 30; occurrence 1 | `dans` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 35; occurrence 1 | `si` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 43; occurrence 1 | `poursuivre l'étude de la` | No secure alternative | medium |
| `MPL_84_097-145_84_scan110.tex` | 84 | 110 | TeX line 43; occurrence 2 | `bi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 11; occurrence 1 | `notera` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 15; occurrence 1 | `\bar a=\tau_i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 16; occurrence 1 | `abus de` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 25; occurrence 1 | `T_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 25; occurrence 2 | `T_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 26; occurrence 1 | `A_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 36; occurrence 1 | `T_i` | `\overline T_i` | low |
| `MPL_84_097-145_84_scan111.tex` | 84 | 111 | TeX line 41; occurrence 1 | `1` | `3` | low |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 7; occurrence 1 | `raisonnablement bien` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 7; occurrence 2 | `soit déduit` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 8; occurrence 1 | `on ne suppose ni les $A_i$ ni $A/A_i$` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 8; occurrence 2 | `engendrent $A$` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 14; occurrence 1 | `exige` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 16; occurrence 1 | `T_1` | `T_2` | low |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 22; occurrence 1 | `\alpha_1(x)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 29; occurrence 1 | `\alpha_2(a_2)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan112.tex` | 84 | 112 | TeX line 29; occurrence 2 | `\alpha_2(a_2)^2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 4; occurrence 1 | `N` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 10; occurrence 1 | `\alpha_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 10; occurrence 2 | `x_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 10; occurrence 3 | `2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 20; occurrence 1 | `x\bar y` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 21; occurrence 1 | `\alpha_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan113.tex` | 84 | 113 | TeX line 27; occurrence 1 | `n` | `n_1` | low |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 8; occurrence 1 | `la sous-algèbre` | No secure alternative | medium |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 19; occurrence 1 | `1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 27; occurrence 1 | `apparemment` | No secure alternative | medium |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 27; occurrence 2 | `mais` | No secure alternative | medium |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 38; occurrence 1 | `*` | No secure alternative | medium |
| `MPL_84_097-145_84_scan114.tex` | 84 | 114 | TeX line 42; occurrence 1 | `vérifiée` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 3; occurrence 1 | `Sous réserve` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 5; occurrence 1 | `\alpha_2T_2(x)\alpha_3T_3(x)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 13; occurrence 1 | `N` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 16; occurrence 1 | `se prouvent` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 20; occurrence 1 | `T_1` | `\sigma_1` | low |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 20; occurrence 2 | `T_2` | `\sigma_2` | low |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 20; occurrence 3 | `T_3` | `\sigma_3` | low |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 26; occurrence 1 | `\longrightarrow` | `\longleftrightarrow` | low |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 32; occurrence 1 | `n_1` | `N_1` | low |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 32; occurrence 2 | `x\sigma_2(x\sigma_1(x))` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 35; occurrence 1 | `x_1^2n_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan115.tex` | 84 | 115 | TeX line 38; occurrence 1 | `T` | No secure alternative | medium |
| `MPL_84_097-145_84_scan116.tex` | 84 | 116 | TeX line 6; occurrence 1 | `Via` | No secure alternative | medium |
| `MPL_84_097-145_84_scan116.tex` | 84 | 116 | TeX line 15; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan116.tex` | 84 | 116 | TeX line 15; occurrence 2 | `=` | No secure alternative | medium |
| `MPL_84_097-145_84_scan116.tex` | 84 | 116 | TeX line 20; occurrence 1 | `Donc` | No secure alternative | medium |
| `MPL_84_097-145_84_scan116.tex` | 84 | 116 | TeX line 20; occurrence 2 | `en` | No secure alternative | medium |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 2; occurrence 1 | `là` | No secure alternative | medium |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 2; occurrence 2 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 6; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 12; occurrence 1 | `à` | No secure alternative | medium |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 14; occurrence 1 | `\wedge` | `*` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 24; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 25; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 29; occurrence 1 | `2` | `3` | low |
| `MPL_84_097-145_84_scan117.tex` | 84 | 117 | TeX line 29; occurrence 2 | `i.e.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan118.tex` | 84 | 118 | TeX line 6; occurrence 1 | `prouver` | No secure alternative | medium |
| `MPL_84_097-145_84_scan118.tex` | 84 | 118 | TeX line 6; occurrence 2 | `l'on a un hom` | `c'est un hom` | low |
| `MPL_84_097-145_84_scan118.tex` | 84 | 118 | TeX line 9; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan118.tex` | 84 | 118 | TeX line 15; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan118.tex` | 84 | 118 | TeX line 19; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 4; occurrence 1 | `T_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 4; occurrence 2 | `x` | `a` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 4; occurrence 3 | `x` | `a` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 4; occurrence 4 | `x` | `a` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 8; occurrence 1 | `x` | No secure alternative | medium |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 12; occurrence 1 | `x` | `a` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 12; occurrence 2 | `a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 18; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 21; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 23; occurrence 1 | `standart` | `standard` | low |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 27; occurrence 1 | `donc` | No secure alternative | medium |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 27; occurrence 2 | `fini` | No secure alternative | medium |
| `MPL_84_097-145_84_scan119.tex` | 84 | 119 | TeX line 28; occurrence 1 | `I` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 2; occurrence 1 | `twistée` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 2; occurrence 2 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 4; occurrence 1 | `OPS` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 4; occurrence 2 | `constante` | `constants` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 10; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 12; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 14; occurrence 1 | `X_J` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 14; occurrence 2 | `X_J` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 18; occurrence 1 | `j` | `j_0` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 18; occurrence 2 | `j` | `j_0` | low |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 18; occurrence 3 | `\mathfrak a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan120.tex` | 84 | 120 | TeX line 18; occurrence 4 | `inv.` | `action` | low |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 2; occurrence 1 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 2; occurrence 2 | `\gamma` | `\Gamma` | low |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 2; occurrence 3 | `\mathfrak a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 2; occurrence 4 | `\mathfrak a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 4; occurrence 1 | `k` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 4; occurrence 2 | `X_J` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 4; occurrence 3 | `X_J` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 6; occurrence 1 | `\mathfrak a` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 6; occurrence 2 | `pour` | `puis` | low |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 11; occurrence 1 | `X` | `\mathcal X` | low |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 14; occurrence 1 | `\subset` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 16; occurrence 1 | `p.r.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 16; occurrence 2 | `X_i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan121.tex` | 84 | 121 | TeX line 22; occurrence 1 | `de fait` | `de suite` | low |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 6; occurrence 1 | `où` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 6; occurrence 2 | `revêts` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 17; occurrence 1 | `\pi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 23; occurrence 1 | `\alpha_1,\alpha_2,\alpha_3` | `x_1,x_2,x_3` | low |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 23; occurrence 2 | `\alpha_1\wedge\alpha_2\wedge\alpha_3` | `x_1\wedge x_2\wedge x_3` | low |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 25; occurrence 1 | `Une` | `La` | low |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 27; occurrence 1 | `?` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 27; occurrence 2 | `\operatorname{Tr}_1,N_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 28; occurrence 1 | `pas univ. inj.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 31; occurrence 1 | `\wedge` | `*` | low |
| `MPL_84_097-145_84_scan122.tex` | 84 | 122 | TeX line 31; occurrence 2 | `\wedge` | `*` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 3; occurrence 1 | `\varpi` | `\overline\omega` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 4; occurrence 1 | `\varpi'` | `\overline\omega'` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 7; occurrence 1 | `\equiv` | `=` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 10; occurrence 1 | `\beta` | `\alpha` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 10; occurrence 2 | `\equiv` | `=` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 10; occurrence 3 | `\operatorname{id}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 10; occurrence 4 | `\operatorname{id}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 11; occurrence 1 | `\equiv` | `=` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 14; occurrence 1 | `-\varpi'` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 17; occurrence 1 | `1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 21; occurrence 1 | `E'_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 21; occurrence 2 | `*` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 22; occurrence 1 | `E'_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 26; occurrence 1 | `x_1` | `u_1` | low |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 26; occurrence 2 | `\varphi'_2(u_2)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 26; occurrence 3 | `\pi'_1\beta_1(x_1)\otimes\alpha'_2(\alpha_2(u_2))` | No secure alternative | medium |
| `MPL_84_097-145_84_scan124.tex` | 84 | 124 | TeX line 27; occurrence 1 | `x_1` | `u_2` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 3; occurrence 1 | `exacerbatic` | `exacerbation` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 4; occurrence 1 | `culturelte` | `culturelle` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 5; occurrence 1 | `le` | `les` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 7; occurrence 1 | `dénou` | `dénoue-` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 10; occurrence 1 | `aur` | `aura` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 11; occurrence 1 | `po` | `pour` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 19; occurrence 1 | `quelqu` | `quelques` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 20; occurrence 1 | `pr` | `pro-` | low |
| `MPL_84_097-145_84_scan125.tex` | 84 | 125 | TeX line 38; occurrence 1 | `structuran` | `structurant` | low |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 8; occurrence 1 | `i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 8; occurrence 2 | `+` | `-` | low |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 11; occurrence 1 | `-` | `+` | low |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 16; occurrence 1 | `scindées` | No secure alternative | medium |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 23; occurrence 1 | `Je dis qu'il est fonctoriel pour les` | No secure alternative | medium |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 24; occurrence 1 | `scindées` | No secure alternative | medium |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 26; occurrence 1 | `M'_i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan126.tex` | 84 | 126 | TeX line 29; occurrence 1 | `E^{\prime\prime\prime}_i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan127.tex` | 84 | 127 | TeX line 19; occurrence 1 | `pui` | `puis-` | low |
| `MPL_84_097-145_84_scan127.tex` | 84 | 127 | TeX line 31; occurrence 1 | `jusqu'a` | `jusqu'au` | low |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 4; occurrence 1 | `\varpi_i` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 11; occurrence 1 | `\chi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 23; occurrence 1 | `-` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 29; occurrence 1 | `\simeq` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 36; occurrence 1 | `p.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 37; occurrence 1 | `+` | `-` | low |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 38; occurrence 1 | `tr` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 38; occurrence 2 | `\varphi` | `\chi` | low |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 39; occurrence 1 | `Si` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 41; occurrence 1 | `=` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 43; occurrence 1 | `\gamma` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 43; occurrence 2 | `on peut` | No secure alternative | medium |
| `MPL_84_097-145_84_scan128.tex` | 84 | 128 | TeX line 43; occurrence 3 | `v` | No secure alternative | medium |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 5; occurrence 1 | `avoi` | `avoir` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 12; occurrence 1 | `mie` | `mieux` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 21; occurrence 1 | `un` | `uni-` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 22; occurrence 1 | `doig` | `doigt` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 23; occurrence 1 | `questio` | `question` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 25; occurrence 1 | `avo` | `avoir` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 26; occurrence 1 | `arithme` | `arithmé-` | low |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 30; occurrence 1 | `comme` | No secure alternative | medium |
| `MPL_84_097-145_84_scan129.tex` | 84 | 129 | TeX line 32; occurrence 1 | `potentie` | `potentiel-` | low |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 9; occurrence 1 | `donné` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 26; occurrence 1 | `comp.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 28; occurrence 1 | `\simeq 0` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 28; occurrence 2 | `T_{-U}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 28; occurrence 3 | `\Theta_{p,p'}` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 31; occurrence 1 | `p` | `\rho` | low |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 34; occurrence 1 | `\eta` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 45; occurrence 1 | `b'_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 45; occurrence 2 | `b_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 51; occurrence 1 | `+` | `-` | low |
| `MPL_84_097-145_84_scan130.tex` | 84 | 130 | TeX line 57; occurrence 1 | `\eta` | No secure alternative | medium |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 6; occurrence 1 | `circons` | `circons-` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 11; occurrence 1 | `aîné` | `aînée` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 15; occurrence 1 | `d'une` | No secure alternative | medium |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 17; occurrence 1 | `qu'il` | `qu'ils` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 20; occurrence 1 | `;` | `,` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 22; occurrence 1 | `cett` | `cette` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 28; occurrence 1 | `passaien` | `passaient` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 29; occurrence 1 | `:` | No secure alternative | medium |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 35; occurrence 1 | `tou` | `tout.` | low |
| `MPL_84_097-145_84_scan131.tex` | 84 | 131 | TeX line 42; occurrence 1 | `Le.massacre` | `Le massacre` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 4; occurrence 1 | `p(x)` | `\psi(x)` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 11; occurrence 1 | `p''_3` | `p''_2` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 12; occurrence 1 | `p''_3` | `p''_2` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 34; occurrence 1 | `+` | `-` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 62; occurrence 1 | `U_2` | `U'_2` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 74; occurrence 1 | `U` | `b` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 75; occurrence 1 | `b_2` | `U'_2` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 81; occurrence 1 | `b` | `U` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 85; occurrence 1 | `U_1` | `U''_1` | low |
| `MPL_84_097-145_84_scan132.tex` | 84 | 132 | TeX line 91; occurrence 1 | `U` | `b` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 4; occurrence 1 | `conflit` | No secure alternative | medium |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 7; occurrence 1 | `qu'en` | `qu'en-` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 9; occurrence 1 | `vrai` | `vrai-` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 12; occurrence 1 | `to` | `tout` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 13; occurrence 1 | `an` | `ans` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 23; occurrence 1 | `.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 35; occurrence 1 | `;` | No secure alternative | medium |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 36; occurrence 1 | `a c c e p t` | `a c c e p t é` | low |
| `MPL_84_097-145_84_scan133.tex` | 84 | 133 | TeX line 38; occurrence 1 | `.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 3; occurrence 1 | `\wedge` | `\vee` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 3; occurrence 2 | `-` | `+` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 8; occurrence 1 | `T_U` | `\Lambda_U` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 8; occurrence 2 | `\eta` | `\zeta` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 8; occurrence 3 | `\zeta` | `\xi` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 17; occurrence 1 | `+` | `-` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 18; occurrence 1 | `p'_i` | `p'_2` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 18; occurrence 2 | `+` | `-` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 22; occurrence 1 | `L_2` | `L_1` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 25; occurrence 1 | `+` | `-` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 28; occurrence 1 | `+` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 30; occurrence 1 | `b_2` | `b_1` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 33; occurrence 1 | `qui doit` | `qui où le` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 33; occurrence 2 | `pourtant être` | `produit être` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 34; occurrence 1 | `étrange` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 38; occurrence 1 | `dûs` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 38; occurrence 2 | `non` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 41; occurrence 1 | `R` | `\sim` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 50; occurrence 1 | `\lambda\operatorname{Hom}` | `\lambda` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 53; occurrence 1 | `qui a le` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 53; occurrence 2 | `val.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 56; occurrence 1 | `\alpha` | `a` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 59; occurrence 1 | `\eta` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 72; occurrence 1 | `U'` | `U'_0` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 74; occurrence 1 | `\sim` | No secure alternative | medium |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 80; occurrence 1 | `soit` | `c'est` | low |
| `MPL_84_097-145_84_scan134.tex` | 84 | 134 | TeX line 80; occurrence 2 | `trouvée` | No secure alternative | medium |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 6; occurrence 1 | `pulsion` | `pulsions` | low |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 7; occurrence 1 | `.` | No secure alternative | medium |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 12; occurrence 1 | `méttais` | `mettais` | low |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 16; occurrence 1 | `inconditionnelle` | No secure alternative | medium |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 17; occurrence 1 | `roses` | `coses` | low |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 22; occurrence 1 | `ambiguité` | `ambiguïté` | low |
| `MPL_84_097-145_84_scan135.tex` | 84 | 135 | TeX line 40; occurrence 1 | `j` | `je` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 7; occurrence 1 | `x` | No secure alternative | medium |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 17; occurrence 1 | `\Psi_1(f_1)[` | `[\Psi_1(f_1)` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 19; occurrence 1 | `\Psi_2 f_2` | `\Psi_2(f_2)` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 26; occurrence 1 | `U_2` | `f_2` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 27; occurrence 1 | `U_2` | `f_2` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 51; occurrence 1 | `x_1` | `u_1` | low |
| `MPL_84_097-145_84_scan136.tex` | 84 | 136 | TeX line 51; occurrence 2 | `x_2` | `u_2` | low |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 18; occurrence 1 | `:` | No secure alternative | medium |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 21; occurrence 1 | `de` | `des` | low |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 23; occurrence 1 | `C'étai` | `C'était` | low |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 25; occurrence 1 | `peut-êtr` | `peut-être` | low |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 26; occurrence 1 | `pas` | No secure alternative | medium |
| `MPL_84_097-145_84_scan137.tex` | 84 | 137 | TeX line 27; occurrence 1 | `comme` | No secure alternative | medium |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 9; occurrence 1 | `\lambda_2+` | No secure alternative | medium |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 11; occurrence 1 | `E_1` | `E_2` | low |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 19; occurrence 1 | `Si on` | No secure alternative | medium |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 25; occurrence 1 | `)` | No secure alternative | medium |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 33; occurrence 1 | `u_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 38; occurrence 1 | `\Psi_1(x_1)` | `\psi_1(x_1)` | low |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 50; occurrence 1 | `\psi(x)y` | `y(x)\psi` | low |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 51; occurrence 1 | `T` | `\pi` | low |
| `MPL_84_097-145_84_scan138.tex` | 84 | 138 | TeX line 51; occurrence 2 | `x` | No secure alternative | medium |
| `MPL_84_097-145_84_scan139.tex` | 84 | 139 | TeX line 15; occurrence 1 | `destructio` | `destruction` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 8; occurrence 1 | `\pi` | `\alpha` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 9; occurrence 1 | `\lambda_1` | `\lambda` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 12; occurrence 1 | `q` | No secure alternative | medium |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 17; occurrence 1 | `q(m_1)` | `q_1(m_1)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 17; occurrence 2 | `q(m_2)` | `q_2(m_2)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 21; occurrence 1 | `x_1*x_2` | `x_1\otimes x_2` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 23; occurrence 1 | `q(m_1)` | `q_1(m_1)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 23; occurrence 2 | `q(m_2)` | `q_2(m_2)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 27; occurrence 1 | `q(m_1)` | `q_1(m_1)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 28; occurrence 1 | `q(m_2)` | `q_2(m_2)` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 38; occurrence 1 | `\chi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 44; occurrence 1 | `x_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 51; occurrence 1 | `=` | `\in` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 53; occurrence 1 | `\lambda_2\chi` | `\chi\lambda_2` | low |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 54; occurrence 1 | `\chi` | No secure alternative | medium |
| `MPL_84_097-145_84_scan140.tex` | 84 | 140 | TeX line 72; occurrence 1 | `f` | No secure alternative | medium |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 2; occurrence 1 | `Blan` | `Blan-` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 16; occurrence 1 | `rejoind` | `rejoindre` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 22; occurrence 1 | `attachant` | `attachants` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 31; occurrence 1 | `ensuit` | `ensuite` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 32; occurrence 1 | `mo` | `mon` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 33; occurrence 1 | `d'ex` | `d'exa-` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 37; occurrence 1 | `confor` | `confor-` | low |
| `MPL_84_097-145_84_scan141.tex` | 84 | 141 | TeX line 39; occurrence 1 | `fall` | `fallu` | low |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 3; occurrence 1 | `avec` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 5; occurrence 1 | `Concentrons` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 5; occurrence 2 | `\longrightarrow` | `\mathrel{-\!\!-\!\!-}` | low |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 7; occurrence 1 | `être` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 23; occurrence 1 | `E_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 41; occurrence 1 | `x_1\otimes x_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 51; occurrence 1 | `donnée` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 51; occurrence 2 | `équivaut` | No secure alternative | medium |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 51; occurrence 3 | `involution` | `involutive` | low |
| `MPL_84_097-145_84_scan142.tex` | 84 | 142 | TeX line 51; occurrence 4 | `qui induit` | No secure alternative | medium |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 4; occurrence 1 | `honneu` | `honneur` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 6; occurrence 1 | `ressurgis` | `ressurgis-` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 6; occurrence 2 | `choses` | `choses.` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 6; occurrence 3 | `ce` | `cet-` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 6; occurrence 4 | `en` | `en-` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 12; occurrence 1 | `pou` | `pour` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 12; occurrence 2 | `su` | `sur-` | low |
| `MPL_84_097-145_84_scan143.tex` | 84 | 143 | TeX line 12; occurrence 3 | `guèr` | `guère` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 3; occurrence 1 | `*` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 6; occurrence 1 | `\wedge` | `\vee` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 12; occurrence 1 | `u_i` | `f_i` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 14; occurrence 1 | `u_i` | `f_i` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 14; occurrence 2 | `u^!_i` | `f^!_i` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 31; occurrence 1 | `E_1\otimes E_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 40; occurrence 1 | `f(x_1` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 43; occurrence 1 | `f_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 46; occurrence 1 | `L_1` | `B_1` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 59; occurrence 1 | `L_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 61; occurrence 1 | `\chi f_1\otimes f_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 61; occurrence 2 | `f^!_1f^!_2` | `f^!_1\otimes f^!_2` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 70; occurrence 1 | `f_1(` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 77; occurrence 1 | `x^!_1` | `x'_1` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 80; occurrence 1 | `\lambda_2` | `\lambda_1` | low |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 80; occurrence 2 | `\lambda_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 84; occurrence 1 | `\lambda_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 87; occurrence 1 | `f_1(f^!_1(x_1)\otimes u_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 87; occurrence 2 | `\longrightarrow` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 90; occurrence 1 | `\lambda_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan144.tex` | 84 | 144 | TeX line 90; occurrence 2 | `\lambda_2u_2` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 1 | `à` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 2 | `ave` | `avec` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 3 | `mépris` | `mépris,` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 4 | `intellec` | `intellec-` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 5 | `ré` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 6 | `de` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 7 | `a` | `aus-` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 8 | `Mais` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 4; occurrence 9 | `-` | ` ` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 6; occurrence 1 | `dire` | No secure alternative | medium |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 6; occurrence 2 | `armes` | `armes.` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 8; occurrence 1 | `t r a i t` | `t r a i t s` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 8; occurrence 2 | `inverstis` | `inverstis-` | low |
| `MPL_84_097-145_84_scan145.tex` | 84 | 145 | TeX line 14; occurrence 1 | `107` | `109` | low |

# Abbreviations

These expansions are editorial suggestions in English/French for this glossary only. Punctuation and lack of punctuation remain as written in the transcription; an uncertain abbreviation remains uncertain there.

| Written form(s) | Proposed expansion / meaning | Caution |
|---|---|---|
| `alg.`, `alg`, `k.alg` | algèbre / algebra over k | Context distinguishes the algebra from its underlying module. |
| `appl.`, `applic.` | application | |
| `ass.` | associée | Usually the associated bilinear form. |
| `autom.`, `autom` | automorphisme | |
| `bil.` | bilinéaire | |
| `can.`, `inc`, `inj` | canonique, inclusion, injection | Diagram abbreviations are not expanded. |
| `car.` | caractéristique | Especially characteristic 2. |
| `cf.` | confer / compare | |
| `chgt.` | changement | Change of base. |
| `coeff.` | coefficient(s) | |
| `comb. lin.`, doubtful `cond. lin.` | combinaison linéaire / condition linéaire | The first part on 108 is not securely read. |
| `comm.` | commutatif / commutativité | The wording on 134 includes a doubtful `non`; it was not made commutative by interpretation. |
| `comp.` | compatible | Doubtful abbreviation in the trivialisation on 130. |
| `cond.` | condition | |
| `def`, `déf` | définition / by definition | Superscript over an equality. |
| `diag.` | diagramme | |
| `e.g.` | exempli gratia / for example | |
| `endom` | endomorphisme | 144. |
| `ens.` | ensemble | |
| `ét.` | étale | |
| `etc.` | et cetera | Present only where written. |
| `Ex` | exemple | Underlined on 144; the following attempt is unfinished. |
| `ext.` | extension | |
| `hom`, `hom.` | homomorphisme | |
| `Hom` | homomorphisms | A named mathematical object; `Hom^!` is separately preserved. |
| `i.e.` | id est / c'est-à-dire | |
| `id` | identité | A map label, not a word expanded in the text. |
| `inj.` | injectif / injective | |
| `inut.` | inutile | Cancelled and doubtful on 98. |
| `inv.`, `invo.` | involution | `inv.` can also denote invariant; the doubtful word on 120 is left unresolved. |
| `iso`, `iso.`, `isom`, `isom.` | isomorphisme | |
| `Ker` | kernel / noyau | |
| `lin.` | linéaire | |
| `loc.` | localement | Usually locally free. |
| `mbs` | membres | Occurs in the calculations. |
| `mod.` | module | |
| `NB`, `NB.`, `N.B.` | nota bene | Several are underlined or marginal. |
| `nb` | nombre | Number of nonzero coordinates on 116. |
| `néc.` | nécessairement | |
| `n°`, `n°s` | numéro, numéros | Includes references within the reused typed text. |
| `op.` | opération / action | Contextual suggestion, not a resolved mathematical identification. |
| doubtful `OS` | on suppose | On 97 the alternative is `on`; expansion is especially tentative. |
| `OK`, `OK.`, `O.K.` | okay / verification accepted by the author | Does not certify the argument editorially. |
| doubtful `p.` | Possibly the symbol p followed by punctuation | 128; no secure expansion. |
| `p.ex.` | par exemple | |
| `p.r.` | par rapport | |
| `pr`, `proj` | projection | |
| `pt` | point | In `au pt de vue` on 112. |
| `quad.`, `qu.` | quadratique | |
| `Quad` | quadratic forms | Named mathematical object on 97. |
| `rev.` | revêtement | |
| `rg` | rang | |
| `sc.` | scindé / splitting | In the chi-splitting calculation on 128; expansion is contextual. |
| `Spec` | spectre | |
| `t.q.`, `tq.` | tel que | |
| `tjrs` | toujours | |
| `tir.` | tiré | Especially `tir. de` in 136. |
| `Tr`, `Tr.` | trace | Its subscript and distinction from `t`, `T` are retained. |
| `univ.` | universellement | Usually in `univ. injectif`. |
| `val.` | valeurs | |
| `M.`, `J.`, `S.` in the typed quotation | Personal initials | No names supplied or inferred. |

# Legibility and limits

All 48 supplied nonblank pages were visually read in order, whole page and overlapping halves, and then read a second time against their saved fragments. No OCR was used. Blank scan 123 was omitted from the supplied images and has no invented page fragment. The context archive stayed unread during these readings and the notation comparison; its directory names were inadvertently listed earlier, a metadata-only event recorded in the progress log.

The mathematical handwriting varies from reasonably open prose to very compressed exploratory algebra. I trust the clear prose and the larger displayed formulas more than the overwritten coefficients, tiny subscripts, scope of bars, and arrowheads. The least secure mathematical areas are the cancelled construction on 99, the trace/invariant notation and lower margin on 102–105, the dense change-of-splitting work on 132–140, and the abandoned calculations on 144. One cancelled word on 97 remains `\illegible{1}` after enlargement; formula symbols are always attempted with `\unsure`, never replaced by an illegibility count.

The reused typed sheets are easier to read in their interiors, but many right edges lose letters, hyphens or punctuation. The visible fragment is the first reading, and a possible completed word is only an alternative. Source spellings, unusual agreements, spacing, incomplete quotations and the out-of-order printed folio 480 are preserved. Scan 129 was read after rotating its inverted typed text; its handwritten folio was retained separately.

The second audit made substantive corrections, including exclamation exponents versus primes, headless strokes, directions and grouping of arrows, the position of handwritten folios, and small marginal pointers. These checks reduce avoidable errors but do not make uncertain handwriting certain. The fragment passed mechanical brace, environment, delimiter, inventory and file-set checks; a complete TeX compilation could not be performed because the available TeX installation lacks the required document formats/packages, as recorded in `scripts/mechanical_qa/compile_report.txt`.
