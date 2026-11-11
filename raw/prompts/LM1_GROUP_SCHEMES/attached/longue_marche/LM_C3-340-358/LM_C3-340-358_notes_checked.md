# LM_C3-340-358 — research notes, checked against the corrected transcription (scans 340–358)

Source: the first pass's research notes (answers/unzipped/LM_C3-340-358/LM_C3-340-358_notes.md, §5, notes 1–47),
each checked against LM_C3-340-358_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked
**Claude (second pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations), unproved
claim, unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks. Scans 340–343: σ² = −1 and ρ² = ρ − 1 (the underbraces of scans 341–342), hence, for
σ, ρ regular, Tr σ = 0, det σ = 1, Tr ρ = det ρ = 1 by Hamilton–Cayley (the values used on these pages); ε₀ = −σ⁻¹ρ =
σρ = 1 + N₀, ε₁ = −ρσ⁻¹ = ρσ = 1 + N₁ (scan 342), N = σ + ρ. Scans 353–358: ε₀ = −σ⁻¹ρ, ε₁ = −ρσ⁻¹ (scan 355), and
the pinned forms ρ = (0 u; v w), σ = (0 u′; v′ w′) of (26).

## Notes of the first pass

### Scans 340–343

- **N1 — scan 340 — conjecture — keep.** "Ce calcul suggère fortement que les relations (64) impliquent déjà (68)…
  c'est m̄ à peu de choses près une démonstration" is an expectation, not a proof. What remains, as stated, is that
  (64) (essentially (51)–(56) without (55)) implies (55), the independence of ε₀, ε₁ on every fibre, i.e. N₀, N₁
  non-homothetic on every fibre; the page argues by contradiction on a fibre where N₁ = λN₀.
- **N2 — scan 340 — drop.** The "calcul immédiat" and "(\*\*) N₀ = ρ⁻¹N, N₁ −" are cancelled by Grothendieck (zigzag
  and slanted strokes, framed); a cancelled step is not a claim of the text.
- **N3 — scan 340 — own idea (first pass) — correct.** λ² = λ³ = 1 gives λ = λ³(λ²)⁻¹ = 1 in any commutative ring.
  On the page the two relations come from N₁ = λN₀ on the fibre together with N₁ = σ̃(N₀), σ̃² = 1 (λ² = 1) and
  N₁ = ρ̃(N₀), ρ̃³ = 1 (λ³ = 1), cancelling N₀ ≠ 0 (N₀ regular). The λ³ step needs N₁ = ρ̃(N₀), which supports N₀ in
  the inserted "= ρ̃(N₁|N₀)" of (\*), where the ink shows N₁. Revised: derivation and dependency added.
- **N4 — scans 341–342 — conjecture — correct.** "Je ne serais pas étonné qu'on ait aussi des conditions
  équivalentes à (51) à (56) sous la forme (75)… ε₀ = −σ⁻¹ρ est unipotent régulier, en exigeant de plus, au besoin,
  que σ, ρ soient également réguliers". The ink of (75) has ρ³ and a blotted sign; the relations used on these pages
  (σ² = −1, ρ² = ρ − 1) make the intended polynomial ρ² − ρ + 1 (ρ³ = −1 follows from it, a possible source of the
  slip). The consequence sought, N = ρ + σ idempotent, is reduced on scan 343 to Tr σρ = 2 and left open.
- **N5 — scan 342 — unproved claim — correct.** "(ce qui équivaut, si N régulier, à (77) Tr N = 1, det N = 0 (?))":
  Hamilton–Cayley gives N² − N = (Tr N − 1)N − det N, and for N regular 1 and N are locally part of a basis (a⇔a′ of
  scan 344), so N² = N ⇔ Tr N = 1, det N = 0; the "(?)" is answered positively. The display is numbered (75) in the
  ink, repeating the (75) of scan 341.
- **N6 — scan 343 — conjecture (open question) — keep.** det(σ+ρ) = det σ + det ρ + det σ·Tr(σ⁻¹ρ) = 2 − Tr σρ
  (σ⁻¹ = −σ), so det N = 0 ⇔ Tr σρ = 2, numbered (69), with the margin "calcul déjà fait V. p. – ? (cf formule (69))".
  "Ce n'est pas entièrement élucidé — à revenir à la charge!": the implication (75) ⇒ (69) is left open, with the
  proposal to start from (75) instead of (68).

### Scans 344–349

