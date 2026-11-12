# LM_C4-039-057: second-pass changes (scans 39–57)

**Pages.** These scans are §51 "Exemple: la tour de Fermat", 2) "Z_{ρ,σ}: version provisoire" (from scan 41) and
3) "Les groupes O_N^*" (from scan 51). Upper numbers 667 (scan 39), 668 (41), 669 (43), 670 circled (45), 671 (47),
672 (49), 673 (51), 674 (53), 675 (55), 676 (57); lower numbers 38–56.

**Witness coverage.** No text witness reaches these pages. CSG and IUT end with §37; Carmona–Kuenzer ends at the §49
heading. Searches for distinctive words of the package found nothing: "vaseux", "trente six", "maladresse", "densité
schématique", "parfait en son genre", "quatre cas de signes", "Z/12", "section ensembliste", "schéma en Modules". The
ink alone decides. The Grothendieck Circle table was used for section titles and page numbers only: §51 at p. 664,
2) at p. 665, 3) "Les groupes O_N^* et variantes" at p. 673, 4) "La suite 1 → N^{0+}_{ρ,σ} → N_{ρ,σ} → O*_{12} → 1" at
p. 677.

**Other points.**
- Footers: the images in `img_140-4` carry no printed archive footer. The first pass's footer `\margin` lines were left
  as they are.
- Compilation: the first-pass file stops at the first tikz-cd inside a macro argument with `answers/fixed/build/wrap.tex`.
  The checked file stops at the same place, and compiles (12 pages) once the pipeline's `fix_tikzcd_in_macros.py` has
  been run on a copy (35 diagrams get `ampersand replacement`). That repair was not written into the output, so the
  markup stays the first pass's.
- Crops are in `second_pass/work_LM_C4-039-057`; the evidence column names the crop file. Margin notes were rotated
  (scan 41 by −60°, scan 48 by −33°, scan 49 by −50°).

