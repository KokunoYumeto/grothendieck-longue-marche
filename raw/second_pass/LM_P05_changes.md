# LM_P05 (scans 41–50): second-pass changes

Ms. pp. 19–23 (folios 40–49): the end of the explicit description of 1-morphisms of the groupoid systems, the
"Catégorie bordélique précisée" in group-theoretic terms (scans 43–44), the switch to the triangle
Π_{D*} → Π_U → Π_e (scans 44–45), and the dictionary a)–d) for 1-morphisms of the systems of diagrams D′ → D
(scans 48–50). Every scan was read in both halves at the archive's resolution; enlarged and rotated crops of the
disputed places are in `second_pass/work_LM_P05` (named s41_*, s42_*, …; cmp_* are side-by-side glyph
comparisons). Witnesses: CSG = `CSG_G103d_draft_2026-02.txt` (ll. 862–1229), IUT =
`IUT_galoisI_historical_witness.txt` (ll. 902–1293), CK = `Carmona_Kuenzer_207page_historical_witness.txt`
(ll. 736–904). CSG loses most primes in extraction; IUT keeps them. The checked file compiles (pdflatex, wrapper with
stub macros).

Rows that change the mathematics: 5, 16–18, 20, 32, 36, 39, 42, 44. Rows 10, 19 and 40 change how a display or diagram is
represented, not its content.

## Changes

