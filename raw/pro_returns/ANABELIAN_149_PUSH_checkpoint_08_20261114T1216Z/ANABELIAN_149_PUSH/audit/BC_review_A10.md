# Independent review of A.10

**Outcome: the stated point-separating quotient criterion and its explicit characteristic-two application pass this review.** This review concerns A.10 and the inputs from A.9/A.3 used there; it does not certify the later generalizations A.13 onward.

## Abstract implication

A collision of point sections remains a collision after a finite constant extension. One may therefore define the cover and maps over that extension and make a chosen lift of the first point rational. The geometric prime-to-p Galois-closure hypothesis ensures that the cover is represented by an open subgroup in the same arithmetic prime-to-p extension. The fixed-fibre argument of A.3 supplies a matching rational lift whose section is equal in the cover's own arithmetic prime-to-p extension. A.1 then gives a p-primary Jacobian difference. Under each induced Albanese homomorphism this difference maps to the difference of the two images. The assumed absence of geometric p-primary points forces every image difference to vanish. Geometric point injectivity of the product map forces equality of the lifted points and then equality downstairs. No claim about immersion, separability of the product map, or a single finite quotient separating all points is required.

## The elliptic target has no geometric 2-primary torsion points

The exact count on the displayed plane cubic over F4 is seven affine points and two points at infinity. The independent program `code/BC_review_A10.py` performs this count directly in F2[a]/(a²+a+1), without importing the A-series computation. The Frobenius polynomial is consequently X²+4X+4. Faithfulness of the prime-to-two Tate-module action on endomorphisms and Cayley–Hamilton give (π+[2])²=0 in End(E). A nonzero elliptic endomorphism is an isogeny, and the composite of two such isogenies is not zero; hence π=[−2]. The F4-Frobenius is purely inseparable, so multiplication by 2 has no nonzero geometric kernel point. Iterating gives absence of all geometric 2-primary torsion points.

The exact standard inputs were reopened in Milne, *Abelian Varieties*, version 2.0, 16 March 2008: I, Theorem 10.15 (printed p.49) for faithful Tate-module action, and II, Theorem 1.1 (printed p.75) for the Frobenius point-count formula. Public source: <https://www.jmilne.org/math/CourseNotes/AV.pdf>. The no-nilpotent step uses the elliptic dimension-one condition; a product of supersingular elliptic curves would have nonzero nilpotent endomorphisms, so that step should not be generalized without argument.

## The two maps separate every geometric point

Both maps are rational maps from a smooth proper curve to the proper smooth cubic, so they extend uniquely. At finite x with u nonzero, z and v=u/z are regular units. Equality of both images gives x, w0=z+v and w1=az+a⁻¹v. The coefficient matrix has determinant a+a⁻¹=1 and recovers z and v; the equation Y=z³−A then recovers the original point. The displayed affine cover is smooth there because the base is smooth and the cubic extension is étale where z is a unit.

At x=a² the base hyperelliptic covering is unramified because h=1. On its F=0 branch, the respective valuations of u,F,z,v are 2,6,2,0. The three residue values of v are the cube roots of unity, since v³ is the hyperelliptic conjugate of F and has residue 1. Their image pairs are (v,a⁻¹v). On the other branch, z ranges over the cube roots of unity and v=0, giving (z,az). The two triples are individually injective and mutually disjoint: equality would force z=v nonzero and a=a⁻¹. The independent program checks all six pairs.

At infinity x has pole order two, and the étale cubic cover has three points with z/x residue ξ in {1,a,a²}; v/x has residue ξ⁻¹. Projective limits are determined by w/x. The two image limits, in that order of ξ, are (O,T), (T,T), (T,O). These are distinct. Every finite-x point has both map images in the affine chart Z=1, so none can coincide with an infinity pair. These cases exhaust all geometric points. A finite-field enumeration alone would not establish this global assertion; the invertible matrix, local valuations, and projective limits do.

## Computational scope

`code/BC_review_A10_output.json` records a passing independent certificate for the point count, matrix determinant, exceptional finite pairs, and infinity pairs. It is supplementary to the algebraic proof and does not decide equality of sections by enumerating finite quotients. No correction to the mathematical statement of A.10 was needed. The exact I.10.15 citation was communicated to its author.
