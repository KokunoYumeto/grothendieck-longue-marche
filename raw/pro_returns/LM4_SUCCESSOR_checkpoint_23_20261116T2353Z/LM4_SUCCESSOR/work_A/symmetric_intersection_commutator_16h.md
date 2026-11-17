# The actual symmetric filling intersection and its completion

Research proof, 16th hour. The discrete intersection calculation and the
finite-extension argument below concern the actual symmetric deletion.
They do not make a nonabelian involution cocycle a coboundary and do not
identify the projected fixed subgroup with the source image.

## 1. Actual spaces and maps

Use the notation of
`work_DE/next_marginal_source/symmetric_deletion_fixed_lifting.md`.
Thus X=Y_b, A consists of the eight divisors v=u or w=u with
u in mu_5 minus {1}, Bdiv=F(A), Y=X minus A, V=F(Y)=X minus Bdiv,
and Z=Y intersect V. All fundamental groups use the literal source
basepoint (399/200,1/200). Put P=pi_1(Z), G_1=pi_1(Y),
G_2=pi_1(V), Q=pi_1(X). The actual filling homomorphisms are onto.
Let N_A=ker(P->G_2) and N_B=ker(P->G_1). They are the normal
closures of the indicated actual meridians.

The product coordinate q=vw makes X and Y actual bundles over
B=C* minus mu_5, with fibers respectively a six-punctured sphere
and a fourteen-punctured sphere. The same holds for V by F.
Consequently X,Y,V are aspherical; Q is F_5 semidirect F_6, and
G_1,G_2 are F_13 semidirect F_6. These are group splittings obtained
by lifting free base generators, not assertions of geometric sections.

The mixed divisor intersection A intersect Bdiv is finite. For example,
for u,t in mu_5 minus {1}, its two component types have

    v=u, w=(u+t-ut)/u,
    v=u, w=t/(u+t-1).

The other types follow by interchanging v and w. No component is shared.
The exact algebraic geometry certificate in the DE directory verifies
that all 64 points lie in X and are transverse. For the argument below,
only finiteness is required. Thus

    Y union V = X minus (A intersect Bdiv).

## 2. Discrete intersection equals mutual commutator

Removing finitely many points from a smooth real four-manifold induces
an isomorphism on pi_2. Indeed, maps of S^2 and homotopies or nullhomotopies
of dimension at most three can be approximated relative to their boundary
by maps transverse to every removed point; the dimension inequality makes
every inverse image empty. Since pi_2(X)=0,

    pi_2(Y union V)=0.

The actual open cover Y,V is a homotopy pushout of Z->Y and Z->V.
All spaces are connected, and both maps on pi_1 are onto: a loop can
be perturbed off a complex divisor, and a meridian is killed by filling
that divisor. The homotopy fibers of the two maps are therefore connected.
As pi_2(Y)=pi_2(V)=0, their homotopy exact sequences give the surjections
pi_2(hofib)->pi_2(Z) required in Brown--Loday Lemma 4.1. The same exact
sequences identify pi_1(hofib) injectively with N_B and N_A.

That lemma therefore gives, for these actual maps,

    pi_2(Y union V) = (N_A intersect N_B)/[N_A,N_B].

The crossed-module product in the lemma becomes the ordinary mutual
commutator when the crossed modules are inclusions of normal subgroups.
This is also explicit in Brown (1984), Propositions 2.5 and 2.8.
We conclude

    N_A intersect N_B = [N_A,N_B].                         (1)

No asphericity of Z is used. Ordinary van Kampen also gives
Q=P/(N_A N_B). Thus the standard actual fiber-product surjection becomes

    P/[N_A,N_B] = G_1 x_Q G_2.                            (2)

It is the quotient by the mutual commutator that is identified here;
the comparison from P itself is not asserted to be injective.

## 3. Finite-kernel extensions of a finitely generated free-by-free group

Lemma. Let Q have an exact sequence

    1 -> F_m -> Q -> F_n -> 1

with m,n finite. Every extension 1->D->E->Q->1 with D finite has a
finite-index subgroup of E meeting D trivially. In particular some finite
quotient of E is injective on D. Every finite-index subgroup of Q has the
same property.

Proof. The quotient F_n is free, so Q=F_m semidirect F_n. First let D=A
be central. Choose homomorphic lifts i:F_m->E and j:F_n->E, using the
freeness of the two factors. For b in F_n, conjugation by j(b) and the
lift i of the prescribed action differ by a homomorphism d_b:F_m->A:

    j(b)i(x)j(b)^(-1)=i(b.x)d_b(x).

Centrality of A makes d_b a homomorphism. Let e be the exponent of A and
put K=[F_m,F_m] F_m^e. This is characteristic and finite-index in F_m,
and every homomorphism F_m->A vanishes on K. Thus j(F_n) normalizes i(K).
The subgroup i(K)j(F_n) projects isomorphically onto K semidirect F_n.
It has finite index in E and meets A trivially. Its core in E is a
finite-index normal subgroup meeting A trivially.