| # | Scan | Place | First pass | Corrected | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 41 | l. 3 | `\alpha_{D^*U}` (second occurrence) | `\alpha_{D^*,U}` | A comma stands between the star and *U* here, not in l. 1. Witnesses normalise both to α_{D∗,U}. | medium |
| 2 | 41 | l. 6, line start | `\deleted{\unsure{tels que}}\inserted{tels que}` | `\deleted{\illegible{1}}\inserted{tels que}` | The struck word has two ascenders and no *q* descender: it is not "tels que". "tels que" is written just below it as the replacement. | medium |
| 3 | 41 | square, top left | `\unsure{\mathcal G'_{i'}\|\widehat G'_{i'}}` | `G'_{i'}` | Cursive capital *G*; the mark above is the prime, written as a short crossed stroke, not a hat. Same letter as the G_i, G′_{i′} → G_{τi′} of scan 39. IUT: G′_{i′}. | medium |
| 4 | 41 | square, bottom left | `\unsure{\mathcal G_{\tau i'}\|\widehat G_{\tau i'}}` | `G_{\tau i'}` | As row 3. | medium |
| 5 | 41 | ll. 12–14 | `$(…)$ \illegible{1} \unsure{ci-dessus} avec $K$` | `$(…)$ avec lui-= et avec $K$` | "avec" is written small after the closing parenthesis at the line end; the next line begins "lui-=" (= for *même*), then "et avec K". CSG, IUT, CK: "avec lui même et avec κ". The tuple must be compatible with itself and with K: two compatibilities, matching "les deux compatibilités". | high |
| 6 | 41 | last equation, struck start | `\deleted{\unsure{\rho(\beta_{i'})}}` | `\deleted{\unsure{\rho(\beta_{i'})\|p(\beta_{i'})}}` | Hatched over; same letter question as the insertion above the line (unresolved 3). | low |
| 7 | 42 | l. 1 | `En \unsure{résumé\|résumant}` | `En résumé` | The word ends in *é* with a descending flourish; no *-ant*. CSG, IUT, CK: "En résumé". | medium |
| 8 | 42 | first diagram, E_i → E | `\unsure{\rho_i\|f_i}` | `\rho_i` | Looped ρ with a short tail, no f cross-bar. CSG: ρ_i. ρ_i names E_i → E on scans 39, 43, 46. | medium |
| 9 | 42 | l. 10 | `enfin \deleted{de \illegible{1}}` | `enfin \deleted{de systèmes}` | "de systèmes" legible under the stroke. | medium |
| 10 | 42 | prism | prose description in brackets; `\unsure{f_{i'}\|f^0_{i'}}` on E′_{i′} → E_i | tikz-cd drawing of the four rows (rows 2 and 4 shifted right), with every arrow and label as written; bracketed note for the doubled stroke of the d_{i′} arrow and the overwritten marks; label `f_{i'}` | Each object, arrow and label checked on the image. The mark above the *f* is its detached top hook, not a 0 (compare f^0_{i′} on scan 50). The two diagonal injections carry hooks. | medium |
| 11 | 42 | left margin | `\mathcal E_i\longrightarrow\mathcal E` | `\mathcal E_i\hookrightarrow\mathcal E` | The arrow is drawn with a hook. | medium |
| 12 | 42 | left margin, l. 3 | `le $f_{i'}$` | `\deleted{le} $f_{i'}$` | "le" is blotted out in heavy ink. CSG, IUT omit it. | low |
| 13 | 42 | left margin | `des $f_{i'}$`; `\unsure{condition sur les couples}` | `\unsure{de\|des} $f_{i'}$`; `condition sur les couples` | "condition" and "couples f_E, β_{i′}" are legible; the article is a short *d*-word. CSG, IUT: "de". | medium |
| 14 | 42 | left margin | `revenant \unsure{à dire} que` | `\illegible{1} \unsure{savoir} que` | s-a-v-o-i-r before "que", no *n-t*; small marks before it are unread. CSG, IUT, CK: "savoir que". | medium |
| 15 | 42 | left margin, end | `(\unsure{\mathcal E'_{i'}})$ \unsure{tombe dans} $\unsure{\rho_i(\mathcal E_i)}$` | `$ \unsure{$\mathcal E'_{i'}$} dans $\unsure{\rho_i(\mathcal E_i)\|p_i(\mathcal E_i)}$` | "dans" is clear and there is no "tombe". The letter before (E_i) has a long straight stem like a Latin p. CSG, IUT: "applique E_{i′} dans p_i(E_i)". | medium |
| 16 | 42 | right margin, l. 1 | `\unsure{On} \illegible{1}` | `OPS` | Capitals O, P, S: the abbreviation of "On peut supposer", which CSG and IUT expand. | high |
| 17 | 42 | right margin | `l'image de \illegible{3} sur $\operatorname{Spec}(\bar K)$` | `l'image de $\unsure{\psi\|\varphi}\sigma(D_i^*)$ \unsure{sur} $\operatorname{Spec}(\bar K)$` | A crossed circle (ψ or φ), σ, then (D_i^*). CSG, IUT: "ψ(σ(D_i∗)) avec Spec(K)". | medium |
| 18 | 42 | right margin, end | `\unsure{\varphi(\rho(D_{i'}^*))\simeq\varphi(\widetilde U)} \illegible{3})` | `$\varphi(\rho(D_i^*))\simeq\varphi(\unsure{\widetilde U\|\widetilde U_i})$ \unsure{avec} $\operatorname{Spec}\bar K$` | No prime on the index; the line ends "avec Spec K̄", and no closing parenthesis is written. CSG: "ϕ(ρ(D_i∗)) = ϕ(U) avec Spec K [?])". | medium |
| 19 | 42 | right margin → main text | margin ends `i.e. \deleted{\illegible{1}} $\alpha\gamma'_{i'}=p(\beta_{i'})\gamma_i\alpha_{i'}$` | moved into the main display, after the formula for α_{i′} | It sits on the baseline of the main formula, directly to its right, below the end of the margin note. CSG, IUT, CK place it after the main formula. | medium |
| 20 | 42 | main text before the formula | `\unsure{pour} des` | `\unsure{où on a} posé` and the tag `(*)` before α_{i′} = … | "posé" (accent visible) is clear; before it a w-shaped "où", a crossed stroke and a dot. The blot read as "des" is a looped parenthesis with a star inside and ")" (crop cmp_star_42_43): the label (*). CK tags this formula (∗); CSG, IUT: "où on a posé". Scan 43's "relation plus précise (*)" points back to it. | medium |
| 21 | 42 | before "la face" | `i.e. la face` | `et \unsure{i.e.\|où} la face` | "et" is written before a dotted sign. CSG, IUT, CK: "et où la face". | low |
| 22 | 42 | same line | `postérieure du prisme` | `postérieure des prismes` | "des", and "prismes" with its final *s*. All witnesses agree. | high |
| 23 | 42 | last lines | `\unsure{aussi}`; `\unsure{l'autre carré}` | `aussi`; `l'autre carré` | Both legible. | medium |
| 24 | 43 | l. 1 | `comm., s'en déduit` | `comm. s'en déduit` | A full stop, no comma. | medium |
| 25 | 43 | l. 6, line end | `étant commutative` | `étant \deleted{\unsure{cont}}commutative` | A struck "cont" joins the start of "commutative". | low |
| 26 | 43 | heading | `Catégorie \unsure{bordélique} \unsure{précise\|précisée}` | `Catégorie bordélique précisée` | "bordélique" is legible; "précisée" has its second *e*. Witnesses agree on "bordélique précisée" (but write "Conjecture"; see witness errors). | medium |
| 27 | 43 | l. 13 | `\deleted{couples \illegible{2}}\inserted{homs de gr. profinis}` | `\deleted{couples $(I$, \unsure{systèmes}}\inserted{homs de gr.} profinis` | Struck "couples (I, systèmes"; "homs" and "de gr." written above; "profinis" stands on the line after the struck words. | low |
| 28 | 43 | last display | `\unsure{\overset{k_i}{\simeq}\|\xrightarrow[\sim]{k_i}}` | `\overset{k_i}{\simeq}` | ≃ with k_i above, no arrowhead. | medium |
| 29 | 44 | l. 3 | `est donné par \unsure{par} un hom` | `est donné par par un hom` | "par" ends one line and begins the next. | medium |
| 30 | 44 | upper left margin | `\unsure{pas}`; `aussi $\unsure{\gamma_i}\beta_{i'}$, avec $\unsure{\gamma_i}\in…$` | `pas`; `aussi $\gamma\beta_{i'}$, avec $\unsure{\gamma\|\gamma_i}\in…$` | γ stands directly before β with no index; the second γ may be followed by *i* or by the start of ∈. CSG, IUT: "γβ_{i′}, avec γ ∈ Im κ_i". | low |
| 31 | 44 | upper left margin, end | `Mais $\alpha$ \illegible{2} ?!` | `Mais $\alpha$ unique \unsure{?!\|??}` | u-n-i-q-u-e with the *q* descender. CSG, IUT: "Mais α unique ??". | medium |
| 32 | 44 | condition 2° | `\unsure{\subset\|=}` | `\subset` | Two strokes joined on the left (a squared ⊂). An = would have two free strokes. CSG, IUT read "=". | high |
| 33 | 44 | right margin | `\unsure{\operatorname{Im}(fk'_{i'})}`; `\deleted{\illegible{2}}` | `\unsure{\operatorname{Im}(fk'_{i'})\|\operatorname{Im}k'_{i'}}`; `\deleted{\unsure{cette} image}` | The stroke between Im and k′ may be an f or a parenthesis. The struck words end in "image". | low |
| 34 | 44 | last line | `et de définir $\Pi_D$` | `et de déduire $\Pi_D$` | d-é-d-u-i-r-e, with no f descender. CSG, IUT, CK: "déduire". | high |
| 35 | 45 | l. 2 | `un iso sur les $\pi_0$` | `un iso sur $\pi_0$` | "les" is written only before π_1. Witnesses agree. | medium |
| 36 | 45 | first display | `\xrightarrow{\varphi}` | `\xrightarrow{\varphi'}` | A prime above φ, like those on Π′_{D*}, ρ′ and Π′_U. CSG, IUT: ϕ′. The source triangle has its own φ′. | high |
| 37 | 45 | after the first display | — | `\deleted{dans}` | "dans" at the end of that line is struck through and rewritten at the start of the next line. | medium |
| 38 | 45 | "sont les …" | `\deleted{\illegible{1}}\inserted{\uline{\unsure{quintuplets\|quintuples}}}` | `\deleted{\unsure{couples}}\inserted{quintuplets}` | The inserted word ends in *-lets*, with two ascenders before the final *s*. The line under it is the stroke through the word below, not an underline. CSG, IUT: "quintuplés". | medium |
| 39 | 45 | insertion above "foncteurs" | `\inserted{et iso de foncteurs}` | `\inserted{et $3$ iso de foncteurs}` | A dark *3* stands between "et" and "iso". CSG: "et 3-isomorphismes"; CK: "et 3 isomorphismes". The quintuplet is 2 functors and 3 isomorphisms (α_{D*U}, α_{Ue}, K). | high |
| 40 | 45 | diagram | two tikz-cd diagrams, the second nested inside the first `\diagram` (a plain ladder, then the same with 2-cells) | one diagram, with the 2-cells α_{D*U}, α_{Ue} | The page has one diagram; the duplicate came from the earlier fix. | high |
| 41 | 45 | upper left margin (vertical) | `\inserted{de groupes \unsure{abéliens}}`; `écrire`; `\unsure{\bar k}` | `\inserted{de groupes (\unsure{commutatifs\|abéliens})}`; `\unsure{définir\|écrire}`; `\unsure{\bar k\|k}` | The parenthesised word begins with *c* and has no *b* or *l* ascender. The verb before the box is partly hidden by its edge, with one tall first stroke. The bar over k may be the top edge of the box. CSG, IUT: "(commutatifs)", "définir". | low |
| 42 | 45 | lower left margin | `par un \unsure{indice de ramification}` | `par un $d$ \unsure{indice de ramification}` | A *d* stands after "par un". CSG, IUT: "par un d (indice de ramification)". | medium |
| 43 | 46 | l. 4 | `\unsure{\Pi_U,\Pi'_U}` | `\Pi_U,\Pi'_U` | Both legible, with the prime on the second. | medium |
| 44 | 46 | display | `\mathcal E\xrightarrow{p}\Gamma` | `\mathcal E\xrightarrow{\varphi}\Gamma` | The label is a circle crossed by a vertical stroke (φ), unlike the p's of scan 47. CSG: E −φ→ Γ; CK: ϕ. | high |
| 45 | 46 | "De =" | `De \unsure{=}` | `De =` | A clear = sign (for *même*). | medium |
| 46 | 46 | last sentence | `Si on change \inserted{\illegible{2}} $\widetilde U_i$, … groupe isom, défini à aut. int. près.` | `Si on change $\widetilde U_i$, … groupe isom, \inserted{l'isom} défini à aut. int. près.` | The interlinear "l'isom" is joined by a curved line to the caret before "défini" on the next line. CSG, IUT: "l'isomorphisme défini à automorphisme intérieur près". | medium |
| 47 | 47 | l. 2 | `\unsure{d'où noyaux}` | `d'où noyau` | No final *x*. | medium |
| 48 | 47 | diagram (D) | `\unsure{\varepsilon_i}` | `\varepsilon_i\,\deleted{\illegible{1}}` | ε_i, followed by a heavily struck mark. | medium |
| 49 | 48 | right of the boxed f_E; next line | `\margin{[\uline{\illegible{1}}]}` and `\unsure{tenant du} choix d'un isom` | `[\deleted{\unsure{dép.}}\inserted{s'explicite} en termes du choix d'un isom` | "[" is followed by "s'explicite", written over a struck "dép", then "en"; the next line reads "termes du choix". CSG, IUT, CK: "[s'explicite en termes du choix d'un isomorphisme". Item a) is thus parallel to b) on scan 49. | high |
| 50 | 48 | left margin | `\deleted{\illegible{2}}` | `\deleted{\unsure{correspondant}}` | One long struck word. | low |
| 51 | 49 | l. 2 and l. 3 | `\unsure{\nu_{i'}\|\gamma_{i'}}` (twice) | `\nu_{i'}` | A v-shaped ν in both places, matching the ν of scan 48. | medium |
| 52 | 49 | margin at d) | `$\alpha_{i'}$ décrit` | `$(\alpha_{i'})$ décrit` | α_{i′} is in parentheses. | medium |
| 53 | 50 | second tuple | `\unsure{f'\|g'}` | `f'` | A large f with a prime; no g bowl. | high |
| 54 | 50 | second tuple, last entry | `(\alpha'_{i'})` | `(\unsure{\alpha'_{i'}\|\alpha'_i})` | The subscript shows *i* without a clear prime, as in the first tuple. CSG, IUT: (α′_i). | low |

