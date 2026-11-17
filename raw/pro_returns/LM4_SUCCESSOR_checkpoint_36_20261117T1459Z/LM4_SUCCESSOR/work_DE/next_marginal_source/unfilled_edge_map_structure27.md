# Actual unfilled edge maps: one embedded inclusion edge and one free target

Research, checkpoint27. This note concerns the actual **unfilled** amalgam
`V=R^0 *_K p(R^0)` of B134. It makes no assertion that the following subgroups
survive the initial quotient `V_*=V/N_*`. The two actual cross sheets and all
ten generators of `N_*` remain as in the frozen B134 source.

## 1. Exact regional intersections, also in the actual completions

Use B112/B117: `K=F(a,B,d,e,f)`, `K1=CKC`, `L=<K,k>`, `E1=CLC`,
`h=fk=Cz`, `k1=CkC=hkh^-1`. The actual ordinary retraction `r:R^0 -> K`
fixes K and satisfies

    r(CuC)=zeta(u), zeta(a)=zeta(B)=zeta(d)=zeta(e)=1, zeta(f)=f,
    r(k)=r(k1)=1.

Both K and E1 have their full induced profinite topologies by B117 and
C-conjugation. Since `r(E1)=<f>` and `f in E1`,

    E1 intersect K = <f>,
    E1hat intersect Khat = closure<f>.

Here `f in E1` is literal: `ChC=h`, so E1 contains h,k1 and hence
`k=h^-1 k1 h` and `f=h k^-1`. The same retraction argument proves the
completed intersection without a completion/intersection exchange.

There is a stronger separate intersection:

    K intersect K1 = 1,          Khat intersect K1hat = 1.            (1)

Indeed an element of the latter intersection is `f^lambda`, because r
fixes Khat and sends K1hat into closure<f>. Applying the C-conjugate
retraction shows that it is also `(CfC)^mu`. The actual z-height character
in B117's `A(Omega) semidirect ( (C2(C)*Z(k)) x Z(z) )` sends f and CfC
to 1. Consequently `lambda=mu` in Zhat.

For each n>=2, use the explicit continuous finite quotient obtained by
killing every graph generator and z, and mapping

    C -> the lamp at 0,       k -> cyclic shift

in `C2 wr C_n`. This is an actual regional homomorphism. In additive lamp
notation, f and CfC have images `(delta_0,-1)` and `(delta_-1,-1)`.
For any integer L their L-th powers have the same shift and their lamp
vectors differ by `delta_0+delta_-L`. This follows by telescoping the
successive shifted lamps; it holds for negative integers as well, and
therefore for a profinite exponent by taking a representative modulo
2n. Equality forces L=0 modulo n. Thus lambda is zero modulo every n,
so lambda=0. This proves (1), discretely and compactly. No assertion
about intersections after the cross filling is involved.

## 2. The target six-generator subgroup is genuinely free before filling

Keep the exact B134 words

    a1=CaC, w0=a a1^-1, v0=p(w0),
    s=v0^-1 k v0, sigma(CuC)=p(C eta(u) C).

Conjugating the subgroup `T=<sigma(K1),s>` by v0 gives

    v0 T v0^-1 = < D', k >,       D'=p(a K1 a^-1).                  (2)

To verify the right subgroup in (2), use `w0 C=a C a^-1`, and use
`eta(K)=K`. Hence

    v0 sigma(K1) v0^-1
       =p(a C a^-1 K a C a^-1)=p(a K1 a^-1).

The right vertex subgroup D' has trivial intersection with the common
K, by (1), because a belongs to K and p preserves K by eta. The left
vertex cyclic subgroup <k> intersects K trivially by the actual base
winding. Ordinary amalgam normal form therefore gives

    T = sigma(K1) * <s> = F6.                                    (3)

This is the literal free basis consisting of the five sigma-images of
the chosen free K1 basis and s. It is not the B117 group E1: its five
prospective B117 relators are precisely rho_0,...,rho_4, which are
imposed only in N_*. In particular the pre-filling target assignment
from the six generators is a free-group map, not already a homomorphism
from E1.

The subgroup T also has its full induced profinite topology in V.
For completeness the full completion of V is the proper amalgam of its
two actual R^0 completions over Khat. Given finite quotients of the two
vertices, choose a finite-index fully invariant subgroup of K contained
in their two edge restrictions (after the specified eta identification).
On each vertex, the product of its prescribed quotient with the actual
retraction followed by this common K quotient has exactly that edge
kernel. The two resulting finite groups embed in a finite permutation
quotient of their finite amalgam, by the standard matching regular-action
construction. This proves the requisite cofinal vertex and edge topology.
The universal property then identifies the completion with the proper
full profinite amalgam.

