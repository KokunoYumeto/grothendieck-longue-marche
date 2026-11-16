# Independent audit of FP.37

**Conclusion: the stated necessary quadratic pentagon equation is proved.**
For actual multiplier-one gentle elements, the finite evaluation in the
marked group `S4`, with `p=(123)` and `t=(1234)`, defines an additive
coordinate `nu4`. Every genuine multiplier-one GT element satisfies
`epsilon2(W)=nu4`. The argument makes no finite-to-profinite lifting claim,
and does not prove that their difference is nonzero on the gentle group.

## Structural checks

1. Since the actual normalized free-group automorphism preserves the
   conjugacy class of `xy`, its quotient value `p R^-1 t R` has order four.
   The six possible `R` in `A4` are precisely `t^(2 nu4) p^a`.
   The induced quotient automorphism is `Inn(p^-a)`. Thus its kernel is
   preserved, and the standard GT multiplication formula gives addition
   of both finite coordinates. The quotient by `V4` has the exact marked
   pair of FP.33, so `a=a_f` with the same sign convention.
2. The reversing half twist interchanges the first and third pentagon
   generators, and the fourth and fifth, while fixing the second.
   Antisymmetry therefore gives the two inverse conjugate factors in
   FP.37.3 in their printed order.
3. For `z=(X4 X5)^-1`, the multiplier-one three-cycle is
   `H f(X5,z) f(X4,X5)=1`, where `H=f(z,X4)`. The checked central-factor
   equality gives `f(X5,z)=z^-1 H^-1 z`. Consequently the printed formula
   `f(X4,X5)=z^-1 H z H^-1` has the correct order.
4. The harmonic enumeration uses the image of the actual same frame beta,
   the actual positive level-three map, and the exact swap identity
   `f=s^-1 beta s beta^-1`. The square of the half twist is central in this
   two-generator braid subgroup, so this matches the involutory modular
   convention. Thus all actual parameter values occur among the finite
   possibilities enumerated. Surjectivity of those possibilities onto
   actual gentle elements is not needed and is not asserted.
5. The marked order-48 group has derived subgroup of order 12, disjoint
   from its central involution, and maps isomorphically there to `A4`.
   Hence a commutator word has the unique claimed lift of its marked S4
   value. Central stripping was checked against **both** generators.

## Independent certificate

`code/check_quadratic_pentagon_audit.py` imports no code from the audited
certificate. It implements the ring `(Z/4)[omega]/(omega^2+omega+1)`,
projective multiplication, and an adjugate-based inverse independently.
It checks the braid relations and central quotient, all reversing
conjugacies, the central order-three strip, the marked S4 quotient and
derived A4 complement, and the positive level-three map of the order-192
harmonic pair group. It independently obtains four harmonic values for
each rho and verifies all 24 printed matrix identities

`P = v^(epsilon2+nu4) w_rho^c`,

where `v` and `w_rho` are distinct nonidentity commuting involutions.
Therefore `P=1` forces the stated equality. Output is in
`records/check_quadratic_pentagon_audit.out` and
`records/quadratic_pentagon_audit.json`.

The existing strengthened actual R2 witness of LI.8 has `f in F'''` and
therefore has both coordinates zero. It does not settle nonvanishing of
this new character. No claim identifying this character with Delta or
the cubic-frame parity is justified by the audited calculation.
