# Targeted calculations performed after the transcription freeze

Run: MPL_57_133-179; date 2026-11-18. These are editorial mathematical checks, not changes to the transcription and not claims of new mathematics. The longer two-ring normality and Cohen–Macaulay checks are in `research_counterexamples_review.md`; the Fourier chain-map diagnostic is in `research_fourier.md`.

## C02 — normalization defects in three control singularities

Work over an algebraically closed field of characteristic zero. For a node, the normalization is the pair of power-series branches and the original ring consists of pairs with equal constant terms, so the normalization defect is one and there are two branches. For the cusp `k[[t²,t³]] ⊂ k[[t]]`, the quotient is spanned by the class of t, so its defect is one and it has one branch.

For the ordinary planar triple point, use

\[
k[[x,y]]/(xy(x-y))\longrightarrow k[[t]]^3,
\qquad f\longmapsto(f(t,0),f(0,t),f(t,t)).
\]

The map is injective because its three kernels intersect in the product of the three distinct branch equations. It is the normalization map. The image of the constant terms has dimension one, imposing two linear conditions. The image of the degree-one terms is `(a,b,a+b)`, imposing one condition. In every degree d≥2, the images of `x^d,y^d,x^(d−1)y` are `(1,0,1),(0,1,1),(0,0,1)`, with determinant one, so there is no further condition. The quotient therefore has length three.

For three coordinate axes in three-space, the normalization has the same three branches but the only restriction is equality of the constants, so the defect is two. Substituting in `defect − branches + 1` gives additive dimensions zero for a node, one for a cusp, one for a planar triple point, and zero for the three coordinate axes. The Fourier research collaborator independently checked the degree-wise triple-point calculation; it is not inferred from Hua's prose alone.

## C05 — the graph arithmetic and its limits

For a connected unmarked nodal graph, let c₀ be its vertices, c₁ its edges, and ρ=c₁−c₀+1. Direct substitution gives

\[
3g-2\rho-2c_0+c_1+\lambda-1
=3g-3-c_1+\lambda.
\]

With stable vertices the unstable-component correction λ is zero. If independent marked points are also counted, their number must be included separately. This is an arithmetic verification only: it neither identifies every drawing nor proves a product description of a stratum, smoothness, asphericity, a fundamental-group assertion, or an arithmetic theorem from the results register.

## P02 — monomorphism without quasi-compactness

Over a characteristic-zero field k, distinct integers have invertible differences in k. Consequently the map from the disjoint union of copies of `Spec k` indexed by integers to `G_a`, taking component n to n, has diagonal equal to an isomorphism onto its fibre product and is a monomorphism. Its domain is not quasi-compact, so the map to the affine scheme `G_a` is not affine. This is precisely a check of the warning on scan 135, not a counterexample to the Picard-kernel theorem.

## P03, R05, R11 — identity-section tests

Take X=Σ=S=P¹_k and all structure and section maps to be identities. In P03, the frozen tensor formula sends L=O(1) to O(2), whose restriction along the section is itself and is not trivial; tensoring instead with the inverse gives O. In R05, a rigidification along the identity forces a line bundle itself to be trivial, so the absolute Picard class O(1) cannot have the asserted rigidified representative; its relative class modulo base pullback is zero. In R11, the last unquotiented Picard arrow is Z→0 and is not an isomorphism, whereas the quotient by Pic(Σ) is zero and has the claimed identification. These tests concern the literal statements and do not determine whether a prime or adjective was omitted in the handwriting.

## D02 — an automorphism group and a stabilizer are different objects

For X=P¹, L=O(1), and j the identity into P¹, an element of PGL₂ fixing j by postcomposition must be the identity. The automorphism group of X is nevertheless PGL₂. Thus the literal parenthesis equating freeness of the action with triviality of all of Aut(X) cannot be used without specifying the extra datum whose automorphisms are meant. The compressed source remains a reading question.

## P07 and P09 — puncture control cases

For one labelled section, the quotient G_m/G_m is trivial. For two, `(u,v) ↦ u/v` is surjective with diagonal kernel, giving T≅G_m; choosing the opposite ratio reverses that chosen identification. For S=Spec F₂, the projective line has exactly the three rational points 0,1,∞, so removing all three leaves no section. The latter check concerns the point count and the failure of a proposed converse under the manuscript's vanishing conclusions; no proof of its still-unverified transgression/Kummer identity is counted here.

## N01 — why the target is separated

The two open embeddings of A¹ into the affine line with doubled origin agree away from zero and differ at zero, so dense-open agreement alone does not give uniqueness into a nonseparated target. With a separated target, the equalizer is closed; agreement on a schematically dense open forces that equalizer to be all of the source. This verifies the role of the hypothesis in gluing representatives, without deciding the truth of the cancelled quasi-coherence proposition.

## D04, Q02, U01, U05, Q05 — formal checks

- **D04:** the short exact sequence for an effective Cartier divisor with L=O_X(Y) gives the connecting map H¹(L|Y)→H²(O_X); it verifies the degree, not the ink reading.
- **Q02:** the low-degree Leray sequence and the section's retraction make the H² pullback injective and kill the preceding obstruction; this is on the specified site, before any further comparison of topologies.
- **U01:** contraction with the ith basis vector supplies a homotopy for multiplication by f_i; a linear combination summing to one contracts the Koszul complex.
- **U05:** divide the stated quadratic inequality by h² and let h grow; positive a gives m≤1, and positive integral degree gives m=1. The prior analytic surface inputs are not independently proved.
- **Q05:** O(1) on P¹ and the trivial bundle become isomorphic on each standard affine chart but have different degrees globally, so the absolute Picard presheaf is not separated for open-cover descent.

The research-note bodies carry the individual sources, qualifications, RESULTS_STATE links, and confidence levels. `CHECK_EVENTS.tsv` records the actual kinds of these checks.
