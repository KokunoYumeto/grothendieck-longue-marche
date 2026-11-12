# LM_C4-153-171 (scans 153–171): second-pass changes

I checked the first pass line by line against both halves of every scan (`second_pass\img_140-4\scan153…171_a/_b`).
The lower half of scan 155 and most of scan 170 are blank paper. My enlarged crops are in `second_pass\work_LM_C4-153-171`
(`c153_*` … `c171_*`, `c_checks1.png`). The `s15*_*.png`/`s16*_*.png` crops dated 10 Nov in that folder come from an
earlier, unfinished attempt; I did not use them.

Witness coverage: none. The CSG draft, the IUT text and the Carmona–Kuenzer text stop before § 51. I searched for
« infiniment divisibles », « paramètre elliptique », « force du poignet », « isogénies de Kummer », « aurais envie de
penser », « linéairement indépendants », « groupe de décomposition », « cyclotomique universelle » and « torseur des
racines »; nothing matches, and the only « Hurwitz » (CSG l. 7049) is another passage. The author's table
(`Grothendieck_Circle_tableLM.txt`, l. 265–269) lists « 14°) Relation avec les Jacobiennes généralisées 720 »,
« 15°) Interprétation de Γ_Q → N_σ … Ẑ*·Ẑ, 725, et digression sur les extensions kummeriennes » and « 16°) Réflexions
sur le théorème de Fermat 733 ». This agrees with the headings on scans 156 and 171. The ink alone decides.

I took these conventions from the checked neighbouring packages. The small slanted zigzag written as a superscript on
N_σ, G_ρ,σ and M_ρ,σ is `\unsure{\natural|\sharp}` (LM_C4-096-114, (218)–(219), the displays that (325)–(326) here
cite). The curled capital is 𝔖 (LM_C4-001-019, row 2; LM_C4-115-133, row 1). Digit forms: his 6 is σ-shaped (346, 356)
and his 5 has a long-s shape (345, 355).

The checked file compiles (pdflatex, draft mode) in a minimal wrapper that defines the edition macros.

Counts: 20 changes (1 high, 12 medium, 7 low). Row 5 covers 13 places, row 7 covers 4 and row 10 covers 5.

