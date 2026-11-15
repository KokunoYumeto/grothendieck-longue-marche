# Ghost symmetries, built into our work: the countersign

By Claude Fable 5.2 at effort high, 14 November 2026 (clock read at 17:33 UTC before writing). For the main session
(Claude Opus 5.5 at effort max) and the user.

Sources read for this: Olver, Sanders, Wang, *Ghost Symmetries* (`Papors\OS\Ghost Symmetries.pdf`, all nine pages);
Andrews, Connes, La Gatta, arXiv:2611.13129v1 (the introduction's paragraph on the uncertainty operator and
Theorem `thm:unc` only); `UNSTUCK_LM_EXPERT.md`, `UNSTUCK_POINCARE_FERMAT.md`, `USER_HUNCH_DELTA_20261114.md`; and
what I had read for `MOONSHINE_DICTIONARY_20261114.md`. The statements of our returns are used as our intakes give
them; I opened no return. Bookkeeping marks: **(paper)** = stated in the paper; **(ours)** = in our files;
**(exact)** = a computation or definition I can write out; **(mine)** = my construction, checked by no one;
**(conj.)** = conjecture.

The user's thread, which organises the file: the ghost is the countersign. It is whatever must be added to cancel
the ambiguity of integration; on our side, Δ and the ghosts of the stuck items are whatever cancels a
local-to-global sign. "The obstruction is the definition."

## 1. The paper's mechanism

- **Local theory (paper, (1)-(3)).** An evolutionary vector field v is a derivation that commutes with the total
  derivatives. It is determined by its characteristic Q = v(u), because v(u_J) = D_J Q for J ≥ 0. Brackets are
  computed on characteristics: [P, Q] = D_Q(P) − D_P(Q).
- **Nonlocal variables (paper, p. 2).** Allow u_J = D_J u with J negative, i.e. antiderivatives. D⁻¹ is defined up to
  a constant of integration.
- **The paradox (paper, Example 1).** For the characteristics 1, u_x, D_x⁻¹u the Jacobi sum computed on
  characteristics is 1, whatever the constants.
- **Ghosts (paper, Def. 3, Example 5).** On the nonlocal algebra a derivation is no longer determined by its
  characteristic: "there are nonzero evolutionary vector fields with zero characteristic". The bracket of the two
  *local* fields 1 and u_x is zero on every local variable and equals 1 on D_x⁻¹u. That ghost supplies the −1 that
  cancels the Jacobi defect. "The problem is not with the nonlocal vector field … but rather the local commutator."
- **Structure (paper, Thm 7, Cor. 8).** Ghosts depend only on the independent variables; every ghost is a
  combination, with constant coefficients, of basis ghosts γ_J, where γ_J(u_K) = χ^{J+K} and χ^K = D_K(1). Every
  field is (a field given by a characteristic) + (a ghost).
- **Calculus (paper, (13)-(17)).** Ghost symbols are carried formally: "No attempt should be made to substitute …
  inside the bracket (this would create exactly the paradox)". Ghosts commute with each other (15);
  [γ_J, u_K] = χ_{J+K} (17).
- **Constants of integration** "do not play a significant role" there: they can all be set to zero.

Two operators stand behind it: D (differentiate) and D⁻¹ (integrate), and the ghost lives in ker D, the constants.
Andrews-Connes-La Gatta do the same move with two projections P, P̂ = FPF and F² = 1: the obstruction "a function
cannot be both time-limited and band-limited" is made into the operator U = (1 − P) + (1 − P̂), and its two sectors
are the sign sectors F ≈ +1 and F ≈ −1 (their Theorem `thm:unc`).

## 1a. The principle, made precise enough to use

The user: local-to-global is forgetful, and the thing that cancels the obstruction "is whatever it needs to be …
because otherwise you couldn't have gone there". As a statement:

**Every problem on our list is a map ρ : Glob → Loc (restrict a global object to its local shadows) with three
pieces of data.**
1. **The forgetful part K** = what ρ forgets. The global objects over one local datum form a torsor under K. The
   elements of K are the ghosts.
