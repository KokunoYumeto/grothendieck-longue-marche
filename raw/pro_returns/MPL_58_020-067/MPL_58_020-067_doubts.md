# MPL_58_020–067: notation and doubts

## Package notation table

The primary reader checked the recurring forms below throughout the two visual passes and then compared their LaTeX occurrences before freezing. The table records graphic conventions, not a normalization of the mathematics: a missing condition, inconsistent letter, changed degree, or different authorial spelling stays where it occurs. Unresolved differences remain marked in the fragment and in the register below.

| Sign or practice | LaTeX transcription | Locations / cautions |
|---|---|---|
| Ordinary prime | `'`, `''` | Typed algebra sheets 20, 22, 24, 47, 49 and handwritten 23–27, 42–52, 65–67. Upper ticks are distinguished from the lower dot of an exclamation mark; no secure shriek exponent was found in these retained pages. |
| Asterisk | `^*`, `_*` | Pullback and direct image, units on 66, induced characters on 63. The doubtful exponent in the circled condition on 60 remains `A'_n` versus `A^*_n`. Asterisks have not been converted to primes. |
| Double quotation marks | two backticks and two apostrophes | Examples 22, 25, 27, 30, 31, 33, 39, 40, 50. No editorial straight double quotes are used for source quotation marks. Double quotes inside TikZ options delimit labels and are code, not source punctuation. |
| Plain dash between mathematical objects | `\mathbin{-}`; TikZ `dash` | 30, 33, 35, 40–43, 46, 48, 59, 60, 65, 67. A dash is retained when no arrowhead is secure; doubtful dash/arrow distinctions are explicit. |
| Single arrow, isomorphism arrow, equivalence | `\longrightarrow`, `\overset{\sim}{\longrightarrow}`, `\simeq`, `\Longleftrightarrow` | Directions and heads checked independently of expected exactness. In 67 the cropped comparison is an arrow with a wavy upper stroke, not a nondirectional equivalence. In 50 the final relation is a wavy stroke, with inequality retained only as an alternative. |
| Double arrows and curved implications | TikZ `Rightarrow`, `Leftarrow`, `Leftrightarrow` | The comparison chart on 37 and chains on 56, 58–60, 62. Three faint labels on the curved arrows of 37 remain uncertain `h`; they are distinct from arrowheads. The lower doubled relation on 65 is `=` versus `\Rightarrow`. |
| Underlining and double underlining | `\uline{…}`, `\uuline{…}` | Extent and cancellation preserved. Mathematical letter underlines use standard `\underline`; the typed integer symbol on 63 has two visible underlines, rather than a substituted blackboard-bold alphabet. |
| Structure-sheaf letter | `O`, `\underline O`, doubtful `\mathcal O` | Underlines visible on the notes and reused typescripts are retained. Unadorned occurrences are not silently supplied with underlines; the cancelled script-like glyph before Lambda on 40 remains doubtful. |
| Underlined prime-ideal letters | `\underline p`, `\underline P` | 22. Visible typed letters plus underlines are retained rather than silently replaced with Gothic ideals. |
| Formal-module alphabet | `\unsure{\mathfrak F\|\mathcal F}` | 31, 33, 41, 43, 50; the same unresolved Gothic/script distinction is registered consistently. Plain algebraic `F` is not globally changed to this alphabet. The graphs on 57 have separately doubtful script/plain labels. |
| Formal-scheme alphabet | `\mathfrak X`, `\mathfrak X'` | 42–43, explicitly linked there to `X_{/Y}`. The categorical letter `\mathcal L` on 33 remains script L; the invertible module `L` elsewhere is plain L. |
| Formal completion | `X_{/Y}`, `F_{/Y}`, `\hat X`, `\hat F` | 30–50 and 56–62. Both of the author's graphic forms are kept; primes, hats, subscripts and slash placement are not made uniform by mathematical inference. The uncertain hat/tilde on 48 is marked locally. |
| Hat on a cone | `\hat C` | 65, 67. Scan 67 explicitly calls this a projective cone. The hat is therefore not an editorial declaration of formal completion, and the visible `Spec S[z]` of 65 has not been replaced by another construction. |
| Closure bar | `\bar x`, `\overline{x'}`, `\bar U` | 21–27, 33, 36–38, 46, 50, 52; separated from a completion hat. |
| Tensor sign and scalar-extension subscript | `\otimes`, `V'_{(K)}` | Typed 20 and later algebra sheets. The handwritten parenthesized `(K)` on 20 is an insertion, not part of a reconstructed uniform subscript convention. |
| Lowercase dimension bounds and field letters | `h`, `k`; locally `\unsure{k\|h}` | 21, 23, 25, 27, 67. The initial bound on 21 and the final bound on 27 favor k-shaped ink, even where h would harmonize an argument; those differences remain explicit. The last coefficient-field glyph on 67 is also marked. |
| Capital bound and similar lowercase letters | `K`, `n`, `m` | 27 has `K+1=(n+h)+1` and inserted `K-n`; the initial n/h remains doubtful. Grading variables on 56–62 were checked separately; 61 retains uncertainty in the lower bound m/n. |
| Looped ell | `\ell` | Hyperplanes on 27 and the prime distinct from p on typed 63. Not replaced by the digit 1. |
| Xi, zeta and z | `\xi`, `\zeta`, `z` with local alternatives | 33 associated-point annotation has xi/z uncertainty; 65's Picard quotient generator is xi/zeta. The isolated-point statements on 56–62 use the z actually written. |
| Phi and varphi | `\Phi`, `\varphi` | 46 support family; 48 completion subscript remains capital/lowercase doubtful; 35 comparison map; 63 induced characters; 65 units calculation. These have not been unified merely because the glyphs resemble one another. |
| Gamma | `\Gamma` | Sections on 46, 48, 56, 67. One cancelled expression on 38 is F(n)/Gamma(X) doubtful and is not used to harmonize the rest. |
| Lambda and ideal J | `\Lambda`, `J` | 40–41, including negative powers, the inverse ideal, and `J/J^2`; the exponent 2 on 40 remains locally doubtful. |
| Greek nu versus n | `\nu`, `n_s` | Genus formulas on 66: nu and the subscripted n terms are kept distinct. |
| Sum, coproduct-shaped sign and direct sum | `\sum`, `\coprod`; locally `\bigoplus` alternative | 56's first large sign remains doubtful. The squared-bottom signs on 57, 58, 60 are encoded as coproduct-shaped glyphs; 61 and 63 visibly have sums. No sign was selected from the algebraic interpretation. |
| Weak, strict and effective LG language | `(LG)_n`, `LG`, written `faible`, `strict`, `stricte`, `effective`, `effectif` | 33–43. Parentheses and word endings vary in the source and remain. The rewritten definition on 33 has not been supplied with an absent word “stricte”; the later explanation uses it explicitly. |
| Successor-degree bounds | `i\leq n`, `i=n+1`, `>n+1`, etc. | 33–36 and 56–62. Each inequality and index was re-read; the strange induction inequality on 34 is still marked rather than repaired. The uncertain grading inequalities on 57 and 58 remain different local readings. |
| Formal condition names | `A_n`, `A'_n`, `C'_i`, `C_n` | 58–62. Circled or braced placement is reproduced; the prime/star doubt on 60 is not settled from the neighboring naming scheme. |
| Source blanks | visible blank space, empty target, or incomplete sentence | 48's unfinished depth condition; missing relation symbols in typed 57 and 61; blank reference on 51; absent summation sign above lambda in 63 (12); incomplete targets on 65/67; final sentence of 67. A blank is not filled by an expected formula. |
| Finite-interval brackets | `\unsure{[\![1,n]\!]\|[1,n]}` | Typed 53. Double/single bracket ambiguity remains localized. |
| Internal page numbers and corner numerals | `\mspage{…}` and `\margin{…}` | Internal folios/printed sheet identifiers are retained on 20, 22, 24, 30, 47, 49, 51, 53, 63. The separate corner sequence equals scan minus one and is transcribed as a margin without an unsupported attribution of its hand. Upside-down corner numerals on 51, 53, 61, 63 are rotated. |
| Reversed show-through | not a second recto text layer | 52/53, 62/63 and especially 65/66. On 65, the two pale circles, circled slash and two faint bottom curve sketches are mirrored versions of stronger recto drawings on 66; only their actual recto instances are transcribed. The distinct strong arc/loop and K-like strokes on 65 remain. |


