# LM_C4-191-209 (scans 191–209): second-pass changes

I checked the first pass line by line against both halves of every scan (`second_pass\img_140-4\scan191…209_a/_b`).
The lower half of scan 192 is blank paper. My enlarged crops are in `second_pass\work_LM_C4-191-209` (`c191_*` …
`c209_*`). The files `A1_191-192.jpg` … `J1_209.jpg` dated 10 Nov in that folder come from an earlier attempt; I did not
use them. For the notation of (8) I also looked at `scan188_b.jpg` (the definition (5) in the previous package).

Witness coverage: none. These scans are § 52 (folios 743–752); the CSG draft, the IUT text and the Carmona–Kuenzer text
stop earlier. I searched for « discrétification », « hom de Lie », « Enveloppe schématique », « quasi-unipotent »,
« irrédondance », « Galois-Teichmüller », « Autext », « Cas profini », « L'avenir le décidera », « Réflexion faite » and
« situations extrêmes »; the only hits are other passages. The author's table (`Grothendieck_Circle_tableLM.txt`,
l. 271–279) lists « 52. Approximations de Lie des systèmes de Galois-Teichmüller 737 », « 2°) Cas profini 744 » and
« 3°) Approximation de Lie des systèmes de Galois-Teichmüller 748 », which agrees with the headings on folios 744 (scan 193)
and 748 (scan 201). The ink alone decides.

Conventions taken from the neighbouring packages: the small zigzag superscript is `\unsure{\natural|\sharp}`
(LM_C4-153-171, checked); the germ classes are written with Latin k, as in the first passes of scans 188–190 and 210.

The checked file compiles (pdflatex, draft mode) in a minimal wrapper that defines the edition macros. A word-level diff
against the first pass shows only the changes below.

Counts: 29 changes (3 high, 17 medium, 9 low); 17 places unresolved.