2. **The obstruction group Ob** = the local data that come from nothing global, modulo those that do.
3. **A duality or exactness theorem** that identifies K with a computable group: the dual of an obstruction group,
   a kernel of a derivative, a lim¹, or the last term of a product formula.

Without 3 the principle is a tautology. With 3 it has teeth: a ghost is determined by the obstructions it cancels,
the ghosts form a known group, and "is there a ghost" becomes "is that group zero".

| Problem | ρ forgets | K (ghosts; fibres of ρ are K-torsors) | The theorem that makes it usable | What it pins down |
|---|---|---|---|---|
| The paper | the values on u_J, J < 0 | fields with zero characteristic; spanned by the γ_J; values in ker D | Thm 7, Cor. 8 (paper) | the missing Jacobi term, exactly |
| A profinite limit | everything not seen at a finite level | lim¹ of the constants (phantom classes) | Milnor's sequence 0 → lim¹ H^{n−1} → H^n(lim) → lim H^n → 0 | LM7 E.32, LM8 F.21: the phantom part of H²(G_ℚ, ℤ_ℓ(2)) (ours) |
| Kummer and Galois cohomology over ℚ | the global origin of local classes | Ш¹(M) | Poitou-Tate: Ш¹(M) is dual to Ш²(M*); the cokernel of H¹(ℚ, M) → ∏′H¹(ℚ_v, M) is dual to H¹(ℚ, M*) | sections: 3.4. The canceller of a local family is its Artin symbol |
| A product formula | which place carries the sign | μ₂: the last sign | Hilbert reciprocity | LM7 E.25: the sign at ∞ is the sign at 2 (ours) |
| Frames at level N (Δ) | the relative sign between the primes of N | Ob(N) = Z(SL₂(ℤ/N))/{±1} (2.3) | reciprocity of the frames of Galois elements (Gannon (6.3.4)); E.58 for existence | Δ_N, and with it the whole frame at level N from the single-prime frames and the multiplier (3.1) |
| The centralizer of A₅ (item 2.4) | whether two complements are conjugate discretely | ker(H¹(A₅, Γ[m]) → H¹(A₅, Γ̂[m])), over all m (`NOTE_BOGGI_ZALESSKII_STEP.md`, item 2) | missing: this is the gap of the two published proofs | 𝒦; equivalently a second profinite fixed point of A₅ (read-in, Prop. 2.3) |
| A1 | the p-part | the p-primary classes T_D on the covers (3.5) | missing in general; A.C2.7, A.C2.20 in cases (ours) | the collision, as an element of the ghost module M |

Two remarks that come out of the table.
- The frame row has both an existence theorem for ghosts (E.58) and a reciprocity that kills them on Galois
  elements; that is why Δ could be settled. The centralizer row and the A1 row have neither yet; the items GS3 and
  GS6 ask for them in this form.
- The group Ob(N) has extra elements exactly when 8 divides N, because (ℤ/8)^× is not cyclic. The classical
  failure of local-to-global for Kummer classes (Grunwald-Wang: 16 is an 8th power at every odd prime and not in
  ℚ) has the same cause **[memory]**. The 16 that LM6 F.45, F.46 select for tangential sections may be this one.

## 2. The construction on our side

### 2.1 Differentiation, integration, constants

Our objects are automorphisms Φ_F of B̂ = Ĉ₂ ⊔ Ĉ₃ = ⟨s, r⟩ with Φ_F(τ) = τ^λ, i.e. elements F = (λ, f) of ĜT₀ (ours).

- **Characteristic.** f, the cocycle: "an element is determined by its pair" (Grothendieck, cote 145, scan 11, as
  corrected in `INTAKE_20261114.md` §12) (ours).
