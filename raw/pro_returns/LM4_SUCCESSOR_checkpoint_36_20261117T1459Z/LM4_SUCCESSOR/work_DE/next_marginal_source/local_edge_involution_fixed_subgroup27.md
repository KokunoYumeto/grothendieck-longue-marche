# The exact local edge involution has trivial fixed subgroup

Research, checkpoint27. This concerns only the proper local amalgam Dloc
of `unfilled_edge_map_structure27.md`, Section5. Its map to the actual
quotient V_* need not be injective, and no assertion below is transferred
through that map.

Let E1=CLC be the actual B117 subgroup, K1=CKC its actual free-five
retract, and eta1=Ad(C) eta Ad(C). The local group Dloc is the amalgam of
two copies of E1 over K1, with the second edge marking eta1. Its literal
involution kappa exchanges the two factors and acts by eta1 on their
common edge. Then

    Dloc^kappa=1,                 (Dlochat)^kappa=1.                (1)

## 1. The folded group and its exact full topology

Folding the two vertex factors gives the exact presentation

    Ffold=Dloc semidirect <kappa>
         = E1 *_{K1} Q1,       Q1=K1 semidirect_eta1 C2(kappa).    (2)

This can be checked by eliminating the second copy of E1: its elements
are kappa E1 kappa, and the only common-edge identification is
kappa u kappa=eta1(u). Conversely the index-two kernel of the character
kappa->1, E1->0 in the right-hand presentation has precisely the two
E1 vertices and the eta1 edge marking. The two maps are inverse on all
named generators.

Both edge embeddings in (2) are injective and have full topology. The
following finite-target argument supplies proper full completion, rather
than assuming it merely from those separate edge topologies. Given finite
quotients of E1 and Q1, choose an eta1-invariant finite-index normal
subgroup L of K1 contained in both edge restriction kernels. For example,
intersect the first restriction with its eta1-image and the second
restriction; the latter is already eta1-invariant. Combine the E1 target
with the actual E1->K1 retraction followed by K1/L. Its exact edge kernel
is L. Combine the Q1 target with its canonical quotient
(K1/L) semidirect C2. Its exact edge kernel is also L.

The two finite vertex images now amalgamate over the same finite group
K1/L. Take sufficiently many copies of their faithful regular permutation
actions to use one finite set of common size. Each restriction to K1/L
is a free action with the same number of orbits. Identify the paired
orbits equivariantly. Both finite vertex groups then act faithfully on
that common finite set, agreeing on the edge. This is a finite quotient
of (2) refining both originally prescribed vertex kernels.

Thus the full completion is the proper profinite amalgam

    Ffoldhat=E1hat amalg_{K1hat} Q1hat.                            (3)

The universal property identifies this with the actual completion of
Ffold. Dloc has index two in Ffold, hence has full induced topology there,
and its completion is the kernel of the same parity character. No
assertion that Dloc embeds in V_* is used.

## 2. The actual edge reflection is a six-cone free product

The certified common-neck prefix basis P1,...,P5 satisfies
eta(Pi)=Pi^-1. Its C-conjugate is therefore a free basis of K1 inverted
by eta1. Write those five generators as q1,...,q5. Then

    Q1=<kappa,q1,...,q5 | kappa^2=1,
                              kappa qi kappa=qi^-1>.

With sigma0=kappa and sigma_i=kappa qi this is exactly the free product
of six cyclic groups of order two: each displayed relation is
sigma_i^2=1, and the inverse substitution is qi=sigma0 sigma_i. The same
inverse presentations and full-completion universal property give the
full free profinite product of six C2 groups. Its selected involution
centralizer is exactly <kappa>, discretely by reduced words and compactly
by the Herfort--Ribes full free-product centralizer theorem already used
with its primary proof in B122/B129.

## 3. Centralizer in the fold, and the exact limit

In the ordinary Bass--Serre tree of (2), kappa fixes the Q1 vertex. It
fixes no edge: every edge stabilizer is conjugate to the torsion-free free
group K1. The fixed subtree is connected, so that vertex is the only
fixed vertex. Every centralizing element preserves it. Consequently

    C_Ffold(kappa)=C_Q1(kappa)=<kappa>.

For (3), K1hat is a full free profinite group and has no element of order
two. Hence kappa again fixes no edge. Its fixed subgraph is nonempty
(the displayed Q1hat vertex) and connected by the original prime-order
fixed-profinite-tree theorem, Zalesskii--Mel'nikov (1989), Theorem2.8,
whose full proof was verified for B122. A connected profinite subgraph
without edges has only one vertex. The compact centralizer therefore
preserves Q1hat and is precisely <kappa> by Section2. Intersecting with
the parity kernel Dlochat proves the compact equality in (1); the ordinary
intersection proves its discrete version.

No torsion-freeness of E1hat is assumed or needed: the absence of edge
stabilizers containing kappa and its known fixed vertex are sufficient.
No fixed-subgroup assertion for the image a_loc(Dloc) in V_* follows from
(1). A nontrivial invariant quotient kernel can create new fixed elements,
just as the separately proved actual inner-star face illustrates. The
main unresolved condition remains the actual kernel symmetry/interactions
in the ambient quotient, not the local group's fixed calculation.

The complete argument was independently assessed by A before this note
was saved; the exact final source is retained for root review. No new
producer, finite-group census, formal source or register change is used.
