# LM_C4-229-247 (scans 229–247): second-pass changes

I checked the first pass line by line against both halves of every scan (`second_pass\img_140-4\scan229…247_a/_b`).
The lower half of scan 237 is blank paper. My enlarged and rotated crops are in `second_pass\work_LM_C4-229-247`
(`c229_1` … `c247_2`). The `m229.png` … `m232b.png` files dated 10 Nov in that folder come from an earlier, unfinished
attempt; I did not use them.

Witness coverage: none for the text. The CSG draft, the IUT text and the Carmona–Kuenzer text stop before § 53 (ms. pp.
760–771). I searched for « Malgoire », « germe résiduel », « germes d'espaces », « filtre impropre », « bons cas »,
« Germesp », « scindée », « involutif », « amalgam », « radiolog », « homéomorphe à R », « D∞ » and « ST1,1 »; the hits
are other passages. The author's table (`Grothendieck_Circle_tableLM.txt`, § 53) lists « 2°) Les groupes GL(2, R)±1~,
SL(2, R)~ 761 », « 3°) Le groupe GL(2, Z)~ 763 », « 4°) L'isomorphisme GL(2, Z)~ ≃ ST1,1 766 » and « 5°) Digression sur
les revêtements des germes d'espaces, … 768 ». This agrees with the headings on scans 231, 238 and 242 and with the page
numbers 762–771. The ink alone decides.

Conventions kept from the first pass: its macros and layout, including the printed footer block (folio, URL, address)
it gives at the end of each scan. That footer is not on the archive-resolution images; I left it as the first pass
has it. The circle of half-lines is 𝕊 (row 1), the letter the first pass of LM_C4-210-228 uses for the same object on
scans 225–228; it is not the curled 𝔖 of the other C4 packages.

The checked file compiles (pdflatex, draft mode) in a minimal wrapper that defines the edition macros.

Counts: 20 changes (4 high, 13 medium, 3 low). Row 1 covers 4 places.

