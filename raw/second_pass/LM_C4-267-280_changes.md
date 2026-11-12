# LM_C4-267-280 (scans 267–280): second-pass changes

I checked the first pass line by line against both halves of every scan (`second_pass\img_140-4\scan267…280_a/_b`).
The lower half of scan 280 is blank paper apart from the foliation 279. My enlarged crops are in
`second_pass\work_LM_C4-267-280` (`c266_end.png`, `c267_1` … `c280_1`); the evidence column names them. The
`m267_0.png` … `m280_0.png` crops dated 10 Nov in that folder come from an earlier, unfinished attempt; I did not use them.

Witness coverage: none. The CSG draft, the IUT text and the Carmona–Kuenzer text stop near manuscript p. 300 (the
cross-ratio λ, (79)–(80)). I searched them for « corrélation », « Revuni », « Teichmüller spéciaux », « interprétation
différentielle », « anabélien », « 1-connexe », « J'admets », « relation grossière », « transport de structure »,
« germes de surfaces », « convergence compacte » and « produit fibré sur G »; the only hits (CSG l. 4098 and 4111,
« convergence uniforme / compacte de u et de son inverse »; § 25, l. 5912 ff.) are other passages. The author's table
(`Grothendieck_Circle_tableLM.txt`, l. 281–295) lists § 53, « Le groupe de Teichmüller spécial ST_{1,1} ≃ GL(2, Z) et le
groupe SN_{1,1} » (p. 760), whose item 5°, « Digression sur les revêtements des germes d'espaces, et relations entre
germes topologiques et germes différentiables des surfaces » (p. 768), contains these pages (781–787); the table's
« ST » agrees with the « S𝒯 » of scan 280. The ink alone decides.

