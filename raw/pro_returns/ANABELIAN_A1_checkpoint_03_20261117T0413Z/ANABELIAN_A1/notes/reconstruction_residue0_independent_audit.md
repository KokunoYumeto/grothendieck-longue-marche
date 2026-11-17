# Independent audit of the residue-characteristic-zero construction

17 November 2026. Literature auditor, independently of the configuration auditor's draft. This records the checks actually made; it is not a substitute for writing the coordinate lemma in the paper.

## Exact source input

Opened Emmanuel Lepage, *Covers in p-adic analytic geometry and log covers I: Cospecialization of the (p')-tempered fundamental group for a family of curves*, Ann. Inst. Fourier 63 (2013), 1427–1467, https://www.numdam.org/article/AIF_2013__63_4_1427_0.pdf, tool reference `turn87view0`. Independently read local text lines 530–635.

- Theorem 1.6: for a log regular fs log scheme X, and a set L of primes invertible on X, the restriction from L-finite Kummer étale covers to L-finite algebraic covers of the trivial-log locus is an equivalence.
- Theorem 1.8: if S is a noetherian henselian scheme with closed point s and X is connected fs log with underlying scheme proper over S, restriction KCov(X) -> KCov(X_s) is an equivalence.
- Applying these to a DVR of residue characteristic zero permits L equal to all primes. Applying them also to Spec R with the standard log structure retains the complete arithmetic group G_K, not only the residue-field group. The hypothesis in Corollary 1.9 that the DVR be complete is unnecessary when applying Theorems 1.6 and 1.8 separately.

## Difference and cluster checks

Let lambda=1+t and let f scale exactly the ball v(a)>0 by lambda and fix its complement and infinity. For any distinct finite a,b, the ratio (f(a)-f(b))/(a-b) is a principal unit. In the crossing case the extra summand ta has valuation strictly larger than v(a-b)=v(b). Within either region the assertion is immediate. Consequently every difference has the same valuation and initial form, and the same holds for every quotient of products of differences. All nonzero rational numbers are valuation units, hence fixed.

Stable marked genus-zero fibres have labelled component trees and node thicknesses determined by these data. Each stable component has at least three special points, so an isomorphism respecting every label and branch is unique on underlying curves. At a node with chart e1+e2=nq, an automorphism over the fixed log base and fixed underlying nodal ring A sends e_i to u_i e_i with (u1-1)x=(u2-1)y=0 and u1u2=1. Thus u1-1 lies in both (x) and (y), whose intersection is zero in the reduced nodal local ring. The log lift, when it exists, is unique.

## Necessary strengthening of the draft's compatibility argument

Uniqueness of log **isomorphisms** alone does not establish commutation with the log **contraction maps** that forget markings. A contracted component can support a log generator whose underlying function is identically zero, so the underlying morphism does not determine its unit part. For example, a tail with coordinate z=x/pi^n maps a target horizontal generator x to pi^n z. Its logarithmic unit z must be compared explicitly.

The proposed explicit coordinate remedy passes the audit. Use cluster coordinates

    z=(x-a)/pi^m,       w=(x-b)/pi^n,
    z=(b-a)/pi^m + pi^(n-m)w,

and reciprocal coordinates near infinity. After extracting the smaller valuation, the residual factor in the last expression is a nonzero constant, w, or c+w. The valuation and c are determined by the initial form of b-a. They are unchanged by f. Products and quotients of these coordinates describe the horizontal and nodal divisorial-log generators. Thus the characteristic exponents and residual unit functions agree for every pullback, including on a contracted tail. Equality of unit functions may be checked component by component because the nodal fibre is reduced. This provides the required compatibility of the log isomorphisms with forgetting markings.

For a finite extension, write pi_L=epsilon*pi_M^e. The same epsilon and e occur on both sides, and the map on associated graded valuation rings preserves the equal initial forms. This gives compatibility with base change. The construction uses only labels, the valuation, and their initial forms, so Galois equivariance follows from f's G_K-equivariance. The alternative observation that f is exactly affine on each cluster inside the positive-valuation ball and is identity outside it is a useful check on these formulas.

## Arithmetic at marked points

The required conclusion is stronger than preservation of abstract inertia groups: the quotient D_a/I_a must be identified with G_{K(a)} over the fixed arithmetic base. This check passes. The fields K(a) and K(f(a)) are identical subfields of the chosen algebraic closure. Near the mark a the point map is exactly x -> lambda*x, or identity, on a sufficiently small valuation disc. The corresponding local parameter comparison fixes K(a). The log-mark restriction of the comparison is therefore over the unchanged log trait of K(a); applying the same two theorems identifies its arithmetic quotient with the same G_{K(a)}. Any principal-unit change of a parameter has a unique n-th root congruent to 1, for every n, by Hensel's lemma in residue characteristic zero. Thus no extra Kummer arithmetic class has been introduced.

The comparison of finite covers consequently identifies the finite residue-field extensions of points over a mark, as extensions of K(a), and their ramification indices. This is precisely the cusp information needed in the next step.

## Passage to the entire small étale site

This passage passes the audit, conditional on the coherent log comparisons just described. A quasi-compact separated étale object over P1_K is an open subscheme of the finite normalization of P1_K in its generic finite separable algebra. The normalization is étale away from some finite Galois-stable set S. Enlarge S to contain 0,1,infinity. Transport the finite cover of P1-S by the compatible Galois-category equivalence, normalize, and transport the omitted points using their cusp decomposition orbits. The preserved inertia actions imply that exactly the unramified points are available to retain in an étale object.

Morphisms are determined by maps of the generic finite algebras: their extensions to the normal compactifications are unique, and restriction to the chosen opens is characterized by the retained point sets. Both conditions are preserved. Joint surjectivity of families is characterized on geometric points and is preserved as well. Quasi-compact separated étale objects form a basis of the small étale topology, so the transported basis yields an equivalence of the full small étale topoi over BG_K. The induced map on closed points is f modulo G_K and preserves their residue fields. Restriction at the fixed point infinity gives the A1_K equivalence.

Finally, a K-polynomial inducing f would agree with the identity on the infinitely many nonzero rational units. It would therefore be the identity polynomial, contradicting f(t)=(1+t)t. Hence the resulting pinned relative equivalence is not induced by a K-morphism. This last argument does not need a separate reconstruction/full-faithfulness theorem.

## Verdict and limit

No mathematical obstruction was found after the explicit contraction-coordinate repair. The proof should include that calculation and the arithmetic marked-point identification; neither should be replaced by the phrase “the clusters are unchanged.” This audit concerns the B8 topos construction. It does not independently verify the separate generic-arc/centralizer argument proposed for B7.