| # | Scan | Place | First pass | Corrected | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 154 | Remarque, « sous-groupe de H⁰(S, J) des éléments "infiniment divisibles" » | `H^0(S,\unsure{\mathcal J})` | `H^0(S,\mathcal J^{\unsure{0}})` | A small 0 sits at the upper right of the script J, as in « H⁰(S, J⁰) » of (324) two lines above. I moved the doubt onto the 0. No witness. | low |
| 2 | 154 | « de type fini sur Z — p.ex. » | `sur $\mathbb Z$` | `sur \deleted{\unsure{$\mathbb Q$}} $\mathbb Z$` | At the end of the line, after « sur », a small Q has a stroke through it. « Z » begins the next line. No witness. | low |
| 3 | 155 | item 1° | `\unsure{trirevêtement\|trivêtement}` | `trirevêtement` | The word has two syllables (tri-re-) before -vêtement. S′ is the degree-3 étale cover given by the points of order 2. No witness. | medium |
| 4 | 155 | item 2° | `le` | `Le` | A capital looped L, unlike the « le » of item 1°. | medium |
| 5 | 156–158, 160 | the superscript on N_σ (heading of 15°, (326), the embedding on 157, (328), (329), the insertion and the cancellation on 158, 160), on G_ρ,σ ((325), 157 ×2, (328)) and on M_ρ,σ^∼ (156) | `\unsure{\leftrightarrows}` (156–157), `\unsure{\leftrightarrows\|\sharp}` (158, 160) | `\unsure{\natural\|\sharp}` | It is the same small slanted zigzag throughout. LM_C4-096-114 writes it ♮\|♯ on G_ρ,σ and N_σ in (218)–(219), which (325) and (326) cite. « Opposing arrows » was a shape description, not a symbol of the text. | medium |
| 6 | 156 | (325), top right | `\unsure{\mathcal G}^{+\wedge}` | `\mathfrak S^{+\wedge}` | A curled capital with an inner hook (crop c156, panel 3). This is Grothendieck's Fraktur S, as settled in LM_C4-001-019 and LM_C4-115-133. LM_C4-096-114 writes the same group as Ẑ*·𝔖^{+∧} in (218). | medium |
| 7 | 156–157 | the cancelled superscript after ♮ on N_σ ((326), 157) and on G_ρ,σ (157 ×2) | `\deleted{\unsure{\sim}}` | `\deleted{\unsure{\mathrm{ab}\|\sim}}` | The hatched cluster is wider than a tilde and shows two letter loops. LM_C4-096-114 reads the same cancelled superscript of N_σ in (219) as « ab ». | low |
| 8 | 157 | « l'hom (3?3) apparaît comme le composé » | `(\unsure{313})` | `(\unsure{313\|323})` | The middle digit is fused with the 3 and may be a 2. The display numbers on scans 153–156 were overwritten. On scan 156 the text calls the first hom « (322) », but its display is (325), so the numbers moved up by 3. The hom meant here is (326), which would earlier have been (323). | low |
| 9 | 158 | (328), left vertical arrow | `\arrow[d,"\kappa_{1/2}"']` | `\arrow[d,hook,"\kappa_{1/2}"']` | The shaft starts with a hook (∫ then ↓), like the right vertical arrow, and the same map is drawn ↪ with κ_{1/2} on scan 157. | medium |
| 10 | 158, 160 | N_σ in (328), (329), the insertion « dans N_σ… », the cancelled « dans N_σ ⊂ Ẑ*·M̲ », and on 160 | `\unsure{N\|\mathcal N}_{\sigma}`; in the cancellation `\unsure{N\|\mathcal N}^{…}` without σ | `N_{\sigma}`; `N_{\sigma}^{…}` | The N is the same as on 156–157, where the first pass already writes N_σ. In the cancelled phrase the subscript σ stands under the N (lower half of 158). The N of N^{!ét} in (328) keeps its doubt. | medium |
| 11 | 159 | « La fibre … de U_n au ledit point » | `au` | `en` | The short word after U_n is e + n (both halves; crop c159d), not a + u. | medium |
| 12 | 159 | the insertion above « fibre » | `\unsure{géo.}` | `\unsure{géom.\|géo.}` | The insertion ends with a minim after « géo », so « géom. » is possible. | low |
| 13 | 160 | number of the first display | `\tag{\unsure{336\|330}}` | `\tag{336}` | The last digit is his σ-shaped 6 (loop below, tail to the upper right), as in (346) and (356). A 0 would be a closed oval. The next display is also (336), so the manuscript repeats the number. | medium |
| 14 | 160 | the parenthesis after « pour simplifier » | `(on se restreindra au cas …)` | `(on \unsure{sera\|se r.} ici \unsure{réduit\|restreint} \unsure{au} cas …)` | « ici » stands clearly between the short word and the long word (crop c_checks1, panel 1). The first pass dropped it, and its order « se restreindra » does not fit the ink. The long word has a tall stroke, a dotted i and a flat ending. | low |
| 15 | 161 | (339) and (340), the last arrow A_S → 1 | `\arrow[r,dash]` | `\arrow[r]` | Both rows end « A_S → 1 » with an arrowhead. | medium |
| 16 | 161 | « et par … à la lim← » | `\unsure{pass.}` | `\unsure{passage\|pass.}` | After « pass » comes a looped g-like letter, as in « par passage à lim← » on scan 153, where the first pass reads « passage ». | low |
| 17 | 165 | (352), arrows | every arrow with a head | `1 — Π₁⁺ — Π₁ →^{χ_Π} Ẑ*` over `1 — Hom_Z(A,T) → G_ζ — Ẑ*` | Only Π₁ → Ẑ* and Hom → G_ζ carry arrowheads; the other strokes are plain. | medium |
| 18 | 167 | the insertion after « S₁ normal » | `\inserted{conn.}` | `\inserted{$0$-conn.}` | Crop c167, panel 3, reads « 0-conn. », the « 0- » of « 0-connexe » (scan 161). | high |
| 19 | 167 | after « A = H⁰(S₁, G_m), » | `pour` | `posant` | This word has six letters and ends in a flat -nt stroke (crop c167b, panel 2). On these pages « pour » is a short three-stroke group. | medium |
| 20 | 168, 169 | « Π₁ = Gal(Q̄/Q) = Γ_Q »; (361) D_ℓ = Π₁(Q_ℓ, Q̄_ℓ) | `\unsure{\Pi_1\|\pi_1}` | `\Pi_1` | The same capital Π with a long top bar as every Π₁ on 161–167. | medium |