| # | Scan | Place | First-pass reading | Corrected reading | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 39 | (25), parenthesis after β = β₀τ^{ν₂} | `(\unsure{\beta\|\beta_0}\in\Gamma\underline M)` | `(\unsure{\beta_0\|\beta}\in\Gamma\underline M)` | c039_1_beta: the β ends in a small closed loop at the lower right, the same subscript-0 loop as in β₀τ^{ν₂} on that line. The loop is attached, so the doubt stays. | low |
| 2 | 39 | (26), "i.e. · de (21)" | `\text{i.e. membre de (21)}` | `\text{i.e. \unsure{membre} de (21)}` | c039_3b_ie: a flat run, one ascender, a short tail. "membre" fits but is not secure. Doubt added. | low |
| 3 | 39 | (27) a), "ζ · de la forme" | `\text{\unsure{localem.} de la forme}` | `\text{localement de la forme}` | c039_4_localem: "loc·l" followed by the long horizontal "-ment" stroke, as in "localement" of b) two lines below. There is no abbreviation point. | medium |
| 4 | 40 | insertion after "automorphismes" | `\inserted{i.e. des \uline{épimorphismes}}` | `\inserted{i.e. des épimorphismes}` | c040_2_partout: the stroke under "épimorphismes" runs on and curves down to the insertion point "(—" after "automorphismes". It is the insertion line, not an underline. | medium |
| 5 | 41 | line after (31): "L'équation · , en α₀,β₀" | `L'équation du lacet,` | `L'équation des lacets,` | c041_3_lacets: d-e-s with the end hook of s, and "lacets" with t and a final s before the comma. "du lacet" on scan 39 (c039_6_lacet1) is written d-u, with no s. | medium |
| 6 | 41 | diagonal margin note, "· bien · …" | `\unsure{épi}\ldots` | `épi\ldots` | c041_9_margin_rot: é-p-i with its accent, then the three dots. | medium |
| 7 | 41 | same note, verb before "bien" | `\unsure{est}` | `\unsure{soit\|est}` | c041_9_margin_rot: four letters, beginning with a descending s. "est" would begin with a loop. Doubt kept. | low |
| 8 | 41 | "comme un · de L₀" | `\unsure{normalisateur\|normaliseur}` | `normalisateur` | c041_8f_sharps: n…l·s, a short a, a tall t, then -eur. "normaliseur" has no t. | medium |
| 9 | 41 | "(ou M_{ρ,σ}^·)" | `\mathcal M_{\rho,\sigma}^{\unsure{\sharp}}` | `\mathcal M_{\rho,\sigma}^{\unsure{\natural\|\sharp}}` | c041_8f_sharps: a slanted zigzag, unlike the crossed # on L₀ in the line above. It is the sign written on the script G in (40) on scan 44 (c044_1_eq40). | low |
| 10 | 42 | (35), first line | `&=\alpha-\rho(\alpha_0)+\nu_3\lambda_1` | `&=\alpha_0-\rho(\alpha_0)+\nu_3\lambda_1` | c042_5_eq35: the first α carries the same small o as the α₀ in ρ(α₀). (45) on scan 45 has α₀ in the same formula. | medium |
| 11 | 43 | display u(λ₀), fourth member | `\underbrace{l_0^{2\nu}}_{\lambda_0^{2\nu}}` | `\underbrace{l_0^{(2\nu)}}_{\lambda_0^{2\nu}}` | c043_1_l02nu: the exponent is written in parentheses, (2ν), like l₀^{(μ)} before it. The label below has none. | medium |
| 12 | 43 | display u(λ₁), third member | `=((\unsure{\zeta\|\xi}\rho u)(\lambda_0))` | `=(\unsure{\zeta\|\xi}\rho u)(\lambda_0)` | c043_2_ulambda1: one parenthesis before ζ and one after λ₀. The outer pair is not in the ink. | medium |
| 13 | 43 | "savoir le schéma en groupes · (heuristique) engendré par ρ,σ" | `libre` | `\unsure{lisse\|libre}` | c043_3_libre, c043_4_lisse: a looped l, i, then s-shaped letters with no ascender. "libre" would show the tall b. Compare "lisse" on scan 41 (c041_11_lisse). "libre" stays as the alternative because the context leads one to expect it (notes). | low |
| 14 | 45 | last line: "sont justifiés (· là où ils ont un sens, i.e. …)" | `(\unsure{car maintenant} \unsure{là où ils ont un sens}` | `(\unsure{au moins} là où ils ont un sens` | c045_3_aumoins: after the parenthesis comes a short word a-u, then a five-letter word with an i-dot ending in -ns ("moins"). "maintenant" would be twice as long and end in t. The next line, "là où ils ont un sens, i.e., pour u_𝔊 et λ ∈ M)", is clear. | medium |
| 15 | 47 | "On aura ensuite …", display u(λ₁), third member | `=((\unsure{\zeta\|\xi}\rho u)(\lambda_0))` | `=(\unsure{\zeta\|\xi}\rho u)(\lambda_0)` | c047_1_ulambda1: as in row 12. | medium |
| 16 | 47 | (51), right column: "d'où μ = ·" | `\unsure{4\nu'+2+\nu_2\|4\nu'+2\nu_2+1}` | `4\nu'+2+\nu_2` | c047_2_mu: "4ν' + 2 + ν₂", with a distinct plus between 2 and ν₂. The ink settles the literal reading. It is a slip for the 4ν'+2ν₂+1 of scans 42–43 (notes R20, N1). | high |
| 17 | 48 | (54), middle term | `\underline Z_{\rho,\sigma}` | `\widetilde{\underline Z}_{\rho,\sigma}` | c048_3_eq54: a tilde stands over the middle Z, like the tilde of Z̃^{+0} to its left. The sequence is the kernel sequence of Z̃_{ρ,σ} → G_m×μ×μ from (53). | medium |
| 18 | 49 | (57), sign between the two sets | `\unsure{\simeq\|\Vert}` | `\simeq` | Half image: a wavy stroke beside a straight one, the ≃ turned upright, as in (73) on scan 53. | medium |
| 19 | 51–57 | ring-scheme letter, 33 places: 𝕆_N, 𝕆_N^*, 𝕆_1, 𝕆_1^*, 𝕆^*, 𝕆_{12}^*, underlined 𝕆_{12}^* | `\unsure{\mathcal O_N\|\Phi_N}` and `\unsure{\mathcal O_N^{*}\|\Phi_N^{*}}` (scans 51–52); `\unsure{\mathbb O_{..}\|\mathbb D_{..}}` (scans 53–57) | `\mathbb O_N`, `\mathbb O_N^{*}`, `\mathbb O_{12}^*`, `\underline{\mathbb O}_{12}^*`, … | c051_1_ON, c051_3_heading: a round oval whose left side is doubled by an inner upright, the hand-drawn blackboard O. Φ would need the upright through the middle and beyond the oval; 𝔻 would need a straight left side. The same letter appears on every page. The author's table of contents (Circle witness) names the section "Les groupes O_N^* et variantes" (p. 673) and writes O*_{12} (p. 677). | medium |
| 20 | 51 | "Je dis qu'il y a · 𝕆_N une structure" | `\unsure{sur\|dans}` | `\unsure{dans\|sur}` | c051_2_dans: d-a-n with an ascending d. A horizontal stroke runs through the word and may be a strike (see unresolved). | low |
| 21 | 52 | (68), last term in the bracket | `\lambda\unsure{\lambda'\|\lambda}` | `\lambda\lambda'` | c052_1_eq68: the second λ carries a prime at its top right. There is no N before the product (notes R34). | medium |
| 22 | 57 | Proposition, "ν',ν'' (à valeurs dans ·)" | `\mathbf G_a` | `\unsure{\mathbb O_1\|\mathbf G_a}` | c057_1_valeurs: a heavy oval with an inner upright and subscript 1, perhaps written over an earlier G_a. On the line above, the author writes {0,1}_{S₀} ⊂ G_a = 𝕆₁. | low |

