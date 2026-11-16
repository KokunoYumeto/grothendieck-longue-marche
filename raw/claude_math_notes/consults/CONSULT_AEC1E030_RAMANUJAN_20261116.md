# Consult: Ramanujan's signatures as the structure common to S6, Δ and the eta and theta series

By Claude Fable 5.2 at effort high (agent aec1e030), for the main session (Claude Opus 5.5 at effort max). Clock
read: 16 November 2026, 00:16 UTC.

**What I opened.** Of the elliptic-expansion paper (`…\Proof of the elliptic expansion Moonshine Conjecture of
Căldăraru, He, and Huang\main.tex`): the abstract, the definition of the expansions at τ = ρ and τ = i with their
displayed coefficients, the remark on hypergeometric inversion, Theorem `main`. Nothing else: not
Berndt-Bhargava-Garvan, not the AC26 construction, not Engel, not the main session's §19. The S6 facts are used as
the brief states them.

Marks: **[CHH-proof]** = read in that paper. **(exact)** = written out here; series identities checked by a script
against the paper's displayed coefficients. **(mine)** = my identification or argument, checked by no one.
**[memory]** = not checked against a source.

## Summary

1. The four signatures are the four genus-zero subgroups of the modular group of index 12/s; each Fermat-type
   identity is x + (1 − x) = 1 on such a tripod. Theorem-level, classical; I state it from memory.
2. The S6 sphere condition is exactly a statement about the Hodge bundle: the base orbifold S²(3,4) is the weighted
   projective line P(3,4) with coordinates (E₆^{1/2}, E₄), J*λ = O(1), every Seifert bundle on it is the circle
   bundle of J*λ^k, and p = ±k. So p mod 12 is the class of the bundle in Pic(M_{1,1}) = ℤ/12, and "sphere" is
   k = ±1. (mine, exact given the brief's description of S6.)
3. S6's class and Δ use the same group (ℤ/12)^×/{±1} with its character χ₁₂, and in both the condition is "the sign
   at 3 and the sign at 4 agree". But S6's class is abelian data (a character of SL₂(ℤ), i.e. a power of the eta
   multiplier), and Δ is not (first consult, (c)2). No map from one to the other is established.
4. Elliptic-expansion moonshine says: in the flat coordinate, j at the equianharmonic point is the Hesse (level 3)
   function and at the harmonic point the Legendre (level 2) function centred at λ = 1/2. It gives each of the two
   points a rational local frame, separately. It fixes the coordinate of S6's multiplicity-3 point; it does not
   bear on the relative sign Δ.

## (a) The structure

**A1. Signatures as groups [memory for the list; (exact) for the count].** The period ₂F₁(1/s, 1 − 1/s; 1; x) is a
weight-one object on a genus-zero group with three special points:

| s | group | index in PSL₂(ℤ) | special points | weight-one period z_s | the identity |
|---|---|---|---|---|---|
| 2 | Γ(2) ≅ Γ₀(4) | 6 | three cusps | θ₃² | θ₃⁴ = θ₂⁴ + θ₄⁴ |
| 3 | Γ₀(3) | 4 | two cusps, one point of order 3 | a(q) = Σ q^{m²+mn+n²} | a³ = b³ + c³ |
| 4 | Γ₀(2) | 3 | two cusps, one point of order 2 | square root of a weight-two form | A² = B² + C² |
| 6 | the j-line through E₆/E₄^{3/2} | 2 | (see below) | E₄^{1/4} | E₄³ = E₆² + 1728Δ |

index × s = 12 in every row (exact). The first three are subgroups of the modular group. The fourth is not: with
4x(1 − x) = 1728/j the x-line is the double cover of the j-line branched at j = 0 and j = 1728, which is not an
orbifold covering of the modular orbifold (index 2 at a point of order 3) **[memory for the formula; the remark is
(exact)]**. So "signature 6" lives on the modular orbifold itself, with the multivalued weight-one period E₄^{1/4}.

**A2. The identities are one identity (exact).** In each row x_s = (c/a)^k and 1 − x_s = (b/a)^k for the
Hauptmodul x_s: the identity is x + (1 − x) = 1 on a tripod. For s = 2 this is the first consult's statement with
the three cusp etas. The maps between the rows are the maps between the curves (Γ(2) → Γ₀(2) is
λ ↦ 4λ(1 − λ) up to normalisation; all map to the j-line); the classical quadratic and cubic transformations of
the ₂F₁ are pull-backs along them **[memory]**.

**A3. The lattices [memory; the s = 4 entry least certain].** z₂ = θ₃² is the theta series of ℤ[i]; z₃ = a(q) that
of ℤ[ω]; z₄² a weight-two form on Γ₀(2) that is the theta series of D₄ in a suitable variable; z₆⁴ = E₄ that of E8.
If the s = 4 entry holds, the four signatures are the four lattices ℤ[i], ℤ[ω], D₄, E8 of ranks 2, 2, 4, 8.