For arbitrary finite D, the centralizer C_E(D) has finite index in E.
Its kernel over its image Q_0 in Q is Z(D), and that kernel is central.
The group Q_0 has finite index in Q. Its intersection with F_m is a
finite-index finitely generated free group, and its image in F_n is
also finite-index free. The resulting free-by-free exact sequence
splits. Apply the central case to C_E(D)->Q_0, then take the core in E.
This also proves the assertion for every finite-index subgroup of Q.
No goodness or profinite homotopy-excision theorem is required.

## 4. The full topology on the actual fiber product

Lemma. Suppose every finite-kernel extension of Q separates its kernel
in a finite quotient. Let G_1->Q and G_2->Q be epimorphisms, and let
D=G_1 x_Q G_2. Then the full profinite topology on D is induced by the
product of the full profinite topologies on G_1 and G_2. Consequently

    hat D = hat G_1 x_(hat Q) hat G_2.                    (3)

Proof. Write R_i=ker(G_i->Q), embedded as a coordinate subgroup of D.
Let K be any finite-index normal subgroup of D. Projection D->G_i is
onto, so K intersect R_i is normal in G_i. The extension

    1 -> R_i/(K intersect R_i)
      -> G_i/(K intersect R_i) -> Q -> 1

has finite kernel. Choose a finite-index normal subgroup A_i of G_i
such that A_i intersect R_i is contained in K intersect R_i. (The
construction may be chosen to give equality.) Let
D_0=D intersect (A_1 x A_2), and let Q_0 be its image in Q. Both are
finite-index. The kernel of D_0->Q_0 is

    (A_1 intersect R_1) x (A_2 intersect R_2),

which is contained in K. Therefore the finite homomorphism D_0->D/K
factors through Q_0. Its kernel is a finite-index subgroup Q_1 of Q_0.
Taking the core of Q_1 in Q gives Q_2 normal of finite index. Now

    D intersect ((A_1 intersect preimage(Q_2))
                  x (A_2 intersect preimage(Q_2)))

is contained in K. This proves the claimed induced full topology.

For completeness the closure of D in the completed product is exactly
the displayed compact fiber product. If an open rectangular neighborhood
of a compatible pair is represented by cosets g_i A_i with A_i normal
finite-index, compatibility in hat Q says that the two cosets
q_i(g_i)q_i(A_i) meet in hat Q. The subgroups q_i(A_i) have finite index
in Q; the same cosets therefore already meet in Q, as can be checked
in the finite quotient by their intersection. Adjusting g_i within A_i
gives an actual pair in D in that neighborhood. The induced-topology
assertion now identifies hat D with this closure, proving (3).

## 5. Actual compact intersection calculation

Apply the previous lemmas to the actual Q=F_5 semidirect F_6 and (2).
Let mathcal N_A and mathcal N_B be the closed actual filling kernels
in hat P. They are the closures of N_A and N_B: completion of a
surjective quotient has exactly the closed normal closure of its kernel.
The closure of the discrete mutual commutator equals the closed mutual
commutator of those closures, by density and continuity of commutation.
Thus (2) and (3) identify the actual maps as

    hat P / closure([N_A,N_B])
        = hat(G_1 x_Q G_2)
        = hat G_1 x_(hat Q) hat G_2.

The kernel of the last actual comparison from hat P is also
mathcal N_A intersect mathcal N_B. Consequently

    mathcal N_A intersect mathcal N_B
        = [mathcal N_A,mathcal N_B]_closed
        = closure(N_A intersect N_B).                    (4)

This proves the completion/intersection comparison in this actual
example. It is derived from finite extensions of the actual filled
free-by-free group, not from an interchange of arbitrary intersections
and closures.

## 6. What remains for fixed lifting

F exchanges the two kernels and hence preserves their common mutual
commutator. The actual quotient in (2), and its completed counterpart,
carry the coordinate-swap involution after identifying G_2 with G_1 by F.
For a fixed target d and a lift x, the element x^(-1)F(x) is still a
nonabelian C_2 cocycle with values in the group in (1) or (4). A fixed
lift exists precisely when its class is neutral. Neither (1) nor (4)
proves that neutrality. In particular these results do not identify
the projected fixed subgroup in G_1 with the actual source image and
do not prove the original source-kernel equality. The local fixed-node
commuting relations provide particular neutral classes, as in the DE
note, but arbitrary ambient conjugates remain a separate issue.

## Primary sources actually opened and checked

Brown, R., & Loday, J.-L. (1987). Van Kampen theorems for diagrams of
spaces. Topology, 26(3), 311--335. Primary author PDF:
https://groupoids.org.uk/pdffiles/RB-Loday1.pdf . Verified: Lemma 4.1
and its proof, printed p. 320, including its weaker hypothesis (b);
Theorem 3.1 and Corollary 3.4 checked for context. Retrieval references
turn826view0, turn827view0.

Brown, R. (1984). Coproducts of crossed P-modules: Applications to second
homotopy groups and to the homology of groups. Topology, 23(3), 337--345.
https://doi.org/10.1016/0040-9383(84)90016-8 . Verified author PDF:
https://www.groupoids.org.uk/pdffiles/coproducts-Topology.pdf .
Propositions 2.5 and 2.8, Theorem 3.1, Corollary 3.2 and their proofs
were opened and read. Retrieval references turn828view0, turn829view0.
The completion argument above is proved here directly and is not
attributed to either discrete homotopy source.