Counts: 54 changes, 11 high, 33 medium, 10 low.

## Places still unresolved (30)

1. 41, l. 1: "donnée des commutativités" (kept) against "la donnée de commutation" in the witnesses. The word has three ascenders, which favours *commutativités*, and the short word before it may be "de" or "des".
2. 41, l. 6: the struck word before "tels que".
3. 41, last two equations: ρ or p in front of (β_{i′}) (insertion and struck start) and in the boxed formula. The inserted glyph is a closed loop with a short tail, like ρ. The boxed one is an R-shaped overwriting. The margin restatement on scan 42 has a straight-stemmed p, and all witnesses read p.
4. 41, tuple: the overwritten subscripts of f_{D*} and α_{D*D}.
5. 42, l. 1: "homs"; the struck word after "dans un".
6. 42, left margin: the marks before "savoir"; the token before "dans" (E′_{i′}?); ρ_i or p_i before (E_i).
7. 42, right margin: ψ or φ; "sur"; Ũ or Ũ_i; "avec"; the closing parenthesis is missing in the ink.
8. 42, main text: the w-shaped mark, crossed stroke and dot before "posé" (read "où on a" with the witnesses).
9. 42, main text: the dotted sign between "et" and "la face" (i.e. or où).
10. 42, prism: the overwritten β_{i′} under p_i and a second overwritten mark near the arrowhead into Γ.
11. 43: the overwritten symbol in Γ′_{i′} = Im(…) (Ξ-like; the witnesses leave a blank).
12. 43: "à un Π_U connexe" (kept) against the witnesses' "aux Π_U connexes".
13. 43, 47, 48: k or κ on π → E, and the K/k after the struck mark on scan 47.
14. 43: "indexé" (kept) against "indexés".
15. 44: d_i or d_{i′} inside k_i∘(d·id_{T(K̄)}) and in the margin's "d L_i". The prime is not visible; the first-pass d_{i′} is kept.
16. 44: "?!" or "??" after "Mais α unique".
17. 44, right margin: Im(f k′_{i′}) or Im k′_{i′}; L′_{i′} after int(β_{i′}^{-1}); "même".
18. 45: "0-morphisme" or "homomorphisme"; in the oblique margin "entier", "positif" and five unread words before "constants".
19. 45, vertical margin: "commutatifs"; "définir" or "écrire"; k̄ or k; T_K or 𝒯_K.
20. 45, last line: the structure of "compatibles avec α_{D*U}, (β_{D*U}) et avec α_{Ue}, (β_{Ue}), ~~et avec~~" (possible parentheses).
21. 46, l. 7: "d'isom. défini mod. iso. int." (a light "défini"-like word may precede "isom.").
22. 47: "par l'action de Γ" (kept). The witnesses read "via"; the end of the previous line has a struck "pa…".
23. 47: the ≃ in T(K̄) ≃ Ker p_i may end in an arrowhead.
24. 48: π or π′ and I or I′ in D′; "au système de diagramme" (kept) against the witnesses' "aux systèmes de diagrammes".
25. 48: inner "[" or "(" before "un autre choix".
26. 49: Γ or Γ′ in c); I or I′ in d).
27. 49: Ũ′_{i′} (kept) — the prime on U is not certain.
28. 50: p′_{i′} or f′_{i′} on the top row of the exact-sequence map.
29. 50: α_{i′} or α_i in the first tuple.
30. 50: the initial of "compatibilité" is written over a tall stroke, perhaps a started *f*. The reading of the word is secure.

