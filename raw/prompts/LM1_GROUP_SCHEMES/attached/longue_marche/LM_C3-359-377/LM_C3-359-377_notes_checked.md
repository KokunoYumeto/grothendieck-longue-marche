# LM_C3-359-377 — research notes, checked against the corrected transcription (scans 359–377)

Source: the first pass's research notes (answers/unzipped/LM_C3-359-377/LM_C3-359-377_notes.md, §5: R359.1–R363.2, the
unnumbered notes on scans 364–368, notes 1–14 on scans 369–373, R374.1–R377.2), each checked against
LM_C3-359-377_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude (second pass)** are new.
Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme), unproved claim, unpursued implication,
own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks (C1): 2×2 matrices; ρ(u) = ρuρ⁻¹; ε₀ = −σ⁻¹ρ, ε₁ = −ρσ⁻¹ (56); for invertible 2×2 A,
A⁻¹ = (Tr A − A)/det A, hence Tr A⁻¹ = Tr A/det A; in Π₀,₃ the loops satisfy ℓ∞ℓ₁ℓ₀ = 1, matching (64).

## Notes of the first pass

### Scans 359–363

- **R359.1 — scan 359 — unpursued implication — keep.** The criterion "the only sections satisfying (46) are zero" is
  stated over S; whether (43) is a monomorphism after every base change is the stronger question, and (43) lies before
  this package. The label (46) of 2ν = 0, ν² = 0 is now settled, so the cross-reference "qui satisfont (46)" is coherent.
- **R359.2 — scan 359 — own idea (first pass) — keep.** Over F₂[η]/(η²), λ = 1 + η gives λ² = 1 + 2η + η² = 1 and
  2λ = 2, with λ ≠ 1; checked.
- **R359.3 — scan 359 — unpursued implication — correct.** The computation it asks for is easy and done in note C359a
  below: in the coordinate S = T − 1 the group law is S ↦ S⊗1 + 1⊗S + S⊗S, so the isomorphism with the "schéma des nbs
  duaux … relatif au module Z/2Z" holds as schemes, not as group schemes with the additive law.
- **R360.1 — scan 360 — unproved claim — keep.** "Il se trouve que μ'₂S opère librement par translations" on the scheme of
  unipotents "(ou non)" of G and (47) for the regular ones are stated without proof. Freeness on points follows from
  359 (λε = ε forces λ = 1); the quotient statement (47) needs an fppf argument not given here.
- **R360.2 — scan 360 — conjecture (question) — correct.** In the corrected reading the vertical arrows of (48) carry ≀,
  so the diagram first asserts bijections Borels ⥲ one-parameter subgroups; the question "ne seraient pas injectives" doubts
  exactly these marks. Scans 361–362 give the other explanation, so the ≀ marks record the starting expectation, not the
  conclusion.
- **R360.3 — scan 360 — unproved claim — keep.** B = Norm(B_u) is said to be checked "à coups d'alg. lin. dans M"; the
  projective formula B̃ = Norm(B̃_u) is left (scan 361: "pas très trivial"). (49) is used again as a label on scan 362.
- **R361.1 — scan 361 — conjecture (proposed explanation) — keep.** The quantifier "qu'une|qu'aucune" remains doubtful in
  the ink; the "ne … pas" that follows favours "qu'une".
- **R361.2 — scans 361–362 — unpursued implication — correct.** The sign before "valeur" is now read m̄: "bien qu'ils
  aient même valeur pour t = 1". The point stands: evaluation at 1 does not determine the parametrised subgroup in PG, and
  the derivative at 0 (scan 362) separates the two.
- **R361.3 — scan 361 — own idea (first pass) — keep.** Checked: over R = F₂[η]/(η²), c(1 + tN) = 1 + t(1+η)N + tη in
  R[t] forces c = 1 + tη and then η(t² − t) = 0, false in R[t]; the two parametrisations differ in PG though they agree at
  t = 1.
- **R362.1 — scan 362 — own idea (first pass) — keep.** "Partout non nulle" must mean non-zero in every fibre, so that a
  coordinate of Ñ is locally a unit and νÑ = 0 gives ν = 0.
- **R362.2 — scan 362 — unpursued implication — keep.** The conclusion that one must give the parametrised subgroups
  ε̃₀, ε̃₁ in addition to ρ̃, σ̃ is the formulation of the Proposition on scan 363.
- **R363.1 — scan 363 — unproved claim — correct.** Uniqueness in "∃ uniques ε₀, ε₁" is the computation of scans 361–362
  (two lifts λε, ε give the same parametrised subgroup only if λ = 1); what the page leaves unproved is existence of a
  lift of the given parametrisation, locally on S.