The closed subgroups D'hat and closure<k> have trivial intersections with
Khat, by the already proved compact version of (1) and winding. The full
closed-vertex-subgroup result of Lopes and Zalesskii (2025, Corollary2.18,
with Lemma2.17) consequently gives their closed generated group as their
free profinite product. Both factors have full topology in their vertices,
so its map from the abstract Fhat6 is injective. Conjugating by v0 proves

    closure_Vhat(T) = Fhat6.                                     (4)

This is precisely the zero-edge-intersection application already used
and primary-proof-audited in B133; it does not use a nontrivial-cyclic-edge
subamalgam assertion.

## 3. The inclusion-side abstract edge really embeds in V

B134 uses the flexible abstract edge `E=E1 * <y>` with inclusion-side
assignment `y -> s'=w0^-1 p(k) w0`. This assignment is injective before
passing to V_*.

Conjugation by w0 changes E1 to `a E1 a^-1`, since `a1 in E1`, and changes
y to p(k). Its left-vertex intersection with K is exactly

    <ell>,              ell=a f a^-1,                            (5)

by Section1. In the right vertex the subgroup `<ell,p(k)>` is p of the
regional subgroup `<eta(ell),k>`. We show that the latter is the free
product of its two infinite cyclic factors.

Use the actual B117 presentation

    L = H *_<k> ( <k> x F(a,d,e,V4) ),
    H=<h,k | [h^2,k]>,       f=h k^-1,       V4=f^-1 B f.

The certified actual eta words give

    eta(ell)=w f^-1 w^-1,
    w=a f V4 f^-1 a^-1 f (d e d^-1) f^-1 d^-1.                   (6)

These are literal K-word equalities, checked independently from the
complete five-word eta dictionary. Each displayed F4 block is nontrivial.
Every nonzero f-power lies outside <k>, by the h-exponent character of H.
For every nonzero integer n, also

    f^-1 k^n f notin <k>.                                        (7)

One direct detector for (7) is `H -> C2(C)*Z(k)`, h->C, k->k:
the image is `k C k^n C k^-1`, a reduced word not in <k>.

Now expand `w^-1 k^n w` using (6). The initial leaf a commutes with k,
so the central H block is `f^-1 k^n f`. The leaf blocks around it, and
all the remaining alternating f and leaf blocks, are nontrivial and
outside the amalgamated cyclic group. Thus this is a reduced amalgam
word beginning in the leaf factor with d and ending there with d^-1.
For any nonzero n_1,m_1,...,n_r,m_r, the product

    (w^-1 k^{n_1} w) f^{m_1} ... (w^-1 k^{n_r} w) f^{m_r}

is still reduced: every joining f^{m_i} lies in H outside <k>, between
the nontrivial leaf end blocks. It cannot be the identity. Pure powers
are nontrivial as well. Conjugating back proves

    <k,eta(ell)> = <k> * <eta(ell)> = F2.                         (8)

The actual retraction L->K kills k and fixes eta(ell). Therefore any
element of this F2 lying in K equals its retraction and is a power of
eta(ell). Its exact intersection with K is that cyclic subgroup.
Applying p gives

    <ell,p(k)> = <ell> * <p(k)>,
    <ell,p(k)> intersect K = <ell>.                              (9)

The two vertex subgroups `a E1 a^-1` and `<ell,p(k)>` in V thus have
exactly the same intersection <ell> with the ambient edge. Ordinary
reduced-word normal form embeds their subamalgam, giving

    <a E1 a^-1,p(k)>
       = (a E1 a^-1) *_<ell> ( <ell> * <p(k)> )
       = (a E1 a^-1) * <p(k)>.

Conjugating by w0^-1 proves that the **actual** inclusion-side map
`E1*<y> -> V`, y->s', is injective. No full induced topology for this
nontrivial-cyclic-edge subamalgam is inferred here.

## 4. The precise remaining actual matching gate

Let i0:E->V be the embedding just proved and let pi:V->V_* be the actual
initial quotient by all rho_i and theta(rho_i). Then

    ker(i:E->V_*) = i0^-1(N_*) = E intersect N_*                   (10)

under the explicit identification. The target E1 generator assignment
has free image F6 in V, and becomes a homomorphism from E1 only after
its five defining rho-relations are imposed. The extra y-image and the
five mirror relations remain essential. Neither (3) nor the injectivity
of i0 proves that the two E->V_* kernels match.

Thus B134's first matching step is now localized to actual normal-closure
intersections with two explicitly identified embedded pre-filling groups,
rather than to an unknown presentation of the inclusion-side edge. The
remaining questions are exact post-N_* intersections, the subsequent
matching union, and its restriction to the actual source F6. No finite
stabilization, source normal-generation statement, closed-intersection
exchange, or fixed-source conclusion has been inserted.