## Witnesses' own errors

| Scan | Witness | Reading | Ink |
|---|---|---|---|
| 41 | CSG, IUT, CK | "dans le diagramme" | "dans les diagrammes" |
| 41 | CSG, IUT, CK | "fD1, FU" in the tuple | f_D, f_U |
| 41 | CK | "fi′′ ◦ κ′i′ (i = τi′)" | f_{i′}∘k′_{i′} = k_i (the "= k_i" dropped) |
| 41 | CK | "γi−1 p(β−1i′ αγi′′)" | γ_i^{-1}·(ρ\|p)(β_{i′}^{-1})·αγ′_{i′} (parenthesis misplaced) |
| 42 | CSG, IUT | "On peut supposer" | the abbreviation "OPS" |
| 43 | CSG, IUT, CK | "Conjecture bordélique précisée" | "Catégorie bordélique précisée" |
| 43 | CK | "Ses objets" | "Ces objets" |
| 44 | CSG, IUT | int(β_{i′})^{-1} f(E_{i′}) "=" E_i | ⊂ |
| 44 | CSG, IUT, CK | κ_i ∘ (d_i, id_{T(K)}) | k_i ∘ (d · id_{T(K̄)}) (a product dot, not a comma) |
| 44 | CSG, IUT, CK | "Je me a'perçois" | "Je m'aperçois" |
| 45 | CSG, IUT | "quintuplés" | "quintuplets" |
| 45 | CSG, IUT, CK | μ_U : f_U −∼→ g_U | μ_U : f_U → g_U (plain arrow; only μ_{D*} has ≃) |
| 46 | CSG | "l'objet référence de Πe" | "l'objet-repère de Π_e" |
| 46 | CSG, IUT, CK | "et un isomorphisme λi" | "et des isom λ_i" |
| 47 | CSG, IUT, CK | "s'insèrent dans une famille" | "s'insérant" |
| 47 | CSG, IUT, CK | "un homomorphisme de suites exactes" | "des homs de suites exactes" |
| 48 | CSG, IUT, CK | "un homomorphisme f de D′ dans D" | "un 1-morphisme f" |
| 49 | CSG, IUT | box "αi′ ∈ Γ (i′ ∈ I′)" | α_{i′} ∈ 𝓔 (required by ρ_i f_{i′} = int(α_{i′}) f_𝓔 ρ′_{i′} and β_{i′} = p(α_{i′})α) |
| 49 | CSG, IUT | "c), d) ensemble" | "c, d ensemble" |
| 50 | CSG, IUT | "la fonctorialité de f◦i′" | "la compatibilité de f^0_{i′}" |
