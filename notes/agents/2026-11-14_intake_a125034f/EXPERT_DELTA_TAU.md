# Δ and the external zero τ_G of the globalization note

By Claude Fable 5.2 at effort max (field expert of the Longue Marche line, agent a125034fd35557818), 14 Nov 2026.
Read for this: the user's note `Papors\Chatnotes\globalization_note.tex` in full; my own pages on Δ
(`EXPERT_IMPLICATIONS_E65_LM.md`, its part 2, the two consults). No literature. The chain behind Δ (LM7_PUSH D.50,
E.58, E.65; LM4 D.32, D.34) is by GPT-6 Astra (ChatGPT Pro mode), refereed by Claude Opus 5.5 at effort max.
Notation: `τ_G` is the external zero of the note; `τ` stays an involution of multiplier −1; `c` is complex
conjugation; `ℋ` is the multiplier-one part of `ĜT₀`. "Hunch" marks what is mine and unproved.

## Answer in short

The resemblance has one exact core, and the rest is shared shape.

**The core: both are a non-trivial idempotent on a connected base, and Δ is the sign of one.**
- In `S = G(Z)` the integer `0` is an idempotent (`0·0 = 0`) different from the zero `τ_G` and from `1`. In the
  model `S ≅ D ⊂ Z × B` the idempotents of `Z × B` are the four corners `(0,0), (0,1), (1,0), (1,1)`; `S` contains
  three of them, `τ_G = (0,0)`, `0 = (0,1)`, `1 = (1,1)`, and misses `(1,0)`. On `Spec S` the idempotent `0` is the
  indicator of one point: it is `1` in the stalk `B` at the new generic point `{τ_G}` and `0` at every point of
  `Spec Z`. The spectrum is connected (a chain of specializations) and still carries this idempotent. In a ring that
  cannot happen; it happens here because `S` has no subtraction, so the complement `1 − 0` does not exist.
- In the Δ picture the element of E.58 has `r`-frame of class `5·I` modulo 12 and trivial `s`-frame (referee A).
  Now `Z/12 = Z/3 × Z/4` has the idempotents `0, 1, 4, 9`, and `e ↦ 1 − 2e` sends them to the four square roots of
  one, `1, −1, 5, 7`. So **`5 = 1 − 2·4` is the sign of the idempotent `4`, the one that is `1` at the prime 3 and
  `0` at the prime 2.** The two parities are the two components of a sign; Galois has the signs `±1` of the trivial
  idempotents `0, 1` (the diagonal); the classes with `Δ = 1` are the signs `5, 7` of the two mixed idempotents.
  Read on the modular orbifold: the frame sign is a function on the two elliptic points, constant for Galois,
  non-constant for E.58's element, although the orbifold is connected. For Galois it is constant because both signs
  come from one field; `ĜT₀` lacks the relation that ties the two frames.
- So in both cases a weaker structure (a semiring; automorphisms with only the 2-cycle and 3-cycle relations) lets a
  connected object carry an idempotent that the stronger structure (a ring; Galois) forbids, and the bit is that
  idempotent. The matching of corners: `τ_G` and `1` (the trivial idempotents of `S`) with the Galois diagonal; the
  integer `0` (the mixed idempotent `S` has) with one off-diagonal class; the missing corner `(1,0)` with the other
  one. `S` has one mixed corner, `ĜT₀` has both.

**Lead (e), `B` against `F₂`: this is the hinge, not the end.** The idempotents of a commutative ring form a
Boolean algebra, and it carries both structures at once: join and meet, which is the Boolean semiring (`1 + 1 = 1`),
and symmetric difference and meet, which is the Boolean ring (`1 + 1 = 0`). The map `e ↦ 1 − 2e` turns symmetric
difference into the product of signs. An idempotent absorbs (`e·e = e`, as `τ_G` and `0` do); its sign is a unit of
order two and its values form a coset (as `Δ = 1` does). One object holds both: the group semiring `B[F₂]`, which is
also the semiring of subsets of `F₂` under union and product. It has four elements `∅, 1, a, 1 + a` with `a² = 1`:
`∅` is a zero of the kind `τ_G` is (identity for union, absorbing for product), `{1, a}` is the group `F₂`, and
`1 + a` is an idempotent that absorbs the non-empty elements. Galois lands in `{∅, 1} ≅ B`; `ĜT₀` reaches `a`.

## 1. What corresponds to what