- **N7 — scan 344 — unpursued implication — keep.** The proposition of "Sections régulières de G" puts fibrewise
  non-scalarity, the rank-two subalgebra A_ρ, cyclic vectors and companion forms in one list; b)–c″) are stated only
  for M = End(F), with differing locality qualifiers, so their use for a non-split Azumaya algebra goes through a
  local splitting.
- **N8 — scan 344 — own idea (first pass) — keep.** c) carries no locality qualifier in the ink ("Le O_S[T]-module
  F_ρ est isomorphe à O_S[T]/(T² − wT + v)"). For F = L ⊕ L, ρ = 0 ⊕ 1, F_ρ ≅ L ⊕ L over O_S[T]/(T(T−1)) ≅ O_S × O_S,
  which is free only if L is trivial, while a) holds: c) is meant locally. Confidence high.
- **N9 — scan 345 — unproved claim — keep.** "a ⇔ a′ trivial (algèbre linéaire des Modules M et des sous-modules
  O_S1 loc facteur direct)" and "b ⇔ b′ ⇔ b″ trivial": the passage from fibrewise non-scalarity to a locally free
  direct summand O_S + O_Sρ, and the lifting of a cyclic vector from a fibre (a ⇒ b), are only sketched.
- **N10 — scans 345, 347 — unproved claim — correct.** d) "et il en reste ainsi après chaque chgt de base S′ → S":
  the proof on scan 347 shows that u commuting with ρ equals u′ = a + bρ (u(e₀) = u′(e₀), then u(e₁) = ρu(e₀) =
  u′(e₁)), and "Comme b stable par chgt de base" gives the base-change statement, since the cyclic basis of b) pulls
  back. Revised: the argument on the page is complete once a ⇒ b is granted.
- **N11 — scan 346 — unproved claim — correct.** The ink reads "OPs α ∈ ΓSℓ(2)" (not ΓSG). Replacing a solution α
  of (7) by λα multiplies det α by λ², and by αt (t ∈ A_ρ*) by det t = c²v + wcd + d²; making det α = 1 needs a
  square root or a norm, so "On peut alors prendre α ds SG" holds fppf (étale if 2 is invertible) locally, not
  Zariski locally as the corollary's "loc. Zar".
- **N12 — scan 346 — unpursued implication — keep.** Corollary 3 describes the indeterminacy of α as right
  multiplication by A_ρ* (condition ⑧: c²v + wcd + d² invertible): the local solutions of (7) form a torsor under the
  unit group of the quadratic algebra A_ρ, a formulation the page does not pursue.
- **N13 — scan 347 — own idea (first pass) — keep.** Corollary 1 is a local (Zariski) conjugacy criterion; the global
  obstruction for regular ρ, ρ′ with equal trace and determinant can be phrased with the isomorphism torsor of the
  cyclic modules over the common algebra O_S[T]/(T² − wT + v). Confidence medium.
- **N14 — scan 348 — unproved claim — correct.** The parenthesis reads "(Alors D est uniquement déterminé par ε i.e.
  par N, [et réciproquement struck] D détermine N mod homothétie)", and the inserted c′) "∃ loc. base|Zar e₀, e₁ tel
  que ε = (1 1; 0 1)". The equivalences with D, B, SB and the uniqueness of D, B, SB are stated without proof.
- **N15 — scan 348 — own idea (first pass) — keep.** Over k[η]/(η²) with 2 ≠ 0 in k, N = ηI₂ has N² = 0 and
  det N = 0 but Tr N = 2η ≠ 0: square-zero does not give the "strictement nilpotent" condition det N = tr N = 0, which
  explains the adjective. Confidence high.
- **N16 — scan 349 — unpursued implication — keep.** If ρ is a scalar λ on a fibre, δ(ρ) = (2λ)² − 4λ² = 0 there, so
  δ invertible ⇒ ρ regular; regular nilpotents (δ = 0) show the converse fails. The page does not describe the regular
  locus beyond this sufficient condition.
- **N17 — scan 349 — unproved claim — keep.** "une corr. biunivoque entre les projecteurs élémentaires dans M, et les
  couples de Killing (B,T)" continues on scan 350 (T = A_P*, B₀ the stabiliser of D₀ = ker P, (13)); the inverse
  construction is not written.

### Scans 350–352

- **N18 — scan 350 — unproved claim — keep.** "Le schéma des ε unipotents réguliers, ou encore des N nilp. régul.
  est un fibré en droites épointées (i.e. un G_m-torseur) sur le schéma 𝒫 des Borels": stated without proof.