| # | Scan | Place | First pass | Corrected | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 191 | line 3, article before the struck prefix | `\unsure{des\|de}` | `des` | Same d–e–final-hook shape as « des » two lines below (« ce sont des »); the sentence begun on scan 190 is « appeler les groupes Π … des L-T-groupes ». Crop c191_deleted_meta. No witness. | medium |
| 2 | 191 | line 3, struck prefix under « L-T- » | `\deleted{\unsure{méta-}}` | `\deleted{méta-$L$-}` | The strike runs through « méta-L- »: é, t, a, then an L with its dash, all under one stroke, before « groupes »; « L-T- » is written above. Scan 190 has the struck « M'inspirant de la terminologie "métabélienne" », so the first name was « méta-L-groupes ». Crop c191_deleted_meta. | medium |
| 3 | 193 | (8), name of the map | `\unsure{K_i^{\mathcal{G}}\|\kappa_i^{\mathcal{G}}}` | `k_i^{\unsure{\natural\|\sharp}}` | The superscript is the small zigzag, not a script G (his 𝒢 is the large looped capital of (6)). The symbol is identical with (5) on scan 188, « (k_i^♮)_{i∈I} de germes d'hom. extérieurs … k_i^♮ : T → Π », which (8) carries over to the profinite case; scans 190 and 210 write k_i for its members. Crop c193_k8b, compared with scan188_b. | medium |
| 4 | 193 | the two struck interlinear trials after « une » | `\deleted{\unsure{0-conn.}} \deleted{\unsure{0-connexe}}` | `\deleted{\unsure{0-connexe}} \deleted{\unsure{0-conn.}}` | On the page « 0-connexe » stands left (under « soit M ») and « 0-conn. » right (under « une »); the first pass had them in reverse order. Readings unchanged. Crop c193_conn. | medium |
| 5 | 194 | struck word after « de groupe G) » | `\deleted{\unsure{tel\|et}}` | `\deleted{\unsure{et\|tel}}` | A short word ending in a crossed t; no l is visible. Crop c194_schema. | low |
| 6 | 194 | « qui ___ un(e) schéma » | `\unsure{soit\|est}` | `soit` | Four letters, his tall initial s and a final crossed t, as « soit » on scan 193; « est » would begin with a small e loop. Crop c194_schema. | medium |
| 7 | 194 | « laquelle ___ néc. » | `\unsure{sera\|ser.}` | `ser.` | The ink is « ser » with a point; the first pass preferred an expansion. The same abbreviation recurs on scan 205 (row 22). Crop c194_schema. | medium |
| 8 | 195 | « un corps ___ » | `\unsure{quelcon-que\|quelconque}` | `quelconque` | The « dash » is his flat final stroke of n: « on » in « on aura » two lines lower is a single dash. It is mid-line, not a hyphenation. Half image scan195_a. | medium |
| 9 | 196 | line 1, article before the replaced « schéma » | `la` | `\unsure{la\|les}` | The word is l, an e loop and a crossing final stroke: either « les » or « le » overwritten to « la » after « schéma » became « multiplicité »; a plain « la » is not what the ink shows. Crop c196_la2. | low |
| 10 | 197 | « est la "courbe … universelle" » | `est la courbe … universelle''` | `est la ``courbe … universelle''` | A double tick stands before « courbe »; it opens the quotation that « universelle" » closes. Crop c197_courbe. | medium |
| 11 | 197 | insertion above the struck « (qui se ramène d'ailleurs essentielle- » | `\inserted{et au cas d'une multiplicité}` | `\inserted{et au cas \unsure{$1$-multi.\|d'$1$ multi.} \illegible{1} relatif}` | Six words: « et », « au », « cas », a 1 followed by « multi » (his m looks like w, as in « multiplicité » on scan 193), an unread word beginning with d, and « relatif » (final f with ascender and descender). « relatif à un corps de base k » agrees with « cas ». The d' left of the 1 belongs to the struck « d'ailleurs » below. Crops c197_insert2–6. | low |
| 12 | 197 | the hom « ___ : T → 𝓜 » | `\unsure{k_i\|\kappa_i}` | `k_i` | The same letter as in (8) and (5) (row 3); nothing in his hand supports a Greek κ. Crop c197_classe. | medium |
| 13 | 197 | « appartenant à un des ___ » | `$\unsure{K_i^{\mathcal{G}}\|\kappa_i^{\mathcal{G}}}$` | `$k_i^{\unsure{\natural\|\sharp}}$` | Same symbol as (8) (row 3): the germ class of which k_i is a member (scan 190: « les germes d'hom k_i … de la classe k_i^♮ »). Crop c197_classe. | medium |
| 14 | 198 | « et un ___ » before (15) | `\unsure{hom\|lacet}` | `hom` | Looped h, o, then m humps; no crossed t, unlike « lacets » on the same page. Half image scan198_a. | medium |
| 15 | 198 | (15), twice | `\unsure{k\|\kappa}` | `k` | Same letter as rows 3 and 12. Half image scan198_a. | medium |
| 16 | 199 | « pour tout ___ corps K » | `\unsure{bon\|\deleted{bon}}` | `\deleted{bon}` | A horizontal stroke runs through the middle of the whole word and past it, like the stroke through « de car. 0 » after K; both restrictions are struck. Crop c199_bon. | medium |
| 17 | 201 | « Si G_Q provient ___ un schém. » | `de un` | `d'un` | The ascender of the d curls over to the right as his apostrophe; there is no e after the d. Crop c201_dun2. | medium |
| 18 | 202 | (25), « pour presque ___ ℓ } » | `\unsure{\forall\|\mathrm{tt}}` | `\unsure{\mathrm{tt}\|\forall}` | Two parallel uprights joined by one crossbar (H-shaped), his « tt » (tout); a ∀ has converging strokes. Crop c202_tt. | low |
| 19 | 203 | NB after (31), abbreviation | `\unsure{ops\|qps}` | `\unsure{oPS\|ops}` | A bowl joined to a stem that rises (no descender), the top of the stem curling into a P bowl, then a capital S: « oPS », on peut supposer (the IUT witness prints the abbreviation « O.P.S. » elsewhere, l. 4331). q is excluded. Crop c203_ops. | low |
| 20 | 204 | NB, « les hyp. 1°) ___ 4°) » | `\(1^\circ):4^\circ)\)` | `\(1^\circ)\) à \(4^\circ)\)` | A dot with a slanted accent over it, his compressed « à » (as « à un corps » on scan 197). Crop c204_a4. | medium |
| 21 | 205 | line 3, « un ___ distingué Π » | `un \deleted{\unsure{définissant la \(LT\)-structure\|définissant la \(LT\)-struct.}} distingué` | `un \inserted{sous-groupe} \deleted{définissant la \(LT\)-\unsure{struct.\|structure}} distingué` | « sous-groupe » is written small just above the struck « définissant la LT-struct. » at the end of the line and is not struck; the first pass dropped it. The struck phrase was moved: « définissant la LT-structure de 𝓜 » follows two lines later. The doubt on the deleted ending is kept in shorter form. Crop c205_sg. | high |
| 22 | 205 | NB, « en cas particuliers importants ___ 𝒢_0 = Π_0 » | `on` | `\unsure{ser.}` | s, e, r and a point, the same form as « ser. » on scan 194 (row 7); there is no « on ». Crop c205_imp2. | low |
| 23 | 205 | after the inserted « son adh. » | `\(\unsure{\widehat{\mathcal{G}}_0\|\mathcal{G}_0^{*}}\)` | `\(\mathcal{G}_0^{\deleted{\unsure{\wedge\|*}}}\)` | The mark at the upper right of 𝒢_0 (he writes the hat after the letter, as in « Π_0^ » under (32)) is crossed out; with « son adh. » inserted and « =dfn 𝒢 » added, the closure no longer needs it. Crop c205_adh. | medium |
| 24 | 205 | (32), top middle | `\unsure{\widehat{\mathcal{G}}\|\mathcal{G}^{*}}_{\unsure{\deleted{0}\|0}}` | `\mathcal{G}^{\deleted{\unsure{\wedge\|*}}}_{\deleted{\unsure{0}}}` | Both the superscript mark and the subscript of the upper 𝒢 are blotted out; the annotation beneath, « = 𝒢_0^ » (hat and 0), is intact. The object is 𝒢, the closure named in the text. Crop c205_G32. | low |
| 25 | 206 | inserted qualifier of « groupe de Teichmüller … discret » | `\inserted{``absolu''}` | `\inserted{``direct''}` | The quoted word begins with d and ends with a crossed t: d-i-r-e-c-t; « absolu » has neither. « Groupe de Teichmüller "direct" » is the author's term on scan 187, and it matches (33) Π = Π^+, 𝒢 = 𝒢^+. Crop c206_direct. | high |
| 26 | 206 | insertion « 𝒩 ⥲ Γ est » | `…\Gamma$, est}` | `…\Gamma$ est}` | No comma between Γ and « est ». Crop c206_enfait. | low |
| 27 | 206 | « le groupe fondamental ___ schéma ou de la dite multiplicité » | `\deleted{de cette} schéma` | `dudit \deleted{\unsure{cette}} schéma` | « dudit » (d-u-d-i-t) is not struck; the strike starts after it, over a short word with two tall letters. « dudit schéma ou de la dite multiplicité » is the parallel the sentence needs. Crop c206_dudit. | medium |
| 28 | 207 | « de ___ multiplicité modulaire » | `\unsure{la\|leur}` | `\unsure{leur\|la}` | After the l come an e loop and three humps, more than « la ». Crop c207_leur. | low |
| 29 | 207 | « multiplicité modulaire ___ » | `universelle` | `convenable` | c-o-n-v-e-n-a-b-l-e: an 8-shaped b before the final l and e, no dotted i, no double l. It fits case b), which admits subgroups of finite index of the Teichmüller group (insertion on scan 206). Crops c207_conv, c207_conv2. | high |

