# Independent focused review of the root proof supplement

Review completed 2026-11-17 23:25 UTC by GPT-6 Astra Pro, `/root/mechanical_support`, with a separate targeted check of §§6 and 8 by `/root/mechanical_support/norm_orientation_review`; effort settings were not exposed.

**Verdict:** the five requested arguments withstand the checks below. One real precision issue was found in §6's exact norm formula and has already been corrected by the root agent; the final sign is unchanged. Root also added the explicit `n >= 1` range in §5 and the relative invariant-algebra justification in §3, and those revisions were inspected. No image or frozen transcription was inspected during this review, and no reviewed source file was edited by either reviewer.

## Findings and actual checks

| Supplement location | Check performed | Result |
|---|---|---|
| §§4–5: rational map and divisor multiplicities | Independent ramification/pullback argument; independent exact symbolic computation of the second iterate, its denominator, and the specialization at t=2. | Confirmed for m=2^n with n≥1 and 2 invertible. The whole fiber has degree m², with reduced geometric support of degree m²/2+2. |
| §3: intrinsic quotient | Checked the canonical branch labels, invariance under all three involutions, and a relative invariant-algebra argument. | Correct; no normality assumption on the base is needed for this quotient construction. Invariance alone should be accompanied by degree/finite-flatness, as detailed below. |
| §6: tangent norm/jet duality | Two independent line-map calculations; primary-source verification of the determinant definition of norm. | Final factor (-1)^(n−1) confirmed. Exact formula for an arbitrary source-unit required qualification; root's revised text now has it. |
| §7: unrestricted target-data category | Checked the action, torsor condition, all branch stabilizers, normalization uniqueness, and the possibility of changing the group by an automorphism. | Valid counterexample to the unrestricted list; no refutation of the intended compatible category or its quadratic application follows. |
| §8: projective-bundle orientation and twisting | Independent determinant/tangent calculations for both projectivization conventions; checked the characteristic-three case and the torsor of compatible square roots. | Confirmed with the stated conventions and base assumptions. |

### RPR.01 — Multiplicity calculation confirmed; state the positive-iteration range

For m even and invertible, every point of E[m] contributes coefficient two to the pullback on E, while q has ramification index two precisely at E[2]; dividing those coefficients by the ramification indices yields coefficient one at the four two-torsion images and coefficient two at all other ±-orbits. This proves the stated geometric divisor formula and support count. The range must be n≥1: for n=0, m=1, the support consists only of t and the displayed formula m²/2+2 does not apply; the root agent has now stated this range explicitly.

For a relative Cartier-divisor formulation, define q_* by the finite-flat norm and use q^*q_*D=D+[-1]^*D for the invariant torsion divisor D; faithfully flat pullback by q then gives the claimed equality. Over a possibly nonreduced base, describe the torsion image as a finite étale quotient with reduced **geometric fibers**, not as an absolutely reduced scheme. Exactness of invariants when 2 is invertible identifies the image of E[m] with E[m]/{±1}, so this is distinct from the nonreduced fiber at the non-two-torsion orbits.

The independent symbolic calculation gave exactly the supplement's numerator

\[
16t(t-1)z(z-1)(z-t)A^2B^2C^2
\]

