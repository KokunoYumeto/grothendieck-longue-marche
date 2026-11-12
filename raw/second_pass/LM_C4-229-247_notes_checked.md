# LM_C4-229-247 (scans 229–247): research notes, checked

I checked each of the first pass's notes 1–68 (`answers\unzipped\LM_C4-229-247\LM_C4-229-247_notes.md`, § 5 and the
literature checkpoints) against the corrected text (`LM_C4-229-247_checked.tex`). Each is kept, corrected or dropped,
with the reason; none had to be dropped. My own notes follow as M1–M5. Scan numbers are filename scans; « changes, row n »
refers to `LM_C4-229-247_changes.md`.

## The first pass's notes

- **R01**: scan 229; implication not pursued. **Keep, sharpened.** Sl(2,ℝ) is homeomorphic to 𝕌 × ℝ² (Iwasawa
  decomposition KAN, K = SO(2) ≅ 𝕌, AN ≅ ℝ²), so its universal covering is homeomorphic to ℝ³ and contractible. This is
  what the proof on scan 230 uses.
- **R02**: scan 229, (13); own idea of the first pass. **Keep, settled.** Cor. 2 on scan 230 answers it: an element of
  determinant −1 inverts the kernel generator ω′₀, so (13) is not a central extension. Over the connected group
  Sl(2,ℝ), (14) is central.
- **R03**: scan 230; unproved claim. **Keep.** « s'identifie topologiquement à l'inclusion 𝕌 → 𝕌 × ℝ² » follows from the
  same decomposition, which also makes (15) a homotopy equivalence.
- **R04**: scan 230, Cor. 1; unproved claim. **Keep.** The proof is the « Corollaire (à la prop. p. 762) » on scan 231:
  conjugate the cyclic group into 𝕌 and read its inverse image in ℝ as (1/n)ℤ.
- **R05**: scan 230, Cor. 2; unproved claim. **Keep, sharpened.** An element of determinant −1 reverses the orientation
  of the circle of half-lines, so every lift of it conjugates the deck translation t ↦ t+1 into t ↦ t−1. This proves
  the statement for all such elements at once, not only for one reflection.
- **R06**: scan 230; own idea of the first pass. **Correct.** The « ∈ » of « exp 2iπt ∈ u » is consistent: through (11),
  z ↦ ℝ⁺z, u is read as a half-line (a point of 𝕊₀), and exp 2iπt lies on it. Nothing in the text needs review.
- **R07**: scan 231; question. **Keep.** « Je voudrais décrire Gl(2,ℤ)~ par générateurs et relations » is answered on
  scans 234–237: Theorem (25), Cor. 1 (28), Cor. 2 (34).
- **R08**: scan 231; unproved claim. **Keep.** « par conjugaison SPS que ℨ ⊂ 𝕌 »: a finite subgroup preserves an averaged
  scalar product, and an orthonormal basis for it with the same orientation gives a conjugating element of Sl(2,ℝ).
- **R09**: scan 231, Proposition; implication not pursued. **Keep; text corrected.** The proposition reads « … sont
  isomorphes à ℤ » (changes, row 4). The amalgam built from these inverse images is (31)–(32) on scan 236.
- **R10**: scan 232, (17)–(18); own idea of the first pass. **Keep, confirmed.** At 3× the exponents in (18) are 2n and
  3n with no minus sign (crop c232_4). Lifts of ρ, σ are ρ̃ω′₀ᵃ, σ̃ω′₀ᵇ with ω′₀ central, and (17) holds for them iff
  3a = −2b, i.e. (a, b) = (2n, −3n). The solutions do form a ℤ-torsor, but the action is (ρ̃ω′₀^{2n}, σ̃ω′₀^{−3n}); (18)
  as written has a sign slip.
- **R11**: scan 232, « Faire la vérification »; question. **Keep.** M1 carries the verification out.
- **R12**: scan 232, margin « il vaut mieux dire »; unproved claim. **Keep, sharpened.** The inverse image of L_ρ is ≅ ℤ
  and exactly one of its two generators lies over ρ (the other lies over ρ⁻¹ ≠ ρ). Which power of ω₀ its cube is
  depends on the sense in which ρ turns the half-lines; see M1.