## Doubt register

Line numbers below refer to the per-page LaTeX source; they are approximate locations on the image. Confidence is confidence in the proposed reading, not in its mathematical plausibility. The particularly overwritten or compressed scans 30, 31, 38, 41, 44, 46, 50, 58, 65 and 67 are conservatively rated low wherever a doubt mark occurs. Nested doubt marks are listed individually; alternatives are separated only at the outermost brace level.

| File | Scan | Approximate line | Reading | Alternatives | Confidence |
|---|---:|---:|---|---|---|
| 58.pdf | 21 | 3 | `préschéma` | `Undetermined` | medium |
| 58.pdf | 21 | 6 | `k` | `h` | low |
| 58.pdf | 21 | 6 | `au` | `Undetermined` | medium |
| 58.pdf | 21 | 11 | `lemme` | `Undetermined` | medium |
| 58.pdf | 21 | 11 | `bien` | `Undetermined` | medium |
| 58.pdf | 21 | 11 | `général` | `Undetermined` | medium |
| 58.pdf | 21 | 12 | `conn. géom.` | `Undetermined` | medium |
| 58.pdf | 21 | 15 | `Supposons` | `Undetermined` | medium |
| 58.pdf | 21 | 15 | `un` | `Undetermined` | medium |
| 58.pdf | 21 | 18 | `On le suppose` | `Undetermined` | medium |
| 58.pdf | 21 | 25 | `donc` | `Undetermined` | medium |
| 58.pdf | 21 | 26 | `X` | `X^2` | low |
| 58.pdf | 21 | 28 | `s'induisant` | `Undetermined` | medium |
| 58.pdf | 21 | 30 | `d'où une` | `Undetermined` | medium |
| 58.pdf | 23 | 4 | `loc. de t.f.` | `Undetermined` | medium |
| 58.pdf | 23 | 5 | `loc` | `Undetermined` | medium |
| 58.pdf | 23 | 5 | `noeths` | `Undetermined` | medium |
| 58.pdf | 23 | 6 | `une générisation` | `Undetermined` | medium |
| 58.pdf | 23 | 7 | `pt gén. de $Y$` | `Undetermined` | medium |
| 58.pdf | 23 | 9 | `cas des` | `Undetermined` | medium |
| 58.pdf | 23 | 9 | `variétés` | `Undetermined` | medium |
| 58.pdf | 23 | 10 | `intég` | `Undetermined` | medium |
| 58.pdf | 23 | 12 | `Autrement` | `Undetermined` | medium |
| 58.pdf | 23 | 18 | `géom.` | `Undetermined` | medium |
| 58.pdf | 23 | 18 | `t` | `Undetermined` | medium |
| 58.pdf | 23 | 23 | `universellement ouvert` | `Undetermined` | medium |
| 58.pdf | 23 | 24 | `$f$` | `Undetermined` | medium |
| 58.pdf | 23 | 24 | `h+1` | `h_0` | low |
| 58.pdf | 23 | 31 | `entre` | `Undetermined` | medium |
| 58.pdf | 23 | 32 | `théorème` | `Undetermined` | medium |
| 58.pdf | 23 | 35 | `connexion` | `connexité` | low |
| 58.pdf | 25 | 6 | `notations` | `Undetermined` | medium |
| 58.pdf | 25 | 9 | `supposer` | `Undetermined` | medium |
| 58.pdf | 25 | 9 | `[unreadable: estimated 3 words]` | `No secure reading` | low |
| 58.pdf | 25 | 10 | `y_0` | `Y` | low |
| 58.pdf | 25 | 10 | `géom.` | `Undetermined` | medium |
| 58.pdf | 25 | 12 | `\widehat{\underline O}` | `\underline O` | low |
| 58.pdf | 25 | 15 | `Bien plutôt` | `Undetermined` | medium |
| 58.pdf | 25 | 19 | `théor. de dim` | `Undetermined` | medium |
| 58.pdf | 25 | 31 | `complété de` | `Undetermined` | medium |
| 58.pdf | 25 | 31 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 25 | 33 | `formellt` | `Undetermined` | medium |
| 58.pdf | 25 | 34 | `dimensions` | `Undetermined` | medium |
| 58.pdf | 25 | 34 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 27 | 4 | `n` | `h` | low |
| 58.pdf | 27 | 4 | `élts` | `Undetermined` | medium |
| 58.pdf | 27 | 4 | `démontre` | `Undetermined` | medium |
| 58.pdf | 27 | 5 | `sur` | `Undetermined` | medium |
| 58.pdf | 27 | 5 | `puisque` | `Undetermined` | medium |
| 58.pdf | 27 | 6 | `formellt` | `Undetermined` | medium |
| 58.pdf | 27 | 6 | `équidim.` | `Undetermined` | medium |
| 58.pdf | 27 | 8 | `(n+h)` | `Undetermined` | medium |
| 58.pdf | 27 | 9 | `k` | `h` | low |
| 58.pdf | 27 | 12 | `connexité` | `Undetermined` | medium |
| 58.pdf | 27 | 12 | `int` | `Undetermined` | medium |
| 58.pdf | 27 | 16 | `mais` | `univ.` | low |
| 58.pdf | 27 | 18 | `de dim` | `Undetermined` | medium |
| 58.pdf | 27 | 22 | `et` | `Undetermined` | medium |
| 58.pdf | 27 | 24 | `satisfait les` | `Undetermined` | medium |
| 58.pdf | 27 | 30 | `en` | `Undetermined` | medium |
| 58.pdf | 27 | 31 | `th.` | `Undetermined` | medium |
| 58.pdf | 27 | 31 | `EGA` | `Undetermined` | medium |
| 58.pdf | 27 | 32 | `connexité` | `Undetermined` | medium |
| 58.pdf | 27 | 32 | `initial` | `Undetermined` | medium |
| 58.pdf | 28 | 4 | `Théorie` | `Undetermined` | medium |
| 58.pdf | 30 | 3 | `0` | `Undetermined` | low |
| 58.pdf | 30 | 7 | `4` | `Undetermined` | low |
| 58.pdf | 30 | 8 | `I-adique` | `Undetermined` | low |
| 58.pdf | 30 | 9 | `complet` | `Undetermined` | low |
| 58.pdf | 30 | 9 | `pour` | `Undetermined` | low |
| 58.pdf | 30 | 10 | `avait` | `Undetermined` | low |
| 58.pdf | 30 | 15 | `local` | `Undetermined` | low |
| 58.pdf | 30 | 16 | `I` | `Undetermined` | low |
| 58.pdf | 30 | 18 | `en termes` | `Undetermined` | low |
| 58.pdf | 30 | 19 | `\mathbin{-}` | `\longrightarrow` | low |
| 58.pdf | 30 | 21 | `X'` | `X` | low |
| 58.pdf | 30 | 22 | `pro-Modules` | `Undetermined` | low |
| 58.pdf | 30 | 22 | `X'_{Y'}` | `\widehat X_{Y'}` | low |
| 58.pdf | 30 | 25 | `généraliserons` | `Undetermined` | low |
| 58.pdf | 30 | 26 | `voulons` | `montrons` | low |
| 58.pdf | 30 | 26 | `puissent` | `Undetermined` | low |
| 58.pdf | 30 | 29 | `différence` | `Undetermined` | low |
| 58.pdf | 30 | 29 | `essentielle` | `Undetermined` | low |
| 58.pdf | 30 | 30 | `ici` | `Undetermined` | low |
| 58.pdf | 30 | 30 | `on se borne` | `Undetermined` | low |
| 58.pdf | 30 | 31 | `en ce qui concerne` | `Undetermined` | low |
| 58.pdf | 30 | 31 | `énoncés` | `Undetermined` | low |
| 58.pdf | 30 | 32 | `les` | `Undetermined` | low |
| 58.pdf | 30 | 32 | `th.` | `Undetermined` | low |
| 58.pdf | 30 | 32 | `de` | `Undetermined` | low |
| 58.pdf | 30 | 33 | `connexité` | `Undetermined` | low |
| 58.pdf | 30 | 33 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 30 | 34 | `des bornes` | `Undetermined` | low |
| 58.pdf | 30 | 34 | `cohom.` | `Undetermined` | low |
| 58.pdf | 30 | 35 | `pour des raisons` | `Undetermined` | low |
| 58.pdf | 30 | 35 | `seront` | `Undetermined` | low |
| 58.pdf | 30 | 36 | `\leq n` | `Undetermined` | low |
| 58.pdf | 30 | 36 | `récurrence` | `Undetermined` | low |
| 58.pdf | 30 | 37 | `du` | `Undetermined` | low |
| 58.pdf | 30 | 37 | `théor.` | `Undetermined` | low |
| 58.pdf | 30 | 39 | `d'ailleurs très générale` | `Undetermined` | low |
| 58.pdf | 30 | 41 | `pour` | `Undetermined` | low |
| 58.pdf | 30 | 41 | `cohomologies` | `Undetermined` | low |
| 58.pdf | 30 | 42 | `f_*` | `Undetermined` | low |
| 58.pdf | 30 | 42 | `qui se trouvent` | `Undetermined` | low |
| 58.pdf | 30 | 43 | `convenables` | `Undetermined` | low |
| 58.pdf | 30 | 44 | `cohomologiques` | `Undetermined` | low |
| 58.pdf | 30 | 44 | `supposées` | `Undetermined` | low |
| 58.pdf | 31 | 6 | `développ.` | `Undetermined` | low |
| 58.pdf | 31 | 12 | `de` | `Undetermined` | low |
| 58.pdf | 31 | 12 | `sur` | `Undetermined` | low |
| 58.pdf | 31 | 13 | `etc` | `Undetermined` | low |
| 58.pdf | 31 | 14 | `présentent` | `Undetermined` | low |
| 58.pdf | 31 | 14 | `un` | `Undetermined` | low |
| 58.pdf | 31 | 14 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 31 | 15 | `l'observation` | `Undetermined` | low |
| 58.pdf | 31 | 15 | `faite` | `Undetermined` | low |
| 58.pdf | 31 | 15 | `plus` | `Undetermined` | low |
| 58.pdf | 31 | 15 | `explicite` | `Undetermined` | low |
| 58.pdf | 31 | 17 | `procédés usuels` | `Undetermined` | low |
| 58.pdf | 31 | 18 | `cônes projetants` | `Undetermined` | low |
| 58.pdf | 31 | 20 | `rang` | `Undetermined` | low |
| 58.pdf | 31 | 22 | `Ces` | `Undetermined` | low |
| 58.pdf | 31 | 22 | `résultats` | `Undetermined` | low |
| 58.pdf | 31 | 25 | `nous aurons donc` | `Undetermined` | low |
| 58.pdf | 31 | 26 | `est dû` | `Undetermined` | low |
| 58.pdf | 31 | 28 | `été` | `Undetermined` | low |
| 58.pdf | 31 | 28 | `démontré` | `Undetermined` | low |
| 58.pdf | 31 | 28 | `nous` | `Undetermined` | low |
| 58.pdf | 31 | 29 | `Bourbaki` | `Undetermined` | low |
| 58.pdf | 31 | 30 | `nullité` | `Undetermined` | low |
| 58.pdf | 31 | 31 | `et montrant que dans la situation précédente` | `Undetermined` | low |
| 58.pdf | 31 | 32 | `il` | `Undetermined` | low |
| 58.pdf | 31 | 32 | `était` | `Undetermined` | low |
| 58.pdf | 31 | 32 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 31 | 40 | `dépendant de` | `Undetermined` | low |
| 58.pdf | 31 | 41 | `\leq` | `Undetermined` | low |
| 58.pdf | 31 | 44 | `\mathfrak F` | `\mathcal F` | low |
| 58.pdf | 31 | 45 | `\hat{\mathfrak F}` | `Undetermined` | low |
| 58.pdf | 31 | 45 | `est` | `Undetermined` | low |
| 58.pdf | 31 | 46 | `O_{X}` | `Undetermined` | low |
| 58.pdf | 31 | 47 | `corps de sections` | `Undetermined` | low |
| 58.pdf | 31 | 48 | `\mathfrak F` | `\mathcal F` | low |
| 58.pdf | 31 | 49 | `et` | `Undetermined` | low |
| 58.pdf | 31 | 50 | `pour les sections` | `Undetermined` | low |
| 58.pdf | 31 | 50 | `voir` | `Undetermined` | low |
| 58.pdf | 31 | 51 | `N°` | `Undetermined` | low |
| 58.pdf | 31 | 51 | `d'un` | `Undetermined` | low |
| 58.pdf | 31 | 51 | `Grothendieck` | `Undetermined` | low |
| 58.pdf | 31 | 52 | `cela` | `Undetermined` | low |
| 58.pdf | 31 | 52 | `est` | `Undetermined` | low |
| 58.pdf | 31 | 52 | `utile` | `Undetermined` | low |
| 58.pdf | 31 | 54 | `Cela qui` | `Undetermined` | low |
| 58.pdf | 31 | 56 | `\rho` | `p` | low |
| 58.pdf | 31 | 58 | `\rho` | `p` | low |
| 58.pdf | 31 | 59 | `plus loin` | `Undetermined` | low |
| 58.pdf | 32 | 9 | `Premières` | `Undetermined` | medium |
| 58.pdf | 32 | 9 | `fondamentaux` | `Undetermined` | medium |
| 58.pdf | 32 | 13 | `I` | `II` | low |
| 58.pdf | 32 | 13 | `théorie` | `Undetermined` | medium |
| 58.pdf | 32 | 13 | `les` | `Undetermined` | medium |
| 58.pdf | 32 | 14 | `théorie` | `Undetermined` | medium |
| 58.pdf | 32 | 14 | `quelconques` | `réguliers` | low |
| 58.pdf | 32 | 24 | `utilise` | `utiliser` | low |
| 58.pdf | 32 | 27 | `9` | `Undetermined` | medium |
| 58.pdf | 32 | 31 | `[unreadable: estimated 1 words]` | `No secure reading` | low |
| 58.pdf | 33 | 9 | `propriété` | `Undetermined` | medium |
| 58.pdf | 33 | 9 | `d'ordre` | `Undetermined` | medium |
| 58.pdf | 33 | 10 | `tt` | `$\forall$` | low |
| 58.pdf | 33 | 13 | `\text{est}` | `Undetermined` | medium |
| 58.pdf | 33 | 26 | `dans ceux` | `Undetermined` | medium |
| 58.pdf | 33 | 30 | `la dite` | `Undetermined` | medium |
| 58.pdf | 33 | 31 | `si` | `Undetermined` | medium |
| 58.pdf | 33 | 32 | `définie` | `Undetermined` | medium |
| 58.pdf | 33 | 34 | `\mathfrak F` | `\mathcal F` | low |
| 58.pdf | 33 | 35 | `il` | `Undetermined` | medium |
| 58.pdf | 33 | 39 | `\xi` | `z` | low |
| 58.pdf | 33 | 40 | `point` | `Undetermined` | medium |
| 58.pdf | 33 | 40 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 33 | 41 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 33 | 42 | `tq` | `Undetermined` | medium |
| 58.pdf | 33 | 42 | `\xi` | `z` | low |
| 58.pdf | 33 | 43 | `\xi` | `z` | low |
| 58.pdf | 33 | 46 | `LG` | `Undetermined` | medium |
| 58.pdf | 33 | 46 | `?` | `Undetermined` | medium |
| 58.pdf | 33 | 47 | `d'alors` | `Undetermined` | medium |
| 58.pdf | 33 | 47 | `pour tout` | `Undetermined` | medium |
| 58.pdf | 33 | 59 | `Précaution` | `Undetermined` | medium |
| 58.pdf | 33 | 64 | `tout` | `Undetermined` | medium |
| 58.pdf | 34 | 11 | `régulièrement` | `réellement` | low |
| 58.pdf | 34 | 15 | `résolution` | `Undetermined` | medium |
| 58.pdf | 34 | 17 | `vérifier que le foncteur` | `Undetermined` | medium |
| 58.pdf | 34 | 17 | `et la` | `Undetermined` | medium |
| 58.pdf | 34 | 18 | `limite` | `Undetermined` | medium |
| 58.pdf | 34 | 18 | `G` | `Undetermined` | medium |
| 58.pdf | 34 | 26 | `projectif` | `Undetermined` | medium |
| 58.pdf | 34 | 38 | `Confiance` | `Undetermined` | medium |
| 58.pdf | 34 | 39 | `faut le prouver` | `Undetermined` | medium |
| 58.pdf | 34 | 39 | `en mettant une` | `Undetermined` | medium |
| 58.pdf | 34 | 42 | `n+1<0` | `n\geq0` | low |
| 58.pdf | 34 | 42 | `on` | `Undetermined` | medium |
| 58.pdf | 34 | 46 | `ne l'exige que la` | `Undetermined` | medium |
| 58.pdf | 34 | 47 | `n+1` | `n` | low |
| 58.pdf | 34 | 47 | `L_\alpha` | `Undetermined` | medium |
| 58.pdf | 34 | 48 | `n+1` | `n` | low |
| 58.pdf | 34 | 48 | `\hat L_\alpha` | `Undetermined` | medium |
| 58.pdf | 34 | 50 | `Cet` | `Cat` | low |
| 58.pdf | 34 | 50 | `résultat` | `réserve` | low |
| 58.pdf | 35 | 4 | `\alpha` | `Undetermined` | medium |
| 58.pdf | 35 | 11 | `sommes` | `Undetermined` | medium |
| 58.pdf | 35 | 32 | `et puis par l'hyp. de réc.` | `Undetermined` | medium |
| 58.pdf | 35 | 37 | `que` | `Undetermined` | medium |
| 58.pdf | 35 | 38 | `l'hyp` | `Undetermined` | medium |
| 58.pdf | 35 | 38 | `pour` | `Undetermined` | medium |
| 58.pdf | 36 | 6 | `Cependant` | `Undetermined` | medium |
| 58.pdf | 36 | 18 | `n` | `0` | low |
| 58.pdf | 36 | 22 | `U` | `Undetermined` | medium |
| 58.pdf | 36 | 30 | `pour` | `Undetermined` | medium |
| 58.pdf | 36 | 30 | `donc que` | `Undetermined` | medium |
| 58.pdf | 37 | 12 | `de` | `Undetermined` | medium |
| 58.pdf | 37 | 13 | `concentré` | `Undetermined` | medium |
| 58.pdf | 37 | 15 | `qui` | `Undetermined` | medium |
| 58.pdf | 37 | 17 | `X` | `Undetermined` | medium |
| 58.pdf | 37 | 24 | `h` | `Undetermined` | medium |
| 58.pdf | 37 | 27 | `h` | `Undetermined` | medium |
| 58.pdf | 37 | 29 | `h` | `Undetermined` | medium |
| 58.pdf | 38 | 14 | `\eta` | `\xi` | low |
| 58.pdf | 38 | 15 | `connexe` | `Undetermined` | low |
| 58.pdf | 38 | 18 | `\eta` | `\xi` | low |
| 58.pdf | 38 | 21 | `\eta` | `\xi` | low |
| 58.pdf | 38 | 28 | `pour` | `Undetermined` | low |
| 58.pdf | 38 | 31 | `resp.` | `Undetermined` | low |
| 58.pdf | 38 | 31 | `associative` | `Undetermined` | low |
| 58.pdf | 38 | 32 | `connue` | `Undetermined` | low |
| 58.pdf | 38 | 36 | `de même que` | `Undetermined` | low |
| 58.pdf | 38 | 37 | `sont aussi` | `Undetermined` | low |
| 58.pdf | 38 | 40 | `en liaison avec` | `en biject. avec` | low |
| 58.pdf | 38 | 40 | `celles de` | `Undetermined` | low |
| 58.pdf | 38 | 40 | `F(n)` | `\Gamma(X)` | low |
| 58.pdf | 38 | 50 | `L'immersion` | `Undetermined` | low |
| 58.pdf | 38 | 50 | `la` | `Undetermined` | low |
| 58.pdf | 38 | 50 | `[unreadable: estimated 1 words]` | `No secure reading` | low |
| 58.pdf | 38 | 51 | `voisinage` | `Undetermined` | low |
| 58.pdf | 38 | 51 | `de` | `Undetermined` | low |
| 58.pdf | 38 | 51 | `[unreadable: estimated 1 words]` | `No secure reading` | low |
| 58.pdf | 38 | 52 | `particulier` | `Undetermined` | low |
| 58.pdf | 38 | 52 | `fini` | `Undetermined` | low |
| 58.pdf | 38 | 52 | `ét.` | `Undetermined` | low |
| 58.pdf | 38 | 53 | `donne` | `Undetermined` | low |
| 58.pdf | 38 | 54 | `étales` | `d'actions` | low |
| 58.pdf | 39 | 9 | `X` | `Undetermined` | medium |
| 58.pdf | 39 | 10 | `Y` | `X` | low |
| 58.pdf | 39 | 15 | `et d'un` | `et un` | low |
| 58.pdf | 40 | 17 | `\mathcal O` | `Undetermined` | medium |
| 58.pdf | 40 | 19 | `2` | `Undetermined` | medium |
| 58.pdf | 40 | 28 | `plus gén.` | `Undetermined` | medium |
| 58.pdf | 40 | 28 | `et on a les mêmes` | `Undetermined` | medium |
| 58.pdf | 40 | 29 | `injectif` | `Undetermined` | medium |
| 58.pdf | 40 | 31 | `donc` | `Undetermined` | medium |
| 58.pdf | 40 | 31 | `surjectifs` | `Undetermined` | medium |
| 58.pdf | 40 | 32 | `de même` | `Undetermined` | medium |
| 58.pdf | 40 | 35 | `\deleted{H^1(Y,\Lambda^{-n})}` | `H^1(Y,\Lambda^{-n})` | low |
| 58.pdf | 41 | 3 | `énoncés` | `Undetermined` | low |
| 58.pdf | 41 | 3 | `résultent` | `Undetermined` | low |
| 58.pdf | 41 | 5 | `du` | `Undetermined` | low |
| 58.pdf | 41 | 8 | `(i)` | `Undetermined` | low |
| 58.pdf | 41 | 10 | `pour` | `Undetermined` | low |
| 58.pdf | 41 | 11 | `\mathfrak F` | `\mathcal F` | low |
| 58.pdf | 41 | 14 | `alors` | `Undetermined` | low |
| 58.pdf | 41 | 31 | `alors` | `Undetermined` | low |
| 58.pdf | 41 | 35 | `Th 2` | `Dém` | low |
| 58.pdf | 41 | 35 | `Cas` | `Undetermined` | low |
| 58.pdf | 41 | 39 | `\deleted{\uline{Pr. 2} Si $(X,Y)$ satisfasse $(LG)$ [resp. $(LG)$ effectif], \deleted{Alors} $X$ quasi-projectif, -- alors}` | `Undetermined` | low |
| 58.pdf | 42 | 3 | `plat` | `Undetermined` | medium |
| 58.pdf | 42 | 7 | `Th 2` | `Undetermined` | medium |
| 58.pdf | 42 | 8 | `pré` | `Undetermined` | medium |
| 58.pdf | 42 | 8 | `loc.` | `Undetermined` | medium |
| 58.pdf | 42 | 13 | `Y` | `X` | low |
| 58.pdf | 42 | 19 | `les conditions` | `Undetermined` | medium |
| 58.pdf | 42 | 35 | `alors` | `Undetermined` | medium |
| 58.pdf | 42 | 36 | `on` | `Undetermined` | medium |
| 58.pdf | 42 | 38 | `Y` | `X` | low |
| 58.pdf | 42 | 48 | `pas la peine pour $F'$ dans la suite` | `Undetermined` | medium |
| 58.pdf | 42 | 51 | `\mathfrak F'` | `F'` | low |
| 58.pdf | 43 | 3 | `tel que` | `Undetermined` | medium |
| 58.pdf | 43 | 5 | `\mathfrak F'` | `\mathcal F'` | low |
| 58.pdf | 43 | 10 | `loc.` | `Undetermined` | medium |
| 58.pdf | 43 | 16 | `peut se généraliser` | `Undetermined` | medium |
| 58.pdf | 43 | 22 | `et` | `Undetermined` | medium |
| 58.pdf | 43 | 23 | `U'` | `Undetermined` | medium |
| 58.pdf | 43 | 27 | `\text{i.e.}` | `\div` | low |
| 58.pdf | 43 | 31 | `(i)` | `Undetermined` | medium |
| 58.pdf | 43 | 32 | `plat` | `Undetermined` | medium |
| 58.pdf | 43 | 34 | `X` | `Undetermined` | medium |
| 58.pdf | 44 | 10 | `puisse` | `Undetermined` | low |
| 58.pdf | 44 | 10 | `omise` | `Undetermined` | low |
| 58.pdf | 44 | 11 | `premiers cas` | `Undetermined` | low |
| 58.pdf | 44 | 12 | `sans doute non plus dans` | `Undetermined` | low |
| 58.pdf | 44 | 14 | `donnant` | `Undetermined` | low |
| 58.pdf | 46 | 4 | `complet` | `Undetermined` | low |
| 58.pdf | 46 | 21 | `a priori fidèle` | `Undetermined` | low |
| 58.pdf | 46 | 25 | `]` | `Undetermined` | low |
| 58.pdf | 46 | 28 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 46 | 33 | `dominés` | `domiciliés` | low |
| 58.pdf | 46 | 35 | `composantes` | `Undetermined` | low |
| 58.pdf | 46 | 36 | `de dimension` | `Undetermined` | low |
| 58.pdf | 46 | 36 | `support de dimension` | `Undetermined` | low |
| 58.pdf | 46 | 36 | `\ne 1` | `+1` | low |
| 58.pdf | 46 | 37 | `non nuls` | `Undetermined` | low |
| 58.pdf | 46 | 40 | `les` | `Undetermined` | low |
| 58.pdf | 46 | 40 | `dim.` | `Undetermined` | low |
| 58.pdf | 46 | 41 | `\overline{x}` | `Undetermined` | low |
| 58.pdf | 46 | 41 | `\ne2` | `\ge2` | low |
| 58.pdf | 46 | 42 | `i.e. celles de $X'$` | `Undetermined` | low |
| 58.pdf | 46 | 42 | `de` | `Undetermined` | low |
| 58.pdf | 46 | 42 | `t` | `Undetermined` | low |
| 58.pdf | 46 | 43 | `cycles associés à $F'$` | `Undetermined` | low |
| 58.pdf | 46 | 44 | `\dim\overline{x}` | `Undetermined` | low |
| 58.pdf | 46 | 44 | `x\in X'` | `Undetermined` | low |
| 58.pdf | 46 | 45 | `ne se prolonge pas` | `Undetermined` | low |
| 58.pdf | 46 | 45 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 46 | 46 | `faisceaux` | `Undetermined` | low |
| 58.pdf | 46 | 46 | `\operatorname{prof}F'_x` | `Undetermined` | low |
| 58.pdf | 46 | 47 | `Y'` | `Undetermined` | low |
| 58.pdf | 46 | 47 | `\dim` | `Undetermined` | low |
| 58.pdf | 46 | 49 | `équivalente` | `Undetermined` | low |
| 58.pdf | 46 | 52 | `x\in Y'` | `Undetermined` | low |
| 58.pdf | 46 | 54 | `pour` | `Undetermined` | low |
| 58.pdf | 46 | 55 | `pas de cycles associés` | `Undetermined` | low |
| 58.pdf | 46 | 61 | `x` | `Undetermined` | low |
| 58.pdf | 46 | 61 | `de` | `Undetermined` | low |
| 58.pdf | 46 | 62 | `tout` | `Undetermined` | low |
| 58.pdf | 46 | 66 | `revenir là` | `Undetermined` | low |
| 58.pdf | 46 | 66 | `considérant` | `Undetermined` | low |
| 58.pdf | 46 | 70 | `F'` | `Undetermined` | low |
| 58.pdf | 46 | 70 | `\hat F'` | `Undetermined` | low |
| 58.pdf | 46 | 72 | `2` | `3` | low |
| 58.pdf | 48 | 10 | `\hat F'_{x'}` | `\widetilde F'_{x'}` | low |
| 58.pdf | 48 | 11 | `aux` | `Undetermined` | medium |
| 58.pdf | 48 | 17 | `sur $F_x$` | `Undetermined` | medium |
| 58.pdf | 48 | 42 | `K'` | `C'` | low |
| 58.pdf | 48 | 43 | `\hat A_\Phi` | `\hat A_\varphi` | low |
| 58.pdf | 48 | 44 | `\hat C'` | `\hat G'` | low |
| 58.pdf | 48 | 44 | `\hat K'` | `\hat C'` | low |
| 58.pdf | 48 | 47 | `non` | `Undetermined` | medium |
| 58.pdf | 49 | 31 | `?` | `Undetermined` | medium |
| 58.pdf | 50 | 3 | `On considère` | `Undetermined` | low |
| 58.pdf | 50 | 3 | `[unreadable: estimated 1 words]` | `No secure reading` | low |
| 58.pdf | 50 | 5 | `3` | `Undetermined` | low |
| 58.pdf | 50 | 7 | `\mathfrak F'` | `\mathcal F'` | low |
| 58.pdf | 50 | 8 | `\mathfrak F'` | `\mathcal F'` | low |
| 58.pdf | 50 | 9 | `\mathfrak F` | `\mathcal F` | low |
| 58.pdf | 50 | 9 | `je` | `Undetermined` | low |
| 58.pdf | 50 | 10 | `\mathfrak F'` | `\mathcal F'` | low |
| 58.pdf | 50 | 13 | `tel que` | `Undetermined` | low |
| 58.pdf | 50 | 17 | `X'` | `Undetermined` | low |
| 58.pdf | 50 | 19 | `et` | `Undetermined` | low |
| 58.pdf | 50 | 19 | `[unreadable: estimated 3 words]` | `No secure reading` | low |
| 58.pdf | 50 | 21 | `supposer` | `Undetermined` | low |
| 58.pdf | 50 | 22 | `effet` | `Undetermined` | low |
| 58.pdf | 50 | 23 | `x'\notin Y'` | `Undetermined` | low |
| 58.pdf | 50 | 23 | `\dim\overline{x'}\in T_1` | `Undetermined` | low |
| 58.pdf | 50 | 24 | `i.e.` | `Undetermined` | low |
| 58.pdf | 50 | 24 | `quitte à` | `Undetermined` | low |
| 58.pdf | 50 | 25 | `limiter` | `Undetermined` | low |
| 58.pdf | 50 | 25 | `à un ouvert convenable` | `Undetermined` | low |
| 58.pdf | 50 | 26 | `Considérons` | `Undetermined` | low |
| 58.pdf | 50 | 31 | `localisé` | `Undetermined` | low |
| 58.pdf | 50 | 33 | `partie` | `Undetermined` | low |
| 58.pdf | 50 | 34 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 50 | 35 | `sympathique` | `Undetermined` | low |
| 58.pdf | 50 | 38 | `X` | `Undetermined` | low |
| 58.pdf | 50 | 46 | `tel` | `Undetermined` | low |
| 58.pdf | 50 | 48 | `il n'est pas possible que` | `Undetermined` | low |
| 58.pdf | 50 | 49 | `\rightsquigarrow` | `\ne` | low |
| 58.pdf | 52 | 3 | `en les` | `Undetermined` | medium |
| 58.pdf | 52 | 8 | `X` | `Undetermined` | medium |
| 58.pdf | 53 | 11 | `[\![1,n]\!]` | `[1,n]` | low |
| 58.pdf | 54 | 3 | `Applications` | `Undetermined` | medium |
| 58.pdf | 54 | 4 | `hyperplans` | `projectifs` | low |
| 58.pdf | 56 | 9 | `fermé` | `fini` | low |
| 58.pdf | 56 | 15 | `a')` | `d)` | low |
| 58.pdf | 56 | 16 | `\coprod_m` | `\bigoplus_m` | low |
| 58.pdf | 56 | 22 | `c)` | `Undetermined` | medium |
| 58.pdf | 56 | 33 | `-m` | `Undetermined` | medium |
| 58.pdf | 56 | 34 | `-m` | `Undetermined` | medium |
| 58.pdf | 56 | 35 | `-m` | `Undetermined` | medium |
| 58.pdf | 56 | 36 | `-m` | `Undetermined` | medium |
| 58.pdf | 56 | 48 | `pour tout $m$` | `Undetermined` | medium |
| 58.pdf | 56 | 56 | `*` | `Undetermined` | medium |
| 58.pdf | 57 | 10 | `s` | `z` | low |
| 58.pdf | 57 | 16 | `3.1` | `Undetermined` | medium |
| 58.pdf | 57 | 19 | `\gg` | `\ge` | low |
| 58.pdf | 57 | 24 | `0` | `Undetermined` | medium |
| 58.pdf | 57 | 41 | `\mathcal F(n)` | `\sigma F(n)` | low |
| 58.pdf | 57 | 42 | `\mathcal F(m)` | `F(m)` | low |
| 58.pdf | 57 | 62 | `h ind` | `Undetermined` | medium |
| 58.pdf | 57 | 63 | `filtr.` | `Undetermined` | medium |
| 58.pdf | 58 | 20 | `0` | `i` | low |
| 58.pdf | 58 | 20 | `X` | `U` | low |
| 58.pdf | 58 | 38 | `\operatorname{prof}` | `Undetermined` | low |
| 58.pdf | 58 | 39 | `ne peut` | `Undetermined` | low |
| 58.pdf | 58 | 40 | `avoir un pt de $Z$ pour` | `Undetermined` | low |
| 58.pdf | 58 | 40 | `[unreadable: estimated 2 words]` | `No secure reading` | low |
| 58.pdf | 58 | 40 | `pts isolés` | `Undetermined` | low |
| 58.pdf | 58 | 48 | `\geq` | `\gg` | low |
| 58.pdf | 58 | 48 | `-h` | `Undetermined` | low |
| 58.pdf | 58 | 58 | `résout` | `Undetermined` | low |
| 58.pdf | 59 | 9 | `\mathbin{-}` | `\longrightarrow` | low |
| 58.pdf | 59 | 14 | `l'hom.` | `Undetermined` | medium |
| 58.pdf | 59 | 18 | `vectoriels` | `Undetermined` | medium |
| 58.pdf | 59 | 25 | `finie` | `Undetermined` | medium |
| 58.pdf | 59 | 27 | `\in` | `Undetermined` | medium |
| 58.pdf | 59 | 30 | `-m` | `m` | low |
| 58.pdf | 60 | 3 | `f` | `j` | low |
| 58.pdf | 60 | 3 | `F\deleted{(m)}` | `\deleted{F(m)}` | low |
| 58.pdf | 60 | 6 | `Y` | `Z` | low |
| 58.pdf | 60 | 47 | `A'_n` | `A^*_n` | low |
| 58.pdf | 61 | 11 | `s` | `x` | low |
| 58.pdf | 61 | 17 | `3;1` | `3.1` | low |
| 58.pdf | 61 | 20 | `f` | `g` | low |
| 58.pdf | 61 | 21 | `m` | `n` | low |
| 58.pdf | 61 | 24 | `M` | `pq` | low |
| 58.pdf | 62 | 16 | `\Updownarrow` | `\Downarrow` | low |
| 58.pdf | 62 | 25 | `à supposer que` | `Undetermined` | medium |
| 58.pdf | 65 | 4 | `U` | `1` | low |
| 58.pdf | 65 | 5 | `U` | `1` | low |
| 58.pdf | 65 | 19 | `Pic $C$` | `Undetermined` | low |
| 58.pdf | 65 | 23 | `\text{loc.}` | `Undetermined` | low |
| 58.pdf | 65 | 24 | `\subset\underline{Z\xi}` | `\text{engendré}` | low |
| 58.pdf | 65 | 27 | `\text{cas local}` | `Undetermined` | low |
| 58.pdf | 65 | 33 | `\xi` | `\zeta` | low |
| 58.pdf | 65 | 34 | `\xi` | `\zeta` | low |
| 58.pdf | 65 | 44 | `v` | `Undetermined` | low |
| 58.pdf | 65 | 45 | `g^m/f^n` | `Undetermined` | low |
| 58.pdf | 65 | 47 | `g^m/f^n=u` | `Undetermined` | low |
| 58.pdf | 65 | 58 | `\xi` | `\zeta` | low |
| 58.pdf | 65 | 58 | `=` | `\Rightarrow` | low |
| 58.pdf | 65 | 58 | `\xi` | `\zeta` | low |
| 58.pdf | 65 | 60 | `0` | `\bullet` | low |
| 58.pdf | 65 | 64 | `\mathbin{-}` | `Undetermined` | low |
| 58.pdf | 65 | 69 | `1` | `\downarrow` | low |
| 58.pdf | 65 | 72 | `U` | `C` | low |
| 58.pdf | 66 | 6 | `0` | `\bullet` | low |
| 58.pdf | 66 | 7 | `a` | `Undetermined` | medium |
| 58.pdf | 66 | 10 | `1` | `Undetermined` | medium |
| 58.pdf | 66 | 18 | `m` | `Undetermined` | medium |
| 58.pdf | 66 | 34 | `1` | `Undetermined` | medium |
| 58.pdf | 66 | 39 | `\widetilde A_\xi` | `Undetermined` | medium |
| 58.pdf | 66 | 71 | `1-h=` | `Undetermined` | medium |
| 58.pdf | 66 | 73 | `=` | `:` | low |
| 58.pdf | 66 | 77 | `\ne` | `=` | low |
| 58.pdf | 66 | 114 | `x` | `Undetermined` | medium |
| 58.pdf | 67 | 3 | `k` | `h` | low |
| 58.pdf | 67 | 5 | `projetant` | `Undetermined` | low |
| 58.pdf | 67 | 13 | `conditions` | `Undetermined` | low |
| 58.pdf | 67 | 22 | `f^*` | `\pi^*` | low |
| 58.pdf | 67 | 24 | `\underline O_{X'}(1)` | `Undetermined` | low |
| 58.pdf | 67 | 34 | `Il` | `Undetermined` | low |
| 58.pdf | 67 | 42 | `Soit` | `Sur` | low |
| 58.pdf | 67 | 42 | `partie` | `part.` | low |
| 58.pdf | 67 | 43 | `vectoriel` | `Undetermined` | low |
| 58.pdf | 67 | 51 | `évidemment` | `Undetermined` | low |
| 58.pdf | 67 | 53 | `si $j$ est la section nulle de $C_X$, est` | `Undetermined` | low |

