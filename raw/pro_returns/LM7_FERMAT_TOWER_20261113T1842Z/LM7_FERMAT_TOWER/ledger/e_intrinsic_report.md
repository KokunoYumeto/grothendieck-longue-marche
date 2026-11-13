# Intrinsic cubic supplement E.31

## Deliverables

The complete statement and proof are in sections/E_intrinsic_obstruction.tex. The result ledger is ledger/e_intrinsic_results.json. The independent exact program code/e_intrinsic_obstruction.py has executed successfully and has corresponding .out and .json files. No new external theorem was used, so e_intrinsic_refs.bib records that existing verified sources suffice.

## New result beyond inherited depth

Inside the zero toric fiber of the complete abelian calculation E.24, the original tangential section lifts fully, while the Kummer class of the rational generalized-Jacobian torus point

t = (7,7,1,1,3+zeta3)

does not lift even to the intrinsic class-two pro3 quotient. Its toric image is exactly (1,1). The contradiction comes from a second actual map of the cubic, h=(x+y)/(x+zeta3*y), rather than from the original Fermat covering map. The latter toric minimum therefore cannot classify intrinsic liftability: two classes in one fiber give different answers.

The essential affine term is retained. At the source tangent O, h has leading coefficient zeta3*(1-zeta3)^-3. Multiplying by the two character values on t gives the total target Kummer pair (zeta3,7) modulo3. At the prime (3+zeta3) above7 this produces Frobenius and inertia coordinates (2,0),(0,1). Every possible Heisenberg lift has nontrivial commutator2C, but the tame relation forces commutativity in the exponent3 quotient. All nine central lift choices were checked.

This proof computes an actual cross term in the intrinsic based arithmetic action. The geometric quotient onto the order27 Heisenberg group is surjective, and the action over Q(zeta3) is the shear

(a,b,c) -> (a,b,c + kappa3(zeta3)(g)*b).

The quotient map kills the intrinsic third lower central subgroup, second derived subgroup, and third lower central subgroup of the marked peripheral normal subgroup. A Weil-restriction map over Q displays both conjugate comparisons simultaneously. These give the required exact morphisms to the intrinsic class-two, metabelian, and marked-depth problems.

The same finite obstruction applies to every class in alpha plus three times the kernel of the toric section map, an explicit nonempty coset in the zero toric fiber. The full classification of the remaining intrinsic section classes is not claimed.

## Audit

The A-structure agent independently verified the divisor characters, the conjugate cusp coordinate, the nontrivial tangential constant, the local field Q7, the Frobenius coefficient2, and the intrinsic factorization. The program also proves the exact field identities, verifies all27 group elements have exponent3, and checks all81 instances of the displayed inner-action shear.