**A4. The exponents 1/12 and 5/12 (exact).** E₄^{1/4} = ₂F₁(1/12, 5/12; 1; 1728/j) is the uniformizing equation of
the triangle (2, 3, ∞): 1/12 = 1/4 − 1/6 and 5/12 = 1/4 + 1/6. Multiplication by 5 on ℤ/12 (the frame a(3): −1 at
3, +1 at 4) exchanges the two exponents; multiplication by 7 sends them to their negatives. The two numerators
{1, 5} are the theta indices of η = θ_{6,1} − θ_{6,5}, and χ₁₂ takes opposite values on them. So **the relative sign
ε between 3 and 4 is the exchange of the two local periods at j = 0 relative to j = 1728.** This is an identity of
numbers; that the frame of an element of ĜT₀ acts on the periods this way is the open item 2(a) of DELTA_ON_GT.

**A5. The common multiplier (exact).** Pic(M_{1,1}) = H²(SL₂(ℤ), ℤ) = Hom(SL₂(ℤ), ℂ^×) = ℤ/12, generated by the
Hodge bundle λ; η^{2k} trivialises λ^k twisted by the character v_η^{2k}. So a class k ∈ ℤ/12 is a power of the eta
multiplier. (ℤ/12)^× acts on this group, and (ℤ/12)^×/{±1} = ℤ/2 with character χ₁₂. With ℤ/12 = ℤ/3 × ℤ/4:

| unit | sign at 3 | sign at 4 | χ₁₂ |
|---|---|---|---|
| 1 | + | + | + |
| 11 | − | − | + |
| 5 | − | + | − |
| 7 | + | − | − |

**What is and is not a theorem in (a).** A1, A2, A4, A5 are classical or exact. "χ₁₂ is the common multiplier" is
exact as arithmetic: both S6 and Δ ask whether a unit of ℤ/12 lies in {±1}. It is not established that the two
units are the same object: S6's is a class in Hom(SL₂(ℤ), ℂ^×), Δ's a class in the centre of SL₂(ℤ/12), and those two
groups are not dual to each other.

## (b) The S6 sphere condition is a statement about the Hodge bundle

All (mine), exact given the brief's description (multiple fibres 3 and 4 over j = 0 and j = 1728; monodromy
ℤ/3 ∗ ℤ/4 → SL₂(ℤ); p = 12l₀ − 4l₁ − 3l₂).

- **The base is P(3,4).** An orbifold sphere with points of order 3 and 4 is the weighted projective line P(3,4). Put
  v = E₄ (weight 4) and u = E₆^{1/2} (weight 3). Then J : P(3,4) → P(4,6) = M̄_{1,1}, (u, v) ↦ (E₄, E₆) = (v, u²). The
  point of order 3 is v = 0 (j = 0), the point of order 4 is u = 0 (j = 1728). Outside the cusp the orbifold
  fundamental group is ℤ/3 ∗ ℤ/4, mapping onto SL₂(ℤ) = ℤ/4 ∗_{ℤ/2} ℤ/6 by the monodromies of IV* (order 3) and III
  (order 4): the brief's map. So S6's base is the modular stack with a square root of E₆ adjoined.
- **J*λ = O(1).** Weights are preserved; degrees agree: deg λ = 1/24 on P(4,6), J has stack degree 2, and deg O(1) =
  1/12 on P(3,4).
- **Every Seifert bundle is a power of it.** Pic P(3,4) = ℤ·O(1). The unit circle bundle of O(−1) is S³ ⊂ ℂ² with
  weights (3,4); that of O(k) is S³/μ_k, with H₁ = ℤ/k. The Seifert Euler number of O(k) is k/12. Hence
  **p = ±k, the sphere condition is k = ±1, and the Seifert bundle is then the circle bundle of J*λ or of its
  dual.** The local characters of O(k) at the two points are (k mod 3, −k mod 4): the brief's class in
  H²(SL₂(ℤ), ℤ) = ℤ/12, which is k up to the sign conventions.
- **So yes:** p mod 12 is the power of the Hodge bundle, and the two local classes are the characters by which
  μ₃ ⊂ Aut(E_ρ) and μ₄ = Aut(E_i) act on the fibre: the signature-3 point (ℤ[ω]) and the signature-4 point (ℤ[i]).
- **The cusp.** The fibre over the cusp is 1728Δ = v³ − u⁴ = 0: in S³ the torus knot T(3,4), the link of the E₆
  curve singularity. On P(4,6) it is the trefoil T(2,3). S6 replaces the trefoil by T(3,4).
