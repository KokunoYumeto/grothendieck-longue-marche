# A.67 independent DE proof, source, and certificate audit

**PASS.** Read the entire candidate and the complete exact certificate. Independently executed all certificate computations without modifying the owner script/output; the normalized full result equals the author JSON. Retained output: `notes/de_A67_certificate_rerun.out`. No mathematical correction is needed.

## Actual covers and completeness

The three translated x-coordinate functions have the displayed divisors and constant product. Their independent odd-divisor vectors give a connected V4 extension, and cyclic permutation of the three roots supplies an actual order-three lift. The composite is A4-Galois and branches only above O. In a surjection from the geometric rank-two fundamental group to A4, the commutator is nontrivial, hence is a nonzero V4 element. The C3 quotient is an actual elliptic isogeny. The residue exact sequence has a trivial proper-H1 summand and a unique nontrivial irreducible two-dimensional C3 summand over F2, so no extra equivariant unramified quadratic twist is missed. Averaging gives the stated lift conjugacy.

The explicit quotient map and target equation were independently rerun modulo the original cubic equation. Pole degree establishes degree three. The target j equation, its double quadratic factor, the two r values, and the actual complementary elliptic quotient all check. The independent elliptic differentials and V4 character decomposition give J_X isogenous to E' times F cubed. At two, the displayed j(F) has positive valuation: the factor36±21sqrt3 is a unit. Potential good reduction and the special j=0 supersingularity give two-rank0; actual norm quotients preserve the conclusion for every intermediate.

## Three-adic pointed model

For the chosen cyclic3 kernel on a good supersingular E', the three points reduce to O. The single chart t=c*u separates their reductions0,1,−1, and the formal addition law gives the actual residual translation u↦u+1. The horizontal divisor degrees of each f_j are zero on every component of the regular semistable base tree. The intersection equations therefore make its vertical orders constant; after scaling, the functions are units with constant main reduction and the displayed rational-centre reductions. Because two is invertible, Hensel roots split the main component and the node collars. The tame V4 cover of the rational centre is genus0 with four unramified nodes, and the four elliptic tails exhaust genus4. This is an actual normalization/gluing construction, not a quotient/reduction interchange.

The exact residual rational map and all node/cusp orbits were independently rerun. Its four nodes are P1(F3), and its six cusps are F9 minus F3. The C2 quotient has four distinct cusp images and two distinct node images. The C3 quotient has two free cusp orbits at w=±i, separate from node orbits0,∞.

## Wild C3 quotient

The generic C3 action is free, hence its proper quotient has genus2. The actual norm quotient makes its Jacobian potentially good, so a semistable model has a tree. Distinct source component orbits restrict to distinct quotient valuations. On the centre, the orbit polynomial produces v^3−v in the quotient residue field and proves that the centre image is exactly rational. The three cycled tails have trivial decomposition group and give one elliptic component. On the fixed tail, translation by P reduces to the identity through its isomorphism to the good E' component. Its orbit polynomial places every cube in the quotient residue field; the residue field is between k(C)^3 and k(C), so its normalization still has genus1. These two genera exhaust the generic genus. Thus resolution or semistabilization cannot introduce a further positive-genus component. The free residual cusp orbits give smooth distinct marked images; the rational centre has two marks and two outgoing branches and survives marked stabilization. This verifies the precise A41/A42 pointed hypothesis without a false general wild-quotient assertion.

At coefficient3, the actual four supersingular elliptic tails and norm quotients give good Jacobians of three-rank0. At coefficient2, the explicit elliptic factor proof applies. At coefficient primes≥5, the closure order12 is prime to the residue characteristic and the existing A59/SGA1 tame good-model argument applies; A57 handles the genus≥2 curves. The genus1 rows are exactly the isogeny families of A40. No all-solvable or universal TaskA5 conclusion is added.

## Fresh primary checks

- **verified:** Silverman VII Proposition5.5, printed197, and its proof referral to Appendix A.1.4(b); the appendix proof is printed413. Reopened exact statement and characteristic-two proof: turn1062view0, turn1063view4, turn1064view3. URL https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf .
- **verified:** Serre--Tate, original Theorem1 and Corollary2, printed493, with perfect residue-field and prime-to-residue Tate-module hypotheses. The exact indexed original was reopened as turn1064view0/turn1064view1; the initial scan-only open had no text and is not counted as the source check. URL https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf .
- **verified:** Liu 9.2.2 factorization, 9.2.5 rational exceptional divisor, and 9.2.7 elimination of indeterminacy, printed395–397, reopened turn1064view2. The exact Jacobian/Picard comparison10.4.24, printed542–543, was reopened turn1062view1/turn1063view0. URL https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf .

The remaining invoked A40/A41/A42/A46/A57/A59 results are established project dependencies; the new geometric and finite computations above were checked independently.
