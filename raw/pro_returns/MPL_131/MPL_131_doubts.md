# MPL 131 — notation and doubts

## Shared notation table

This table was maintained from the first page and completed during the second visual audit, before opening the context archive. The file identifier is **131.pdf** throughout; scan numbers are its PDF page numbers, not the handwritten folios or the old typescript page numbers. The transcription follows the scan order, including the reused sheets.

| Manuscript sign or recurring form | LaTeX reading and checks against the ink |
|---|---|
| Plain capitals `F,S,A,B,X,Z,T` | Plain mathematical capitals; no promotion to script or Gothic letters from mathematical expectation. |
| Local structure sheaf / local ring | `\mathcal O` in the handwritten local-ring expressions, including scans 023, 031, 033 and 037. |
| Handwritten prime ideal | `\mathfrak p` where the elongated p-shaped ideal letter is visible; the crowded localization indices on scan 012 remain p/eta alternatives. |
| Ideals on reused sheets n° 392 | Underlined `a,p` are `\underline a,\underline p` on scans 008 and 021. The underlined matrix `U` on scan 010 is `\underline{U}`. |
| Ideals on reused sheets n° 371 | The letters `a,b,a_i,b_j` on scans 030 and 032 are plain, as printed; they were checked separately from the underlined notation on n° 392 sheets. |
| Functor elements, eta/y-shaped letter | The looped letter with a descending tail is `\eta` where clear; early or overwritten occurrences retain eta/y alternatives. The remaining occurrences on scans 012 and 016 were rechecked individually, including cancelled matter. |
| Xi-shaped element | `\xi` follows the vertically curling sign, especially the representing element on scans 023–033 and the final pair on 041. Its looped variants were compared within the equalities on 027. |
| Distinct or unresolved eta/xi occurrences | Scan 023 retains an eta/y-shaped element followed by a visibly different `\xi_t`; scan 041 retains an uncertain eta/xi superscripted element and a clear final `\xi`. These are not silently made identical. |
| Phi-shaped morphism | `\varphi`, including the local isomorphism on 037 and the typed monoid maps on 040; barred phi is `\bar\varphi`. |
| Relative lattice invariant | `\chi(M,M')` on n° 392 sheets; not a Roman `X`. All cyclic identities on scan 021 were checked. |
| Multilinear signs and indices | `\varepsilon(\alpha,\beta)` and `\alpha,\beta,\gamma` follow the typed sheet on 013. The apparently missing operand after the tensor sign in (18) remains missing. |
| Number systems | Plain `N,Z,Q` where the source prints plain capitals; no automatic blackboard-bold substitution. |
| Opposite algebra / opposite category | A raised small circle is `^\circ`, including `E_i^\circ` on 032 and the handwritten scheme category. |
| Prime, double prime, exclamation mark | `'` and `''` follow visible prime strokes. An exclamation mark would require both its stroke and its separate dot; none was inferred from a prime. |
| Arrow versus plain stroke | Visible arrowheads determine `\to`, `\longrightarrow`, `\hookrightarrow` or TikZ arrows. A plain joining stroke is `\mathbin{-}` or `no head`; unresolved strokes retain an explicit alternative. The hook on scan 020 was enlarged and retained. |
| Parallel arrows | Two distinct arrows are retained in descent/equalizer diagrams; no replacement by an implication sign. |
| Direct / inverse limit | `\varinjlim` and `\varprojlim` follow the arrow under the written limit sign, including the marginal drawings. |
| First two L-conditions | `\underset{\leftarrow}{L}_1` and `\underset{\leftarrow}{L}_2` where a left arrow is written beneath L, verified on scans 023, 025, 029, 031, 033 and 037. |
| Revised third/fourth L-conditions | The two raised loops remain `00` versus `\circ\circ` alternatives. Old indices and cancellation states are retained locally. The fourth arrow points right on 025 and 029 but appears left on 031; that visible difference is preserved. |
| Other L labels | Scan 027 has a right arrow beneath `L_{\mathrm{loc}}`; the last `L_2` on 041 has no visible arrow. Plain lattice `L_1,L_2` on the typescript sheets are unrelated letter uses and remain plain. |
| Superscripts on local models | `X^{(*)}`, `X^{(a)}`, `X^{(x)}` and their uncertain alternatives follow the individual visible marks on 031–041. No uniform index was imposed on the abandoned and revised drafts. |
| Hats and bars | `\widehat B`, `\hat S`, `\bar\eta`, `\bar x` follow the actual decoration; a prime is not substituted for a hat. |
| Exterior power | A raised n over the wedge is `\overset{n}{\bigwedge}` on the lattice sheet 021. |
| Tensor powers / finite-support families | `A^S` and `A^{(S)}` remain distinct on 028 and 038–040; products and tensor signs retain their written subscripts. |
| Universal quantifier | `\forall` when the symbol is written; `tout`, `tt` or `tte` when a word or abbreviation is written. |
| Quotation marks | Written double quotation marks become two backticks and two apostrophes; the doubtful isolated guillemet on 037 remains marked rather than converted. |
| Underlining and emphasis | `\uline`, `\uuline`; three distinct strokes, when present, are represented with nested underlining. Encircled numbers use standard `\textcircled`. |
| Deletion, insertion, margin | `\deleted`, `\inserted`, `\margin`; uncertainty remains inside a cancellation. The inventory separately records nested components of densely revised passages. |
| Diagrams and drawings | All diagrams use `tikz-cd`; curves, borders, linkage strokes and separators are reproduced with TikZ rather than prose descriptions. |
| Sheet identifiers | `\mspage` records visible manuscript/pencil identifiers. Folios 7 (008) and 9 (010) are upside down relative to the typescript; folio 11 (012) is rotated. Original typed page numbers and n° 392 / n° 371 are transcribed separately. |
| Short forms and endings | Abbreviations are preserved in the TeX. The expansion list below is editorial; uncertain French endings are not regularized to fit grammar. |

