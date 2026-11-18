# Notation table and reading doubts

## Package notation table

This table records the primary reader's comparison of recurring signs before the transcription was frozen and before the context archive was opened. A shared doubt is kept shared; resemblance of mathematical roles was not used to identify two different shapes. TeX grouping braces and math-mode delimiters are editorial typesetting syntax, not extra manuscript content.

| Written sign or convention | LaTeX treatment | Comparison and remaining caution |
|---|---|---|
| Plain Latin category and object letters | `C`, `E`, `F`, `G`, `H`, `K`, `P`, `S`, `T`, `X`, `Y`, with the visible case | A curved or quickly written capital is not automatically made calligraphic; case and alphabet doubts remain local. |
| Calligraphic category and sheaf letters | `\mathcal C`, `\mathcal E`, `\mathcal P`, `\mathcal O` | Kept distinct from plain capitals where the script stroke is visible; particularly the categorical pages 159–161 and the sheaf pages. |
| Crossed-out Gothic group-category name | `\mathfrak{G}`, locally `\unsure{\mathfrak{G}}` | Scan 141; the cancelled occurrence is less secure than the following one. |
| Looped descending torsor-functor name | `\unsure{\mathfrak{Z}}` | All occurrences on 141 and 143 were compared directly. The alphabet/name remains unresolved; the same tentative Gothic Z is used throughout those pages. |
| Barred and crossed Gothic F-shaped letter | `\mathfrak F` / `\mathfrak{F}` | Scan 152 has a visibly different shape from the looped symbol on 141/143. These were compared again before freeze and were not conflated. |
| Small looped symbol in group formulas | `\unsure{\mathfrak z|\zeta}` | Repeated on 177; the same ordered alternatives are kept, including inside Hom and arrow targets. |
| Raised `gr` on Hom | `\operatorname{Hom}^{\mathrm{gr}}` | Scan 141: an abbreviation in the exponent, not a prime. |
| Underlined Hom and sheaf letters | `\underline{\operatorname{Hom}}`, `\underline A` | The underline is retained; a proposed alternate script alphabet is not substituted. |
| Lowercase fundamental-group and component signs | `\pi_1`, `\pi_0` | Kept distinct from uppercase Pi, including the repeated component and simplicial formulas on 179–186. |
| Uppercase Pi, superscript/subscript 1 | `\Pi^1`, `\Pi_1` | The location of 1 follows the ink, not an imposed convention for group versus torsor functor. |
| Large title on 175 | `\unsure{\pi_2|\Pi_2}` | Size alone does not settle case; the doubt survives comparison. |
| Replaced functor name on 165–170 | `\Pi^1` and `\Phi`, with struck predecessors inside `\deleted` | The live round Phi on 166–169 differs visibly from Pi on 165/170. Revision is retained instead of harmonizing the entire section. |
| Tilde and bar over letters/groups | `\widetilde{...}`, `\overline{...}` | Checked separately from primes and show-through. Later unbarred or untilde occurrences are not silently supplied with the earlier mark. |
| Pointing letter in torsor formulas | `\xi` where clear | Distinct from the provisional Gothic functor letter; the point in the diagram on 181 has a clear xi-like form. |
| Pointing letter on 185–186 | `\unsure{\zeta|\xi}`, and the corresponding powers | Compared together: the single upper loop and long descender favour zeta, but the alphabet remains uncertain. All live occurrences use the same ordered alternatives. |
| Greek parameters and arrows' labels | `\alpha`, `\beta`, `\gamma`, `\lambda`, `\varphi`, etc., with local doubts | Labels are read separately from objects; examples of unresolved forms include Lambda/A on 145 and S/delta on 172. |
| Primes, double primes and triple primes | `'`, `''`, `'''` | Kept separately from superscript circles, powers and punctuation. Unclear primes on 142, 147, 177 and 187 remain marked. |
| Circle-like superscripts | `^\circ`, `^{(0)}`, `^0`, according to visible placement | Not all are read as a numeral zero. Scan 170's small circle and scan 168's different forms are retained. |
| Stars and their positions | `_*`, `^*`, `u_*(\alpha)` | Subscripts and superscripts are not interchanged; especially the simplicial indices on 179–186. |
| Ambiguous degree on 176 | `\unsure{I|2}`, `\unsure{2|1}`, as locally written | No cohomological degree is supplied from what a spectral sequence would normally require. |
| E/F discrepancies | The visible `E` or `F`, or `\unsure{E|F}` in context | In particular, `E_S` on 169 and the final `E` in both functors on 186 are retained; scan 158's final expression remains E/F uncertain. |
| Directed inverse and direct limits | `\varprojlim`, `\varinjlim` | Used where a direction is actually visible, rather than inferred from the argument. |
| Limit with a plain underline | `\underline{\lim}`, sometimes with an index below | Scan 176 was rechecked: several lower strokes have no arrowhead, unlike the explicit direct-limit arrow in the upper H² chain. |
| Plain connecting strokes | `-`, `\mathbin{-}`, or TikZ `dash` | A morphism is not given an arrowhead merely because it is a morphism. Headless strokes remain on 142, 145, 151, 153, 157, 159, 162, 181 and 187. |
| Parallel diagram arrows | Separate shifted TikZ arrows | Arrow number, direction, headlessness and labels follow the image; the simplicial diagrams retain two and three separate arrows. |
| Equality-like shorthand in prose | Literal `$=$` | For example `de = de` on 156, `des =` on 185, and the signs around the question on 180. Not expanded to a French word. |
| Double quotation marks | Two backticks and two apostrophes | Used for manuscript quotation marks. A ditto mark in the component diagram on 181 is retained as a separate pair of strokes. |
| Underlining | `\uline`, `\uuline`, or ordinary math `\underline` | Separate underlined words are not merged automatically; the double underline on `ponctué` on 186 is retained. |
| Strikes and insertions | `\deleted{...}`, `\inserted{...}` | An insertion follows its caret/connecting stroke where recoverable; a crossed readable word is never made live merely because it completes the sentence. |
| Circles and transposition strokes | TikZ inside `\figure` | The circle around `universels` on 160 and the circled inserted `loc` on 180 are retained, as are the free drawings on 176, 183 and 184. |

## How to use the doubt tables