- **R363.2 — scan 363 — unproved claim — keep.** The normalisation λ₀ = 1 "ce qui détermine ρ de façon unique en termes
  de σ, et inversement" is asserted; the item now opens "Soient(?) ρ, σ des relèvements de ρ̃, σ̃".

### Scans 364–368

- **Scan 364, items 4–5, (57)–(57′) — unproved claim — keep.** The trace criterion for fibrewise independence and the
  uniqueness under Tr(ρ + σ) = 1 (with lifts found "loc. fppf") are asserted, with a pointer to the proposition of
  p. 478′ (§48 VII).
- **Scan 364, Remarques 1, (58)–(59) — unpursued implication — correct.** (59) checked: ε′₀ = −ρ⁻¹σ = (−σ⁻¹ρ)⁻¹ = ε₀⁻¹
  and ε′₁ = −σρ⁻¹ = ε₁⁻¹. In the corrected reading "(ρ⁻¹, σ⁻¹) satisfait aux m̄s conditions", the symmetry then
  extends to inversion, which (60)–(63) treat.
- **Scan 365, (62) — unproved claim — correct.** The "calcul matriciel immédiat" checks: unipotence of ε₀ = −σ⁻¹ρ gives
  det ρ = det σ, and Tr ρ⁻¹ + Tr σ⁻¹ = (Tr ρ + Tr σ)/det ρ = (det ρ)⁻¹ under (57′). Only the middle term −1/v needs
  det ρ = −v from the canonical épinglage (§48 IV, p. 446 in the author's table), not on these pages; the modular case
  (det ρ = 1, entry v₁/v = −1) is consistent with it.
- **Scan 365, four épinglages, char. 2 — own idea (first pass) — keep.** In characteristic 2, (1 + N)⁻¹ = 1 − N = 1 + N
  for N² = 0, so ε₀⁻¹ = ε₀ and ε₁⁻¹ = ε₁ on those fibres: the four épinglages reduce to two there, those of L₀ and L₁.
- **Scan 366, "On a préféré normaliser" — unpursued implication — keep.** The choice of L₁ and of ε₁ rather than ε₁⁻¹ is
  tied to the form [α,ρ] = [β,σ]ε₁(ν) of the loop equation (§§44–45, pp. 356 and 384 in the author's table).
- **Scan 366, item 2, (64) — unproved claim — correct.** The group's letter is now read 𝔖 with a mark (row 21 of the
  changes). The preservation of the product relation is immediate and checked: cyclic permutation preserves a product
  equal to 1, and ε̃₀⁻¹σ̃⁻¹ρ̃ = 1 because σ̃ε̃₀ = ρ̃. The identification with (ρ,σ) ↦ (σ,ρ) holds only up to that
  cyclic permutation (note C367a).
- **Scan 367, opening question — conjecture (question) — keep.** It is answered on the same page by composition with
  τ′∞ and τ∞.
- **Scan 367, automorphisms and Z/2Z × Z/2Z — unproved claim — correct.** The relations check: τ′∞ and τ∞ are
  commuting involutions with τ∞τ′∞ = the exchange ℓ₀ ↔ ℓ₁ = σ∞, so τ∞ = σ∞τ′∞ and the group has order 4. But the group
  does not stabilise L₀ as written; see C367a.
- **Scan 367, ε̃₁ without inverse — own idea (first pass) — correct (resolved).** The triple must end with ε̃₁⁻¹: ρ̃σ̃⁻¹ε̃₁⁻¹
  = 1 while ρ̃σ̃⁻¹ε̃₁ = ε̃₁², and (61) gives ε″₀ = ε₁⁻¹. The ink has ε̃₁ without exponent, a slip of the author; the
  transcription keeps it.
- **Scan 368, recapitulation and (2) — unproved claim — keep.** The parametrisation by B′₀ × Tρ × Tσ is recalled from
  (III) (§48 III, p. 443); its bijectivity is not reproved here.
- **Scan 368, diagonal margin note — conjecture (question) — correct.** The reading is now settled: "Nous partons
  maintenant de ρ, σ, B′₀, ε₁ (d'où L₁) et nous posons la question à quelles conditions, on peut avoir une
  paramétrisation (2)". The answer starts on scan 369 with condition (4) and on scan 370 with surjectivity.
- **Scan 368, between (2) and (3) — unproved claim — correct.** The algebra checks: for a ∈ Tρ, ρ(ua⁻¹) = ρ(u)a⁻¹, so
  [ua⁻¹, ρ] = uρ(u)⁻¹, likewise for σ, and (1) becomes uρ(u)⁻¹ = uσ(u)⁻¹ε₁(ν(u)), i.e. (3). Only the scheme-theoretic
  points (ν a morphism of schemes B′₀ → G_a) remain.
- **Scan 368, ν(u) = det(u) − 1 — unpursued implication — keep.**

### Scans 369–373

1. **Scan 369, "par un argument connu" — unproved claim — keep.** σ(B′₀) ⊂ B′₁ ⇒ σ(B′₀) = B′₁ needs that both are
   "pré-Borels" of the same rank, fibrewise.
2. **Scan 369, (4) — unpursued implication — keep.** The criterion is now read in context: "un morphisme … → 𝒢ρ,σ =dfn
   schéma des solutions de (1)" (corrected from "relations").
3. **Scan 369, (5) and right margin — unproved claim — keep.**
4. **Scan 369, NB in the lower left margin — unpursued implication — keep.** Most words remain doubtful; no use of its
   content should be made beyond "détermine pratiquement B₀ … ambiguïté … deux Borels".
5. **Scan 370, surjectivity of (6) — conjecture (question) — keep.**
6. **Scan 370, necessity of (8) — conjecture (doubt) — keep.** The table dates (8) to §48 II (p. 434), the section titled
   by the equation ζ = ηε₁(μ − 1) that (7) restates.
7. **Scan 371, "La suite montrera si cette restriction est judicieuse" — conjecture (expectation) — keep.**
8. **Scan 371, stability of 𝒳σ under μ₂ — own idea (first pass) — correct (done).** With the universal point ε of
   μ₂ = Spec O_S[ε]/(ε² − 1), det(εη) = det η and Tr(εησ) = ε Tr(ησ), so stability is (ε − 1)Tr σ = 0 in O_S[ε]/(ε² − 1);
   since 1, ε is a basis, this is Tr σ = 0, over any base, residue characteristic 2 included. The author's "condition de
   stabilité" is thus exact.
9. **Scan 371, (10) — unproved claim — correct.** The phrase is « le résultat essentiel auquel nous tenions » (corrected
   from « crucial »); the content of the note stands.
10. **Scan 372, "trivial par définition" and "exige justement Tr σ = 0" — unproved claim — keep.** Necessity is
    immediate: b(σ) = −σ makes σ and −σ conjugate, so 2 Tr σ = 0, i.e. Tr σ = 0 when 2 is invertible, and for the
    universal point ε of μ₂ (note 8) Tr σ = ε Tr σ gives Tr σ = 0 over any base. Sufficiency, the local existence of b,
    is not shown on the page.
11. **Scan 372, transported group law — own idea (first pass) — keep.**
12. **Scan 373, (16)–(17) — unproved claim — keep.**
13. **Scan 373, margin "ε² = 1 résulte déjà de la première relation" — unproved claim — correct (checked).** Taking
    determinants in (19): det[α,ρ] = det[β,σ] = det ε₁(μ − 1) = 1 and det(ε·1) = ε² for 2×2 matrices, so ε² = 1.
14. **Scan 373, eliminating ε′ in (20) — own idea (first pass) — drop.** The author does it himself on scan 375: "on aura
    (det b)² = (det a)²", then the inverse image of the diagonal by δρ², δσ².

### Scans 374–377

- **R374.1 — scan 374, (22) — unproved claim — keep.**
- **R374.2 — scan 374, after (24) — unpursued implication — correct.** The wording is "déduit de l'expression de ceux-ci
  en termes de (B′₀, T₀), Tρ, N′σ en remplaçant N′σ par Tσ" (corrected from "des descriptions"); see also C374.
- **R375.1 — scan 375, projection mono and iso — unproved claim — correct.** The inverse is explicit: u ∈ T₀ is recovered
  from det u = det b by T₀ ⥲ G_m, u ↦ det u. In the corrected reading the image is "défini par l'équation (21)" and the
  author adds "on aura (det b)² = (det a)²".
- **R375.2 — scan 375, (22) épi onto μ₂ × μ₂ — unproved claim — keep.**
- **R376.1 — scan 376, (25)–(26) — unproved claim — keep.**
- **R376.2 — scan 376, tori except in char. 3 and 2 — unproved claim — correct (checked).** Tρ, the centraliser of the
  regular ρ, is the unit group of O_S[ρ] ≅ O_S[x]/(x² − x + 1), étale where the discriminant −3 is invertible, and det
  restricts to the norm, so STρ is the norm-one torus away from 3; likewise STσ with x² + 1 (discriminant −4) away from 2.
  (25) is then an extension of G_m by a 2-dimensional torus, a torus of dimension 3 away from 2 and 3.
- **R376.3 — scan 376, characteristic polynomials — own idea (first pass) — keep.**
- **R377.1 — scan 377, the action through δσ — unpursued implication — correct (checked).** For u = (μ λ; 0 1) ∈ B′₀
  and ε₀(λ′) in the upper unipotent L₀, uε₀(λ′)u⁻¹ = ε₀(μλ′) = ε₀(det(u)λ′), and det u = det b = δσ(b) by (21); the
  kernel of δσ on SG*∘(0) acts trivially on Λ₀.
- **R377.2 — scan 377, (28) — own idea (first pass) — keep.**

## Notes added in the second pass

- **C359a — scan 359 — own idea (check) — Claude (second pass).** With S = T − 1 the ring is Z[S]/(S², 2S) as written,
  and the multiplication T ↦ T⊗T of μ₂ gives S ↦ S⊗1 + 1⊗S + S⊗S, where S⊗S ≠ 0 (Z/2 ⊗ Z/2 = Z/2). So μ′₂ is not the
  additive group of Z ⊕ (Z/2)S: its fibre over F₂ is μ₂ (1 + S grouplike), not α₂, and it is trivial over Z[1/2].
- **C359b — scan 359 — unpursued implication — Claude (second pass).** The cancelled "est réduit" shows a first sufficient
  condition (S reduced: ν² = 0 ⇒ ν = 0), replaced by "2 section régulière de O_S" (2ν = 0 ⇒ ν = 0). Non-zero solutions of
  (46) need a section that is both 2-torsion and nilpotent, which is the criterion stated for (43).
- **C362 — scan 362 — unproved claim (check) — Claude (second pass).** The margin "σ⁻¹ρ = −λ₀ε₀ donc … = ρ(ε₀)": from
  ρ = −λ₀σε₀, int ρ = int σ ∘ int ε₀, so ρ(ε₀) = σ(ε₀). The mathematics gives σ(ε₀), not σ⁻¹(ε₀), in the doubtful
  reading; the transcription keeps the doubt.
- **C365 — scan 365 — unproved claim (check) — Claude (second pass).** (60)–(61): ε″₀ = −σρ⁻¹ = (−ρσ⁻¹)⁻¹ = ε₁⁻¹ and
  ε″₁ = −ρ⁻¹σ = ε₀⁻¹. The overwritten index in (61) must be 1; the ink is a blot, so the doubt mark stays.
- **C367a — scan 367 — own idea (check of a claim) — Claude (second pass).** As written, τ′∞ sends ℓ₀ to ℓ₁⁻¹, so the
  group {1, τ′∞, τ∞, σ∞} exchanges L₀ and L₁ and does not stabilise L₀ (the ink, checked enlarged, reads L₀); what it
  stabilises is the class of L∞ (τ′∞(ℓ∞) = ℓ∞⁻¹, τ∞(ℓ∞) = ℓ₀ℓ₁ = ℓ₀ℓ∞⁻¹ℓ₀⁻¹), as the index ∞ suggests. The two
  identifications hold up to the operations of scan 366: φ∘τ′∞ gives (ρ̃, ε̃₀⁻¹, σ̃⁻¹), a cyclic permutation of
  (σ̃⁻¹, ρ̃, ε̃₀⁻¹), and φ∘τ∞ gives (σ̃⁻¹ρ̃σ̃, σ̃⁻¹, ε̃₀⁻¹), the conjugate by σ̃⁻¹ of (ρ̃, σ̃⁻¹, ε̃₁⁻¹). "Stabilise L₀" and
  "conserver ou remplacer par son inverse le troisième facteur" are therefore true only after normalising the cyclic order.
- **C369 — scan 369 — unproved claim (check) — Claude (second pass).** "Deux sections de B′₁ qui ont m̄ déterminant … donc
  qui coïncident bien modulo (B′₁)u": B′₁ is conjugate to {(μ λ; 0 1)}, on which det = μ gives B′₁/(B′₁)u ≅ G_m, and
  conjugation preserves det. The step is complete without the doubtful "donc ablt".
- **C374 — scan 374 — unproved claim (possible slip) — Claude (second pass).** The ink reads "intersections de SG*ρ,σ,
  SG*♭ρ,σ(0) avec SGρσ", which would define SGρ,σ through itself. The intended intersection is with 𝒢ρ,σ, as in (15)
  (𝒢♭(0) = 𝒢ρ,σ ∩ 𝒢*♭(0)) and as "en remplaçant N′σ par Tσ" requires.
- **C376 — scans 375–376 — unpursued implication — Claude (second pass).** In the modular case, outside characteristics
  2 and 3, SG∘(0) is a 3-dimensional torus and SG*♭(0) is an extension of μ₂ × μ₂ by it (23); with (22) and (27),
  SG*ρ,σ is the semidirect product of Λ₀ ≅ G_a by that group, which acts through the character δσ. The exceptional fibres (STρ in
  characteristic 3, STσ in characteristic 2) are where non-reduced or unipotent parts can appear, and the page does not
  treat them.