- **R13**: scan 232, (19)–(20); own idea of the first pass. **Keep.** M2 applies it to the map under (16).
- **R14**: scan 233, « cette extension est scindée »; implication not pursued. **Keep, sharpened.** τ̃ : t ↦ 1/2 − t of
  (21) is an involution and, by Cor. 2, inverts ω′₀. So the inverse image of {1, τ} is ℤ ⋊ ℤ/2, an infinite dihedral
  group, like the groups D of scan 236.
- **R15**: scan 233, (22)–(23); own idea of the first pass. **Keep, corrected.** The ink of (22) has exp(πit − 2iπt)
  (changes, row 7); the correct member is exp(πi − 2iπt), and −exp 2iπt should be −exp(−2iπt). For τ′(z) = iz̄ the lift
  is τ̃′(t) = 1/4 − t; the written (23), 2iπ(1/8 − t), has a stray factor 2iπ and puts the fixed parameter 1/8 where 1/4
  belongs. The fixed point exp(πi/4) = (√2/2)(1 + i) is right.
- **R16**: scan 233, « Ceci résulte aussitôt de la prop. précédente »; unproved claim. **Keep.**
- **R17**: scan 234, Theorem (25); implication not pursued. **Keep, made precise.** With a = ρ̃, b = σ̃⁻¹ the presentation
  becomes ⟨a, b | a³ = b²⟩, the braid group B₃ (the group of the trefoil knot). The theorem is the classical
  identification of the inverse image of SL(2,ℤ) in the universal covering of SL(2,ℝ) with B₃; its centre is ⟨ω₀⟩ and
  the kernel to Sl(2,ℤ) is ⟨ω₀²⟩ = ⟨ω′₀⟩.
- **R18**: scan 234, « il suffit de montrer »; unproved claim. **Keep.**
- **R19**: scan 235, comparison of (27) with the exact sequence of Sl(2,ℤ)~; unproved claim. **Keep, settled.** The
  injectivity of ℤ → Π, not written in (27), follows from the comparison map: its composite n ↦ ω₀ⁿ into Sl(2,ℤ)~ is
  injective since ω₀ has infinite order. The five lemma then applies.
- **R20**: scan 235, « Je vais essayer de présenter … »; announcement. **Keep.**
- **R21**: scan 236, the three groups ≅ D_∞; unproved claim. **Keep, sharpened.** Infinite order of ρ̃, σ̃, ω₀ follows from
  (19)–(20) (ρ̃⁶ = ω′₀⁻¹, σ̃⁴ = ω′₀, ω₀² = ω′₀ with ω′₀ of infinite order); the inversion by τ̃′ is (24).
- **R22**: scan 236, (31)–(32); implication not pursued. **Keep.**
- **R23**: scan 236, (33); unproved claim. **Keep, updated.** The middle member of the second row is live (changes,
  row 9): r̃_∞ := σ̃r̃₀ = r̃₀σ̃⁻¹, true by (24) since r̃₀ = τ̃′ and r̃₀² = 1. Then r̃_∞² = σ̃·τ̃′(σ̃) = 1, and likewise r̃₁² = 1.
- **R24**: scan 237, Cor. 2 and (34); unproved claim. **Keep, checked.** From (33), r̃₀r̃₁ = r̃₀ρ̃⁻¹r̃₀ = τ̃′(ρ̃⁻¹) = ρ̃ and
  r̃_∞r̃₀ = r̃₀σ̃⁻¹r̃₀ = σ̃, so the underbraces of (34) carry the factors in the right order.
- **R25**: scan 237, (34); own idea of the first pass. **Keep, made precise.** Setting both factors equal to 1 gives
  ⟨r₀, r₁, r_∞ | rᵢ² = (r₀r₁)³ = (r_∞r₀)² = 1⟩, the Coxeter presentation of PGL(2,ℤ) as the (2,3,∞) triangle reflection
  group. (34) presents its extension by ℤ and keeps only the product of the two relations.
- **R26**: scan 238, « dont on sait que c'est un isomorphisme »; unproved claim. **Keep.** This is the isomorphism of
  the extended mapping class group of the once-punctured torus with GL(2,ℤ) through the action on H₁;
  orientation-reversing classes are included, since the target is GL.
- **R27**: scan 238, the tangent action; unproved claim. **Keep.**
- **R28**: scan 238, U₁,₀; own idea of the first pass. **Keep.** The ink has « il opère sur U₁,₀ » right after (36)
  defines U₁,₁; a slip of the author.
