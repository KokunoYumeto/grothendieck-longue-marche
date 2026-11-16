# A205 independent complete proof and certificate audit

Reviewer: local_preprint. Date: 2026-11-16, immediately after CP16.
Source: sections/selmer_central_local_matching.tex.
Certificate: code/selmer_weight_four_matching_certificate.py.
Result: PASS, with no mathematical correction requested.

## Actual section and conjugacy maps

The kernel of E_(r+1) -> E_r is the actual central geometric module Zhat(r+1)^(b_(r+1)), with its cyclotomic arithmetic action. Literal lifts of the fixed lower representative differ by continuous central one-cocycles. Central conjugation changes them by a coboundary.

The proof of global and finite-local geometric centralizer vanishing is exact: the first nonzero Hall weight has a nonzero coefficient-prime component fixed by chi_l^j. Globally and at every finite place there is an arithmetic element with chi_l^j different from one. Multiplication by that nonzero scalar is injective on the torsion-free Hall lattice. Hence an additional lower geometric conjugator cannot identify different global H1 correction classes.

The real-place stabilizer is retained explicitly. The map from a lower stabilizer element to the central difference cocycle of an actual lifted conjugator is independent modulo coboundaries, additive, continuous and independent of the reference central twist. Its compact image is exactly the extra translation subgroup used in the local allowed cosets.

## Actual local allowed sets and closed intersections

Each full local point or cusp section is aligned with the lower representative by an actual geometric conjugator and then lifted. Its difference from the chosen global lift is the central cocycle displayed in A205.8. Changing choices gives exactly the stated real translation coset, and only a coboundary at finite places.

At a finite place, full multiplicative Kummer injectivity gives at most one ordinary centre and one completed tangent parameter per cusp label. The three displayed tangent maps exclude overlap between an ordinary point and a cusp: the resulting field equations are x=0, x=1 or (1-x)/x=-1. Thus the allowed set has at most three points, and exactly one when an ordinary image is present. Real point transport inside each interval commutes with conjugation in every finite etale fibre; the compatible inverse limit gives the claimed full-section comparison. The two real Kummer signs per cusp and the real stabilizer cosets are retained.

The fixed-support H1 comparison follows from the literal tame inertia equation q^m a=q a. Since m>=3 and the coefficient lattice is torsion-free, inertia outside l vanishes. Finite fixed-support cohomology and the finite H0 derived-limit vanishing give the compact inverse-limit topology. The closed-span Nakayama argument proves finite generation without replacing an image by its closure. The local groups have the same compact comparison. Hence the allowed inverse images are closed subsets of a compact global correction group, and the finite-intersection criterion is exact. Finite coefficient and coefficient-prime tests recover the same closed sets because those maps separate points of the local inverse limits.

## Exact fourth-weight cohomology

The A61 H2 bounds, together with finite real H3 and its zero transition maps for the even dyadic twist, give integral H3=0. Finite H2 is therefore bounded by order two at l=2 and is zero at odd l. The Euler characteristic with the ordinary real H0 term has the stated normalization. The fourth-power ideals have exact valuations 4,1,1 at 2,3,5 and are the unit ideal at every larger prime. Consequently the finite H1 orders are uniformly bounded.

Every resulting finite integral H1 class is a fractional coboundary. The absence of invariants in Q_l(4) makes the invariant fractional classes inject exactly, giving local coefficient orders 16,3,5. Their product is C240 with the literal cocycle (chi^4-1)/240.

The local restriction of a nonzero fractional class cannot vanish at any finite place: an integral coboundary would force its fractional primitive to be integral because some local chi_l^4-1 is nonzero. The three Frobenius evaluations are exactly k/3 modulo16 at (q,l)=(3,2), and k/16 modulo3 and modulo5 at (2,3) and (2,5). The CRT map is an isomorphism, and each of the three Hall coordinates is independent. Thus the global lift torsor has exactly 240^3=13,824,000 members.

The real H1 group for the even twist is zero, so every global lift of a real-matching lower section has the same required class-four real image. The finite witness bound follows by excluding each member of the finite global torsor at a chosen place. An ordinary finite lower image leaves at most one candidate by local restriction injectivity, giving the exact two-place bound when that candidate fails elsewhere. The source does not assert that the complete matching intersection always succeeds.

## Independent execution

During the CP16 write pause, the certificate was copied to /tmp/local_preprint_a205_audit and executed there, leaving work/ untouched. It passed:

- the literal cyclotomic one-cocycle polynomial identity;
- 14,214 fourth-power-ideal unit cases;
- all 240 distinct and exhaustive CRT localization classes;
- 72 finite-place restriction-order checks;
- the 240^3 global lift count;
- the finite real-transition checks.

The temporary execution output and data have now been copied into the retained work/ audit evidence. This arithmetic certificate supplements the complete continuous-cohomology, conjugacy and compactness proof audited above.