| # | Scan | Place | First pass | Corrected | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 229, 233 | the circle of half-lines: « rev. universel de 𝕊₀ pointé » and (11) (229); « l'action de τ sur 𝕊₀ », « 𝕊̃₀ ≃ ℝ » (233) | `\unsure{\mathbb S_0\|\mathfrak S_0}`, `\unsure{\widetilde{\mathbb S}_0\|\widetilde{\mathfrak S}_0}` | `\mathbb S_0`, `\widetilde{\mathbb S}_0` | An S with an extra vertical stroke on its left: the doubled-stroke form of ℝ, ℤ and 𝕌 on the same lines. It is not the curled 𝔖 (a G-like curl with an inner hook) of the C4 packages. The first pass of LM_C4-210-228 writes 𝕊ᵢ, 𝕊₀ for this circle. No witness. | medium |
| 2 | 230 | Dém., the cancelled phrase that « l'image inverse 𝕌~ » replaces | `\deleted{\unsure{au dessus de}}` | `\deleted{\unsure{au dessus de} $\mathbb U$}` | The strike line runs on through a hatched 𝕌 after « dessus de ». The raised 𝕌~ at the end of the line belongs to the insertion (crop c230_4). No witness. | medium |
| 3 | 230 | lower-left margin, « au centre {±1} … Sl(2,ℝ) » | `\{\pm1\}\unsure{\subset\|\text{ de }}` | `\{\pm1\}$ de $` | After {±1} stands a d with an ascender, crossed by the vertical separator line, not an open ⊂ (rotated crop c230_4). No witness. | medium |
| 4 | 231 | Proposition, last line | « est isomorphe à ℤ » | « sont isomorphes à ℤ » | The verb is s–t, as « sont » elsewhere, and the adjective ends in -phes (crop c231_3). The subject « L'image inverse … des sous-groupes » is singular; the plural is the author's. No witness. | medium |
| 5 | 231 | proof of the Corollaire, « ℨ ⊂ 𝕌 » | `\unsure{\subset\|\in}` | `\subset` | An open c without the middle bar of his ∈ (compare « t ∈ ℝ » two lines below). No witness. | medium |
| 6 | 233 | before « Considérons l'image inverse de {1,τ} » | — | `\unsure{i)}` | A short stroke with a small circle above it and a closing parenthesis stand at the start of the line (crop c233_3); the first pass omits them. They look like an item number « i) »; no « ii) » follows in this package. No witness. | low |
| 7 | 233 | (22), end of the first line | `\exp(\unsure{\pi it\|\pi i}-2i\pi t)` | `\exp(\pi it-2i\pi t)` | After « πi » stands a crossed t identical to the t of « 2iπt » (crop c233_3, 3.5×). The formula as written is a slip of the author: −z̄ = exp(πi − 2iπt); the next line, exp 2iπ(1/2 − t), is right. No witness. | medium |
| 8 | 235 | last line, « en m'inspirant … de Sl(2,ℤ) » | « du formulaire » | `\unsure{du formulaire\|des formulaires}` | The article looks like d-e-s rather than d-u, and the noun may end in s (crop c235_2). Not settled. No witness. | low |
| 9 | 236 | (33), second row, between « r̃_∞ =^{dfn} » and « = r̃₀σ̃⁻¹ » | `\deleted{\unsure{\widetilde\sigma\widetilde r_0}}` | `\unsure{\widetilde\sigma\,\widetilde r_0}` (live) | Heavy retracing: the σ, the r, the 0 and both tildes keep their shapes. Deletions on these pages are zigzag hatching, as under (34) on 237. The second « = » needs a left member, and the row repeats (30), « r_∞ = σr₀ = r₀σ⁻¹ », as row 1 repeats « r₁ = ρ⁻¹r₀ = r₀ρ ». By (24), σ̃r̃₀ = r̃₀τ̃′(σ̃) = r̃₀σ̃⁻¹. Crops c236_1, c236_2. No witness. | medium |
| 10 | 237 | (34), struck brace under the two factors | `\deleted{\unsure{\text{amalgamée}\|\underbrace{\hspace{9em}}_{\omega_0}}}` | `\deleted{\underbrace{\hspace{9em}}_{\unsure{\omega_0}}}` | The hatched zigzag is a brace from under ρ̃ to under σ̃. Its hatched label is a short token the size of « ω₀ », far too short for « amalgamée » (crop c237_1). No witness. | medium |
| 11 | 239 | (39), index of Aut ext | `\unsure{\mathrm{loc}\|\mathrm{lac}}` | `\mathrm{lac}` | ℓ, a round a, c: the same index as « Aut_lac(Π₁,₁) » in (41) and in the display after it on 240 (crop c239_1). Autext_lac is the author's notation; his table writes « Autextlac(π) » (§§ 15, 18, 35). No witness covers the page. | high |
| 12 | 241 | last sentence, the loop in quotation marks | ``` ``\unsure{radiologique}'' ``` | ``` ``rectiligne'' ``` | The word has the shape of « rectilignes » in « les chemins rectilignes » four lines above: re-cti-li-gne, two i-dots, a g with a loop (crop c241_1). It describes the drawn ℓ′₀: a straight segment from a towards 0, a small circle round 0, and back. No witness. | high |
| 13 | 242 | insertion « (au moins dans … "bons cas") » | « dans les » | « dans des » | Both words after « moins » begin with a d (crop c243_3, row 7). The main text of 243 has « dans les bons cas »; this insertion does not. No witness. | medium |
| 14 | 243 | upper-left margin note | « cela ne fait pas \unsure{aller} \unsure{loin\|long} ? » | « cela \unsure{a été} fait par Olivier Leroy ? » | Rotated crops c243_1–c243_3. Line 2 is clear: « par Olivier Leroy ? » (O-l-i-v-i-e-r with two i-dots, L-e-r-o-y, the question mark at the top right). Line 1 is « cel… », a short group I cannot read with certainty, then « fait ». The note stands beside the « topos limite projective des (petits) topos étales ». No witness. | high |
| 15 | 243 | (48), second line of the gloss | « valeur E » | « valeur \unsure{E\|\Phi} » | The last sign is a loop crossed by a vertical with a foot, the Φ of « Rev(S, Φ) » in the same display, not the printed E of « E ↦ » (crop c243_3, row 2). The sense requires E, the value of the constant covering. | low |
| 16 | 243 | condition 1°, « ce qui …, si S est loc. connexe, … ∀S_i ∈ Φ » | « ce qui s'exprime, … par ∀S_i ∈ Φ » | « ce qui signifie, … que ∀S_i ∈ Φ » | The verb has two descenders (g, f), as in « Ceci signifie que » above. The word before ∀ is the q-u of « que (S, Φ) » at the start of the previous line (crop c243_4). No witness. | medium |
| 17 | 243 | left margin by condition 1° | « que le germe d'espaces est non vide » | « que ce germe d'espaces est non vide » | The article has no ascender: « ce » (rotated crop c243_3, row 4). No witness. | medium |
| 18 | 243 | end of condition 2° | « soit triviale. » | « soit trivial. » | The word ends in l and a period, with no final e (crop c243_3, row 5). It agrees with « l'hom. ext. ». No witness. | medium |
| 19 | 245 | residual germ, « (il est vide ssi Y est ouvert) » | `\unsure{ssi}` | « ssi » | The same three-s group as « connexe ssi » and « i.e. ssi » on 247, which the first pass reads without doubt. No witness. | medium |
| 20 | 247 | number of the last display | `(\unsure{55\|53})` | `(55)` | Two identical digits in the long-s shape his 5 takes (noted in LM_C4-153-171); a 3 would have two bumps. (53) and (54) precede on 246–247. | high |

