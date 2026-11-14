# Independent audit of D.67

**Result: PASS.** I read the entire proof, metadata, and exact producer, checked the invoked conclusions of D.54–D.56 and D.64–D.65, and independently reran the certificate. No correction is required.

Editorial cross-reference recorded after the mathematical audit: root identified A.13 as the location of the discrete Out(F2) = GL2(Z) identification, and part C is changing the earlier A.12 reference accordingly. This does not alter any map or proof step.

## Specified automorphisms and peripheral maps

The composition convention in the code is the one used in the proof. The displayed identities are actual identities on the two free generators, including all inner corrections between the elementary reflection B and the cusp-normalized alpha0. The commutator images of R and B are the stated conjugates of c and c inverse. Consequently their continuous extensions define actual elements of the full peripheral outer group.

The eight signed permutation automorphisms satisfy the precise dihedral multiplication law. Their eight distinct integral homology matrices prove that passage to outer automorphisms does not identify any of them. Thus the specified group has order eight. The discrete torus identification supplies the asserted geometric realization with these actual outer labels; the proof does not infer geometric realization solely from a profinite homology matrix.

The words give b1 = r b0, delta = r squared, and the outer class of zeta0 = delta b0. Combined with the already proved full standard centralizers, these identify both V0 and V1 and their intersection exactly.

## Full normalizers and the centralizer of D

Each Vj has exactly one nonidentity multiplier-one element, namely delta. Conjugation preserves the multiplier and therefore fixes delta. Its action on the other two nonidentity elements has image of order at most two. The kernel is exactly Vj: Vj is abelian, and its ambient centralizer is contained in the computed ambient centralizer of bj, which is Vj. This establishes the full bound of eight elements on each normalizer. The specified D realizes all eight and normalizes both groups, proving the claimed equalities.

The mod-two homology kernel on this actual D is exactly V0. An arbitrary ambient normalizer of D preserves this kernel because the actual homology representation conjugates matrices and preserves the identity matrix. It therefore belongs to the already computed normalizer of V0. This proves full self-normalization of D. Its ambient centralizer consequently lies in D and is its ordinary order-two center. No ambient finiteness or faithfulness is assumed in this step.

## Complete finite-overgroup list for the specified b0

The proof uses the exhaustive nine abstract types from D.55. The cyclic-four involution is positive by D.55, and the cyclic-six involution is positive by D.56, so neither can be the specified negative b0.

In S3, every involution inverts the normal cubic subgroup. In the order-twelve dihedral group, the central involution is positive because it is the involution in a cyclic-six subgroup; every negative involution is therefore a reflection and also inverts the normal cubic subgroup. D.54 gives an order-three mod-two matrix for every cubic element. Since b0 has identity mod-two matrix, either inversion relation would identify this cubic matrix with its inverse, which is impossible. This is an exact representation obstruction at the specified b0 and does not assume that all negative involutions have its reduction.

Any Klein-four overgroup is contained in the full centralizer V0 and hence equals it. In any order-eight dihedral overgroup, the central involution is the square of a quartic element and hence positive. It commutes with b0, so it is exactly delta, the unique positive nonidentity element of V0. Therefore V0 is an index-two normal subgroup of that overgroup, forcing the overgroup into its computed full normalizer D. Equality follows from orders.

The final conjugation statement is the explicit bijection on overgroups induced by the specified ambient conjugator. It makes no assertion that the two known involution orbits exhaust all negative involutions.

## Executed verification

I executed the producer source with its output redirected to the part-a audit directory, leaving part-c source and registered outputs unchanged. The independent rerun passed:

- 156 exact free-generator equalities;
- 64 free-word multiplication pairs;
- 64 integral homology multiplication pairs;
- 12 mod-two conjugation pairs;
- 6 cubic inversion pairs.

Captured stdout: `work/part_a/d67_audit_stdout.txt`.
Independent result: `work/part_a/standard_negative_overgroups_d67_output.json`.

The finite certificate checks the stated word maps and finite matrix comparisons. The full normalizer and overgroup upper bounds are established by the proof using the earlier full centralizer and finite-type theorems, with the distinction made explicitly in both text and metadata.
