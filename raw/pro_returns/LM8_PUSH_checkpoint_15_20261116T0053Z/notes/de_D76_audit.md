# D76 integration, exact certificate, and source audit

Integrated as sections/D_alexander_three_axes.tex after the full root and FGH written-proof audits passed. FGH's detailed ledger is notes/fgh_D76_audit.md; the original full candidate remains notes/de_three_axis_draft.tex. D75's separate proof and audits remain unchanged.

The new assertion applies to every actual Alexander module A_(a,b), whether or not its section fibre exists. The first two stable axes carry the completed Kummer parameters a,b. The third carries a−b+(1−chi)/2, and the half-cyclotomic term is an actual integral coboundary. This uses D39's exact reflection identity, not a graded approximation.

The three-axis interpolation map has exactly two constant compatibilities and one linear compatibility. Its cokernel is free of rank3. Every higher diagonal discrepancy is corrected integrally by uvL(u), since uv restricts to −u²/(1+u). Therefore the dual kernel has component functionals supported in constant and linear jets; under multiplication by t−1 those become polynomials of degree at most2 in the measure coordinate. Every integral gauge preserves this degree bound.

If a sum of three locally invariant classes is globally invariant, each translation defect is such a polynomial. Local unit invariance gives f(2z)=f(z). Combining doubling with scaling gives successively7A=0,3B=0,C=0; all are valid on arbitrary five-primary torsion coefficients. Exact global affine images then make each summand globally invariant. This proves the joint quotient injection, including zero-axis and infinite-depth cases, without assuming independence.

Pontryagin duality and D63 give the stated compact surjection. Its dual is divisible and hence injective, so the compact map splits continuously. The complementary compact kernel is not classified in this theorem, and no assertion of section existence is made. The finite-support cusp parameter kappa(101) has two distinct boundary contributions and therefore a Z5² factor.

## Executed exact certificate

code/de_three_axis.py, code/de_three_axis.json and code/de_three_axis.out executed PASS. The code constructs a compatible triple with nontrivial jets and verifies its integral lift through degree8, including exact first and second axis restrictions. It symbolically computes the translated measure polynomial, the doubling/scaling defect, and the successive coefficients7,3,1. The Vandermonde determinant is2; invertibility of2,3,7 is verified modulo5^n for n1–7. These checks substantiate the identities; the continuous duality statement is proved in the text.

## Primary and established inputs

- verified: D35's actual Fox multiplier and D39's exact diagonal reflection, with their primary Ihara/NSW source audits retained. The third-axis formula is multiplied out explicitly in the proof.
- verified: D63's compact local/global dual quotient and D75's complete one-axis affine image and invariant function calculation. Root and FGH reread the exact used steps.
- The jet interpolation, polynomial-defect annihilation, joint quotient injection, and continuous splitting are proved directly. No additional unverified external theorem is used.

No diagnostic PDF was created. D77's proposed full local/global invariant classification is separate notes-only research and was not used to strengthen this registered result.