- **Differentiation.** The two coboundary operators D_s(β) = β·s(β)⁻¹ and D_r(A) = A·ρ(A)⁻¹ for the rotations of
  order 2 and 3. The 2-cycle and 3-cycle relations say that f is in the image of each (ours: "g = A·ρ(A)⁻¹", "f is
  the Int(s)-coboundary of its own image").
- **Integration.** The frames β_F = D_s⁻¹(f), A_F = D_r⁻¹(f), with Φ_F(s) = β_F s β_F⁻¹, Φ_F(r) = A_F r A_F⁻¹ (ours).
  These are our nonlocal variables.
- **Constants.** ker D_s = C(s), ker D_r = C(r). In the full group they are ⟨s⟩ and ⟨r⟩ (Herfort-Ribes, as LM7_PUSH
  E.58 uses it): the true constants, harmless, as in the paper. In a quotient G of B̂ the kernels C_G(s), C_G(r) are
  larger. **The ghost values live in C_G(s)/⟨s⟩ and C_G(r)/⟨r⟩: constants at level G that are not constants globally.**
- **On the Lie algebra (exact).** On a module with an action of C₃ without invariants, (1 − ρ)² = −3ρ, so
  D_r⁻¹ = −(1 − ρ)ρ⁻¹/3; for C₂ on the −1 part, D_s⁻¹ = (1 − s)/2. Integration is division by 3 for the r-frame and
  by 2 for the s-frame. In a pro-ℓ quotient with ℓ ≠ 2, 3 the frames are determined by f: no ghosts. At 3 for r and
  at 2 for s the primitive exists and is unique only up to Tate cohomology of C₃, C₂. This is the statement of our
  intake "the s-frame is rigid at the prime 2 and the r-frame at the prime 3" read from the other side: the constants
  of the r-frame sit at the primes other than 3, those of the s-frame at the primes other than 2. In the paper the
  constant of integration of D_x⁻¹ is a function of the other variables; here it is a function of the other primes.

### 2.2 Ghosts, and the element of E.58

- **Definition (mine).** For an open normal U, 𝒰 = B̂/R_nil(U). F is a *U-ghost* if Φ_F is the identity on 𝒰. Its
  *ghost value* is the pair of its frames in (C_𝒰(s)/⟨s⟩) × (C_𝒰(r)/⟨r⟩), up to the common true constants. This is the
  paper's K-ghost: zero on all variables down to depth K, a constant on the next.
- **E.58 is the paper's Example 5 (ours, refereed).** The lift Φ of E.58 "is the identity modulo R_nil(H)", f lies
  in R_nil(H), and its r-frame is 5I modulo 12. Zero characteristic at level H, non-zero value on the nonlocal
  variable.
- **The structure theorem is half proved in our returns (ours).** The relative lifting theorem of E.58 says that
  the identity of 𝒰 with any triple of conjugators taken in the centralizers of the boundary values lifts. That is
  Theorem 7 in our setting: ghosts of level U are given by constants, and every admissible configuration of
  constants occurs. What is not in our files: that the ghost value determines the ghost modulo deeper ghosts.

### 2.3 The obstruction as an operator: the relative sign between two primes

This is the central construction (mine).

- **The local-to-global sign (exact).** SL₂(ℤ/12) = SL₂(ℤ/4) × SL₂(ℤ/3) has centre {±1} × {±1} = {1, 5, 7, 11}. The
  global sign −1 = 11 is the generic automorphism of an elliptic curve. In PSL₂(ℤ/12) the centre is
  {1,5,7,11}/{±1}, of order 2. Its non-trivial element ε is "−1 at one of the two primes and +1 at the other",
  without saying which: 5 = (+ at 4, − at 3) and 7 = (− at 4, + at 3) are the same element. It is the kernel of
  PSL₂(ℤ/12) → PSL₂(ℤ/4) × PSL₂(ℤ/3). So ε is exactly a sign that every single-prime test loses.
- **In general (exact).** For any level N the group of such signs is
  Ob(N) = {a ∈ (ℤ/N)^× : a² = 1}/{±1} = Z(SL₂(ℤ/N))/{±1}.
  It is trivial when N is a power of an odd prime, and of order 2^{k−1} when N has k odd prime factors (with extra
  elements when 8 divides N). In the congruence completion the group is (∏_p μ₂)/μ₂: one relative sign for each pair
  of primes. **Ghost values of this kind exist only where primes mix**: this is the experts' "one pattern" as a
  computation.
- **The operator (exact).** The scalar matrix a·I with a² = 1 is diag(a⁻¹, a), i.e. the diamond operator ⟨a⟩ of
  level N. It is an automorphism of X₁(N), defined over ℚ. The **sign idempotent** of a is e_a = (1 − ⟨a⟩)/2. On
  modular forms of level N it projects onto the nebentypus characters χ with χ(a) = −1. For N = 12 and a = 5 or 7
  (the same in Ob), e_ε projects onto the character (12/·) = (−4/·)(−3/·), the character of ℚ(√3); the product of the
  theta series of the Gaussian and the Eisenstein lattice lies there. Ob(12) is the group of X₁(12) over X₀(12).
  This is the analogue of U = (1 − P) + (1 − P̂): on objects of PSL type, (1 − ⟨7⟩)/2 + (1 − ⟨5⟩)/2 = 2e_ε, with
  eigenvalues 0 and 2 for the two sign sectors.
- **What Galois elements do (reciprocity).** By Gannon (6.3.4), σ ∈ G_ℚ acts on level-N data through
  G_σ = diag(χ(σ), χ(σ)⁻¹), which is the diamond operator of its cyclotomic character. So for a Galois element the
  central sign of the frame is the one its multiplier dictates. This is the product formula that makes the local
  signs cancel.
- **Definition by cancellation (mine, conj. that it agrees with E.65's Δ at N = 12).**
  For F ∈ ĜT₀ whose frames reduce to central elements at level N,
  **Δ_N(F) := (central class of the frame pair of F) · ⟨λ(F)⟩⁻¹ ∈ Ob(N).**
  Δ_N(F) is the countersign: the element of Ob(N) by which the frame must be corrected for the reciprocity of the
  previous point to hold. It is zero on G_ℚ by construction of the definition; it is ε on the element of E.58
  (λ = 1, frame 5I). An F with Δ_N(F) = ε acts on level-N objects as the reflection 1 − 2e_ε relative to what its
  multiplier predicts. Our returns already contain units of this shape: LM8 A.22's involution acts "by 1 − 2e, e the
  idempotent of a ℤ₅[ζ₃]-component", and the Longue Marche expert calls Δ "the sign of an idempotent of ℤ/12".
- **Why it is "not a number" (exact).** Over a given pair of single-prime frame classes (A₄, A₃), the frames at
  level 12 form a torsor under Ob(12): choosing lifts to SL₂(ℤ/4) and SL₂(ℤ/3) fixes the class only up to the
  relative sign. There is no preferred point unless something supplies one. The multiplier supplies one (the
  Galois-type frame); Δ is the difference from it. So Δ is a sign relative to a reference, a trivialisation of a
  μ₂-torsor, which is the user's "plus or minus zero, whichever is needed to cancel".

### 2.4 The rules of the ghost calculus, on our side

| Paper | Our side | Bookkeeping |
|---|---|---|
| Do not evaluate a ghost inside a bracket | Compose frames in B̂ (or in 𝒰 with the conjugators kept), never after reduction modulo a centralizer of a finite level. The frame of a product is A_F · Φ_F(A_{F′}) times a true constant | exact rule; it is what E.65 does by using Herfort-Ribes |
| (17): [γ_J, u_K] = χ_{J+K}, a ghost becomes visible one level deeper | A U-ghost becomes a visible automorphism on the relative pro-ℓ completion of a smaller V: the element of E.58 "acts on G₃ = B/[N,N]N³ nontrivially" | (ours) for E.58; in general there are no ghosts for all U at once, since ⋂ R_nil(U) = 1 |
| The ghost arises as the bracket of two local fields | Prime components: by D.50 and E.58 an F can be lifted prime by prime; the commutator of a 2-component with a 3-component is a ghost. The Fermat tower's D.46 is "a Galois commutator on the relative pro-2 part, the identity on every odd part" | (mine) as a general statement |
| (15): ghosts commute | True at a level where the centralizers are abelian modulo true constants (central signs: yes). Not automatic otherwise | conj. with that scope |
| Ghosts take values in the constants; u-dependent terms are never ghosts | The second expert's rule: every solved case was solved "by a map to a rigid target in which ghosts cannot exist". A target without constants kills the ghost | the same principle |
| Constants can be set to zero | **Breaks.** Our constants are arithmetic and form towers that need not be Mittag-Leffler. Besides the frame ghosts above (honest elements, like E.58) we have phantom ghosts: classes in lim¹ of the constants (LM7 E.32, LM8 F.21), with no element behind them. The paper has no second kind | where the translation stops |

## 3. What follows

### 3.1 A family of characters, of which Δ is the first (conj., mine)

- For every N, Δ_N extends to a continuous homomorphism ĜT₀ → Ob(N), zero on G_ℚ, compatible with N | N′.
- Each Δ_N is non-zero on ĜT₀ when Ob(N) ≠ 1 (E.58's theorem with U = Γ(N)/±1 and a central conjugator).
- Together they give Δ_∞ : ĜT₀ → (∏_p μ₂)/μ₂ (with the extra 2-part), and a closed subgroup
  ĜT₀^{rec} = ⋂ ker Δ_N ⊇ G_ℚ: the elements whose frames obey the reciprocity of the multiplier at every level.
- Ob(N) is the group of exact divisors of N modulo the Fricke involution (dictionary, row 7). So the "+e" of the
  moonshine groups and our ghost signs are indexed by the same set. The lambency note
  (`LAMBENCY_IN_AG_20261114.md`) uses this.

### 3.2 Δ on ĜT (LM7_PUSH E.3): the pentagon as the Jacobi identity (conj.: Δ_N = 0 on ĜT)

In B̂ the two frames are independent: s and r lie in no common finite subgroup and satisfy the single relation
sr = τ. That is why the relative sign is free on ĜT₀. In the paper the Jacobi identity with a third, nonlocal field
is what forces the ghost. Our third element is in Γ_{0,[5]} (mine; the facts on torsion from memory):
- Γ_{0,[5]} has torsion elements δ₀, δ₁, δ₂ of orders 5, 4, 3: the rotations with 0, 1, 2 punctured poles. Each has a
  rigid quotient (three special points), so each has a frame unique up to a finite group: three rigid frames
  Θ₅, Θ₄, Θ₃ for any F that acts on Γ̂_{0,[5]}.
- Forgetting the punctured pole sends δ₁ to the class of s (the square, harmonic) and δ₂ to the class of r
  (equianharmonic). So β_F and A_F are images of Θ₄ and Θ₃.
- δ₁ = δ₀σ₄ and the other braid relations tie Θ₃, Θ₄, Θ₅ in one group. The five-cycle relation is the statement
  that F acts there.
The prediction of the mechanism: these relations force the relative sign of the images of Θ₄ and Θ₃ to be the one
the multiplier dictates, i.e. Δ_N = 0 on ĜT; and the element of E.58 fails to extend to Γ̂_{0,[5]} exactly by ε.
The level-12 structure in which to compute is that of genus 2 (five points and infinity; Sp₄(ℤ/12) with the same
centre {1,5,7,11}).

### 3.3 The icosahedral centralizer 𝒦 (item 2.4)

- **In ghost terms (ours, read-in Prop. 2).** F ∈ 𝒦 iff C(τ) ∩ β_F C(s) ∩ A_F C(r) ≠ ∅ in Γ̂_{0,[12],1}: the two frames
  become one element modulo the constants of the larger group. So 𝒦 is the group of ghosts of the pair
  (B̂ ⊂ Γ̂_{0,[12],1}).
- **No sign here (exact).** The μ₂ at hand is the full twist, 1 → μ₂ → B₁₂(S²) → Γ_{0,[12]} → 1, and the inverse image
  of A₅ is 2I. A centralizing element could only act on 2I through a character 2I → μ₂, and 2I is perfect. So
  the countersign of this problem is not a sign: perfectness removes every abelian constant. The constants that
  remain are those of the dictionary's 4.2 (a torus, in the Eisenstein-lattice quotient).
- **Rule (15) as a test (conj.).** If 𝒦 is abelian, then, being a closed subgroup of the free profinite group
  closure(F_T), it is ∏_{p∈S} ℤ_p for a set S of primes; the Galois group of ℚ(√5) (which normalises it, by the
  read-in) acts through a character ψ. Either ψ is cyclotomic and 𝒦 lies in a cusp group of the tripod C_T, which
  is excluded because an element of 𝒦 dies in every rigid sub-configuration (second expert's lever), or ψ has the
  weight of a complex-multiplication character. The second case is the statement of LM8 G.20 for the tripod C_T:
  "a procyclic subgroup with open arithmetic normalizer lies in a conjugate of inertia". So: **𝒦 is trivial, or
  non-abelian, or a counterexample to the G.20 statement on C_T.**

### 3.4 Sections of the tripod

- **Our own countersign (ours).** LM7 E.25: κ₂(−1) ∪ κ₂(−1) = (−1, −1) is non-zero exactly at 2 and at ∞. The sign
  at ∞ is cancelled by the sign at 2: Hilbert's product formula. LM7's R3 already says the shape map must "add the
  prime 2".
- **The operator.** For local Kummer data (a_v) the obstruction to being global is its Artin symbol in G_ℚ^{ab}
  (ANABELIAN D.27: "orthogonal to all dual cyclic characters"). Definition by cancellation: the ghost
  characteristic of a system of local sections is the family of Artin symbols of its Kummer data on the tripod
  and on every cover that is again a tripod minus points. A genuine section has all of them zero.
- **Two kinds of ghost.** The frame kind (a section whose local data are those of a point at every prime but whose
  frames differ by a relative sign) and the phantom kind (lim¹). The first is where the dictionary's unit
  u = 1 − 1728/j and the reciprocity of D.27, D.28 act. The second is the uniformity in ℓ that both experts expect
  to resist.

### 3.5 A1

- **The ghost (ours).** A collision is a pair P ≠ Q that no prime-to-p quotient separates; on every prime-to-p cover
  D the class T_D = [Q′ − P′] is p-primary. T_D is the ghost characteristic: it lives in the part the tests leave
  out, the p-part of the Jacobians of the covers. A.C2.7 (a free deck orbit) is the statement that the basis
  ghosts are indexed freely.
- **The countersign.** Q′ = P′ + T_D in J_D: T_D is what must be added for the two points to be equal where the
  tests look. In characteristic 2, where A1 is open in genus two, T_D is 2-primary: a sign in the literal sense.
- **Construction (mine).** The ghost module M = lim over prime-to-p covers D of J_D[p^∞], with the norm maps, a
  module over the completed group ring of the prime-to-p group. Collisions between rational points are
  Frobenius-fixed, norm-compatible elements of M with free orbits; T_{PR} = T_{PQ} + T_{QR}. A1 is: there are none.
  The second expert's lever (a map to a p-rank-zero abelian variety) is a quotient of M that vanishes.

## 4. Items for GPT-6 Astra (ChatGPT Pro mode), each placed against the prompt it should join

**GS1. The ghost characters Δ_N.** Join: the LM7 continuation (`PUSH_ITEMS_LM7_CONTINUED.md`, with E.3) and
LM8_PUSH Part C. Prove or refute: (a) for F ∈ ĜT₀ acting trivially on PSL₂(ℤ/N), the frames reduce to elements of
the centre, and the class Δ_N(F) ∈ Ob(N) is a homomorphism on that subgroup; (b) the formula
Δ_N(F) = (central frame class)·⟨λ(F)⟩⁻¹ defines a continuous homomorphism on all of ĜT₀ (with the torsor of 2.3
made explicit), and Δ₁₂ is the Δ of E.65; (c) Δ_N = 0 on G_ℚ for every N, from the reciprocity of the frames at the
harmonic and equianharmonic points (the torsion representations of y² = x³ − x and y² = x³ + 1); (d) Δ_N is onto
Ob(N) on ĜT₀ for every N, by E.58; determine the image of Δ_∞ and the relations among the Δ_N; (e) the action of F
on the sector e_a of level-N modular forms and on the cusps of X₁(N). Background: the referee reports on D.50, E.58,
E.65; LM7 D.15-D.25; Gannon §6.3.3; this file.

**GS2. The pentagon as the Jacobi identity.** Join: the same continuation, as the route to E.3. Prove or refute:
(a) the three rigid frames Θ₃, Θ₄, Θ₅ in Γ̂_{0,[5]} for every F ∈ ĜT, with the centralizers of δ₀, δ₁, δ₂ computed
discretely and profinitely; (b) β_F and A_F are the images of Θ₄ and Θ₃ under forgetting a punctured pole; (c) the
relations among δ₀, δ₁, δ₂ and the half-twists force Δ_N(F) = 0 for every N, or produce an element of ĜT with
Δ_N ≠ 0; (d) the element of E.58 does not extend to Γ̂_{0,[5]}, with the relation at which it fails; (e) the same
computation in Sp₄(ℤ/12) for the genus-2 level structure. Background: Harbater-Schneps; Lochak-Schneps;
Gonçalves-Guaschi on torsion in sphere braid groups; the LM3 and LM3b returns' normalizer rows.

**GS3. 𝒦: abelian, procyclic, cuspidal.** Join: the LM4 successor, item 2.4 of `PUSH_ITEMS_20261114.md`, beside
R1-R12. Prove or refute: (a) closure(F_T) is free profinite of rank 2 and 𝒦 is a closed subgroup normalised by an
open subgroup of the Galois group of the field of definition of the icosahedral point; (b) [𝒦, 𝒦] is trivial; (c) if
𝒦 is abelian it is ∏_{p∈S} ℤ_p with a character ψ, and ψ is neither cyclotomic nor of the weight of a
complex-multiplication character, hence 𝒦 = 1; (d) if (b) fails, exhibit two non-commuting elements. Background:
`POINCARE_AND_A5_20261114.md`, `EXPERT_ON_BOGGI_A5.md`, `UNSTUCK_POINCARE_FERMAT.md` §4, LM8 G.10, G.19, G.20 and
LM8_PUSH Part A.

**GS4. The ghost structure theorem.** Join: LM8_PUSH Part B (torsion and multiplier-one elements on the tripod).
Prove or refute: for open normal V ⊂ U, the ghost value map from the U-ghosts to the conjugator triples in
B̂/R_nil(V) is injective modulo V-ghosts, and its image is the set of triples E.58 allows; the U-ghosts modulo
V-ghosts form an abelian group exactly when the centralizers at level V are abelian modulo ⟨s⟩, ⟨r⟩, ⟨τ⟩; the
commutator of a p-component and a q-component of two elements of ĜT₀ is a ghost, with its value computed.

**GS5. Sections: the countersign of a section.** Join: the successor on sections over ℚ (LM6 B.27 with ANABELIAN
Part D). Prove or refute: (a) for a system of local sections of the tripod, the Artin symbols of its Kummer data
on the tripod and on the open subcurves obtained from the maps λ ↦ 4λ(1 − λ), j, and the Fermat covers are zero
exactly when the system comes from a global section of the corresponding nilpotent quotient; (b) the frame-ghost
sections (local data of a rational point at every prime) are classified by relative signs, and each is excluded by
one of these symbols; (c) what remains is a class in the lim¹ of LM7 E.32 type; state it. Background: the two
final intakes of 14 November; LM7 E.25, E.32; ANABELIAN D.27-D.29.

**GS6. A1: the ghost module.** Join: the ANABELIAN successor (A1). Prove or refute: (a) the construction of M and
the additivity of T; (b) a collision gives a non-zero Frobenius-fixed norm-compatible element of M with free deck
orbits at every level; (c) M has no such element for curves of genus two in characteristic 2, starting with the
two classes over F₄ that the run left to certificates; (d) the lever of `UNSTUCK_POINCARE_FERMAT.md` §1 as a
vanishing quotient of M.

## 5. What is not done

I did not open E.65, D.50 or E.58 themselves; 2.3's identification of the frame with a diamond operator and of
Galois frames with the diamond operator of the multiplier rests on our intakes and on Gannon (6.3.4). The torsion
facts on Γ_{0,[5]} and the step "abelian closed subgroup of a free profinite group is ∏ ℤ_p" are from memory. No
item above has been linted as a prompt.
