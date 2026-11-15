# Notation table

This table was maintained from the first page and completed by a comparison of recurring forms against the scans before the transcription was frozen. It records visible forms, not a normalization to an expected mathematical statement; uncertainty remains explicit in the page files.

| Recurring visible form | LaTeX encoding | Evidence and limits of the reading |
|---|---|---|
| Double-stroked derived-functor capitals | `\mathbb R`, `\mathbb L` | Handwritten pages throughout; an undoubled `L` above a tensor is retained where that is what is visible, e.g. 100 and 102. |
| Raised exclamation mark attached to a functor | `f^!`, `\mathbb R^!f`, `\mathbb L^!f` | Scan 98 contains different placements. A prime is not substituted for `!`; the doubtful first exponent is marked. |
| Lower exclamation mark attached to R | `\mathbb R_!f`, `\mathbb R_!f_*` | Both forms occur, including 110–120; the additional star is retained only where visible. |
| Pullback star, pushforward star, and prime | `f^*`, `f_*`, `f'` | Read separately from an exclamation mark. The `f'`/`f^*` ambiguity on 102 is marked. |
| Dots on complexes | `L_\bullet`, `M^\bullet`, `K^\bullet` | Both upper and lower positions occur. They have not been made uniform; 134 even has an unadorned final `M`. |
| Derived tensor product | `\overset{\mathbb L}{\otimes}` or `\overset{L}{\otimes}` | Decoration follows the ink. An ordinary tensor, including the right side on 142, is not supplied with a derived decoration. |
| Curled/script initial H in Hom | `\mathcal Hom` | Clear in 98–106, 134, 144 and 146. The top three cursive forms on 136 are marked `\unsure{\mathcal Hom\|\operatorname{Hom}}`; the straighter middle forms remain plain. |
| Plain Hom and derived-category Hom | `\operatorname{Hom}`, `\operatorname{Hom}_{D(A)}` | Distinguished from the curled initial where visible, particularly on 104 and 136. This is a letterform decision, not a decision based on the expected category. |
| Script cohomology H and script O | `\mathcal H`, `\mathcal O` | Used when visible; an underlined O versus script O ambiguity on 102 is retained. |
| Typescript script F, G, H, S | `\mathcal F`, `\mathcal G`, `\mathcal H`, `\mathcal S` | Scan 99, including handwritten mathematical characters within the typescript. |
| Typescript doubled/overstruck H and S | `\mathbb H`, `\mathbb S` | Scan 99. These are distinct from the script alphabets on that page. |
| Typescript exterior-form-space capital | `A_x^p` | Scan 99: the visible A is not replaced by a wedge or Lambda. |
| Gothic letter in the ramification typescript | `\unsure{\mathfrak g\|\mathfrak J}` | Scan 121; the particular Gothic letter remains uncertain. |
| Underlined variables in reused typescripts | `\uline{p}`, `\uline{m}`, `\uline{N}`, etc. | An underline is encoded separately rather than converted to a Gothic alphabet. The plain typed `m` on 145 remains plain. |
| Uppercase/lowercase typescript ambiguities | `\unsure{S\|s}`, `\unsure{V\|v}` | Exponents on 125, 127 and 131, and the subscript of M on 139, respectively; neither has been silently regularized. |
| Dual sign and primes | `^\vee`, `'` | Dual signs on 134–146 are distinct from primes on resolutions and from complex dots. |
| Trace notation | `\operatorname{Tr}_*`, `\operatorname{tr}^*`, `\operatorname{Tr}` | Position and case are retained per occurrence; the extra doubtful mark on 132 remains marked. |
| Tor notation and bounds | `\operatorname{Tor}_i`, `[N,M]`, `[N,N']`, `[N-2d,M]` | The changes of endpoint letters on 138–142 remain visible, including the overwritten `M`/`N'` ambiguity. No sign conversion between homological and cohomological grading is imposed. |
| Isomorphism sign | `\simeq`, or a tilde over an arrow when visible | A horizontal isomorphism sign is not automatically made an arrow. |
| Plain horizontal connector versus arrow | `-`, `\text{---}`, or `\to` with an explicit `\unsure` alternative | Missing or doubtful arrowheads remain missing/doubtful, e.g. 100, 112 and 140. Diagram arrows likewise follow visible heads. |
| Literal diagram objects and labels | `tikzcd` inside `\diagram{...}` | The objects, labels and directions are transcribed even where an algebraic inconsistency results. Drawings and cancellation strokes are separate TikZ figures. |
| Single and double underlining | `\uline{...}`, `\uuline{...}` | Only visible strokes are encoded; heavy typewriter serifs on the headings of 139 and 143 are not underlining. |
| Double quotation marks | LaTeX opening two backticks and closing two apostrophes | Applied consistently; no guillemets were substituted for handwritten quotation marks. |
| Two short horizontal strokes in prose | `$\unsure{=}$` | Scans 124 and 144; retained as the sign, not expanded to a word in the transcription. A possible verbal expansion is listed below. |
| Circled section/part identifiers | `\textcircled{...}`, with `\margin` where marginal | 26 on 100, 30 on 124, 31 on 138, 32 on 144; subsections 1, 2, 3 on 100, 108, 122; letters a and b on 144, 146. They are not treated as a stated total page count. |
| Visible foliation and typescript page numbers | `\mspage{...}` | The small foliation 97–145 is retained, as are independently visible page numbers on reused typescripts. No missing number is supplied. |
| A versus Lambda on a coefficient sheaf | Literal `A_X` or `\Lambda_X` | Scan 128 retains the letter change visible there. |
| Struck and added text | `\deleted`, `\inserted` | A readable cancellation remains transcribed; additions are placed at the indicated attachment. Nested deletion within insertion is retained, including `et borné` on 146. |

