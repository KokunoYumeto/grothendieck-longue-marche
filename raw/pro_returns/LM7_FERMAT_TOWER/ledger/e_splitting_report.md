# Class-two audit of the splitting in §51.12

E.26 proves that the abelian splitting does not lift integrally or profinitely even to the class-two quotient. With the original modular generators and x=(sigma rho)^2, y=(rho sigma)^2, the exact free-group identities are (x rho)^3=[x,y] and ((x rho)sigma)^2=1. The preimage of the unique abelian complement is the infinite dihedral extension of S3 by Z(sign), of class 1 modulo3.

The explicit quotient P/(gamma_3(F) F^3) has 162 elements. The program constructs its regular permutation group from all 162 Hall normal forms, checks closure, all 4,251,528 associativity triples, and all 729 generator pairs for sections. It finds zero sections. The abelian quotient has 54 elements and nine sections; all 81 lift pairs give an order-nine lift of the order-three generator. The preimage of the chosen complement is D18. Every normalized one-cochain modulo3 was checked against the explicit carry cocycle, with no solution.

Exact quotient maps propagate the obstruction to the metabelian and third-derived extensions. The relative pro-p class-two extension has zero section classes for p=3, two for p=2, and one for p>=5. The rational class-two extension has a section obtained by multiplying x rho by c^(-1/3), with a single conjugacy class. The marked-depth quotient of E.2 has an explicit surjection to the class-two Lie quotient; the permutation swap does not preserve its defining ideal, as a displayed degree-four monomial proves.

Files: `sections/E_splitting.tex`, `code/e_splitting.py`, `code/e_splitting.out`, `code/e_splitting.json`, `ledger/e_splitting_results.json`. All code assertions passed. No external theorem or additional reference is required beyond the independently proved internal statements cited in E.26.