**Counts:** 22 changes (high 1, medium 14, low 7), of which row 19 is one systematic change at 33 places.

## Places still unresolved

1. 39, (26): "i.e. \unsure{membre} de (21)" (row 2).
2. 39, parenthesis below (27): "mais dépend \unsure{apparemment} de ν₃". The word is a dot, a W-shaped group on the base
   line, a dot and a long "-ment" stroke (c039_5b_pour). "évidemment" fits as well as "apparemment". The struck word
   before "), mais" (`\unsure{pour|$\nu_3$}`) is also left open.
3. 40, "pour le premier, \uline{partout} \deleted{\unsure{car. 2}}\inserted{(en tte caractéristique)} pour le second".
   Above the end of the line stands a word r·t.–2 over a short struck word (en?). The next line begins with a struck
   "car" (c040_2b–2e). Whether the upper word is "partout", and whether its line is an underline or a strike, is not
   settled.
4. 41, "il me semble --- \unsure{ça coince|se corse} en car. 2 et 3". The second word is c, a round letter, flat strokes
   and a tall final letter (c041_5c_coince). Neither alternative accounts for the tall letter.
5. 41, "en \unsure{m'interdisant|n'utilisant} \unsure{encore un} groupe". The first word of the next line has an i-dot,
   so "ancien" or "aucun" are possible (c041_7c_aucun).
6. 41, the insertion "\unsure{à la fois|de façon}" (c041_8e_fois). The superscript on L₀, a crossed #, is kept as
   `\unsure{\sharp}`.
7. 42, first line: "D'où le \deleted{…} (schéma \deleted{et) groupe}". The closing parenthesis inside the deletion is
   not visible, and the struck words after "(schéma" may be "en groupes" (c042_1_doule).
8. 42, (33), second line: a †-shaped mark after (β₀−σ(β₀)) and a small mark under ω^{ν₂} (c042_3_usigma) are not
   transcribed. They may be multiplication points or insertion marks.
9. 42–48, the ornate group letter (`\unsure{\underline C^{+}|\underline G^{+}}`), left as the first pass has it. The
   second pass of C3-606-624 (scan 616) reads the same looped letter as calligraphic 𝒢.
10. 39–47, the parameter letter (`\unsure{\zeta|\xi}`), left as it is. The Circle table prints the §48 II title as
    "L'équation ζ = η λ₁^{(μ−1)}", while the second pass of C3-568-586 read the same ʃ-shaped letter as ξ.
11. 44, (40): the superscript on G (`\unsure{G^{\sharp}|G^{\natural}}`). It is the zigzag of row 9.
12. 45, the struck opening sentence ("note que u définit un hom au … d'indice de 3"), and whether its second line is
    struck (c045_4_top).
13. 47, "ce qui \deleted{\unsure{signifie}}": the struck word is short, e-t followed by q (et qui? et que?)
    (c047_3_revient).
14. 48, "(qui est \uline{mono.} \unsure{?} en car. ≠ 2,3)".
15. 51, "il y a \unsure{dans|sur} 𝕆_N". If the horizontal stroke through the word is a strike, no replacement is
    written (row 20).
16. 55, the three struck lines before (79): the middle line and the final symbol, β or (78) (c055_1_struck).
17. 57, "(à valeurs dans \unsure{\mathbb O_1|\mathbf G_a})" (row 22).
18. Overwritten signs left with doubt marks: (31) both rows, (32), the first sign in (61), (85), the sign before 3ν₂ν₃
    in (86), and "μ = 1∓2ν₂+4ν'" in the scan-50 margin. The mathematics favours particular readings (notes R25, R47,
    N1, N2), but the ink does not settle them.

## Witnesses' own errors

No witness text covers scans 39–57, so no readings could be collated. Two remarks on the Circle table:
- 51, Circle table: "3) Les groupes ON∗ et variantes". The heading on the page reads "3. Les groupes 𝕆_N^*." with no
  "et variantes". This is the later table's wording, not a misreading.
- 57 (p. 677, beyond this package), Circle table: "O1∗2". This is a text-extraction garble of O*_{12} (the 𝕆_{12}^* of
  scans 55–57).