for F_t(F_t(z))−t; its denominator is the square of a monic degree-eight polynomial. At t=2 the numerator has degree fifteen, the denominator degree sixteen, their gcd has degree zero, and gcd(ABC,(ABC)')=1; ABC takes the nonzero values −8,1,−8 at 0,1,2. Thus there are three finite simple points, six finite double points and one simple point at infinity: degree sixteen and ten support points, as claimed.

### RPR.02 — Relative quotient and descent are valid with a small proof bridge

The identification of J with the three nonidentity elements of V is canonical: j corresponds to the double transposition exchanging t with j and exchanging the other two marked points. Independently substituting the three homographies into F_t gave zero invariance residuals, and the computed pairwise resultants of A,B,C were 4t(t−1)², 4t(t−1), and −4t²(t−1), all units on the stated base; their discriminants are units there as well. This confirms the three disjoint degree-two branch axes and the labelled branch values without excluding characteristics three or five.

For completeness, the homogeneous degree-four map is finite locally free of degree four: its graph over either target chart is a relative degree-four divisor in a projective line, and the exact sequence from O(−4) to O computes its pushforward as a locally free module of rank four. The averaging idempotent (1/4)Σ_g g makes the invariant algebra (F_*O)^V a direct summand commuting with base change; over each geometric fiber, degree four and V-invariance identify the map as the rational-function quotient, so this invariant algebra has rank one and equals O of the target. The canonical branch labels and uniqueness of an isomorphism of three-pointed projective lines then supply the stated étale descent, including over a nonnormal base.

The uniqueness qualification is also correct: postcomposition by z↦z² preserves the three labelled values and increases degree, whereas the prescribed zero/pole multiplicities and degree four fix the rational function up to the remaining scalar.

### RPR.03 — Norm precision issue corrected; sign confirmed

Originally §6 wrote N(y)=(-1)^(n−1)x/u for a general unit in x=u y^n. If u depends on the source parameter, x/u need not be a target element, and Y^n−x/u need not be a polynomial over the target; this is a genuine reason not to state that exact identity generally. The current revision, inspected at 23:23 UTC, restricts the exact polynomial identity to target-pulled-back u and uses the conormal identity [N(y)]=(-1)^(n−1)u₀⁻¹[x] for an arbitrary source-unit, with u₀ its restriction to the section.

Writing the leading pullback as φ:C_x→C_y^⊗n, the induced norm line map is ψ=(-1)^(n−1)φ⁻¹; therefore (ψ⁻¹)^∨=(-1)^(n−1)φ^∨. This independently confirms κ_norm=(-1)^(n−1)κ_jet and the degree-two minus sign after the correction. [Stacks Project, Tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2), opened independently in this review, supports the determinant definition and arbitrary base-change compatibility of the norm; it was not used as a reference for the cover classification.

### RPR.04 — Counterexample survives group automorphisms as well as conjugacy

On each fiber over x≠0, the displayed action of (Z/2)² on the four pairs (y,c) is free and transitive; over x=0, both points have exactly the first factor as stabilizer. Any smooth finite extension of this fixed punctured torsor over A¹ is its normal completion, so the second-factor embedding cannot be realized by choosing another marked branch. Allowing an automorphism of G does not repair the example: an automorphism carrying one inertia factor to the other also carries the torsor's inertia subgroup to the other, whereas preserving the specified torsor class preserves its actual inertia subgroup.

Thus the failure is precisely essential surjectivity for independently chosen, incompatible target data. The supplement correctly refrains from declaring the intended “ad hoc” category or the G=μ₂ application false. Its automorphism qualification is also sound: a line with an nth-power identification still has μ_n automorphisms, so uniqueness must refer to a specified morphism of the full root objects.

### RPR.05 — Orientation and square-root torsors confirmed

For the convention of lines L⊂p*V_J, Q≅L⁻¹⊗det(V_J), hence T≅Hom(L,Q)≅L⁻²⊗det(V_J); the quotient convention gives the dual determinant factor. The determinant of ker(O^J→O) has the sign transition functions, and the sign line is canonically self-dual, so both conventions yield the stated orientation twist while retaining their distinct trivialization conventions. This uses the surjectivity of the sum map and never a splitting by one-third of the diagonal, so characteristic three causes no problem.

Squaring the character used to twist by a μ₄-torsor gives the quotient μ₂-torsor Q₀/{±1}, exactly the required orientation factor. The sheaf of compatible square-root isomorphisms is a μ₂-torsor and need not have a section globally, as the supplement already states. Neither calculation proves the later fine-moduli claim, and no such conclusion was drawn here.

## Limits

This was a targeted skeptical review of §§3–8 on the requested issues, not a fresh proof check of the endomorphism enumeration, every assertion in §2, the full manuscript cover equivalence, or any external register result. The independent polynomial calculation was run directly in the review session; it did not rerun or certify the root's entire certificate script. Frozen files, images, main notes, and the shared event log were untouched.
