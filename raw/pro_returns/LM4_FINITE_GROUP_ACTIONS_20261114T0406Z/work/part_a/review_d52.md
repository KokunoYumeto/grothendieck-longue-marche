# Independent audit of D.52

**Result: PASS.** I read the complete TeX proof, its result metadata, and its finite program, checked the D.33 and D.50 inputs against their specified statements, and reran `work/part_c/code/torus_finite_types_d52.py` successfully. The rerun stdout is retained at `work/part_a/d52_audit_stdout.txt`.

## Exact representation kernels

D.33 supplies the total order bound `|G| divides 24` and injectivity of `A_p` on actual finite p-subgroups. Thus `ker(A_2|G)` cannot have even order, by Cauchy's theorem, and has order 1 or 3. This uses no faithfulness assertion at the prime 2 on odd subgroups. When the kernel has order 3, an actual Sylow 2-subgroup is a complement: its order equals the index of the kernel, its intersection with the kernel is trivial, and its product with the normal kernel is all of G. The displayed multiplication map is therefore an isomorphism.

## Normality of the order-three subgroup in the dyadic image

For the actual image `H <= GL2(Q2)`, four Sylow 3-subgroups give a transitive conjugation image in S4. The kernel has order at most six. If its order were divisible by 3, its unique subgroup of order 3 would be characteristic in that kernel and hence normal in H, contradicting four Sylow subgroups. The image is consequently A4 or S4 and the remaining kernel has order one or two.

A faithful 2-dimensional characteristic-zero representation of V4 has all three nonidentity sign matrices, including the scalar -I. The A4 order-three conjugation cannot permute that scalar with the other two matrices. This excludes faithful A4 and S4 images. The central-double-cover case has a normal subgroup of order 8; the established D.50 classification makes it D8. Its automorphism group has order 8, so every element of order 3 centralizes it. The resulting direct product has a normal Sylow 3-subgroup, which contradicts the initial four. The argument is exhaustive at orders dividing 24.

The subsequent Q2(zeta3) centralizer and semilinear normalizer descriptions follow explicitly from the irreducible degree-two minimal polynomial and a vector/cyclic-vector basis. The two coefficient alternatives for a square root of -1 are `a^2 = -1` and `a^2 = 1/3`, both excluded by dyadic unit squares modulo 8. The finite centralizer is therefore C3 or C6, and the outside element's square is a scalar sign. These yield C3, C6, S3, D12, and Dic12 with the indicated presentations.

## Three-adic determinant character

The proof uses injectivity of A3 only on the actual normal C3. This is sufficient: a group element centralizes or inverts C3 exactly as its matrix centralizes or inverts that faithful image. In Q3(zeta3), the minimal polynomial is irreducible by the odd valuation of its discriminant. The normalizer is the explicitly described multiplication/field-conjugation group.

The norm-minus-one obstruction includes nonintegral coordinates. After extracting the common minimum valuation m, the integral norm has valuation 0 and residue 1 when the sum of the two unit-normalized coordinates is nonzero modulo 3; otherwise it has valuation exactly 1. Hence the full norm has valuation 2m or 2m+1. Norm -1 forces the first case with m=0 and then has the wrong residue. This proves the obstruction. Finite multiplication maps have determinant 1, and finite semilinear maps have norm 1 and determinant -1. Therefore the three-adic multiplier is exactly the centralizing/inverting character on the normal C3.

## Abstract types and multipliers

In the kernel-C3 case, complements 1, C2, and C4 give the listed cyclic, symmetric, and dicyclic possibilities. For V4 and D8 complements, D.50's global sign character and the proved three-adic determinant character force the indicated inversion action. The explicit generators `az` and `ar` and their displayed powers identify these semidirect products with D12 and D24. No general extension classification is being substituted for the given maps.

Conjugation invariance of the multiplier kills the multiplier of a normal C3 that is inverted. D.43 then makes each reflection's negative three-adic coordinate a global negative sign; products give global positive rotations. The Dic12 and C12 restrictions on order-four generators use the exact D.50 square-one restriction and the three-adic character. The proof does not assert global multipliers for arbitrary cyclic C3 or C4 subgroups.

## Realizations and finite certificate

The D.50 maps realize 1, C2, C4, V4, and D8. The two displayed integral matrices act on the actual torus, fix the removed origin, and give twelve distinct homology matrices satisfying the dihedral relations. Their full profinite outer action is injective because those homology matrices remain distinct. Its four specified subgroups give C3, C6, S3, and D12. This yields exactly nine realized types. C12, Dic12, and D24 remain explicitly unresolved as occurrences, so the allowed list does not silently become an existence or conjugacy classification.

The executed certificate passed all 121 norm-matrix identities, 72 three-adic residue cases, all eight D8 automorphisms, the twelve integral torus matrices, 144 multiplication pairs for the V4 extension, 576 pairs for the D8 extension, 144 pairs for C12, and the dicyclic presentation and unique involution check. These verify the displayed finite maps; the proof's valuation and kernel arguments supply the unbounded assertions.

No mathematical correction is required.
