# Independent D audit of E.67

**PASS, after the exact factor-one-half correction in the integral description of the moment map.** The defining wedge formula, all matrices, and the literal witness were already normalized correctly. The corrected section now agrees with its alternating-measure identification.

The audit used the actual sources in research_e67, the marked quotient in E.41, the actual local source and full ramified classification in E.61, and the integral trace argument of E.66. No deliverable file was changed by this audit.

## Actual kernel and completed module

Completing the marked peripheral generator to a free pro-three basis gives the stated geometric splitting onto the rank-nine filled group. The free group on the compact generator space B and its left-translation semidirect product have the same universal maps in both directions as the original rank-ten group. Finite characteristic coset partitions are cofinal among the clopen partitions of B. This proves the normal-closure model with the specified actual conjugates.

At class two, the integral BCH coordinates over Z3 give the compact inverse limit of the finite free class-two groups. The quotient kernel is exactly the closed third lower-central subgroup. The completed exterior module and the alternating part of the two-variable measure module agree through the stated maps and division by two.

The actual cusp Frobenius fixes the marked generator by its q-power. Its possible unknown central correction on other generators does not affect q times the permutation action on the first kernel module or q squared times the exterior action on the centre. The proof retains that unknown correction when changing the Frobenius coordinate.

## Nonunit inertia and the centralizer

The actual filled-group Frobenius has no fixed point other than one under any positive power: every nonzero lowest lower-central coordinate would give an eigenvalue-one vector, while its eigenvalues are products of positive-weight cusp and elliptic eigenvalues. For an affine translate, every periodic point is its unique fixed point, when one exists.

The compact orbit argument gives uniform growth of all finite three-power cycles away from that point. Ordinary trace then forces integral invariant measures to be Dirac measures there. For the weighted finite-coefficient argument, the geometric sum has exactly the three-adic valuation of the cycle-length ratio because q is congruent to one modulo three. Thus the invariant part of D0/aD0 vanishes for every nonzero a.

I checked the sign in the central equation and the nonunit step explicitly. The equation forces the central inertia correction to be delta1 wedge r; reducing modulo a and applying the weighted lemma gives r=a v. Conjugation by the actual element (v,0) subtracts the required central inertia term and changes the Frobenius first coordinate to its augmentation times delta1. Its remaining central coordinate is retained.

An element centralizing d^a first has trivial B coordinate by Dirac support, and then has its D coordinate in Z3 delta1 by the torsion-free exterior decomposition. This gives the complete centralizer, including nonunit a. Its actual conjugation action gives exactly the two displayed coboundary relations. Compact valuation annuli give the asserted homeomorphism with the full geometric orbit space.

The zero-D inertia case is also complete: a nonzero central inertia would be killed by q times a finite permutation minus one at every integral level, an injective operator. Hence it vanishes. The full-to-marked ramified image and its uniqueness then follow from the actual full classification in E.61 and the nonzero images of all other cusp vectors after filling Q.

## Moment and nonlifting witness

Under delta_g wedge delta_h mapping to delta_(g,h) minus delta_(h,g), raw integration of [h]-[g] is twice the defining moment. The author corrected the text to one half of that integral. The equivalent alternating bilinear formula, equivariance and right inverse are correct.

The actual quotient Frobenius matrix is obtained by deleting the invariant B0 direction using the displayed projection. I independently checked the elementary-divisor pattern: after primitive row operations on the seven-by-two cusp gluing block, two two-by-two blocks have unit off-diagonal entry and determinant of three-adic valuation three, while the remaining five cusp blocks have valuation two. This gives C27 squared times C9 to the fifth power. The displayed mod-three character kills both gluing columns and every remaining coboundary column, and takes value one on the first moment of the literal witness.

The witness is the actual commutator of the marked inertia and its conjugate by the A0 cusp loop. It is central modulo the stated third lower-central subgroup, so the tame relation holds. Its nonzero moment class proves its central Frobenius parameter is nonzero; the complete centralizer/equivalence calculation excludes every full lift, including conjugate representatives.

## Fresh execution

The copied-source run in d_e67_audit/code passed. The complete generated JSON is identical to the source certificate. The program SHA256 is 07408e971a10a3fcbb5a7c243dda2691b429640e9c34519c9c00517408260cc4. Actual stdout records the matrix and Smith checks, literal tame word, 3000 class-two identities, 1000 nonunit centralizer checks, 3000 moment checks and 144 weighted trace valuations.

The corrected source hashes and exact reviewed scope are recorded in audit.json. The theorem remains restricted to the explicitly stated marked-cusp inertia locus; the remaining unramified fibres and inertia surviving in B are not silently included.
