# C31: a smaller proved homology annihilator

Status: exact structural calculation completed; the C31 target remains OPEN.
No new modular solution or full lift is asserted in this note.

Let G be finite and let A be a normal finite abelian subgroup of exponent r,
with quotient Q. The integral homology Hochschild--Serre spectral sequence
has, in total degree two, subquotients of

H2(Q,Z), H1(Q,A), and H0(Q,H2(A,Z))=H0(Q,wedge²A).

Both of the latter groups are annihilated by r: their chain modules and the
exterior-square module are annihilated by r. If e annihilates H2(Q,Z), the
three-step filtration therefore shows that r²e annihilates H2(G,Z). No
splitting of the group extension or of the homology filtration is used.
Inducting through the derived series shows that

M = product_i exponent(G^(i)/G^(i+1))²

annihilates H2(G,Z). The square on the abelian base factor is unnecessary but
is a valid harmless upper bound. DE independently checked this argument,
including the exact integral spectral-sequence terms.

The actual176-generator finite source group used by the original C31
centralization has order2^146*3^30. The executed GAP calculation
`code/pbc_derived_h2_bound.g` reconstructs the same original pc group,
computes its actual derived series and abelian invariants, verifies the
subgroup normalities and generator power containments, and retains the
derived generators in the original pc coordinates. Its completed output
`code/pbc_derived_h2_bound.out` contains the success marker. The factor
exponents are

[6,3,4,6,4,3,2],

so the proved homology bound is

M=107495424=2^14*3^8.

The complete group orders, invariants, factor exponents, and original-coordinate
generators are in `code/pbc_derived_h2_bound.json`. Provenance is
`code/pbc_derived_h2_bound_provenance.json`, bound to the original source hash
95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88.

For K=R/[F_n,R], Hopf identifies tors(K)=H2(G,Z). Since K is finitely
generated abelian, K is abstractly free plus its finite torsion subgroup.
If M kills that torsion subgroup, tors(K) intersects M K trivially. Hence
the original target plus a sum of genuine centralizer commutators, all of
which lie in tors(K), vanishes integrally whenever it vanishes modulo M in
the ORIGINAL presentation. This is the same already audited positive gate
as the |G|-modulus argument, with a smaller proved annihilator. Power-word
corrections s² and r³ remain forbidden.

The new bound reduces coefficient size from194 to27 bits. The input and
independent external-memory DAG verifier have now been adapted to this
explicit modulus, retaining the existing original diagonal-power proofs.
The verifier was independently validated against the previously fully
replayed small known certificate: every mathematical output field agrees.
The actual new native-v6 search is running; its bounded-integer arithmetic
was compared byte for byte with the entire501,122,419-byte trace of the
original GMP run on this same source. All11,735,720 records agree exactly.
This is arithmetic validation, not a C31 lifting certificate.

At20:30 UTC the active search had processed19,000 genuine source rows;
the target remainder still had2,297 nonzero coordinates. The completed
power and exterior phases and the ongoing triple phase do not establish
nonlifting: the algorithm intentionally omits source rows exceeding its
fixed collection budget, and only a positive exact witness is accepted.
Any success still requires exact expansion and replay of all used ORIGINAL
source rows before a full lifting claim. The old large-modulus version5
basis and the small-modulus GMP basis are both paused intact; neither has
been discarded or reinterpreted as a failed lift. Their complete proof
records remain preserved through independently verified lossless encodings.
