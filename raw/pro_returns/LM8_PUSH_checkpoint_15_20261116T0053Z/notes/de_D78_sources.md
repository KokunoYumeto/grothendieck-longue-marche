# D.78 source and dependency ledger

**Unregistered candidate, pending independent audits.** Full proof: `notes/de_finite_sha_draft.tex`. Exact coefficient certificate: `notes/de_finite_sha_certificate.py/.json/.out`. No diagnostic PDF has been created.

## Freshly inspected primary statements

- **verified:** Milne, *Arithmetic Duality Theorems*, second edition, I.Theorem4.10(a), printed pp.56–57. Fresh opening `turn1022view0`, exact theorem `turn1023view3`. This gives the perfect pairing between the finite degree-one and degree-two global localization kernels. Taking finite Pontryagin duals of the existing inverse limit in D.63 yields the direct limit used in D.78. No interchange with an infinite product of local cohomology groups is used. URL: https://www.jmilne.org/math/Books/ADTnot.pdf .
- **verified:** Nakamura–Sakugawa–Wojtkowiak, *Polylogarithmic analogue of the Coleman–Ihara formula, I*, arXiv1410.1045v3, manuscript p.2, equations(1.1)–(1.2) and the paragraph immediately following(1.3), freshly opened as `turn1022view1`. These fix the raw cyclotomic Kummer character and the actual Jacobi-sum image unramified outside five. D.31/D.39 already prove its comparison with the chosen Fox convention, including the cubic coefficient κ3/48. No special-value formula or interpolated negative-weight character is asserted. URL: https://arxiv.org/pdf/1410.1045 .
- **verified:** Milne, *Class Field Theory*, V.Theorem3.23, printed p.164/PDFp172, fresh exact opening `turn1023view4`. It realizes a conjugacy class in the actual finite affine cocycle image by an unramified Frobenius. This proves descent of a locally trivial finite cocycle to its actual finite operator image. URL: https://www.jmilne.org/math/CourseNotes/CFT.pdf .

## Internal inputs checked at their exact scope

D.1 gives class number one and the S-unit calculation for Q(ζ5). D.77 supplies the local independence of ζ5 and φ modulo fifth powers and primitive local raw κ3. These imply actual local surjectivity to the global unramified operator image by the Frattini argument. D.31 gives the integral weight-three cocycle h on the full group; its normalized mod-five reduction c=48h has character χ³=χ⁻¹. D.35 and D.39 give the actual twisted Fox multiplier at every element, including all primes. D.63 defines the compact kernel and its finite-localization inverse limit. D.74 applies to the present finitely ramified pair once the rational point t=−2 supplies a section. D.77 computes all other compact groups; the three depths are zero here.

## New proof gates

The global action image is the actual compact semidirect product Z5²⋊I0, supplied by inertia at2 and3. The local-at-five image is exactly its primitive logarithm-line subgroup H5⋊I0. Its saturation is proved by the incompatibility of the local unit class κ6 with the sole global S-unit class κ5. All cochain gauges are integral.

Translation coinduction is established directly for continuous functions on the compact translation group. The local restriction kernel is then exactly the connecting image of an invariant quotient of the local line module. A primitive local cubic multiplier kills all higher jets; the three quotient characters are χ⁻²,χ⁻³,χ⁻⁴, giving a kernel of order five. This is an upper bound for the actual finite-localization inverse limit, without computing the whole H1(I0,Q5/Z5(−1)).

The lower bound is proved at one fixed finite coefficient level: the ten-dimensional order-five dual of Λ/(u,v)^4. Explicit constant, linear or cubic primitives work at every unramified Frobenius. At2/3 constant primitives work on the entire decomposition group; at5 the same local three-jet calculation supplies an integral primitive in the same module. This is the necessary uniform statement, stronger than separate triviality in a divisible target at each place.

## Executed exact certificate

All500 choices of χ∈F5× and a,b,c∈F5 satisfy the displayed primitive identity for the actual Fox-semilinear action. The program derives the coefficient matrix, uses the Cartier convention χ times inverse transpose, and avoids matrix-inverse artifacts by an equivalent transposed identity. It also derives the local line matrices, finds the unique normalized local primitive, pulls it back into the actual ten-dimensional module, and checks the quotient determinant −315/512 has five-adic valuation one. Finite computations support these explicit identities; the arithmetic image, infinite coinduction, and duality arguments are proved in the text.