- **N19 — scan 350 — unproved claim — keep.** "lisse de dim relative 2" and "fibré-lisse de dim relative 1 sur le
  schéma des Borels": the counts agree (Borel scheme of relative dimension 1, G_m-torsor of dimension 1 over it; tori
  of a fixed Borel form a B_u-torsor), but no proof is given.
- **N20 — scan 350 — unproved claim — correct.** The identification of the fibre product with "le schéma des
  épinglages de G … i.e. des iso Gℓ(2)_S ⥲ G" is given without construction, and for G it needs a restriction on the
  isomorphisms: see C2.
- **N21 — scan 350 — unpursued implication — correct.** "Le proj. él. associé au couple de Killing opposé (T,B₁) est
  1 − N" (confirmed in the ink, a later darker hand). With P = (0 0; 0 1) the projector of the opposite pair, with
  image D₀ and kernel D₁, is 1 − P; "1 − N" is a slip of letter, the projector having first been called N on this
  page ("associant à [N struck] P", "le schéma des projecteurs élémentaires N").
- **N22 — scan 351 — unproved claim — correct.** "un torseur sur GP(1)_S ≃ Aut_{S-gr} Gℓ(2)_S ≃ Aut_{S-gr} Sℓ(2)_S ≃
  Aut_{S-gr}(GP(1)_S)": the first isomorphism fails for the full automorphism functor of Gℓ(2), which has a non-inner
  involution (C2); the other two hold.
- **N23 — scan 351 — unproved claim — correct.** (15) PN = 0, NP = N: with N = (0 1; 0 0) and P = (0 0; 0 1) (image D₁,
  kernel D₀ = N(F)) both hold, and (16) Pε = P, εP = P + N follow at once from ε = 1 + N. Conversely PN = 0 says
  N(F) ⊂ ker P and NP = N says N kills ker P, so for N regular nilpotent ker P = N(F) = ker N: the same Borel. Revised:
  verified.
- **N24 — scan 351 — unpursued implication — keep.** (17)–(19): Tr²ρ/det ρ is invariant under ρ ↦ λuρu⁻¹, and the
  next page asks when it is a complete invariant for local conjugacy in PG.
- **N25 — scan 352 — unpursued implication — correct.** The invariant is a morphism PG → 𝔼¹ (affine line; the ink has
  a double-stroke E). "Ces conditions sont suffisantes quand Δ(ρ̃) inv. i.e. Tr ρ inv." (det ρ is a unit); scan 353
  shows that the condition cannot be dropped.
- **N26 — scan 352 — unproved claim — keep.** "loc. fppf, existe λ ∈ ΓG_m telle que … λ² = det ρ′/det ρ": the cover
  O_S[X]/(X² − a), a = det ρ′/det ρ, is free of rank 2, hence faithfully flat, also in residue characteristic 2.
- **N27 — scan 352 — unpursued implication — keep.** τ′² = τ² with τ invertible gives τ′ = ετ, ε = τ′/τ ∈ Γμ₂; the
  proof uses μ₂, not the two constant signs, which matters when 2 is not invertible.
- **N28 — scan 352 — own idea (first pass) — keep.** The proof breaks exactly at the division by Tr ρ; the
  conjugacy quotient over the locus where Tr ρ is not invertible could be studied with square-zero test bases such as
  that of scan 353. Confidence medium.

### Scans 353–354

- **N29 — scan 353 — unproved claim — correct.** "il y a des contre-exemples évidents": ρ = (0 1; −1 w), ρ′ =
  (0 1; −1 w′) over A = A₀[w, w′]/(w², ww′, w′²) have det 1 and Δ = 0. A projective conjugacy over a faithfully flat
  B would give λ² = 1 and w′ = λw in B; but I = (w, w′) has I² = 0, and IB ≅ I ⊗_A B is free over B/IB ≠ 0 with
  basis w, w′, so w′ ∉ (B/IB)w. Revised: proof supplied (A₀ a field, or any A₀ ≠ 0 with the same argument).
  Confidence high.
- **N30 — scan 353 — own idea (first pass) — drop.** Repeats N29 (the traces w, w′ are lost by squaring) without a
  further idea.
