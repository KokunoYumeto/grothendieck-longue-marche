# Exact fixed subgroup on the actual both-family filled surface

Proposed proof for independent review, 2026-11-16, checkpoint16. This concerns
Y_b itself. It does not solve fixed-element lifting through the subsequent
symmetric deletion kernels. The coordinate q below is the original product
q=vw, not the eta coordinate of the separate tangential construction.

## Statement and actual marking

Let

\[
Y_b=\{(v,w)\in(\mathbb C^*\setminus\{1\})^2:
                 v\ne w,\ vw\notin\mu _5\},\qquad
L_b=Y_b\cap\{v+w=2\}.
\]

Use the actual base point P=(399/200,1/200), and define

\[
F(v,w)=\left(\frac{v(w-1)}{1-v},
             \frac{w(v-1)}{1-w}\right).
\]

This is a base-point-fixing involution of Y_b. Write Pi_b=pi_1(Y_b,P),
sigma=F_* and H_b=image[pi_1(L_b,P)->Pi_b]. Then

\[
C_{\Pi_b}(\sigma)=H_b\cong F_{11},\qquad
C_{\widehat\Pi_b}(\widehat\sigma)=\overline{H_b}
                                      \cong\widehat F_{11}.
\]

Equivalently, in the actual split extensions by the based involution,
its centralizers are H_b times C2 and H_b-closure times C2. The closed
source group is its actual compact image, and its full topology is proved
below rather than assumed. The original source L before the eight
constant/moving fillings maps surjectively to L_b on fundamental groups;
therefore these are also exactly the images of that original source in
Pi_b and its full completion.

## 1. Actual bundle and the fixed-point cover

The product projection p:Y_b->B, B=C* minus mu5, has fiber coordinate v:

\[
X_q=\mathbb P^1\setminus\{0,\infty,1,q,+\sqrt q,-\sqrt q\}.
\]

All six points are distinct for q in B. On small simply connected base
neighborhoods the square roots can be labeled, and isotopy extension for
the moving punctures gives actual local trivializations. Thus this is a
locally trivial six-punctured-sphere bundle. Its base and fiber are
aspherical with free groups B_*=F6 and N=F5. The homotopy exact sequence,
using pi_2(B)=0, gives

\[
1\longrightarrow N\longrightarrow\Pi_b
 \xrightarrow{p_*}B_*\longrightarrow1.
\]

Because B_* is free, the group extension splits after choosing lifts of
its six generators. No geometric global section is asserted from that
noncanonical group splitting.

On the q-fiber the involution is

\[
F_q(v)=\frac{v-q}{v-1}.
\]

Its projective matrix squares to (1-q)I. It exchanges respectively
{0,q}, {1,infinity}, and {sqrt q,-sqrt q}; thus it preserves X_q. It has
exactly the two fixed points v=1 plus/minus sqrt(1-q), equivalently v+w=2.
The whole fixed locus is precisely L_b, and F fixes P literally.

The restriction L_b->B is the actual finite unramified double cover

\[
w(2-w)=q,\qquad (w-1)^2=1-q.
\]

Its possible branch values 1 and infinity are removed from B. At
q_*=399/40000 the chosen source point has v=399/200, the plus root.
The image B0 of pi_1(L_b,P) in B_* is the kernel of the character

\[
\epsilon:B_*\longrightarrow C_2
\]

that records the sign of sqrt(1-q). In the puncture basis it is one on
the loop about q=1 and zero on the loops about q=0 and the four other
fifth roots. Therefore B0 has index two and rank11. In particular the
source map to Pi_b is injective, since its composition with p_* is the
injective covering map. It identifies H_b with B0 and supplies the actual
splitting

\[
\Pi_0:=p_*^{-1}(B0)=N\rtimes H_b.
\]

F fixes the whole source pointwise, so sigma fixes H_b pointwise.

## 2. The actual fiber orbifold and its cone permutation

Put c=1-q and u=v-1. Then F_q(u)=c/u. The quotient coordinate

\[
a=u+c/u
\]

has the three deleted values infinity, -2, q-2. Its two order-two cone
points are plus/minus 2sqrt(1-q). These five points are pairwise distinct
in the required sense for q in B: the deleted values are distinct, the
cone points are distinct, and no cone point is deleted.

The actual orbifold fundamental group of this quotient is

\[
E=N\rtimes\langle\sigma\rangle
 \cong C_2*C_2*F_2.
\]

Indeed a sphere with three punctures and two order-two cone points has
presentation

\[
\langle a_0,a_1,d_0,d_1,d_\infty:
 a_0^2=a_1^2=1,\ a_0a_1d_0d_1d_\infty=1\rangle,
\]

and eliminating d_infinity gives the displayed free product. The
index-two manifold cover is exactly X_q. The chosen based involution
sigma is the first cone element, up to the harmless fiber conjugacy
in this identification. The two cone elements have distinct independent
images in E_ab tensor F2 = F2^4.

This is also an actual orbifold bundle over B. Locally choose the two
square roots of 1-q and trivialize the moving quotient punctures and cone
points; lifting this isotopy through the double orbifold cover gives
compatible local equivariant trivializations of X_q. Thus base transport
permutes the two conjugacy classes of cone involutions exactly as it
permutes the two fixed points. Its permutation character is epsilon.
This statement uses the actual fixed-point cover, not a separately chosen
unmarked free-product isomorphism.