| In the note | In the Δ picture | Kind |
|---|---|---|
| `S ↪ Z × B`, visible coordinate `p`, bit `b` | `ĜT₀ → V × F₂`, `V` the image in all pro-ℓ, nilpotent and graded quotients, bit Δ | shape; see the first difference below |
| the kernel `A = {0, τ_G} ≅ B` of `p` | the part of `ĜT₀` that `V` does not see, modulo `ker Δ`: two classes, the identity and E.58's element `(1, f)`, `f` in the nilpotent residual | shape (lead (a)) |
| the plain quotients `Z/n` merge `τ_G` with `0`; the globalized quotients `G(Z/n)` keep it | quotients through `V` merge `(1, f)` with `1`; the quotients `V_n × F₂` keep it | shape |
| the idempotents `τ_G, 0, 1`; `0` is the indicator of the new generic point | the frame sign as an idempotent of `Z/12`; non-trivial exactly when `Δ = 1` | **exact** (the core above), once item T1 is proved |
| `Z` is the universal ring under `S`: imposing cancellation merges the two zeros | imposing a compatibility kills the bit: Galois; by my hunch H1 also section 47 (`C^φ`); for the pentagon it is E.3 | shape |
| `Frac(S) ≅ B`: collapse everything arithmetic, one bit is left | the continuous characters of `ĜT₀` to `F₂` that vanish on Galois | a statement (item T2); lead (c) |
| `S^{±1} = {0, τ_G}`: the sign fixes both zeros | `c` acts on `ℋ`; the classes of involutions are `H¹(⟨c⟩, ℋ)`, and Δ is a function on them | a statement (item T3); lead (b) |
| the prime ideals `P_Σ` of the monoid `(Z, ×)`, one for each set of primes | the idempotents of `Ẑ`, one for each set of primes: the source of every prime-mixing element we have (LM8 A.22, LM4 D.29, E.58) | exact as a remark, and the reason the two pictures look alike |

No counterpart on the Δ side: the absorbing law (`n·τ_G = τ_G`); the classification of ideals and congruences; the
Krull dimension 2; `0` prime and not irreducible; the stalks; the class group. No counterpart in the note: the
frames and the two CM curves; the field `Q^ab(3^{1/4})`; the pentagon; section 47.

Two differences that limit the leads.
- **Lead (a) holds at the neutral fibre only.** In `S` only the fibre of `p` over `0` has two points; over `n ≠ 0`
  the bit is forced. In a group all fibres look alike: by E.58 the image of `ĜT₀` in `V × F₂` is the whole product,
  so Δ is free over every visible element. The proper sub-object of the product is the Galois image, where the bit
  is tied to the visible data.
- **`S` is detected by `Z` and one bit; `ĜT₀` is not.** `S ↪ Z × B` is injective. The part of `ĜT₀` that `V` misses
  is far larger than one bit (LM7 D.40–D.44: over bases with non-abelian simple part the image is a full fibre
  product). Δ is one bit of it, the first one found. So lead (c) cannot mean "one bit detects everything"; its
  provable form is item T2, and I expect more than one character there (the frame at the point of order five, hunch
  H4 of my implications page).

## 2. The leads, one by one

- **(a)** Kept as shape, with the two limits above. The exact version is the idempotent statement (T1).
- **(b)** Kept, and it gives the most. The involutions of `ĜT₀` over `c` are the `g·c` with `g ∈ ℋ` and
  `g·(cgc⁻¹) = 1`; Δ is zero on the conjugates of `c`. **Hunch: an involution with `Δ = 1` exists, and it is "two
  complex conjugations glued across the primes 2 and 3".** Take `γ ∈ G_Q` with `γ(3^{1/4}) = i·3^{1/4}`. Then
  `γcγ⁻¹` is a complex conjugation and `σ = γcγ⁻¹c` is a Galois element of multiplier one that moves `3^{1/4}`
  (in the dihedral group of `Q(i, 3^{1/4})` it is the square of the rotation). If the product decomposition of E.58
  lets one take the part of `σ` on the 2-side with the identity on the 3-side, and if that operation commutes with
  conjugation by `c`, the result `σ₂` has bits `(1,0)` and satisfies `σ₂·(cσ₂c⁻¹) = 1`; then `σ₂c` is an involution
  with `Δ = 1`, a second conjugacy class. This is the note's doubled fixed point of the sign in the group: one class
  for each idempotent, the trivial ones giving the Galois conjugations. It would also be the tripod form of LM4
  D.29 (a conjugation at one prime only), with multiplier `−1` at every prime as LM4 D.32 demands.
- **(c)** Kept as item T2. The analogue of `Frac(S) ≅ B` is the quotient of `ĜT₀` by the closed normal subgroup
  generated by Galois, and its characters. For the two elliptic points alone I expect exactly one bit (my H2: the
  maximal abelian extensions of `Q(i)` and `Q(√−3)` meet in one quadratic extension of `Q^ab`).
- **(d)** Corrected and made exact: not "`S` in `Z × B` against the parities onto `F₂ × F₂`", but the four
  idempotents of a product of two factors. `S` has three corners, Galois two, `ĜT₀` four.
- **(e)** Resolved above: join against symmetric difference on one Boolean algebra, `e ↦ 1 − 2e`, and `B[F₂]`.

## 3. What is mathematics here, and what it gives