- **The ghost here.** A unit class k = 5 or 7 has a free local action at each of the two points, exactly like
  k = ±1, and gives a lens space with |H₁| ≥ 5. It passes each single-prime test and fails only in the pair. This
  is the group Ob(12) of the ghost note, in a second place.

**What does not hold.** The asymmetry (3, 4) against the stabilizers (6, 4) of the stack: 3 is the effective order
at ρ (μ₆ modulo the generic μ₂), 4 is the full order at i. P(3,4) is not the modular stack; it is its cover by
E₆^{1/2}. I have not checked against Engel or AC26 that their construction uses this orbifold and no other
(item R2).

## (c) Elliptic-expansion moonshine in this language

- **The statement [CHH-proof].** With S_{τ*} the map to the disc centred at τ* ∈ {ρ, i}, rescaled by the
  Chowla-Selberg period, and c_{τ*}(t) the flat coordinate of the versal deformation of the CM curve, the series
  j(s_{τ*}⁻¹(c_{τ*}(t))) are rational functions of t, coming from the inversion formulae for ₂F₁(1/3, 2/3; 1; ·) at ρ
  and ₂F₁(1/2, 1/2; 1; ·) at i. Displayed: 13824t³ − 46656t⁶ + 99144t⁹ − … and 1728 + 20736t² + 147456t⁴ +
  851968t⁶ + ….
- **The two rational functions (mine; they reproduce every displayed coefficient).**
  At ρ: j = 27t³(8 − t³)³/(1 + t³)³, the j-function of the Hesse pencil (level 3).
  At i: j = 64(4t² + 3)³/(4t² − 1)², the j-function of the Legendre family at λ = 1/2 + t (level 2), centred at the
  harmonic point.
- **In our terms.** Each CM point carries a local coordinate, canonical up to the stated normalisation, in which
  j is a rational function with rational coefficients: a rational frame at the orbifold point. At ρ it is the
  level-3 coordinate, with μ₃ acting by t ↦ ωt and j a function of t³. At i it is the level-2 coordinate, with
  t ↦ −t and j a function of t². These are the signature-3 and the signature-2 tripods. The paper says the
  signatures 4 and 6 should give further cases.
- **On S6's multiplicity-3 point.** E₄ has a simple zero in t at the Hesse point t = 0, so the flat coordinate is,
  to first order, the coordinate v = E₄ of P(3,4) at its point of order 3. The multiplicity 3 of S6 is the
  ramification t ↦ t³ of the flat coordinate. At i the flat coordinate has order 2, and S6's order 4 is a further
  square root (u² = E₆). So the elliptic expansion gives the natural chart at S6's multiplicity-3 point and half of
  the chart at the multiplicity-4 point.
- **On Δ's sign at 3.** The sign at 3 is which of t ↦ ωt, t ↦ ω̄t the frame induces. The rationality of the
  expansion is the local reason a Galois element's sign at 3 is dictated by its cyclotomic character. The theorem
  treats the two points one at a time. Δ is the relative sign between them, so the theorem does not bear on Δ; it
  supplies the two normalisations between which Δ is measured.

## Items for GPT-6 Astra (ChatGPT Pro mode)

**R1 (companion; background for DELTA_ON_GT and S6).** Open Berndt-Bhargava-Garvan. For each signature give the
group, the Hauptmodul, the weight-one period as a modular form, the identity in the form x + (1 − x) = 1, and the
lattice whose theta series is a power of the period; settle the s = 4 lattice and the status of s = 6; give every
transformation between signatures as a map of curves.

**R2 (join the S6 prompts).** From the AC26 construction and Engel's surface: prove or refute that the base
orbifold is P(3,4) with coordinates (E₆^{1/2}, E₄), that the monodromy map is the one above, that J*λ = O(1), that the
vanishing-circle bundle is the circle bundle of J*λ^k with p = ±k, and that the circle over the cusp fibre lies
over the torus knot T(3,4); state the sphere condition as k = ±1 and classify the total spaces for the unit classes
5 and 7.

**R3 (companion).** Prove the two closed forms of (c) for all coefficients from the flat coordinates of Tu and of
Căldăraru-He-Huang; do the signature-4 and signature-6 analogues the paper says to expect; express each flat
coordinate through E₄, E₆ and the Chowla-Selberg period.

**R4 (join DELTA_ON_GT, item 2).** Prove or refute: the central frame class a of an element of ĜT₀ of multiplier
one acts on the two local solutions at j = 0 of the equation of E₄^{1/4} by the permutation of the exponents 1/12,
5/12 induced by multiplication by a, and Δ = 1 exactly when they are exchanged relative to the frame at j = 1728.
Then decide whether the class k of (b), for the circle bundle attached to such an element's action on the
punctured neighbourhoods of the two points, equals a.
