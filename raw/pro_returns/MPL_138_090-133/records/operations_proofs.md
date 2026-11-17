# Bounded proofs and counterexamples for the operations notes

Author: GPT-6 Astra Pro, root of run MPL_138_090-133; reasoning-effort setting is not exposed.
Written after the transcription freeze. No result here changes a reading.
These are independently written checks, not claims of novelty.

## P1. Pulling back a cellular graph

Let B={0,1,∞}, let A be a finite connected graph embedded in the sphere,
and suppose each component D of its complement is an open disc containing
at most one member of B. For every finite branched cover f:X→S² with branch
values in B, each component of f⁻¹(D) is an open disc. Indeed, if D has no
branch value, its connected finite unramified covers are trivial; if D has
one branch value, remove it, use the cyclic monodromy classification of
connected finite covers of a punctured disc, and fill the unique puncture.
This gives precisely a disc with local model w↦w^e. Thus f⁻¹(A) is cellular.
For connected X its graph is connected: attaching discs to disjoint graph
components cannot join them. The branch points on A cause no difficulty
for finiteness of the lifted graph, by the same local model.

Conversely, in a category containing the reference sphere and all double
covers branched over a pair from B, universality forces A to be cellular and
prevents a face from containing two points of B. A double cover branched at
those two points restricts over that face to an annulus, not a disc: its
Euler characteristic is 2−2=0 and it has two boundary ends. Such double
covers have index at most 2 above 1 and are allowed in the folded-edge
cartographic setting of scan98. This converse has not been asserted here
for a narrower category that requires every point over1 to have index2.

This is a corrected *mathematical formulation*, not a new transcription of
the damaged clause on scan125. Independently of the precise category,
A=[0,1] refutes the context's criterion “A contains at most one of B”:
its inverse image is the very graph defining each original map, although
A contains both0 and1. The corrected condition concerns complementary
faces. Michel Hua's project's §15 and RESULTS_STATE entry
138-operations-subset-criterion are the explicit comparison targets.

## P2. Composition and the exceptional endpoint

For local finite holomorphic maps, write f(w)−y=w^e times a unit and
φ(t)−φ(y)=(t−y)^d times a unit; substitution gives
e_(φ∘f)(w)=e_f(w)e_φ(f(w)). This proves the local multiplicativity used below.
If f and φ have branch values in B and φ(B)⊆B, their composite has branch
values in B. Its graph over [0,1] is tautologically f⁻¹(φ⁻¹([0,1])).

For the strict convention e_f=2 at every point above1, a sufficient
condition for φ∘f to be strict again is:

- φ(0),φ(∞) belong to {0,∞};
- if φ(1)=1, then e_φ(1)=1;
- at each other point of φ⁻¹(1), the index is exactly2.

Then a point of X above such an “other” point is unramified for f, and a
point above1 has e_f=2 and e_φ=1. This isolates the endpoint exception:
if A has a leaf at the reference point1, the inverse image under the
local square map consists of two rays, so the lifted point has valency2
and may be regarded as the midpoint of an edge. The identity φ is the
simplest example, within the folded-edge reference sphere. This supplies
a local answer to scan128; it does not reconstruct all the global
equivalences proposed on scan132.

The inequality e_φ≤2 alone does not imply the strict conclusion at other
points of φ⁻¹(1). An unramified such point would leave index1 in the
composite. Scan132 may implicitly rule these out through its requirement
that the graph have an optional rounded endpoint only at1; the manuscript
does not spell out that equivalence. We retain that as a scope question.

## P3. The two quadratic constructions must be distinguished

For m_c(z)=z/(cz+1−c), nonconstancy requires c≠1. Matrix multiplication or
direct substitution gives m_c²=id exactly when c(c−2)=0, in characteristic0.
Thus c=0 gives the identity and c=2 the nonidentity involution.
The uncertainty in the second denominator on scan127 line77 is untouched.

For q(t)=(2t−1)², q−1=4t(t−1), so q maps B into B and is branched only
over B. It always sends a Belyi map to a Belyi map, but need not preserve
the cartographic restriction at1: for f=z³, q∘f−1=4z³(z³−1), giving index3
above1 atz=0. Thus the local nonramification condition sketched on scan127
cannot be omitted. The “cleaning” polynomial 4t(1−t)=1−q(t) instead has
its critical point over1; for any Belyi map h, 4h(1−h) has index2 at all
points over1, since h is unramified above1/2.

## P4. Explicit holomorphic oranges, for every n≥1

Set

\[
F_n(z)=\frac{4z^n}{(1+z^n)^2}.
\]

Its degree is2n, and the fibres over0,1,∞ have multiplicities
(n,n), (2 repeated n times), (2 repeated n times), respectively:
F_n−1=−(z^n−1)²/(1+z^n)² and
F_n'=4nz^(n−1)(1−z^n)/(1+z^n)³.
For 0<s<1 the two solutions of 4t/(1+t)²=s are positive real.
Consequently F_n⁻¹([0,1]) is the union of the n rays z^n≥0, including
their common endpoints0 and∞. This is the meridian orange with n edges.

For every a>0, h_a(z)=az preserves each ray and each complementary sector.
The path h_(a^u),0≤u≤1, is an isotopy through automorphisms of that map.
For a≠1, F_n∘h_a≠F_n, so these give distinct functions realizing the same
embedded holomorphic map. The statement on scan131 that n≥2 eliminates
nonidentity holomorphic automorphisms is therefore false, and the list
I,II,III is incomplete. This counterexample was already identified in
Michel Hua's project, §15, “Cartes holomorphes”; the explicit F_n family
and local indices here verify that the examples satisfy the strict
definition on scan129, rather than merely being abstract embedded graphs.