## Abbreviations encountered

Expansions here are editorial suggestions only. They have not been substituted into any page file. A word whose final stop merely ends a sentence is not listed as an abbreviation.

| Written form | Possible expansion | Examples / caution |
|---|---|---|
| Alg.; alg. | Algèbre; algèbre / algébrique | 49; 38 |
| cat.; Mod. | catégorie; Modules | 33 and categorical passages |
| cf | confer / compare | 24 and references |
| chap.; par.; § | chapitre; paragraphe; section | 30, 51, 53 |
| coh.; cohom. | cohérent(e)(s); cohomologique(s) | 30, 36, 42–50, 60 |
| comm. | commutatif / commutative | 38 |
| conn. géom. | connexité géométrique | 21, uncertain written reading |
| cor.; Cor. | corollaire, or correspond where used with a point | 27, 44, 50; on 46 “x cor.” probably “x correspondant” |
| CQFD; C.Q.F.D.; cqfd. | ce qu'il fallait démontrer | 20, 26, 27, 63; capitalization retained locally |
| développ. | développement | Cancelled 31 |
| dim; dim. | dimension | Throughout; these are also mathematical operators |
| div. de 0 | diviseur de zéro | 48 |
| EGA | Éléments de géométrie algébrique | 21, 27; reference expansion only |
| ens. | ensemble | 31, 46, 50, 56 |
| équidim.; formellt | équidimensionnel; formellement | 27 and 25; “formellt” is a contraction, not modernized spelling |
| équiv.; ext. | équivalence; extension | 41; 34 |
| ét.; rev.; rev étale | étale; revêtement; revêtement étale | 38–39 |
| filtr. | filtration / filtré | Graph label on 57, uncertain |
| gén.; géom. | général / générique; géométrique | 23, 25, 38, 40; the expansion depends on the actual phrase |
| hom; hom.; isom; isom. | homomorphisme; isomorphisme | 33–43, 59, 67 |
| hyp.; réc. | hypothèse; récurrence | 35, 50 |
| i.e. | id est | Several passages; the reading before the condition on 43 is uncertain |
| imm. | immersion | 30 |
| inj.; mono. | injectif / injective; monomorphisme | 35; 42 |
| inv. | inversible | 40 |
| loc; loc.; rel. | localement / local; relativement / relatif | 23–66; preserve the local grammatical form |
| long. | longueur | 59 |
| n°; N° | numéro | Typed sheet identifiers and cross-references |
| N.B. | nota bene | Cancelled 34 |
| noeth; noeth.; noeths | noethérien / noethérienne / noethériens | 23, 42, 46 |
| p. ex. | par exemple | 30, 31, 36 |
| part. | partie | Alternative on 67, not securely distinguished from the full word |
| pl. fid.; pl. fidèle | pleinement fidèle | 33, 38, 41 |
| Pr.; prop. | proposition | 20–63 |
| prof | profondeur | Mathematical operator in depth conditions |
| pt; pts | point; points | Throughout |
| qu. projectif | quasi-projectif | 43 |
| resp; resp. | respectivement | 38–43 |
| ssi | si et seulement si | 38 |
| t.f. | type fini | Cancelled condition on 23 |
| th; th.; Th.; théor. | théorème | Several passages; case and stops retained |
| top. | topologie | 46 |
| tq | tel que | 33 |
| tt; tt. | tout | 33–34; not replaced by the universal-quantifier symbol |
| univ. | universellement | Alternative on 27 |
| éd. | édition | 51 |