The notation comparison does not convert a difficult glyph into a certain reading merely because the mathematics suggests one. A retained difference is either visible in the source or explicitly marked as unresolved, with examples above and in the audit observations.

## Doubt register

Approximate line numbers refer to the physical line of the individual page TeX fragment, so that each doubt can be located without silently assigning a manuscript line division. All entries are visual readings made before the context was opened. A vertical bar at brace depth zero separates a proposed reading from an alternative. Nested doubt occurrences also have individual entries.

| Cote | Scan | Approx. line | Reading | Alternative | Confidence |
|---|---:|---:|---|---|---|
| 131 | 2 | 4 | conditions | — | low |
| 131 | 2 | 4 | d'exactitude | — | low |
| 131 | 2 | 13 | fppc | fpqc | low |
| 131 | 2 | 16 | changts | — | low |
| 131 | 2 | 16 | fid. | — | low |
| 131 | 2 | 17 | plt | — | low |
| 131 | 2 | 17 | par. | — | low |
| 131 | 2 | 17 | qcts | — | low |
| 131 | 2 | 25 | A | — | low |
| 131 | 2 | 25 | g. | — | low |
| 131 | 2 | 25 | algèbres | — | low |
| 131 | 2 | 30 | finis | — | low |
| 131 | 2 | 34 | - | \longrightarrow | low |
| 131 | 2 | 39 | pour | — | low |
| 131 | 2 | 39 | assurer | aux | low |
| 131 | 2 | 39 | foncteurs | — | low |
| 131 | 2 | 39 | sur | — | low |
| 131 | 2 | 40 | pour | — | low |
| 131 | 2 | 40 | v. | — | low |
| 131 | 2 | 40 | (de t.f. sur k) | — | low |
| 131 | 2 | 41 | n'induit aucune | — | low |
| 131 | 2 | 41 | f. | — | low |
| 131 | 2 | 41 | ou : | — | low |
| 131 | 2 | 42 | F séparé | — | low |
| 131 | 2 | 42 | local | — | low |
| 131 | 2 | 42 | complet | — | low |
| 131 | 2 | 51 | a | — | low |
| 131 | 2 | 52 | tout | — | low |
| 131 | 2 | 52 | \eta | y | low |
| 131 | 2 | 52 | \eta | y | low |
| 131 | 2 | 52 | - | \longrightarrow | low |
| 131 | 2 | 53 | modulaire | — | low |
| 131 | 2 | 53 | \eta | y | low |
| 131 | 2 | 53 | modulaire | — | low |
| 131 | 2 | 56 | \eta | y | low |
| 131 | 2 | 58 | irréductiblement | — | low |
| 131 | 2 | 58 | F_{s'_0} | F_{s'} | low |
| 131 | 2 | 58 | si | — | low |
| 131 | 2 | 58 | sur | — | low |
| 131 | 2 | 61 | \longrightarrow | - | low |
| 131 | 2 | 61 | \eta | y | low |
| 131 | 2 | 61 | \eta | y | low |
| 131 | 2 | 61 | modulaire | — | low |
| 131 | 2 | 61 | \eta | y | low |
| 131 | 2 | 61 | modulaire | — | low |
| 131 | 3 | 2 | Caractérisation | — | medium |
| 131 | 4 | 4 | en suppos | — | medium |
| 131 | 4 | 8 | --- | — | medium |
| 131 | 4 | 8 | 4^\circ | 2^\circ | medium |
| 131 | 4 | 8 | correspondants | — | medium |
| 131 | 4 | 9 | compl. | — | medium |
| 131 | 5 | 2 | - | \longrightarrow | low |
| 131 | 5 | 2 | le | — | low |
| 131 | 5 | 2 | commencer | — | low |
| 131 | 5 | 2 | \eta | y | low |
| 131 | 5 | 4 | pas | — | low |
| 131 | 5 | 4 | que la | — | low |
| 131 | 5 | 4 | la plus | — | low |
| 131 | 5 | 4 | forme | — | low |
| 131 | 5 | 4 | affaiblie | — | low |
| 131 | 5 | 4 | nouvelle | — | low |
| 131 | 5 | 6 | \hat S | — | low |
| 131 | 5 | 6 | canon. | — | low |
| 131 | 5 | 10 | Comme le | — | low |
| 131 | 7 | 4 | pré | — | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | - | \longrightarrow | low |
| 131 | 7 | 4 | tel que et | — | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | U | — | low |
| 131 | 7 | 4 | - | \longrightarrow | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | \eta | y | low |
| 131 | 7 | 4 | - | \longrightarrow | low |
| 131 | 7 | 11 | \eta | y | low |
| 131 | 7 | 11 | \eta | y | low |
| 131 | 7 | 18 | X | Z | low |
| 131 | 7 | 18 | qu. fini | — | low |
| 131 | 7 | 18 | \eta | y | low |
| 131 | 7 | 18 | X | Z | low |
| 131 | 7 | 18 | \eta | y | low |
| 131 | 7 | 22 | changement | — | low |
| 131 | 7 | 22 | pour | — | low |
| 131 | 7 | 22 | \eta | y | low |
| 131 | 7 | 22 | capturant | — | low |
| 131 | 7 | 22 | l'expression | — | low |
| 131 | 7 | 22 | des | — | low |
| 131 | 7 | 23 | et | — | low |
| 131 | 7 | 23 | sur | — | low |
| 131 | 7 | 23 | un | — | low |
| 131 | 7 | 24 | pour | — | low |
| 131 | 7 | 24 | foncteur | — | low |
| 131 | 7 | 24 | pour | — | low |
| 131 | 7 | 24 | le | — | low |
| 131 | 7 | 24 | morphisme | — | low |
| 131 | 7 | 25 | X\times_{S'}X | X_{S'} | low |
| 131 | 7 | 25 | S' | — | low |
| 131 | 7 | 26 | pour | — | low |
| 131 | 7 | 26 | T | — | low |
| 131 | 7 | 26 | plongé | — | low |
| 131 | 7 | 26 | cette | — | low |
| 131 | 7 | 10 | Illegible: approximately 1 word(s) | No recoverable reading after visual enlargement | low |
| 131 | 9 | 6 | X | Z | medium |
| 131 | 9 | 6 | \eta | y | medium |
| 131 | 9 | 8 | X | Z | medium |
| 131 | 9 | 8 | \eta | y | medium |
| 131 | 9 | 10 | aux des | — | medium |
| 131 | 9 | 10 | X | Z | medium |
| 131 | 9 | 10 | \eta | y | medium |
| 131 | 9 | 10 | X | Z | medium |
| 131 | 9 | 10 | - | \longrightarrow | medium |
| 131 | 9 | 10 | \eta | y | medium |
| 131 | 9 | 10 | modulaire | — | medium |
| 131 | 9 | 10 | \eta | y | medium |
| 131 | 9 | 10 | - | \longrightarrow | medium |
| 131 | 9 | 10 | peut | pt | medium |
| 131 | 9 | 10 | \simeq | \text{même} | medium |
| 131 | 9 | 16 | lisse | — | medium |
| 131 | 9 | 17 | mor. | — | medium |
| 131 | 9 | 17 | mor. | — | medium |
| 131 | 9 | 18 | \eta | y | medium |
| 131 | 9 | 18 | - | \longrightarrow | medium |
| 131 | 9 | 18 | \eta | y | medium |
| 131 | 9 | 21 | si | — | medium |
| 131 | 9 | 23 | - | \longrightarrow | medium |
| 131 | 9 | 25 | tf. | — | medium |
| 131 | 9 | 25 | \eta | y | medium |
| 131 | 9 | 25 | - | \longrightarrow | medium |
| 131 | 9 | 25 | \eta | y | medium |
| 131 | 9 | 27 | un | — | medium |
| 131 | 9 | 14 | Illegible: approximately 1 word(s) | No recoverable reading after visual enlargement | low |
| 131 | 10 | 18 | A-\{0\} | A:-\{0\} | medium |
| 131 | 12 | 3 | 10 | 9 | low |
| 131 | 12 | 3 | irred. | — | low |
| 131 | 12 | 4 | peu plus | — | low |
| 131 | 12 | 4 | générique | — | low |
| 131 | 12 | 8 | cpte | — | low |
| 131 | 12 | 15 | 7 | 5 | low |
| 131 | 12 | 15 | et | — | low |
| 131 | 12 | 16 | $=$ | m\textsuperscript{e} | low |
| 131 | 12 | 20 | 5 | 7 | low |
| 131 | 12 | 31 | \mathfrak p | — | low |
| 131 | 12 | 31 | premier | primaire | low |
| 131 | 12 | 31 | $\xi$ | — | low |
| 131 | 12 | 31 | \xi_0 | \eta_0 | low |
| 131 | 12 | 31 | si $\unsure{\xi_0&#124;\eta_0}\in\operatorname{Im}F(A_{\unsure{\mathfrak p&#124;\eta}})$ | — | low |
| 131 | 12 | 31 | \xi_0 | \eta_0 | low |
| 131 | 12 | 31 | \mathfrak p | \eta | low |
| 131 | 12 | 31 | se prolonge en un $\unsure{\eta&#124;y}\in F(A/\unsure{I^n})$, | — | low |
| 131 | 12 | 31 | \eta | y | low |
| 131 | 12 | 31 | I^n | — | low |
| 131 | 12 | 31 | alors $\xi\in\varprojlim(A/\unsure{I^n})$ | — | low |
| 131 | 12 | 31 | I^n | — | low |
| 131 | 12 | 31 | provenant d'un | — | low |
| 131 | 12 | 31 | pour | — | low |
| 131 | 12 | 31 | \mathfrak p | \eta | low |
| 131 | 12 | 31 | \mathfrak p | \eta | low |
| 131 | 12 | 34 | noeth. irred. | — | low |
| 131 | 12 | 34 | schéma | — | low |
| 131 | 12 | 34 | annulé par le nilradical | — | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 34 | S'_0 | — | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 34 | petit | grand | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 34 | \eta | y | low |
| 131 | 12 | 36 | X | — | low |
| 131 | 12 | 39 | faisant intervenir la | formulant la | low |
| 131 | 12 | 39 | représentabilité | — | low |
| 131 | 12 | 39 | non | — | low |
| 131 | 12 | 39 | formulation | — | low |
| 131 | 12 | 39 | en disant que une condition | — | low |
| 131 | 12 | 39 | Modulaire ou | — | low |
| 131 | 12 | 39 | pro-modulaire | — | low |
| 131 | 12 | 39 | F | — | low |
| 131 | 12 | 39 | commute à l'extension | — | low |
| 131 | 12 | 39 | fid. plt | — | low |
| 131 | 12 | 41 | fid plt sur | — | low |
| 131 | 12 | 41 | alors $F(A)\xrightarrow{\sim}F(A')$ | — | low |
| 131 | 12 | 41 | longueur | — | low |
| 131 | 12 | 44 | 7 | — | low |
| 131 | 12 | 45 | 5 | — | low |
| 131 | 12 | 31 | Illegible: approximately 1 word(s) | No recoverable reading after visual enlargement | low |
| 131 | 14 | 4 | f | f\textsuperscript{t} | medium |
| 131 | 14 | 4 | s | S | medium |
| 131 | 14 | 10 | cptes | — | medium |
| 131 | 14 | 11 | ess. de type fini et à ext. résiduelle finie | — | medium |
| 131 | 14 | 15 | les pts de | — | medium |
| 131 | 14 | 15 | re | — | medium |
| 131 | 14 | 15 | B | — | medium |
| 131 | 14 | 19 | tout | — | medium |
| 131 | 14 | 19 | \leftarrow | — | medium |
| 131 | 14 | 19 | \eta | y | medium |
| 131 | 14 | 19 | \eta | y | medium |
| 131 | 14 | 19 | \eta | y | medium |
| 131 | 14 | 19 | des variantes | du contraire | low |
| 131 | 14 | 20 | et | — | medium |
| 131 | 14 | 20 | \eta | y | medium |
| 131 | 14 | 22 | tout | — | medium |
| 131 | 14 | 22 | fini | — | medium |
| 131 | 14 | 22 | \eta | y | medium |
| 131 | 14 | 22 | \eta | y | medium |
| 131 | 14 | 24 | fera résulter | peut vérifier | medium |
| 131 | 14 | 24 | et avec | — | medium |
| 131 | 14 | 24 | finitude | — | medium |
| 131 | 14 | 26 | \simeq | = | medium |
| 131 | 14 | 26 | renforce aussi | remplace aussi | low |
| 131 | 15 | 6 | 1,2,3,4° | — | medium |
| 131 | 16 | 2 | de | — | medium |
| 131 | 16 | 2 | \eta | y | medium |
| 131 | 16 | 8 | (Et) | — | medium |
| 131 | 16 | 8 | sont | — | medium |
| 131 | 16 | 10 | le axiome | l'axiome | low |
| 131 | 16 | 10 | direct | discret | low |
| 131 | 16 | 12 | soient | — | medium |
| 131 | 16 | 16 | un point gén. | — | medium |
| 131 | 16 | 16 | A | — | medium |
| 131 | 16 | 16 | d'un point de localité | — | medium |
| 131 | 16 | 16 | avec $A$ premier | — | medium |
| 131 | 16 | 16 | $\eta\in$ | $y\in$ | medium |
| 131 | 16 | 16 | \eta\in F | y\in F | medium |
| 131 | 16 | 16 | \eta | y | medium |
| 131 | 16 | 16 | \eta | y | medium |
| 131 | 16 | 16 | \eta | y | medium |
| 131 | 16 | 21 | repré. | — | medium |
| 131 | 16 | 21 | Ce qu'il est néc. | Ce qui est néc. | low |
| 131 | 16 | 21 | val. (loc.) | — | low |
| 131 | 17 | 4 | Limitation | — | medium |
| 131 | 17 | 8 | Mémo-finité | Mono-finité | low |
| 131 | 17 | 10 | Champs de | — | medium |
| 131 | 17 | 14 | d) | — | medium |
| 131 | 17 | 16 | modules principaux | — | medium |
| 131 | 17 | 16 | f\textsuperscript{rs} | — | medium |
| 131 | 17 | 18 | distingués | disjoints | medium |
| 131 | 17 | 21 | propres | — | medium |
| 131 | 17 | 21 | resp. | — | medium |
| 131 | 17 | 23 | univ. | — | medium |
| 131 | 17 | 30 | Seshadri M. | — | medium |
| 131 | 17 | 2 | Illegible: approximately 2 word(s) | No recoverable reading after visual enlargement | low |
| 131 | 20 | 2 | appliquant | — | medium |
| 131 | 20 | 4 | \eta | y | medium |
| 131 | 20 | 4 | déjà fait | — | medium |
| 131 | 20 | 4 | pour | par | medium |
| 131 | 23 | 4 | a) | — | medium |
| 131 | 23 | 6 | b) | — | medium |
| 131 | 23 | 8 | c) | — | medium |
| 131 | 23 | 11 | le | — | medium |
| 131 | 23 | 19 | de f | — | medium |
| 131 | 23 | 21 | \eta | y | medium |
| 131 | 25 | 2 | de b) | — | medium |
| 131 | 25 | 8 | se déduisant suivant | — | medium |
| 131 | 25 | 12 | Corollaire | — | medium |
| 131 | 25 | 15 | conditions suivantes | — | medium |
| 131 | 25 | 17 | \underset{\leftarrow}{L}^{00} | \underset{\leftarrow}{L}^{\circ\circ} | medium |
| 131 | 25 | 17 | 3 | — | medium |
| 131 | 25 | 17 | cas | — | medium |
| 131 | 25 | 20 | \underset{\rightarrow}{L}^{00} | \underset{\rightarrow}{L}^{\circ\circ} | medium |
| 131 | 25 | 20 | 4 | — | medium |
| 131 | 25 | 22 | \sim | — | medium |
| 131 | 25 | 28 | \underset{\leftarrow}{L}^{00} | \underset{\leftarrow}{L}^{\circ\circ} | medium |
| 131 | 25 | 28 | \underset{\rightarrow}{L}^{00} | \underset{\rightarrow}{L}^{\circ\circ} | medium |
| 131 | 25 | 28 | 4 | — | medium |
| 131 | 26 | 17 | v | w | medium |
| 131 | 27 | 2 | b | — | medium |
| 131 | 27 | 8 | réduction | réductions | medium |
| 131 | 27 | 11 | compatible | — | medium |
| 131 | 27 | 17 | F | — | medium |
| 131 | 27 | 17 | se réduit à | — | medium |
| 131 | 27 | 17 | il suffit de | — | medium |
| 131 | 28 | 11 | de | — | medium |
| 131 | 29 | 2 | que | — | medium |
| 131 | 29 | 9 | déduit | désire | medium |
| 131 | 29 | 13 | proreprésentabilité | — | medium |
| 131 | 29 | 13 | finis | — | medium |
| 131 | 29 | 13 | ceux | — | medium |
| 131 | 29 | 15 | 00 | \circ\circ | medium |
| 131 | 29 | 15 | 00 | \circ\circ | medium |
| 131 | 29 | 15 | 4 | — | medium |
| 131 | 30 | 31 | Alors | — | medium |
| 131 | 31 | 2 | (car loc et) | (cas loc et) | low |
| 131 | 31 | 4 | Prop. | — | low |
| 131 | 31 | 8 | On suppose | — | low |
| 131 | 31 | 14 | B | — | low |
| 131 | 31 | 14 | et | — | low |
| 131 | 31 | 15 | A\twoheadrightarrow A/\mathfrak m | B\twoheadrightarrow B/\mathfrak m | low |
| 131 | 31 | 17 | 00 | \circ\circ | low |
| 131 | 31 | 17 | 00 | \circ\circ | low |
| 131 | 31 | 21 | * | 0 | low |
| 131 | 31 | 21 | * | 0 | low |
| 131 | 31 | 21 | * | 0 | low |
| 131 | 31 | 28 | une | — | low |
| 131 | 31 | 29 | tout | — | low |
| 131 | 31 | 29 | les | — | low |
| 131 | 33 | 3 | énoncé-type | — | low |
| 131 | 33 | 15 | T_a | T_t | medium |
| 131 | 35 | 20 | L | — | low |
| 131 | 35 | 22 | R' | K' | low |
| 131 | 35 | 23 | L' | L | low |
| 131 | 35 | 26 | 6 | a | low |
| 131 | 35 | 33 | 6 | a | low |
| 131 | 35 | 35 | 1 | i | low |
| 131 | 35 | 38 | exprime que | — | low |
| 131 | 37 | 2 | loc. | — | medium |
| 131 | 37 | 2 | fini si | — | medium |
| 131 | 37 | 4 | modulaires | — | medium |
| 131 | 37 | 4 | a | 6 | medium |
| 131 | 37 | 8 | et alors | — | medium |
| 131 | 37 | 14 | double | — | medium |
| 131 | 37 | 14 | d'où le | — | medium |
| 131 | 37 | 14 | soit | — | medium |
| 131 | 37 | 14 | « | — | medium |
| 131 | 37 | 14 | local | — | medium |
| 131 | 38 | 9 | définissent | définissant | medium |
| 131 | 39 | 4 | les | — | low |
| 131 | 39 | 5 | On veut donc | — | low |
| 131 | 39 | 5 | $(X,\eta)$ correspondants | — | low |
| 131 | 39 | 5 | X^{a,a} | X^{(a)} | low |
| 131 | 39 | 5 | apparentés | — | low |
| 131 | 39 | 5 | il résulte | — | low |
| 131 | 39 | 5 | on a | — | low |
| 131 | 39 | 7 | S | Z | low |
| 131 | 39 | 12 | $\ldots$ | — | low |
| 131 | 39 | 13 | bien plus faibles | — | low |
| 131 | 39 | 15 | AQT | — | low |
| 131 | 41 | 2 | X^{(*)} | X^{(x)} | medium |
| 131 | 41 | 2 | \eta^{(x)} | \xi^{(x)} | medium |
| 131 | 41 | 2 | \eta_x | y_x | medium |
| 131 | 42 | 9 | M_{\mathrm I} | N_{\mathrm I} | medium |