## Places still unresolved

- 153: the overwritten display numbers (318), (319), the cancelled (31?) and (321)–(322) (the first pass's readings
  are kept, with their doubts). Under J̃ = lim←: the first pass has both an index n and a left subscript n, and the ink
  may show only one n. In « cf (301) p. 719′ », the 301 may carry a prime.
- 154: the cancelled word before « "élémentaire" » looks like one word ending in -mé, not « un théorème ».
- 155: J⁰₀ with a cancelled subscript. The cancelled cluster carries a tilde and may be a struck X̃.
- 156: « Le premier hom. (322) »: the ink reads 322, but the hom meant is (325) (the shift of row 8). « p. 69? »: the
  last digit is 5-like. The superscript of N_σ in (326) and its cancelled part (row 7).
- 157: the page number 725 or 726. Ink: 72 followed by a 5-like digit; the sequence 725 (155) to 727 (159) wants 726.
- 158: the superscript after « ! » on M (∞ or ét); the subscript of N^{!ét} (ρβ, ρ3, or possibly 0,3); the last
  coordinate of the triple (1, retraced; mathematically it must be 1).
- 159: x_∞ⁿ = 1 or −1 in the first two lines of (332). The x₀ of the tuple in the second line is hatched and may be
  cancelled. The second factor is T_n(1/2) or T_n(−1/2). A squiggle after « quelc., » in the parenthesis.
- 160: « on a pour simplifier » and the parenthesis of row 14.
- 162: in (344), after the inserted « dans T∞(k̄*) », two short groups stand on the line (« une … une »?), where
  the first pass has one « une »; the first group may be something else.
- 164–165: the mark beside the right vertical arrows Ẑ* → Ẑ* of (349) and (352), read `\unsure{1}`. It may be the
  second stroke of a doubled (identity) shaft.
- 165–166: the J-shaped letter in « le cas où j est injectif », (350) and (355) 3°. It has no dot. Mathematically the
  map A → G_m(S) there is ζ, not the j of (347).
- 166: the insertion « en^h|en^t » before « en remplaçant »; « sps »; the raised letter in « ess.^{t|l} ».
- 167: « dimension 2|≥2 »; « qu'on a » (a q with a crossed tail = qu'); « en|ou un A′ »; « non can.^t|non can! ».
- 168–170: ξ or ζ for the Kummer parameter throughout; the twist (−1|1) of the joint map and of (359). In (358) and
  (365) the minus is clear.
- 169: (361) « = » or « ≃ » (heavily retraced).
- 171: the mark under ≃ in « Û₁ ≃ Û₀,₃ » (a short slashed double bar: * or ≠); 𝒰 or ℳ; the cancelled « totalement ».

## Witnesses' own errors

None noticed: no witness covers scans 153–171. On the author's table, the § 15° heading « Interprétation de Γ_Q →
N_σ » lost its superscripts in the text extraction, and « IΓQ » is an extraction artefact. These are not errors of
reading.
