# Independent PBC audit of D.65

Auditor: /root/pbc_groups. Completed 2026-11-15, approximately 17:44 UTC.
Draft: notes/de_alexander_kernel_type_draft.tex.
Outcome: **PASS**. No mathematical correction required.

## Completeness and the two topologies

The uniform five-adic topology on the product P is deliberately
stronger than the original m-adic null-family/cohomology topology.
Z5[[u,v]] and its product P are complete for this uniform topology.
The proof that C is closed is valid: an approximation modulo 5^nP
also approximates modulo m^n, and one fixed null family suffices
to check the required finite exceptional set for that n.

The coordinate operators are Z5-linear, with a common bound
preserving 5^n. Thus H is closed and complete.
The formula ord_m(5^n z)=n+ord_m(z) is exact for this formal power
series ring. It proves five-saturation of C; applying it after
the coordinate operator proves saturation of H.
Consequently the induced topology on H is its intrinsic
five-adic topology, and the quotient neighborhoods on H/C
are exactly its intrinsic subgroups 5^n(H/C).

Closedness gives separation. For completeness, the successive
representative adjustment by C is legitimate at every stage,
and yields differences in 5^nH. The representatives converge
in H to a lift of the entire compatible quotient system.
There is no assumption that the original cohomology topology
is Hausdorff or that a general quotient of a complete module
is automatically complete.

## Residual dimension and complete-free classification

D.48's Chebotarev primes make D_q(1) arbitrarily m-adically
small, so arbitrary constant coefficient sequences give
elements of H. If such an element equals 5b+c with b in H
and c in C, evaluation at u=v=0 makes its residues modulo5
finitely supported. This is precisely the kernel condition
for reduction of product Z5 modulo c0. Thus the induced
F5^N/F5^(N) map remains injective modulo5.

The latter vector space has dimension continuum, while P
has cardinality continuum, proving the exact dimension.
The digit-lifting construction from a basis of M/5M is
valid for a complete separated torsion-free Z5-module:
each successive digit has finite support, so the final
coefficient family tends to zero five-adically.
The minimum-valuation argument proves uniqueness.
The resulting isomorphism preserves every intrinsic 5^n
subgroup, so the claimed homeomorphism in that topology
also follows.

## Abstract splitting of the compact term

The quotient R_s is torsion-free, hence L_s is a pure
submodule of J_s: if 5^n j belongs to L_s, then j belongs
to L_s. Over the DVR Z5, Smith normal form reduces any
finite system of linear equations to power-of-five
divisibilities and zero equations. Every finite system
defining a retraction is solvable in J_s, and purity makes
it solvable in L_s. Its solution sets are closed in the
compact product of copies of L_s.
The finite-intersection property supplies an abstract
Z5-linear retraction. No continuity in the nonseparated
cohomology topology is deduced or needed.

The final specializations also check: D.44 and D.64
have zero compact retained term for the reasons stated;
D.1 concerns the Tate weights 3,4,5, so every scalar
q^(j−1)−1 used there is nonzero and injective on Z5.
All assertions remain confined to finite ramification.

This audit uses the self-contained module proof and the
already independently audited D.48/D.63/D.64 constructions;
it introduces no new external theorem or computation.