## Places still unresolved

1. Scans 193, 197, 198: the case of the letter k (written k, as on scans 188–190 and 210) and the superscript zigzag
   (`\natural|\sharp`).
2. Scan 194, (10) and (11): U or M in Π_1(·, G; a) (overwritten capital; the mathematics needs U).
3. Scan 194: « une|un » before the replaced « courbe algébrique »; « quasi-projectif|quasi-projective ».
4. Scan 196: « la|les » before « multiplicité modulaire » (row 9).
5. Scan 196: « 1|L »-multiplicités.
6. Scan 196: whether the last « catégorie » is underlined; the stroke may be the tail of the g.
7. Scan 197: the fourth and fifth words of the insertion (« 1-multi. » or « d'1 multi. »; an unread word before
   « relatif »).
8. Scan 197: the sign between ν and Q in Π_1(U_{g,ν} … _Q) (struck Q or ξ).
9. Scan 197: 𝓜 or 𝒜 for the LT-group (overwritten).
10. Scan 198: L or T in « le normalisateur de L ».
11. Scan 200: the mark after « unipotents » in (21) (« ) » or « , »).
12. Scan 201: « etc.|et » (overwritten); whether « le » before « groupe des points adéliques » is struck.
13. Scan 205: the abbreviation « ser. » in the NB; the exact struck decorations of 𝒢 in (32) and after « son adh. ».
14. Scan 206: « Donc » and « idem|item »; the struck « Γ|k en fait »; « int. ».
15. Scan 207: the subscript « Q̄_0 » of Γ.
16. Scan 208: the end of the margin note (« cette structure »).
17. Scan 209: the struck « Je vais|vois réfléchir|rappeler ».

## Witnesses' own errors

None noticed: no witness transcribes scans 191–209. The author's later table titles 3° « Approximation de Lie des
systèmes de Galois-Teichmüller » (l. 277), while the heading in the ink on folio 748 is « Enveloppe schématique d'un
T-L-groupe profini : a) Les hom. admissibles. » This is the author's later retitling, not a transcription error.