## Legibility, editorial scope, and least secure passages

These pages were read directly, in one stream, without OCR. The reused typed sheets are generally the most legible, but their handwritten supplements, deliberately unfilled typescript positions and occasional overtyping still matter; 57 and 61 were read independently even where their typed text repeats. The small internal folios are not conflated with the separate corner numerals, whose authorship cannot be established from these images alone.

The least secure extended passages are the heavily revised introduction on 30–31; the cancelled end of 25; the overwritten definitions and tiny annotations on 33–34; the marginal lemma and cancelled decomposition discussion on 38; the cancellation boundary of the bottom proposition on 41; the compressed final qualification on 44; the categorical statement and diagonal margin on 46; the middle and lower corrections on 50; the two collapsed words in the support condition on 58; the kernel labels and unit calculation on 65; and the cancelled clause on 67. These are recoverable only in part and should not be quoted as clean mathematical statements without returning to the scans. In particular, a syntactically valid LaTeX rendering is not independent confirmation of a difficult reading.

All `\illegible{n}` marks estimate numbers of physically unreadable words after enlargement; none is a placeholder for a formula or diagram. Difficult symbols receive a proposed reading with doubt instead. A missing printed symbol is different from an unreadable word and remains a visible blank. For uncertain cancellation boundaries, the doubt may enclose a deletion macro; this records uncertainty about the state of the text as well as its wording.

Drawing geometry is reconstructed in TikZ rather than represented by inserted scan images. Relative placement, crossings, points, labels, arrows and enclosures were checked visually, but the paths are approximations to pen strokes, not facsimile tracings. The recto/verso distinction on 65–66 was corrected during the second reading: mirrored show-through is not counted as an additional drawing on 65. This decision, and each page's audit, is recorded in `records/visual_audit.md`.

The uncertainty labels are qualitative. “Medium” means a plausible direct reading with a remaining graphic ambiguity; “low” covers competing readings, physically collapsed ink, and marked readings on the most overwritten sheets. No numeric error rate or independent second human reading is claimed. The later research notes may pose reading questions, but the frozen page files are not amended from context or from expected mathematical correctness.