- **Mathematics:** T1 (Δ as the sign of an idempotent of `Z/12` built from the frames); T2 (all characters trivial
  on Galois); T3 (involutions with `Δ = 1`); T4 (the same splitting inside `ĜT`); the elementary statements about
  `G(R)` in T5. **Shape only:** the two families of congruences against visible and Δ-keeping quotients; the Krull
  chain against `G_{Q_p} ⊂ G_Q ⊂` a larger group; "the universal ring merges the zeros" against "a compatibility
  kills the bit".
- **For E.3 (Δ on `ĜT`).** The note does not decide it. The idempotent form gives the finite search a sharp target:
  Δ is not zero on `ĜT` exactly when some element of `ĜT` has a frame sign `5` or `7` modulo 12, that is, when the
  pentagon tolerates a sign that differs at the primes 2 and 3. And it names the mechanism to test (T4): whether
  `ĜT` has the splitting across primes that E.58 proves for `ĜT₀`.
- **For `C^φ` of section 47.** Only the shape "imposing the missing law merges the two". It supports the hunch that
  `C^φ` lies in `ker Δ` and adds no argument.
- **For the involutions.** The most concrete gain: a candidate second conjugacy class (lead (b)), with a
  construction to check.

## 4. Prompt items for GPT-6 Astra (ChatGPT Pro mode), each to be proved or refuted

- **T1.** For `F ∈ ℋ` let `(ε₃(T_F), ε₂(W_F))` be the two frame parities of LM7_PUSH E.65. There is a homomorphism
  `u : ℋ → μ₂(Z/3) × μ₂(Z/4) = {1, 5, 7, 11} ⊂ (Z/12)^×` whose two components are these parities, with
  `u(G_{Q^ab}) = {±1}` and `u = 5` on the element of E.58; hence `Δ(F) = 1` if and only if the idempotent
  `(1 − u(F))/2` of `Z/12` is `4` or `9`. Determine the ring in which the two frames are naturally one sign (the
  product of the reductions of `Z[ζ₃]` and `Z[i]` at the levels where the parities are read), and prove that the
  sign is constant on the two elliptic points for every automorphism compatible with the harmonic covering
  `w = 4λ(1 − λ)`.
- **T2.** Determine the group of continuous characters `ĜT₀ → F₂` that vanish on the Galois image, and the
  abelianization of the quotient of `ĜT₀` by the closed normal subgroup generated by the Galois image. Decide
  whether Δ generates the first group.
- **T3.** `ĜT₀` contains an involution with `Δ = 1`. Test the construction of lead (b): decide whether the product
  decomposition of LM7_PUSH E.58.2 commutes with conjugation by `c`, and whether `σ₂c` is an involution for
  `σ = γcγ⁻¹c`, `γ(3^{1/4}) = i·3^{1/4}`. Then determine `H¹(⟨c⟩, ℋ)`, the map to `F₂` given by Δ, and the conjugacy
  classes of involutions of `ĜT₀`.
- **T4.** `ĜT` contains an element whose frame sign modulo 12 is `5` or `7`. Equivalently (E.65), Δ is not zero on
  `ĜT`. Decide first whether the decomposition of E.58.2 holds with the pentagon, at the smallest level of the
  five-point group that mixes the primes 2 and 3.
- **T5 (the note's side; short).** For a commutative ring `R`: the idempotents of `G(R)` are those of `R` together
  with `τ_G`; `R` is the universal ring under `G(R)`; `G(R) ↪ R × B` with image `{(0,0)} ∪ R × {1}`; `Spec G(R)` is
  `Spec R` with one new generic point, and the idempotent `0` is its indicator. For a profinite group `𝒢` with a
  continuous character `Δ : 𝒢 → F₂` and a closed subgroup `Γ ⊂ ker Δ`: the semiring of closed subsets of `𝒢` maps
  onto `B[F₂]`, `Γ` lands in `{∅, 1}`, and the completed group ring of `𝒢/ker` maps onto two copies of the visible
  group ring glued modulo 2. State which statements of the note have an analogue under this map and which do not.

**Where they go.** T1, T2 and T4 belong in the successor of LM7_PUSH (the prompt on Δ; items 1, 5 and 8 of my
implications page are their neighbours). T3 belongs in LM8_PUSH Part B (task B.5, the involutions), or in the same
successor if LM8_PUSH is split as I proposed. T5 is small; it can ride with the successor as a closing Part, or be a
note of ours. None belongs in ANABELIAN_149_PUSH. One neighbour does: the same shape on the side of sections (two
sections that every pro-ℓ quotient identifies, a twisted `H¹` between them) is Lead 19 and task D.8 of LM8_PUSH,
which the consolidation plan moves to ANABELIAN_149_PUSH Part D.

## What I did not do

No source was opened beyond the note. T1's statement about the ring where the two frames are one sign rests on
referee A's value `q(A) = [5I]` and on the intake's description of the parities; I have not read E.65's own
definition of `ε₂(W)`, and the two parities are read on two different frames, so "one sign in `Z/12`" may need the
adjustment T1 asks for. The involution of lead (b) is a hunch with a construction, checked by no one. My context is
at about 73 %; I edited no prompt.
