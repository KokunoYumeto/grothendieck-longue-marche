# D.26: isolated quotients and the complete homology refinement tower

The new result preserves D.25 and makes an actual further lift. Every quotient `G_j = B/[N,N]N^j` is isolated in the gentle GT-shadow groupoid. The proof uses the finite equations themselves: a commutator word reduces to the identity modulo four; this fixes the sign of the projective braid relation; generation then forces the same matrix intertwiner as A.17. The induced map preserves N and therefore descends to an automorphism of G_j.

The exact integral cusp map has Smith invariant factors `1^96,2`. Appending the primitive cusp cycle gives `1^97`; its Hermite normal form is also the identity. Thus the unique C2 obstruction to correcting conjugators disappears when the multiplier is allowed to vary. Starting with h=0 modulo2 and modulo3, the iterative equation uses lambda=1+12h and preserves lambda=1 modulo72, or m=0 modulo36. The original level-six multiplier is retained.

All twenty-four D.25 automorphism certificates extend to the profinite group `G = lim_j G_j`, with abelian kernel Zhat^97 over Q. At2 and3, generation is preserved by retaining the initial invertible kernel matrix modulo the prime. At every other prime, explicit averaging supplies centralizing conjugators for the identity automorphism, with the same finite Q coordinates. Chinese remainders assemble the local constructions. One profinite cusp gauge makes the conjugator a commutator at every level. A joint finite quotient G6 times Fab/36 selects the discrete D.25 gauge that agrees with it.

`code/d_cm_refine.py` records the integer matrices, Smith factors, cusp coordinates and all24 explicit lifts through exponents2,4,8,16 and3,9,27,81. All384 general-m hexagon checks pass. The saved stdout is `code/d_cm_refine.out`; the exact coefficients are in `code/d_cm_refine.json`.

## Routes actually tested

1. Dolgushev-Guynee's Definition3.13 and Remark3.16 were opened. Isolation is verified for these exact quotients. It supplies reduction homomorphisms, with no general assertion of surjectivity. Theorem5.2/Corollary5.4 still require all finer finite quotients.
2. Dolgushev-Le-Lorenz's full original preprint was opened. AppendixB, TheoremB.2 proves all charming shadows are genuine in the abelian pure-quotient setting. Our pure quotient surjects onto C2^2 times SL2(F3), so its hypothesis fails by the displayed quotient map.
3. The dihedral family in BDHP2026 Remark3.2 has pure quotient embedded in D_n^3, hence metabelian. Our quotient surjects onto SL2(F3), whose second derived subgroup is nontrivial. No quotient map from that dihedral family can supply these witnesses.
4. The entire family of characteristic abelian-exponent refinements of N was tested by an integral calculation and solved as an inverse system, not merely at finitely many exponents.
5. To identify exactly what remains, map two free generators of rank97 N onto two transpositions generating S3, and take the normal core in B after intersecting with [N,N]N^6. The resulting finite quotient lies below G6 but kills fewer commutators than every G_j. This proves, through explicit quotient maps, that the solved tower is not cofinal in D.22's full system.

Full profinite GT0 liftability of the twelve nonarithmetical CM shadows remains unresolved. No class-two quotient computation is claimed; the rank4656 second layer remains a possible next test.
