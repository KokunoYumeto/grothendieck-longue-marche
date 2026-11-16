# D75 independent PBC audit — PASS

Completed 2026-11-15, approximately 20:30 UTC. I read the complete
`notes/de_compact_axis_draft.tex`, inspected its exact certificate, and
rechecked the local/global duality passage in D63. This is independent of
the root and FGH audits. No mathematical gap was found.

The actual axis quotient, after the integral gauge, identifies its Tate
untwist with the augmentation ideal of `Z_5[[Z_5]]`. The displayed
multiplication by the augmentation variable intertwines the actual
semilinear action, including the multiplier factor. Its discrete dual is
the continuous functions on `Z_5`, modulo constants, with the actual
affine action. This is an injection into the dual of the original
Alexander module, not a replacement of that module by an unrelated
permutation representation.

For a primitive Kummer class, restriction to the cyclotomic kernel has
image `Z_5`: otherwise its reduction modulo 5 would inflate from the
units, whose first cohomology with the nontrivial scalar action vanishes.
Scaling gives the exact translation subgroup `5^d Z_5`. The normalized
affine image is therefore precisely the asserted semidirect product.
For invariant functions modulo constants, the translation defect is
additive. Conjugating translation by the pure unit 2 forces this defect
to vanish. The remaining invariant functions are exactly the valuation
ball functions, modulo constants. Continuity supplies the direct sum,
rather than a product, on the discrete dual in the zero-local-class case.

The two integral gauges are compatible on the first `r` ball functions:
the extra local translation lies in `5^r Z_5`, as follows by evaluating
the local unit-2 element. Hence the local/global quotient really has the
stated rank `N-r`, or countably infinite rank when the local class is zero.
Equivariance of the actual dual injection proves that its intersection
with global invariants is exactly its own global invariants. D63's exact
compact kernel sequence, finite local duality, and Pontryagin duality
then give the claimed continuous quotient of `K_s`. The quotient splits
continuously because its discrete dual is a direct sum of divisible
`Z_5`-modules. This does not split the nonseparated global obstruction
group and does not identify the complementary factor of `K_s`.

The local coordinates in the Kummer basis `(5,6)` give the stated minimum
valuation formula. The logarithm sums converge for the actual `c_0`
coefficients. For the example `kappa(2)-c kappa(3)`,
`c=log(16)/log(81)` is an integral unit with residue 3 modulo 5; the local
coordinates cancel exactly while the global class remains primitive.
The prime-101 example and the finite-rank family have the asserted depths.

## Independent execution

I copied the owner's certificate to
`notes/pbc_D75_certificate_rerun.py`, ran it without changing the owner's
files, and compared the entire resulting JSON with
`code/de_compact_axis.json`. The comparison passed. It checks all six
finite affine orbit partitions, the integral determinant-one ball
function matrices, the 20-digit logarithm ratio, and the five prime
examples. The source and output hashes are retained in
`notes/pbc_D75_certificate_rerun_comparison.json`.

## Primary-source and scope checks

Milne, *Arithmetic Duality Theorems*, I Corollary 2.3 (printed p.28) and
I Corollary 4.16 (printed p.62), were opened at the primary author PDF
`https://www.jmilne.org/math/Books/ADTnot.pdf`; current retrieval references
are `turn970view0` and `turn970view1`. The actual inverse-limit/finite
cohomology bridge is the previously independently audited D63 argument.
The finite certificate is supplementary evidence; the continuous
duality and exact affine-image assertions follow from the proof above.

**Verdict: PASS.** No claim is made about the complete complementary
compact factor, the nonseparated obstruction, or a general section
classification.