Context used: the end of scan 266 (« satisfaisant la condition de compatibilité, s'expri- », crop `c266_end`) and the
definition of Ep(A), the « épaississement » of an arc, on scan 264 (first pass of LM_C4-248-266).

Other points.
- Footers: the images carry no printed archive footer. The first pass's footer `\margin` blocks were left as they are,
  as in the other checked packages.
- Conventions kept: the first pass's `\unsure{\mathbb S|\mathcal S}`, `\unsure{\mathbb D|D}` and `\unsure{\mathrm{Revuni}}`
  marks, its `\unsure{\overline{\mathrm m}|=}` for the barred-m sign (« même »), and its layout of the displays.
- Compilation: with the pipeline wrapper `answers\fixed\build\wrap.tex` (xelatex), the first pass and the checked file
  stop at the same place: scan 270, (118), where an `array` stands inside `\diagram` inside `\[…\]`. With `\diagram`
  defined as `\ensuremath{#1}` both compile without errors (7 pages). The markup was left as the first pass has it.

Counts: 20 changes (2 high, 10 medium, 8 low). Rows 3, 6 and 12 are one correction at three places.

| # | Scan | Place | First pass | Corrected | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 267 | first line, before « par la commutation des diagrammes » | `\unsure{voit\|vient}` | `\unsure{mant\|me}` | Scan 266 ends « s'expri- » (`c266_end`), so this word ends it. At 4× (`c267_3`) it is a flat m-stroke, a dot, a dash and a small closing loop: more than « me » needs, so « mant » (s'exprimant) comes first. There is no v. No witness. | medium |
| 2 | 267 | label of the display before (109) | `(\unsure{108\|100})` | `(108)` | At 2.5× (`c267_1`) the last digit is a closed double loop, unlike the open middle 0. The labels run (107), (108), (109); (100) is H(A) → H(A′) of scan 265. | high |
| 3 | 267 | (110), second row, argument of D_x^{*~} | `E_{\unsure{f\|\rho}} A` | `\unsure{\mathrm{Ep}\|E_p}A` | At 4× (`c267_3`) a lowered p hangs from the E: a descender with a small bowl and no ascender, so not f. Ep(A) is the « épaississement » of A defined on scan 264; scan 271 writes it with a full p (row 13). The alternatives are the form of the preceding package. | medium |
| 4 | 267 | « un groupe comm. T (=T_x) » | `$T$` | `$\unsure{T\|\overline T}$` | The top stroke of this T runs far to the left of the stem, much longer than the bar of the T in « (=T_x) » and in « T-groupoïdes » below (`c267_4`). The first pass marks the same form `\unsure{T\|\overline T}` on scans 276–277; the preceding package writes the orientation module T̄_x. | low |
| 5 | 268 | (113), subscript of Hom | `\underline{\mathrm{Tors}}(\unsure{G\|T})` | `\underline{\mathrm{Tors}}(\unsure{T\|G})` | At 3× (`c268_1`): an open curl, then a stem with a top bar and a hooked foot, the hooked T of « Tors » itself; the curl may be an abandoned G. (112) and the first row of (113) have Tors(T). | low |
| 6 | 269 | « … les T_x-torseurs S_x^~(A) et D_x^{*~}(…) » | `E_{\unsure{f\|\rho}}(A)` | `\unsure{\mathrm{Ep}\|E_p}(A)` | The same lowered p as in row 3 (half `scan269_a`, l. 9). | medium |
| 7 | 269 | upper target of the two forgetful functors before (117) | `\unsure{\mathbb{S}}_x^{\sim}` | `\unsure{\mathbb{S}}_x^{\unsure{*\sim\|\sim}}` | At 3.5× (`c269_3`) a small star joined to the tilde stands there, like the star of D_x^{*~} just below. The same slip « S_x^* » is in « Les corrélations entre S_x^* et D_x^{*~} » above (first pass `\unsure{*\|\sim}`, kept). | low |
| 8 | 271 | « d'où la bijection canonique … (120) — » | `\unsure{attendue}` | `\unsure{cherchée}` | At 2.5× (`c271_4`) the word is two groups, each opening with the c-h ligature that looks like a d: « cher » and « chée ». There is no double t for « attendue ». | medium |
| 9 | 271 | next line, before « qui donne en particulier (96) » | `\deleted{\unsure{de}}` | `\deleted{\unsure{des}}` | At 5× (`c271_4`): d, e and a final s, inked over. | low |
| 10 | 271 | (123), first line, lower of the two struck items after « de u » | `\deleted{\unsure{isom.}}` | `\deleted{\unsure{associés}}` | At 3.5× (`c271_3`) the struck word has the form of « associés » in « associés par (120) » on the next line, where the author rewrote it after the two maps. | medium |
| 11 | 271 | (123), « A′ ∈ … son image par u_𝕊 » | `\unsure{\mathcal{A}'_x\|\mathcal{A}_{x'}}` | `\mathcal{A}'_x` | At 3× (`c271_2`) the prime stands at the top right of the A; the x below it has none. | medium |
| 12 | 271 | (123), « β la section de D_x^{*~} sur … associée par la corrélation h_x » | `\unsure{E_p(A)\|E_\rho(A)}` | `\unsure{\mathrm{Ep}\|E_p}(A)` | At 3× (`c271_2`): the lowered p of row 3, joined to the E. | medium |
| 13 | 271 | (123), « β′ la section de D_{x′}^{*~} sur … déduite de β » | `\unsure{E_p(A')\|E_\rho(A')}` | `\mathrm{Ep}(A')` | At 3× (`c271_2`) a full lowercase p with its bowl stands on the line after the E: « Ep(A′) ». | high |
| 14 | 273 | « … structure différentiable (C_1) au voisinage … I. Soit G » | `au voisinage de $I$` | `au voisinage \unsure{des\|de} $I$` | At 2.5× (`c273_2`) the word has d, e and the final curl of an s. « de I » two lines higher is a single letter. | low |
| 15 | 274 | struck words after « opère trivialement sur I, », under the insertion « Alors G̃ s'exprime » | `\deleted{et \unsure{On va supposer}}` | `\deleted{et Quitte à \illegible{1}}` | At 1.5× (`c274_1`) the struck words are « et », « Quitte » (the form of « Quitte à remplacer » at the top of the page) and the accented-i « à »; the next word, a W-like group with a descender, is illegible. | medium |
| 16 | 274 | the next struck line and its parenthesis | `\deleted{\unsure{quitte\|encore} à un sous-groupe ouvert plus petit (d'indice divisant $2^{\unsure{\operatorname{card}I\|\operatorname{Card}I}}$) …}` | `\deleted{encore à un \unsure{sous-groupe} ouvert plus petit (d'indice divisant $2^{\operatorname{card}I}$) …}` | « Quitte » is on the line above (row 15), so this line begins « encore ». The exponent has the small c of « card » (`c274_1`). A zigzag cancellation covers the middle of the line, so « sous-groupe » now carries a doubt mark. | medium |
| 17 | 274 | last line, « on est ramené au cas où … = 1 » | `\operatorname{Card}` | `\operatorname{card}` | At 2× (`c274_1`) the c has the height of the a, as in the exponent of row 16. | medium |
| 18 | 274 | same place, the letter after « card » | `I` | `\unsure{I\|S}` | An S with a vertical stroke through it (`c274_1`), not the serifed I of « sur I » above: an I written over S, or the author's S (he alternates I and S for the marked set on these pages). | low |
| 19 | 275 | « on peut supposer que Δ_{x,1} soit un … » | `disque ouvert` | `\unsure{disque ouvert\|disques ouverts}` | (`c275_1`) Both words end in s-strokes, as in the cancelled « des disques ouverts » at the top of the page; the plural looks copied by slip. | low |
| 20 | 276 | « J'aurai pris soin de prendre … stable par u ↦ u⁻¹ » | `$U$` | `$\unsure{U\|\widetilde U}$` | At 4× (`c276_2`) a short thick wave stands above the U, smaller than the tildes of Ũ on the page. U comes first: with Ũ, « ce qui implique qu'il en est de même de Ũ » would say nothing. | low |

## Places still unresolved

56 places, most of them first-pass doubts that the ink does not settle; the doubt marks stay in the checked file.

- 267: the first word, mant or me (row 1); « ess^t. » and « const^t »; the endings of the underlined « Revuni »
  (Revuni, Revuniv or Revunis; the same on scans 268–269); S̃ written over H in the left member of (110).
- 267–280: the alphabet of the circle and disc letters (𝕊 or 𝒮, 𝔻 or D); the preceding package writes 𝕊_x and plain D_x^*.
- 268: the inked-over symbol after F_1 in (114); the stroke before G_1; résulte or résultent; the overwritten Isom in (116).
- 269: sous or sur T_x; the slip « S_x^* »; the two letters in Corr_x(𝔛) = Corr_x(X); « couples » under « triples ».
- 270: passer; the stray « a » in the second triple; Or; the struck « fonctorialité des constructions ».
- 271: the hatched word at the start of the second line of (123) (first pass « On »); the upper struck item (u_𝕊?).
- 272: barred m or = (« du = coup », « elle est la = pour A et A′ »); the struck « caract. ».
- 273: the connectors « ou » or ∼, « ou » or - in (124)–(125); the cancelled mark after « Soit G »; a stray C before
  the inserted « (C_1) »; des or de (row 14).
- 274: the illegible word after « Quitte à » (row 15); « = que »; the blot after the cancelled parenthesis; I or S (row 18).
- 275: the struck parts of (131); « suite décr. » (the first struck word could also be « fond^t », système fondamental);
  un or une; soit or soient; the subscript of the source in u|Δ_{x,1}^* : Δ_{x,?}^* → Δ_{x,0}^* (a b-like 1); row 19.
- 276: p_1 or p_i; the struck « Je suppose »; On aura or J'aurai; T or T̄; row 20.
- 277: 1-connexe; tte; ℤ^I or T^I in (139) (a Z and a T superposed); 𝒯 or τ.
- 278: the small a or α after Sp𝒯; pris; I or S at the end.
- 279: the mark on p_1 in (144); trans or tras.
- 280: the struck words above « voie différentielle » (construit or explicite, par); voire or voie; G or G̃ and T_I or
  T̄_I in the insertion; S𝒯 or Sp𝒯.

## Witnesses' own errors

None noted: no witness covers scans 267–280.
