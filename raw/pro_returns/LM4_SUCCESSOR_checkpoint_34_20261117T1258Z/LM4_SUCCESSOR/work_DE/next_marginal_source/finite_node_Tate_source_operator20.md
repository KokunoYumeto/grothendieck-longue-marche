# The full finite node domain and the actual source-operator ideal

Research proof, 16 November 2026, checkpoint 20 cycle. No numbered
statement is added during the current formal freeze. This is a finite
operator description of the full obstruction domain, not a proof that
the obstruction vanishes.

## 1. Actual groups and the exact finite domain

Use B104's based groups and its genuine geometric involution. Put

    G_ev = G semidirect S,  S=F11,
    Lambda=Z[G_ev],  D=Lambda^128.

The convention is `s^-1 g s=psi_s(g)`, so left conjugation by s is
`theta_s=psi_s^-1`. Every chosen source lift is literally fixed by F;
therefore theta_s commutes with F on G. The fixed coefficient group is

    K=G_ev^F = diag(R) semidirect S.

B104.8 supplies the actual equivariant sequence

    0 -> Z2 -> D -> P -> M_ab -> 0.

Equivalently, writing Lbar for the image in P,

    0 -> Z2 -> D -> Lbar -> 0.                         (1)

The 128 node faces include both sheets. Their Lambda translates encode
every retained-deck and actual even-source translate, including the
entire old-source orbit. This is the finite CW sequence, not a finite
selection from an infinite direct sum. Its kernel is the actual H2 of
the cover: the source-cylinder faces have been eliminated using their
proved injective boundary, with unique completion of each node syzygy.

The genuine F action on these faces is the one independently checked
in `finite_even_node_F2.json` and
`finite_node_F2_independent_review20.json`. It is obtained from the
actual symmetric local torus and common whiskers; it is not an
arbitrary lift of the one-chain action. There are sixteen fixed
physical faces. Their raw orientation signs are negative. In each
sheet four of these have neutral coefficient cocycle and four have
the other cone class. The remaining physical faces occur in pairs.

## 2. No new neutralization on adjoining the source operators

Consider one fixed face e, with

    F(e)=-a e,  a in G,  F(a)a=1.

A coefficient basis element g e is fixed up to this minus sign exactly
when `F(g)a=g`. In the enlarged ring write a coefficient uniquely as
`g s`, with g in G and s in S. Its fixed-index equation is

    F(g) theta_s(a) = g.                              (2)

Apply theta_s^-1. Since it commutes with F, (2) has a solution exactly
when `F(h)a=h` has a solution in G. Thus adjoining the actual even
source group creates no new neutral fixed-face cocycle. In particular,
the four other-cone faces in each sheet remain nonneutral. This is an
actual normal-form argument; no invariant of an approximate quotient
or presumed preservation of a chosen meridian splitting is used.

For a neutral face choose the audited coefficient c with F(c)a=c and
replace its generator by e'=c e. Then F(e')=-e'. Its coefficient index
is fixed precisely for g in K. Equivalently, the original fixed-index
solutions form a free transitive left K-torsor. Every remaining index
lies in a two-element orbit. A negative fixed integral generator has
Tate H1 equal to F2 and Tate H2 zero. Each two-element orbit is an
induced integral C2-module, after changing one basis sign if necessary,
and has zero Tate cohomology. Paired physical faces are induced for
the same reason, regardless of their printed raw signs.

There are eight neutral faces in total. Consequently, with its actual
left F2[K] action,

    H1(C2,D) = F2[K]^8,       H2(C2,D)=0.              (3)

Here H1 and H2 can equivalently be read as positive-degree Tate groups.
The finite periodic C2 resolution commutes with the direct sums of
coefficient orbits, so infinite coefficient support is not introduced.

## 3. The eight actual source normalizations

The four neutral first-sheet faces are the fixed nodes with node
indices (0,1), (8,1), (12,1), and (16,1). Their audited half-chains
give the four first-sheet source peripherals. The opposite-sheet
faces use the actual alpha_b^-1 pullback, not an unidentified positive
old-base action; their neutral node indices are (0,0), (8,0), (12,0),
and (16,0). Their four half-chains give the other four source
peripherals. These are the eight actual words rho_j in the full
source F19-to-F11 dictionary. The raw fixed-face coefficients may
choose another point of the corresponding K-torsor. Multiplying the
normalized generator by the explicitly matching fixed-deck unit
selects the half-chain whose diagonal is the prescribed source word.

Thus bases in (3) may be chosen so that the composite

    H1(C2,D) -> H1(C2,Lbar) -> H1(C2,P)=I_F2[R]

sends the eight generators to `rho_j-1`. If the right-defect convention
instead prints `rho_j^-1-1`, multiplication by the fixed diagonal unit
rho_j changes it to rho_j-1 over F2. This does not change the generated
left ideal. Both-sheet word comparisons and their full integral
half-chains, not merely abelian winding coordinates, are retained in
B96 and the actual source certificates.

The K action on I_F2[R] is left multiplication by the diagonal R and
the actual theta action by S. Naturality through mixed meridian
conjugators follows from the intrinsic right-defect sequence used in
B95: an actual F-commuting source operator carries the defect class
`r^-1-1` to `theta_s(r)^-1-1`. These elements span the augmentation
ideal. No literal tensor action on an unpreserved free-factor splitting
is needed.

The actual source-kernel image is

    I=<theta_s(rho_j):s in S,1<=j<=8>.

The elementary group-ring identities for products and inverses now
give the exact image

    image H1(C2,D) = sum_j F2[K](rho_j-1) = J_I.        (4)

This is the full source ideal. It is eight-generated over the enlarged
operator ring F2[K], while it need not be finitely generated over
F2[R]. The precise finite permutation-module presentation, and the
distinction from finite presentation of its reduced augmentation
kernel, are recorded in A's
`finite_source_operator_coset_presentation20.md` and independently
reviewed in `review_finite_source_operator_cosets20.md`.

## 4. The exact residual map

The cohomology sequence of (1), together with H2(C2,D)=0, gives

    H1(C2,D) -> H1(C2,Lbar) -> H2(C2,Z2) -> 0.

Using (4), the composite from H1(C2,Lbar) to I_F2[R]/J_I therefore
descends uniquely to an F2[K]-linear map

    kappa_fin: H2(C2,Z2) -> I_F2[R]/J_I.               (5)

If U denotes the image of H1(C2,Lbar) in H1(C2,P), then

    image(kappa_fin)=U/J_I.

This is the same actual residual obstruction as B91/B96/B102, now with
the finite whole-orbit domain and actual geometric Z2. It is not a
kernel identification between two unrelated choices of common-whisker
presentation. It follows from B104's geometric relative CW model and
its unique source-cylinder completion.

The proof supplies no value for (5), no finite generation of Z2, no
simultaneous free basis for the nonlinear node relations, and no
nonabelian or profinite fixed lift. B105's induced spherical submodule
has zero Tate cohomology itself; that does not remove the remaining
kernel or its quotient-cohomology effects.
