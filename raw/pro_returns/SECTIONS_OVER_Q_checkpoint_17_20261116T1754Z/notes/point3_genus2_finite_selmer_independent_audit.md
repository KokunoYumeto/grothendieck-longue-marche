# Independent audit of A193

Auditor: `local_preprint`. Full mathematical source and exact certificate: **PASS**.

Sources reviewed:

- `sections/point3_genus2_finite_selmer_loci.tex`
- `code/point3_genus2_finite_selmer_certificate.py`
- its retained output and data

The actual local Kummer field is the Eisenstein field `Q2(theta)`, `theta^4=54`. The three displayed classes represented by `3-theta`, `-theta`, and `-86-theta` are independent. The norm of the first is 27; the quotient of the third by the second is `1+(43/27)theta^3`, whose norm is a dyadic square and whose depth three excludes a square in the degree-four local field. The odd valuation of `-theta` separates the remaining direction. The branch-orbit calculation gives exactly one nonzero rational two-torsion class. The formal subgroup index and Nakayama argument, followed by the two independent logarithmic coordinates, therefore identify the actual local completion with `Z2 D + Z2 E* + C2 T`.

The finite Selmer criterion is the divisibility of the literal `E*` coordinate. I checked the logarithmic normalization and all three cases: positive odd valuation, negative even valuation, and the unit disc about three. The finite tests are necessary for the displayed quotient sections; the proof does not infer a global quotient section from a passing finite Jacobian test.

The cyclic-eight cover and its boundary words give the integral module `Z2[V]/(V^4+1)`, with the retained `C8` splitting. Thus the actual finite quotient has order `2^(4n+3)` and exact lower-central class `4n`, using the valuation of `V-1` in `Z2[zeta8]`. The example `t=14641/14587` has the displayed dyadic sheets and is excluded at the stated finite level.

The retained certificate was independently rerun successfully before CP15. The only suggested wording clarification concerned the finite odd-order kernel of the map from local points to their two-primary completion; it did not alter any map or mathematical conclusion.
