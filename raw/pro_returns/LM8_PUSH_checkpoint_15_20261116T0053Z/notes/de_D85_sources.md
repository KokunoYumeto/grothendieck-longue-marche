# D85 source, dependency, and exact-computation ledger

**Unregistered candidate.** Full proof: `notes/de_sha_global_independence_draft.tex`. Supporting exact certificate: `notes/de_sha_global_independence_certificate.py/.json/.out`. No canonical source or result-register entry is changed by these notes.

## Verified established inputs and their exact scopes

- **verified:** D83 gives the actual global and local operator subgroups for every closed away-five lattice, before imposing its local-generator equality. Its uniformly convergent Kummer cochains and one integral gauge in the lattice apply to infinite support. The present proof uses exactly those formulas.
- **verified:** D82 proves that the actual Kummer cocycle of five factors through the untwisted image, that the quotient by its joint kernel with the cyclotomic character is the full affine group, and that the joint kernel contains an actual cubic-primitive element. The raw moment normalization is Nakamura–Sakugawa–Wojtkowiak equations(1.1)–(1.2), <https://arxiv.org/pdf/1410.1045>, independently opened in the D82 audits. No new higher-weight extension or formal replacement action is assumed.
- **verified:** D78/D81 establish continuous translation coinduction and the actual inclusion of the coefficient invariants. D85 also explains the finite-coset transversal for its open rank-two lattice and why the natural restriction map is the same coefficient inclusion.
- **verified:** D84 computes the rank-one connecting ideal with its actual semilinear action, including the three-jet extension, the exact cyclotomic-power relation inherited from D79, and the natural augmentation-square inclusion at both infinite indices. D85 maps its extra finite-index term to that actual module; it does not compare rational dimensions or choose unrelated invariant identifications.
- **verified:** D77 computes all local/global Cartier invariants, their natural axis maps, and the continuous splitting of the compact kernel. The exact infinite comparison in D85 is written using that same axis quotient.
- **verified:** D43 and D80 give the local discrete Cartier H1 vanishing and a single common finite coefficient level despite arbitrary infinite ramification. Their finite-duality source is Milne ADT I.Corollary2.3, <https://www.jmilne.org/math/Books/ADTnot.pdf>. The exceptional primes are finite at the original residual cubic level; no uniform denominator claim is made for all primes separately.
- **verified:** Finite affine Chebotarev descent is the established D78/D83 argument, with the primary theorem Milne CFT V.3.23, <https://www.jmilne.org/math/CourseNotes/CFT.pdf>. It is applied at a finite coefficient level before taking the filtered union.
- **verified:** D74 computes the whole first-cohomology fibre only once the explicit rational point supplies section existence. D85 asserts no general existence criterion.

## New integral module argument

The only new away-lattice shape is `L=Z5*u + 5^h*Z5*r`, with h positive and u,r an integral basis. In its actual completed group-ring coordinates, the ideal is `(x,g_h)` with `g_h=(1+y)^(5^h)-1`. Modulo y times this ideal, it is exactly `x Z5[[x]] direct-sum Z5*g_h`, and x annihilates the second term. The local relation is `f_lambda(x)+nu*g_h`. The extra cyclic term carries exact compact character chi cubed, hence nontrivial tame character chi squared after the Cartier untwist. Its coinvariants vanish integrally, leaving the actual D84 ideal module.

The natural map at lambda zero and an exact valuation boundary is explicitly the augmentation-square inclusion into the augmentation ideal after the actual axis quotient. The extra cyclic term maps to zero and has zero coinvariants. Thus no comparison of infinite coranks is used.

The nonzero cubic class remains nonzero on the finite cyclic global coefficient quotient: an actual valuation-one, cubic-zero operator has multiplier minus one equal to y times a unit, forcing any hypothetical primitive to be constant. A primitive cubic element in the joint kernel then contradicts it.

## Certificate scope

The supporting program uses monic Groebner reduction over the integers for the ideal `(xy,y*g_h)`. It checks the exact extra-generator character, detects the incorrect character, and checks the coupled local relation including negative exponents after clearing only units. It exhausts all480 ordered residual bases and all five lambda residues, and verifies the local-depth minimum with actual cancellations and infinite values. It also checks the new actual point `t=-799`, its prime factorization, the Smith form of its away lattice, and its exact five-adic logarithm depth. These finite calculations support the new algebra; the proof handles all indices and all infinite limits structurally.
