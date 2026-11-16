# Independent audit of A.61

**PASS.** The P/B/C agent read the complete uniform proof and inspected the exact certificate program. An independent execution at p=3,7,11,19 reproduced every stored output row, without changing the owner's outputs; see `notes/pbc_A61_independent_rerun.json`.

## Algebraic divided-operator proof

The elementary point count gives trace zero and the actual Frobenius identity F²=[−p]. The monic division numerator and coprimeness show that the reduced division polynomial is a nonzero constant; the recurrence at (0,0) gives its sign −1. Thus the divided polynomial is integral and monic of the stated degree, also at p=3.

The invariant vector field has p-th power zero in characteristic p: its p-th power is another invariant vector field, but the quarter-rotation gives it the opposite scalar eigencharacter. Hence the divided operator D^p/p is well-defined modulo p. Its two product identities are checked by the full multinomial expansion. Cyclic orbit divisibility handles all intermediate distributions in the p-factor identity; the p+1-factor identity uses DR constant, so every remaining intermediate derivative contributes an extra p.

The characteristic-zero logarithmic division identity has the correct principal parts at every torsion point and at O. The evenness of the division polynomial and the Laurent expansion of x remove the possible constant discrepancy. Reducing the integral identity and applying the divided operator identify the actual Frobenius root R, not an arbitrary primitive. Its pole order is exactly p. The kernel-of-derivation and elliptic no-simple-pole arguments give DR=a in Fp× and R=−cD^(p−2)x.

The hidden degree-p Taylor cancellation is established fully. The functions R,A,S and a are all defined over Fp, so the step a^(p−1)=1 is legitimate. The pole bound for E(R) follows by lifting R in L(pO), applying D^p/p, and taking its Frobenius root in L(2O). Applying the operator to h=R^(p+1)/a+S^p gives DS=RA/a. Consequently S has no linear term at any zero of R, while R has a simple zero there. The first Taylor term of h is exactly degree p+1; the otherwise invisible degree-p term is also zero.

## Actual charts and stable model

The main chart has normalized special function field Fp(E)^(1/p), giving one genus-one component with actual radicial degree p to the good elliptic fibre. The nonzero differential makes its generic point smooth. The centres are the p simple zeros of R=yQ(x), with Q squarefree and disjoint from the two-torsion x-coordinates.

Lifting these centres over an unramified extension preserves divisibility by p of every lower Taylor coefficient. The two chart constructions use the correct different scales: x=a+rho*U at non-two-torsion centres, and y=rho*U, x=a+rho²*W at two-torsion centres. The displayed valuations are strictly positive for every lower or higher unwanted term, including p=3. Unit partial derivatives give actual smooth integral charts with the Artin–Schreier special curve. Its pole, uniformizer, ramification jump, different and genus check directly.

The positive-genus valuations persist under common regular resolution and stable contraction; they are distinct because their restrictions have distinct centres or the generic point on the elliptic fibre. Their genera exhaust the generic genus, so every remaining component is rational and the dual graph is a tree. The actual map to the good elliptic model extends after resolving indeterminacy; the main component consumes its whole degree. Every off-main subtree is therefore constant. All p-torsion sections specialize to O, while all positive-genus tails lie over other points. Separating the cusp sections puts them on the rational marked tree at the unique main point over O. Thus the hypotheses of the actual A.41–A.42 criterion hold.

## Cover and conclusion scope

The division divisor gives the stated connected degree-p cover and ramification at all p² torsion points. The translation ratio has p-divisible principal divisor, so every p-torsion translation lifts after a finite constant extension. The resulting order-p³ central extension is nonabelian because its peripheral commutator has order p. The quarter-rotation fixes the central group and has no nonzero invariant linear functional on E[p]; it therefore kills the p-th-power map and proves exponent p. This identifies the actual Heisenberg group. The previously audited A.59 applies to this genuine p-group cover, while A.41–A.42 supply the separate full fixed-group assertion. No inference from a merely abstract module or Jacobian decomposition is made.

## Primary sources independently reopened

- Silverman, *The Arithmetic of Elliptic Curves*, second edition, https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf : Exercise III.3.7(a)–(f), printed pp.105–106 (`turn968view0`, `turn968view1`), and Theorem V.2.3.1(b), printed p.142 (`turn967view1`). The exercise's general Weierstrass hypotheses include characteristic three; its short-form suggestion is not an exclusion.
- Liu, *Algebraic Geometry and Arithmetic Curves*, https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf : Theorem9.2.2, Remark9.2.6 and Theorem9.2.7 (`turn969view0`), and Theorem9.3.21 (`turn969view1`). These supply the actual resolution and positive-genus persistence inputs used in the established A.52/A.58 argument.
- Crew, *Etale p-covers in characteristic p*, https://www.numdam.org/item/CM_1984__52_1_31_0.pdf : Corollary1.8 (`turn967view2`, page-image references `turn969view2`–`turn969view3`) for the one-branch p-rank calculation.

No substantive gap or required correction found. The finite polynomial checks support the formulas; the uniform operator proof supplies the assertion for every inert prime.
