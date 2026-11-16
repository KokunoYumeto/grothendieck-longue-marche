# Independent PBC audit of D.64

Auditor: /root/pbc_groups. Date: 2026-11-15, completed 17:28 UTC.
Draft audited: notes/de_alexander_one_prime_draft.tex, complete statement and proof.
Outcome: **PASS**. No mathematical correction required.

## Group presentation and coefficient comparison

1. The use of the maximal pro-five quotient is not circular. If
   N=ker(G→P) had a nonzero P-invariant homomorphism to F5, its kernel
   would be closed and normal in G, and the resulting extension of P by
   F5 would be pro-five. This contradicts maximality. The five-term
   sequence therefore gives H1 equality and H2 injection before any
   all-coefficient comparison is asserted.
2. Localization from the one-prime group over Q(zeta5) gives dimensions
   4 and 1 in degrees 1 and 2. The residue character detects tame inertia,
   while the degree-five cyclotomic character detects Frobenius because
   v5(q^4−1)=1. Thus the two local generators extend to a minimal
   four-generator presentation.
3. The local relator has abelianization (1−q^4)e_tau, of valuation one.
   Every element of R^5[R,F] has abelianization divisible by 25.
   Hence the relator survives in the one-dimensional relation module.
   The given finite-five-group coinvariant argument proves normal
   generation; it does not merely assume a presentation from a rank
   count.
4. The pro-five group is consequently the actual free product
   (Z5 semidirect Z5) * F2, with the specified local group embedded.
   Compact normal forms prove that the two-generator factor is precisely
   the claimed semidirect product.
5. Free-product restriction gives the higher-cohomology isomorphism.
   The base F5 inflation comparison follows from the already established
   dimensions and injection. Every finite P-module has a filtration by
   trivial F5 modules, so induction using the full long exact sequences
   proves the comparison for all needed finite coefficients.

## Actual action, averaging, and integral first cohomology

6. Each actual finite Alexander module has five-power action over
   Q(zeta5); hence it is a P-module. This is checked using the finite
   filtration, not by replacing the arithmetic action with a graded
   approximation.
7. The local decomposition subgroup maps onto C4 and intersects P in D.
   A coprime complement inside that actual subgroup normalizes D.
   The restriction isomorphism is equivariant for this complement, so
   exact averaging gives the asserted global/local H2 isomorphism.
   At the local field over Q(zeta5), Q=q^4 lies in 1+5Z5; the discarded
   factors have no positive five-primary cohomology.
8. The compact passage is valid: local and finite-ramification
   cohomology groups with finite coefficients are finite, so the
   relevant inverse systems satisfy Mittag--Leffler.
9. For nonzero local valuation pair, D.43 applies over the finite local
   extension and gives H0(D,A)=H1(D,A)=0. Every cocycle therefore has a
   unique representative vanishing on D. Arbitrary values at the two
   free generators extend by the universal property applied to their
   graphs in A semidirect P. This proves the actual compact isomorphism
   H1(P,A)=A².
10. The normalized representatives form a C4-stable module. On its
    mod-five associated graded, the factor is
    F5(j+2)^(j+1) tensor W, with W a nonzero two-dimensional C4-module.
    Exact averaging and actual surjectivity onto each finite
    augmentation quotient yield arbitrarily large invariant mod-five
    quotients. Compactness, torsion-freeness and countability then give
    the claimed countable product of Z5. There is no inference of
    inverse-limit surjectivity from successive finite-index images.

## Unrestricted cohomology and section fibres

11. A finite-coefficient global class locally zero away from five first
    comes from the finite-ramification group by the residue sequence.
    Its q restriction is zero, so the actual H2 restriction isomorphism
    forces the class to vanish. Thus every finite K_r is zero.
    D.63 supplies surjectivity, including cancellation of the
    reciprocity functional by the component at five.
12. Restriction at q is an actual retraction of finite-ramification
    inflation. The algebraic splitting of the non-Hausdorff continuous
    H2 group is therefore justified without inserting an unsupported
    closure. D.48 and D.63 give the stated Jannsen kernel and separated
    quotient.
13. The pullback extension has the explicit continuous set section
    x^{a(g)} y^{b(g)}. Its multiplication defect is consequently a
    continuous two-cocycle in the actual compact module. Its vanishing
    is equivalent to a continuous splitting, and the H2 restriction
    isomorphism reduces this exactly to the local q obstruction.
14. Since q−1 is a five-adic unit, local completed unit Kummer classes
    vanish. The local pair is precisely the valuation pair. D.42's
    three cusp lines therefore give a_q b_q (a_q−b_q)=0, including the
    zero pair. Zero abelian inertia outside S forces zero entire
    metabelian inertia, so every unrestricted lift descends to the
    stated finite-ramification group. D.35 gives the exact torsor and
    cusp parameters with no additional stabilizer quotient.

## Independently opened primary source

Gartner--Wingberg, *Corestricted Free Products of Profinite Groups*,
Theorem 4.2, printed page 27, was independently opened at
https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/CFP.pdf .
Browser references: turn757view0, turn758view0.
The theorem gives the degree-two restriction isomorphism, and the
higher-degree isomorphisms under the stated quotient-dimension
hypothesis. Taking a finite index set and the corestricting subgroup
equal to each factor is legitimate; the quotient groups are trivial.
The augmentation-ideal argument in D.64 also directly proves the
specialization used.

Milne ADT's finite localization, cohomological-dimension and
Poitou--Tate inputs were independently opened during the immediately
preceding D.63 audit; their precise references and checks are retained
in notes/pbc_D63_audit.md.
