# Independent audit of D.54 and D.55

**Result: PASS.** The proof fragments, both metadata files, and the shared exact certificate were read independently. The certificate was rerun successfully; its 14 cases are recorded in `work/part_a/d54_d55_audit_stdout.txt`. No proof correction is required.

## D.54: actual cyclic covers and the cubic norm

The input is an actual order-three representative, supplied by D.27, and the exact cusp-normalizer element of D.48, with prescribed quotient label and cube `c^kappa`, where the three-adic coordinate of `kappa` is a unit. This does not replace the full extension by one of its primary quotients.

An invariant nonzero character `chi: F -> C_q`, with `q != 3`, extends to the actual semidirect product by assigning zero to its specified section. The cube equation gives `3 chi(v) = 0`, so the cusp-normalizer element belongs to the precise kernel extension and has the form `v = n s` with `n` in the covering subgroup. The resulting surface cover has type `(1,q)`: its degree is `q`, all boundary monodromies are zero, and all `q` boundary lifts have degree one.

The representatives `c_i = f^i c f^(-i)` are the actual boundary classes of this finite cover. Conjugation by `v` preserves each label because `(v f^i v^(-1)) f^(-i)` belongs to the covering subgroup. Its action on each boundary homology class is multiplication by the three-adic multiplier, which is one. Conjugation by the selected section has the same action on homology, since it differs from conjugation by `v` by an inner automorphism of the covering subgroup.

The integral splitting is justified by the actual deck-average idempotent over `Z_3`. The filled cover is the compact torus with the index-`q` lattice displayed in the proof. Its deck transformations are translations, so act trivially on filled homology. The boundary module is the regular deck lattice modulo the norm line; it has no deck invariants because `q` is a unit. Thus `(1-e)M` is exactly the boundary module and `eM` maps isomorphically to filled homology. The latter maps isomorphically to base homology through the lattice inclusion, whose index is a three-adic unit. All these maps commute with the induced automorphism. In particular this is an integral equivariant splitting, not merely a dimension calculation over a field.

The cubic norm is zero on base homology by the cyclotomic relation, and is multiplication by three on the fixed boundary summand. It therefore vanishes on the entire mod-three homology of the cover. Applying it to `v = n s` makes the actual cube zero in that homology. The same cube is a unit power of a primitive boundary, whose class is nonzero because the cover has at least two boundaries. The contradiction proves the asserted invariant-character exclusion for every prime `q != 3`.

The deductions are exact: a nonzero invariant covector exists precisely when the reduction of `A_q-I` is singular; at three, D.48 gives determinant three and therefore injectivity over `Z_3`. A fixed element has zero image in every coordinate of the actual abelianization `F -> product_p Z_p^2`, whose kernel is the closed commutator subgroup. The scalar cubic conclusion uses diagonalizability of a finite-order matrix in characteristic zero after excluding the eigenvalue multiset containing one.

For a finite subgroup, a nontrivial kernel of `A_2` would have an element of order two or three, since D.33 bounds its order by a divisor of 24. The primary order-two case is excluded by D.33 and the order-three case by the new character argument at `q=2`. D.52's faithful-image classification consequently removes `C_12` and `D_24`.

## D.55: the square norm and full primary faithfulness

D.46 explicitly treats every positive involution before it addresses order-four lifting. Its conclusion supplies `A_2=-I` and vanishing mod-two first cohomology for every section centralizer. Thus no prior representation of the positive involution as a square is required.

The closed-subgroup cusp lemma is valid for an arbitrary prime. When the prime-part of the supernatural index is bounded, choose an open neighborhood attaining its maximal valuation. Restriction to every smaller open neighborhood remains injective by transfer, so the first-cohomology neighborhood colimit cannot vanish. When the prime-part is unbounded, choose an open neighborhood of index divisible by the prime. A selected full cusp primary subgroup forces the degree of its boundary lift to be prime to that prime, so this cannot be the only boundary lift. A character dual to that boundary restricts nontrivially to the selected full cusp subgroup. These are exact open subgroup and finite-cover maps. For the normalizer application the selected cusp is the given `c`, so no additional conjugator choice is needed.

Every torsion element in the cusp normalizer injects into the order-two quotient, and would therefore be an involution section. The global multiplier one makes it centralize the entire cusp, contradicting the preceding lemma. For its labelled root `v`, the exact equation `v^2=c^kappa` then forces `kappa_2` to be a unit: otherwise `2z=-kappa` is soluble in the full profinite integers, and `v c^z` is an actual involution with nontrivial quotient label. This argument uses the full global multiplier, as the proof explicitly states.

For an invariant odd-prime character, the same cover argument over `Z_2` has action `-I` on the deck-invariant base module and identity on the boundary augmentation. The square norm vanishes modulo two. It cannot equal the nonzero homology class of the unit boundary power. Therefore no such character exists. At an odd prime a determinant-one involution matrix is diagonalizable with equal eigenvalues, and the identity possibility has just been excluded; the remaining matrix is exactly `-I`.

For each prime `p`, a nontrivial kernel of `A_p` on a finite subgroup again contains an element of order two or three. Positive involutions have image `-I`; negative involutions have determinant `-1` globally by D.43; and cubic elements have nontrivial image at their primary prime by D.33 and at every other prime by D.54. This proves faithfulness at every prime.

The use of the three-adic normalizer to remove `Dic_12` is valid with this faithfulness. Its normal subgroup of order three has the faithful irreducible quadratic representation. The order-four inverter would also have to retain order four. D.52's exact quadratic-field calculation says that a finite-order inverter squares to the identity: its square is a norm, the only possible finite scalar alternatives are `1` and `-1`, and the latter is not a norm in `Q_3(zeta_3)`. This gives the stated contradiction. The nine remaining types have the explicit existing realizations in D.50 and D.52.

Finally the square of an arbitrary order-four outer element is positive, so its homology square is `-I` everywhere. At a negative multiplier coordinate the roots of `X^2+1` must be equal, giving a scalar matrix; the root is integral and a unit, and for odd `q` its residue forces `q = 1 mod 4`. The dyadic coordinate is already positive. This conclusion leaves exactly the scalar cases stated in the fragment.

## Executed certificate and scope

The program `work/part_c/code/torus_cover_norm_d54_d55.py` was rerun directly. It verifies seven cubic cases with cover degrees `2,5,7,11,13,17,19` and seven square cases with cover degrees `3,5,7,11,13,17,19`.

For each case it constructs the graph chain complex of the specified cyclic cover, verifies first homology rank `q+1`, the boundary rank `q-1`, nonvanishing of every individual boundary vector, the rank-two deck average, its exact complementary decomposition, commutation of the forced action with the deck action, fixed boundary vectors, and the vanishing norm. These finite computations check the displayed module identities; the proof's exact maps establish the all-prime result. The output explicitly makes no finite-to-full automorphism lifting inference.

The metadata preserves the remaining cubic and quartic scalar multiplier cases and geometric conjugacy as unresolved. The new complete result is the abstract finite subgroup existence list together with full primary homology faithfulness; it does not silently assert those remaining conclusions.