## Abbreviations

Expansions here are editorial suggestions only; the transcription retains the abbreviated forms.

| Form | Suggested expansion | First scan recorded |
|---|---|---:|
| top | topologie | 2 |
| fppc | fidèlement plat, quasi-compact ? (reading and expansion uncertain) | 2 |
| g. | gauche | 2 |
| ext. | extension | 2 |
| alg clos | algébriquement clos | 2 |
| noeth | noethérien | 2 |
| pt | point | 2 |
| tt | tout | 2 |
| dim | dimension | 2 |
| fid. | fidèlement ? | 2 |
| changts | changements ? | 2 |
| tte | toute | 4 |
| préschém. | préschéma | 4 |
| loc. | localement | 4 |
| qu. | quasi | 4 |
| cf. | confer / voir | 4 |
| cor | corollaire | 4 |
| prop. | proposition | 4 |
| NB | nota bene | 4 |
| N.B. | nota bene | 4 |
| pts | points | 4 |
| hom | homomorphismes | 4 |
| compl. | complet | 4 |
| canon. | canonique | 5 |
| loc. cit. | loco citato | 6 |
| irréduct. | irréductible | 7 |
| gén. | générique | 7 |
| i.e. | id est | 7 |
| néc. | nécessairement | 7 |
| non ram. | non ramifié | 7 |
| ens | ensemble | 7 |
| infᵗ | infinitésimalement | 7 |
| cor. | corollaire | 8 |
| C. Q. F. D. | ce qu’il fallait démontrer | 8 |
| resp. | respectivement | 8 |
| Alg. | Algèbre | 8 |
| chap. | chapitre | 8 |
| éd. | édition | 8 |
| imm. | immersion | 9 |
| repr. | représentable | 9 |
| t.q. | tel que | 9 |
| mor. | morphisme ? | 9 |
| inf. | infinitésimalement | 9 |
| qu. cpte | quasi compacte (reading uncertain) | 12 |
| pt. gén. | point générique | 12 |
| ext. résiduelle | extension résiduelle | 12 |
| long | longueur | 12 |
| irred. | irréductible | 12 |
| préschéma | préschéma (written term, not silently changed to schéma) | 14 |
| desc. | descente | 14 |
| fid. plts | fidèlement plats | 14 |
| hypo. | hypothèse | 14 |
| cel | cela (uncertain abbreviated form) | 14 |
| loc. noeth | localement noethérien | 14 |
| NR. | non ramifié | 16 |
| pt gén. | point générique | 16 |
| f. et s | faut et suffit (abbreviated condition marker) | 16 |
| RG | représentabilité générique (suggested) | 17 |
| V.A. | variété abélienne (suggested) | 17 |
| comm. | commutatif | 17 |
| pbs | problèmes | 17 |
| divis. | divisorielles | 17 |
| p.ex. | par exemple | 17 |
| exerc. | exercice | 21 |
| prés. finie | présentation finie | 23 |
| t.f. | type fini | 23 |
| hyp. | hypothèse | 23 |
| isom. | isomorphisme | 23 |
| mono | monomorphisme | 23 |
| aff | affine | 23 |
| Ens. | Ensembles (bibliographic abbreviation) | 24 |
| ess. | essentiellement | 25 |
| plts | plats | 25 |
| t. | type | 27 |
| f. et s. | faut et suffit | 29 |
| représ. | représenté | 31 |
| t. f. | type fini | 33 |
| sous-ens | sous-ensemble | 35 |
| homs | homomorphismes | 35 |
| S-isom | S-isomorphisme | 37 |
| fasc. | fascicule | 40 |