The face centres are the n roots of z^n=−1 and the edge midpoints are the
n roots of z^n=1. Fixing either set along this identity component forces
a=1 (their absolute values are1). For caseI, with the real equator and
the sole vertex∞, the connected group is z↦az+b (a>0,b∈R);
normalizing a chosen edge midpoint to0 and fixing it kills b but leaves a. Fixing both face
centres and∞ kills the whole group by the three-fixed-points property of
Möbius transformations. For III, normalized as the ray from0 to∞, the
connected group is a>0 scaling and is one-dimensional, not Aff(1,C).

## P5. One face of order at least3 is a sufficient finite-case repair

Assume a finite connected holomorphic map in the strict sense of scan129.
An automorphism isotopic to the identity through map automorphisms fixes
each incidence and hence each corner as a boundary prime end of every
face. A face is conformally a disc; its finite analytic boundary arcs
give the usual prime-end compactification. If it has at least three
corners, its conformal automorphism fixes three distinct boundary prime
ends and is the identity, because a nonidentity disc Möbius automorphism
cannot fix three boundary points. The identity theorem then makes the
automorphism the identity on the connected surface.

“Order” counts boundary occurrences, so repeated underlying vertices must
not be conflated with repeated prime ends. The proof uses the finite
analytic boundary structure furnished by a finite Belyi map. No claim
about infinite maps or arbitrary wild embeddings is made. This verifies
the finite sufficient condition proposed, with an expressed reservation,
on scan130; it does not verify the subsequent classification of exceptions.

Indeed, that classification misses a different configuration with no face
of order≥3. The rational function

\[
R(z)=\frac{z^4}{4(z^2-1)}
\]

has passport (4)|(2,2)|(2,1,1), since
R−1=(z²−2)²/[4(z²−1)] and
R'=z³(z²−2)/[2(z²−1)²]. Its ordinary embedded map has one vertex, two
loop edges and three faces, all of order1 or2. It is neither I nor an
orange, so the “condition ... signifie” classification in scans130–131
is not equivalent to the face-order condition. This does not give an
additional continuous automorphism family and is not a counterexample
to the sufficient rigidity condition just proved.

## P6. Finite order versus an infinite isotopy kernel

The finite-order disc step on scan126 is precisely the conclusion of
Constantin–Kolev, Proposition3.2: a periodic homeomorphism of a closed
disc fixing its boundary pointwise is the identity. The reduction to
the boundary uses the elementary fact that an increasing periodic
homeomorphism of an interval is the identity. We checked the stated
proposition and its proof's invariant-arc step, but did not re-prove the
paper's preceding plane-topology lemma2.4.

Once “isotopic to identity as an automorphism of the map” fixes every
incidence, cut along the edges and apply the disc statement to each
face. Thus a finite kernel in scan126(b) is trivial, proving the intended
b⇒a under the finite cellular hypotheses. The full existence of invariant
rigidifications and the contractibility of their space remain unverified
here. In particular, finiteness cannot simply be dropped: the subgroup
h_(2^m),m∈Z, of P4 acts faithfully and lies wholly in the isotopy kernel.
This is a map-preserving action on a sphere, not the centralizer π1
comparison on admissible hyperbolic surfaces in RESULTS_STATE LM4 C.12.

Primary source: A. Constantin and B. Kolev, “The theorem of Kerékjártó on
periodic homeomorphisms of the disc and the sphere,” L'Enseignement
Mathématique40 (1994),193–204, Proposition3.2; author version
https://arxiv.org/pdf/math/0303256 (pp.3–4).

## P7. Field of definition and commutation

For a fixed algebraic sphere map φ and a Belyi map f,
σ(φ∘f)=(σφ)∘(σf). Thus φ defined overQ supplies commutation with every
σ∈Gal(Qbar/Q); definition overK gives it for Gal(Qbar/K).
This is the extra arithmetic hypothesis in Wood's definition of a
Belyi-extending map, §3.1 and Proposition2. Branch-point conditions alone
only prove that composition remains a Belyi map, not that the operation
commutes with the full Galois action.

The sextic family from scans107–112 supplies an explicit test. Let f_c
have the normalization checked in arithmetic_certificate.py and let
c run through the three roots of 25c³−12c²−24c−16. The clean maps
β_c=4f_c(1−f_c) still send0,1,∞ into {0,∞}. If β_c and β_d were isomorphic,
the identity
4u(1−u)−4v(1−v)=−4(u−v)(u+v−1)
would force f_d∘h=f_c or f_d∘h=1−f_c for a source Möbius map h.
The second case is excluded by the different passports over0 and1.
In the first, the unique pole∞ and the unique zeros of orders3 and2
force h to fix∞,0,1, so h=id and c=d. These clean maps are therefore
permuted nontrivially by Galois. In the folded-edge reference category,
evaluate the operation defined by β_c on the reference identity cover:
its nontrivial conjugation proves that this fixed operation is not
Galois-equivariant. This example depends on the independently certified
sextic normalization; it is a check for this run, not a novelty claim.

## P8. Orbit separation has a limited meaning

If Ω is a Galois-equivariant operation and I is any Galois-invariant
function on dessins, then I∘Ω is Galois-invariant by direct substitution.
Different values can prove that two dessins lie in different orbits.
No such invariant can separate members *within* one orbit. In particular,
the three sextic dessins above are a single orbit, so invariant refinements
cannot distinguish them as different Galois orbits.
Nothing here proves that all spherical operations, even the rational
ones, give a complete system of invariants or reconstruct the full
arithmetic image in EXIT_TOWER E.24.