## Places still unresolved

- 229: the subscript of u (𝕊¹ ?); « revêtement » or an abbreviation before « exponentiel »; the struck word after (12)
  (« s'écr. »?); the struck « Propo » and « contra ».
- 230: « sous-g. inv. »; the digit in « Sl(2,ℝ)~ » of Cor. 1 (2 written like a loop); the struck « qui », « dernier »,
  ℝ, « can. » and the struck sign before ω′₀ in Cor. 2.
- 231: below (16), the replacement map reads n ↦ ω₀ⁿ, and a heavy hook from the struck row above may be a prime
  (ω′₀ⁿ). Mathematically the kernel generator is ω′₀ (notes, M2). Also « SPS »; ℨ or 𝔷; the struck upper map.
- 232: the struck « distinct de | ≠ » and « l'unique »; « vaut »; L̃_ρ or L_ρ in the lower-left margin.
- 233: the overwritten denominators in exp(πi/4) (4 over 8?) and in (23) (8 over 4?); the struck « d'une façon » and
  « de la »; « un gr. »; the − in the margin « τ(x+iy) = −x+iy »; the « { » after exp in (22); the extra « ) ».
- 234: « aussi | ainsi »; the struck word before « dans »; Π or π; the struck exponent in the first underbrace.
- 235: « central »; « des | de » 5; the struck label and the struck token after « τ̃′² = » in (28); « élément »;
  « avec | en »; r₁ or σ₀ for the middle element; « du formulaire | des formulaires ».
- 236: D_σ̃ (a ρ may lie under the σ); the argument of j; « somme ».
- 237: the struck exponents on r̃₀ and the struck « = » in (34).
- 238: « différentiablement | différentiellement » (the second line looks like « -tiellement »; the author's table
  has « Action différentielle » for 1°); the struck symbol before X₁; U₁,₀ as written.
- 239: « 1°) » and the retraced letter after it; the struck mark between S and 𝒯; the struck ω's in a) and b); a comma
  or a semicolon before « τ̃′² = 1 » in a).
- 240: « -lacets »; « ! » at the end of the NB; the superscript on U′₁,₁; the struck « de S ».
- 241: the signs in the vertex labels a∓e₁, a−e₀∓e₁, a∓e₀; « classe »; « compose ».
- 243: the short group in the margin (« a été »?); « ess! | ess^t »; ¹E or Ẽ; « valeur E | Φ ».
- 244: strokes through « S » and « germe » in « à tt espace S, le germe (S, Φ) »; « induit | induite »; the struck word
  after « top. ».
- 245: in the margin square (52), whether the arrow between Germ and Gerres has two heads, « Gerres », and the words
  « On a un diagramme de morphismes canoniques »; « dans | ds ».
- 246: « mais pour [quoi | qui] il me faut faire »: after « mais » stand p, a short group, a q-group and « il me »; the
  phrase is not settled. The struck subscript of Φ.
- 247: « Germesp »; « toujours | tjrs »; « rev! | rev. »; « 1-connexe | 1. connexe »; « du germe » or « des germes »
  after « au dessus ».

## Witnesses' own errors

None noticed: no text witness covers scans 229–247. In the author's table the extraction lost the tildes and the « ≃ »
(« ST1,1 GL(2, Z) »), and the 5°) title reads « revêtements des germes d'espaces » where the ink heading has « les
[revêtements de] germes d'espaces ». These are a later title and an extraction artefact, not errors of reading.
