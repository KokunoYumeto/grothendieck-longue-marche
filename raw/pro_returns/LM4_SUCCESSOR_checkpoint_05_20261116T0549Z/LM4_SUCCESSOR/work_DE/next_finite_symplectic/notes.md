# Actual nonnilpotent finite quotient: isolated post-checkpoint candidate

Found05:48UTC16 November2026. Formal sources remain frozen. Independent review is requested before theorem promotion.

Use the actual common-base13 tetrahedral and6 cyclic braid words from B.61. Specialize unreduced Burau at−1 modulo3 on eleven strands, then quotient its fixed all-ones line. Projectivize the resulting ten-dimensional representation. The generator relations and inverses are checked exactly.

This projective representation is intrinsically the homology representation of the double cover of the sphere branched over all twelve named vertices. The cover is defined by sending every puncture loop to1 in C2, so every mapping class lifts; the two choices differ by the hyperelliptic involution, acting as−I on homology. Projectivization therefore defines a representation of the full sphere mapping-class group, making the kernel A5-invariant. This geometric identification should receive independent review.

Complete exact enumeration gives tetrahedral image order144, cyclic image order1440, intersection order3 with its two nonidentity elements of order3. The tetrahedral image has derived subgroup of order24. Its intersection with the common C3 is trivial. Its order144 has3-part9, while its derived order is divisible by3, so the group is not nilpotent: a nilpotent group of this order has abelian Sylow3 subgroup and derived subgroup of2-power order. Thus even this subgroup proves the ambient finite image is nonnilpotent.

The full55-pair source-H1 matrix has a primitive integral kernel of rank7, with an identity minor on the free source coordinates. All seven corresponding actual words map into the derived subgroup of the tetrahedral finite image. Hence its finite abelianization is zero on the completed kernel of the source map to ambient H1. B.58 puts the actual K in that completed kernel. Therefore q(K) lies both in the finite derived subgroup and in the common C3, forcing q(K)=1.

The topology step is finite free-module exactness: `ker(M:Zhat^13→Zhat^55)=ker(M:Z^13→Z^55) tensor Zhat`. The commutator subgroup of the free profinite source maps onto the derived subgroup of its finite image. Thus annihilating the seven integral kernel directions in that finite abelianization is enough; no equality of discrete and completed rigid kernels is used.

Subject to review, the standard B52/B46 argument then gives closed products for all two-factor finite-index refinements containing ker(q). This is a finite nonnilpotent quotient family; it does not imply K=1 or control arbitrary finite quotients.

Reproduce in order: `python prepare.py`, compile `enumerate.cpp` with C++17, run `./enumerate`, then `python analyse.py`. Matrices use the exact B61 relative marking. The C++ enumeration uses precomputed action tables on all59049 ternary rows; every group multiplication is exact. `analyse.py` independently recomputes every144² tetrahedral product with NumPy integer matrices, the full commutator subgroup, and the source-H1 kernel checks. Actual stdout and complete matrix sets/certificates are retained.