## Legibility and limits

Every full-page image and both supplied overlapping halves were viewed directly during the sequential first pass. Every page received a second comparison against its image; additional crops, enlargements and rotations were used for faint margins, cancelled diagrams, folios and crowded formulas. No OCR was used, and no context content was read before the transcription was frozen.

The typed sheets are substantially clearer than the rapid handwriting, although their faint characters, primes, underlining and superscripts still required checking. The least trusted passages are **scan 002’s pale pencil annotations; scan 005’s interleaved marginal revision; scan 007’s bottom cancelled paragraphs and diagrams; scan 012’s rotated N.B., revised numbering and clipped bottom cancellations; scan 016’s final remark; scan 017’s first example heading; scan 031’s clipped aside and overwritten quotient; scan 035’s cancelled exterior diagram labels; and scan 039’s extensively crossed-out draft**. Their proposed readings are evidence to reconsider, not reliable quotations from which to deduce a theorem. In particular, the strange reading “Mémo-finité / Mono-finité” on scan 017 is retained only as a low-confidence attempt at the visible strokes.

“Medium” means a plausible visual reading with unresolved letters, endings or symbols; “low” means substantial obstruction, faintness, clipping or competing readings. The register assigns confidence to the marked reading, not to the truth of the mathematics or to every other passage on the same sheet. Nested doubts appear separately so that an uncertain subscript is not hidden inside a longer uncertain sentence. The tiny number of `\illegible` marks denotes physically unrecovered words after enlargement, never an omitted mathematical symbol. Unmarked text is not guaranteed error-free; this remains a difficult diplomatic transcription, and the audit record identifies the corrections and the limits of inspection.
