# Root full audit of A.77: commutator subgroup of order at most two

**PASS.** Root read the entire candidate and certificate source, checked
the actual quotient/Jacobian comparisons, freshly reopened the required
good-reduction statement, and independently reran the complete finite
certificate with byte-identical JSON. DE's complete independent audit
and replay also pass. This approves canonical integration after the
already completed checkpoint15 save.

## The finite-group reduction has the needed exact scope

The actual geometric cover gives two generators. A commutator subgroup
of order two is central because it has trivial automorphism group.
Thus the finite closure is nilpotent of class two; its odd Sylow factors
are abelian, and projection of the actual two generators generates the
two-group factor. This reduction uses the actual closure group and does
not assume that an arbitrary group with a small derived subgroup is
cyclic by a small subgroup without proof.

Take an irreducible representation of that two-group over the same
auxiliary-adic splitting field used later in Tate homology. Its kernel
defines an actual quotient with faithful irreducible representation.
An abelian such quotient is cyclic. In the nonabelian case its centre
is cyclic by Schur's lemma and faithfulness. Every square is central,
so the quotient by the centre is C2 squared: rank at most two comes
from the actual generators, and rank at most one would make the group
abelian.

The exact collected word u^a v^b sigma^d is central precisely when
both exponents a,b are even. It follows that the centre is generated
by u squared, v squared and sigma. If the cyclic centre has order at
least four, sigma is a square in it. Consequently one of the other
two generators must have primitive square in that centre, supplying
a cyclic subgroup of index two. With centre of order two, either
one generator already has order four or the product of the two
involutions does. These are all cases. The original centre need not
be cyclic; only the faithful irreducible quotient has that property.
A.76's separately audited classification then applies to each quotient.

## The Jacobian maps are actual and only surjectivity is claimed

For each of these finitely many distinct normal kernels N, the proof
forms the actual quotient q_N:C to C/N of the given curve. The target
cover has the precise group just analyzed. The audited cyclic-index-two
families, or the elliptic isogeny case, give potential good Jacobian
reduction and special two-rank zero for every target.

The sum of their Picard pullbacks is a homomorphism from the product
of those Jacobians to J_C. On divisors, the pullback of the image of
a point counts its orbit with its stabilizer multiplicities. This
proves q_N^*q_N* equals the sum over N, including ramification, and
the reverse norm-pullback composite equals the degree. On rational
Tate homology the image of pullback is therefore exactly the
N-invariant subspace.

After extending the auxiliary-adic coefficient field, Maschke
semisimplicity shows that every irreducible summand belongs to the
invariants of its own kernel, one of the chosen N's. The sum of
these actual pullback images spans all rational Tate homology.
Scalar descent preserves this spanning property. Hence the abelian
image has full dimension and the sum map is surjective.

The product usually has excess dimension. The proof correctly does
not call that whole product isogenous to J_C. Complete reducibility
instead gives J_C as an isogeny factor, while the actual surjection
already transfers good reduction. After a common extension and
good reduction, isogeny invariance and additivity of special two-rank
transfer rank zero. There is no inference from an abstract character
table to an unconstructed geometric map.

## Cusp data, all intermediates and the odd factors

For the nonabelian two-group source the actual handle commutator
generates its central derived group, so cusp inertia is exactly that
order-two subgroup. Riemann--Hurwitz gives genus1+|G|/4 and cusp
count|G|/2. Its quotient by inertia is an actual unramified elliptic
isogeny with kernel G/G'. If that kernel has exponent e, its point
differences are killed by e; actual degree-two pullback kills the
source cusp differences by2e.

Every proper intermediate has at least two cusps: inertia lies in
every maximal subgroup of the finite two-group and hence in its
Frattini subgroup. Norms transfer good reduction, special rank zero
and the actual principal cusp divisors. Point pushforward has
coefficient one after the specified algebraic base extension, so
ramification does not invalidate the torsion bound. The intermediate
genus is positive because it maps nonconstantly to E.

These are precisely the geometric inputs of A.41, A.42 and A.59,
including the rational endpoint components and all coefficient primes.
The original elliptic base is treated separately. For odd abelian
factors, the proof repeats the actual connected coprime isogeny
pullback: extension of the Abel map through nodes, finite etale odd
isogeny, separate nilpotent theorem for the tree, and literal copies
of each rational joining subtree. It does not claim that the whole
odd pullback has special rank zero. Packets, finite-field restriction
and inner path ambiguities retain the proved earlier scopes.

## The illustration and executed support

The order32 group has the given explicit normal forms and associative
multiplication, exponent four, centre C2 cubed and derived group C2.
Thus it has no cyclic subgroup of index two. The four actual quotient
maps give three D8 quotients and one Q8 quotient. Their degree-two
characters and the sixteen linear characters satisfy the complete
orthogonality and degree-square accounting checked by the program.
This is supporting finite data, not the uniform representation proof.

The draft SHA-256 is
`7752d6addfa2162f0008ee82049a7a062420e4791b865ac6df809614a662e6e0`.
The executed source SHA-256 is
`c2b05f26e7b19bc767ad3903921e7ff63efa289fb51d2ded3b36e15fee704dda`.
The whole JSON SHA-256 is
`4909041203e23a0c9f82ffa7f9698a422ac84d1e97fdd691ddcf9f2f9f9fcdbb`.
The root runner and output comparison are retained under
`code/root_A77_certificate_rerun.py` and `notes/root_A77_certificate_*`.

## Primary source check and retrieval limits

The direct fresh Serre--Tate PDF opening returned no readable lines,
so it was not counted as a fresh statement read. Root then recovered
the exact indexed primary text by searching the PDF URL for the
theorem/corollary and reopening the earlier primary reference.
Serre--Tate, *Good reduction of abelian varieties*, Theorem1 and
Corollary2 on printed493, including the finite-index Tate-module
argument, were fully readable in `turn1208search4` and `turn1208view0`:
<https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf>.
The corollary applies to the actual surjection used here. Dupuy--Rabinoff
Theorem1.1/Proposition3.2 and Lehr--Matignon Theorem6.13 were freshly
read in the immediately preceding A.75/A.76 audits. No unverified
source or priority claim is introduced, and A.45 remains open.

## Exact undivided orthogonality addendum, 2026-11-16

The root-requested certificate refinement now asserts the undivided character dot products equal 32 times the Kronecker delta before division. The exact matrix is 32 times the 4-by-4 identity. The owner preserved the original candidate and canonical sources and outputs, and all prior mathematical output fields remain unchanged. Root preserved its prior audit and rerun files in `notes/root_A77_before_orthogonality_precision/`, reran the entire updated candidate, and obtained whole-JSON byte equality. The current source hash is `5d0d069078341dc3efd2be436df862db906c74e6ec29f710f191d90ded484b5f`; the result hash is `6ba7bc108f812fa229b1db404ec0a95e814cf80c00fe424bdc3772227d5262f8`. The canonical source/output hashes are recorded in `notes/fgh_A77_orthogonality_precision.json`. The theorem and its proof did not change. PASS.