## 5. Both embedded edge groups and an exact symmetric local quotient

There is more structure before the normal-closure interactions are taken.
Since theta(s')=s, the theta-mate of the embedded inclusion edge is

    theta(i0(E))=<p(E1),s>=p(E1)*<s>.                              (11)

Moreover sigma(K1)=p(K1) as a subgroup. Hence the ENTIRE target generator
image `<sigma(K1),s,p(k1)>` is exactly (11), not just its free-six subgroup
of Section2. Each rho_i lies in this theta-mate; each theta(rho_i) lies in
the inclusion edge itself.

Let eta1=Ad(C) eta Ad(C) be the actual involution of the free group K1.
Start with the free product `F_*=K1*<k1>*<y>` and let R be the five B117
words

    [(f1 k1)^2,k1],       [k1,u_i] (1<=i<=4).

There is a literal involution kappa0 of F_*: act by eta1 on K1 and exchange
k1 and y. Thus E=F_*/<<R>>. In the embedded E, the words kappa0(R) are
exactly theta(rho_0),...,theta(rho_4), with no relator or connector omitted.
Define

    Dloc=F_*/<<R,kappa0(R)>>.                                     (12)

This is a proper ordinary amalgam of two copies of E1 over the free K1:
one copy has base generator k1 and the other has base generator y, with
the second K1 marking twisted by eta1. Indeed the first five relations
are exactly one E1 presentation; after applying the invertible eta1
basis change, the second five are exactly the other. Both K1 embeddings
are actual retracts by B117. Therefore the ordinary amalgam is proper.
It has a proper full profinite completion with full vertex topologies:
choose a common fully invariant finite K1 kernel inside the prescribed
restrictions, use each K1-retraction to make that exact edge kernel, and
then match the two finite regular actions. This is a local quotient
statement only, not its embedding into V_*.

The involution kappa0 descends to a genuine involution kappa of Dloc,
interchanging its two E1 factors with the specified eta1 marking. The
actual inclusion induces a homomorphism `a_loc:Dloc->V_*`. In these
terms the other edge homomorphism is exactly

    b_loc = theta composed with a_loc composed with kappa.         (13)

This follows on K1, k1 and y separately. On K1 it gives sigma; on k1 it
gives theta(s')=s; on y it gives p(k1). Both maps already kill the second
set of local relations, so replacing E by Dloc in the B134 HNN pushout
does not change the actual group.

Consequently the ordinary initial kernel-matching gate is the concrete
condition

    ker(a_loc) is kappa-invariant.                               (14)

It is weaker than requiring Dloc to embed. If (14) holds, B134's matching
union starts and stays trivial for the maps from Dloc, so V_* embeds as
the resulting proper HNN base. If it fails, one must retain the entire
matching normal closure. Nothing here proves (14).

There is an exact independent finite version. The B134 matching normals
can be chosen theta-invariant cofinally: if N is matching, (13) implies
that theta(N) is also matching, and N intersect theta(N) refines it.
For a theta-invariant finite-index normal N in V_*, the matching condition
is precisely

    a_loc^-1(N) is kappa-invariant in Dloc.                        (15)

For explicit verification, put A_N=a_loc^-1(N). Equation (13) gives
`b_loc^-1(N)=kappa(A_{theta(N)})`. Matching means
`A_N=kappa(A_{theta(N)})`, which is symmetric in N and theta(N). If N
is theta-stable this reduces to (15). Thus the actual finite comparison
has two specified involutions, on the base and on a known proper local
amalgam; no closure of an ordinary matching union has been substituted.

The outstanding structural issue is now the interaction of the two local
fillings inside V, or equivalently the kernel of a_loc and its kappa
symmetry. Each separate local quotient (12) is completely understood as
a proper amalgam, but that fact alone does not prove its survival after
both normal closures are imposed in the ambient V. The source F6
intersection remains the actual one in B133/B134.

## Evidence and scope

`check_unfilled_edge_maps27.py/.out/.err/.json` checks the exact eta(ell),
conjugator w, the simultaneous old/leaf basis inverses and the actual w0
cone identities, directly from `annular_neck_reflection23.json`. The
all-exponent normal-form and finite-wreath arguments are the proofs above,
not a finite sample or group census. B134's prior one-sheet omission is
not reused: all claims here are before N_*, with the final two-sheet
quotient retained explicitly.

Primary: Lopes, L. C., & Zalesskii, P. A. (2025). Prosoluble subgroups of
the profinite completion of the fundamental group of compact 3-manifolds.
Journal of the London Mathematical Society, 112(4), e70330.
https://doi.org/10.1112/jlms.70330 . Corollary2.18 and Lemma2.17 were opened
and read with their complete proofs in the B133 audit; the exact trivial
edge-intersection hypotheses are verified here.
