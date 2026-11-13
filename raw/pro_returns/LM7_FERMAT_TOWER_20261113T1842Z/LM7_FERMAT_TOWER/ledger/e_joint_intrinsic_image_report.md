# E.83 — the intrinsic obstruction image in the conjugate joint quotient

The exact central map from the rank-330 intrinsic lattice to the four-dimensional joint target factors through the index-nine lattice established in E.80. The new result evaluates the resulting map on local second cohomology, including its literal coordinates in the retained E.74 and E.82 Smith bases.

## Natural cohomology map

Write the product-central coordinates as `(r,s,r',s')`. The actual intrinsic coefficient image is

`L = { r'-r in 3 Z3, s+s'-2r in 3 Z3 }`.

Its basis `(r,s,a,b) -> (r,s,r+3a,2r-s+3b)` has determinant nine and the specified integral involution. Both its local H2 and the ambient target H2 are `C3^2`. Their explicit coordinate maps are `(r,b-a)` and `(r+r',s+s')`; inclusion induces `(r,t) -> (2r,2r)`.

The intrinsic H2 group surjects onto the first of these groups by the actual coefficient surjection and the natural coinvariant presentation. Thus its image in the joint obstruction group is exactly the diagonal `C3`. The remaining quotient character is `(xi,eta) -> eta-xi`.

The proof gives the literal equivariant diagram of central extensions and proves naturality of the nonabelian connecting obstruction, retaining its cochain choices and the E.77 factor of one half. In E.80's normalized coordinates, the target obstruction is exactly `(Delta R,Delta S) mod 3`. Therefore every intrinsic class-two preimage lies in the locus `Delta R = Delta S mod 3`.

The obstructed E.80 family has `Delta R=0` and `Delta S=7(5-N-M)`. Its members with `N+M != 2 mod 3` have **empty intrinsic class-two preimage**, a stronger and earlier obstruction than a putative intrinsic class-three lift. No existence assertion for the compatible members is inferred from this necessary image condition.

## Full coefficient and source coordinate extraction

The four unit-character rows are derived from the actual divisors of `h`, `1-h` and their conjugates, with E.37's current positive peripheral convention and `U_d=(v_d,-u_d)`. Their elliptic columns are determined integrally by vanishing on the actual proper elliptic map `j_*=[3I;U]`. The resulting 4 by 10 matrix is displayed in the theorem. Its induced 4 by 330 Hall matrix is fully saved and checked against 660 independent associative tensor expansions.

Both actual arithmetic intertwiners are verified. The E.78 change of Frobenius marking preserves these coefficient matrices by the literal conjugation formula and the commutative CM image on V; the proof retains that comparison explicitly.

In E.74's ordered 93 positive Smith coordinates, the resulting diagonal character is

`lambda(b) = b_89 + b_91 + 2 b_92 mod 3`.

All three contributing coordinates have order 27. Its complete kernel is `C3^63 x C9^24 x C27^6`; replace `b_89` by `k=(b_89+b_91+2b_92)/3 in C9`, with inverse `b_89=3k-b_91-2b_92 mod27`. All 6,561 triples in this changed coordinate block are checked in both directions.

## Comparison with all E.82 cusp families

Every cusp-family obstruction is killed by this character. The proof is geometric: modulo three only the B cusps have nonzero paired abelian image, namely `(y,y)`, while the two second-degree coefficients sum to zero. The complete 405 matrix columns are also independently checked.

On E.82's exact residual quotient `C3^11 x C9`, with its retained ordered coordinates, the induced character is

`eta_9 + eta_10 mod3`.

Its complete kernel is `C3^10 x C9`, with inverse `eta_9=-eta_10`. The theorem thus specifies one additional quotient of the remaining intrinsic obstruction coordinates, with the exact cohomological map and its inverse retained.

## Executed programs

`a_joint_intrinsic_image.py` is self-contained apart from SymPy. It verifies the small exact integer Smith systems and their inverse matrices, all 81 ambient residue vectors, all 729 actual-image inputs, nine index-two normalizations, and 81 descended-family residues.

`a_joint_intrinsic_coordinates.py` reads the retained E.41 Hall construction, E.74 actual matrices and Smith transformations, and the complete E.82 certificate. It derives all four unit rows; checks the 660 independent degree-three tensor images, both abelian and both degree-three arithmetic intertwiners, the exact index-nine image, all cohomological relation maps, all 405 cusp columns, and both kernel coordinate inverses. Every input hash is recorded. Both programs have actual PASS stdout and deterministic JSON certificates.

To run the coordinate program from its research location, use the existing main code directory as `--source-code` and the final E.82 JSON as `--cusp-certificate`. After integration all dependencies have their ordinary names in the same code directory and no arguments are needed.

The natural obstruction square and the explicit residual quotient sharpen the retained intrinsic map. The full compatible class-two image and its conjugacy fibres are the next separate calculation, reserved as E.85.
