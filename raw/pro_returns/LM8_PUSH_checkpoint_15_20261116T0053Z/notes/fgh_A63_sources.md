# A63 source and proof-gate ledger

Candidate `notes/fgh_A63_draft.tex` is unregistered pending full independent audits. Its exact certificate has executed PASS.

## Fresh primary sources

- **verified:** Silverman, The Arithmetic of Elliptic Curves2e, https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf , CorollaryIV.4.4 printed126 (PDF143), and TheoremIV.7.4 printed134 (PDF151). Freshly opened exact passages in `turn989view2` and `turn989view3` after full source `turn986view0`. These supply the integral p-series divisibility and the height/inseparable-degree comparison. The exact height-one torsion valuation1/(p−1) is proved by comparing the two uniquely lowest terms, not quoted without a source.
- **verified:** Liu, Algebraic Geometry and Arithmetic Curves, https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf , Proposition10.1.16 printed460–461 (PDF476–477), Theorem10.3.34(b) printed518–519 (PDF534–535), freshly opened `turn989view0` and `turn989view1`. These give extension of actual automorphisms to the canonical model and its identification with the unique stable model. The same theorem's proof explicitly describes the contracted rational chains. The elementary marked-fibre/tree argument is written out in the candidate.

## Internal dependencies and new gates

A62 provides the actual exponent-p Heisenberg deck group, exact proper stable main/tail charts with k2/4 and all positive-genus components, and compact type. A41/A42 apply only after the explicit companion/path proof. A11 transfers normalizer recognition through the actual open immersion to A62; no nilpotent-closure assertion is used for the enlarged composite.

The key new step is exact integral translation in a good local parameter s: s(P+T)−s(P) is divisible by t(T), so at the actual tail Gauss valuation its quotient by rho has strictly positive valuation. Thus the actual Gc action fixes reduced U. Its residual AS action is precisely V↦V+c; the centre acts faithfully, so its kernel is a noncentral order-p subgroup acting identically on that tail. Every generic stabilizer is trivial or exactly the centre, so this kernel gives a free marked orbit with identical specialization. The subgroup can depend on the tail. All rational stable components are pointwise fixed because the graph is fixed and each has at least three fixed nodes. The same-unmarked-point assertion is converted explicitly into a rational joining path after marked separation.

## Exact certificate

`notes/fgh_A63_certificate.py/.json/.out` verifies the symbolic degree/cusp/Euler identities; both strict radius inequalities; every tail character and its noncentral kernel in the Heisenberg models atp5,13,17,41; and an actual critical point (13,Y), Y²11, of exact order13 in E(F41²). The latter refutes a blanket odd-torsion avoidance argument and explains why the new actual-group proof is needed. It does not refute the fixed-group conclusion.