The current-doubt table below is generated from the final page fragments, so its readings agree with the frozen transcription. It distinguishes the preferred reading from any alternative inside the macro; a single tentative reading does not imply that no other reading is possible. Confidence is deliberately conservative, and **low** means that the ink does not support a confident identification, not that an alternative has been proved correct.

The line locators refer to physical lines of the individual TeX page fragment, **not to a claimed count of handwritten lines**: paragraphs were reflowed as the prompt permits. The scan number and local text identify the corresponding place on the image; selected difficult loci are described more precisely after the table. The auxiliary `doubts_rows.tsv` and `audit_changes.tsv` preserve the reading history, including superseded first-pass proposals; they are not competing final transcriptions.


## Current doubt-macro table

This table reflects the macros in the **current page fragments**. The historical working file `doubts_rows.tsv` contains superseded readings; those historical readings and alternatives are not added here.

Every locator is a one-based **physical TeX source line, not a manuscript line**. For scan NNN, the source is `pages/MPL_29_141-187_29_scanNNN.tex`. Each macro occurrence has its own row, including repeated occurrences on one source line and nested doubt macros.

Confidence defaults conservatively to **low**; this is a mechanical default, not an independent visual assessment. A supplied confidence is carried only when the same scan has an exact matching current reading in `doubts_rows.tsv`. Alternatives shown here come only from unescaped top-level `|` separators in the current macro. The TSV index preserves each full argument exactly; the table displays source newlines as line breaks.