- **N31 — scan 353 — unproved claim — keep.** "proviennent canoniquement des ε₀, ε₁ unipotents réguliers de SG":
  Grothendieck takes this up himself on scan 358 ("vérifier avec soin une assertion faite par la bande un certain nb
  de fois") and reduces injectivity to λ² = 1, (44); see N46, N47.
- **N32 — scan 353 — unproved claim — correct.** Margin "pour un relèvement plus commode (?) de σ et ρ, soit
  ε₀ = −σ⁻¹ρ, ε₁ = −ρσ⁻¹": if ε₀ = cσ⁻¹ρ with c a unit, then ε₁ = ρ(ε₀) = cρσ⁻¹ carries the same scalar, and the
  one rescaling σ ↦ −c⁻¹σ gives both normalised forms at once. Revised: the simultaneous normalisation is proved.
- **N33 — scan 353 — unpursued implication — keep.** Condition 2° was first "partout" and became "en chaque fibre
  'non équivalents'"; it is exactly what makes Tr(σ+ρ) invertible (C3) and the off-diagonal entries u, v units in
  (26).
- **N34 — scan 354 — unproved claim — keep.** "ε̃₀(G_a), ε̃₁(G_a), ε̃₀ ∈ Γε̃₀(G_a) définissent un épinglage canonique
  de PG donc de G": the two root groups and the root-group section are named, but canonicity and descent are not
  argued.
- **N35 — scan 354 — unpursued implication — correct.** From (26), −ρσ⁻¹ = (−u/u′ 0; (vw′ − wv′)/(u′v′) −v/v′); with
  u′ = −u, v′ = −v its lower left entry is (w + w′)/u, and ε₁ = (1 0; 1 1) gives w + w′ = u, i.e. w′ = u − w, as in
  (36) "w + w′ = u" and (41) "w′ = 1 − w". The ink has w′ in the denominators of that matrix and, in (29), "w′ + w = u
  i.e. w′ = w − u" (the + retraced over another sign, the right side unchanged): slips, kept in the transcription.
- **N36 — scan 354 — unproved claim — correct.** (30): with u′ = −u, v′ = −v, w′ = u − w one gets ρ + σ = (0 0; 0 u) =
  uP, P the elementary projector of the pinning, so σ = uP − ρ is determined by ρ, its coefficient u and P, as the
  margin says. Revised: verified.
- **N37 — scan 354 — own idea (first pass) — keep.** After fixing the pinning the pair (ρ, σ) is described by the
  units u, v and w ((26)–(31)); a classification must still account for the residual scalars and for descent.
  Confidence medium.

### Scans 355–358

- **N38 — scan 355 — conjecture (aim) — keep.** "On aimerait donner des 'critères numériques' intrinsèques": the
  proposition that follows (a)–f)) carries this out on the same pages.
- **N39 — scan 355 — unproved claim — correct.** The margin "ceci exprime que ε₀ est régulier et indépendant de ε₁,
  cf loc. cit." (for Tr(σ+ρ) invertible, given (32 a, b)) is proved in C3.
- **N40 — scan 355 — unpursued implication — keep.** "P et u sont uniquement déterminés, u = Tr(σ+ρ), P = (1/u)(σ+ρ)":
  the formulas commute with base change, so the decomposition (34) is compatible with base change wherever Tr(σ+ρ)
  is invertible.
- **N41 — scan 356 — unproved claim — correct.** "cet isom est unique", "cet φ est encore unique": among isomorphisms
  induced by algebra isomorphisms M₂(O_S) ≅ M this holds (an inner automorphism fixing (1 0; 1 1) and normalising the
  upper unipotent group is trivial), but the involution g ↦ det(g)⁻¹g of Gℓ(2) fixes both unipotent matrices, so among
  all group isomorphisms φ is unique only up to it (C2). The ink of (36) also has w′ for the upper right entry of
  φ⁻¹(σ), where "u + u′ = 0" needs u′.
- **N42 — scan 357 — unproved claim — correct.** (40), "que j'ai oublié d'expliciter": if det Q = 0 and u = Tr Q is a
  unit, Hamilton–Cayley gives Q² = uQ, so P = u⁻¹Q has P² = P, det P = 0, Tr P = 1; by the remark of scan 349
  (condition b) already implies regularity) P is an elementary projector. Conversely Q = uP gives det Q = 0,
  Tr Q = u. Revised: the cited prop. p. 475′ (scans 348–349) suffices.
- **N43 — scan 357 — unproved claim — correct.** In the pinned frame of (31), 1 = I, N₀ = (u/v)E₁₂, N₁ = E₂₁,
  P = E₂₂ form a basis of M₂(O_S) (u/v a unit), and ρ = v(N₀+N₁) + wP, σ = −v(N₀+N₁) + (u−w)P hold. The coefficient
  matrix (v w; −v u−w) has determinant uv, a unit, which gives the stated replacements of N₀ or N₁ (or of P) by ρ or
  σ. Revised: verified.
