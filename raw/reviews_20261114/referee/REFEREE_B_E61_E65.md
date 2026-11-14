# Referee B: LM7_PUSH E.65 and the rows under it (E.61, E.62 as used, E.64, E.67, LM7 D.25 and E.1 as used)

Referee: Claude Opus 5.5 at effort max (referee B), 14 November 2026. Launched by the main session (Claude Opus 5.5 at
effort max). The return checked is by GPT-6 Astra (ChatGPT Pro mode):
`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped\LM7_PUSH\`.
Leads read, not relied on: `pro_intake_20261114\INTAKE_20261114.md` (Claude Fable 5.2 at effort high) and
`CONSULT_LM_EXPERT.md` (Claude Fable 5.2 at effort max). No program of the return was run; `history\` was not opened.
My scripts and their outputs are in `C:\Users\user\Documents\pro_intake_20261114\referee\checks\` (list at the end).
Every script passes; none reads a file of the return.

## Verdicts

| Row | Verdict |
|---|---|
| **E.65** | **Proved, with two gaps that I close.** (1) The Galois-vanishing step (line 272-280) is asserted by reference to E.1 and LM7 D.25, whose own justification is the comparison LM7 D.15, stated there as "Known" with a sketched proof. I give the comparison for the case used (Section 1, step 9), including the model and sign bookkeeping that the return leaves implicit; it confirms the claim. (2) Existence of the pure r-frame for an arbitrary F (line 101-106 cites only uniqueness); closing argument in step 2. The clause "the element of E.58 has Δ = 1", and with it "ker Δ has index two", is conditional on E.58; referee A (`REFEREE_A_D50_E58.md`, written while this report was being finished) finds E.58 and D.50 proved as claimed, so with both reports these clauses stand. No error found. |
| **E.61** | **Proved as claimed**, including E.61.4 and the whole sewing part (E.61.5-E.61.22). E.61.4 was recomputed over the entire signed image of F modulo 12; every braid identity was rechecked through the faithful Artin representation; relation (IV), Definition 5.1 and relation (R′) were checked in the Nakamura-Schneps preprint. |
| **E.62 (as E.65 uses it)** | E.65 uses only the action convention s ↦ sf, r ↦ f⁻¹r (E.65.8, line 96: "used throughout E.58-E.62"), which E.62 shares (`E_gl23_ferrari_agent.tex` lines 57 and 238). None of E.62's finite counts enters E.65. The dependency is nominal; E.62's own counts were not refereed (outside the scope). |
| **E.64** | **Proved as claimed in every step I could check; no error found.** Three steps rest on results I did not verify: existence of the quartic frame H_F (E.39, outside my scope), the profinite form of the sewing comparison E.64.3 (Boggi 2026 v6, Theorem 2.3 and Proposition 2.6(i), not opened), and the Galois formula E.64.13 (Nakamura-Tsunogai-Yasuda 2010, Propositions 4.11-4.13, not freely accessible). None of the three is used by E.65 or E.67. The orbifold formula E.64.28, which the proof only sketches, is proved here (step E64-9). |
| **E.67** | **Proved as claimed for every universal statement** (E.67.1, E.67.3, E.67.4, E.67.6, E.67.9-E.67.12, the order 1944). The 48 per-origin statements (one framed Mordell target in each of the 24 E.1 and 24 E.17 origin cosets, with the saved corrections c_{j,t}) are finite data claims that I did not recompute; I verified the structure that reduces each of them to one membership test (step E67-7). |
| **LM7 D.25 and E.1 (as used for the parity)** | The definition of the two bits, the 24/24 split, the field identities (D.25.1) and the sign rule are correct (recomputed). The identification of the bits with the Galois restrictions to M′ = Q(i, (3/4)^{1/4}) rests on LM7 D.15 (sketched); my re-derivation (step 9) confirms it for every Galois element of multiplier one. |
| **Register defect** | In the LM7_PUSH register the dependency "D.25" of E.1, E.58 and E.65 means **LM7 D.25** (Fermat-tower register; `LM7_FERMAT_TOWER\sections\D_cm_shadow.tex`), not LM7_PUSH's own D.25 (an order-five peripheral cycle, `D_cycle_agent.tex`). E.65's dependency list also omits Herfort-Ribes and LM7 D.15 and lists E.62, which it does not use. |

### What this means for E.3

- **"Is Δ zero on ĜT?" is a correct reformulation of E.3.** E.65's proof gives: some element of ĜT has a multiplier-one,
  cusp-fixing action on G_6 in the extra CM coset (the meaning of E.3 in E.1 and LM7 D.25) if and only if Δ is not zero
  on ĜT. The direction "Δ(F) = 1 ⇒ extra coset" goes F ↦ H = Fσ⁻¹ (σ Galois of the same multiplier) ↦ H³, which has
  ρ ≡ 0 mod 3, hence V = I and q₁₂(f) = I mod 12, hence fixes Q and induces an E.1-type automorphism of G_6 with
  parity δ(H³) = δ(H) = 1 (step 11). The converse is the definition. This equivalence does **not** need E.58.
- **What E.58 adds.** If E.58 holds (referee A: proved as claimed), Δ is a nonzero continuous character of ĜT₀ with
  kernel of index two containing the Galois image. Then: Δ ≠ 0 on ĜT would give a continuous quadratic character of ĜT trivial on G_Q, so ĜT ≠ G_Q, an
  open problem of the field; Δ = 0 on ĜT would give ĜT ⊂ ker Δ ⊊ ĜT₀, an explicit relation that the pentagon adds to
  the two- and three-cycle relations at the full profinite level. If E.58 failed, Δ might vanish on all of ĜT₀ and E.3
  would be answered negatively (no element of ĜT₀ at all reaches the extra coset).
- **Scope remark.** For an element of multiplier λ ≠ 1, E.65 defines Δ(F) = δ(Fσ⁻¹) by Galois translation; it does not
  define signed CM coordinates T_F, W_F for λ ≠ 1 (only the projective 𝒯_G, 𝒲_G). E.3 as stated in E.1 and LM7 D.25
  concerns multiplier one, so this does not affect the reformulation.
- E.61, E.64 and E.67 give no value of Δ on ĜT. E.67.1 rewrites δ on ĜT ∩ ℋ as ε₃(𝒟₃) + ε₂(𝒟₄) + ε₂(B₄); this is an
  identity of characters, correct as stated, and assigns nothing.

---

## 1. E.65 step by step (`sections\E_cm_character_agent.tex`)

Notation as in the return: B̂ = Ĉ₂ ∐ Ĉ₃ = ⟨s, r⟩, F̂ = ker(B̂ → S₃) free on x = (sr)⁻², y = sxs; U, L, S = ULU,
R₊ = UL, R₀ = −R₊; q: B̂ → Q = SL₂(Z/12)/{±I}; q₁₂ the signed map x ↦ U², y ↦ L² on F̂.

**Step 1. The action (lines 85-99, E.65.8).** Claim: ĜT₀ acts on B̂ through u ↦ u^λ, v ↦ f(u²,v²)⁻¹v^λf(u²,v²), with
s = uvu, r = uv, sr = u⁻¹ modulo the centre; at λ = 1 the action fixes sr. *Verified.* The formula is the standard one
(Nakamura-Schneps 2000, formula (1.1), checked in their preprint, line 102 of my text extraction: for B₃ it reads
τ₂ ↦ f(τ₂², τ₁²)τ₂^λ f(τ₁², τ₂²) = f⁻¹τ₂^λ f by (I)). By hand: s⁻¹r = (uvu)⁻¹uv = u⁻¹, and s = s⁻¹ modulo the centre.
I also checked that the B-form of the multiplier-one action is s ↦ sf, r ↦ f⁻¹r, and that these define an endomorphism
of B̂ exactly when (sf)² = 1 ⟺ (I) and (f⁻¹r)³ = 1 ⟺ (II) with m = 0, because conjugation by r sends x ↦ y ↦ z = (xy)⁻¹
(matrix check `check_e61_e65_matrices.out`, lines "R_+ U^2 R_+^{-1} = L^2" and "r y r^{-1} = z"). E.62 uses the same
convention (its lines 57, 238).

**Step 2. Frames: existence, uniqueness, continuity (lines 101-106).** Claim: C_B̂(s) ∩ F̂ = C_B̂(r) ∩ F̂ = 1, giving
uniqueness and continuity. *Verified; existence of A_F is not argued in E.65 — gap closed here.*
- Uniqueness. The paper of Herfort-Ribes 1985 was not accessible to me. The fact needed follows from the
  classification of closed solvable subgroups of free profinite products (Herfort-Ribes 1989, Theorem 3.2, quoted in
  Guralnick-Haran, arXiv:1001.3599, introduction): such a subgroup is conjugate into a factor, or ≅ Ẑ_σ ⋊ Ẑ_σ′
  (torsion-free), or a free product C₂ ∐ C₂ (non-abelian), or a Frobenius group Ẑ_σ ⋊ C (non-abelian). If w ∈ F̂
  commutes with s, the closed subgroup ⟨s, w⟩ is abelian and contains an involution, so it is of the first type, hence
  finite, so w has finite order; F̂ is torsion-free, so w = 1. Same for r. (The same conclusion follows from profinite
  Bass-Serre theory: a nontrivial element of a vertex group fixes exactly one vertex, since edge stabilizers are trivial.)
- Existence (closing argument). Φ_F(s) = sf has order 2 and Φ_F(r) = f⁻¹r has order 3; finite subgroups of a free
  profinite product are conjugate into a factor, so sf = γsγ⁻¹ and f⁻¹r = γ′r^{±1}γ′⁻¹. The sign is +: in B̂^ab = Z/6,
  f ∈ F̂′ maps to 0, so f⁻¹r and r have the same image, while r⁻¹ has another. In S₃ the image of γ (resp. γ′) centralizes
  s̄ (resp. r̄), so right multiplication by a power of s (resp. r) puts the conjugator in F̂.
- Continuity: F̂ → B̂, A ↦ ArA⁻¹, is a continuous injection of a compact space into a Hausdorff space, hence a
  homeomorphism onto its closed image, and F ↦ f⁻¹r is continuous. (Wording at line 105: "the indicated conjugacy
  class" means the F̂-orbit of r, which is half of the B̂-conjugacy class; harmless.)

**Step 3. E.61.4 and the covariance (lines 108-129, E.65.9-10).** Claim: V_FSV_F⁻¹ = Sq₁₂(f), V_FR₀V_F⁻¹ = q₁₂(f)⁻¹R₀
with V_F = U^{8ρ_F}; hence qΦ_F = Ad(V_F)q on B̂, and q₁₂Φ_F = Ad(V_F)q₁₂ signed on F̂. *Verified.* E.65.10 holds as a
polynomial identity over Z[n] with n = 8ρ (sympy, `check_e61_e65_matrices.out`: "E.65.10a", "E.65.10b"). For the signed
restriction: both sides are lifts of the same projective class; Φ_F preserves F̂ (it acts trivially on S₃), q₁₂(F̂) mod 4
is the four-group V₄, V_F ≡ I mod 4, and −I ∉ V₄ (checked), so the two lifts agree modulo 4 and hence are equal.

**Step 4. The class-two sign (lines 131-148, E.65.11).** Claims: the three-cycle equation kills the class-two image of f;
θ(h)⁻¹h = [x,y]^{ρ²+2d}; hence ρ_F ∈ 2Ẑ and q₄(β_F) = I. *Verified* in the integral Heisenberg model by sympy (symbolic
ρ, d): [y,z] = [z,x] = [x,y] in class two, so f(z,x)f(y,z)f(x,y) ↦ [x,y]^{3c} and c = 0; θ(h)⁻¹h = [x,y]^{ρ²+2d}
independently of the commutator convention. So ρ² ∈ 2Ẑ, i.e. ρ is even (only the 2-adic component is constrained).
Consistency with Galois: ρ_σ = −κ₂(σ) (Marin 2008, end of Section 4: ρ coincides with −8ρ₂ for the 8-scaled
coordinate; LM7 D.18), and κ₂ is even on G_{Q^ab} because √2 ∈ Q(ζ₈).

**Step 5. The modulo-four normalization (lines 150-162).** Claims: q₄(A_F) = I because the centralizer of R₀ in V₄ is
trivial; T_FR₀ = R₀T_F, W_FS = SW_F modulo 12; the centralizers at three are ⟨−I⟩×⟨R₀⟩ ≅ C₆ and ⟨S⟩ ≅ C₄.
*Verified* by enumeration: C_{V₄}(R₀) = {I}; no element of V₄ conjugates R₀ to −R₀; the trace (−1 versus 1) fixes the
sign for R₀ and the reduction mod 4 (S ≠ −S) fixes it for S; C_{SL₂(F₃)}(R₀) has the six elements ±R₀^k and
C_{SL₂(F₃)}(S) = ⟨S⟩; ker(R₀ − I) = ker(R₊ + I) = F₃(1,−1).

**Step 6. Multiplicativity (lines 164-177, E.65.12).** Claims: A_{FG} = Φ_F(A_G)A_F, β_{FG} = Φ_F(β_G)β_F, ρ additive,
T and W homomorphisms. *Verified* by hand: Φ_FΦ_G(r) = Φ_F(A_G)A_F r (…)⁻¹ with Φ_F(A_G)A_F ∈ F̂, so uniqueness gives the
law; ρ is additive because the multiplier-one action is trivial on F̂^ab; substituting step 3 gives
T_{FG} = q₁₂(A_F)⁻¹V_F q₁₂(A_G)⁻¹V_G = T_F T_G. ε₃ and ε₂ are characters (checked: ε₃ on C(R₀) has kernel ⟨R₀⟩).

**Step 7. The sign comparison (lines 179-192, E.65.13).** Claim: δ is "exactly the extra-CM parity of E.1, including its
global-sign convention". *Verified for the convention:* E.1 (`E_agent.tex` lines 69-80) uses the lift of each class whose
reduction mod 4 lies in V₄, the sign of A⁻¹ on ker(R − I) and the class of β⁻¹ mod 3 in {±I, ±S}; with V = I these are
ε₃(T_F) and ε₂(W_F). I recomputed the 48 pairs: |C_H(r)| = 6, |C_H(s)| = 8, 24 with equal bits and 24 with unequal
bits; all normalized r-conjugators are I mod 4 (as D.25 says). For F with ρ_F ≢ 0 mod 3, Φ_F does not induce the identity
on Q, so E.1's parity is not literally defined; E.65's δ is its extension, and the reduction to E.1-type elements is
made by cubing (step 11). The arithmetic content of line 182-192 is step 9.

**Step 8. Transport under all multipliers (lines 194-269, E.65.14-17).** Claims: frames β_G ∈ F̂, A_G ∈ F̂s^{b_G} with
Φ_G(r) = A_G r^{ε_G} A_G⁻¹; the intertwiner 𝒱_G = [[λ, t_G],[0,1]] with q_ℓΦ_G = Ad(𝒱_G)q_ℓ (Marin, Lemmas 4.1-4.3);
𝒯_G, 𝒲_G projective representations normalizing ⟨R₀⟩, ⟨S⟩; δ(GFG⁻¹) = δ(F). *Verified.*
- Φ_G(r) ↦ 2λ in B̂^ab = Z/6 (u, v ↦ 1), so Φ_G(r) is conjugate to r^{ε_G}, ε_G ≡ λ mod 3; Φ_G acts trivially on S₃
  because λ is odd; the coset normalization and uniqueness follow as in step 2; the multiplication law keeps the coset
  because b is additive modulo 2.
- Marin 2008 (arXiv:0801.2507, Section 4, opened): Lemma 4.3 states that R(σ₁) = a_λ forces R(σ₂) = R(σ₁) or
  R(σ₂) = b_λ(u) = [[1−u, λu²],[−1/λ, 1+u]]; this is exactly the matrix at E.65 line 231. My sympy check: the (2,1)
  entry of NMN − MNM is −c(1+λc); c = −1/λ forces b = λ(a−1)²; V = [[λ, λu],[0,1]] conjugates U to U^λ and L to
  b_λ(u); the joint centralizer of U and L is scalars over any commutative ring (E.64.25). Marin's normalization
  c_g = [[1,ρ],[0,1]] with the right action of diag(1,λ) is projectively the same as [[λ, t],[0,1]].
- Equality of 𝒱_F mod 12 with V_F for F ∈ ℋ: a shear [[1,m],[0,1]] sends S to [[−m, 1+m²],[−1, m]], which is ±S only for
  m ≡ 0 mod 12 (checked).
- E.65.16: derived by hand from the multiplication law and qΦ_G = Ad(𝒱_G)q; the signs agree because both sides are I
  mod 4.
- E.65.17: by enumeration over GL₂(F₃), every projective normalizer of ⟨R₀⟩ (12 matrices) preserves F₃(1,−1) and ε₃ on
  C(R₀), and every projective normalizer of ⟨S⟩ (16 matrices) preserves ε₂.

**Step 9. Galois vanishing (lines 271-280). Gap in the text; closed here.** Claim: for σ ∈ G_Q of multiplier one,
δ(σ) = 0. The return argues that "both restrictions in (E.65.13) are its action on the same field", and alternatively
that E.1 gives δ = 0 on the kernel of ρ mod 3 (an index ≤ 3 subgroup, which suffices for an F₂-valued character). Both
routes rest on the dictionary of LM7 D.15 (`LM7_FERMAT_TOWER\sections\D.tex` lines 642-658, status Known, proof a
sketch): the frames give the Galois action on the torsion of the two CM fibres, modulo signs. E.65 does not say which
model and which sign. Closing argument (for σ ∈ G_{Q^ab} = ker χ):
1. Use the Legendre family E_λ: y² = x(x−1)(x−λ) over U₀,₃ = P¹ − {0,1,∞} with base point the tangential point 01⃗.
   Its signed monodromy on F̂ = π₁(U₀,₃) is q₁₂ (x ↦ U², y ↦ L²; the fibres at 0 and 1 are of type I₂, unipotent
   monodromy), and the Galois action on π₁^orb([U₀,₃/S₃], 01⃗) is Φ_σ (Ihara; Nakamura-Schneps (1.1)).
2. s̄ ∈ S₃ swaps 0 and 1, so s is the transported inertia at λ = 1/2; r is the transported inertia at a root λ₀ of
   λ² − λ + 1 (fixed by σ ∈ G_{Q(√−3)}). For σ fixing the point p, path transport along a path in U₀,₃ gives: the action
   of σ on the Tate module of E_p, in the basis transported from 01⃗, is mono(c_σ)·ρ_{01⃗}(σ), with the path cocycle
   c_σ ∈ F̂. By uniqueness of pure frames (step 2), c_σ is the inverse frame; ρ_{01⃗}(σ) is a normalized shear for χ = 1
   and, by uniqueness of the intertwiner (step 8), equals V_σ mod 12. Hence, signed: W_σ = ρ_{E_{1/2},12}(σ) and
   T_σ = ρ_{E_{λ₀},12}(σ), in transported bases.
3. E_{1/2} ≅ y² = x³ − 4x, the twist of E₄: y² = x³ − x by 2 (sympy: X = 4x − 2, Y = 8y). Since √2 ∈ Q^ab,
   W_σ ≡ ρ_{E₄,12}(σ) up to a fixed conjugation. Mod 3, W_σ is projectively trivial iff σ fixes x(E₄[3]), i.e. iff σ fixes
   r₀ = (3/4)^{1/4} (D.25.1). So ε₂(W_σ) = [σ moves r₀]. Consistency: Q(E₄[4]) = Q(ζ₈) is abelian (halves of (0,0) lie
   in Q(i), halves of (1,0) in Q(√2)), so ρ_{E₄,4}(σ) = I, as W_σ ≡ I mod 4 requires.
4. Shifting x by (1+λ₀)/3 gives E_{λ₀}: y² = x³ + c′³ with c′ = −(2λ₀−1)/3 = 1/√−3 (sympy), the quadratic twist of
   E₃: y² = x³ + 1 by c′. On G_{Q^ab} its twisting character is σ(√c′)/√c′ = σ((−3)^{1/4})/(−3)^{1/4} = σ(r₀)/r₀,
   because (−3)^{1/4} = ζ₈·3^{1/4} and 3^{1/4} = √2·r₀. Hence T_σ = (σ(r₀)/r₀)·ρ_{E₃,12}(σ).
5. On E₃[4], σ acts by (σ(r₀)/r₀)·I (y(P) = √3(√3−1)r₀ for a half P of (−1,0), and the other halves are [ζ₃]-images).
   So T_σ ≡ I mod 4, as proved in step 5: an independent consistency check of the sign. On E₃[3], σ fixes the rational
   point (0,1), which spans the fixed line of the order-3 automorphism, i.e. F₃(1,−1) = ker(R₀ − I). So T_σ acts on
   F₃(1,−1) by σ(r₀)/r₀: ε₃(T_σ) = [σ moves r₀].
6. Therefore δ(σ) = [σ moves r₀] + [σ moves r₀] = 0 for every σ ∈ G_{Q^ab}.
The argument uses only standard comparisons (path transport; the Galois action on the orbifold fundamental group with
tangential base point), the uniqueness statements already verified, and the algebra checked in `check_d25_fields.out`.
It confirms the claim of E.65, of LM7 D.25 ("No Galois element can give one of them") and the model choice in LM7 D.15.

**Step 10. Extension and continuity (lines 282-299, E.65.5-6, E.65.18).** *Verified.* χ is onto Ẑ^×, so every F is
Hσ; two choices differ by an element of G_Q ∩ ℋ, where δ = 0 (step 9); Δ(F₁F₂) = δ(H₁·σ₁H₂σ₁⁻¹) = δ(H₁) + δ(H₂) by
E.65.17; the compact surjection ℋ × G_Q → 𝒢 is a quotient map; uniqueness is immediate.

**Step 11. E.58's value and the reduction of E.3 (lines 301-315).** *Verified, conditional on E.58 for the value.* With
q(A) = [5I], q(β) = 1, V = 1 (E.58.5): the normalized lift of [5I] is 5I (I mod 4, −I mod 3; −5I ∉ V₄ mod 4; 5I ∈ q₁₂(F)),
so T = 5I, ε₃ = 1, W = I, ε₂ = 0, δ = 1. Cubing: V_{H³} = U^{24ρ} = I and q₁₂(f_{H³}) = I mod 12 for every ρ (checked), so
Φ_{H³} induces the identity on Q, preserves N̂_B and its characteristic open subgroup N̂_B′N̂_B⁶, and induces an E.1-type
automorphism of G_6 with parity δ(H³) = 3δ(H) = δ(H). E.1's parity of that automorphism equals δ(H³) because the
Q-images of the frames are determined by the G_6-action (LM7 D.25.6).

**Step 12. Finite certificate (lines 317-326).** Not run (rule). My own checks replace it.

## 2. E.61 step by step (`sections\E_genus_one_sewing_agent.tex`)

| Step (lines) | Claim | Verdict and check |
|---|---|---|
| 80-90 | f = β(y,x)β(x,y)⁻¹; β unique; β^ab = (u,u); ρ = −u; E.61.2 | Verified by hand (s swaps x, y; f ∈ F̂′). Uniqueness as in E.65 step 2. "ρ is the Nakamura-Schneps frame coordinate": NS Definition 5.1 (preprint, my extraction line 954) defines ρ₂(F) by g_F ≡ (xy)^{ρ₂} with f = g_F(y,x)⁻¹g_F(x,y); g_F is unique, so h = g_F and ρ = ρ₂(F). Verified. |
| 92-111 | q₁₂(F) mod 4 = V₄ (abelian, −I ∉ V₄); S, R define B̂ → PSL₂(Z/12) restricting to the projectivization of q₁₂ | Verified by enumeration: ⟨U²,L²⟩ mod 4 has the four listed elements; q₁₂(F) has order 96 and does not contain −I; SR = U⁻¹, SU²S⁻¹ = L². |
| 113-122 | q₁₂(f) = SgS⁻¹g⁻¹ (signed); the cube (q₁₂(f)⁻¹R)³ is I | Verified: SL²S⁻¹ = U², SU²S⁻¹ = L² give the substitution; R³ = I over Z fixes the sign mod 4. |
| 124-156 | E.61.12-14: ε has kernel Q₈; the cubic condition holds exactly for g = X^kS^j; then SgS⁻¹g⁻¹ = [[1,k],[k,1+k²]], k = ε(g) = ρ | Verified on all 24 elements; the other 12 give −I. |
| E.61.4 | q₁₂(f) = [[1,−8ρ],[−8ρ,1+64ρ²]] mod 12 | Verified directly: for every g in the signed image q₁₂(F) (96 elements) with SgS⁻¹g⁻¹ ≡ I mod 4 and the signed cubic condition (24 such g), SgS⁻¹g⁻¹ equals the displayed matrix with ρ ≡ ε(g) mod 3. |
| 158-166, E.61.7 | η_m is a homomorphism; Ferrari generators map to e₁, e₂ | Verified over Z (sympy): aba = bab, bcb = cbc, ac = ca; η(ca⁻¹) = e₁, η(abac⁻¹b⁻¹a⁻¹) = e₂. |
| 168-195, E.61.15-17, E.61.8 | η(E₁) = η(E₃) = 1; the four E-factors vanish; f(η(b)²,η(c)²) = ((−B, A−1), q⁻¹); E.61.8 | Verified symbolically over Z with det q = 1. The vanishing uses f ∈ F̂′ with one argument trivial; f(L²,U²) = q⁻¹ uses (I). At m = 12, E.61.4 gives A = 1, B = −8ρ, so the value is 1. |
| 197-223, E.61.18-20 | The four maps A₃ → B₄ and their central squares | Verified through the faithful Artin representation (`check_braid_identities.out`): each pair satisfies uvuv = vuvu; (uv)² = X₃₄Z, X₂₃Z, X₂₃Z, X₁₂Z; Z central. |
| 225-253, E.61.21-22 | Relation (IV) in A₃ form; the four rewritten factors; central powers cancel; the word is NS's (R′) at multiplier one | Verified against the NS preprint: (IV) is f(τ₁, τ₂⁴) = τ₂^{8ρ₂}f(τ₁²,τ₂²)τ₁^{4ρ₂}(τ₁τ₂)^{−6ρ₂} (my extraction line 123), and (τ₁τ₂²)² = (τ₁τ₂)³ gives E.61.21. The four maps are NS's {D_{a1},x₅₁}, {D_{e2},x₅₁}, {D_{e2},x₄₅}, {D_{a3},x₄₅}; NS's four displayed formulas (proof of Claim 8.3) omit the central Z-powers, which E.61.22 retains; I rederived all four lines, including Z^{±2ρ}. NS's (R′) at μ = 0 is literally E.61.6. |
| 255-266 | Certificate and research note | Not run; replaced by the checks above. |

The statement's last sentence ("this specified sewing projection supplies no additional CM parity restriction") is
correct: E.61.8 vanishes at m = 12 for every multiplier-one gentle pair. Note that η_m is defined on B̂₄, not on Γ̂₁,₂;
E.61 does not claim that R_ρ(f) = 1 in B̂₄, only computes its image.

## 3. E.64 step by step (`sections\E_hyperelliptic_CM_agent.tex`)

| Step | Claim | Verdict and check |
|---|---|---|
| E64-1 (167-201) | Υ̂_g is preserved by Φ_{2g+2,F}; deck involution fixed; genus-zero quotient | Verified, with one citation unopened. Braid identities E.64.14 verified for n = 4, 6, 8 (z_last = δz_firstδ⁻¹, W_n = z_nz_last⁻¹, z_n central). The deduction Φ(W_n) = v_nW_n^λv_n⁻¹ uses only Φ(z_k) = z_k^λ for the initial full twists (NS (1.1) restricts to the first strands). The relator set is the classical Birman-Hilden presentation (W_n commutes with σ₂,…,σ_{n−1} in B_n anyway). Endo-Kamada 2016 not opened. |
| E64-2 (203-243) | Genus-two sewing E.64.3 | Discrete part verified: (z₄, −2) corresponds to δ₁δ₂⁻¹ = d²z₄⁻¹; the action is consistent with that subgroup; Φ₆(T₅) = T₅^λ follows from the central-shift lemma (f(cX, Y) = f(X, Y) when c is central in ⟨c, X, Y⟩ and f ∈ F̂′). The profinite isomorphism rests on Boggi 2026 v6 (Theorem 2.3, Proposition 2.6(i)) and Margalit-Winarski Section 6, not opened. Not used by E.65 or E.67. |
| E64-3 (245-286) | Mordell subgroup θ: B̂₃^mor ≅ q̂⁻¹(⟨r⟩) | Verified: the braid relation for θ, θ((uv)³) = z₄, q(θ(u)) = q(θ(v)) = ab, θ(k₁) = ξ₁, θ(k₂) = ξ₂, all of E.64.18 (Artin representation). The Hopfian argument and the five-lemma step are correct. |
| E64-4 (288-332) | Quartic subgroup G₄ ≅ q̂⁻¹(⟨s⟩); C₄ ∐ C₂; cusp relation | Verified: y² = d⁴ = z₄; q(d) = s, q(y) = s², q(x) = s⁻³; k₀ = ξ₂⁻¹, k₁ = ξ₁⁻¹; dξ₁d⁻¹ = ξ₂⁻¹, dξ₂d⁻¹ = ξ₁; x = ξ₁d⁻³; x⁴z₄³ = [ξ₁, ξ₂⁻¹] with [p,q] = pqp⁻¹q⁻¹ (the convention used throughout; E.64.29 and E.64.31 hold in the same convention). E.64.21 checked by hand (α²(k₀) = k₀⁻¹ is exactly Y² = D⁴). The kernel onto C₄ equals K (index and torsion-freeness). |
| E64-5 (334-348) | Completion of the two inclusions | Verified (standard semidirect-product argument; closures of ⟨r⟩, ⟨s⟩ are Ẑ because exponent sums 2, 3 are injective on Ẑ). |
| E64-6 (350-397) | Frames A_F, β_F lifted; H_F exists, unique; cocycle laws | Verified, except existence of a conjugator for d, taken from E.39 (outside my scope). Lifting through the centre: exponent sums. Uniqueness of H_F: C_{C₄∐C₂}(d̄) = ⟨d̄⟩ (same argument as E.65 step 2), then K̂ ∩ ⟨d⁴⟩ = 1. |
| E64-7 (399-454) | M_F unipotent shear with M_FLM_F⁻¹ = Q(f)⁻¹LQ(f); t_F ≡ 8ρ_F mod 12; C₃ ≡ T, C₂ ≡ W | Verified: E.64.17 table holds for conjugation gξg⁻¹ (Artin representation), giving Q(a) = U, Q(b) = L; e = f(z₃, c²) ∈ K̂ commutes with a; f(z₃,c²) = f(y₃,c²) by the central-shift lemma, so the NS formula (1.1) is matched; E.64.25 and E.64.27 checked symbolically. Since Q = q₁₂ on ⟨a²,b²⟩ and M_F ≡ V_F mod 12, C₃(F) ≡ T_F and C₂(F) ≡ W_F mod 12 for every F ∈ ĜT of multiplier one, not only on the E.1 fibre. |
| E64-8 (E.64.11) | Centralizers and determinants | Verified: aI + bR₊ = [[a,b],[−b,a+b]] has determinant a² + ab + b²; aI + bS has a² + b². |
| E64-9 (456-483, E.64.28) | The orbifold formula is a homomorphism | **The proof is a sketch; I prove it.** With (II) rotated, x^m f(z,x) = f(y,x)y^{−m}f(z,y)z^{−m}, so Ω(x)Ω(y)Ω(z) = 1 is equivalent to (II) with m replaced by −m−1. That relation is obtained from (II) by applying the swap x ↔ y (which sends z to x⁻¹zx), then rotating and inverting with (I). So (I) and (II) imply that E.64.28 is a homomorphism of ⟨x,y,z ∣ xyz = 1⟩, hence of both central extensions (Ω(y)², Ω(z)³ resp. Ω(d)⁴ are central powers). Independently tested in characteristic quotients of F₂ (relatively free groups of the varieties of S₃, A₄, D₄ and the Heisenberg group mod 3: 54 shadows, λ ∈ {1,5,7,11} and {1,3,5,7}): E.64.28 holds in every shadow, while wrong variants fail (`check_gt_shadow_formulas.out`). |
| E64-10 (485-502) | B₃, B₄ commute with R₊, S; determinant one; 𝒟₃, 𝒟₄ characters | Verified (covariance; [k₁,k₂]u⁶ = z₃^mor and x⁴z₄³ = [ξ₁,ξ₂⁻¹] checked; commutative targets). |
| E64-11 (504-531, E.64.13) | Galois formula via NTY | Not verified: NTY 2010 Propositions 4.11-4.13 not freely accessible. Formal consistency: E.67 gives ε₃(𝒟₃(σ)) = ε₃(T_σ) = [σ moves r₀] (my step 9), so E.64.13 requires ρ_K(σ) ≡ [σ moves r₀] mod 2 on G_{Q^ab}; I could not test this without NTY's definition of ρ_K. |

## 4. E.67 step by step (`sections\E_orbifold_CM_agent.tex`)

| Step | Claim | Verdict and check (`check_e67_orbifold.out`) |
|---|---|---|
| E67-1 (99-113, E.67.3) | M, G are the quotients by [K,K]K³, orders 54 and 36 | Verified: xyz = 1, y² = 1, z³ = 1 (resp. z⁴ = 1); orders 54, 36; k₁ ↦ e₁, k₂ ↦ e₂; ξ₁ = xd³ ↦ e₁, ξ₂ = d²y⁻¹ ↦ e₂; x²y = e₁, z²y = e₂. |
| E67-2 (115-134, E.67.9) | B₃ acts on F₃(1,−1) as the identity for every multiplier-one gentle pair | Verified: (B₃ − I)e₁ = (I − R²)a; the image of I − R² is F₃w; B ∈ C(R) with (B − I)e₁ ∈ F₃w acts by +1 on w (enumeration). Needs only (I), (II) and E.64.28 at λ = 1. |
| E67-3 (136-142, E.67.1) | ε₃(C₃) = ε₃(𝒟₃); δ = ε₃(𝒟₃) + ε₂(𝒟₄) + ε₂(B₄) | Verified: formal from E67-2, E64-7 (C₃ ≡ T, C₂ ≡ W) and multiplicativity on the commutative centralizers. |
| E67-4 (144-166, E.67.4) | Gaussian table; B₄e₁ = e₁ − v | Verified: Ω(x²y) = (e₁ − v, I) for all v; v = (I − B)e₁ gives (0,0), (2,0), (1,1), (1,2); bit = v₂². |
| E67-5 (168-198, E.67.11-12) | Four Gaussian automorphisms with unique frames; nine framed Mordell targets; the six translation values | Verified: each x ↦ x, z ↦ ((I−B)e₁, S) extends to an automorphism of the order-36 group acting by B on V; frames unique; exactly nine Mordell targets; E.67.12 derived from the two- and three-cycle equations. |
| E67-6 (200-244, E.67.6) | Θ(K₆) = Θ(N′) = ℳ × 𝒢, order 3⁹, projection ranks 3 and 6 | Verified with N_B rebuilt from scratch (97 Schreier generators of ker q₁₂ on ⟨x,y⟩): commutator span of rank 9, stable under conjugation; equal to the displayed ℳ × 𝒢; Mordell images have even deck coordinate, Gaussian ones lie in V ⋊ ⟨−I⟩, so sixth powers die. Θ(F̂′) has rank 15 (Mordell projection 9, Gaussian 6); the Gaussian part equals 𝒢. |
| E67-7 (246-270) | In each of the 24 E.1 and 24 E.17 fibres exactly four attainable vectors: one Mordell target, all four Gaussian targets; E.67.7 coset formula | Universal part verified: the homogeneous equations meet ℳ in 0 (so at most one Mordell target per origin); of the 729 cosets of ℳ in Θ_M(F̂′) exactly nine contain a target, one each; all four Gaussian targets lie in 𝒢 = Θ_G(F̂′), so they are reached from every origin. Whether each of the 48 saved origins lies in one of the nine target cosets is a data claim that I did not recompute (it needs the saved words). E.67.7 is elementary once a correction exists. |
| E67-8 (272-279) | The pair generates M × G of order 1944 | Verified (enumeration). |

## 5. LM7 D.25 and LM7_PUSH E.1, as far as they define and identify the parity

- **Definition** (E.1 `E_agent.tex` lines 69-80; D.25 `D_cm_shadow.tex` lines 141-153): normalized lifts (mod 4 in V₄),
  the sign of A⁻¹ on ker(R − I) = F₃(1,−1), the class of β⁻¹ mod 3 in {±I, ±S}. Matches E.65 with V = I. Verified,
  with the 24/24 split recomputed.
- **D.25.1** (lines 56-75): Q(E₃[4]) = Q(i, r₀) = Q(x(E₄[3])). Verified by sympy: the halves of (−1,0) on E₃ have
  x = −(1 ± √3), y² = −9 ∓ 6√3; (√3(√3−1)r₀)² = −9 + 6√3; the product of the two y² is −27; ψ₃ = 3x⁴ − 6x² − 1 for E₄,
  a² = 1 + 2/√3, b² = 1 − 2/√3, (ab)² = −1/3, w = a + ib has w² = 2/√3 and w⁴ = 4/3 = r₀⁻⁴.
- **Sign rule** (lines 77-89): y(P) = (x(P)²/4)(x(P−Q₀) − x(P+Q₀)) with Q₀ = (0,1). Verified as an identity for every
  point P (sympy).
- **Identification with Galois restrictions** (lines 145-153, 208-211; E.1 lines 78-79): rests on LM7 D.15. Re-derived
  in Section 1, step 9, for every σ of multiplier one. Correct.
- LM7 D.15's model claims (λ = 1/2 gives the twist of E₄ by 2; λ₀ gives a quadratic twist of E₃ by the cube root
  constant) verified by sympy. Its proof is a sketch; the step that matters here is supplied above.

## 6. External results

| Source | Where used | Status |
|---|---|---|
| Herfort-Ribes 1985, Theorem B′ | E.58, E.61, E.64, E.65 (centralizers of s, r, d̄ meet the free kernel trivially; finite subgroups conjugate into factors) | Paper not accessible to me; referee A confirmed Theorem B′ from the GDZ scan (Section 4, p. 159) and its hypotheses for C₂ ∐ C₃. Independently, the needed consequence is derived above from Herfort-Ribes 1989, Theorem 3.2 (closed solvable subgroups), as quoted verbatim in Guralnick-Haran arXiv:1001.3599, and agrees with profinite Bass-Serre theory. Hypotheses hold (free profinite products of finite cyclic groups; free kernels are torsion-free). |
| Marin 2008, Lemmas 4.1-4.3 | E.65.15 | Opened (arXiv:0801.2507). Statement and normalization match; Marin's ρ restricts to −8ρ₂ on Galois elements, consistent with V_σ = U^{8ρ_σ}, ρ_σ = −κ₂(σ). |
| Nakamura-Schneps 2000 (preprint newGT.pdf) | E.61 (Definition 5.1, (IV), (R′)), E.64 ((1.1)) | Opened; all four places match (see the E.61 table). |
| Nakamura-Tsunogai-Yasuda 2010 | E.64.13; E.64.17 attribution; E.67 attribution of B₃ | Not freely accessible (Cambridge; author page refused the connection). E.64.17 verified directly; E.64.13 not verified. |
| Shpilrain 2002 | E.61 certificate (faithful representation) | Not needed: I used Artin's representation, faithful by Artin's theorem. |
| Endo-Kamada 2016; Margalit-Winarski; Boggi 2026 v6 | E.64.2, E.64.3 | Not opened. E.64.2's relators are the classical Birman-Hilden presentation; E.64.3's profinite form depends on Boggi. Not used by E.65 or E.67. |
| Basualdo Bonatto-Robertson 2026 | E.61 (descriptive sentence) | Not opened; not load-bearing. |

## 7. Scripts (all in `C:\Users\user\Documents\pro_intake_20261114\referee\checks\`, run with `python -I -B`)

- `check_e61_e65_matrices.py` / `.out`: 70 checks, 0 fails (E.61.4 mod 12, E.61.12-14, V₄, E.65.10-11, centralizers and
  normalizers at three, Marin intertwiner, E.58 bits, E.1 split).
- `check_e61_sewing_eta.py` / `.out`: 13 checks, 0 fails (η_m, E.61.15-17, E.61.8).
- `check_braid_identities.py` / `.out`: 60 checks, 0 fails (E.61.18-20, E.64.4-6, 14, 17-22, 29, 31, E.67.8).
- `check_gt_shadow_formulas.py` / `.out`: E.64.28 against 54 two- and three-cycle shadows in four characteristic
  quotients; holds in all; wrong variants fail.
- `check_e67_orbifold.py` / `.out`: 33 checks, 0 fails (E.67.3-6, 9-12, the order 1944, the target-coset structure).
- `check_d25_fields.py` / `.out`: 22 checks, 0 fails (D.25.1, the sign rule, the two Legendre CM fibres).