| File / cote | Scan | Approximate locator | Reading | Alternatives | Confidence |
|---|---:|---|---|---|---|
| 29.pdf / 29 | 141 | TeX source line 6 (occurrence 1) | <code>$\mathfrak{G}$ catégorie de groupes</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 7 (occurrence 2) | <code>quelconque</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 15 (occurrence 3) | <code>(G'\times G')</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 21 (occurrence 4) | <code>et</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 22 (occurrence 5) | <code>plats</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 28 (occurrence 6) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 28 (occurrence 7) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 29 (occurrence 8) | <code>classes</code> | — | medium |
| 29.pdf / 29 | 141 | TeX source line 32 (occurrence 9) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 34 (occurrence 10) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 37 (occurrence 11) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 41 (occurrence 12) | <code>$u_*(\alpha)=v_*$</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 55 (occurrence 13) | <code>plat</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 55 (occurrence 14) | <code>on</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 61 (occurrence 15) | <code>résultera</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 63 (occurrence 16) | <code>localement</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 64 (occurrence 17) | <code>(S_1,a_1)=(P,\xi)</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 65 (occurrence 18) | <code>revient à remplacer</code> | — | low |
| 29.pdf / 29 | 141 | TeX source line 68 (occurrence 19) | <code>g</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 5 (occurrence 20) | <code>S</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 9 (occurrence 21) | <code>je dis que</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 14 (occurrence 22) | <code>fait</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 18 (occurrence 23) | <code>``naturelle''</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 24 (occurrence 24) | <code>S'_1</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 36 (occurrence 25) | <code>$\xi$ en $\xi$</code> | — | low |
| 29.pdf / 29 | 142 | TeX source line 36 (occurrence 26) | <code>...</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 7 (occurrence 27) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 8 (occurrence 28) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 8 (occurrence 29) | <code>\mathfrak{Z}</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 14 (occurrence 30) | <code>va</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 16 (occurrence 31) | <code>ens</code> | <code>cat</code> | low |
| 29.pdf / 29 | 143 | TeX source line 22 (occurrence 32) | <code>est</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 23 (occurrence 33) | <code>vraisemblt</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 23 (occurrence 34) | <code>inutiles</code> | — | low |
| 29.pdf / 29 | 143 | TeX source line 23 (occurrence 35) | <code>dessus</code> | — | low |
| 29.pdf / 29 | 145 | TeX source line 8 (occurrence 36) | <code>p</code> | — | low |
| 29.pdf / 29 | 145 | TeX source line 8 (occurrence 37) | <code>S''</code> | — | low |
| 29.pdf / 29 | 145 | TeX source line 21 (occurrence 38) | <code>-</code> | <code>\longrightarrow</code> | low |
| 29.pdf / 29 | 145 | TeX source line 25 (occurrence 39) | <code>p_i^\alpha p_{ij}^{\alpha\beta}</code> | — | low |
| 29.pdf / 29 | 145 | TeX source line 42 (occurrence 40) | <code>-</code> | <code>\longrightarrow</code> | low |
| 29.pdf / 29 | 145 | TeX source line 48 (occurrence 41) | <code>-</code> | <code>\longrightarrow</code> | low |
| 29.pdf / 29 | 145 | TeX source line 51 (occurrence 42) | <code>13</code> | <code>23</code> | low |
| 29.pdf / 29 | 145 | TeX source line 56 (occurrence 43) | <code>\Lambda</code> | <code>A</code> | low |
| 29.pdf / 29 | 145 | TeX source line 68 (occurrence 44) | <code>comm. de</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 5 (occurrence 45) | <code>diag</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 6 (occurrence 46) | <code>\theta_2</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 7 (occurrence 47) | <code>s''</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 8 (occurrence 48) | <code>\theta_3</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 10 (occurrence 49) | <code>Rem.</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 11 (occurrence 50) | <code>E'''</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 13 (occurrence 51) | <code>on a $\overline{s}''=\operatorname{diag}$</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 14 (occurrence 52) | <code>\overline{s}'''</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 16 (occurrence 53) | <code>derniers</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 16 (occurrence 54) | <code>jonction</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 17 (occurrence 55) | <code>comme</code> | — | low |
| 29.pdf / 29 | 147 | TeX source line 18 (occurrence 56) | <code>Enfin, on peut supposer que $s''=\overline{s}''$.</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 7 (occurrence 57) | <code>généralt</code> | — | medium |
| 29.pdf / 29 | 149 | TeX source line 21 (occurrence 58) | <code>étale</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 22 (occurrence 59) | <code>étale</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 24 (occurrence 60) | <code>il faut</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 25 (occurrence 61) | <code>les fibres</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 25 (occurrence 62) | <code>aient une composante connexe</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 26 (occurrence 63) | <code>-</code> | <code>\longrightarrow</code> | low |
| 29.pdf / 29 | 149 | TeX source line 27 (occurrence 64) | <code>par exemple si</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 28 (occurrence 65) | <code>\illegible{1}</code> | No reading proposed; the macro encodes an unreadable-word count. | low |
| 29.pdf / 29 | 149 | TeX source line 36 (occurrence 66) | <code>uni</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 38 (occurrence 67) | <code>$S'\to S$</code> | — | low |
| 29.pdf / 29 | 149 | TeX source line 39 (occurrence 68) | <code>$X'\to X$</code> | — | low |
| 29.pdf / 29 | 150 | TeX source line 3 (occurrence 69) | <code>X</code> | — | low |
| 29.pdf / 29 | 150 | TeX source line 29 (occurrence 70) | <code>Mandeuil</code> | — | low |
| 29.pdf / 29 | 151 | TeX source line 7 (occurrence 71) | <code>rev. étale</code> | — | low |
| 29.pdf / 29 | 151 | TeX source line 9 (occurrence 72) | <code>-</code> | <code>\longrightarrow</code> | low |
| 29.pdf / 29 | 151 | TeX source line 11 (occurrence 73) | <code>on peut</code> | — | low |
| 29.pdf / 29 | 151 | TeX source line 11 (occurrence 74) | <code>=</code> | — | low |
| 29.pdf / 29 | 151 | TeX source line 33 (occurrence 75) | <code>i</code> | — | low |
| 29.pdf / 29 | 151 | TeX source line 37 (occurrence 76) | <code>-</code> | <code>\to</code> | low |
| 29.pdf / 29 | 151 | TeX source line 41 (occurrence 77) | <code>-</code> | <code>\to</code> | low |
| 29.pdf / 29 | 152 | TeX source line 6 (occurrence 78) | <code>\mathcal{E}_\pi^\pi</code> | — | low |
| 29.pdf / 29 | 152 | TeX source line 10 (occurrence 79) | <code>min</code> | — | low |
| 29.pdf / 29 | 152 | TeX source line 21 (occurrence 80) | <code>\mathcal E</code> | — | low |
| 29.pdf / 29 | 152 | TeX source line 22 (occurrence 81) | <code>F</code> | <code>\pi</code> | low |
| 29.pdf / 29 | 152 | TeX source line 26 (occurrence 82) | <code>E\times_\pi U</code> | — | low |
| 29.pdf / 29 | 152 | TeX source line 32 (occurrence 83) | <code>*</code> | — | low |
| 29.pdf / 29 | 152 | TeX source line 42 (occurrence 84) | <code>Changt de base</code> | — | medium |
| 29.pdf / 29 | 152 | TeX source line 54 (occurrence 85) | <code>\pi_S</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 3 (occurrence 86) | <code>revêtements</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 3 (occurrence 87) | <code>variétés</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 3 (occurrence 88) | <code>locaux</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 3 (occurrence 89) | <code>finis</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 10 (occurrence 90) | <code>2</code> | <code>1</code> | low |
| 29.pdf / 29 | 153 | TeX source line 10 (occurrence 91) | <code>($n$ un entier)</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 18 (occurrence 92) | <code>étale</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 20 (occurrence 93) | <code>G</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 22 (occurrence 94) | <code>n-1,a</code> | <code>n-1</code> | low |
| 29.pdf / 29 | 153 | TeX source line 22 (occurrence 95) | <code>dimension</code> | <code>diminution</code> | low |
| 29.pdf / 29 | 153 | TeX source line 29 (occurrence 96) | <code>(i)</code> | <code>(iii)</code> | low |
| 29.pdf / 29 | 153 | TeX source line 29 (occurrence 97) | <code>(iii\ \mathrm{bis})</code> | <code>(ii\ \mathrm{bis})</code> | low |
| 29.pdf / 29 | 153 | TeX source line 29 (occurrence 98) | <code>théorème de Galois</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 30 (occurrence 99) | <code>(iii)</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 31 (occurrence 100) | <code>morphismes</code> | — | low |
| 29.pdf / 29 | 153 | TeX source line 39 (occurrence 101) | <code>d'inertie</code> | <code>d'isotropie</code> | medium |
| 29.pdf / 29 | 153 | TeX source line 39 (occurrence 102) | <code>d'inertie</code> | <code>d'isotropie</code> | medium |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 103) | <code>fibre de</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 104) | <code>les</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 105) | <code>celui</code> | <code>ceux</code> | medium |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 106) | <code>X^n</code> | <code>X</code> | low |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 107) | <code>celui</code> | <code>ceux</code> | medium |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 108) | <code>isomorphe</code> | <code>bijection</code> | low |
| 29.pdf / 29 | 154 | TeX source line 5 (occurrence 109) | <code>enlever</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 8 (occurrence 110) | <code>on sait</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 9 (occurrence 111) | <code>induit</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 9 (occurrence 112) | <code>d'où un homom.</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 9 (occurrence 113) | <code>morphisme</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 9 (occurrence 114) | <code>hom.</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 13 (occurrence 115) | <code>Y</code> | <code>X</code> | low |
| 29.pdf / 29 | 154 | TeX source line 13 (occurrence 116) | <code>qui est un</code> | <code>d'où un</code> | low |
| 29.pdf / 29 | 154 | TeX source line 13 (occurrence 117) | <code>morphisme</code> | — | low |
| 29.pdf / 29 | 154 | TeX source line 14 (occurrence 118) | <code>?</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 4 (occurrence 119) | <code>X</code> | <code>X_0</code> | low |
| 29.pdf / 29 | 155 | TeX source line 5 (occurrence 120) | <code>donc</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 6 (occurrence 121) | <code>$x\in X_0$</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 6 (occurrence 122) | <code>puisque est connexe</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 7 (occurrence 123) | <code>l'ens</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 8 (occurrence 124) | <code>fidelt</code> | — | medium |
| 29.pdf / 29 | 155 | TeX source line 13 (occurrence 125) | <code>\prime</code> | — | low |
| 29.pdf / 29 | 155 | TeX source line 27 (occurrence 126) | <code>Comme</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 3 (occurrence 127) | <code>dans</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 6 (occurrence 128) | <code>en $y$</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 6 (occurrence 129) | <code>pts géom.</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 6 (occurrence 130) | <code>les classes</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 6 (occurrence 131) | <code>sous $H$</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 11 (occurrence 132) | <code>\Leftarrow</code> | — | low |
| 29.pdf / 29 | 156 | TeX source line 14 (occurrence 133) | <code>loc.</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 3 (occurrence 134) | <code>Remonter</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 3 (occurrence 135) | <code>par ex. fini</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 6 (occurrence 136) | <code>sans</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 7 (occurrence 137) | <code>sans inertie</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 9 (occurrence 138) | <code>X/G\to X</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 17 (occurrence 139) | <code>opère trivialt</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 18 (occurrence 140) | <code>X</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 20 (occurrence 141) | <code>on a</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 20 (occurrence 142) | <code>finissons-en pour $(ii)$</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 23 (occurrence 143) | <code>et on est ramené à</code> | — | low |
| 29.pdf / 29 | 157 | TeX source line 24 (occurrence 144) | <code>un</code> | <code>ens.</code> | low |
| 29.pdf / 29 | 157 | TeX source line 24 (occurrence 145) | <code>X(\alpha)</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 11 (occurrence 146) | <code>Poser</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 11 (occurrence 147) | <code>Soit</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 11 (occurrence 148) | <code>quotients par</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 11 (occurrence 149) | <code>injection</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 11 (occurrence 150) | <code>($X,Y$ conn.)</code> | <code>($X$ connex.)</code> | low |
| 29.pdf / 29 | 158 | TeX source line 33 (occurrence 151) | <code>f</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 34 (occurrence 152) | <code>de</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 42 (occurrence 153) | <code>$Y$ connexe</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 42 (occurrence 154) | <code>Y</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 42 (occurrence 155) | <code>connexe</code> | <code>connexes</code> | low |
| 29.pdf / 29 | 158 | TeX source line 44 (occurrence 156) | <code>le morphisme</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 48 (occurrence 157) | <code>c.à.d.</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 48 (occurrence 158) | <code>Alors</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 49 (occurrence 159) | <code>connexe d'un revêtement est galoisienne</code> | — | low |
| 29.pdf / 29 | 158 | TeX source line 52 (occurrence 160) | <code>E(X/H)</code> | <code>F(X/H)</code> | medium |
| 29.pdf / 29 | 159 | TeX source line 3 (occurrence 161) | <code>1</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 9 (occurrence 162) | <code>les</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 9 (occurrence 163) | <code>les sommes $\coprod(f_i:X_i\to Y)$</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 23 (occurrence 164) | <code>les</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 25 (occurrence 165) | <code>points</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 26 (occurrence 166) | <code>$\xi\in$</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 28 (occurrence 167) | <code>X/H</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 28 (occurrence 168) | <code>est non ramifié</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 29 (occurrence 169) | <code>Y</code> | — | low |
| 29.pdf / 29 | 159 | TeX source line 39 (occurrence 170) | <code>-</code> | <code>\to</code> | low |
| 29.pdf / 29 | 160 | TeX source line 13 (occurrence 171) | <code>Ce</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 21 (occurrence 172) | <code>restreint</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 21 (occurrence 173) | <code>façon</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 21 (occurrence 174) | <code>connue</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 21 (occurrence 175) | <code>permettant</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 21 (occurrence 176) | <code>(i), (ii)</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 29 (occurrence 177) | <code>satisfont à certaines conditions</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 38 (occurrence 178) | <code>correspondantes</code> | — | low |
| 29.pdf / 29 | 160 | TeX source line 40 (occurrence 179) | <code>resp.!</code> | — | medium |
| 29.pdf / 29 | 160 | TeX source line 42 (occurrence 180) | <code>bons</code> | — | medium |
| 29.pdf / 29 | 162 | TeX source line 6 (occurrence 181) | <code>k</code> | <code>K</code> | low |
| 29.pdf / 29 | 162 | TeX source line 7 (occurrence 182) | <code>enfin</code> | — | low |
| 29.pdf / 29 | 162 | TeX source line 17 (occurrence 183) | <code>Y'</code> | <code>X'</code> | low |
| 29.pdf / 29 | 162 | TeX source line 18 (occurrence 184) | <code>prouvé</code> | — | low |
| 29.pdf / 29 | 162 | TeX source line 18 (occurrence 185) | <code>en</code> | — | low |
| 29.pdf / 29 | 162 | TeX source line 18 (occurrence 186) | <code>se</code> | — | low |
| 29.pdf / 29 | 162 | TeX source line 18 (occurrence 187) | <code>comparaison</code> | — | low |
| 29.pdf / 29 | 163 | TeX source line 3 (occurrence 188) | <code>dans $f$</code> | — | low |
| 29.pdf / 29 | 163 | TeX source line 4 (occurrence 189) | <code>Par les plats)</code> | — | low |
| 29.pdf / 29 | 164 | TeX source line 3 (occurrence 190) | <code>pro Groupe</code> | — | medium |
| 29.pdf / 29 | 165 | TeX source line 17 (occurrence 191) | <code>un</code> | — | low |
| 29.pdf / 29 | 165 | TeX source line 17 (occurrence 192) | <code>si</code> | — | low |
| 29.pdf / 29 | 165 | TeX source line 18 (occurrence 193) | <code>isom.</code> | — | low |
| 29.pdf / 29 | 165 | TeX source line 18 (occurrence 194) | <code>tel</code> | — | low |
| 29.pdf / 29 | 165 | TeX source line 26 (occurrence 195) | <code>$f_i$</code> | — | low |
| 29.pdf / 29 | 165 | TeX source line 26 (occurrence 196) | <code>-</code> | <code>\to</code> | low |
| 29.pdf / 29 | 165 | TeX source line 28 (occurrence 197) | <code>alors il s'ensuit</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 3 (occurrence 198) | <code>\Pi</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 3 (occurrence 199) | <code>Je</code> | <code>S</code> | low |
| 29.pdf / 29 | 166 | TeX source line 3 (occurrence 200) | <code>\bar\xi'</code> | <code>\bar\xi_i'</code> | low |
| 29.pdf / 29 | 166 | TeX source line 5 (occurrence 201) | <code>\Pi</code> | <code>\Phi</code> | low |
| 29.pdf / 29 | 166 | TeX source line 7 (occurrence 202) | <code>reste</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 7 (occurrence 203) | <code>on</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 24 (occurrence 204) | <code>deux</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 24 (occurrence 205) | <code>partout</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 24 (occurrence 206) | <code>alors</code> | — | low |
| 29.pdf / 29 | 166 | TeX source line 24 (occurrence 207) | <code>on gagne</code> | — | medium |
| 29.pdf / 29 | 167 | TeX source line 3 (occurrence 208) | <code>S</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 5 (occurrence 209) | <code>minimal</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 7 (occurrence 210) | <code>pour que</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 7 (occurrence 211) | <code>\Phi(\pi)</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 7 (occurrence 212) | <code>ait un</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 7 (occurrence 213) | <code>élémt</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 9 (occurrence 214) | <code>corresp. d'élémts</code> | <code>corresp. d'éléments</code> | low |
| 29.pdf / 29 | 167 | TeX source line 9 (occurrence 215) | <code>être</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 9 (occurrence 216) | <code>réduire</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 15 (occurrence 217) | <code>mbr</code> | <code>mb.</code> | medium |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 218) | <code>les groupes</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 219) | <code>on gagne</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 220) | <code>les uns inclus dans les autres</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 221) | <code>est</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 222) | <code>on</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 223) | <code>encore fibré sur</code> | — | low |
| 29.pdf / 29 | 167 | TeX source line 19 (occurrence 224) | <code>le groupe est</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 3 (occurrence 225) | <code>sait</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 3 (occurrence 226) | <code>la pro. de la descente finie</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 3 (occurrence 227) | <code>constant</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 3 (occurrence 228) | <code>\pi_{S^{(0)}}</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 11 (occurrence 229) | <code>l'on fait maintenant comme suit</code> | — | low |
| 29.pdf / 29 | 168 | TeX source line 11 (occurrence 230) | <code>elle est</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 3 (occurrence 231) | <code>si on a fixé un</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 3 (occurrence 232) | <code>si on a</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 3 (occurrence 233) | <code>à travers</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 5 (occurrence 234) | <code>G</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 8 (occurrence 235) | <code>Exemple</code> | <code>Exemples</code> | low |
| 29.pdf / 29 | 169 | TeX source line 8 (occurrence 236) | <code>de</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 8 (occurrence 237) | <code>génération</code> | — | low |
| 29.pdf / 29 | 169 | TeX source line 8 (occurrence 238) | <code>présent</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 3 (occurrence 239) | <code>tte</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 5 (occurrence 240) | <code>tt</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 5 (occurrence 241) | <code>En effet l'intersection</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 5 (occurrence 242) | <code>puisque</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 5 (occurrence 243) | <code>les</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 8 (occurrence 244) | <code>et si</code> | — | low |
| 29.pdf / 29 | 170 | TeX source line 10 (occurrence 245) | <code>On aura</code> | — | medium |
| 29.pdf / 29 | 171 | TeX source line 3 (occurrence 246) | <code>Revêtts</code> | — | medium |
| 29.pdf / 29 | 171 | TeX source line 9 (occurrence 247) | <code>fid plat de type f. sur $S$</code> | — | low |
| 29.pdf / 29 | 171 | TeX source line 10 (occurrence 248) | <code>fid plat sur $S$</code> | — | low |
| 29.pdf / 29 | 171 | TeX source line 21 (occurrence 249) | <code>loc. noeth.</code> | — | low |
| 29.pdf / 29 | 171 | TeX source line 29 (occurrence 250) | <code>\text{étales}</code> | — | low |
| 29.pdf / 29 | 171 | TeX source line 34 (occurrence 251) | <code>les ramener</code> | — | medium |
| 29.pdf / 29 | 171 | TeX source line 38 (occurrence 252) | <code>T</code> | — | low |
| 29.pdf / 29 | 172 | TeX source line 10 (occurrence 253) | <code>S</code> | <code>\delta</code> | low |
| 29.pdf / 29 | 172 | TeX source line 10 (occurrence 254) | <code>C_i</code> | — | low |
| 29.pdf / 29 | 172 | TeX source line 14 (occurrence 255) | <code>\varphi</code> | — | low |
| 29.pdf / 29 | 172 | TeX source line 16 (occurrence 256) | <code>H^1_{C_4}(\widehat V/V,G)\simeq</code> | — | low |
| 29.pdf / 29 | 174 | TeX source line 5 (occurrence 257) | <code>Th de comparaison</code> | — | medium |
| 29.pdf / 29 | 175 | TeX source line 3 (occurrence 258) | <code>\pi_2</code> | <code>\Pi_2</code> | low |
| 29.pdf / 29 | 176 | TeX source line 10 (occurrence 259) | <code>I</code> | <code>2</code> | low |
| 29.pdf / 29 | 176 | TeX source line 10 (occurrence 260) | <code>2</code> | <code>1</code> | low |
| 29.pdf / 29 | 176 | TeX source line 16 (occurrence 261) | <code>j</code> | <code>i</code> | medium |
| 29.pdf / 29 | 176 | TeX source line 20 (occurrence 262) | <code>H^*</code> | <code>\Pi^*</code> | low |
| 29.pdf / 29 | 176 | TeX source line 20 (occurrence 263) | <code>j</code> | <code>i</code> | medium |
| 29.pdf / 29 | 176 | TeX source line 33 (occurrence 264) | <code>E^p</code> | <code>E_2</code> | low |
| 29.pdf / 29 | 176 | TeX source line 42 (occurrence 265) | <code>i</code> | — | low |
| 29.pdf / 29 | 177 | TeX source line 4 (occurrence 266) | <code>\simeq</code> | <code>\cong</code> | low |
| 29.pdf / 29 | 177 | TeX source line 9 (occurrence 267) | <code>\widetilde Y''</code> | <code>Y''</code> | low |
| 29.pdf / 29 | 177 | TeX source line 22 (occurrence 268) | <code>1</code> | — | low |
| 29.pdf / 29 | 177 | TeX source line 22 (occurrence 269) | <code>\mathfrak z</code> | <code>\zeta</code> | low |
| 29.pdf / 29 | 177 | TeX source line 25 (occurrence 270) | <code>\mathfrak z</code> | <code>\zeta</code> | low |
| 29.pdf / 29 | 177 | TeX source line 31 (occurrence 271) | <code>\mathfrak z</code> | <code>\zeta</code> | low |
| 29.pdf / 29 | 177 | TeX source line 35 (occurrence 272) | <code>H^1</code> | — | low |
| 29.pdf / 29 | 177 | TeX source line 35 (occurrence 273) | <code>\mathfrak z</code> | <code>\zeta</code> | low |
| 29.pdf / 29 | 177 | TeX source line 38 (occurrence 274) | <code>Y</code> | <code>X</code> | low |
| 29.pdf / 29 | 177 | TeX source line 42 (occurrence 275) | <code>\mathfrak z</code> | <code>\zeta</code> | low |
| 29.pdf / 29 | 179 | TeX source line 10 (occurrence 276) | <code>composantes connexes</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 10 (occurrence 277) | <code>q.c.</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 16 (occurrence 278) | <code>considérons</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 21 (occurrence 279) | <code>n'a qu'un nb fini de valeurs</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 22 (occurrence 280) | <code>ou $S''$ a</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 27 (occurrence 281) | <code>groupe</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 28 (occurrence 282) | <code>le nb</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 28 (occurrence 283) | <code>n''-n'</code> | — | low |
| 29.pdf / 29 | 179 | TeX source line 28 (occurrence 284) | <code>n''-n'</code> | — | low |
| 29.pdf / 29 | 180 | TeX source line 8 (occurrence 285) | <code>Ce sont les $\Pi_0$</code> | — | low |
| 29.pdf / 29 | 180 | TeX source line 9 (occurrence 286) | <code>(triviaux)</code> | — | low |
| 29.pdf / 29 | 180 | TeX source line 19 (occurrence 287) | <code>$G$ et</code> | — | low |
| 29.pdf / 29 | 180 | TeX source line 20 (occurrence 288) | <code>-----</code> | — | medium |
| 29.pdf / 29 | 180 | TeX source line 22 (occurrence 289) | <code>voir la</code> | — | low |
| 29.pdf / 29 | 180 | TeX source line 23 (occurrence 290) | <code>axiome</code> | <code>hypose</code> | low |
| 29.pdf / 29 | 181 | TeX source line 4 (occurrence 291) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 5 (occurrence 292) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 6 (occurrence 293) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 8 (occurrence 294) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 9 (occurrence 295) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 10 (occurrence 296) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 13 (occurrence 297) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 14 (occurrence 298) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 15 (occurrence 299) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 16 (occurrence 300) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 16 (occurrence 301) | <code>i_0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 17 (occurrence 302) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 18 (occurrence 303) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 20 (occurrence 304) | <code>i</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 20 (occurrence 305) | <code>i</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 21 (occurrence 306) | <code>\dagger</code> | <code>\pi</code> | low |
| 29.pdf / 29 | 181 | TeX source line 25 (occurrence 307) | <code>compact</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 25 (occurrence 308) | <code>treillis</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 30 (occurrence 309) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 31 (occurrence 310) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 32 (occurrence 311) | <code>----</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 34 (occurrence 312) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 38 (occurrence 313) | <code>i</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 38 (occurrence 314) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 39 (occurrence 315) | <code>2</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 44 (occurrence 316) | <code>h</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 49 (occurrence 317) | <code>k^0_0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 49 (occurrence 318) | <code>0</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 57 (occurrence 319) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 57 (occurrence 320) | <code>1</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 59 (occurrence 321) | <code>f(p'_1(\xi))=</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 63 (occurrence 322) | <code>un</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 68 (occurrence 323) | <code>\xi</code> | — | low |
| 29.pdf / 29 | 181 | TeX source line 68 (occurrence 324) | <code>i_0</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 182 | TeX source line 5 (occurrence 325) | <code>complexe</code> | — | medium |
| 29.pdf / 29 | 182 | TeX source line 25 (occurrence 326) | <code>deux ponctuations</code> | — | low |
| 29.pdf / 29 | 182 | TeX source line 28 (occurrence 327) | <code>et est même d'une</code> | — | low |
| 29.pdf / 29 | 182 | TeX source line 29 (occurrence 328) | <code>ponctuation donnée, que deux ponctuations, ne diffèrent que par un</code><br><code>élémt de $G$, d'ailleurs unique</code> | — | low |
| 29.pdf / 29 | 182 | TeX source line 32 (occurrence 329) | <code>les</code> | — | low |
| 29.pdf / 29 | 183 | TeX source line 34 (occurrence 330) | <code>permute</code> | <code>commute</code> | medium |
| 29.pdf / 29 | 183 | TeX source line 46 (occurrence 331) | <code>de</code> | — | low |
| 29.pdf / 29 | 183 | TeX source line 51 (occurrence 332) | <code>\pi_0F</code> | — | low |
| 29.pdf / 29 | 183 | TeX source line 64 (occurrence 333) | <code>isomorphisme</code> | <code>homéomorphisme</code> | low |
| 29.pdf / 29 | 184 | TeX source line 11 (occurrence 334) | <code>fini</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 14 (occurrence 335) | <code>qu. tot.</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 14 (occurrence 336) | <code>disco</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 19 (occurrence 337) | <code>k[[s,t]]</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 20 (occurrence 338) | <code>k\eta_1 ds</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 22 (occurrence 339) | <code>opère sur $\overline E$</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 23 (occurrence 340) | <code>$\gamma$</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 23 (occurrence 341) | <code>que</code> | <code>soit</code> | low |
| 29.pdf / 29 | 184 | TeX source line 52 (occurrence 342) | <code>t_1</code> | <code>u_1</code> | low |
| 29.pdf / 29 | 184 | TeX source line 52 (occurrence 343) | <code>t_1</code> | <code>u_1</code> | low |
| 29.pdf / 29 | 184 | TeX source line 52 (occurrence 344) | <code>t_1</code> | <code>u_1</code> | low |
| 29.pdf / 29 | 184 | TeX source line 106 (occurrence 345) | <code>b</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 117 (occurrence 346) | <code>B</code> | — | low |
| 29.pdf / 29 | 184 | TeX source line 132 (occurrence 347) | <code>c</code> | <code>E</code> | low |
| 29.pdf / 29 | 185 | TeX source line 4 (occurrence 348) | <code>de</code> | <code>des</code> | low |
| 29.pdf / 29 | 185 | TeX source line 18 (occurrence 349) | <code>strictement pro</code> | — | medium |
| 29.pdf / 29 | 185 | TeX source line 26 (occurrence 350) | <code>\xi</code> | — | low |
| 29.pdf / 29 | 185 | TeX source line 27 (occurrence 351) | <code>\alpha</code> | <code>*</code> | low |
| 29.pdf / 29 | 185 | TeX source line 30 (occurrence 352) | <code>cosimplicial</code> | — | low |
| 29.pdf / 29 | 185 | TeX source line 31 (occurrence 353) | <code>objet simplicial de</code> | — | low |
| 29.pdf / 29 | 185 | TeX source line 38 (occurrence 354) | <code>G</code> | — | low |
| 29.pdf / 29 | 185 | TeX source line 42 (occurrence 355) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 185 | TeX source line 43 (occurrence 356) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 185 | TeX source line 43 (occurrence 357) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 9 (occurrence 358) | <code>on va de</code> | — | low |
| 29.pdf / 29 | 186 | TeX source line 9 (occurrence 359) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 10 (occurrence 360) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 12 (occurrence 361) | <code>\zeta^0</code> | <code>\xi^0</code> | low |
| 29.pdf / 29 | 186 | TeX source line 13 (occurrence 362) | <code>\zeta^1</code> | <code>\xi^1</code> | low |
| 29.pdf / 29 | 186 | TeX source line 14 (occurrence 363) | <code>\zeta^2</code> | <code>\xi^2</code> | low |
| 29.pdf / 29 | 186 | TeX source line 18 (occurrence 364) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 19 (occurrence 365) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 22 (occurrence 366) | <code>\zeta</code> | <code>\xi</code> | low |
| 29.pdf / 29 | 186 | TeX source line 33 (occurrence 367) | <code>----</code> | — | low |
| 29.pdf / 29 | 186 | TeX source line 36 (occurrence 368) | <code>sur des</code> | — | low |
| 29.pdf / 29 | 186 | TeX source line 38 (occurrence 369) | <code>(connexes, les $F^i$</code> | — | low |
| 29.pdf / 29 | 186 | TeX source line 40 (occurrence 370) | <code>-----</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 9 (occurrence 371) | <code>Y</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 20 (occurrence 372) | <code>\&amp;</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 25 (occurrence 373) | <code>U</code> | <code>U'</code> | low |
| 29.pdf / 29 | 187 | TeX source line 25 (occurrence 374) | <code>entier alg</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 30 (occurrence 375) | <code>\text{surj}</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 35 (occurrence 376) | <code>par prolongement</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 41 (occurrence 377) | <code>il</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 42 (occurrence 378) | <code>X'</code> | <code>\widetilde X'</code> | low |
| 29.pdf / 29 | 187 | TeX source line 43 (occurrence 379) | <code>X'</code> | <code>\widetilde X'</code> | low |
| 29.pdf / 29 | 187 | TeX source line 44 (occurrence 380) | <code>gagne</code> | — | low |
| 29.pdf / 29 | 187 | TeX source line 44 (occurrence 381) | <code>.....</code> | — | low |

## Particularly uncertain loci and literal readings

| Cote/file | Scan | Approximate place | Current reading / editorial caution | Confidence |
|---|---|---|---|---|
| 29.pdf | 141, 143 | Torsor-functor definition and repeated product formula | The looped letter is provisionally Gothic Z; it remains unresolved after direct comparison with the quite different Gothic F on 152. | low |
| 29.pdf | 141 | Last line, continued on 142 | The final phrase is compressed and faint; use the current marked reading, not the earlier `rend l'assertion` proposal preserved in the historical log. | low |
| 29.pdf | 147 | Handwritten cancellation, inserted line and barred-point discussion | Fine writing lies over reversed typescript; bars, primes, point labels and several connective words are the weakest parts. | low |
| 29.pdf | 148 | Typed item 4° | The visible `V de W` and the last un-tilde `W^2` are retained literally; a mathematically expected X or tilde is not substituted. | high |
| 29.pdf | 149 | Long crossed existence condition | The second reading favours `les fibres ... aient une composante connexe`; one word remains physically unreadable and is marked `\illegible{1}`. | low |
| 29.pdf | 150 | Circular's handwritten signature | `Mandeuil` is only a tentative surname reading; no external identification was used. | low |
| 29.pdf | 153 | Heading, (iii bis), final proof paragraph | The replacement noun in the heading, the tiny added subscript after n−1 and `dimension|diminution` are uncertain; the two later words remain `d'inertie|d'isotropie`. | low |
| 29.pdf | 154 | Bottom insertion and base letter before `vérif` | The crossed Y/X and the inserted relative clause remain uncertain; the two visible question marks are author marks, not editorial doubt signs. | low |
| 29.pdf | 158 | Upper/left insertions and last Gal 6 formula | Y in the left insertion is struck; adjective number remains uncertain; the last expression is E(X/H) with F(X/H) as alternative. | low |
| 29.pdf | 159 | Axiom 8 above `section` | The small crossed word is `\deleted{\unsure{les}}`, not an extra live or inserted `toute`. | medium |
| 29.pdf | 160 | Rotated margin | The abbreviated condition and connector words are poorly legible; the transposition of `universels` is clearer than the marginal prose. | low |
| 29.pdf | 162 | Normalization example | The letter in the vanishing fundamental-group expression remains Y′/X′ uncertain; the terminology `conoyau` is retained as seen. | low |
| 29.pdf | 166–168 | Rewritten end of the reduction argument | The live Phi is secure; several cancelled connectors and the abandoned limit paragraph are not. The current `on gagne` readings supersede earlier `ce qui prouve` / `c'est fini` attempts. | low |
| 29.pdf | 169 | Middle paragraph | `E_S` is the visible capital, although the fibre in the preceding paragraph is called F. | high |
| 29.pdf | 176 | Degrees, indices and limit strokes | I/2, 2/1, j/i and a grid label remain uncertain; plain underlined limits were distinguished from the explicit direct-limit arrow. | low |
| 29.pdf | 177 | Repeated small looped symbol | `\mathfrak z|\zeta` is used consistently; it is not expanded to a word such as centre. | medium |
| 29.pdf | 179 | Final generator count | The written bound is read `n''-n'`; no expected +1 has been inserted. | low |
| 29.pdf | 180 | Oblique marginal problem | `voir la` and `axiome|hypose` are uncertain. The inserted circled `loc`, underlined `noeth`, and the author's `J'ignore` are clearer. | low |
| 29.pdf | 181 | Repeated equivalences and last condition | No distinct prime is visible on either right-hand f. The final quantified sign resembles i₀; xi remains an alternative. | low |
| 29.pdf | 182 | Large cancelled bracket | Overlapping cancellation loops conceal several words; the whole attempted reading is explicitly tentative, including the final uniqueness clause. | low |
| 29.pdf | 183 | Last line at lower scan edge | `isomorphisme|homéomorphisme` is the current reading; `homomorphisme` was also considered in the first pass. | low |
| 29.pdf | 184 | Isolated top-centre formulas and upper-right prose | The scratched symbols, under-diagram abbreviations and action sentence are among the least trustworthy readings in the packet; all visible graph branches, loops and labels have nevertheless been attempted in TikZ. | low |
| 29.pdf | 185–186 | Copointing and vertical diagram labels | Zeta/xi ambiguity is consistent across the two pages; the terminal E in both functors on 186 is visible and retained. | low for letter; high for E |
| 29.pdf | 187 | Last construction and lower edge | The prime after the first U and the tildes on the two later X′ mentions are not secure; the source of the displayed map has a clear tilde, and `surjectif` is crossed out. | low |

## Abbreviations encountered

These expansions are editorial aids only. They have not been inserted into the transcription, and an ambiguous abbreviation remains ambiguous there.

| Written abbreviation(s) | Tentative expansion / use |
|---|---|
| `abs` with raised `t` | absolument |
| `alg`, `alg.` | algébrique; in `alg clos`, algébriquement clos; in `faisceau d'alg`, algèbres |
| `bas.` | base, according to its position |
| `Bourb.` | Bourbaki |
| `can.` | canonique |
| `cat`, `cat.`, `Catégor.` | catégorie / catégories |
| `cf.`, `Cf` | confer; compare / voir |
| `Changt` | changement |
| `comm.` | commutatif / commutativité, according to its position |
| `comp`, `comp.` | composante / composantes |
| `Cond` | condition / conditions |
| `conn.`, `connex.` | connexe / connexes |
| `corresp.` | correspondance / correspondants, according to its position |
| `cqfd.` | ce qu'il fallait démontrer |
| `d.` in the paired group labels | droite |
| `diagram.` | diagramme |
| `disco` | discontinu; the actual annotation is uncertain |
| `ds` | dans |
| `élémt`, `élémts` | élément / éléments |
| `ens`, `ens.`, `sous-ens.` | ensemble(s), sous-ensemble(s) |
| `esp.` | espace |
| `Ex.`, `ex.`, `p.ex.` | exemple; par exemple |
| `ext.` | extension |
| `f.` in `type f.` | fini |
| `fid`, `fidelt` | fidèlement |
| `g.` in the paired group labels | gauche |
| `Gal` | label for the numbered Galois-category axioms, rather than an expanded word in the text |
| `généralt` | généralement |
| `géom.` | géométrique(s) |
| `gr`, `gr.` | groupe(s); on Hom, morphismes de groupes |
| `hom.`, `homom.` | homomorphisme(s); `hom.` in `pr. hom.` instead means homogène |
| `homog.`, `homo` in principal-bundle phrases | homogène |
| `hyp.`, tentative `hypose` | hypothèse(s) |
| `i.e.` | id est; c'est-à-dire |
| `imm.` | immersion |
| `inj.` | injection / injectif |
| `int.` in the curve example | intègre |
| `irred.` | irréductible(s) |
| `iso`, `isom.` | isomorphisme / isomorphe |
| `loc`, `loc.` | localement, local or local(e), depending on the sentence |
| `loc.cit.` | loco citato |
| `mb.`, `mbr` | membre |
| `mon.`, `mono.` | monomorphisme(s) |
| `N.B.`, `NB` | nota bene |
| `nb` | nombre |
| `néc` | nécessaire(s) |
| `noeth`, `noeth.` | noethérien(ne)(s) |
| `p.` | page |
| `Pb` | problème |
| `pr.` | principal, in the torsor phrase |
| `pro.` in the deleted descent phrase | probably propriété; the reading itself is uncertain |
| `prop`, `prop.` | proposition |
| `pt`, `pts` | point / points |
| `q.c.`, `quasi. cpt` | quasi-compact |
| `qu.`, `quasi-` | quasi; in the small cancelled annotation on 184 the expansion is not secure |
| `rel`, `rel.` | relatif / relativement |
| `Rem.` | remarque |
| `repr.`, `T-repr` | représentable; T-représentable |
| `resp`, `resp.` | respectivement |
| `rev.`, `revêt.`, `Revêtts` | revêtement(s) |
| `ss-` | sous- |
| `surj` | surjectif; the marginal label on 187 remains uncertain |
| `syst.` | système |
| `t.f.` | type fini |
| `Th.`, `th.`, `Th` | théorème |
| `top`, `top.` | topologique / topologie |
| `tot.` | totalement |
| `triv.`, `trivialt` | trivialement |
| `tt`, `tte` | tout / toute; agreement is not regularized in the text |
| `univ.` | universellement |
| `vérif` | vérifier / vérification |
| `vraisemblt` | vraisemblablement |

## Legibility and limitations

The typed sheets are substantially more legible than the rapid handwritten sheets, but reused paper, reverse-side show-through, creases and low contrast sometimes obscure even their annotations. The least secure material is the small brown writing on 147, the overlapping cancellations on 149 and 153–154, the rotated margins on 158/160/180, the revised argument on 167–168, the cancelled bracket on 182, the scratch sheet 184, and several words at the lower edges of 183, 185 and 187. Low-confidence marks are intentional and should be resolved against the images, not by adopting a mathematically smoother sentence.

Every supplied full image and both halves were personally read by the primary transcriber in the first pass, and every page received a second visual audit before freeze. No OCR was used and no scan reading or transcription was delegated. Drawings and diagram layouts are hand-constructed TikZ approximations of the visible shapes and relative positions; they are not facsimiles, and the densely overdrawn sheet 184 is the least exact geometrically. The second pass and notation comparison improve consistency, but do not turn unresolved handwriting into a certain reading.
