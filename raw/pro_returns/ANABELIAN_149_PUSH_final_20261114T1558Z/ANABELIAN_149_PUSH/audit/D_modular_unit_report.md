# D.32: an explicit obstruction to modular-level unit growth

## Proved statement

The actual symplectic-isomorphism cover attached to the section's integral Legendre N-torsion is a geometrically connected finite étale neighbourhood. At every odd level where its torsion image is full GL2(Z/N), each of the three original cusp fibres is one Galois orbit. Thus the rational unit rank is exactly two. Every rational unit has a positive power equal to a rational constant times a monomial in the two original units lambda and 1−lambda.

The proof retains the distinction between the full torsion cover and its central-sign quotient: full inertia has orders N,N,2N, while projective inertia has order N at all three labels. With the two-sided Galois action on level isomorphisms, cyclotomic-kernel restriction acts on left inertia cosets by the right image of a quadratic twist of the section's representation. That twist remains surjective, because the odd-level special linear group has no quotient of order two.

The explicit rational point lambda3 gives full GL2(Z5) image. Type I2 multiplicative inertia at the local prime3 supplies an entire Z5 unipotent subgroup. The four points over F7 give trace4 and an irreducible mod5 polynomial, whose Frobenius moves its fixed line. The two root groups then generate SL2(Z5), and the cyclotomic determinant supplies GL2. This proves an infinite 5-power tower of unbounded geometric size but constant rational unit rank2.

## Consequence and limits

If two different original cusp labels occur in D.31, no nonconstant rational unit on these maximal-image levels can be regular and nonzero at both corresponding closed centres. Thus these levels cannot automatically furnish D.31's sufficient unit. The explicit section used to demonstrate constant rank is itself geometric; no nongeometric section or mixed-label section is constructed.

Manin–Drinfeld gives rank equal to the number of rational cusp orbits minus one on the projectivized congruence curve. It does not turn a large geometric cusp orbit into many independent rational units. A conditional finite-index variant also bounds the unit rank uniformly in a fixed prime-power tower. Arbitrary noncongruence neighbourhoods remain available in D.31, and no obstruction to all such neighbourhoods is asserted.

## Integration and verification

Root read the complete audit and approved integration as “Proved route obstruction.” The separate integrated file is sections/D_modular_unit_obstruction.tex, input immediately after D31. The prior full audit remains audit/D_modular_level_unit_rank_obstruction.md. Metadata and opened references are in audit/D_modular_unit_results.json and sources/D_modular_unit_refs.bib / D_modular_unit_sources.md.

The exact standard-library certificate code/D_modular_cusp_orbits.py/.json returns PASS. It verifies the mod5 groups, inertia orders, all cusp cosets and right-action orbit counts, E3(F7), the rational Frobenius-conjugation identity and the genus/cusp formulas at 5,25,125,625. The all-level and arithmetic claims rest on the written proofs, not on finite extrapolation.

D1–D4 remain unresolved. D32 records a failed proposed main route precisely; it does not supply the missing finite-ramification or mixed-label theorem.
