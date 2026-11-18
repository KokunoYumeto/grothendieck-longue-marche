# Notation table and transcription doubts

## Package notation table

This table records the final, pre-context comparison of recurring signs across the package. It is a transcription convention, not an identification of the mathematics with a modern theory. Different visible forms are retained; uncertainties are also marked at their occurrences in the transcription.

| Visible sign or usage | LaTeX transcription | Locations and decision |
|---|---|---|
| Typed inclusion-map glyph | `\iota`, `\iota_a` | 049, 051; short curved iota, distinguished from v and primes. |
| Distribution bases | `\Delta`, `\Lambda` | 049, 051, 053, 055, 057, 059; preserve the two distinct capitals and all multiindices. |
| Typed multiindex N with heavy upright strokes | `\unsure{\mathbf{N}\|\mathbb{N}}` | 049, 053; bold Roman is first reading; a doubled-stroke typeface remains possible. |
| Rounded distribution-order symbol | `\unsure{\nu}` | 051, 053; same glyph read consistently; its nonstandard printed shape remains doubtful. |
| Looped differentiability-class symbol | `\unsure{\omega\|0}` | 055, 057, 059; do not replace it by a class inferred from the argument. |
| Ordinary, prime, and tame fundamental groups | `\pi_1`, `\pi'_1`, `\pi_1^t` | 050–077, 082–094; the prime stroke and the raised t have been compared. No exclamation exponent is confidently present in this package. |
| Raised abbreviation after top | `top$ {}^t$` | 070; raised t, not a prime or an exclamation mark. |
| Picard exponent | `\operatorname{Pic}^\tau`, `\underline{\mathrm{Pic}}^\tau` | 060, 071–077; tau distinguished from tame t, and underlined Pic from plain Pic. |
| Structure-sheaf O with separate lower stroke | `\underline O` | 064, 071–075, 084, 088; the underline is explicit, not silently changed to a script alphabet. |
| Looped script O and F in stratification draft | `\mathcal O`, `\mathcal F` | 087; forms differ from the separately underlined O above. |
| Script module E | `\mathcal E`, `\mathcal E_1`, `\mathcal E_2` | 086; looped module letter retained. |
| Formal-scheme X | `\mathfrak X` | 088, 090, 092, 094; distinguished from ordinary `X` and `X_0`. The overwritten base letters in cohomology are separately doubtful. |
| Plain T versus finite-group Gamma | `T`, `\Gamma` | T in 073 and the normal-bundle notation in 090; Gamma in 063. No confidently identified script T has been converted to Gamma. |
| Projective-space P, retraced/doubled stem | `\unsure{\mathbf P\|P}` | 061, 062, 067; font remains uncertain. Plain, single-stem P is retained in 065, 068. |
| Typed integers with separate underline | `\underline Z` | 093; no blackboard-bold replacement. |
| Heavy handwritten integer symbol | `\mathbf Z`, `\mathbf Z_\ell` | 072, 074, 076, 082, 088; handwritten form distinct from the typed underlined Z. |
| Underlined group/sheaf names | `\underline G`, `\underline{\operatorname{Hom}}`, `\underline{\mathrm{Pic}}` | Retained where visible; ordinary Hom or Pic elsewhere is not underlined by analogy. |
| Frobenius | `F`, `{}_{F^{\unsure{\nu\|1}}}H^1` | 072; left subscript placement retained. |
| Repeated p exponents | `p^{\unsure{\nu\|1}}`, `p^{-\unsure{\nu\|1}}` | 073; every small exponent retains the same nu/one uncertainty. |
| Bars, hats and tildes | `\bar{}`, `\overline{}`, `\widehat{}`, `\widetilde{}` | 065 upper X-prime has a hat/bar alternative; lower X has a bar. Universal-cover tildes and geometric-point bars remain distinct. |
| Inertia letter I, including possible upper stroke | `I_0`, `\overline I_0`, `\overline I'_0` | 088, 092; the extra upper stroke is retained in the displayed occurrences; it may be a pronounced serif, so no uniform algebraic meaning is asserted. |
| A superscript on the Raynaud sheet | `A^{\unsure{\natural\|\sharp}}` | 085; zigzag/accidental-like sign remains uncertain. |
| Headless connectors | `\mathbin{-}` or `\arrow[...,no head]` | Wherever only a shaft is visible; possible arrows receive an in-place alternative, not a silently added head. |
| Empty typed connectors and operators | spacing with no invented sign | 089, 091, 093; absent equals, membership, roots-of-unity, product and arrow glyphs remain absent. |
| Double quotation marks | two backticks and two apostrophes | All ordinary double quotation marks; no replacement by guillemets. Ditto strokes are transcribed separately. |
| Deleted and inserted text | `\deleted{...}`, `\inserted{...}` | Word and symbol identity retained; cancellation does not imply that the mathematical statement has been refuted. |
| Underlining and double underlining | `\uline{...}`, `\uuline{...}` | Visible text emphasis; separate marginal emphasis strokes reproduced in TikZ. |
| Page numbering | `\mspage{...}` only for confidently authorial numbering | Printed typescript numbering is ordinary text. Archive foliation is a comment. Scan 085's handwritten 69 has uncertain attribution and is only a comment. |

## Final in-place doubt register

The following table is generated from the final page files, including doubts inside deletions and diagrams. “Line” is the physical line of the named LaTeX page file, a precise locator rather than a claim about manuscript line numbering; the nearby fragment helps locate it on the scan. Every listed first reading follows the ink, including spellings and headless connectors. “Low” is conservative: it means the word or symbol should be checked against the scan before quotation as secure text, not that the entire surrounding sentence is doubtful. The raw first-pass and audit records in `work/doubts_records.jsonl` are historical working records and may contain readings superseded by this final register.