- **R29**: scan 239, Theorem; unproved claim. **Keep.**
- **R30**: scan 239, « (judicieusement ?) »; question. **Keep.** The point chosen on 241, a = (1/2, 1/2), is a 2-torsion
  point, fixed modulo ℤ² by −1, τ_∞ and τ′_∞ (not by ρ).
- **R31**: scan 239, (39); unproved claim. **Correct.** The index is « lac » (changes, row 11): Autext_lac(Π₁,₁), the outer
  automorphisms that respect the class of the loop round the puncture up to inversion. 𝒯₁,₁ ≃ Autext_lac(Π₁,₁) is the
  Dehn–Nielsen–Baer theorem for the once-punctured torus, orientation-reversing classes included.
- **R32**: scan 239, presentations a) and b); own idea of the first pass. **Keep, done.** R24 shows that b) follows
  from a) through (33).
- **R33**: scan 240, (41); unproved claim. **Keep.**
- **R34**: scan 240, « il faudrait expliciter l'action »; deferred calculation. **Keep.**
- **R35**: scan 240, ℓ′₀ kept or inverted; unproved claim. **Keep.**
- **R36**: scan 240, the principal covering with group ℤ²; implication not pursued. **Keep.**
- **R37**: scan 241, (42)–(44); unproved claim. **Keep.**
- **R38**: scan 241, « compose comme les fonctions »; implication not pursued. **Keep.** M5 applies the convention to
  the figure.
- **R39**: scan 241, « visiblement opposé »; unproved claim. **Keep, updated.** The loop is the « lacet "rectiligne" direct »
  (changes, row 12): a straight segment from a towards 0, a small circle round 0, and back, as drawn. M5 checks the sign.
- **R40**: scan 241, vertex labels; own idea of the first pass. **Keep.** With a = (1/2, 1/2) the upper-left corner is
  a − e₀ and the lower-right a − e₁; the labels read a∓e₁ and a∓e₀ (signs retraced), so the indices are interchanged.