For additional algebraic precision, let Gamma=Pi_b semidirect C2, with
sigma the specified based involution. Since sigma acts identically on
B_*, E is the kernel of Gamma->B_*, hence normal. Conjugation by Pi_b
acts on the characteristic finite quotient

\[
A=E/([E,E]E^2)\cong\mathbb F_2^4.
\]

It permutes the distinct vectors a0,a1 according to epsilon(p_*(g)).
Inner conjugations from N act trivially on A. This finite quotient will
retain the cone-permutation obstruction after full completion.

## 3. Discrete centralizer

By the ordinary reduced-word normal form in C2*C2*F2, the centralizer of
a nontrivial element of either C2 factor is that factor itself. Therefore
C_N(sigma)=1.

If g in Pi_b centralizes sigma, its conjugation fixes the vector a0 in
A. The cone-permutation calculation forces epsilon(p_*(g))=0, so
 g belongs to Pi_0. Write g=n h with n in N and h in H_b. Because sigma
fixes h pointwise, sigma(g)=g is equivalent to sigma(n)=n. Thus n=1
and g=h. Conversely every h in H_b is fixed. This proves the discrete
claim without assuming that every fixed element is represented by a
pointwise fixed loop.

## 4. Exact full completion, including the actual fiber topology

The necessary completion statement is proved directly. For any
finitely generated free group N, finite-index characteristic subgroups
form a cofinal family: intersect the finitely many subgroups of bounded
index. Let K be one of them. In the chosen splitting Pi_b=N semidirect
B_*, the action on N/K has finite image A_K in Aut(N/K). The homomorphism

\[
\Pi_b\longrightarrow (N/K)\rtimes A_K
\]

has kernel intersecting N in exactly K. Hence N carries its full
profinite topology from Pi_b. Elements outside N are separated using
finite quotients of B_*, so the discrete extension is residually finite.
The closure of N in the full completion is exactly N-hat, and right
exactness of profinite completion gives

\[
1\longrightarrow\widehat N\longrightarrow\widehat\Pi_b
 \longrightarrow\widehat B_*\longrightarrow1.
\]

The chosen group splitting extends continuously, giving the actual
semidirect product on completions. This is not inferred from a generic
free-by-free completion assertion with an unchecked fiber topology.

Since B0 has finite index, its full completion is its closure in B_*-hat.
The actual source H_b maps isomorphically to B0, so its map on completions
is injective, with image H_b-closure. Moreover

\[
\widehat\Pi_0=\widehat N\rtimes\overline{H_b}
             =p_*^{-1}(\widehat B0)
\]

is the actual open subgroup of Pi_b-hat. The completed sigma fixes
H_b-closure pointwise.

Finite extensions commute here with completion: the completion of
E=N semidirect C2 is N-hat semidirect C2, and also, by the universal
property of finite quotients of a free product,

\[
\widehat E=C_2\amalg C_2\amalg\widehat F_2.
\]

The full-profinite free-product centralizer theorem of Herfort--Ribes
(1985), Theorem B', gives C_{E-hat}(sigma)=<sigma>, hence
C_{N-hat}(sigma)=1. This is the full profinite theorem, not a pro-p
recognition assertion and not a closed-subgroup Kurosh inference.

The finite quotient A above is characteristic in E and survives as
E-hat_ab modulo2. Conjugation of Pi_b-hat on it is the continuous
extension of the discrete finite action. Thus it still permutes a0,a1
by the completed epsilon character. If g in Pi_b-hat centralizes sigma,
it fixes a0, so p_*(g) belongs to B0-hat. The open semidirect product
then writes g=n h; its fixedness forces n=1 by the full-profinite
centralizer theorem. Consequently

\[
 C_{\widehat\Pi_b}(\sigma)=\overline{H_b}.
\]

This proves both the absence of new completed outside-cover fixed
elements and the absence of new completed fiber fixed elements.

## 5. Original source and exact remaining gate

The original L is obtained from L_b by deleting the four w=u and four
w=2-u points for u in mu5 except1. Filling those punctures is surjective
on discrete fundamental groups and on full completions. Hence its actual
image in the filled surface is H_b and its actual closed image is H_b-bar.

This theorem identifies the fixed subgroup on Y_b. It does not assert
that a fixed element in a quotient by the two symmetric deletion kernels
has a fixed lift before filling. That latter obstruction concerns the
intersection of the two actual filling kernels and is DE's separate
remaining problem. It is not eliminated by the fiber orbifold's torsion
centralizers or by an abstract group fiber-product surjection.

## Verification and primary source

Exact rational involution, puncture exchange, source-cover and quotient
identities are checked in work_A/code/check_filled_surface_involution.py
and its genuine output. No finite-group census is involved.

Herfort, W., & Ribes, L. (1985). Torsion elements and centralizers in free
products of profinite groups. Journal fur die reine und angewandte
Mathematik,358,155--161. https://doi.org/10.1515/crll.1985.358.155.
The full author-associated text was reopened at
https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups
(retrieval turn815view0). Theorem B' and its proof, printed159--160,
explicitly apply to the full class of finite groups. They give exactly
the finite-factor centralizer equality used here. Existing verified
bibliography key A_HR1985 suffices.