- **N44 — scan 357 — unpursued implication — keep.** "Notre point de vue ici est que nous partons de ρ̃, σ̃ … —
  l'épinglage est en effet défini déjà en termes de ρ̃, σ̃": the normalisation Tr(ρ+σ) = 1, (40), gives a preferred
  lift, whose uniqueness is asked on the next page.
- **N45 — scan 358 — conjecture (question) — keep.** "Y. a-t-il unicité de ρ, σ en termes de ρ̃, σ̃, par les
  conditions ε₁ = −ρσ⁻¹ (i.e. ε₀ = −σρ⁻¹) et (40)?" The question is left for the injectivity check that follows; the
  parenthesis does not match the definition of ε₀ (C4).
- **N46 — scan 358 — unproved claim under examination — correct.** From (44) λ² = 1 and the traces (Tr ε′ = λ Tr ε,
  both equal to 2) one gets 2(λ − 1) = 0, hence (λ − 1)² = λ² − 2λ + 1 = 0: injectivity holds when 2 is invertible or
  the base is reduced, and in general λ − 1 is a square-zero element killed by 2. Revised: the next step completed.
- **N47 — scan 358 — own idea (first pass) — keep.** Over k[t]/(t²), char k = 2, ε = I + E₁₂ and ε′ = (1+t)ε are
  both regular unipotent (det ε′ = (1+t)² = 1, Tr ε′ = 0 = Tr 1, ε′ − 1 = tI + (1+t)E₁₂ regular nilpotent) with the
  same image in PG and ε′ ≠ ε. It is the case λ − 1 = t of N46. Confidence high.

## Notes of the second pass

- **C1 — scan 340 — own idea (error in the text) — Claude (second pass).** The insertion "N = −σN₀ = ρ⁻¹N₀" is false
  under the relations of these pages: −σN₀ = −σ(σρ − 1) = ρ + σ = N holds, but with ρ⁻¹ = 1 − ρ one finds
  Tr(ρ⁻¹N₀) = Tr σρ − 2 − Tr σρ² + 1 = −1, while Tr N = 1, so N ≠ ρ⁻¹N₀ unless 2 = 0. The argument uses only
  N = −σN₀ (N commutes with σ, ρ when N₀ does), so "σ et ρ commutent" stands. Confidence high.
- **C2 — scans 350–351, 356 — own idea (claim needing a restriction) — Claude (second pass).** g ↦ det(g)⁻¹g is an
  automorphism of Gℓ(2) (an involution, equal to transpose-inverse up to an inner automorphism); it is not inner, since
  it inverts the centre, and it preserves T and B₀ and fixes (1 1; 0 1) and (1 0; 1 1). Hence Aut_{S-gr} Gℓ(2)_S ≅ GP(1)_S × Z/2, a
  pinning of G corresponds to two group isomorphisms Gℓ(2)_S ⥲ G, and "cet isom est unique" fails for arbitrary group
  isomorphisms. All three statements hold for isomorphisms induced by algebra isomorphisms M₂(O_S) ≅ M (G = M*), and
  for SG and PG as written. Confidence high.
- **C3 — scan 355 — own idea (proof of the margin claim) — Claude (second pass).** Put Q = σ + ρ; then
  N₀ = −σ⁻¹ρ − 1 = −σ⁻¹Q and N₁ = −Qσ⁻¹. Under (32 a, b) (det Q = 0, N₀² = 0) one has σ(ker Q) = Im Q on each
  fibre where Q ≠ 0, so ker N₁ = σ(ker Q) = Im Q while ker N₀ = ker Q. If Tr Q ≠ 0 on the fibre, Q is a non-zero multiple of a
  rank-one idempotent, Im Q ≠ ker Q and N₀, N₁ are regular and non-homothetic; if Tr Q = 0, either Q = 0 (N₀ not
  regular) or Im Q = ker Q (N₀, N₁ homothetic). So "ε₀ régulier et indépendant de ε₁ en chaque fibre" ⇔ Tr(σ+ρ)
  invertible, as the margin says. Confidence high.
- **C4 — scans 353–358 — own idea (slips in the formulas) — Claude (second pass).** Several displayed formulas
  disagree with the definitions they use; the transcription keeps them as written: (23) "= σ̃(ε̃₁)" for σ̃(ε̃₀) (cf.
  (24)); the w′ of (27), (29) and (36) noted in N35, N41; "ε₁ = −σ⁻¹ρ" on scan 357 for ε₀; and "(i.e. ε₀ = −σρ⁻¹)" on
  scan 358, which is ε₁⁻¹, not ε₀. None of them changes the conclusions drawn on these pages. Confidence high.