| File/cote | Scan | Approximate location | First reading | Alternative(s) | Confidence |
|---|---:|---|---|---|---|
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 15: `Y)$ a une base $\{\Lambda^\alpha\}_{\alpha\in\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m}$ caractérisée par :` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 18: `\qquad \alpha,\alpha'\in\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 20: `)$ admet une base $\{\Delta^\beta\}_{\beta\in\unsure{\mathbf{N}&#124;\mathbb{N}}_r^n}$ définie par :` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 23: `\qquad \beta,\beta'\in\unsure{\mathbf{N}&#124;\mathbb{N}}_r^n.` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 25: `Nous noterons $0$ l'élément nul de $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^{n-m}$ ; on a alors $\iota_a(\Lambda^\alp` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 25: `Delta^{(\alpha,0)}$ pour tout $\alpha$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m$ et par conséquent, $\iota_a$ est injec` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 27: `angle=0$ pour tout multiindice $\beta$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^n$ pour lequel il existe $i$ avec $m<i\le` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan049.tex | 049 | TeX line 27: `ue si $\beta=(\alpha,0)$ pour $\alpha$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m$ convenable. De la formule $\mu=\sum_\b` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 4: `Soit $Y_1$ le \unsure{normalisé&#124;localisé} de $Y$ en $y$,` | `normalisé` | localisé | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 5: `\inserted{\unsure{pour des points étales}}` | `pour des points étales` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 6: `\deleted{\unsure{Alors}}` | `Alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 7: `\inserted{en \unsure{le} $y\in Y$.}` | `le` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `\inserted{\unsure{Quant à} \deleted{\unsure{localisation}} \unsure{en ` | `Quant à` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `\inserted{\unsure{Quant à} \deleted{\unsure{localisation}} \unsure{en un} \deleted{\unsure{V}} \unsur` | `localisation` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `ure{Quant à} \deleted{\unsure{localisation}} \unsure{en un} \deleted{\unsure{V}} \unsure{voisinage de l` | `en un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `nsure{localisation}} \unsure{en un} \deleted{\unsure{V}} \unsure{voisinage de la fibre} \deleted{\u` | `V` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `sation}} \unsure{en un} \deleted{\unsure{V}} \unsure{voisinage de la fibre} \deleted{\unsure{spéciale}}}` | `voisinage de la fibre` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 8: `{V}} \unsure{voisinage de la fibre} \deleted{\unsure{spéciale}}}` | `spéciale` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 9: `\deleted{$X$ \unsure{étant} \inserted{\unsure{en} $X_y$} \unsure{le mêm` | `étant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 9: `\deleted{$X$ \unsure{étant} \inserted{\unsure{en} $X_y$} \unsure{le même sur} $Y$ \unsure{alo` | `en` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 9: ` \unsure{étant} \inserted{\unsure{en} $X_y$} \unsure{le même sur} $Y$ \unsure{alors} $X_1=X\times_Y Y_1$ \uns` | `le même sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 9: `{\unsure{en} $X_y$} \unsure{le même sur} $Y$ \unsure{alors} $X_1=X\times_Y Y_1$ \unsure{le est sur}}` | `alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 9: ` sur} $Y$ \unsure{alors} $X_1=X\times_Y Y_1$ \unsure{le est sur}}` | `le est sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 10: `\inserted{\unsure{on peut supposer} $X_y$ \deleted{\unsure{fibre spéciale}} \un` | `on peut supposer` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 10: `ted{\unsure{on peut supposer} $X_y$ \deleted{\unsure{fibre spéciale}} \unsure{connexe}. Donc, il \unsure{nous es` | `fibre spéciale` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 10: `ser} $X_y$ \deleted{\unsure{fibre spéciale}} \unsure{connexe}. Donc, il \unsure{nous est}}` | `connexe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 10: `{fibre spéciale}} \unsure{connexe}. Donc, il \unsure{nous est}}` | `nous est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 11: `\deleted{$Y_1$, $X_1$ \illegible{2}, \unsure{donc} \illegible{3}}` | `Physically unreadable: estimated 2 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 11: `\deleted{$Y_1$, $X_1$ \illegible{2}, \unsure{donc} \illegible{3}}` | `donc` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 11: `ed{$Y_1$, $X_1$ \illegible{2}, \unsure{donc} \illegible{3}}` | `Physically unreadable: estimated 3 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 12: `\inserted{\unsure{au cas de} $X_1=X\times_Y Y_1$, \unsure{notre} $y$ \un` | `au cas de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 12: `rted{\unsure{au cas de} $X_1=X\times_Y Y_1$, \unsure{notre} $y$ \unsure{induit un morphisme dans}}` | `notre` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 12: ` de} $X_1=X\times_Y Y_1$, \unsure{notre} $y$ \unsure{induit un morphisme dans}}` | `induit un morphisme dans` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 13: `\unsure{alors de} $X_1$, \unsure{et}` | `alors de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 13: `\unsure{alors de} $X_1$, \unsure{et}` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 14: `\inserted{\unsure{le même}}` | `le même` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 15: `\unsure{considérons sur la fibre} géométrique \unsure{en} $Z_y$, il s'\unsure` | `considérons sur la fibre` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 15: `unsure{considérons sur la fibre} géométrique \unsure{en} $Z_y$, il s'\unsure{ensuit}` | `en` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 15: `a fibre} géométrique \unsure{en} $Z_y$, il s'\unsure{ensuit}` | `ensuit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 16: `\inserted{un $X$-\unsure{morphisme} $X_1\leftarrow Z$ \unsure{qui}}` | `morphisme` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 16: `{un $X$-\unsure{morphisme} $X_1\leftarrow Z$ \unsure{qui}}` | `qui` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 17: `\unsure{fait un isom sur la fibre de} $(X_1)_y$.` | `fait un isom sur la fibre de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 26: `\deleted{(\unsure{car par} \illegible{1} $Z$ \unsure{de} \illegible{1}` | `car par` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 26: `\deleted{(\unsure{car par} \illegible{1} $Z$ \unsure{de} \illegible{1}, $X_1$ \unsur` | `Physically unreadable: estimated 1 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 26: `\deleted{(\unsure{car par} \illegible{1} $Z$ \unsure{de} \illegible{1}, $X_1$ \unsure{est étale}}` | `de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 26: `nsure{car par} \illegible{1} $Z$ \unsure{de} \illegible{1}, $X_1$ \unsure{est étale}}` | `Physically unreadable: estimated 1 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 26: `ible{1} $Z$ \unsure{de} \illegible{1}, $X_1$ \unsure{est étale}}` | `est étale` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 27: `\inserted{j'\unsure{ajoute que} $X_1$ \unsure{est étale sur} $Y$ \unsure{su` | `ajoute que` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 27: `\inserted{j'\unsure{ajoute que} $X_1$ \unsure{est étale sur} $Y$ \unsure{sur la fibre}}` | `est étale sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 27: `ajoute que} $X_1$ \unsure{est étale sur} $Y$ \unsure{sur la fibre}}` | `sur la fibre` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 28: `\deleted{\unsure{sur} $X$, $Y_1\to$\unsure{étale} \unsure{sur} $Y` | `sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 28: `\deleted{\unsure{sur} $X$, $Y_1\to$\unsure{étale} \unsure{sur} $Y$.}` | `étale` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 28: `ted{\unsure{sur} $X$, $Y_1\to$\unsure{étale} \unsure{sur} $Y$.}` | `sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 29: `\inserted{\unsure{en} $Y_1$, \unsure{comme pointé}.}` | `en` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 29: `\inserted{\unsure{en} $Y_1$, \unsure{comme pointé}.}` | `comme pointé` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 30: `Donc \unsure{on a}` | `on a` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 32: `Z\simeq X\times_Y Y_1,\quad Y_1\ \text{\unsure{revêtement} fini étale de }Y.` | `revêtement` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 35: `Par \unsure{suite} (\unsure{comme on a prouvé}), \deleted{\uns` | `suite` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 35: `Par \unsure{suite} (\unsure{comme on a prouvé}), \deleted{\unsure{$X_1$ est}}` | `comme on a prouvé` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 35: `uite} (\unsure{comme on a prouvé}), \deleted{\unsure{$X_1$ est}}` | `$X_1$ est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 36: `$X_1$ est étale sur $X$, \unsure{partout}, et \deleted{\unsure{les morphismes}}` | `partout` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 36: `étale sur $X$, \unsure{partout}, et \deleted{\unsure{les morphismes}}` | `les morphismes` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 37: `\inserted{des \unsure{considérations}}` | `considérations` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 38: `de \unsure{profondeur} nous donnent un $X$-isom` | `profondeur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 44: `\uline{NB} \unsure{Ceci prouve} plus qu'on n'avait annoncé, savoir ceci : u` | `Ceci prouve` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 45: `\margin{\deleted{\unsure{R}}}` | `R` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 50: `\pi_1(X_{\bar y},\unsure{\xi}) \arrow[r,dash] &` | `\xi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 51: `\pi_1(X,\unsure{\xi}) \arrow[r] &` | `\xi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 52: `\pi_1(Y,\unsure{\eta}) \arrow[r] & 0` | `\eta` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 55: `\deleted{\unsure{Cela}}` | `Cela` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 56: `généralise (\unsure{en dehors} l'hyp. noethérienne)` | `en dehors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 57: `es résultats de SGA X, où on prend une fibre \unsure{pas}%` | `pas` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 58: `\inserted{\uline{\unsure{néc&#124;ici}}}%` | `néc` | ici | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 59: `\uline{générique} (en revanche, il y faut \unsure{je crois} que $f$ \unsure{soit} propre \ldots).` | `je crois` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan050.tex | 050 | TeX line 59: `evanche, il y faut \unsure{je crois} que $f$ \unsure{soit} propre \ldots).` | `soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan051.tex | 051 | TeX line 37: `varphi$ de $Y$ dans $X$, $\mu$ dans $D(X)$, $\unsure{\nu}$ dans $D(Y)$, $f$ dans $C^r(X)$ et $g$ dans` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan051.tex | 051 | TeX line 39: `(60)\qquad (f.\mu)\times(g.\unsure{\nu})=(f\times g).(\mu\times\unsure{\nu})` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan051.tex | 051 | TeX line 39: `\times(g.\unsure{\nu})=(f\times g).(\mu\times\unsure{\nu})` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan051.tex | 051 | TeX line 42: `(61)\qquad \varphi_*((f\circ\varphi).\unsure{\nu})=f.\varphi_*(\unsure{\nu}).` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan051.tex | 051 | TeX line 42: `_*((f\circ\varphi).\unsure{\nu})=f.\varphi_*(\unsure{\nu}).` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 2: `\mspage{\unsure{III&#124;II}}` | `III` | II | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 7: `\unsure{SGA&#124;§ A} au début` | `SGA` | § A | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 9: `\uline{Lemme 3} $X$ schéma connexe \deleted{\unsure{loc}} noeth.,` | `loc` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 13: `\inserted{Considérons l'\deleted{\unsure{application}}}` | `application` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 14: `\deleted{Alors \unsure{pour tt}}` | `pour tt` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 20: `\unsure{Théorie du recollement} des faisceaux étales, en utilisant lemme 2 ` | `Théorie du recollement` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 27: `\deleted{\unsure{Corollaire}}` | `Corollaire` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 28: `\deleted{\unsure{Proposition}}` | `Proposition` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan052.tex | 052 | TeX line 30: `$S$ \deleted{\unsure{X}} schéma noeth. univ. japonais,` | `X` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 10: `(31)\qquad \iota(\mu\otimes\unsure{\nu})(f,g)=\langle\mu,f\rangle\langle\unsure{\nu` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 10: `\unsure{\nu})(f,g)=\langle\mu,f\rangle\langle\unsure{\nu},g\rangle.` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 17: `\uline{engendré par les éléments} $\mu\otimes\unsure{\nu}$ \uline{avec} $v(\mu)+v(\unsure{\nu})\leq r` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 17: `u\otimes\unsure{\nu}$ \uline{avec} $v(\mu)+v(\unsure{\nu})\leq r$. \uline{En particulier, si} $r$ \ul` | `\nu` | No secure alternative; the first reading remains doubtful. | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 26: `pour $\alpha$ et $\alpha'$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^n$ et $\beta$ et $\beta'$ dans $\unsure{\` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 26: `mathbb{N}}_r^n$ et $\beta$ et $\beta'$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m$. Par conséquent, le produit tensoriel ` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 26: `ha\otimes\Delta_b^\beta$ pour $\alpha$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^n$ et $\beta$ dans $\unsure{\mathbf{N}&#124;\m` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan053.tex | 053 | TeX line 26: `\mathbf{N}&#124;\mathbb{N}}_r^n$ et $\beta$ dans $\unsure{\mathbf{N}&#124;\mathbb{N}}_r^m$.` | `\mathbf{N}` | \mathbb{N} | medium |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 6: `(ii) Pour tt sous-schéma \deleted{\unsure{affine}} normal` | `affine` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 7: `\inserted{\unsure{intègre affine}}` | `intègre affine` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 8: `\deleted{\unsure{de }$S$}` | `de ` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 9: `$S_0$ de $S$, \deleted{\unsure{et}} tt \unsure{rev.} fini étale` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 9: `$S_0$ de $S$, \deleted{\unsure{et}} tt \unsure{rev.} fini étale` | `rev.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 10: `S'$, à fibres géom. connexes non vides, $H^1(\unsure{X},G)$ est fini.` | `X` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 12: `n ouvert non vide $U$ de $S'$ tel que $H^1(X&#124;\unsure{U'&#124;U},G)$ \unsure{soit} fini.` | `U'` | U | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 12: `$U$ de $S'$ tel que $H^1(X&#124;\unsure{U'&#124;U},G)$ \unsure{soit} fini.` | `soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 21: `b) Pour tout \deleted{\unsure{$S$}} \deleted{\unsure{un}} schéma affine normal` | `$S$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 21: `b) Pour tout \deleted{\unsure{$S$}} \deleted{\unsure{un}} schéma affine normal intègre $S'$ \deleted` | `un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 24: `\deleted{\illegible{1}}` | `Physically unreadable: estimated 1 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan054.tex | 054 | TeX line 33: `résulte aussitôt de lemme 3. Pour prouver qu'\unsure{ils} sont entrainés par (iv), on doit utiliser e` | `ils` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan055.tex | 055 | TeX line 28: `'isomorphisme $u_a$ précédent, lorsque $r\neq\unsure{\omega&#124;0}$.` | `\omega` | 0 | low |
| 29; MPL_29_049-094_29_scan055.tex | 055 | TeX line 30: `\uline{Remarque}.-- Lorsque $r=\unsure{\omega&#124;0}$, l'espace $T_a(X)$ n'a pas été défini préc` | `\omega` | 0 | low |
| 29; MPL_29_049-094_29_scan056.tex | 056 | TeX line 5: `\deleted{Alors \unsure{on}}` | `on` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan056.tex | 056 | TeX line 9: `G$ est commutatif, il suffit de faire $H=G$ (\unsure{c'est} une condition \unsure{néce&#124;nécessaire} et s` | `c'est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan056.tex | 056 | TeX line 9: `de faire $H=G$ (\unsure{c'est} une condition \unsure{néce&#124;nécessaire} et suffisante).` | `néce` | nécessaire | low |
| 29; MPL_29_049-094_29_scan056.tex | 056 | TeX line 15: `(ii) \deleted{\unsure{Pour}} Idem avec $X$ revêt \deleted{fini} étale i` | `Pour` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan057.tex | 057 | TeX line 33: ` variété} $X$ \uline{de classe} $C^r$ $(r\neq\unsure{\omega&#124;0})$, \uline{et} $\bar D_a^1(X)$ \uline{l'espa` | `\omega` | 0 | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 4: `\deleted{\unsure{On est}}` | `On est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 7: `\deleted{\unsure{Utilisant}}` | `Utilisant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 8: `\deleted{\unsure{on a}}` | `on a` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 11: `\deleted{\unsure{admet un morphisme lisse surjectif}}` | `admet un morphisme lisse surjectif` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 13: `\deleted{\unsure{et}}` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 15: `\deleted{\unsure{D'une manière}}` | `D'une manière` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 17: `Si $\dim X\geq2$, on est ramené \deleted{\unsure{au cas}}` | `au cas` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 18: `\inserted{\unsure{par}}` | `par` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 19: `d{lisse} $X\to Y$, $\dim Y<\dim X$, \deleted{\unsure{et}}` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 20: `\unsure{qui est} à fibres géom. connexes non vides, de dim 1` | `qui est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 24: `k$ un corps. On suppose que pour tt \deleted{\unsure{$X$}}` | `$X$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 25: `courbe \inserted{\unsure{alg.}} lisse $X$ sur $k$, le nb de rev. étales de` | `alg.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan058.tex | 058 | TeX line 26: `Alors la $=$ chose est \unsure{vrai&#124;vraie} pour \uline{tt} $X$ de t.f. sur $k$.` | `vrai` | vraie | low |
| 29; MPL_29_049-094_29_scan059.tex | 059 | TeX line 9: ` coordonnées. \uline{Nous supposerons} $r\neq\unsure{\omega&#124;0}$.` | `\omega` | 0 | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 12: `\inserted{\deleted{\unsure{intègre}}\unsure{et réduit}},` | `intègre` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 12: `\inserted{\deleted{\unsure{intègre}}\unsure{et réduit}},` | `et réduit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 21: `\inserted{\unsure{par $\pi'_1(X')$ et \ldots}}` | `par $\pi'_1(X')$ et \ldots` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 22: `(\unsure{car cela se prouve&#124;car cela est} pour les grps profinis,` | `car cela se prouve` | car cela est | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 23: `\unsure{voir $(\varphi)$}). ` | `voir $(\varphi)$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 29: `nous ramène au cas de la \unsure{car.ctéristique&#124;caractéristique} $0$, où on a` | `car.ctéristique` | caractéristique | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 30: `\deleted{\unsure{un}}\deleted{\unsure{le groupe}}` | `un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 30: `\deleted{\unsure{un}}\deleted{\unsure{le groupe}}` | `le groupe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 35: `X^n\longrightarrow \unsure{\mathbf P&#124;P}_k^r` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 37: `et un \unsure{hyperplan} \deleted{\unsure{générique}}` | `hyperplan` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 37: `et un \unsure{hyperplan} \deleted{\unsure{générique}}` | `générique` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 38: `\inserted{\unsure{variété lin gén} $L^{r-n+1}$}, défini sur une` | `variété lin gén` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 41: `C=\deleted{\unsure{\mathbf P_k^r&#124;P_k^r}}X^n\times_{\unsure{\mathbf P&#124;P}_k^r}L^{r-n+` | `\mathbf P_k^r` | P_k^r | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 41: `eted{\unsure{\mathbf P_k^r&#124;P_k^r}}X^n\times_{\unsure{\mathbf P&#124;P}_k^r}L^{r-n+1}` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 50: `\deleted{\unsure{de codim $\geq1$}}` | `de codim $\geq1$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan061.tex | 061 | TeX line 53: `\deleted{\unsure{degré}}` | `degré` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 5: `\deleted{\unsure{Soit} $X,\unsure{E}$ \unsure{un préschéma alg. su` | `Soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 5: `\deleted{\unsure{Soit} $X,\unsure{E}$ \unsure{un préschéma alg. sur}}` | `E` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 5: `\deleted{\unsure{Soit} $X,\unsure{E}$ \unsure{un préschéma alg. sur}}` | `un préschéma alg. sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 7: `\deleted{\unsure{type fini sur $k$}}` | `type fini sur $k$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 8: `$X$ \deleted{complet}\inserted{\unsure{propre sur $k$}},` | `propre sur $k$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 9: `\deleted{\unsure{$X'$}}` | `$X'$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 13: `$\unsure{D'_i&#124;D_i}$ les composantes irréductibles de codim $1$` | `D'_i` | D_i | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 15: `\inserted{$d_i$ le pt gén. de $\unsure{D'_i&#124;D_i}$},` | `D'_i` | D_i | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 18: `X'\arrow[d,"p"'] & \unsure{D'_i}\arrow[l,phantom,"\supset" description]\arro` | `D'_i` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 22: `$Y$ un préschém. \deleted{\unsure{alg.}}` | `alg.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 23: `\inserted{localement \unsure{noethérien}},` | `noethérien` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 26: `\deleted{$\unsure{Y}\times\unsure{U}$}\inserted{$P$},` | `Y` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 26: `\deleted{$\unsure{Y}\times\unsure{U}$}\inserted{$P$},` | `U` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 27: `\deleted{$\unsure{Y_k}$}` | `Y_k` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 31: `(i) $Q\times_P P'$ est \inserted{\uuline{\unsure{géométr.}}}` | `géométr.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 33: `\inserted{$\unsure{D_i&#124;d_i}\times_k k(\eta)$,` | `D_i` | d_i | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 34: `$\eta$ \deleted{\unsure{les points}} les pts gén. des comp. irrédu. de $Y$.}` | `les points` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 35: `\deleted{\unsure{fini.}}` | `fini.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 36: `\deleted{[NB Si $Y$ est \unsure{réduit}, il suffit \unsure{de}]}` | `réduit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 36: `ed{[NB Si $Y$ est \unsure{réduit}, il suffit \unsure{de}]}` | `de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 42: `\deleted{\unsure{Y\times D'}}\,P=Y\times U\arrow[r,hook]\arrow[d]&Y\time` | `Y\times D'` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 46: ` \deleted{pour tt $y'\in Y$, $Q_{y'}$ est un \unsure{rev.}}` | `rev.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 47: `erted{Il existe un rev. étale $Q_0$ \deleted{\unsure{sur}}` | `sur` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 48: `\inserted{d'un voisinage \unsure{de $y$}} et}` | `de $y$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 51: `\deleted{\unsure{Q(P')}\,\unsure{Q_0\times_Y P'}}\quad` | `Q(P')` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 51: `\deleted{\unsure{Q(P')}\,\unsure{Q_0\times_Y P'}}\quad` | `Q_0\times_Y P'` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 54: `\deleted{\unsure{Quid?}\quad\unsure{$U_{\bar k}$ géo.}}` | `Quid?` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 54: `\deleted{\unsure{Quid?}\quad\unsure{$U_{\bar k}$ géo.}}` | `$U_{\bar k}$ géo.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 55: `\inserted{\unsure{$Q_0\times_Y k(y'),\ Q_{y'}$ est}}` | `$Q_0\times_Y k(y'),\ Q_{y'}$ est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 56: `\margin{\unsure{(On sait [inf])}}` | `(On sait [inf])` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 57: `\unsure{qui est VU de même pour tout $y'$}` | `qui est VU de même pour tout $y'$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 58: `\deleted{\unsure{fermé}},` | `fermé` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 59: `\unsure{un rev. trivial de $k(y')$. On peut donc supposer $Y$ de sorte à ses composantes` | `un rev. trivial de $k(y')$. On peut donc supposer $Y$ de sorte à ses composantes irrédu. distinctes.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 64: `\inserted{\unsure{pure&#124;donc}}&#96;&#96;\unsure{birat.elle&#124;biréelle}'' sur les fi` | `pure` | donc | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 64: `\inserted{\unsure{pure&#124;donc}}&#96;&#96;\unsure{birat.elle&#124;biréelle}'' sur les fibres,` | `birat.elle` | biréelle | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 65: `on peut supposer $X$ affine, alors \unsure{fixons} une immersion` | `fixons` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 66: `$X\longrightarrow\unsure{\mathbf P&#124;P}_k^n$.` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 69: `\deleted{\unsure{sur $k$}}\inserted{définie}` | `sur $k$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 70: `\deleted{\illegible{1}}` | `Physically unreadable: estimated 1 word(s)` | No defensible word reading at available image resolution. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 74: `de $\unsure{D_i}$ dans $C$ sont des diviseurs non singuliers` | `D_i` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 75: `\deleted{\unsure{de $D$}}` | `de $D$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 76: `\deleted{\unsure{et non singuliers}}, on en \unsure{est}` | `et non singuliers` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 76: `\deleted{\unsure{et non singuliers}}, on en \unsure{est}` | `est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 79: `Mais alors, ce \unsure{sont les conditions}, actuellement` | `sont les conditions` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 81: `\margin{\unsure{Si on sait}` | `Si on sait` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 82: `$\pi_1(X\times_k Y)\quad \pi_1(X,\unsure{D,x})\nearrow$}` | `D,x` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan062.tex | 062 | TeX line 88: `C\times Y=C_Y\deleted{\unsure{\times X}}\arrow[r]\arrow[d]&Q\arrow[d]\\` | `\times X` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 4: `plication du thme de spécialisation \deleted{\unsure{du groupe}}` | `du groupe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 22: `\uline{Corollaire} \deleted{\unsure{Soit}}` | `Soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 24: `\deleted{\unsure{quelconque}}` | `quelconque` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 28: `\deleted{\unsure{Alors $U$}}` | `Alors $U$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 31: `\deleted{\unsure{$U(k)$}}` | `$U(k)$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 32: `$y$, l'image \unsure{directe&#124;inverse} d'un rev étale d'un tel voisinage.` | `directe` | inverse | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 35: `$Z'$ ($Z''$) des parties fermées, \deleted{\unsure{alors}} écrivons` | `alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 36: `\deleted{\unsure{Soit}}` | `Soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan063.tex | 063 | TeX line 46: `est un \uline{\unsure{isomorphisme}}.` | `isomorphisme` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 14: `\deleted{\unsure{Th}}` | `Th` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 15: `\deleted{\uline{Th} (1.)\quad$\unsure{\pi_1(U)}$` | `\pi_1(U)` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 18: `est \unsure{un groupe de}}` | `un groupe de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 20: `\deleted{\unsure{y sont définis}}` | `y sont définis` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 21: `nt des rev. \uuline{doux} des $\underline O_{\unsure{Y'_{ij}&#124;Y_{ij}}}$,` | `Y'_{ij}` | Y_{ij} | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 26: `\uline{Cor. 1} Soit $X$ \deleted{\unsure{Y}} complet,` | `Y` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 28: `Alors $\pi_1(\unsure{U}\deleted{\unsure{X-Y}})$` | `U` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan064.tex | 064 | TeX line 28: `Alors $\pi_1(\unsure{U}\deleted{\unsure{X-Y}})$` | `X-Y` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan065.tex | 065 | TeX line 12: `\pi_1(\unsure{Z})\arrow[r,no head]&\pi_1(X)\arrow[r,no head]` | `Z` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan065.tex | 065 | TeX line 30: `,phantom,"\subset" description]&\widehat X_0&\unsure{\text{pts réguliers}}` | `\text{pts réguliers}` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan065.tex | 065 | TeX line 45: `ow[r,phantom,"\subset" description]\arrow[d]&\unsure{\widehat X'&#124;\overline X'}\arrow[d]\\` | `\widehat X'` | \overline X' | low |
| 29; MPL_29_049-094_29_scan066.tex | 066 | TeX line 10: `\deleted{\unsure{le complément}}` | `le complément` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan066.tex | 066 | TeX line 26: `\deleted{\unsure{irréductible}}\inserted{intègre},` | `irréductible` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 12: `$X\xrightarrow{f}\unsure{\mathbf P&#124;P}_k^r$ un \uline{morphisme},` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 14: `$\dim f(X)\unsure{=&#124;\geq}n$, soit $1\leq s\leq n-1$, et soit $u$` | `=` | \geq | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 16: `$\underbrace{\unsure{\mathbf P&#124;P}_k^r\times\cdots\times\unsure{\mathbf P&#124;P}_k` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 16: `ce{\unsure{\mathbf P&#124;P}_k^r\times\cdots\times\unsure{\mathbf P&#124;P}_k^r}_{s}$,` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 18: `enfin $L_u$ la variété linéaire de $\unsure{\mathbf P&#124;P}_K^r$ définie par $u$,` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 21: `X_u=X\times_{\unsure{\mathbf P&#124;P}_k^r}L_u=X_K\times_{\unsure{\mathbf P&#124;P}_K^r` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 21: `mes_{\unsure{\mathbf P&#124;P}_k^r}L_u=X_K\times_{\unsure{\mathbf P&#124;P}_K^r}L_u.` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 31: `L_u\arrow[r]&\unsure{\mathbf P&#124;P}_K^r\arrow[r]&\unsure{\mathbf P&#124;P}_k^r` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 31: `u\arrow[r]&\unsure{\mathbf P&#124;P}_K^r\arrow[r]&\unsure{\mathbf P&#124;P}_k^r` | `\mathbf P` | P | medium |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 34: `\uline{Corollaire} \deleted{\unsure{Soit}}` | `Soit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 44: `on \deleted{peut} \unsure{pourra alors} utiliser une` | `pourra alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 45: `\unsure{section}` | `section` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 46: `\deleted{\unsure{pas}}` | `pas` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan067.tex | 067 | TeX line 47: `&#96;&#96;\unsure{spéciale}'' \ldots\ pour une courbe.}` | `spéciale` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan068.tex | 068 | TeX line 16: `\deleted{\unsure{(Alors normaux}}` | `(Alors normaux` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan068.tex | 068 | TeX line 19: `\deleted{\inserted{Soit $X$ \unsure{le}}` | `le` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan068.tex | 068 | TeX line 20: `\unsure{les modèles de tels}}` | `les modèles de tels` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan068.tex | 068 | TeX line 22: `\unsure{gros}` | `gros` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 6: `\deleted{\unsure{on a}}` | `on a` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 8: `\deleted{\unsure{de l'un des ens pts réguliers}}` | `de l'un des ens pts réguliers` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 10: `et soit $X_{\unsure{1&#124;\alpha}}$` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 12: `\inserted{propre \deleted{\unsure{normal}} \uline{dominant}}.` | `normal` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 16: `\deleted{\unsure{U}}X\arrow[ur,no head]\arrow[r,no head]&X'\del` | `U` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 16: `rrow[ur,no head]\arrow[r,no head]&X'\deleted{\unsure{U'}}&` | `U'` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 19: `\deleted{Soit $\unsure{U_1&#124;U_0}$ \unsure{l'ens des pts} de $U_0$ où` | `U_1` | U_0 | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 19: `\deleted{Soit $\unsure{U_1&#124;U_0}$ \unsure{l'ens des pts} de $U_0$ où` | `l'ens des pts` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 20: `l'application rationnelle évidente \deleted{\unsure{$X$}}` | `$X$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 21: `$U_0\to X_{\unsure{1&#124;\alpha}}$ induit` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 22: `\deleted{\unsure{par $f$}} est définie,` | `par $f$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 24: `\unsure{un ens fermé} de codim $\geq2$,` | `un ens fermé` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 25: `\deleted{\unsure{donc d'après le}}` | `donc d'après le` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 28: `\unsure{On a un}` | `On a un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 29: `\deleted{\unsure{hom canonique}},` | `hom canonique` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 33: `X_{\unsure{1&#124;\alpha}}\arrow[d,"f"']&&\\` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 36: `U_{\unsure{1&#124;\alpha}}\arrow[ull,"g"']` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 39: `\pi_1(X_{\unsure{1&#124;\alpha}})\arrow[dd,"f_*"']&` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 40: `\deleted{\pi_1(U_{\unsure{1&#124;\alpha}})}\arrow[l]&\\` | `1` | \alpha | low |
| 29; MPL_29_049-094_29_scan069.tex | 069 | TeX line 61: `\margin{\deleted{\unsure{of}}}` | `of` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 4: `Le dernier \unsure{est} est appelé le \uline{groupe fondamental bir` | `est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 6: `rait à l'introduire plutôt comme groupe alg. \unsure{lié&#124;lin}` | `lié` | lin | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 17: `\deleted{\unsure{Alors}}` | `Alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 27: `\deleted{\unsure{tout}}` | `tout` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 31: `\deleted{\unsure{modèle $X$}}` | `modèle $X$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 34: `sur un modèle $X'$ \unsure{déduit de}` | `déduit de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 35: `$X$ \unsure{par éclatemts} ?` | `par éclatemts` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan070.tex | 070 | TeX line 36: `C'est une question au fond de \unsure{schémas génériques} \ldots}` | `schémas génériques` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 7: `ec $Y$ \deleted{factoriel}\inserted{\deleted{\unsure{loc.}}\uline{régulier}}.` | `loc.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 16: `\margin{peut-on \deleted{\unsure{supposer $Y$ régulier??}}` | `supposer $Y$ régulier??` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 17: `\deleted{\unsure{connexe}} \unsure{sur $k$} ?}` | `connexe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 17: `\deleted{\unsure{connexe}} \unsure{sur $k$} ?}` | `sur $k$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 18: `\margin{N.B. factoriel ne suffit pas $=$ \unsure{est des pts de ces}` | `est des pts de ces` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 19: `\unsure{non-réduits, cf côtés} \ldots}` | `non-réduits, cf côtés` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 24: `\unsure{-- en principe} propre.` | `-- en principe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 45: `Or si $\xi$ est \deleted{\unsure{même}} $\tau$-équivalente à $0$,` | `même` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 47: `\deleted{\unsure{alors}}` | `alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 48: `$g^*(\unsure{\eta&#124;\xi})$ est` | `\eta` | \xi | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 50: `donc $i^{*-1}g^*(\unsure{\eta&#124;\xi})\deleted{\text{\unsure{même}}}$ aussi,` | `\eta` | \xi | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 50: `$i^{*-1}g^*(\unsure{\eta&#124;\xi})\deleted{\text{\unsure{même}}}$ aussi,` | `même` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 53: `\deleted{\unsure{aussi}}.` | `aussi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 56: `\deleted{\unsure{le diviseur exceptionnel}}` | `le diviseur exceptionnel` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 59: `0);\node[align=center] at (0,0) {Théorie des \unsure{classes}\\des cycles !};\end{tikzpicture}}}` | `classes` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan071.tex | 071 | TeX line 60: `\margin{$Y$ projectif ?? ou \unsure{proj.} sur $k$}` | `proj.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 8: `\deleted{\unsure{Or}}` | `Or` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 14: `, $f:\underline{\mathrm{Pic}}_Y^\tau\mathbin{\unsure{-&#124;\longrightarrow}}` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 31: `\mathbin{\unsure{-&#124;\longrightarrow}}` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 35: `{}_{F^{\unsure{\nu&#124;1}}}H^1(Y,\underline O_Y)` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 36: `\mathbin{\unsure{-&#124;\longrightarrow}}` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan072.tex | 072 | TeX line 37: `{}_{F^{\unsure{\nu&#124;1}}}H^1(X,\underline O_X)` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 3: `\deleted{\unsure{H}}` | `H` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 6: `$\pi_1(X)\mathbin{\unsure{-&#124;\to}}\pi_1(Y)$ est un isomorphisme` | `-` | \to | low |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 12: `H^0(Y,\underline O_Y/\underline O_Y^{p^{\unsure{\nu&#124;1}}})` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 14: `H^0(X,\underline O_X/\underline O_X^{p^{\unsure{\nu&#124;1}}})` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 20: `f^*:H^0(Y,\underline O_Y^{p^{-\unsure{\nu&#124;1}}}/\underline O_Y)` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 22: `H^0(X,\underline O_X^{p^{-\unsure{\nu&#124;1}}}/\underline O_X)` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 24: `\margin{$Y$ \unsure{lisse} sur $k$ (!)}` | `lisse` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 27: `car \deleted{\unsure{si $f$}} avec les notations ci-dessus, on a un` | `si $f$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 34: `[car $\underline O_X^{p^{-\unsure{\nu&#124;1}}}/` | `\nu` | 1 | medium |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 35: `\underline O_X^{\unsure{\tau}}$ est \deleted{\unsure{li}}` | `\tau` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan073.tex | 073 | TeX line 35: `\underline O_X^{\unsure{\tau}}$ est \deleted{\unsure{li}}` | `li` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 7: `et que $f:X\mathbin{\unsure{-&#124;\to}}Y$ provient d'un morphisme de` | `-` | \to | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 8: `-préschémas $\overline f:\overline X\mathbin{\unsure{-&#124;\to}}\overline Y$,` | `-` | \to | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 11: `\unsure{géomt} connexes.` | `géomt` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 12: `\deleted{Alors \unsure{pour}` | `pour` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 13: `$\forall\,\unsure{y\in Y&#124;s\in S}$ \unsure{sc}` | `y\in Y` | s\in S | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 13: `$\forall\,\unsure{y\in Y&#124;s\in S}$ \unsure{sc}` | `sc` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 16: `\unsure{peut supposer qu'il est constant}.}` | `peut supposer qu'il est constant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 18: `\deleted{\unsure{enfin que}}` | `enfin que` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 19: `Alors \deleted{\unsure{celui}}` | `celui` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 21: `$R^1q_*(\underline O_{\overline Y})\mathbin{\unsure{-&#124;\to}}` | `-` | \to | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 24: `(car il l'est en tt pt par \unsure{évidence&#124;réduction}).` | `évidence` | réduction | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 25: `Alors \unsure{rétrécissant} $S$, si le \unsure{conoyau}` | `rétrécissant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan074.tex | 074 | TeX line 25: `Alors \unsure{rétrécissant} $S$, si le \unsure{conoyau}` | `conoyau` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan075.tex | 075 | TeX line 10: `\deleted{régulière}\inserted{\unsure{séparable primaire&#124;séparablement primaire}}` | `séparable primaire` | séparablement primaire | low |
| 29; MPL_29_049-094_29_scan075.tex | 075 | TeX line 19: `\deleted{\unsure{donc}} c'est une condition un peu idiote!}` | `donc` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan075.tex | 075 | TeX line 24: `\deleted{\unsure{Il y aurait}}\inserted{\unsure{Cela}}` | `Il y aurait` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan075.tex | 075 | TeX line 24: `\deleted{\unsure{Il y aurait}}\inserted{\unsure{Cela}}` | `Cela` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan075.tex | 075 | TeX line 25: `\deleted{\unsure{du moins}} équivaudrait à la conjonction des` | `du moins` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan076.tex | 076 | TeX line 6: `propre \inserted{\unsure{sur $k$&#124;sur}} et universellement normal sur $k$]}` | `sur $k$` | sur | low |
| 29; MPL_29_049-094_29_scan076.tex | 076 | TeX line 8: `\deleted{$(X_i)_{i\in I}$ le système \unsure{ind}}` | `ind` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan076.tex | 076 | TeX line 11: `normal sur $k$, \deleted{\unsure{pour}} on ait \deleted{$\dim\uline{\mathrm{Pic}}_` | `pour` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan076.tex | 076 | TeX line 16: `\uline{Démonstration}. \deleted{\unsure{On est ramené au cas}}` | `On est ramené au cas` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan076.tex | 076 | TeX line 29: `et à ce titre, \unsure{on renvoie aux} théorèmes` | `on renvoie aux` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan077.tex | 077 | TeX line 4: `pour les modèles normaux (\unsure{résultant} de` | `résultant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan077.tex | 077 | TeX line 17: `C_{k(\unsure{u&#124;\omega})} \arrow[r,phantom,"\subset"] & X \arrow[r,` | `u` | \omega | low |
| 29; MPL_29_049-094_29_scan078.tex | 078 | TeX line 6: `($\pi_1$, \unsure{faisc. ét...})}` | `faisc. ét...` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 6: `&7\ \unsure{\leftarrow}\ 9\\` | `\leftarrow` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 11: `\margin{\unsure{total to} \unsure{all the} \unsure{implications}}` | `total to` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 11: `\margin{\unsure{total to} \unsure{all the} \unsure{implications}}` | `all the` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 11: `\margin{\unsure{total to} \unsure{all the} \unsure{implications}}` | `implications` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 15: `\deleted{\unsure{18&#124;13} --- Most examples come from usual` | `18` | 13 | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 16: `\unsure{proper} schemes over $\mathbf Z$!}` | `proper` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 36: `$\unsure{\mathfrak S}-\unsure{\operatorname{Supp}&#124;\operatorname{S` | `\mathfrak S` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 36: `$\unsure{\mathfrak S}-\unsure{\operatorname{Supp}&#124;\operatorname{Spec}}\,D$}}` | `\operatorname{Supp}` | \operatorname{Spec} | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 65: `26\quad \unsure{a)}\\` | `a)` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 66: `\hspace*{2em}\unsure{b)} Normality assumption more natural` | `b)` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 67: `(formal normality, \unsure{in loc.} formal schemes---)` | `in loc.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 69: `28\quad\unsure{15}` | `15` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan082.tex | 082 | TeX line 73: `Proof of $3.6.\unsure{5&#124;8}$ is unbelievably long!` | `5` | 8 | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 3: `\uline{IV}\quad \unsure{4.1.2}\quad` | `4.1.2` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 4: `4.1.2 \unsure{trivial} in terms of \uline{III} p. 16 added.` | `trivial` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 6: `Quite \inserted{\unsure{for $s^*$}} cumbersome; take point of` | `for $s^*$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 11: `\uline{VI}\quad 2\quad\unsure{inutile}` | `inutile` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 38: `$3/\unsure{8.1.6&#124;8.1.1}$ Not too clear. Say that if` | `8.1.6` | 8.1.1 | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 39: `\deleted{$A$ a local or \deleted{\unsure{local}} henselian ring, then to any}` | `local` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 46: `\deleted{$\unsure{\bar x},\bar y$}` | `\bar x` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 56: `& \bar y^{\unsure{\prime}}\arrow[l,dashed]\arrow[dl]\\` | `\prime` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 63: `1&14\ \deleted{\unsure{et}}\\` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan084.tex | 084 | TeX line 76: `\margin{yoga \unsure{stemming} from Abhyankar lemma to be used...}` | `stemming` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 5: `Appliquons \deleted{\unsure{8}}7.2.1 \deleted{\unsure{4}} au groupe formel` | `8` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 5: `ppliquons \deleted{\unsure{8}}7.2.1 \deleted{\unsure{4}} au groupe formel` | `4` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 7: `envisagé dans \deleted{\unsure{10}} 7.1 où le schéma` | `10` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 8: `\deleted{\unsure{dit}} formel abélien $\widehat B$ est algébrisab` | `dit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 9: `\inserted{et où on suppose de plus \deleted{\unsure{que}} $T_0$ isotrivial.}` | `que` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 11: `d{abélien B dont le}\inserted{en groupes $A^{\unsure{\natural&#124;\sharp}}$ sur $S$},` | `\natural` | \sharp | medium |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 15: `\deleted{\unsure{;}} que nous` | `;` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 17: `$A^{\unsure{\natural&#124;\sharp}}$ :` | `\natural` | \sharp | medium |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 19: `(\deleted{\unsure{8}}7.2.2)\qquad` | `8` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 20: `0\longrightarrow T\longrightarrow A^{\unsure{\natural&#124;\sharp}}` | `\natural` | \sharp | medium |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 26: `(7.2.3)\qquad A^{\unsure{\natural&#124;\sharp}}_n\simeq A_n` | `\natural` | \sharp | medium |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 32: `(7.\unsure{2&#124;3}.4)\qquad (A^{\unsure{\natural&#124;\sharp}})^\we` | `2` | 3 | low |
| 29; MPL_29_049-094_29_scan085.tex | 085 | TeX line 32: `(7.\unsure{2&#124;3}.4)\qquad (A^{\unsure{\natural&#124;\sharp}})^\wedge\simeq\widehat A,` | `\natural` | \sharp | medium |
| 29; MPL_29_049-094_29_scan086.tex | 086 | TeX line 7: `\margin{\unsure{d}}` | `d` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan086.tex | 086 | TeX line 9: `\margin{$\unsure{+S_3}$}` | `+S_3` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan086.tex | 086 | TeX line 17: `12\quad Amounts to showing: \deleted{\unsure{$X$}}` | `$X$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan086.tex | 086 | TeX line 18: `\unsure{fnt&#124;finite} flat covering of $S$` | `fnt` | finite | low |
| 29; MPL_29_049-094_29_scan086.tex | 086 | TeX line 19: `is tame with r. to $D_1,D_2$ iff it \deleted{\unsure{is so}}` | `is so` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 6: `est toujours un $\unsure{\mathrm{Ab}&#124;\mathcal A}$, donc` | `\mathrm{Ab}` | \mathcal A | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 7: `nserted{qu. coh.} stratifié} est toujours un \unsure{itou}.` | `itou` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 9: `\unsure{induit&#124;usuel} d'image inverse des Modules` | `induit` | usuel | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 14: `Supposons que si $X'\unsure{-&#124;\longrightarrow}X\times_S S'$ est` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 15: `un \unsure{m.u.} (resp. fini \deleted{\unsure{ou}} non ramif` | `m.u.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 15: `un \unsure{m.u.} (resp. fini \deleted{\unsure{ou}} non ramifié)` | `ou` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 17: `$T_0\times_X X'\unsure{-&#124;\longrightarrow}T\times_S S'$` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 18: `est également un \unsure{m.u.}` | `m.u.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 24: `\unsure{dans le 1er cas}. Alors` | `dans le 1er cas` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 28: `\unsure{(comme au dessus)} si $F'$ est un faisceau` | `(comme au dessus)` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan087.tex | 087 | TeX line 36: `S &&& {T\times_S S'\ \unsure{=}\ T'}\arrow[ull,dashed]\arrow[dl,double] &\\` | `=` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 6: `$D=\deleted{\unsure{+}}\bigcup_0^{\unsure{r}}D_i$,` | `+` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 6: `$D=\deleted{\unsure{+}}\bigcup_0^{\unsure{r}}D_i$,` | `r` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 7: `\unsure{diviseurs} \deleted{avec} \unsure{normaux}` | `diviseurs` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 7: `\unsure{diviseurs} \deleted{avec} \unsure{normaux}` | `normaux` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 10: `$D'=\sum_{i\ne0}D_i$, $\unsure{D'_0&#124;D_0}$ induit sur $X_0$.` | `D'_0` | D_0 | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 37: `\deleted{\unsure{\mu}\longrightarrow}` | `\mu` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 44: `\mu(\deleted{\unsure{\bar\xi}}\bar\xi_0)` | `\bar\xi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 67: `\deleted{\unsure{via op---}}.` | `via op---` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 70: `\alpha\deleted{\unsure{\xi}}\in H^2(\pi_1^t(U),I_0)` | `\xi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 72: `\deleted{\unsure{\xi}}\alpha=?` | `\xi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 98: `\unsure{\simeq}\\` | `\simeq` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 105: `H^{\unsure{n}}(U,J)\Longleftarrow` | `n` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 108: `\deleted{\unsure{$\rho$}} \unsure{can.}` | `$\rho$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 108: `\deleted{\unsure{$\rho$}} \unsure{can.}` | `can.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan088.tex | 088 | TeX line 115: `\simeq\operatorname{Hom}(\unsure{\pi_1^t(U)&#124;\pi_2^t(U)},I)^{\pi_1^t}` | `\pi_1^t(U)` | \pi_2^t(U) | low |
| 29; MPL_29_049-094_29_scan089.tex | 089 | TeX line 26: `qui est représentable \deleted{\unsure{par un}}` | `par un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan089.tex | 089 | TeX line 32: `$\uline{O}_S$. (No\deleted{\unsure{On vit}}tons` | `On vit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan089.tex | 089 | TeX line 35: `\deleted{\unsure{Définition 1.1. Un}}` | `Définition 1.1. Un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan089.tex | 089 | TeX line 36: `abélien, de sorte \deleted{\unsure{qu'il n'y a pratiquement}}` | `qu'il n'y a pratiquement` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan089.tex | 089 | TeX line 40: `t isomorphe à un schéma de la forme \deleted{\unsure{et}}` | `et` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 7: `\inserted{la classe de \deleted{de} Chern \unsure{étale de}}` | `étale de` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 9: `(\deleted{\unsure{\mathfrak X}}T_{X_0/\mathfrak X})` | `\mathfrak X` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 12: `Soit $\sigma:H^2(\unsure{X&#124;X_0},\mu)\unsure{-&#124;\longrightarrow}H^2(U,I)$` | `X` | X_0 | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 12: `Soit $\sigma:H^2(\unsure{X&#124;X_0},\mu)\unsure{-&#124;\longrightarrow}H^2(U,I)$` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 20: `On sait déjà \unsure{que le&#124;par le}` | `que le` | par le | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 31: `\deleted{\unsure{$\rho\beta$}}` | `$\rho\beta$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 33: `(\unsure{commutatif}, \inserted{par lemme 2})` | `commutatif` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 38: `\arrow[r,"\deleted{\unsure{0}}"]&` | `0` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 40: `\arrow[d,"\alpha"'," \deleted{\unsure{\text{étale}}}"]\\` | `\text{étale}` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 42: `{\deleted{\unsure{\mu_0}\longrightarrow}\unsure{I_0}}` | `\mu_0` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 42: `{\deleted{\unsure{\mu_0}\longrightarrow}\unsure{I_0}}` | `I_0` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 46: `$(\unsure{i\ne j})$` | `i\ne j` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 47: `[à vérifier si \unsure{ceci est indispensable}]}` | `ceci est indispensable` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 49: `par lemme 1. Ceci \unsure{nous définit} l'hom.` | `nous définit` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 50: `\deleted{\unsure{dans}} de $\pi_2^t$ défini par une 2-classe].` | `dans` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 51: `Donc \deleted{$\unsure{I_0}$}` | `I_0` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 53: `atorname{Im}\pi_2^t(U)$. Je dis que \deleted{\unsure{alors}}` | `alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 58: `I'_0\deleted{\unsure{:=}}=\deleted{\unsure{I}}` | `:=` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 58: `I'_0\deleted{\unsure{:=}}=\deleted{\unsure{I}}` | `I` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 64: `\operatorname{Ker}\bigl(H^2(U,I'_0)\unsure{-&#124;\longrightarrow}` | `-` | \longrightarrow | low |
| 29; MPL_29_049-094_29_scan090.tex | 090 | TeX line 68: `donc \unsure{$I\beta$&#124;$\operatorname{Im}\beta$}` | `$I\beta$` | $\operatorname{Im}\beta$ | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 11: `ordinaires, \deleted{\unsure{alors}} l'homomorphisme naturel` | `alors` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 20: `\deleted{\unsure{il est}} donc défini par un nombre fini de générate` | `il est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 22: `\deleted{\unsure{préschéma en groupes $G$ sur $S$, on a une}}` | `préschéma en groupes $G$ sur $S$, on a une` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 32: `D'autre part \unsure{un&#124;on} définit de façon évidente un homomorphisme` | `un` | on | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 38: `qui est toujours \deleted{\unsure{inj&#124;un}} un monomorphisme, et qui est un isomorphis` | `inj` | un | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 41: `\uline{Corollaire} 1.5. \deleted{\unsure{Supposons $M$}}` | `Supposons $M$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan091.tex | 091 | TeX line 43: `ordinaires, $M$ de type fini, alors \deleted{\unsure{on a}}` | `on a` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 5: `\deleted{$\unsure{\Pi'}$, \unsure{un}} $\Pi'$, et on a` | `\Pi'` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 5: `\deleted{$\unsure{\Pi'}$, \unsure{un}} $\Pi'$, et on a` | `un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 6: `\deleted{\unsure{donc}} \unsure{aussi} un \uline{épimorphisme}` | `donc` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 6: `\deleted{\unsure{donc}} \unsure{aussi} un \uline{épimorphisme}` | `aussi` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 17: `\deleted{\unsure{il}} $J_0$ apparaît comme groupe d'inertie dans` | `il` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 18: `un revêtement \deleted{\unsure{tame}} modéré de $\mathfrak X/X_0$.` | `tame` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 20: `$\beta\in H^2(\unsure{X&#124;X_0},\mu)$ dans $H^2(\widetilde U^t,J_0)$` | `X` | X_0 | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 21: `est nulle; elle est donc nulle déjà \deleted{\unsure{en}} à un` | `en` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 24: `\unsure{si&#124;et} \deleted{$\unsure{U}$} \unsure{n'est pas no` | `si` | et | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 24: `\unsure{si&#124;et} \deleted{$\unsure{U}$} \unsure{n'est pas noeth}` | `U` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 24: `\unsure{si&#124;et} \deleted{$\unsure{U}$} \unsure{n'est pas noeth}` | `n'est pas noeth` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 27: `\deleted{\unsure{de revêt} $\mathfrak X$ \unsure{nul} /` | `de revêt` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 27: `\deleted{\unsure{de revêt} $\mathfrak X$ \unsure{nul} /` | `nul` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 28: `$D_i$ \unsure{disjoints} \unsure{on peut}}` | `disjoints` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 28: `$D_i$ \unsure{disjoints} \unsure{on peut}}` | `on peut` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 29: `\deleted{\unsure{loisir}}` | `loisir` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 30: `\margin{\unsure{ce qui du} \unsure{pro.} \unsure{dans} \unsure{est} \u` | `ce qui du` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 30: `\margin{\unsure{ce qui du} \unsure{pro.} \unsure{dans} \unsure{est} \unsure{faux}}` | `pro.` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 30: `\margin{\unsure{ce qui du} \unsure{pro.} \unsure{dans} \unsure{est} \unsure{faux}}` | `dans` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 30: `nsure{ce qui du} \unsure{pro.} \unsure{dans} \unsure{est} \unsure{faux}}` | `est` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan092.tex | 092 | TeX line 30: `du} \unsure{pro.} \unsure{dans} \unsure{est} \unsure{faux}}` | `faux` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 4: `\deleted{\unsure{au moins}} $n$ éléments. Or $T$ est isomorphe` | `au moins` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 6: `produit des $n_i$, donc $D(T)$ est \deleted{\unsure{somme}}` | `somme` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 16: `\deleted{$\unsure{n_i}$ \unsure{sss} $(\unsure{n}\unsure{n_i})$}` | `n_i` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 16: `\deleted{$\unsure{n_i}$ \unsure{sss} $(\unsure{n}\unsure{n_i})$}` | `sss` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 16: `\deleted{$\unsure{n_i}$ \unsure{sss} $(\unsure{n}\unsure{n_i})$}` | `n` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 16: `eted{$\unsure{n_i}$ \unsure{sss} $(\unsure{n}\unsure{n_i})$}` | `n_i` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 22: `\uline{Théorème} 3.1. Soi\deleted{\unsure{ant}}t $S$ un préschéma non vide,` | `ant` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 23: `\deleted{\unsure{fixés}} et` | `fixés` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 32: ` \overset{u'}{\deleted{\unsure{a}}}\ D_S(M')\quad0` | `a` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan093.tex | 093 | TeX line 34: `lors $v'$ induit un isomorphisme de \deleted{\unsure{ni}} $D_S(M'')$` | `ni` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 5: `\inserted{(du moins si les $D_i$ \unsure{sont} disjoints)}) ]` | `sont` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 6: `on est ramené au cas où la \unsure{classe} $\beta$ est dans le noyau de` | `classe` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 8: ` H^2(\unsure{X&#124;X_0},\mu_0)\longrightarrow H^2(U,J_0).` | `X` | X_0 | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 12: `l'hypothèse dit que l'image de \deleted{$\unsure{\beta}$}` | `\beta` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 15: ` \qquad\text{dans }H^2(\unsure{U&#124;X_0},\mu_n)\text{ est}` | `U` | X_0 | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 18: `donc \deleted{$\beta_0\in\operatorname{Im}H^{\unsure{1}}$}` | `1` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 20: `$\operatorname{Im}H^2_{D_0'}(\unsure{X&#124;X_0},\mu_n)=\ldots$}` | `X` | X_0 | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 22: ` \unsure{+}\unsure{d}$}` | `+` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 22: ` \unsure{+}\unsure{d}$}` | `d` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 24: `les $\beta^i$ \unsure{correspondent} aux diviseurs $D_i$ (lisses)}` | `correspondent` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 26: `\unsure{En&#124;Enfin} \unsure{fait&#124;faut}, \unsure{nous avons}` | `En` | Enfin | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 26: `\unsure{En&#124;Enfin} \unsure{fait&#124;faut}, \unsure{nous avons}` | `fait` | faut | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 26: `\unsure{En&#124;Enfin} \unsure{fait&#124;faut}, \unsure{nous avons}` | `nous avons` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 34: `sont \deleted{\unsure{tels que}} \uline{uniquement divisibles} par $n$,` | `tels que` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 43: ` {}_n(\operatorname{Pic}(\mathfrak X)/\unsure{\mathcal R_0})` | `\mathcal R_0` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 47: `\deleted{$\unsure{n\gamma}$ \unsure{$n\gamma_0=\beta^{\unsure{2h&#124;2}}$}` | `n\gamma` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 47: `\deleted{$\unsure{n\gamma}$ \unsure{$n\gamma_0=\beta^{\unsure{2h&#124;2}}$}}` | `$n\gamma_0=\beta^{\unsure{2h&#124;2}}$` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 47: `$\unsure{n\gamma}$ \unsure{$n\gamma_0=\beta^{\unsure{2h&#124;2}}$}}` | `2h` | 2 | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 49: `\unsure{défini} par $X_0$ dans $\mathfrak X$]` | `défini` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 50: `\deleted{est de la forme $\unsure{\beta}=n\gamma+\sum\lambda_i\beta^i$}` | `\beta` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 53: `\node[rotate=30,align=center] at (0,.9) {\unsure{dégager un}\\\unsure{lemme}!};` | `dégager un` | No secure alternative; the first reading remains doubtful. | low |
| 29; MPL_29_049-094_29_scan094.tex | 094 | TeX line 53: `lign=center] at (0,.9) {\unsure{dégager un}\\\unsure{lemme}!};` | `lemme` | No secure alternative; the first reading remains doubtful. | low |

## Doubts about placement, page state, and graphical form

| File/cote | Scan | Approximate location | First reading/state | Alternative or limitation | Confidence |
|---|---:|---|---|---|---|
| 29 | 050 | Opening seven lines | Rewritten localization paragraph with interlinear additions | Some attachment points and cancellation boundaries remain uncertain even where a tentative word is supplied. | low |
| 29 | 052 | Lemme 3 revision | Stronger finite-fibre statement replaces a finiteness hypothesis | The deletion crosses the inserted word; the exact order of pen actions is not recoverable. | medium |
| 29 | 054 | Condition (ii) | intègre affine and affine inserted at their written anchors | Crowded interlinear text permits a different attachment; the mathematical hypothesis has not been reconstructed. | low |
| 29 | 061–062 | Generic-curve passages | Rewritten section and neighbourhood qualifiers | Some overlapping insertions have no decisive caret; final wording is not a critical reconstruction. | low |
| 29 | 065 | Central completion diagram | Upper hat/bar X-prime, lower barred X | The shapes differ; no identification of the two operations is imposed. | medium |
| 29 | 066 | Corollary and final paragraph | fermé before de codim; Y-prime of codimension at least 2 | The latter clause is transcribed as written; whether it is an extra hypothesis is a research question. | medium |
| 29 | 068–069 | Cancelled model discussion | Entire crossed passages retained | Multiple cancellation layers cannot always be put in a certain chronological order. | low |
| 29 | 071 | Restriction display | Pic(X) to Pic(U) | X is the visible letter; the surrounding Y does not authorize substitution. | high |
| 29 | 071 | Narrow left and lower margins | Questions about normality, projectivity and cycles | Several words remain only tentative; no argument should depend on those readings alone. | low |
| 29 | 073 | Last quotient denominator | Small raised tau-like mark | It may be a correction stroke, not an exponent. | low |
| 29 | 078 | Cancelled earlier cover title | Pi-one / étale-sheaf abbreviation | Crossed letters are only partly separable; no completion from the live title is made. | low |
| 29 | 082 | Top centre and outlined notation | Individually doubtful English words; script S minus Supp D | Spec D is possible; the extra English phrase is particularly unreliable. | low |
| 29 | 085 | Top centre number 69 | Clear numeral, uncertain writer | Not assigned to authorial pagination; the whole-page diagonal may mark reuse rather than substantive retraction. | medium |
| 29 | 086 | Faint d and plus S-three above item 12 | Tentative marks retained | Could be show-through from the other side rather than recto additions. | low |
| 29 | 087 | Whole cancelled draft and ten-object diagram | All visible objects, connectors and overwritten text retained | Cancellation overlaps several labels; m.u. and the category abbreviation remain unresolved. | low |
| 29 | 088 | Inertia sequences | Upper stroke over first I-zero retained | Serif versus separate bar is not completely decidable. | medium |
| 29 | 089, 091, 093 | Typed displays | Visibly empty positions retained as spacing | Expected operators are not supplied, even where the mathematics makes them predictable. | high |
| 29 | 092 | Bottom-left marginal fragment | Tentative “ce qui du / pro. dans / est faux” | Extremely uncertain and without a secure referent; it is not evidence of a retraction. | low |
| 29 | 093 | First line | Inserted n before égal | No clear caret determines whether it belongs before égal or near ordre. | low |
| 29 | 093 | Second sequence below u-prime | A tentatively cancelled a | Could be n; even the cancellation is uncertain. | low |
| 29 | 094 | Central overwriting and final quotient | Tentative live/deleted layers and script R-zero denominator | The denominator is not identified from the desired proof; the last line is partly at the scan edge. | low |
| 29 | all drawings | TikZ reconstructions | Relative geometry, strokes, labels and emphases approximated | TikZ captures the visible structure, not pen texture or exact pixel geometry; uncertainty in a label is marked in place. | medium |

## Abbreviations encountered

Expansions below are interpretive aids only. They have not been inserted into the transcription. A slash separates plausible expansions when the abbreviated form is not decisive.

| Written form or family | Tentative expansion or explanation |
|---|---|
| alg., algéb. | algébrique / algébriquement |
| birat., birat.elle | birationnel / birationnelle; the second written form is itself doubtful |
| can. | canonique / canoniquement |
| car. | caractéristique, or car where it is an ordinary word; determined locally |
| cat. | catégorie |
| cf. | confer, compare |
| C.Q.F.D., cqfd. | ce qu'il fallait démontrer |
| codim | codimension |
| coh., qu.coh. | cohérent; quasi-cohérent |
| comp., compl. | complet / complément, according to the phrase |
| conn. | connexe |
| constr. | constructible |
| Cor., cor. | corollaire |
| Dém. | démonstration |
| dim | dimension |
| ens. | ensemble |
| équiv. | équivalent / équivalence |
| ét. | étale |
| ext. | extension |
| faisc. | faisceau |
| fnt (doubtful) | finite / finite-type shorthand; unresolved in scan 086 |
| fund. | fundamental / fondamental |
| gal. | galoisien |
| gén. | générique / général |
| géo., géom., géométr. | géométrique / géométriquement |
| gr., grps | groupe, groupes |
| hom. | homomorphisme / homotopie, according to context |
| hyp. | hypothèse |
| i.e. | id est, that is |
| iff | if and only if |
| int. | intègre / intégral; an overwritten occurrence is unresolved |
| irrédu. | irréductible |
| isom. | isomorphisme |
| loc., loc. cit. | localement / local; loco citato |
| m.u. | unresolved abbreviation in the cancelled stratification draft, scan 087 |
| nb. | nombre |
| N.B., NB | nota bene |
| néc. | nécessaire / nécessairement |
| noeth. | noethérien |
| N° / n° | numéro |
| n.r. | non ramifié |
| Pb | problème |
| p.ex. | par exemple |
| préschém. | préschéma |
| proj. | projectif / projective |
| prop., Prop. | propre or proposition, depending on position |
| pts | points |
| quelc. | quelconque |
| r. to | with respect to |
| rat/k | rationnel sur k |
| Réf, réf. | référence |
| resp. | respectivement |
| rev., revêt., revêtts | revêtement(s) |
| SGA | Séminaire de géométrie algébrique; the manuscript's abbreviated reference is retained |
| sss | si et seulement si |
| surj. | surjectif / surjective |
| t.f. | type fini |
| th., thme, Thm | théorème |
| tjrs | toujours |
| top., top with raised t | topologique / topologiquement |
| tt, tte, tts | tout, toute, tous |
| univ. | universel / universellement |

## Legibility and limits

The reused typescripts are mostly substantially clearer than the handwriting, but their overtyped deletions and visibly unprinted mathematical operators require care. The handwritten pages alternate between readable prose and extremely compressed strokes; scans 050 and 062, the margins of 071, the cancelled stratification draft 087, the lower margin of 092, and the overwritten formulas at the foot of 094 are the least secure areas. The Greek/order glyph in the distribution typescript and several font distinctions remain unresolved despite comparison across their occurrences.

The root reader inspected every supplied whole page followed by both halves during the first reading, then performed a second image audit of all 42 retained scans; extra rotations and enlargements were used for difficult areas. No OCR was used, and no second agent transcribed or audited images. The mechanical validation only checks packaging and LaTeX syntax and cannot certify the readings. Doubt marks are part of the deliverable, not a claim that all other ink is infallibly read; badly overwritten text, insertion attachment and cancellation extent merit further expert comparison with the scans.
