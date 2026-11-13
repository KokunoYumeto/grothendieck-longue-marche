# E.78 — evaluated wild class-three arithmetic

## Result and exact scope

The local field is \(k=\mathbb Q_3(\zeta_3)\). The target is the actual quotient
\(C=F/\gamma_4F\) induced by the map
\(h=(x+y)/(x+\zeta_3y)\) from the punctured cubic. The proof retains the source
tangent, an explicit coherent root system, the exact E.49 transport from the
original E.37 Frobenii, and the actual E.77 source presentation over its fixed
free quotient.

The two genuine arithmetic operators have
\((\chi,\kappa_a)=(7,-5/2)\) and \((7,1/2)\). Their entire class-three Hall
actions are printed. The resulting section equation has four actual source
values. Its class-two relation and both class-three errors are explicit
polynomials in those values.

The class-three image is exactly the simultaneous divisibility by three of
the two displayed errors. The exact correction is division by 336 on its
image. Every nonempty full geometric-conjugacy fibre is
\(\mathbb Z_3^4\times(\mathbb Z/9)^2\), with representatives, inverse
coordinates and the actual central conjugators. The preceding class-two
image is also evaluated, with fibres
\(\mathbb Z_3^2\times\mathbb Z/3\). The abelian coordinate map and its inverse
are specified as well.

## A constructed intrinsic obstruction

The family with source values
\[
 a_0=y,\qquad u=x^{5/2}c^N,\qquad a'_0=u'=1
\]
has exact error \(e^{7(2-N)}\). Every family member has an actual intrinsic
class-two preimage:

1. Choose a rational cubic cusp where \(1-h\) has order one.
2. Transport its actual positive inertia generator so that its image is
   exactly \(y\), using the proved surjection on geometric groups.
3. Retain the actual cusp-path conjugator \(u_*\) for the chosen Frobenius.
   Its left cusp-power correction has target class-two value \(x^{5/2}c^2\).
4. In \(N/\gamma_3N\), multiply this source-generator value by
   \([x_*,y_*]^{N-2}\), where the chosen \(x_*,y_*\) map to \(x,y\).
   This is a central change and preserves the exact source relation.

At parameter \(N=2\) the construction has a full intrinsic lift. At
\(N=0\) its nonzero quotient obstruction excludes every intrinsic
class-three lift. Their intrinsic abelian coordinates agree. Thus the
intrinsic example is established by actual maps and source values.

The exact kernel of the general intrinsic-to-target map remains printed.
No conclusion about arbitrary target preimages, full global section sets,
or a based descent of \(h\) to \(\mathbb Q_3\) is asserted.

## Proof and certificate

- Section: sections/E_wild_class3.tex, E78.1–E78.30.
- Self-contained program: code/a_wild_class3.py.
- Actual output: code/a_wild_class3.out.
- Machine-readable certificate: code/a_wild_class3.json.
- Requirements: Python 3 and SymPy; no saved binary input or downloaded paper
  is needed to execute the certificate.

The final execution passes:

- The full symbolic identities for the actual operators and all three error
  polynomials, including the exact central change 336.
- 640 independent checks in an associative Magnus algebra.
- All five Hall images for both evaluated operators.
- Eight exact original-to-E.49 source and root transports.
- 67 class-two and seven class-three lifting cases.
- 180 abelian, 201 class-two, and 35 class-three coordinate/inverse checks.
- The symbolic family error for every parameter \(N\).
- The symbolic cusp-path correction, keeping its unknown \(V,d,e\)
  coordinates until the actual morphism eliminates the required terms.

The all-input theorem is proved by integral polynomial identities,
the actual local source presentation, and explicit conjugacy maps.
Finite numerical checks corroborate those proofs.

## Sources and remaining question

The official original Furusho paper was reopened at Theorem 2, equation
(5), and the complete relevant proof and Corollary 12 in Section 3. Its
verified bibliography entry is reused from E.54. The exact E.49, E.54 and
E.77 internal proof dependencies are recorded separately in the source
evidence ledger.

The remaining intrinsic arithmetic question is the image and the fibres
through the full kernel of \(N/\gamma_4N\to C\), together with the other
actual geometric operators required by E.23. This calculation evaluates
one full arithmetic quotient and constructs a genuine intrinsic
nonlifting example.
