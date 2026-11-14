# MPL_145 — notation, readings, and doubts

## Package-wide notation table

This table records the conventions reconciled during the single-stream visual transcription and the second reading of all 38 scans, before opening the contextual material. It records graphic distinctions; it does not impose a uniform mathematical meaning on a symbol whose use changes within the manuscript.

| Visible convention | LaTeX transcription | Scope and remaining uncertainty |
|---|---|---|
| Double quotation strokes | two backticks and two apostrophes: ` ``...'' ` | No conversion to French guillemets. |
| Underlining and double underlining | `\uline{...}`, `\uuline{...}` | Distinguished from cancellation strokes. |
| Struck writing, including nested cancellations | `\deleted{...}` | Earlier ink remains inside the cancellation; doubtful readings remain marked there. |
| Interlinear or caret-directed additions | `\inserted{...}` | Attached at the visible target; vertical identifications and brace labels retain their two-dimensional placement. |
| Independent marginal writing | `\margin{...}` | Preserved as a separate block, including marginal diagrams and calculations. |
| Prime, exclamation, and star | `'`, `^!`, `^*` | The exclamation exponents on scans 24–26 are distinguished from primes; genuinely doubtful stars remain marked. |
| Curved verbal abbreviation with an upper stroke; compressed two-stroke variant | `$\unsure{\bar m\|=}$`, `$\unsure{=\|\bar m}$`, or `$=$` | The first reading follows the local shape; neither form is expanded in the transcription. The fully spelled words on scan 34 remain words. |
| Circular permutation letter | `\rho` | Distinguished visually from the multiplier `p`; no replacement on mathematical grounds. |
| Multiplier and other scalar letters | `p`, `q`, `r`; `\alpha`, `\beta`, `\gamma`, `\mu` | Exponents, subscripts and duplicated parentheses are retained even in surprising formulas. |
| Loop and inertia-subgroup letters | `l_0`, `l_1`, `l_\infty`; `L_0`, `L_1`, `L_\infty` | Lower-case looped l and upper-case L are kept distinct. |
| Transposition letters | `\sigma_0`, `\sigma_1`, `\sigma_\infty` | The locally written indices 1, 2, 3 on scan 27 are not normalized to 0, 1, infinity. Crowded or overwritten indices are doubtful. |
| Dots, tildes, primes | `\dot\sigma_i`, `\widetilde{\dot\sigma}_i`, `\tilde\sigma_i`, `\dot\sigma'_i` | Dots in scan 16's prose differ from the undotted marginal rational-function formulas. The author's later changes of notation are preserved. |
| Tau | `\tau`, `\dot\tau`, `\tau_i` | The single symbol and indexed lifts are distinguished; the flat-topped tau is not silently read as a sigma. |
| Epsilon | `\varepsilon_i` | The convention change and explicit inversions on scans 13–20 are retained; no global inversion of the symbols was made. |
| Symmetric-group letter | `\unsure{\mathfrak S_3\|\mathcal S_3}` | The large looped S is certain as a letter, but its exact typeface family is not. The uncertainty is retained package-wide. |
| Script extension letter and plain E | `\mathcal E`, `E` | Script and plain forms are distinguished where the ink allows; especially faint or overwritten forms remain doubtful. |
| Hats on extension letters | `\hat{\mathcal E}`, `\widehat{\widehat{\mathcal E}}` | Single and double hats are distinguished, with local uncertainty on scan 26 and elsewhere. |
| Gamma and its decorations | `\Gamma`, `\Gamma_{0,3}`, `\hat\Gamma`, `\widehat{\widehat\Gamma}`, `\tilde\Gamma_P` | Their mathematical meanings are not harmonized here. Subscripts, plus signs and hats follow each occurrence; meanings are discussed separately in the research notes. |
| Leading S and exclamation subgroups | `S\widehat{\widehat{\mathcal E}}^!`, `\widehat{\widehat\Gamma}^!` | Leading S, hat count and exclamation remain independent graphic features. |
| Integer-group letters | `\mathbb Z`, `\hat{\mathbb Z}`, `\hat{\mathbb Z}^*` | Hats and stars appear only where read in the ink; unaccented occurrences are not completed by inference. |
| Character and inertia-map letters | `\chi`, `\kappa_i`, `\hat\kappa_i` | Distinct from lower-case gamma and from the path lambda. |
| Inner-automorphism notation | `\operatorname{int}(g)` or the locally unparenthesized form | Parentheses and dot separators follow the manuscript rather than a uniform house style. |
| Paths and endpoints | `\lambda_i`, `P`, `\bar P` | Path order, bars, and endpoint order remain as written. |
| Primed point labels | `0'`, `1'`, `\infty'` | Scans 28–29; distinct from primes on group elements. |
| Vertical equalities and brace identifications | `\Vert`, `\overset`, `\underset`, `\overbrace`, `\underbrace` | Retained as visible identifications; they are not replaced by explanatory prose. |
| Fundamental products | the written sequence of `l_0`, `l_1`, `l_\infty` | Both orders occur in the manuscript; the explicit correction on scan 17 and later differences are not harmonized. |
| Diagram arrows and undecorated segments | `\arrow` with the locally visible direction and decoration | Arrowheads, equalities, plain segments, hooks and uncertain labels are kept distinct. |
| Separators and the cover logo | `\figure{\begin{tikzpicture}...}` | The separators on scans 15 and 23 are drawings; scan 1's printed logo is a geometric approximation, marked as a crop candidate. |

## Abbreviations and proposed expansions

These are reading aids only. Proposed expansions below are not substituted into the transcription, and a doubtful abbreviation remains doubtful there.

| Written abbreviation or sign | Proposed expansion / qualification |
|---|---|
| `=` or the barred-m form in prose | même; an abbreviation, not an algebraic equality in these verbal contexts |
| `autom.`, `autom`, `Aut` | automorphisme(s) |
| `endom.` | endomorphisme(s) |
| `ext.`, `ext` | extérieur(s) |
| `int.`, `int` | intérieur(s), or the inner-automorphism operation where used as an operator |
| `gr.`, `gr` | groupe |
| `ss-gr.`, `ss-groupe`, `ss-groupes` | sous-groupe(s) |
| `ens.`, `ens`, `sous-ens` | ensemble, sous-ensemble |
| `él.`, `élémt`, `élts` | élément(s) |
| `gén.`, `gén` | générateur(s), according to the passage |
| `hom.`, `hom` | homomorphisme |
| `morph.` | morphisme, in the cancelled occurrence |
| `isom` | isomorphisme(s) |
| `can` | canonique |
| `canoniq` with raised `t` | canoniquement |
| `triv` with raised `t` | trivialement; the abbreviation itself is doubtful on scan 9 |
| `lac` in operator subscripts | lacets / structure à lacets |
| `rev.` | revêtement |
| `syst.` | système |
| `comp.` | composantes, in the passage on connected components |
| `op.` | opération |
| `conj.` | conjugaison; the local word is cancelled or uncertain in several passages |
| `chgts.` | changements |
| `correspond.` | correspondant, probably; retained as written |
| `relati.` | relations, probably; cancelled on scan 23 |
| `pt`, `pts` | point(s) |
| `mb` | membre(s) |
| `resp.` | respectivement |
| `p.r.` | par rapport; an alternative `p.v.` is retained where the ink does not decide |
| `f. et s.` | faut et suffit |
| `sss` | si et seulement si |
| `mod.`, `mod` | modulo |
| `id.`, `id` | identité |
| `def`, `dfn` | définition, as a relation label |
| `NB`, `NB.` | nota bene |
| `i.e.` | id est |
| `p.ex.`, `p.ex` | par exemple |
| `cf.` | confer / compare |
| `etc.`, `etc` | et cetera; retained only where written |

## Legibility and limitations

All 38 whole-page images and both supplied halves of every page were read directly, in order, by the same transcribing stream; every page then received a second visual reading. OCR was not used. The transcription retains uncertain readings in place, including in cancelled passages and formulas; a complete inventory records the attempted transcription of every identified element, not a guarantee that every interpretation of the ink is correct.

The least secure areas are the cramped and stained marginal writing on scan 2, the layered cancellations and shifting indices on scans 13–20, the cancelled superscripts on scans 24–26, the lower-right marginal note on scan 30, and the retraced indices or clipped formula endings on scans 33–34. The precise alphabet of the recurring symmetric-group S, a few hat counts, and several abbreviated word endings remain unresolved. Heavy overlap can conceal an earlier stroke even when the latest reading is intelligible; such uncertainty is marked rather than supplied from mathematical expectation.

Scan 1's printed logo is an approximate TikZ reconstruction rather than a facsimile. The fragment contains no document preamble or editorial mathematical repairs. Structural checks of braces, mathematical delimiters and environments were performed; a full LaTeX compilation could not be completed because the available TeX executables lack the LaTeX format and package files.


## Reading doubts

Locations give a short source-passage anchor and the exact line of the individual LaTeX page file. They do not claim manuscript line numbering: prose was reflowed, and marginal writing is anchored by its own words or formula. Confidence concerns the visible reading, not the mathematical truth of the passage; alternatives remain unresolved.

