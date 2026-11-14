# Root review of D.29: characterwise reciprocity without admissibility

The complete candidate `D_unrestricted_reciprocity_candidate.md` was read and accepted in its exact stated scope on14November2026. The adjacent finite certificate was read and rerun; it verifies the five specified primes by exact trial division, their cusp-avoidance congruences, and45 quadratic Hilbert reciprocity products. These finite checks corroborate the explicit prefix; the universal assertions are established by the proof.

## Convergence and actual local points

Nested moduli ensure that, for each p and each exponent r, every sufficiently late factor is1 modulo p^r. A finite initial product has a fixed p-adic valuation (one if p is one selected prime, zero otherwise), and multiplying by the convergent tail of units gives a nonzero limit. The recursive R_j condition is needed: it fixes the finite valuations of A_p+1 and A_p+2 by comparison with the positive integer P_(j-1). This proves A_p is neither−1 nor−2, so x_p=2+A_p is an actual ordinary local point away from the old and new punctures. Mere convergence would not have justified this conclusion. The real component is separately chosen as1; no real convergence is asserted, and positive partial products have exactly its real Kummer classes.

## Restricted-product failure and all finite extensions

At infinitely many distinct primes the valuation is1. For every modulus n>1, all but finitely many of these primes are prime to n, so their Kummer classes are ramified. This excludes the restricted product, and its modulus-two consequence excludes any global completed multiplicative class. Every finite number field is eventually split by the chosen primes, since its Galois closure occurs in the enumeration. Thus valuation one and failure persist at every such base. The finite-base norm assertion is only norm-of-restriction, with local products over all places above a place; it is correct in that scope.

## Reciprocity

Fix L,n,chi before choosing the finite support set T. Once the prime construction splits a normal closure of the extension cut out by chi, its local character is zero at every later selected prime. At every other place outside T, the chosen limit is a unit and the character is unramified, so their cup invariant vanishes. The identical T works for every finite principal product, although T depends on the character. Local openness of n-th powers allows one sufficiently late principal product to agree with the limit in all Kummer classes over T. Its global Brauer class has invariant sum zero, including the real places. This proves every stated characterwise sum without illicitly applying Poitou–Tate to a tuple outside its domain.

The bound q_j>2^j gives a convergent sum of reciprocal primes, hence Dirichlet density zero. At these primes x_q is2 and1−x_q is−1 modulo q, so both original coordinates are units. Nothing establishes their global completed Kummer classes, or a section, or all finite-neighbourhood conditions. The candidate states all three limitations explicitly. It therefore refutes the proposed implication from characterwise reciprocity and finite-base functoriality to admissibility, without refuting D1–D4.

## Primary source verification

The root independently opened Milne, J.S. (2020), *Class field theory*, version4.03, <https://www.jmilne.org/math/CourseNotes/CFT.pdf>. Verified ChapterIII Proposition3.6 and Lemma3.7, printedpp.109–110 (local Artin/cup invariant and valuation in unramified extensions); ChapterV Theorem3.23, printedp.164 (complete-splitting primes via the identity conjugacy class in a finite Galois extension); ChapterVIII Theorem4.2, printedp.241 (the global Brauer invariant exact sequence). These are precisely the primary inputs used. The global zero and unramified-unit zero statements are independent of any harmless cup-sign convention.

Accepted for integration as a separate proved limitation, with the programs and outputs placed under code/. It does not complete a continuous-section item.