## Editorial conventions for the doubts register

The register below includes every `\unsure` and `\illegible` occurrence in the final individual page files. “Line” means the approximate line in that page's UTF-8 LaTeX source, counted from its first line, not a reconstructed physical manuscript line; several short lines of handwriting can occur within one source paragraph. Alternatives are reported without replacing the first reading in the transcription. Confidence measures the first reading, not the truth of its mathematics: **high** means a residual small uncertainty, **medium** a plausible but genuinely uncertain reading, and **low** damaged, crossed, clipped or severely compressed strokes.

## Doubts register

| File (cote) | Scan | Approx. source line | First reading | Alternative(s) / limitation | Confidence |
|---|---|---|---|---|---|
| 33 | 098 | 3 | `supposons` | No secure alternative | medium |
| 33 | 098 | 3 | `le résolvant` | No secure alternative | medium |
| 33 | 098 | 9 | `!` | No secure alternative | medium |
| 33 | 098 | 10 | `\mathbb R` | No secure alternative | low |
| 33 | 098 | 18 | `et bidualisation` | No secure alternative | low |
| 33 | 098 | 18 | `commutation` | No secure alternative | low |
| 33 | 098 | 18 | `resp.` | No secure alternative | low |
| 33 | 098 | 25 | `\mathbb R` | No secure alternative | low |
| 33 | 100 | 12 | `ré` | No secure alternative | medium |
| 33 | 100 | 12 | `formellement` | No secure alternative | medium |
| 33 | 100 | 12 | `résoln` | No secure alternative | medium |
| 33 | 100 | 12 | `-` | \to | high |
| 33 | 100 | 13 | `et` | No secure alternative | medium |
| 33 | 100 | 16 | `-` | \to | high |
| 33 | 101 | 5 | `=` | \equiv | medium |
| 33 | 102 | 2 | `objets` | No secure alternative | medium |
| 33 | 102 | 2 | `hypertor` | No secure alternative | medium |
| 33 | 102 | 2 | `\underline O` | \mathcal O | medium |
| 33 | 102 | 2 | `Si` | No secure alternative | medium |
| 33 | 102 | 2 | `M_\bullet` | No secure alternative | medium |
| 33 | 102 | 4 | `défini convenablement` | No secure alternative | medium |
| 33 | 102 | 4 | `mais aussi` | No secure alternative | medium |
| 33 | 102 | 8 | `f'` | f^* | medium |
| 33 | 102 | 8 | `-` | = | medium |
| 33 | 102 | 10 | `qqfois` | No secure alternative | medium |
| 33 | 104 | 2 | `en` | No secure alternative | medium |
| 33 | 104 | 6 | `si on ne fait pas d'hyp.` | No secure alternative | medium |
| 33 | 104 | 6 | `coh` | No secure alternative | medium |
| 33 | 104 | 33 | `D^-` | D_0^- | medium |
| 33 | 104 | 33 | `K^-` | No secure alternative | medium |
| 33 | 104 | 33 | `mène` | No secure alternative | medium |
| 33 | 104 | 33 | `itou.` | idem. | medium |
| 33 | 106 | 7 | `R` | No secure alternative | low |
| 33 | 106 | 7 | `(où` | No secure alternative | low |
| 33 | 106 | 15 | `K` | No secure alternative | medium |
| 33 | 106 | 17 | `f_*` | No secure alternative | medium |
| 33 | 106 | 19 | `f` | No secure alternative | low |
| 33 | 106 | 20 | `\mathbb L` | No secure alternative | low |
| 33 | 106 | 25 | `OK` | No secure alternative | medium |
| 33 | 106 | 26 | `ne marche que si` | No secure alternative | low |
| 33 | 106 | 26 | `dc` | No secure alternative | low |
| 33 | 106 | 26 | `on se ramène` | No secure alternative | low |
| 33 | 106 | 26 | `\in` | No secure alternative | low |
| 33 | 106 | 26 | `A_{Y',Y}^{\sharp}` | No secure alternative | low |
| 33 | 106 | 40 | `\operatorname{Hom}^\bullet` | No secure alternative | low |
| 33 | 106 | 40 | `j^*` | No secure alternative | low |
| 33 | 106 | 48 | `1` | No secure alternative | low |
| 33 | 108 | 2 | `donnent` | donneraient | medium |
| 33 | 108 | 2 | `générale` | No secure alternative | medium |
| 33 | 108 | 2 | `provenant` | No secure alternative | medium |
| 33 | 108 | 6 | `plus en particulières` | un peu particulières | medium |
| 33 | 108 | 10 | `et` | No secure alternative | medium |
| 33 | 110 | 24 | `on` | No secure alternative | medium |
| 33 | 110 | 40 | `Y` | No secure alternative | medium |
| 33 | 112 | 5 | `Y` | No secure alternative | medium |
| 33 | 112 | 15 | `n'ont` | No secure alternative | low |
| 33 | 112 | 16 | `se réduit à` | No secure alternative | low |
| 33 | 112 | 22 | `$M_\bullet$` | No secure alternative | low |
| 33 | 112 | 23 | `bornée qui` | No secure alternative | low |
| 33 | 112 | 27 | `On n'a` | No secure alternative | low |
| 33 | 112 | 27 | `pas besoin` | No secure alternative | low |
| 33 | 112 | 27 | `en passant` | No secure alternative | low |
| 33 | 112 | 28 | `aux corps` | No secure alternative | low |
| 33 | 112 | 38 | `Hyp. dimension` | No secure alternative | low |
| 33 | 112 | 40 | `4` | \& | low |
| 33 | 112 | 43 | `de pr.` | No secure alternative | medium |
| 33 | 112 | 38 | `illegible{2}` | Physically obscured or unresolved strokes after enlargement | low |
| 33 | 113 | 22 | `normal` | No secure alternative | medium |
| 33 | 114 | 4 | `\otimes` | No secure alternative | medium |
| 33 | 114 | 17 | `gauches` | No secure alternative | medium |
| 33 | 114 | 17 | `le` | No secure alternative | medium |
| 33 | 114 | 22 | `Y'` | X' | medium |
| 33 | 114 | 22 | `Y` | X | medium |
| 33 | 114 | 25 | `Q` | No secure alternative | medium |
| 33 | 114 | 29 | `f.` | No secure alternative | medium |
| 33 | 114 | 32 | `Ça` | No secure alternative | medium |
| 33 | 116 | 2 | `i^*` | No secure alternative | medium |
| 33 | 116 | 6 | `A` | No secure alternative | medium |
| 33 | 116 | 7 | `f'` | f | medium |
| 33 | 116 | 8 | `g` | No secure alternative | medium |
| 33 | 116 | 10 | `A` | No secure alternative | medium |
| 33 | 116 | 25 | `\xrightarrow{\sim}` | No secure alternative | medium |
| 33 | 116 | 35 | `les` | No secure alternative | medium |
| 33 | 116 | 40 | `g'^*` | f'^* | medium |
| 33 | 117 | 21 | `V` | U | medium |
| 33 | 118 | 4 | `=` | No secure alternative | medium |
| 33 | 118 | 9 | `même pour $H^1$.` | No secure alternative | medium |
| 33 | 118 | 14 | `\mathbb Lg` | No secure alternative | medium |
| 33 | 118 | 17 | `voit` | No secure alternative | medium |
| 33 | 118 | 26 | `propre` | No secure alternative | medium |
| 33 | 118 | 30 | `on` | No secure alternative | medium |
| 33 | 118 | 32 | `\mathbb Rg` | No secure alternative | medium |
| 33 | 120 | 17 | `Équ` | No secure alternative | medium |
| 33 | 120 | 28 | `=` | No secure alternative | medium |
| 33 | 120 | 30 | `où` | No secure alternative | medium |
| 33 | 121 | 15 | `\mathfrak g` | \mathfrak J | medium |
| 33 | 121 | 16 | `\mathfrak g` | \mathfrak J | medium |
| 33 | 121 | 19 | `\eta` | \mathfrak N | medium |
| 33 | 121 | 20 | `\eta` | \mathfrak N | medium |
| 33 | 121 | 21 | `\eta` | \mathfrak N | medium |
| 33 | 121 | 21 | `\eta` | \mathfrak N | medium |
| 33 | 122 | 4 | `poisseux` | poussiéreux | medium |
| 33 | 122 | 6 | `immersion` | No secure alternative | medium |
| 33 | 122 | 8 | `astucieux` | No secure alternative | medium |
| 33 | 122 | 12 | `fondations` | fonctions | medium |
| 33 | 122 | 15 | `encore les fonctions $L$` | No secure alternative | low |
| 33 | 122 | 16 | `où utiliser le` | No secure alternative | low |
| 33 | 122 | 17 | `alors` | No secure alternative | low |
| 33 | 122 | 21 | `enfin` | No secure alternative | low |
| 33 | 122 | 16 | `illegible{1}` | Physically obscured or unresolved strokes after enlargement | low |
| 33 | 123 | 18 | `x` | X | medium |
| 33 | 124 | 5 | `Künneth` | No secure alternative | medium |
| 33 | 124 | 12 | `Notons` | No secure alternative | medium |
| 33 | 124 | 14 | `=` | No secure alternative | medium |
| 33 | 124 | 14 | `langage` | No secure alternative | medium |
| 33 | 124 | 14 | `différents` | No secure alternative | medium |
| 33 | 124 | 14 | `seules` | simples | medium |
| 33 | 124 | 14 | `finitude` | No secure alternative | medium |
| 33 | 124 | 14 | `dém.` | No secure alternative | medium |
| 33 | 124 | 16 | `schémas topologiques` | schémas algébriques | low |
| 33 | 124 | 16 | `profds` | No secure alternative | low |
| 33 | 124 | 16 | `nous` | No secure alternative | low |
| 33 | 125 | 3 | `S` | s | medium |
| 33 | 125 | 3 | `S` | s | medium |
| 33 | 125 | 4 | `zed` | No secure alternative | medium |
| 33 | 125 | 6 | `S` | s | medium |
| 33 | 125 | 6 | `S` | s | medium |
| 33 | 125 | 6 | `S` | s | medium |
| 33 | 125 | 8 | `pi-rational` | bi-rational | medium |
| 33 | 126 | 2 | `général` | No secure alternative | medium |
| 33 | 126 | 4 | `cts` | ét | medium |
| 33 | 126 | 8 | `cohomologies` | No secure alternative | medium |
| 33 | 126 | 8 | `corps` | No secure alternative | medium |
| 33 | 126 | 8 | `et des` | No secure alternative | medium |
| 33 | 126 | 8 | `à` | No secure alternative | medium |
| 33 | 127 | 5 | `0` | O | medium |
| 33 | 127 | 7 | `S` | s | medium |
| 33 | 128 | 2 | `définis` | No secure alternative | low |
| 33 | 128 | 2 | `(*)` | No secure alternative | low |
| 33 | 128 | 2 | `provenant de` | No secure alternative | low |
| 33 | 128 | 2 | `$\ell$-adique` | No secure alternative | low |
| 33 | 128 | 4 | `fonctorialité` | No secure alternative | medium |
| 33 | 128 | 2 | `illegible{1}` | Physically obscured or unresolved strokes after enlargement | low |
| 33 | 129 | 5 | `0` | O | medium |
| 33 | 130 | 2 | `de type` | No secure alternative | medium |
| 33 | 130 | 2 | `mapping cylindre` | No secure alternative | medium |
| 33 | 130 | 4 | `donc` | Tous | medium |
| 33 | 130 | 4 | `aux` | No secure alternative | medium |
| 33 | 130 | 6 | `f` | No secure alternative | medium |
| 33 | 131 | 3 | `S` | s | medium |
| 33 | 131 | 3 | `S` | s | medium |
| 33 | 131 | 3 | `0` | O | medium |
| 33 | 131 | 5 | `S` | s | medium |
| 33 | 131 | 5 | `S` | s | medium |
| 33 | 132 | 4 | `*` | No secure alternative | medium |
| 33 | 132 | 23 | `veut` | vérifie | medium |
| 33 | 132 | 23 | `utiles` | usuelles | medium |
| 33 | 132 | 32 | `est` | No secure alternative | medium |
| 33 | 133 | 3 | `t` | No secure alternative | medium |
| 33 | 133 | 3 | `t` | No secure alternative | medium |
| 33 | 133 | 3 | `t` | No secure alternative | medium |
| 33 | 133 | 5 | `\delta` | No secure alternative | medium |
| 33 | 134 | 2 | `finalement` | No secure alternative | medium |
| 33 | 134 | 2 | `\simeq` | = | medium |
| 33 | 134 | 8 | `homomorphisme` | No secure alternative | medium |
| 33 | 134 | 13 | `on a` | No secure alternative | medium |
| 33 | 134 | 21 | `M^\bullet=M_\bullet` | No secure alternative | medium |
| 33 | 136 | 3 | `\mathcal Hom` | \operatorname{Hom} | medium |
| 33 | 136 | 5 | `\mathcal Hom` | \operatorname{Hom} | medium |
| 33 | 136 | 5 | `\mathcal Hom` | \operatorname{Hom} | medium |
| 33 | 136 | 13 | `L_\bullet` | M_\bullet | low |
| 33 | 136 | 13 | `M_\bullet` | L_\bullet | low |
| 33 | 136 | 13 | `L_\bullet` | M_\bullet | low |
| 33 | 136 | 21 | `Que` | No secure alternative | low |
| 33 | 136 | 26 | `libres` | No secure alternative | medium |
| 33 | 136 | 27 | `désignant` | désignent | medium |
| 33 | 136 | 35 | `b` | 6 | medium |
| 33 | 136 | 21 | `illegible{1}` | Physically obscured or unresolved strokes after enlargement | low |
| 33 | 137 | 29 | `\bigcap_{q=1}^{\infty}` | No secure alternative | medium |
| 33 | 138 | 2 | `partielles` | No secure alternative | medium |
| 33 | 138 | 9 | `$i$` | No secure alternative | low |
| 33 | 138 | 9 | `compris aussi` | No secure alternative | low |
| 33 | 138 | 9 | `$-\infty$` | No secure alternative | low |
| 33 | 138 | 10 | `Tor` | No secure alternative | medium |
| 33 | 138 | 11 | `M` | N' | medium |
| 33 | 138 | 11 | `$N\in\mathbb Z$` | No secure alternative | medium |
| 33 | 138 | 13 | `M` | N' | medium |
| 33 | 138 | 15 | `Ceci posé,` | No secure alternative | medium |
| 33 | 138 | 19 | `M` | N' | medium |
| 33 | 138 | 20 | `Cela` | No secure alternative | low |
| 33 | 138 | 21 | `si` | No secure alternative | low |
| 33 | 138 | 21 | `ce qu'on peut en effet supposer` | No secure alternative | low |
| 33 | 138 | 21 | `que` | No secure alternative | low |
| 33 | 138 | 22 | `Pour` | No secure alternative | low |
| 33 | 138 | 25 | `$L_\bullet$` | No secure alternative | low |
| 33 | 138 | 27 | `N` | No secure alternative | low |
| 33 | 138 | 31 | `[N',M']` | [N',N_1] | medium |
| 33 | 139 | 27 | `*` | No secure alternative | medium |
| 33 | 139 | 32 | `V` | v | medium |
| 33 | 139 | 33 | `V` | v | medium |
| 33 | 139 | 33 | `V` | v | medium |
| 33 | 140 | 2 | `$[N]$` | No secure alternative | medium |
| 33 | 140 | 2 | `M` | N' | medium |
| 33 | 140 | 6 | `M` | N' | medium |
| 33 | 140 | 7 | `=` | No secure alternative | medium |
| 33 | 140 | 12 | `tout` | No secure alternative | medium |
| 33 | 140 | 12 | `\text{---}` | \longrightarrow | high |
| 33 | 140 | 15 | `sss` | ssi | medium |
| 33 | 140 | 16 | `si` | No secure alternative | medium |
| 33 | 140 | 16 | `quasi` | No secure alternative | medium |
| 33 | 140 | 17 | `$\exists$` | No secure alternative | medium |
| 33 | 140 | 23 | `\text{---}` | \to | high |
| 33 | 142 | 3 | `'` | No secure alternative | low |
| 33 | 142 | 3 | `+2d` | No secure alternative | low |
| 33 | 142 | 3 | `hom` | No secure alternative | low |
| 33 | 142 | 5 | `formellt` | No secure alternative | medium |
| 33 | 142 | 7 | `M` | No secure alternative | medium |
| 33 | 142 | 7 | `.` | No secure alternative | medium |
| 33 | 142 | 10 | `de` | No secure alternative | medium |
| 33 | 143 | 25 | `m` | No secure alternative | medium |
| 33 | 143 | 25 | `m` | No secure alternative | medium |
| 33 | 143 | 28 | `r^m` | r^u | medium |
| 33 | 143 | 30 | `m` | n | medium |
| 33 | 143 | 31 | `$r^w$` | No secure alternative | medium |
| 33 | 144 | 30 | `$\operatorname{Hom}^0(Rf_!$` | No secure alternative | low |
| 33 | 144 | 32 | `f_*` | f | medium |
| 33 | 144 | 34 | `$\operatorname{Hom}$` | No secure alternative | low |
| 33 | 144 | 34 | `$A$` | No secure alternative | low |
| 33 | 144 | 39 | `pas besoin` | No secure alternative | medium |
| 33 | 144 | 44 | `$=$` | No secure alternative | medium |
| 33 | 146 | 6 | `\chi` | \gamma | medium |
| 33 | 146 | 6 | `*` | No secure alternative | medium |
| 33 | 146 | 16 | `0` | No secure alternative | medium |
| 33 | 146 | 18 | `\varphi_i` | \varphi | medium |
| 33 | 146 | 18 | `un hom` | No secure alternative | medium |
| 33 | 146 | 21 | `lin.` | No secure alternative | low |
| 33 | 146 | 35 | `préc.` | No secure alternative | low |
| 33 | 146 | 21 | `illegible{1}` | Physically obscured or unresolved strokes after enlargement | low |
| 33 | 146 | 35 | `illegible{1}` | Physically obscured or unresolved strokes after enlargement | low |

## Abbreviations encountered

Expansions in this table are editorial suggestions only. They have not been inserted into the transcription; punctuation and abbreviated forms remain as on the page. A doubtful abbreviated form remains doubtful even when its proposed expansion is familiar.

| Form in the transcription | Suggested expansion or meaning |
|---|---|
| `th`, `th.` | théorème |
| `Prop.` | proposition |
| `hyp`, `hyp.`, `Hyp.` | hypothèse(s) |
| `imm`, `imm.` | immersion |
| `NB`, `N.B.` | nota bene |
| `i.e`, `i.e.` | id est |
| `resp.`, `resp` | respectivement / respectively, according to language |
| `cf.` | confer; compare |
| `hom`, `hom.` | homomorphisme(s); in `K(A)`, homomorphisms of complexes |
| `isom`, `isom.` | isomorphisme |
| `quasi-isom`, `quasi. isom` | quasi-isomorphisme(s) |
| `résoln` | résolution (reading itself uncertain on 100) |
| `qqfois` | quelquefois (uncertain reading on 102) |
| `sup.` | supérieurement, in “bornés sup.” |
| `inj` | injectif |
| `dc` | donc (uncertain reading in the marginal correction on 106) |
| `op.` | opération(s) |
| `Tor-dim`, `Tor-dim.`, `tor-dim.` | Tor-dimension |
| `Ext-dim.` | Ext-dimension |
| `dim`, `dim.` | dimension |
| `ch`, `ch.`, `changt` | changement; abbreviated variants are context-dependent |
| `coh`, `coh.` | cohomologie or cohérent/cohérente, according to syntax |
| `ps. coh`, `ps. coh.` | pseudo-cohérent |
| `loc.`, `loc` | localement |
| `cte`, `cts` | constante, constants |
| `qu. cpt`, `q. cpt` | quasi-compact |
| `qu. sép` | quasi-séparé |
| `qui. qs`, `qui. cp` | tentative: quasi-séparé, quasi-compact; the abbreviated ink on 112 is retained literally |
| `bcpte` | tentative: bicomplexe (112) |
| `t.f.` | type fini |
| `noeth.` | noethérien |
| `néc.` | nécessairement |
| `mb`, `mbres` | membre, membres (of an equality/formula) |
| `tt` | tout |
| `tjs` | toujours |
| `alg.` | algébrique |
| `car.` | caractéristique |
| `p.ex.`, `p. ex.` | par exemple |
| `pt`, `pts` | point, points |
| `géom` | géométrique |
| `ét` (including the site subscript) | étale |
| `nb` | nombre |
| `coeff`, `coeff.` | coefficient(s) |
| `comm.` | commutation |
| `dém.` | démonstration (uncertain reading on 124) |
| `profds` | profonds (uncertain reading on 124) |
| `formellt` | formellement (uncertain reading on 142) |
| `can.` | canonique |
| `dér.` | dérivé(s) |
| `lin.` | linéaire (inside cancelled text on 146) |
| `préc.` | précédent(s) (inside cancelled text on 146) |
| `pr.` | projection, in projection labels |
| `hd`, `w.hd` | homological dimension, weak homological dimension, in the reused English algebra typescript |
| `SGA` | Séminaire de géométrie algébrique |
| `EGA` | Éléments de géométrie algébrique |
| `O.K.`, `OK` | approval/acceptance annotation; no mathematical expansion supplied |
| Two-stroke prose sign transcribed `$\unsure{=}$` | tentative verbal value “même”; the sign itself, rather than this expansion, is transcribed (124, 144) |
| `Ob` | object(s) of a category; retained as mathematical notation |
| `[Co]`, `[A7]`, numerical bracketed references | Bibliographical keys, not silently expanded; the cited source is not identified from this package alone. |

## Legibility and limitations

All 49 whole-page images and both supplied halves were read in order, then read again for the audit; difficult areas were also enlarged or rotated. No OCR was used. The reused typescripts are generally much clearer than the handwritten pages, but small typed indices, overwritten corrections and distinctions between capitals and lowercase letters still cause uncertainty. Their authorship is not established merely by their reuse in this manuscript.

The least secure readings are the dense or faint additions on 106 and 112, the overlapping cancellations on 122, the lower clipped wording on 128, the heavily cancelled passage and overwritten endpoints on 138, the overwritten symbols around 136–142, and the struck passages on 146. The `\illegible` entries concern words obscured by ink or irrecoverable strokes after enlargement; mathematical symbols are instead represented by a proposed reading with `\unsure`. TikZ drawings are geometric transcriptions, not facsimiles of pen texture. Readable mathematical inconsistencies, unusual spellings, omissions and changes of notation have deliberately been left in the transcription. The register makes no statistical claim of accuracy and cannot guarantee that every unmarked reading is correct.