| Cote | Scan | Approximate source passage / TeX line | Reading | Alternative | Confidence |
|---|---:|---|---|---|---|
| 145 | 2 | Near `\deleted{bien \unsure{distinguer} $\bar D_{J,\alpha}$ de…`; TeX line 2 | `distinguer` | — | medium |
| 145 | 2 | Near `…$\bar D_{J,\alpha}$ de $\bar D_J$, \unsure{cf. 9}}`; TeX line 2 | `cf. 9` | — | medium |
| 145 | 2 | Near `…&& \widetilde U(\mathbb C)\deleted{\unsure{\ne U}} \arrow[dl,"\hat\pi"]…`; TeX line 9 | `\ne U` | — | medium |
| 145 | 2 | Near `H_{\deleted{\unsure{u}}}=\bigl\{u\in G\mid \e…`; TeX line 14 | `u` | — | medium |
| 145 | 2 | Near `\margin{$u$ est \unsure{déterminé} \deleted{\unsure{de}}…`; TeX line 28 | `déterminé` | — | medium |
| 145 | 2 | Near `…$u$ est \unsure{déterminé} \deleted{\unsure{de}} par $v$}`; TeX line 28 | `de` | — | medium |
| 145 | 2 | Near `…onnu quand on connaît $v_*$ (\uline{\unsure{ces conditions}}), et quand $v$ est co…`; TeX line 30 | `ces conditions` | — | medium |
| 145 | 2 | Near `…$ est connu, $u$ est connu \deleted{\unsure{aux}} mod. multiplication à…`; TeX line 30 | `aux` | — | medium |
| 145 | 2 | Near `…ses à droite) s'identifie à un sous-\unsure{ens de l'ens} des ′′germes'' \uline{…`; TeX line 44 | `ens de l'ens` | — | medium |
| 145 | 2 | Near `…′′germes'' \uline{d'isom} \deleted{\unsure{des}} \unsure{ss-groupes\|$\…`; TeX line 44 | `des` | — | medium |
| 145 | 2 | Near `…line{d'isom} \deleted{\unsure{des}} \unsure{ss-groupes\|$\pi$-groupes} d'indice finis de $\pi…`; TeX line 44 | `ss-groupes` | `$\pi$-groupes` | low |
| 145 | 2 | Near `$\unsure{H_n\|H_1}=$ sous-ens de $H$ form…`; TeX line 46 | `H_n` | `H_1` | low |
| 145 | 2 | Near `…peut prendre $\pi',\pi''$ d'indice $\unsure{n\|1}$.`; TeX line 46 | `n` | `1` | low |
| 145 | 2 | Near `$\unsure{H_n\|H_1}$ est un \uline{ss-grou…`; TeX line 48 | `H_n` | `H_1` | low |
| 145 | 3 | Near `Les autom. \inserted{\unsure{inerts}} de $\hat\pi_{0,3}=\pi…`; TeX line 2 | `inerts` | — | medium |
| 145 | 3 | Near `\margin{\uline{\unsure{et ne pas\|et non pas}} \uline{$u$}!}`; TeX line 14 | `et ne pas` | `et non pas` | low |
| 145 | 3 | Near `\margin{NB. On doit en fait avoir $\unsure{\beta=\gamma\|\beta\ne\gamma}$ (\unsure{passer} à $(…`; TeX line 22 | `\beta=\gamma` | `\beta\ne\gamma` | low |
| 145 | 3 | Near `…sure{\beta=\gamma\|\beta\ne\gamma}$ (\unsure{passer} à $(\pi_{0,3})_{\unsur…`; TeX line 22 | `passer` | — | medium |
| 145 | 3 | Near `…}$ (\unsure{passer} à $(\pi_{0,3})_{\unsure{\mathrm{ab}}}$)}`; TeX line 22 | `\mathrm{ab}` | — | medium |
| 145 | 3 | Near `…{p}\cdot\operatorname{int}(\deleted{\unsure{h_1}}h_1')l_1^{p}\cdot\oper…`; TeX line 37 | `h_1` | — | medium |
| 145 | 3 | Near `…dot\operatorname{int}\bigl(\deleted{\unsure{l_1^\mu}}l_\infty^{\unsure{\gam…`; TeX line 37 | `l_1^\mu` | — | medium |
| 145 | 3 | Near `…\deleted{\unsure{l_1^\mu}}l_\infty^{\unsure{\gamma'}}\rho^{\unsure{1\|-1}}({…`; TeX line 37 | `\gamma'` | — | medium |
| 145 | 3 | Near `…u}}l_\infty^{\unsure{\gamma'}}\rho^{\unsure{1\|-1}}({h_1'}^{-1})\bigr)(l_…`; TeX line 37 | `1` | `-1` | low |
| 145 | 3 | Near `(\uline{i.e.} \uline{$\gamma'=\gamma\unsure{+2\mu\|+\mu}$}) et on a la relation…`; TeX line 39 | `+2\mu` | `+\mu` | low |
| 145 | 3 | Near `…rrespondante $(2)_2$ avec $\deleted{\unsure{\beta}}\beta'=\beta$.`; TeX line 39 | `\beta` | — | medium |
| 145 | 4 | Near `\pi\ \Gamma \arrow[d,"\varphi"'] & \unsure{D}_{\pi,\Gamma} \arrow[d]…`; TeX line 3 | `D` | — | medium |
| 145 | 4 | Near `…\unsure{D}_{\pi,\Gamma} \arrow[d] & \unsure{D}_\pi \arrow[l] \arrow[d…`; TeX line 3 | `D` | — | medium |
| 145 | 4 | Near `…\arrow[l] \arrow[d] & \widetilde B_{\unsure{\pi\|\Gamma}} \arrow[l] \\`; TeX line 3 | `\pi` | `\Gamma` | low |
| 145 | 4 | Near `\pi'\ \Gamma & \deleted{\unsure{D}}B_{\pi',\Gamma} \arrow…`; TeX line 4 | `D` | — | medium |
| 145 | 4 | Near `& B_\Gamma & \widetilde B_{\unsure{\Gamma}} \arrow[l] &`; TeX line 5 | `\Gamma` | — | medium |
| 145 | 4 | Near `\unsure{D}_{\pi,\Gamma} \arrow[d,…`; TeX line 8 | `D` | — | medium |
| 145 | 4 | Near `…D}_{\pi,\Gamma} \arrow[d,no head] & \unsure{D}_{\pi,\Gamma_i} \arrow[…`; TeX line 8 | `D` | — | medium |
| 145 | 4 | Near `…ma_i} \arrow[l,no head] \arrow[d] & \unsure{D}_\pi \arrow[l,no head]…`; TeX line 8 | `D` | — | medium |
| 145 | 4 | Near `\unsure{B}_{\pi',\Gamma} \arrow[d…`; TeX line 9 | `B` | — | medium |
| 145 | 4 | Near `…unsure{B}_{\pi',\Gamma} \arrow[d] & \unsure{B}_{\pi',\Gamma_i} \arrow…`; TeX line 9 | `B` | — | medium |
| 145 | 4 | Near `…ma_i} \arrow[l,no head] \arrow[d] & \unsure{B}_{\pi'} \arrow[l] \arro…`; TeX line 9 | `B` | — | medium |
| 145 | 4 | Near `Soit $\deleted{\unsure{E}}\mathcal E_\varphi=\bi…`; TeX line 34 | `E` | — | medium |
| 145 | 4 | Near `\deleted{\unsure{$\mathcal E$}}`; TeX line 36 | `$\mathcal E$` | — | medium |
| 145 | 4 | Near `\unsure{\widehat{\widehat{\mathcal E}}}(\pi,I') \arrow[d,"\uns…`; TeX line 41 | `\widehat{\widehat{\mathcal E}}` | — | medium |
| 145 | 4 | Near `…hat{\mathcal E}}}(\pi,I') \arrow[d,"\unsure{\Psi_{\pi'}}",two heads] \arrow[dd,…`; TeX line 41 | `\Psi_{\pi'}` | — | medium |
| 145 | 4 | Near `\unsure{\widehat{\widehat{G}}}(\pi') \arrow[d,"p"] \\`; TeX line 42 | `\widehat{\widehat{G}}` | — | medium |
| 145 | 4 | Near `\unsure{\widehat{G}}(\pi')`; TeX line 43 | `\widehat{G}` | — | medium |
| 145 | 4 | Near `1\arrow[r,no head] & \deleted{\unsure{e}}\pi\arrow[r]\arrow[d,"…`; TeX line 46 | `e` | — | medium |
| 145 | 4 | Near `…ed{\unsure{e}}\pi\arrow[r]\arrow[d,"\unsure{f_\pi}"] & \unsure{\widehat{\…`; TeX line 46 | `f_\pi` | — | medium |
| 145 | 4 | Near `…rrow[r]\arrow[d,"\unsure{f_\pi}"] & \unsure{\widehat{\widehat{G}}}(\pi,I')\arrow[r]\arrow…`; TeX line 46 | `\widehat{\widehat{G}}` | — | medium |
| 145 | 4 | Near `…ehat{G}}}(\pi,I')\arrow[r]\arrow[d,"\unsure{f_{\hat G}}"] & {}\\`; TeX line 46 | `f_{\hat G}` | — | medium |
| 145 | 4 | Near `…\arrow[r,no head] & \pi'\arrow[r] & \unsure{\widehat{\widehat{\mathcal E}}}(\pi')\arrow[r] & {}`; TeX line 47 | `\widehat{\widehat{\mathcal E}}` | — | medium |
| 145 | 4 | Near `\[\bigl(\simeq\unsure{\widehat{\widehat{\mathcal E}}}(\pi,I')\bigr)\]}`; TeX line 49 | `\widehat{\widehat{\mathcal E}}` | — | medium |
| 145 | 5 | Near `\margin{\unsure{$\partial$}}`; TeX line 6 | `$\partial$` | — | medium |
| 145 | 5 | Near `…0',l_1',l_\infty'$ satisfaisant la $\unsure{\bar m\|=}$ relation --- sauf err…`; TeX line 12 | `\bar m` | `=` | low |
| 145 | 5 | Near `…rted{$(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\inft…`; TeX line 25 | `l_0` | — | medium |
| 145 | 5 | Near `…nfty^2=\mathrm{id}$. On définit de $\unsure{\bar m\|=}$ $\sigma_0,\sigma_1$ \…`; TeX line 27 | `\bar m` | `=` | low |
| 145 | 5 | Near `…omme des éléments du gr. \inserted{$\unsure{\mathfrak S_3\|\mathcal S_3}$} des permutations de…`; TeX line 31 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 5 | Near `…tations de l'ens. $\{0,1,\infty\}$, \unsure{qu'on\|puis on} se propose de le faire…`; TeX line 31 | `qu'on` | `puis on` | low |
| 145 | 5 | Near `…vraie} représentation du ss-groupe $\unsure{\mathfrak S_3^+\|\mathcal S_3^+}\simeq\mathbb Z/3\mathb…`; TeX line 31 | `\mathfrak S_3^+` | `\mathcal S_3^+` | low |
| 145 | 6 | Near `par $\rho$, mais pas de $\unsure{\mathfrak S_3\|\mathcal S_3}$, car on a p.ex`; TeX line 2 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 6 | Near `\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\…`; TeX line 7 | `\sigma_0^{-1}\sigma_1^{-1}` | — | medium |
| 145 | 6 | Near `…sigma_1)^2=\rho^2}\qquad\text{dans }\unsure{\mathfrak S_3\|\mathcal S_3}`; TeX line 7 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 6 | Near `…$\operatorname{Aut}(\pi)$, \deleted{\unsure{on a}}`; TeX line 9 | `on a` | — | medium |
| 145 | 6 | Near `…^{-1}=l_1^{-1}l_\infty^{-1}\deleted{\unsure{l_1}}\\`; TeX line 21 | `l_1` | — | medium |
| 145 | 6 | Near `…ns $\operatorname{Aut}(\pi)$ et de $\unsure{=\|\bar m}$`; TeX line 25 | `=` | `\bar m` | low |
| 145 | 6 | Near `On a une représentation de $\unsure{\mathfrak S_3\|\mathcal S_3}$ dans le groupe \uline…`; TeX line 33 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 6 | Near `…ins pour le groupe discret) vu que $\unsure{\mathfrak S_3\|\mathcal S_3}$ opérant sur $\mathbb…`; TeX line 33 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 6 | Near `…bb C}-\{0,1,\infty\}$ admet un (et $\unsure{=\|\bar m}$ deux!) point fixe, \i…`; TeX line 33 | `=` | `\bar m` | low |
| 145 | 6 | Near `…x!) point fixe, \inserted{à savoir $\unsure{-\bar j\|-j}$ ($j$ racine primitive…`; TeX line 33 | `-\bar j` | `-j` | low |
| 145 | 6 | Near `…e troisième de $1$)} qu'on \deleted{\unsure{pourra}} a pris comme origine…`; TeX line 33 | `pourra` | — | medium |
| 145 | 7 | Near `…érifie qu'il commute à l'action de $\unsure{\mathfrak S_3\|\mathcal S_3}$ mod. autom extérieurs…`; TeX line 11 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 7 | Near `…ce qui donne une op. extérieure de $\unsure{\mathfrak S_3\|\mathcal S_3}\times\{\pm1\}=\Gamma_{…`; TeX line 11 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 7 | Near `…un autom $u$ qui normalise \deleted{\unsure{un}} $L_0$ ($\simeq\hat{\m…`; TeX line 13 | `un` | — | medium |
| 145 | 7 | Near `…, $\in\hat{\mathbb Z}^{*}$ \deleted{\unsure{est}} est le multiplicateur…`; TeX line 13 | `est` | — | medium |
| 145 | 8 | Near `…si on \deleted{multiplie} remplace \unsure{$g$\|$u$} par $\operatorname{int…`; TeX line 2 | `$g$` | `$u$` | low |
| 145 | 8 | Near `…in L_0$ ($\alpha\in\hat{\mathbb Z}^{\unsure{*}}$), alors $g$ est remp…`; TeX line 2 | `*` | — | medium |
| 145 | 8 | Near `\lambda g\rho(\unsure{l_0\|\lambda})^{-1}=\uline{l_0^\alph…`; TeX line 4 | `l_0` | `\lambda` | low |
| 145 | 8 | Near `Ceci posé, \deleted{\unsure{les}} les relations $(*)$ e…`; TeX line 6 | `les` | — | medium |
| 145 | 8 | Near `=\deleted{\unsure{\operatorname{int}g\rho(g)l_\infty^p}}\inserted{\operatornam…`; TeX line 13 | `\operatorname{int}g\rho(g)l_\infty^p` | — | medium |
| 145 | 8 | Near `Les relations $(*)\unsure{,}$ et $(**)$ sont vérifi…`; TeX line 37 | `,` | — | medium |
| 145 | 8 | Near `…construction (pour $**$, il suffit $\unsure{=\|\bar m}$ de la vérifier pour l…`; TeX line 37 | `=` | `\bar m` | low |
| 145 | 8 | Near `…r m}$ de la vérifier pour la valeur \unsure{aux\|des} deux mb en $l_0,l_1$).`; TeX line 37 | `aux` | `des` | low |
| 145 | 9 | Near `…omorphisme, mais un automorphisme ? \unsure{Ça} semble délicat\ldots`; TeX line 3 | `Ça` | — | medium |
| 145 | 9 | Near `…n de $u$ (comme autom ext \inserted{\unsure{respectant} la structure à lacets}…`; TeX line 9 | `respectant` | — | medium |
| 145 | 9 | Near `…cets}) non seulement à $\rho$ i.e. $\unsure{\mathfrak S_3^+\|\mathcal S_3^+}$, mais à $\unsure{\mat…`; TeX line 9 | `\mathfrak S_3^+` | `\mathcal S_3^+` | low |
| 145 | 9 | Near `…rak S_3^+\|\mathcal S_3^+}$, mais à $\unsure{\mathfrak S_3\|\mathcal S_3}$ tout entier. Il suffi…`; TeX line 9 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 9 | Near `…uline{NB} Ceci implique qu'il opère \unsure{triv\textsuperscript{t}} sur l'ens. des trois c…`; TeX line 10 | `triv\textsuperscript{t}` | — | medium |
| 145 | 9 | Near `…infty=\operatorname{int}(h)\deleted{\unsure{u}}\sigma_\infty u,`; TeX line 12 | `u` | — | medium |
| 145 | 10 | Near `\exists\ q,r\in\hat{\mathbb Z}^{\unsure{*}}\quad\text{tels que}\q…`; TeX line 4 | `*` | — | medium |
| 145 | 10 | Near `on trouve, en \unsure{passant} au groupe \unsure{abél…`; TeX line 10 | `passant` | — | medium |
| 145 | 10 | Near `…ouve, en \unsure{passant} au groupe \unsure{abélien}, que $\beta=\gamma$ (i…`; TeX line 10 | `abélien` | — | medium |
| 145 | 10 | Near `…défini par $u$, et pas du \deleted{\unsure{choix de u}} de son représentant d…`; TeX line 28 | `choix de u` | — | medium |
| 145 | 11 | Near `plus haut, \deleted{\unsure{pour $g$}} \inserted{savoir $\ta…`; TeX line 3 | `pour $g$` | — | medium |
| 145 | 11 | Near `…avoir $\tau$}, correspond. \deleted{\unsure{aux}} à`; TeX line 3 | `aux` | — | medium |
| 145 | 11 | Near `…e cyclotomique $\chi$, une \deleted{\unsure{deux}} fonction numérique \i…`; TeX line 11 | `deux` | — | medium |
| 145 | 11 | Near `…pi}{\overset{\Vert}{\hat\pi_{0,3}}},\unsure{\mathfrak S_3\|\mathcal S_3})\overset{\mathrm{def}}…`; TeX line 13 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 11 | Near `\deleted{\unsure{donnée}} à valeurs dans $\hat{…`; TeX line 15 | `donnée` | — | medium |
| 145 | 11 | Near `…est un $1$-cocycle sur $\mathcal E_0\unsure{=\|\simeq}\operatorname{Aut}_{\ma…`; TeX line 26 | `=` | `\simeq` | low |
| 145 | 11 | Near `…_{\mathrm{lac}}(\pi,L_0)$, \deleted{\unsure{groupe}} \inserted{\unsure{qui…`; TeX line 26 | `groupe` | — | medium |
| 145 | 11 | Near `…\deleted{\unsure{groupe}} \inserted{\unsure{qui définit}} le ss-gr. des élément…`; TeX line 26 | `qui définit` | — | medium |
| 145 | 11 | Near `…des éléments qui commutent ext. à $\unsure{\mathfrak S_3\|\mathcal S_3}$}`; TeX line 26 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 11 | Near `est injective, \deleted{\unsure{et}} $\beta$ étant défini…`; TeX line 27 | `et` | — | medium |
| 145 | 12 | Near `u(L_1)=\operatorname{int}(g)(L_{\unsure{1\|0}})`; TeX line 13 | `1` | `0` | low |
| 145 | 12 | Near `et ceci détermine déjà \deleted{\unsure{$\operatorname{int}(g)$}} modulo multiplication…`; TeX line 15 | `$\operatorname{int}(g)$` | — | medium |
| 145 | 12 | Near `…un él\textsuperscript{t} de $L_1$, \unsure{par} la donnée de $u$.}`; TeX line 15 | `par` | — | medium |
| 145 | 12 | Near `On a des vues plus géométriques \unsure{de} \inserted{\unsure{sur}…`; TeX line 17 | `de` | — | medium |
| 145 | 12 | Near `…géométriques \unsure{de} \inserted{\unsure{sur}} l'extension de $\unsu…`; TeX line 17 | `sur` | — | medium |
| 145 | 12 | Near `…erted{\unsure{sur}} l'extension de $\unsure{\mathfrak S_3\|\mathcal S_3}$ par $\pi$ \inserted{d…`; TeX line 17 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 12 | Near `…ma_0\sigma_1=l_1^{-1}\rho$ \deleted{\unsure{p.ex.}} i.e. $\rho=\sigma_0\s…`; TeX line 17 | `p.ex.` | — | medium |
| 145 | 12 | Near `…arepsilon_i$ sera l'unique \deleted{\unsure{él\textsuperscript{t}}} \inserted{autom.} dan…`; TeX line 22 | `él\textsuperscript{t}` | — | medium |
| 145 | 12 | Near `…{et} qui fixe $l_i$ et est \deleted{\unsure{de\|$\sigma$}} \inserted{\unsure{de…`; TeX line 22 | `de` | `$\sigma$` | low |
| 145 | 12 | Near `…ted{\unsure{de\|$\sigma$}} \inserted{\unsure{de carré $l_i$}}`; TeX line 22 | `de carré $l_i$` | — | medium |
| 145 | 13 | Near `…me{int}(l_0)\sigma_\infty)\inserted{\unsure{\operatorname{int}(l_\infty^\alpha)}}\qquad\text{i.e.}\quad`; TeX line 7 | `\operatorname{int}(l_\infty^\alpha)` | — | medium |
| 145 | 13 | Near `\deleted{et de $\unsure{=\|\bar m}$`; TeX line 10 | `=` | `\bar m` | low |
| 145 | 13 | Near `\varepsilon_0=\operatorname{int}(l_{\unsure{1\|0}})\sigma_0`; TeX line 12 | `1` | `0` | low |
| 145 | 13 | Near `…peratorname{Aut}(\pi)$, je \deleted{\unsure{trouve}} \inserted{\unsure{écr…`; TeX line 16 | `trouve` | — | medium |
| 145 | 13 | Near `…\deleted{\unsure{trouve}} \inserted{\unsure{écris}}`; TeX line 16 | `écris` | — | medium |
| 145 | 13 | Near `…\sigma_\infty(l_\infty)}_{\inserted{\unsure{l_0l_\infty}}}\sigma_\infty(l_\inft…`; TeX line 31 | `l_0l_\infty` | — | medium |
| 145 | 13 | Near `\deleted{\unsure{l_\infty^{-1}l_\infty}}l_0^{1-\alpha}l_1^{2-\…`; TeX line 40 | `l_\infty^{-1}l_\infty` | — | medium |
| 145 | 13 | Near `\margin{\unsure{prends} $\alpha=\unsure{2\|1}$…`; TeX line 45 | `prends` | — | medium |
| 145 | 13 | Near `\margin{\unsure{prends} $\alpha=\unsure{2\|1}$ ?}`; TeX line 45 | `2` | `1` | low |
| 145 | 14 | Near `\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty\|\varepsilon_1}`; TeX line 34 | `\varepsilon_\infty` | `\varepsilon_1` | low |
| 145 | 14 | Near `…varepsilon_0\varepsilon_1^{\deleted{\unsure{2}}}\underbrace{\varepsil…`; TeX line 45 | `2` | — | medium |
| 145 | 14 | Near `…argin{ces relations ne semblent pas \unsure{conséquences} des autres}`; TeX line 55 | `conséquences` | — | medium |
| 145 | 14 | Near `…est inquiétant, car il n'y a pas d'\unsure{élém\textsuperscript{ts}}`; TeX line 60 | `élém\textsuperscript{ts}` | — | medium |
| 145 | 15 | Near `…groupe envisagé \inserted{\deleted{\unsure{stable}} \unsure{fixé} par $\u…`; TeX line 2 | `stable` | — | medium |
| 145 | 15 | Near `…\inserted{\deleted{\unsure{stable}} \unsure{fixé} par $\unsure{\rho\|\var…`; TeX line 2 | `fixé` | — | medium |
| 145 | 15 | Near `…\unsure{stable}} \unsure{fixé} par $\unsure{\rho\|\varphi}$}, il faudrait donc av…`; TeX line 2 | `\rho` | `\varphi` | low |
| 145 | 15 | Near `…e{\sigma_0l_0}_{\substack{\inserted{\unsure{l_1l_\infty\|l_\infty}}\\\deleted{l_1^{-1}l_\…`; TeX line 8 | `l_1l_\infty` | `l_\infty` | low |
| 145 | 15 | Near `…e plus il faudrait pour les groupes \unsure{discrets} \deleted{utiliser} (et…`; TeX line 41 | `discrets` | — | medium |
| 145 | 15 | Near `…e{discrets} \deleted{utiliser} (et $\unsure{\bar m\|=}$ pour les`; TeX line 41 | `\bar m` | `=` | low |
| 145 | 16 | Near `\pi=\pi_{\unsure{1\|*}}(\overbrace{\mathbb P^…`; TeX line 4 | `1` | `*` | low |
| 145 | 16 | Near `…autour de l'axe $P,\bar P$ \deleted{\unsure{qui}} induit sur $(0,1,\inf…`; TeX line 6 | `qui` | — | medium |
| 145 | 16 | Near `…athbb P^1_{\mathbb C}$ qui \deleted{\unsure{échangent}} \inserted{\deleted{fi…`; TeX line 6 | `échangent` | — | medium |
| 145 | 16 | Near `…deleted{fixent}} induisent \deleted{\unsure{sur}} sur $(0,1,\infty)$ le…`; TeX line 6 | `sur` | — | medium |
| 145 | 16 | Near `…ymétries} autour des axes \deleted{$\unsure{P,\bar P}$} $(0,2)$, $(1,-1)$ et…`; TeX line 6 | `P,\bar P` | — | medium |
| 145 | 16 | Near `…plan $(0,1,\infty)$. On considère $\unsure{\mathfrak S_3\|\mathcal S_3}$ comme opérant sur $(0…`; TeX line 17 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 16 | Near `…$(0,1,\infty)$ dans cet ordre, et $\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$ comm…`; TeX line 17 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 16 | Near `…_0,\dot\sigma_1,\dot\sigma_\infty\in\unsure{\mathfrak S_3\|\mathcal S_3}$ et $\dot\tau\in\mathb…`; TeX line 17 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 16 | Near `…On considère l'extension \inserted{$\unsure{\mathcal E_0}$} de $\unsure{\mathfra…`; TeX line 17 | `\mathcal E_0` | — | medium |
| 145 | 16 | Near `…serted{$\unsure{\mathcal E_0}$} de $\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$ par…`; TeX line 17 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 16 | Near `…bstack{\Vert\\U_{0,3}}}{U_{\deleted{\unsure{0,3}}}},\underbrace{\unsure…`; TeX line 19 | `0,3` | — | medium |
| 145 | 16 | Near `…deleted{\unsure{0,3}}}},\underbrace{\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2}_{\Ga…`; TeX line 19 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 17 | Near `…e fondamental mixte est défini à la \unsure{Malgoire}, \deleted{\unsure{comp…`; TeX line 3 | `Malgoire` | — | medium |
| 145 | 17 | Near `…ni à la \unsure{Malgoire}, \deleted{\unsure{comprenant}} les classes $(\gamma,…`; TeX line 3 | `comprenant` | — | medium |
| 145 | 17 | Near `comme les couples d'un $\unsure{\sigma_i\|\dot\sigma_i}$, et des chemins \inse…`; TeX line 13 | `\sigma_i` | `\dot\sigma_i` | low |
| 145 | 17 | Near `…erted{$\lambda_i$} de $P$ à $\bar P=\unsure{\sigma_i\|\dot\sigma_i}P$ qui se fait sur \del…`; TeX line 13 | `\sigma_i` | `\dot\sigma_i` | low |
| 145 | 17 | Near `…d{stable par la symétrie} \inserted{\unsure{ens. des pts fixes}} \deleted{$\tau\sigma_…`; TeX line 13 | `ens. des pts fixes` | — | medium |
| 145 | 17 | Near `…a_i=\dot\sigma_i\dot\tau$ (symétrie \unsure{par un plan}, fixant $P,\bar P,a_i$…`; TeX line 13 | `par un plan` | — | medium |
| 145 | 17 | Near `…eant les deux autres $a_j,a_k$), et \unsure{ne} passant pas par $a_i$.…`; TeX line 13 | `ne` | — | medium |
| 145 | 17 | Near `…ne} passant pas par $a_i$. \deleted{\unsure{Au}} Désignant par $l_0,l_…`; TeX line 13 | `Au` | — | medium |
| 145 | 17 | Near `…t par $l_0,l_1,l_\infty$ \inserted{(\unsure{sur\|pour} $1\in\Gamma$)} les lac…`; TeX line 13 | `sur` | `pour` | low |
| 145 | 17 | Near `…llant vers $0,1,\infty$ suivant des \unsure{quarts} de grands cercles, on…`; TeX line 13 | `quarts` | — | medium |
| 145 | 17 | Near `(et non $l_0l_1l_\infty=1$ ! \unsure{?} On peut l'écrire $l_0^…`; TeX line 17 | `?` | — | medium |
| 145 | 18 | Near `\sigma_0\sigma_1=\deleted{\unsure{l_0\rho}}\inserted{\rho l_0}\qq…`; TeX line 5 | `l_0\rho` | — | medium |
| 145 | 18 | Near `\sigma_1\sigma_\infty=\deleted{\unsure{l_1\rho}}\inserted{\rho l_1}\qq…`; TeX line 6 | `l_1\rho` | — | medium |
| 145 | 18 | Near `l_0&=(\sigma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\si…`; TeX line 13 | `\sigma_\infty` | — | medium |
| 145 | 18 | Near `…igma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\sigma_0\rho^{-1}})\\`; TeX line 13 | `l_0\sigma_0\sigma_0\rho^{-1}` | — | medium |
| 145 | 18 | Near `l_1&=(\sigma_1\rho)^2\unsure{\sigma_1}\\`; TeX line 14 | `\sigma_1` | — | medium |
| 145 | 18 | Near `l_\infty&=(\sigma_\infty\rho)^2\unsure{\sigma_\infty}\\`; TeX line 15 | `\sigma_\infty` | — | medium |
| 145 | 18 | Near `\unsure{l_0}&=\unsure{\rho^{-1}\sig…`; TeX line 16 | `l_0` | — | medium |
| 145 | 18 | Near `\unsure{l_0}&=\unsure{\rho^{-1}\sigma_0}`; TeX line 16 | `\rho^{-1}\sigma_0` | — | medium |
| 145 | 18 | Near `…rbrace{\rho^{-1}\sigma_0}_{\deleted{\unsure{\sigma_\infty}}}\rho\sigma_0\rho^{-1}`; TeX line 20 | `\sigma_\infty` | — | medium |
| 145 | 18 | Near `\sigma_0(l_\infty)&=\unsure{l_1^{-1}l_0^{-1}}`; TeX line 28 | `l_1^{-1}l_0^{-1}` | — | medium |
| 145 | 18 | Near `…t s'exprimer en fonction des $l_i$; \unsure{puisque} en outre`; TeX line 52 | `puisque` | — | medium |
| 145 | 18 | Near `…ted{ou $\sigma_0\sigma_1\sigma_0=$} \unsure{et $\sigma$}}`; TeX line 56 | `et $\sigma$` | — | medium |
| 145 | 18 | Near `\dot\sigma_{\unsure{1\|0}}^2=\dot\sigma_{\unsure…`; TeX line 59 | `1` | `0` | low |
| 145 | 18 | Near `…\sigma_{\unsure{1\|0}}^2=\dot\sigma_{\unsure{1\|0}}^2=\dot\sigma_\infty^2…`; TeX line 59 | `1` | `0` | low |
| 145 | 18 | Near `\quad\text{est une présentation de }\unsure{\mathfrak S_3\|\mathcal S_3}\text{),}`; TeX line 63 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 18 | Near `\margin{\unsure{comme on voit} \unsure{ils sont} \uns…`; TeX line 65 | `comme on voit` | — | medium |
| 145 | 18 | Near `\margin{\unsure{comme on voit} \unsure{ils sont} \unsure{pas conjugués}…`; TeX line 65 | `ils sont` | — | medium |
| 145 | 18 | Near `…re{comme on voit} \unsure{ils sont} \unsure{pas conjugués}}`; TeX line 65 | `pas conjugués` | — | medium |
| 145 | 18 | Near `…présentation de l'image inverse de $\unsure{\mathfrak S_3\|\mathcal S_3}$ dans $\mathcal E$ (di…`; TeX line 70 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 18 | Near `…aisant dans les relations $\rho=1$, \unsure{on a le groupe $(\sigma_i)$}.}`; TeX line 71 | `on a le groupe $(\sigma_i)$` | — | medium |
| 145 | 19 | Near `\varepsilon_0&=l_0^{\deleted{\unsure{-1}}}\sigma_0l_1^{\deleted…`; TeX line 4 | `-1` | — | medium |
| 145 | 19 | Near `…{\unsure{-1}}}\sigma_0l_1^{\deleted{\unsure{-1}}}\\`; TeX line 4 | `-1` | — | medium |
| 145 | 19 | Near `\varepsilon_1&=l_1^{\deleted{\unsure{-1}}}\sigma_1l_\infty^{\de…`; TeX line 5 | `-1` | — | medium |
| 145 | 19 | Near `…ure{-1}}}\sigma_1l_\infty^{\deleted{\unsure{-1}}}\\`; TeX line 5 | `-1` | — | medium |
| 145 | 19 | Near `…l_\infty\sigma_\infty l_0^{\deleted{\unsure{-1}}}`; TeX line 6 | `-1` | — | medium |
| 145 | 19 | Near `…nfty(l_1l_\infty)^{-1}=l_1^{-1}}}l_{\unsure{1}}=l_0l_\infty l_\infty^…`; TeX line 19 | `1` | — | medium |
| 145 | 19 | Near `…psilon_i^{-1}$ de tantôt ! \deleted{\unsure{il faudrait}} \inserted{qu'il faudr…`; TeX line 21 | `il faudrait` | — | medium |
| 145 | 19 | Near `…}} \inserted{qu'il faudra} \deleted{\unsure{ici}} donc noter $\varepsil…`; TeX line 21 | `ici` | — | medium |
| 145 | 19 | Near `…epsilon_0\varepsilon_1=\rho\deleted{\unsure{l_\infty}}(\ldots),\quad\varepsi…`; TeX line 28 | `l_\infty` | — | medium |
| 145 | 19 | Near `=l_0l_\infty^2\rho\unsure{l_0}l_\infty`; TeX line 38 | `l_0` | — | medium |
| 145 | 19 | Near `\varepsilon_0\varepsilon_1\deleted{\unsure{\varepsilon}}&=l_0l_\infty^2\rho\un…`; TeX line 43 | `\varepsilon` | — | medium |
| 145 | 19 | Near `…ure{\varepsilon}}&=l_0l_\infty^2\rho\unsure{l_0}l_\infty\\`; TeX line 43 | `l_0` | — | medium |
| 145 | 19 | Near `…on_1\varepsilon_\infty&=l_1l_0^2\rho\unsure{l_1}l_0\\`; TeX line 44 | `l_1` | — | medium |
| 145 | 19 | Near `…fty\varepsilon_0&=l_\infty l_1^2\rho\unsure{l_\infty}l_1`; TeX line 45 | `l_\infty` | — | medium |
| 145 | 19 | Near `…lon_\infty,\rho$, avec relations de \unsure{définition}`; TeX line 48 | `définition` | — | medium |
| 145 | 20 | Near `\deleted{$\unsure{[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}]`; TeX line 21 | `[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}] [\underbrace{\rho\sigma_0\rho^{-1}}_{\sigma_1} \underbrace{\rho^{-1}\sigma_0\rho}_{\sigma_\infty}\rho^{-1}]=1` | — | medium |
| 145 | 20 | Near `…4) est conséquence des précédentes (\unsure{vient du fait} $\sigma_1=\rho\sigma_0…`; TeX line 24 | `vient du fait` | — | medium |
| 145 | 20 | Near `l_0&=\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2}}\rho^{-1}(\sigma_0\rho…`; TeX line 27 | `(\rho\sigma_0\rho^{-1})^2` | — | medium |
| 145 | 20 | Near `l_1&=(\deleted{\unsure{\rho}}\sigma_0\rho)^2\\`; TeX line 29 | `\rho` | — | medium |
| 145 | 20 | Near `…_\infty&=(\rho^{-1}\sigma_0\deleted{\unsure{\rho}})^2`; TeX line 30 | `\rho` | — | medium |
| 145 | 20 | Near `\sigma_0(l_\infty)&=l_1\deleted{\unsure{l_\infty^{-1}}}`; TeX line 45 | `l_\infty^{-1}` | — | medium |
| 145 | 20 | Near `…prouve que $\rho$ n'est pas un mot \unsure{p.r.\|p.v.} aux $\sigma_i$\ldots`; TeX line 49 | `p.r.` | `p.v.` | low |
| 145 | 20 | Near `…les relations des débuts, \deleted{\unsure{si dans ces dernières on avait tout pris des primes}, et \unsure{pris les t…`; TeX line 51 | `si dans ces dernières on avait tout pris des primes` | — | medium |
| 145 | 20 | Near `…on avait tout pris des primes}, et \unsure{pris les transposés} $l_i'=l_i^{-1}$, $\sig…`; TeX line 51 | `pris les transposés` | — | medium |
| 145 | 20 | Near `…$l_i'=l_i^{-1}$, $\sigma_i'=\sigma_{\unsure{\dot\rho(i)}}$}`; TeX line 51 | `\dot\rho(i)` | — | medium |
| 145 | 20 | Near `\deleted{i.e. $\sigma_i$} \deleted{\unsure{de notre groupe} $\sigma_i'$} si on y r…`; TeX line 52 | `de notre groupe` | — | medium |
| 145 | 20 | Near `…échange }l_j\text{ et }l_{\deleted{\unsure{j}}k}`; TeX line 56 | `j` | — | medium |
| 145 | 20 | Near `&\deleted{\text{(et le }\unsure{\text{devenir}}\ l_{\dot\rho(i)}\ \tex…`; TeX line 58 | `\text{devenir}` | — | medium |
| 145 | 20 | Near `…ralisateur (ou normalisateur, c'est \unsure{idem}) des $L_i$ dans $\math…`; TeX line 63 | `idem` | — | medium |
| 145 | 20 | Near `\varepsilon_0&=l_0^{\unsure{-1}}\sigma_1\unsure{l_1^{-…`; TeX line 66 | `-1` | — | medium |
| 145 | 20 | Near `…epsilon_0&=l_0^{\unsure{-1}}\sigma_1\unsure{l_1^{-1}\|l_0^{-1}}\\`; TeX line 66 | `l_1^{-1}` | `l_0^{-1}` | low |
| 145 | 20 | Near `…_\infty&=l_0^{-1}\sigma_0 l_\infty^{\unsure{-1}}`; TeX line 68 | `-1` | — | medium |
| 145 | 20 | Near `\mspage{\unsure{19\|10}}`; TeX line 71 | `19` | `10` | low |
| 145 | 21 | Near `…et{\deleted{\sim}}{\rho}\ \deleted{(\unsure{=\rho})}\\`; TeX line 7 | `=\rho` | — | medium |
| 145 | 21 | Near `…ue $\tilde{\mathcal E}$ de $\varphi(\unsure{\tilde{\mathfrak S}_3\|\tilde{\mathcal S}_3})\subset\Gamma$ (ss-gro…`; TeX line 22 | `\tilde{\mathfrak S}_3` | `\tilde{\mathcal S}_3` | low |
| 145 | 21 | Near `…2) est produit $\frac12$ direct de $\unsure{\tilde{\mathfrak S}_3\|\tilde{\mathcal S}_3}$ et de $\pi$. Il faut…`; TeX line 22 | `\tilde{\mathfrak S}_3` | `\tilde{\mathcal S}_3` | low |
| 145 | 21 | Near `…roupe, On trouve que $\tilde\sigma_{\unsure{i\|0}}$ est au dessus $\varp…`; TeX line 22 | `i` | `0` | low |
| 145 | 21 | Near `…st au dessus $\varphi(\tilde\sigma_{\unsure{i\|0}})$ i.e. la symétrie p.…`; TeX line 22 | `i` | `0` | low |
| 145 | 21 | Near `…plan passant par $P,\bar P,\deleted{\unsure{a_i}}i$, qui transforme $l_…`; TeX line 22 | `a_i` | — | medium |
| 145 | 21 | Near `…e structure, via les opérations de $\unsure{\tilde{\mathfrak S}_3\|\tilde{\mathcal S}_3}$ sur $(U,P)$.}`; TeX line 23 | `\tilde{\mathfrak S}_3` | `\tilde{\mathcal S}_3` | low |
| 145 | 21 | Near `…\tilde\sigma_i'$ à des éléments de $\unsure{S\mathcal E\|\mathcal S\mathcal E}$, cf plus bas\ldots}`; TeX line 33 | `S\mathcal E` | `\mathcal S\mathcal E` | low |
| 145 | 21 | Near `…peut maintenant revenir à nos trois \unsure{miroirs}, \unsure{d.} par`; TeX line 36 | `miroirs` | — | medium |
| 145 | 21 | Near `…venir à nos trois \unsure{miroirs}, \unsure{d.} par`; TeX line 36 | `d.` | — | medium |
| 145 | 22 | Near `\deleted{\unsure{\varepsilon_0}}\ \varepsilon_1&=\vare…`; TeX line 7 | `\varepsilon_0` | — | medium |
| 145 | 22 | Near `…ie de $P$ dans $\Gamma=\Gamma_{0,3}=\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$, qui…`; TeX line 15 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 22 | Near `\varphi:\unsure{\mathfrak S_3\|\mathcal S_3}&\longrightarrow\Gamma=…`; TeX line 22 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 22 | Near `…\mathcal S_3}&\longrightarrow\Gamma=\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2\\`; TeX line 22 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 22 | Near `…gma\longrightarrow\tilde\sigma:\quad\unsure{\mathfrak S_3\|\mathcal S_3}\longrightarrow\mathcal…`; TeX line 28 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 22 | Near `\margin{on a d'autre part \deleted{$\unsure{\tilde\rho}$} $\widetilde{\dot\rho…`; TeX line 34 | `\tilde\rho` | — | medium |
| 145 | 23 | Near `…e groupe cartographique ′′triangulé \unsure{pondéré\|pointé}'' de Malgoire, ayant c…`; TeX line 3 | `pondéré` | `pointé` | low |
| 145 | 23 | Near `…\tau_0,\tau_1,\tau_\infty$ \deleted{\unsure{relati.}} avec`; TeX line 3 | `relati.` | — | medium |
| 145 | 23 | Near `…tau_\infty={}}\ l_0&=\tau_{\deleted{\unsure{0}}\infty}\tau_{\deleted{…`; TeX line 6 | `0` | — | medium |
| 145 | 23 | Near `…ed{\unsure{0}}\infty}\tau_{\deleted{\unsure{\infty}}1}\\`; TeX line 6 | `\infty` | — | medium |
| 145 | 23 | Near `…nfty\tau_0={}}\ l_1&=\tau_{\deleted{\unsure{\infty}}0}\tau_\infty\\`; TeX line 7 | `\infty` | — | medium |
| 145 | 23 | Near `\margin{On a les relations $\unsure{\rho}$}`; TeX line 15 | `\rho` | — | medium |
| 145 | 23 | Near `…n de $\hat\Gamma_{0,3}=\Gamma_{0,3}=\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$ par…`; TeX line 16 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 24 | Near `…signe par $\Gamma$ le commutant de $\unsure{\mathfrak S_3\|\mathcal S_3}$ dans $\widehat{\wideh…`; TeX line 2 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 24 | Near `…widehat{\widehat\Gamma}$ \inserted{(\unsure{qui centralise} $\unsure{\tau}$)}, et…`; TeX line 2 | `qui centralise` | — | medium |
| 145 | 24 | Near `…\inserted{(\unsure{qui centralise} $\unsure{\tau}$)}, et par $E$ l'exten…`; TeX line 2 | `\tau` | — | medium |
| 145 | 24 | Near `\Gamma\cap\deleted{\unsure{\mathfrak S_3}}\Gamma_{\unsure{0,3}}&…`; TeX line 5 | `\mathfrak S_3` | — | medium |
| 145 | 24 | Near `…eted{\unsure{\mathfrak S_3}}\Gamma_{\unsure{0,3}}&=\{1,\tau\}\\`; TeX line 5 | `0,3` | — | medium |
| 145 | 24 | Near `\Gamma\cap\unsure{\mathfrak S_3\|\mathcal S_3}&=\{1\}.`; TeX line 6 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 24 | Near `\unsure{\mathfrak S_3\|\mathcal S_3}\times\widehat{\widehat…`; TeX line 13 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 24 | Near `…t\Gamma}\arrow[r,phantom,"\supset"]&\unsure{\mathfrak S_3\|\mathcal S_3}\times\Gamma&`; TeX line 14 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 24 | Near `…kappa_0(\hat{\mathbb Z}))$. Un $u\in\unsure{\hat{\mathcal E}\|\widehat{\widehat{\mathcal E}}}$ est \inserted{pour êt…`; TeX line 18 | `\hat{\mathcal E}` | `\widehat{\widehat{\mathcal E}}` | low |
| 145 | 24 | Near `…quad u(l_i)=\operatorname{int}(g_i^{\unsure{\deleted{-1}\|u}})l_i^p`; TeX line 28 | `\deleted{-1}` | `u` | low |
| 145 | 24 | Near `…\qquad(\operatorname{int}(g_\infty^{\unsure{\deleted{-1}\|u}})l_\infty^p)`; TeX line 32 | `\deleted{-1}` | `u` | low |
| 145 | 24 | Near `(\operatorname{int}g_1^{\unsure{\deleted{-1}\|u}}\cdot l_1^p)`; TeX line 33 | `\deleted{-1}` | `u` | low |
| 145 | 24 | Near `(\operatorname{int}(g_0^{\unsure{\deleted{-1}\|u}})l_0^p)=1`; TeX line 34 | `\deleted{-1}` | `u` | low |
| 145 | 25 | Near `est unique, et $g_i$ défini \unsure{à} multiplication à gauch…`; TeX line 3 | `à` | — | medium |
| 145 | 25 | Near `…=v(\operatorname{int}(g_i^{\deleted{\unsure{-1}}})l_i^p)`; TeX line 7 | `-1` | — | medium |
| 145 | 25 | Near `=\operatorname{int}(v(g_i^{\deleted{\unsure{-1}}}))v(l_i)^p`; TeX line 8 | `-1` | — | medium |
| 145 | 25 | Near `…i)=\operatorname{int}(h_i^{\deleted{\unsure{-1}}})l_i^q`; TeX line 12 | `-1` | — | medium |
| 145 | 25 | Near `…^p=\operatorname{int}(h_i^{\deleted{\unsure{-1}}})l_i^{pq}`; TeX line 13 | `-1` | — | medium |
| 145 | 25 | Near `\overbrace{v(g_i^{\deleted{\unsure{-1}}})h_i^{\deleted{\unsur…`; TeX line 18 | `-1` | — | medium |
| 145 | 25 | Near `…deleted{\unsure{-1}}})h_i^{\deleted{\unsure{-1}}}}^{\deleted{\unsure{(…`; TeX line 18 | `-1` | — | medium |
| 145 | 25 | Near `…^{\deleted{\unsure{-1}}}}^{\deleted{\unsure{(h_i v(g_i))^{-1}}}}`; TeX line 18 | `(h_i v(g_i))^{-1}` | — | medium |
| 145 | 25 | Near `…athbb Z}^{\{0,1,\infty\}}$ \deleted{\unsure{définie par le groupe}} \unsure{formé} des \d…`; TeX line 21 | `définie par le groupe` | — | medium |
| 145 | 25 | Near `…ted{\unsure{définie par le groupe}} \unsure{formé} des \deleted{couples}…`; TeX line 21 | `formé` | — | medium |
| 145 | 25 | Near `…fonctions à valeurs dans $\deleted{\unsure{\mathcal E}}\hat\pi$`; TeX line 21 | `\mathcal E` | — | medium |
| 145 | 25 | Near `=\deleted{\unsure{\tilde v(\tilde u_i(\tilde u))\cdot\gamma_i(\tilde v)}}`; TeX line 28 | `\tilde v(\tilde u_i(\tilde u))\cdot\gamma_i(\tilde v)` | — | medium |
| 145 | 25 | Near `\inserted{\deleted{\unsure{\gamma_i(\tilde v)\cdot v(\gamma_i(\tilde u))}}`; TeX line 29 | `\gamma_i(\tilde v)\cdot v(\gamma_i(\tilde u))` | — | medium |
| 145 | 25 | Near `\unsure{\tilde v(\gamma_i(\tilde u)\gamma_i(\tilde v)\|\tilde v(\gamma_i(\tilde u))\gamma_i(\tilde v)}}`; TeX line 30 | `\tilde v(\gamma_i(\tilde u)\gamma_i(\tilde v)` | `\tilde v(\gamma_i(\tilde u))\gamma_i(\tilde v)` | low |
| 145 | 25 | Near `…n 1-cocycle sur le groupe \deleted{$\unsure{\widehat{\widehat{\mathcal E}}^!}$}\inserted{$S\widehat{…`; TeX line 32 | `\widehat{\widehat{\mathcal E}}^!` | — | medium |
| 145 | 25 | Near `…} à valeurs dans le groupe \deleted{\unsure{produit du groupe}}\inserted{opposé au gr…`; TeX line 32 | `produit du groupe` | — | medium |
| 145 | 25 | Near `\simeq\hat\pi\times\unsure{(\hat{\mathbb Z})^{\{0,1,\infty\}}\|(\hat{\mathbb Z})^3}`; TeX line 42 | `(\hat{\mathbb Z})^{\{0,1,\infty\}}` | `(\hat{\mathbb Z})^3` | low |
| 145 | 26 | Near `…t{de}}\quad p=1,\quad(g_i)=\deleted{\unsure{(l_i^{\alpha_i})}}\deleted{\unsure{(l_i^…`; TeX line 4 | `(l_i^{\alpha_i})` | — | medium |
| 145 | 26 | Near `…{\unsure{(l_i^{\alpha_i})}}\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}(gl_i^{\alpha_i})`; TeX line 4 | `(l_i^{\alpha_i}g^{-1})` | — | medium |
| 145 | 26 | Near `…ehat{\mathcal E}}^!)$ sur $\deleted{\unsure{u}}\tilde u\in S\widehat{…`; TeX line 6 | `u` | — | medium |
| 145 | 26 | Near `…dehat{\mathcal E}}^!$, par \deleted{\unsure{leurs}} conjugaison, et en pa…`; TeX line 6 | `leurs` | — | medium |
| 145 | 26 | Near `…r de $\rho$. On trouve que \deleted{\unsure{$p$ (bien sûr)}} les $\gamma_i$ sont ′…`; TeX line 6 | `$p$ (bien sûr)` | — | medium |
| 145 | 26 | Near `…ma_i(\rho\tilde u\rho^{-1})=\gamma_{\unsure{i+1\|i-1}}(\unsure{\bar u\|\tilde…`; TeX line 8 | `i+1` | `i-1` | low |
| 145 | 26 | Near `…rho^{-1})=\gamma_{\unsure{i+1\|i-1}}(\unsure{\bar u\|\tilde u})`; TeX line 8 | `\bar u` | `\tilde u` | low |
| 145 | 26 | Near `…l y a lieu d'introduire un groupe $S\unsure{\hat{\mathcal E}\|\widehat{\widehat{\mathcal E}}}$ extension de $\mathca…`; TeX line 11 | `\hat{\mathcal E}` | `\widehat{\widehat{\mathcal E}}` | low |
| 145 | 26 | Near `…infty\}}$) et d'introduire \deleted{\unsure{des}} des relèvements des $…`; TeX line 11 | `des` | — | medium |
| 145 | 26 | Near `…sigma_i,\rho$ par des éléments de $S\unsure{\hat{\mathcal E}\|\widehat{\widehat{\mathcal E}}}$\ldots}`; TeX line 11 | `\hat{\mathcal E}` | `\widehat{\widehat{\mathcal E}}` | low |
| 145 | 27 | Near `…de $\Gamma=\Gamma_{0,3}=\underbrace{\unsure{\mathfrak S_{\{0,1,\infty\}}\|\mathcal S_{\{0,1,\infty\}}}}_{\unsure{\mathfrak S_…`; TeX line 3 | `\mathfrak S_{\{0,1,\infty\}}` | `\mathcal S_{\{0,1,\infty\}}` | low |
| 145 | 27 | Near `…y\}}\|\mathcal S_{\{0,1,\infty\}}}}_{\unsure{\mathfrak S_3\|\mathcal S_3}}\times\mathbb Z/2\math…`; TeX line 3 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 27 | Near `Les classes de conjugaison \deleted{\unsure{au dessus des}} de scindages partiels…`; TeX line 9 | `au dessus des` | — | medium |
| 145 | 27 | Near `…des ens. d'invariants de $\deleted{\unsure{\dot\rho}}\tau,\dot\sigma_0\tau,…`; TeX line 9 | `\dot\rho` | — | medium |
| 145 | 27 | Near `…rdre $6$, \inserted{savoir $\varphi(\unsure{\mathfrak S_3\|\mathcal S_3})$} formé de $1,\dot\rh…`; TeX line 9 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 27 | Near `…ndant \inserted{à $P$} (de $\varphi(\unsure{\mathfrak S_3\|\mathcal S_3})$), on trouve des relè…`; TeX line 9 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 27 | Near `…$\bar P$, s'obtiennent en \deleted{\unsure{conj.}} prenant un élémt de $…`; TeX line 9 | `conj.` | — | medium |
| 145 | 27 | Near `…t un élémt de $\mathcal E$ \deleted{\unsure{qui}} qui soit au dessus d'…`; TeX line 9 | `qui` | — | medium |
| 145 | 27 | Near `…ent. On peut donc prendre \deleted{$\unsure{\sigma_0,\tau}$} un des éléments $\si…`; TeX line 9 | `\sigma_0,\tau` | — | medium |
| 145 | 27 | Near `…roduits des précédents par \deleted{\unsure{$\tau$}} $\rho$ ou $\rho^2$\ld…`; TeX line 9 | `$\tau$` | — | medium |
| 145 | 27 | Near `\unsure{Le\|Les} \inserted{seul} pt fix…`; TeX line 11 | `Le` | `Les` | low |
| 145 | 28 | Near `…cle opposé à $0$; ce qui définit un \unsure{isom} du rev. universel de $…`; TeX line 2 | `isom` | — | medium |
| 145 | 28 | Near `…de structure sur $\tilde U\deleted{\unsure{_P}}(P)$, donc il s'envoie…`; TeX line 2 | `_P` | — | medium |
| 145 | 28 | Near `…iels sur les ss-groupes de \deleted{\unsure{conj.}} stabilité $\Gamma_{-1…`; TeX line 8 | `conj.` | — | medium |
| 145 | 28 | Near `\deleted{\unsure{\Gamma}}\quad 2=0',\quad -1=1'…`; TeX line 10 | `\Gamma` | — | medium |
| 145 | 28 | Near `…\{\dot\sigma_\infty,\tau\}$, qui se \unsure{remontent} resp. en $\sigma_0$ et…`; TeX line 12 | `remontent` | — | medium |
| 145 | 28 | Near `…t} resp. en $\sigma_0$ et $\tau_0$, \unsure{ou} $\sigma_1$ et $\tau_1$…`; TeX line 12 | `ou` | — | medium |
| 145 | 29 | Near `Il faudrait quand-$\unsure{\bar m\|=}$ donner aussi une desc…`; TeX line 13 | `\bar m` | `=` | low |
| 145 | 29 | Near `…rtant d'un syst. de gén. de $\Gamma=\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$, qu'…`; TeX line 13 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 29 | Near `\unsure{\rho'\|\dot\rho'}=\rho\tau,\quad\deleted…`; TeX line 16 | `\rho'` | `\dot\rho'` | low |
| 145 | 29 | Near `…'\|\dot\rho'}=\rho\tau,\quad\deleted{\unsure{\tau}}\underset{\substack{\V…`; TeX line 16 | `\tau` | — | medium |
| 145 | 29 | Near `…gma}_\infty\widetilde{\dot\sigma}_0=\unsure{{\rho'}^{\deleted{-1}2}\|\dot\rho^{-2}}\\`; TeX line 23 | `{\rho'}^{\deleted{-1}2}` | `\dot\rho^{-2}` | low |
| 145 | 30 | Near `\deleted{qui décrivent $\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$, on…`; TeX line 2 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 30 | Near `\unsure{sont} conséquences des relat…`; TeX line 32 | `sont` | — | medium |
| 145 | 30 | Near `l_0=\tau_\infty\tau_1,\quad\deleted{\unsure{l_1=\tau_0\tau_\infty}},\\`; TeX line 37 | `l_1=\tau_0\tau_\infty` | — | medium |
| 145 | 30 | Near `l_1=\tau_0\deleted{\unsure{l_\infty=}}\tau_\infty\\`; TeX line 38 | `l_\infty=` | — | medium |
| 145 | 30 | Near `\margin{\deleted{\unsure{Ceci}} Ceci \unsure{implique…`; TeX line 43 | `Ceci` | — | medium |
| 145 | 30 | Near `…margin{\deleted{\unsure{Ceci}} Ceci \unsure{implique} que $\tau_0,\tau_1,\ta…`; TeX line 43 | `implique` | — | medium |
| 145 | 30 | Near `…ue} que $\tau_0,\tau_1,\tau_\infty$ \unsure{conjuguent\|engendrent} \unsure{ss-groupe enge…`; TeX line 43 | `conjuguent` | `engendrent` | low |
| 145 | 30 | Near `…fty$ \unsure{conjuguent\|engendrent} \unsure{ss-groupe engendré} par $l_0,l_1,l_\infty$…`; TeX line 43 | `ss-groupe engendré` | — | medium |
| 145 | 30 | Near `…_0,\tau_1,\tau_\infty$ ??, \deleted{\unsure{et pas plus}}\inserted{par l'une de…`; TeX line 45 | `et pas plus` | — | medium |
| 145 | 31 | Near `\unsure{\text{i)}\|\text{a)}}\quad&\sigma_0^2=\tau_0…`; TeX line 6 | `\text{i)}` | `\text{a)}` | low |
| 145 | 31 | Near `\unsure{\text{ii)}\|\text{b)}}\quad&\rho^3=1\\`; TeX line 7 | `\text{ii)}` | `\text{b)}` | low |
| 145 | 31 | Near `\margin{\deleted{\unsure{i.e.}} ou encore $\deleted{\…`; TeX line 14 | `i.e.` | — | medium |
| 145 | 31 | Near `…e suite (en en passant au quotient $\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2$, ell…`; TeX line 18 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 33 | Near `\unsure{Par\|Pour} le calcul, il s'explic…`; TeX line 5 | `Par` | `Pour` | low |
| 145 | 33 | Near `…rotatebox{90}{$\in$}}{p}},\underset{\unsure{\mathfrak S_3\|\mathcal S_3}}{\underset{\rotatebox{…`; TeX line 7 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 33 | Near `…ma(1)}^p)\cdot\operatorname{int}(g_{\unsure{0\|\infty}})\unsure{(}l_{\sigma(\…`; TeX line 11 | `0` | `\infty` | low |
| 145 | 33 | Near `…atorname{int}(g_{\unsure{0\|\infty}})\unsure{(}l_{\sigma(\unsure{0\|\in…`; TeX line 11 | `(` | — | medium |
| 145 | 33 | Near `…sure{0\|\infty}})\unsure{(}l_{\sigma(\unsure{0\|\infty})}^p)=1`; TeX line 11 | `0` | `\infty` | low |
| 145 | 33 | Near `…orphisme $u$ défini par ce \deleted{\unsure{morph.}} système est`; TeX line 13 | `morph.` | — | medium |
| 145 | 33 | Near `u(l_0)&\unsure{\mapsto\|=}\operatorname{int}(g_0)…`; TeX line 16 | `\mapsto` | `=` | low |
| 145 | 33 | Near `\margin{On retrouve que \unsure{(4)\|(p)} est surjectif, et a co…`; TeX line 37 | `(4)` | `(p)` | low |
| 145 | 33 | Near `…(1)},u(g'_\infty)g_{\sigma'(\infty)}\unsure{)}`; TeX line 40 | `)` | — | medium |
| 145 | 34 | Near `…_0,g_1,g_\infty)=(p,\sigma,\deleted{\unsure{\operatorname{int}}}gg_0l_{\unsure{\sigma0…`; TeX line 6 | `\operatorname{int}` | — | medium |
| 145 | 34 | Near `…{\unsure{\operatorname{int}}}gg_0l_{\unsure{\sigma0\|\sigma(0)}}^{\alpha_{\sigma(0)}},…`; TeX line 6 | `\sigma0` | `\sigma(0)` | low |
| 145 | 34 | Near `…gg_\infty l_{\sigma\infty}^{\alpha_{\unsure{\sigma(\infty)}}}\unsure{)}`; TeX line 6 | `\sigma(\infty)` | — | medium |
| 145 | 34 | Near `…}^{\alpha_{\unsure{\sigma(\infty)}}}\unsure{)}`; TeX line 6 | `)` | — | medium |
| 145 | 34 | Near `…t, et ne dépend que de $u$ \deleted{\unsure{et}}:`; TeX line 12 | `et` | — | medium |
| 145 | 34 | Near `…t, sur le manque d'explicitation du \unsure{2ième\|2ème} mb de cette formule, p…`; TeX line 18 | `2ième` | `2ème` | low |
| 145 | 35 | Near `…ubstack{\Vert\\\hat\Gamma}}{\Gamma}=\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z/2\subse…`; TeX line 4 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 35 | Near `On va regarder les éléments $\unsure{\rho}\deleted{\unsure{\tau}}…`; TeX line 6 | `\rho` | — | medium |
| 145 | 35 | Near `…les éléments $\unsure{\rho}\deleted{\unsure{\tau}},\dot\sigma_0,\sigma_1…`; TeX line 6 | `\tau` | — | medium |
| 145 | 35 | Near `…at{\widehat{\mathcal E}}$, \deleted{\unsure{extérieurs}} (NB. ils sont $\unsur…`; TeX line 6 | `extérieurs` | — | medium |
| 145 | 35 | Near `…\unsure{extérieurs}} (NB. ils sont $\unsure{\bar m\|=}$ dans $\mathcal E$) et…`; TeX line 6 | `\bar m` | `=` | low |
| 145 | 35 | Near `…widehat{\widehat{\mathcal E}}$ (et $\unsure{\bar m\|=}$, en $S\mathcal E$). E…`; TeX line 6 | `\bar m` | `=` | low |
| 145 | 35 | Near `…eratorname{sg}(\sigma))\mid\sigma\in\unsure{\mathfrak S_3\|\mathcal S_3}\}$ dans $\mathcal E$,…`; TeX line 6 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 35 | Near `…remonter à $S\mathcal E$ --- et de $\unsure{\bar m\|=}$ pour $\dot\sigma_0\ma…`; TeX line 6 | `\bar m` | `=` | low |
| 145 | 35 | Near `…ans $\Gamma$ (etc, par conjugaison, \unsure{idem} pour $1,\infty$). On t…`; TeX line 6 | `idem` | — | medium |
| 145 | 36 | Near `(évident sur (8)), qui \deleted{\unsure{se définit}}\inserted{peut se décr…`; TeX line 2 | `se définit` | — | medium |
| 145 | 36 | Near `…$(p\in\hat{\mathbb Z}^*,\ \sigma\in\unsure{\mathfrak S_3\|\mathcal S_3})$ tels que l'on ait`; TeX line 2 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 36 | Near `…e les} i.e. l'ens des $(p,\sigma)$ (\unsure{abstrayant\|satisfaisant} la condition (13)) n'e…`; TeX line 6 | `abstrayant` | `satisfaisant` | low |
| 145 | 36 | Near `…ion (13)) n'est autre que $\deleted{\unsure{\mathbb Z}}\inserted{\{\pm1\}}\ti…`; TeX line 6 | `\mathbb Z` | — | medium |
| 145 | 36 | Near `…\mathbb Z}}\inserted{\{\pm1\}}\times\unsure{\mathfrak S_3\|\mathcal S_3}\simeq\unsure{\mathfrak…`; TeX line 6 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 36 | Near `…re{\mathfrak S_3\|\mathcal S_3}\simeq\unsure{\mathfrak S_3\|\mathcal S_3}\times\mathbb Z_2\simeq…`; TeX line 6 | `\mathfrak S_3` | `\mathcal S_3` | low |
| 145 | 36 | Near `…al E$} des autom. de $\pi$ \deleted{\unsure{ou} $\unsure{\widehat{\wid…`; TeX line 6 | `ou` | — | medium |
| 145 | 36 | Near `…tom. de $\pi$ \deleted{\unsure{ou} $\unsure{\widehat{\widehat\pi}\|\hat\pi}$} qui \unsure{invarien…`; TeX line 6 | `\widehat{\widehat\pi}` | `\hat\pi` | low |
| 145 | 36 | Near `…widehat{\widehat\pi}\|\hat\pi}$} qui \unsure{invarient} $L_0,L_1,L_\infty$, af…`; TeX line 6 | `invarient` | — | medium |
| 145 | 36 | Near `Sans doute il est vrai que le $\unsure{=\|\bar m}$ résultat est valable…`; TeX line 8 | `=` | `\bar m` | low |
| 145 | 36 | Near `…njuguer par un $\tilde\sigma_i$ --- \unsure{ou} $\sigma\in\Gamma_P$)}…`; TeX line 8 | `ou` | — | medium |
| 145 | 37 | Near `…nt \uline{pas} --- on sait bien que \unsure{les extensions locales\|l'extension locale} de $\Gamma_0^+$ \inser…`; TeX line 3 | `les extensions locales` | `l'extension locale` | low |
| 145 | 37 | Near `…locale} de $\Gamma_0^+$ \inserted{(\unsure{précis})} par $\mathbb Z_0$ (q…`; TeX line 3 | `précis` | — | medium |
| 145 | 37 | Near `…voit donc: a) Pour que $\tilde u=(p,\unsure{\sigma},g_0,g_1,g_\infty)$ com…`; TeX line 12 | `\sigma` | — | medium |
| 145 | 37 | Near `…s. que \deleted{$g_0,g_1,g_\infty$ \unsure{soi}} $\sigma$ commute à $\…`; TeX line 12 | `soi` | — | medium |
| 145 | 37 | Near `…fty=\rho(g_1)=\rho^2(g_0)=\rho^{-1}(\unsure{g_0\|g_\infty})$`; TeX line 16 | `g_0` | `g_\infty` | low |
| 145 | 38 | Near `…e déjà $g_0=\rho g_\infty\ \deleted{\unsure{g_0}}$ dans (17)).`; TeX line 2 | `g_0` | — | medium |
| 145 | 38 | Near `…sigma,g_0)\in\hat{\mathbb Z}^*\times\unsure{\mathfrak S_3^+\|\mathcal S_3^+}\times\hat\pi$ tels que…`; TeX line 4 | `\mathfrak S_3^+` | `\mathcal S_3^+` | low |
| 145 | 38 | Near `…n ait la relation qui correspond à (\unsure{2})`; TeX line 4 | `2` | — | medium |
| 145 | 38 | Near `\deleted{\unsure{On remarque d'abord}}`; TeX line 16 | `On remarque d'abord` | — | medium |
| 145 | 38 | Near `\deleted{\unsure{exprimons} que $\tilde u$ commute…`; TeX line 18 | `exprimons` | — | medium |
