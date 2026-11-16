# Independent full audit of D80

**PASS**, reviewed by pbc_groups on 2026-11-15. The entire written candidate and its exact certificate have been checked. This remains notes-only during the checkpoint12 source freeze.

## Actual arithmetic images with infinite support

The completed Kummer group is the five-adic completion of the free abelian group on rational primes; the sign disappears. Its valuation coordinates form the c0 module, so each residual coefficient level has finite support. With the coordinate at five zero, independence of a,b modulo five implies that two actual inertia vectors away from five have unit determinant. Their pro-five inertia images generate the full translation lattice, and the untwisted action is unramified there. D78's faithful actual operator argument therefore still proves H semidirect I0 without assuming a finite global ramification set.

For every q different from five, log(q^4)/(4 log6) is integral. Multiplying these bounded coefficients by a c0 family gives a convergent nonarchimedean sum independent of order. Thus the displayed local logarithm is well-defined and continuous. The primitive local vector, the integral cocycle gauge, the actual local surjection to I0 and the saturated kappa(6)-image give exactly the stated local line subgroup. All coinduction and restriction-kernel arguments inherited from D79 depend on these actual images, not on bounded support. The geometric boundary permutations also transport the unrestricted coefficient diagrams.

## Strict local compact-to-discrete passage

I reread D43 in full at the point used here. Its vanishing H1(G_q,A_s)=0 applies to every nonzero abelian inertia vector, explicitly whether or not a metabelian lift exists. Thus the argument does not assume the global section whose existence is left open.

The stable quotients W_r are finite. Their local H0 and H1 groups are finite, so the H0 inverse system is Mittag--Leffler. The compact-coefficient exact sequence consequently identifies H1(G_q,A_s) with the full inverse limit of H1(G_q,W_r); no lim1 term remains.

For every finite W_r, local Tate duality is a perfect natural pairing between H1(G_q,W_r) and H1(G_q,W_r^D). Contravariance in coefficients gives precisely the transition maps used in the draft. Pontryagin duality therefore takes the inverse limit to the direct limit. Continuous cohomology of a profinite group with discrete torsion coefficients commutes with this filtered union: each continuous cochain from a compact finite power of the group has finite image and lies in one stage; the same statement applies to a witnessing coboundary. Hence H1(G_q,D) is the dual of the zero inverse limit, so it is zero.

This conclusion means that a given finite-level local class becomes zero at some larger finite level. It gives no simultaneous bound over infinitely many q by itself, and the proof correctly does not make that inference.

## One common finite coefficient module

The exceptional set E consists of the finitely many primes where the inertia vector is nonzero modulo five. At every q outside E and five, both exponents lie in5Z5. In characteristic five the exact identity (1+u)^(5x)=(1+u^5)^x makes the inertia multiplier trivial modulo (5,(u,v)^4). Thus the fixed ten-dimensional module M is unramified there even if the complete Alexander module has nonzero deeper inertia.

The original action and the constant cocycle c are unramified away from five. D78's exact universal constant, linear and cubic primitives apply to every possible actual residual Frobenius tuple in M. Since inertia fixes M, those are primitives for the full local Galois group, not merely for a formal cyclic operator.

At each q in the finite set E, local discrete vanishing provides one finite stage W_(r_q)^D in which c dies. Taking the maximum of these finitely many stages and4 gives a single W_R^D. All primitives already in M remain valid after the coefficient inclusion, including at places where W_R^D is ramified: the same vector still satisfies the same cocycle identity. At five the unit-slope primitive is already in M, and real cohomology vanishes at this odd prime. Therefore the one global class is everywhere locally trivial at this one finite level. No direct limit is interchanged with an infinite product.

The class remains globally nonzero through the actual coinduction isomorphism and primitive raw Soule restriction from D78; inflation from the actual operator image is injective in H1. This supplies exactly the lower bound matching the previously proved F5 upper bound. Positive depth retains the zero restriction-kernel result from D79.

## Compact groups and actual points

Independence modulo five makes a,b,a-b globally primitive. D77's boundary depth calculation and continuous product decomposition then give the displayed compact groups and T_s=0. This does not determine arbitrary unrestricted H1 ranks, the nonseparated group, or section existence.

The explicit CRT construction has t=22 modulo36 and t=-1+5^(d+1) modulo5^(d+2). These give v2(t)=1, v3(1-t)=1, and the opposite two valuations zero, proving global independence by actual inertia. Both entries are units at five. Expanding t^4-1 gives exact valuation d+1, while 1-t=2 modulo25. Since log6 has valuation1, the local alpha has exact valuation d and beta is2 modulo five. The depth is therefore exactly d. The integer is positive and different from0 and1. Its actual ordinary point section supplies nonemptiness, after which the finitely ramified H1 theorem D74 applies. No assertion is made that every point of the much larger metabelian fibre is point-theoretic.

## Executed certificate and primary source

Independent execution under a distinct runpy name preserved all owner outputs. The whole serialized result equals the owner's JSON for every rank1 through30, including the exact CRT congruences, inertia determinant and five-adic valuations. Outputs: notes/pbc_D80_independent_rerun.json and notes/pbc_D80_independent_rerun.out.

Verified primary source: J.S. Milne, Arithmetic Duality Theorems, second edition, I Corollary2.3, printed page28, author PDF https://www.jmilne.org/math/Books/ADTnot.pdf. It gives the required natural H1 duality and finiteness for finite local Galois modules. Opened references: turn1044view1 and turn1045view0. The preceding attempted ADT.pdf path was inaccessible; the ADTnot.pdf author copy was successfully opened and the exact corollary inspected.


SHA256 notes/de_sha_unrestricted_draft.tex: 7ec5190814b6fcc73deae923a35c7d16438edb55060598dac814357a3309bf98

SHA256 notes/de_sha_unrestricted_certificate.py: c482eb436bcfab392b9ffb7e3a4f0717eea4e26fe7d0b10fc9ccb0332f60b134

SHA256 notes/pbc_D80_independent_rerun.json: ad8c6e70b79a004a23d51086afb2797d6d47113b73ea5a2dcb7334524a76febe
