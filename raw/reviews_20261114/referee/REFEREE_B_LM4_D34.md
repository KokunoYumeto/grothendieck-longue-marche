# Referee B: LM4 D.34 (global signs and the cusp cycle of a pure involution)

Referee: Claude Opus 5.5 at effort max (referee B), 14 November 2026, second task from the main session (Claude Opus
5.5 at effort max). Return checked: LM4_FINITE_GROUP_ACTIONS (snapshot 2026-11-14 01:56 UTC) by GPT-6 Astra (ChatGPT
Pro mode), `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0156Z_unzipped\`.
Read: `LM4_FINITE_GROUP_ACTIONS_paper.tex` lines 31654-31891 (D.34), 31206-31389 (D.32, statement and the
normalization paragraph), 30063-30262 (D.28), 225-241 (A.7); register rows D.34, D.32, D.28, A.7. Primary source
opened: Kochloukova-Zalesskii 2007, author manuscript (`mat.unb.br/~pz/arquivos/Claus3.pdf`). Referee A's report
`REFEREE_A_LM4_D32.md` (D.32: proved as claimed) was taken into account. Pro's program `pure_involution_d34.py` was not
run. My script: `checks\check_lm4_d34.py` / `.out` (34 checks, 0 fails; reads no file of the return).

## Verdict

**D.34: proved as claimed**, conditional on D.32 as stated (which referee A finds proved as claimed). I found no gap.

- Every nonidentity element of finite order of the pure three-cusp loop-outer group P is an involution with multiplier
  exactly −1 ∈ Ẑ^× at every prime; the same holds in ĜT₀ ≤ P; the multiplier-one kernels are torsion-free.
- For the normalized lift α(x) = x⁻¹, α(y) = f⁻¹y⁻¹f (f ∈ F′), the extension F ⋊_α C₂ has exactly three F-conjugacy
  classes of sections; each fixed subgroup has H¹(−, F₂) = 0; the classes form a triangle whose edges are the three cusp
  normalizers; f = h⁻¹α(h) with h ∈ F′; α inverts x and hyh⁻¹; x ↦ x, y ↦ hyh⁻¹ is an automorphism of every maximal
  pro-p quotient.

The decisive reasons:
1. *A genus-zero lemma for any n ≥ 3 cusps* (lines 31687-31775). For an involution β of
   F_n = ⟨c₁,…,c_n ∣ c₁⋯c_n = 1⟩^ preserving every cusp class with common multiplier μ, μ₂ = −1:
   - each cusp normalizer contains exactly two classes of involutions, and their images in H₁(F_n ⋊ C₂, F₂) = V ⊕ F₂
     differ by the cusp vector [c_i];
   - the profinite Brown theorem (Kochloukova-Zalesskii, Theorem 2 with §1.1) bounds the number of section classes,
     each counted with 1 + dim H¹ of its fixed subgroup, by n;
   - since the n cusp vectors have only the one relation Σ[c_i] = 0, the incidence graph must be a simple n-cycle;
   - this exhausts the bound, so there are exactly n classes, each with H¹ = 0.
2. *Odd primes* (lines 31776-31851). If λ_q = 1 for an odd q, then α preserves the kernel N of the degree-q cyclic cover
   x ↦ 1, y ↦ 0. That cover is a sphere with q + 2 holes, and α restricts to a pure involution of N with λ₂ = −1. By the
   lemma its section classes form a (q+2)-cycle. Conjugation by x induces an automorphism of that cycle of order exactly
   q (it fixes the two edges over x and z and cycles the q edges over y). But q does not divide the order 2(q+2) of
   the cycle's automorphism group. So λ_q = −1.
3. *n = 3* (lines 31853-31883). The three classes are s, x^{e₂}s, y^{e₂}fs, separated by their images in H₁. Since
   fs is an involution with the image of s, fs = h⁻¹sh, which is f = h⁻¹α(h). Abelianizing gives −2[h] = 0, so h ∈ F′.

Not conclusions of D.34, and the claim says so (lines 31679-31682): surjectivity of x ↦ x, y ↦ hyh⁻¹ on the full F,
and conjugacy of the involution to complex conjugation.

### What D.34 gives for Δ (LM7_PUSH E.65) on elements of finite order

My E.65 report (`REFEREE_B_E61_E65.md`) finds Δ: ĜT₀ → F₂ a well-defined continuous character, vanishing on G_Q,
with Δ = δ on the multiplier-one part ℋ and Δ(F) = δ(Fσ⁻¹) for any Galois σ of the multiplier of F.
- **All torsion is visible only through multiplier −1.** By D.34 every torsion element τ ≠ 1 of ĜT₀ is an involution
  with λ(τ) = −1, and ℋ is torsion-free. So δ itself is never evaluated on a torsion element.
- **Exact formula.** Complex conjugation is c = (−1, 1) ∈ G_Q (base point 01⃗; normalized f = 1). With the group law
  (λ, f)(μ, g) = (λμ, f·α_{(λ,f)}(g)) used both by LM4 (D.32, line 31337) and by E.65 (composition Φ_FΦ_G), one gets
  τc = (−1, f_τ)(−1, 1) = (1, f_τ). Hence
  **Δ(τ) = δ((1, f_τ))**: the CM parity of the multiplier-one gentle pair with the same second coordinate as τ.
  (That (1, f_τ) lies in ĜT₀ is consistent with the hexagon at m = 0 and m = −1 being equivalent under the two-cycle
  relation; I proved this equivalence in the E.65 report, step E64-9.)
- **When it vanishes.** Δ(τ) = 0 whenever τ is conjugate in ĜT₀ to c, because Δ is a class function that vanishes
  on G_Q. D.34 does not prove this conjugacy; it explicitly leaves it open (line 31681). Its h with f_τ = h⁻¹α_τ(h)
  would give the conjugacy only if the pair built from h were itself an element of ĜT₀, which is not shown.
- **No cheap constraint.** The dihedral relation c(τc)c⁻¹ = (τc)⁻¹ puts no condition on δ(τc). By E.65.16, conjugation
  by the frames of c inverts every element of C₆ = ⟨−I⟩×⟨R₀⟩ and of C₄ = ⟨S⟩ (the normalizing matrices have
  determinant −1), and ε₃, ε₂ are invariant under inversion.

So D.34 reduces "Δ on finite-order elements" to one question: is δ((1, f)) = 0 for every f such that (−1, f) is an
involution of ĜT₀? A positive answer would follow from the conjugacy of every involution to (−1, 1), which is the
part of the Lochak-Schneps torsion question that D.32 and D.34 leave open. D.34 does not settle Δ on torsion.

---

## Step by step (`LM4_FINITE_GROUP_ACTIONS_paper.tex`)

### The genus-zero lemma (any n ≥ 3)

| Step (lines) | Claim | Verdict and how checked |
|---|---|---|
| 31687-31697 | β² = 1 gives μ² = 1, each μ_q = ±1 | Verified. β²(c_i) is conjugate to c_i^{μ²} and equals c_i; A.7 (normalizer of a cusp group is itself) gives c_i^{μ²} = c_i, and L_i ≅ Ẑ is torsion-free. |
| 31699-31704, (D.34c) | 1 → L_i → N_{E_n}(L_i) → C₂ → 1 | Verified. Kernel: N_{F_n}(L_i) = L_i (A.7; F_n is the completion of a hyperbolic genus-0 group with n ≥ 3 punctures, so A.7 applies). Surjectivity: if β(c_i) = hc_i^μh⁻¹, then h⁻¹β normalizes L_i. |
| 31706-31713 | a_i² = c_i^{v_i}, (μ−1)v_i = 0, solve (1+μ)u_i = −v_i, b_i = a_ic_i^{u_i} an involution | Verified by hand: (v_i)_q = 0 where μ_q = −1 (including q = 2); where μ_q = 1, q is odd and u_q = −(v_i)_q/2; b_i² = c_i^{(1+μ)u_i + v_i} = 1. |
| 31715-31725, (D.34d) | involutions in b_iL_i modulo L_i-conjugation ≅ ker(1+μ)/(1−μ)Ẑ ≅ F₂; representatives b_i, c_i^{e₂}b_i | Verified: (b_ic^t)² = c^{(1+μ)t}; conjugation by c^w shifts t by −(1−μ)w; the quotient is Z₂/2Z₂. Checked numerically in a truncation of Ẑ (2⁶3⁴5³7²) for all eight sign patterns with μ₂ = −1; c_i^{e₂}b_i = b_ic_i^{−e₂} is the second class. |
| 31727-31736, (D.34e) | β acts trivially on V = H₁(F_n, F₂); H₁(E_n, F₂) = V ⊕ F₂; the two local classes are globally distinct | Verified: μ is odd, so [c_i^μ] = [c_i]; for a split extension H₁ is coinvariants plus H₁(C₂); the two images differ by [c_i] ≠ 0. |
| 31738-31752, (D.34f) | Σ_{[Q]}(1 + dim H¹(C_{F_n}(Q), F₂)) = dim H^k(E_n, F₂) ≤ n for k > 1 | Verified against Kochloukova-Zalesskii 2007 (opened): Theorem 2 (Scheiderer, Cor. 12.19) needs no Z/p × Z/p and an open subgroup of finite cd_p = d; here every finite subgroup injects into C₂ (F_n torsion-free) and cd₂(F_n) = 1. §1.1 eq. (5)-(6): N(S) = C_H(S) × S and the Künneth formula give the sum, the Hochschild-Serre bound gives ≤ 1 + (n−1) = n. Closed subgroups of F_n have cd₂ ≤ 1, so each summand is 1 + dim H¹. Every order-two subgroup is a section, and E_n- and F_n-classes agree since E_n = F_nQ. |
| 31754-31769, (D.34g) | the incidence graph is a simple n-cycle; exactly n classes; H¹(C(Q), F₂) = 0 for every section | Verified: edge vectors around a cycle sum to 0; the only zero-sum nonempty set of cusp vectors is the full set (checked for n = 3,…,7); not a forest (n edges need n+1 vertices); a simple cycle through all n edges has n vertices; the bound is then exhausted. |
| 31770-31775 | naturality under automorphisms permuting cusps | Verified: such an automorphism carries N(L_i) and its two classes to those of the image cusp. |

### Odd primes

| Step (lines) | Claim | Verdict and how checked |
|---|---|---|
| 31776-31780 | D.32 gives order two, the normalized lift α, λ₂ = −1 | Taken from D.32 as stated (referee A: proved). α is an actual involution because the normalization (D.32, lines 31314-31340) is a homomorphic section into Aut F; I rechecked that paragraph: uniqueness uses C(x^λ) = closure⟨x⟩ (A.7) and f ∈ F′. λ² = 1 because α² = 1. |
| 31780-31802, (D.34h-i) | χα = χ, N α-invariant; the cover has boundaries 1, q, 1 over x, y, z, degrees q, 1, q, genus 0 | Verified (script, q = 3, 5, 7, 11, 13); Euler characteristic −q with q+2 boundaries gives genus 0. |
| 31804-31822, (D.34j) | α|_N is pure with multiplier λ; it acts by −1 on H₁(N, Z₂) | Verified: x^q is fixed up to power; z^q: the single boundary over z means N·closure⟨z⟩ = F, so any F-conjugate of closure⟨z^q⟩ is an N-conjugate; over y: k_i = x^{λi}f⁻¹x^{−i} ∈ N because χ(f) = 0 and λi ≡ i mod q; the conjugacy α(x^iyx^{−i}) = k_i(x^iyx^{−i})^λk_i⁻¹ checked by substitution. |
| 31824-31840, (D.34k) | E/N = C_q × C₂; conjugation by x acts on the section classes of E_N with order dividing q, fixes the edges x^q, z^q and cycles the q edges over y | Verified: χα = χ makes the action of C₂ on F/N trivial; x^q ∈ N acts trivially on N-classes; the edge permutation is a q-cycle plus two fixed edges, hence order exactly q. |
| 31842-31851 | contradiction with |Aut(C_{q+2})| = 2(q+2) | Verified (script): the dihedral group of the (q+2)-cycle has no element whose edge permutation has type (q,1,1), and q ∤ 2(q+2). (For odd q+2 a reflection fixes exactly one edge, a nontrivial rotation none.) |

### The case n = 3

| Step (lines) | Claim | Verdict and how checked |
|---|---|---|
| 31853-31859 | fα(f) = 1; fs is an involution inverting y | Verified: the second coordinate of α² is fα(f), and α² = 1 forces it to centralize y and lie in F′, hence to be 1 (A.7); (fs)² = fα(f) = 1; (fs)y(fs)⁻¹ = fα(y)f⁻¹ = y⁻¹. |
| 31860-31865, (D.34l) | s, x^{e₂}s, y^{e₂}fs are involutions with images (0,0,1), (1,0,1), (0,1,1) and represent the three classes | Verified: squares are x^{e₂}x^{−e₂} = 1 and fα(f) = 1; images distinct (script); the triangle's edge vectors are [x], [y], [x]+[y] = [z]. |
| 31864-31869, (D.34b) | fs = h⁻¹sh, so f = h⁻¹α(h); h ∈ F′ | Verified: the class of an involution is determined by its image, and fs has the image of s; h⁻¹sh = h⁻¹α(h)s; α acts by −1 on F^ab, so [f] = −2[h] = 0 and [h] = 0 in the torsion-free Ẑ². |
| 31870-31883 | α inverts hyh⁻¹; x ↦ x, y ↦ hyh⁻¹ is an automorphism of each F^{(p)} | Verified: α(h) = hf gives α(hyh⁻¹) = hy⁻¹h⁻¹; same abelian images, so Frattini generation and Hopficity of finitely generated pro-p groups give an automorphism. No full-profinite surjectivity is claimed. |
| 31885-31890 | program | Not run; replaced by my checks. |

## Dependencies, as used

| Dependency | Use in D.34 | Status |
|---|---|---|
| D.32 | order two and λ₂ = −1 for torsion; the normalized lift | Taken as stated; referee A: proved as claimed. The odd-prime part of D.34 holds for every involution of P with λ₂ = −1 independently of D.32. |
| A.7 (Known) | N_Π(L_i) = L_i, C(y) = closure⟨y⟩, torsion-freeness, for genus-0 hyperbolic types | Used exactly as stated; its hypotheses (hyperbolic type, n ≥ 3 cusps; the cover N has q+2 ≥ 5) hold. Not re-derived from its sources (Mochizuki-Tamagawa, Mochizuki, Nakamura). |
| D.28 | the method of the Brown calculation | D.34 applies the same computation at p = 2 directly; I checked it against Kochloukova-Zalesskii. D.28's own conclusions are not used by D.34. |
| Kochloukova-Zalesskii 2007, Theorem 2 and §1.1 | (D.34f) | Opened; hypotheses hold (above). |