- **R41**: scan 241, (43); own idea of the first pass. **Keep.**
- **R42**: scan 242, composition of germ morphisms; unproved claim. **Keep.**
- **R43**: scan 242, « sans doute », « bons cas »; expectation. **Keep; text corrected** to « (au moins dans des "bons
  cas") » (changes, row 13).
- **R44**: scan 242, (47) as a filtered 2-colimit; own idea of the first pass. **Keep.**
- **R45**: scan 242, the improper filter; own idea of the first pass. **Keep.**
- **R46**: scan 243, upper-left margin; question. **Correct.** The note reads « cela [a été] fait par Olivier Leroy ? »
  (changes, row 14): a question of attribution beside the « topos limite projective », not a doubt about the
  mathematics. It presumably points to Olivier Leroy's Montpellier work on the fundamental groupoid of a topos
  (« Groupoïde fondamental et théorème de van Kampen en théorie des topos », Cahiers Mathématiques Montpellier 17,
  1979; I give this reference from memory, to be checked).
- **R47**: scan 243, « a tendance à être multigaloisienne, voire galoisienne »; expectation. **Keep.**
- **R48**: scan 243, conditions 1° and 2°; unproved claim. **Keep; wording corrected:** « ce qui signifie, si S est loc.
  connexe, que ∀S_i ∈ Φ, ∃S_j … » (changes, row 16), « soit trivial » (row 18).
- **R49**: scan 243, order of quantifiers in 2°; own idea of the first pass. **Keep.**
- **R50**: scan 244, spaces as germs with the trivial filter; unproved claim. **Keep.**
- **R51**: scan 244, (49)–(50); unproved claim. **Keep.**
- **R52**: scan 244, « Si 𝒳 est 0-connexe »; implication not pursued. **Keep.**
- **R53**: scan 245, functoriality in the triple; unproved claim. **Keep.**
- **R54**: scan 245, « il est vide ssi Y est ouvert »; unproved claim. **Keep, settled.** The residual germ is empty iff
  some neighbourhood V of Y has V ∖ Y = ∅, i.e. iff Y is a neighbourhood of itself, i.e. iff Y is open.
- **R55**: scan 245, « le germe de X en x est tjrs 1-connexe »; implication not pursued. **Keep, sharpened.** It holds for
  every space X: a covering of a neighbourhood of x is trivial over a smaller one (local triviality), and a locally
  constant map is constant near x, so (48) is an equivalence for the germ at x. The residual germ keeps the monodromy
  round x.
- **R56**: scan 245, X = S ∪ {ω}; unproved claim. **Keep.**
- **R57**: scan 245, the topology on S ∪ {ω}; own idea of the first pass. **Keep.**
- **R58**: scan 246, universal covering of D*ₓ; implication not pursued. **Keep.**
- **R59**: scan 246, independence of the representatives; unproved claim. **Keep.**
- **R60**: scan 246, « à isom unique près »; own idea of the first pass. **Keep.**
- **R61**: scan 247, (54) fully faithful; unproved claim. **Keep.**
- **R62**: scan 247, the groupoid of universal coverings; unproved claim. **Keep.**
- **R63**: scan 247, last formula; unproved claim. **Keep;** the display is numbered (55) (changes, row 20).
- **R64**: scan 247, vertical margin note; implication not pursued. **Keep.**
- **R65**: scan 247, variance of the last formula; own idea of the first pass. **Keep.**
- **R66**: scans 230–231, 243; literature checkpoint (Hatcher, Thm 1.38). **Keep.**
- **R67**: scans 234–240; literature checkpoint (Farb–Margalit). **Keep, sharpened:** compare M3 with their description
  of the mapping class group of the torus with one boundary component as B₃.
- **R68**: scans 243–247; literature checkpoint (SGA 1, exp. V). **Keep.**

## My own notes

- **M1**: scans 232, 236; own idea (verification of the author's « Faire la vérification »). By (29)–(30), ρ = r₀r₁ =
  (0 1; −1 1) and σ = r_∞r₀ = (0 −1; 1 0). σ turns half-lines counterclockwise by a quarter turn and ρ clockwise by a
  sixth (ρe₀ = −e₁; the lower-left entries are +1 and −1). With t ↦ exp 2iπt and ω′₀ : t ↦ t+1, the generators above
  them therefore satisfy σ̃⁴ = ω′₀ and ρ̃⁶ = ω′₀⁻¹, hence σ̃² = ω₀ and ρ̃³ = ω₀⁻¹ with ω₀ the half-turn: exactly (20).
- **M2**: scan 231, (16); claim checked. The map ℤ → Gl(2,ℤ)~ under (16) must be n ↦ ω′₀ⁿ: the kernel of
  Gl(2,ℤ)~ → Gl(2,ℤ) is generated by ω′₀, while ω₀ maps to −1. The ink of the replacement map is ω₀ⁿ with a heavy hook
  above it that may be a prime (kept `\unsure`). In (27) on 235 the maps n ↦ ω₀ⁿ are right, because there the quotient
  is Sl(2,ℤ)/±1.
- **M3**: scans 234, 238–239; implication not pursued. On orientation-preserving classes the Theorem of 239 identifies
  S𝒯⁺₁,₁ with Sl(2,ℤ)~ ≅ B₃ (R17). This matches the classical isomorphism of the mapping class group of the torus with
  one boundary component with B₃, if the puncture is blown up to a circle of directions: the T₀-generator ω′₀
  corresponds to the boundary twist Δ⁴ and ω₀ to Δ². It gives an independent check of (25) and of the Theorem.
- **M4**: scan 235, Cor. 1 (28); implication not pursued. Since τ̃′ has determinant −1 and τ̃′² = 1, (28) exhibits
  Gl(2,ℤ)~ as the semidirect product of Sl(2,ℤ)~ ≅ ⟨a, b | a³ = b²⟩ by the involution that inverts both generators.
  The amalgam (32) of three infinite dihedral groups is another form of the same statement.
- **M5**: scan 241, figure and (40); own idea (check). With x, y the paths a → a+e₀, a → a+e₁ and composition « comme
  les fonctions », xyx⁻¹y⁻¹ runs y⁻¹, x⁻¹, y, x: down the right edge, left along the bottom, up the left edge, right
  along the top, as the arrows of the figure show. That is the boundary of the square round 0 turned clockwise, the
  opposite of the direct loop ℓ′₀; so [x, y] = ℓ′₀⁻¹, which is (40), [x, y]ℓ′₀ = 1.
