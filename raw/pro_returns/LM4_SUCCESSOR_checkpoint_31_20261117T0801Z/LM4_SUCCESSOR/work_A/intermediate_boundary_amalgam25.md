# A proper completed boundary amalgam before the four remaining prefix relations

Research, checkpoint25. The actual regional group R, selected cone c,
neck K, full prefix P=P5 and boundary T=cP are retained. The proved
boundary subgroup is `H=<c,k,T>=C2(c)*Z²(k,T)`. Its embeddings in R
and in the isolated boundary corner have full induced topology. The
actual completed face in R is `Khat intersect Hhat=closure<P>`.

## 1. The exact intermediate group

Write the isolated corner as

`B=<D,u,k,j | D²,j²,[k,D],[k,u],juj=u^-1>`.

Its marked boundary subgroup is `c=jDj`, `T=uD`, with the same k.
The ordinary amalgam

`M=R amalgam_H B`

is therefore proper, using the already proved marked injections. Its
presentation, after eliminating D and u, is exactly

`<R,j | j², [jcj,k], jPj=P^-1>`.

All regional relations are already in R. The full actual mirror
extension is the further quotient

`X=M / normal_closure{j P_i j P_i : i=1,2,3,4}`.

The P_i are the actual prefixes, not a substitute basis in a different
neck marking. This retains the entire actual group: the fifth prefix
relation and the cross relation are precisely the corner, and its
mirror conjugate supplies the second cross relation as before.

## 2. A corner retraction whose companion map extends over R

Let B0 be the j-even subgroup. Its exact graph-product presentation is

`<D,k,u,k',c | D²,c²,[D,k],[k,u],[u,k'],[k',c]>`,

where `k'=jkj`. There is an actual retraction rho:B0->H:

`D ->1`, `k'->1`, `u->T`, `c->c`, `k->k`.

Every displayed relation is respected, and rho(T=uD)=T. Its companion
endomorphism on H, obtained by first conjugating by j, is

`nu(c)=1`, `nu(k)=1`, `nu(T)=T^-1 c=P^-1`.

Since P=cT, we have nu(P)=P^-1 and `nu³=nu`.

Crucially this companion extends over the ACTUAL regional group.
Let lambda:R->Z be its marked branch-height character, sending h to1
and C,k,a,b,d,e to0. All actual regional relations respect lambda;
f=hk^-1 and P=aBfde both have height1. Thus

`v:R->R`, `v(g)=P^(-lambda(g))`

is a homomorphism with image in H. Its restriction to H is exactly nu,
and `v³=v` because lambda(P)=1. This is an actual extension, not an
assumed arbitrary retraction from R to H.

## 3. Cofinal exact common finite edge kernels

Let A_R and A_B be any prescribed finite-index normal subgroups of R
and B. The full induced topology of H in R supplies a finite-index
normal subgroup V_R contained in A_R such that

`V_R intersect H` is contained in `A_B intersect H`.

Let psi:R->R/V_R and N=ker(psi|H). Use the finite product homomorphism

`Phi=(psi, psi composed v, psi composed v²): R -> (R/V_R)^3`.

Its exact restriction kernel on H is

`L=N intersect nu^-1(N) intersect nu^-2(N)`.

This is finite-index normal in H, is contained in A_B intersect H,
and is nu-stable: applying nu cycles the final two conditions because
nu³=nu. Also ker(Phi) is contained in A_R, by the first coordinate.

The actual paired map on B0,

`b -> (rho(b) mod L, rho(j b j) mod L)`,

extends over B=B0 semidirect C2(j) by sending j to coordinate swap.
On H it is `h -> (h mod L,nu(h) mod L)`. Nu-stability makes its
restriction kernel exactly L. Intersect its kernel with A_B; the
restriction is still L, because L was chosen inside A_B intersect H.
We have constructed finite-index normal kernels on both vertices,
refining the prescribed ones, with the IDENTICAL actual edge kernel L.

Write their finite images as F_R,F_B and the common edge as H/L.
The finite-group amalgam `F_R amalgam_(H/L) F_B` is proper and
virtually finitely generated free. The usual finite permutation
construction aligns free actions of the finite edge group and yields
a finite quotient injective on both finite vertices; its free kernel
also proves residual finiteness of this finite-group amalgam. These
are the same elementary finite-head facts already proved in B114/B118.

It follows that each vertex has its full induced topology in M.
Moreover every finite target of M factors through one of these
finite-group amalgams: apply the construction to its two restriction
kernels. Thus the full profinite pushout is proper and is exactly

`Mhat = Rhat amalgam_Hhat Bhat`.

This argument does not assume residual finiteness of M, separability
of arbitrary products, or an automatic properness theorem for a
general full profinite amalgam. It uses the explicit companion
extension v and the already established full topology of H in R.

## 4. Exact discrete selected-cone centralizer at this intermediate stage

All involutions of `H=C2(c)*Z²` are H-conjugate to c, by the ordinary
free-product normal form; `C_H(c)=<c>`. In the actual regional vertex,
B112 gives `C_R(c)=F5_source times <c>`. In the isolated corner,
the already checked cyclic-amalgam normal form gives

`C_B(c)=<k'> times <c>`, `k'=jkj`.

Consider the actual Bass–Serre tree of M. The c-fixed subtree contains
the base edge. At either of its endpoints, every incident c-fixed
edge is carried to the base edge by that vertex's c-centralizer:
the associated conjugate of c lies in H, and its unique H-involution
class permits adjustment of the edge representative by an element
of H to make that representative centralize c. Applying this along
finite paths in the fixed subtree makes its centralizer quotient the
single edge. The subgroup normal-form theorem, equivalently the same
successive adjustment of a reduced amalgam word, gives

`C_M(c)=C_R(c) amalgam_<c> C_B(c)`

`       =(F5_source * Z(k')) times C2(c)=F6 times C2(c)`.

Conjugating by j gives the selected opposite-cone version

`C_M(D)=(j F5_source j * Z(k)) times C2(D)`.

These are DISCRETE statements about M. No completed centralizer
formula is inferred merely from properness of Mhat. In particular
the centralizer action on a profinite tree must not be handled by
an unproved finite-path argument.

## 5. The six actual source words remain exactly marked

Take the five original positive regional source words in R, including
their entire selected-gap conjugation a. Their j-conjugates, followed
by k, freely generate the ordinary factor in C_M(D). They are exact
prelifts of the six actual one-neck source words. Under M->X, the four
remaining prefix relations identify `j x j=eta(x)` on all of K;
hence these five j-conjugates become the actual outer regional words,
and k is the actual inner good source loop.

This can be checked on the raw words before using their B112 simplified
Nielsen basis: the local plus tuple is literally the j-image of the
minus tuple after the full neck reflection is imposed. The check
therefore retains the real based source words and does not infer their
final images from ranks. No freeness of those images in X follows.

The complete literal comparison is executed in
`work_A/code/check_intermediate_source_prelifts25.py/.out/.err`, with
all words and source hashes in `work_A/intermediate_source_prelifts25.json`.
It reads the stable actual nine-generator package and imports no prior
producer. The intermediate words use j freely around the five inner
regional words; eta is applied only in the explicitly labeled final
quotient map. All six comparisons use the original positive source
words, not just the simplified B112 Nielsen basis.

## 6. An actual embedded carrier for the four torsion relations

Inside B put `Q0=<P,j>`. The relation jPj=P^-1 holds. The map from
the abstract infinite dihedral group to B has a left inverse: send
D,k to1, u to the actual P, and j to j. In fact
`P=j D j u D` maps to P. Thus Q0 is the genuine infinite dihedral
subgroup, with full induced topology in B. Its mirror-even subgroup
is exactly <P>, so

`Q0 intersect H=<P>` and `Q0hat intersect Hhat=closure<P>`.

The completed equality here follows just from the continuous parity
character and the embedded full Q0hat, not from an intersection exchange.
Together with the actual discrete equality K intersect H=<P> in R,
ordinary amalgam normal form embeds the subgroup

`J0=K amalgam_<P> Q0` in M.

Every reduced alternating syllable outside <P> remains outside H
in its respective vertex, which is the complete injection proof.
Since P1,...,P5 are the actual free K basis and P=P5,

`J0=F(P1,P2,P3,P4)*D_infinity(P5,j)`.

The invertible Nielsen change `w_i=jP_i`, i=1,...,4, fixing the
dihedral factor, gives

`J0=F(w1,w2,w3,w4)*C2(j)*C2(jP5)`.

Thus all four remaining relations are precisely `w_i²=1` on four
independent free generators of this actual carrier. They are cyclically
reduced length4 in the R/H/B amalgam: Pi is outside H for i<5 by
the exact face intersection, and j is outside H by mirror parity.
In particular each w_i is hyperbolic of translation length2 before
these relations are imposed.

Its quotient by the four squares is the actual six-C2 mirror vertex Q.
The final group is the categorical pushout `M *_(J0) Q`, where
J0->Q is surjective, equivalently the already stated normal-closure
quotient of M. This is not a proper amalgam with two injective edge maps.
No small-cancellation criterion or congruence-extension property of
J0 in M has been proved. The two completed face intersections alone
are not used to assert that the full completion of J0 embeds in Mhat.

## 7. Exact remaining gate

The intermediate group retains all regional relations and has the
known discrete source centralizer. The final four relations identify
the remaining actual neck prefixes with their mirrored inverses.
They can introduce new centralizing elements or relations in the
source image; no survival theorem has been proved. The exact completed
face Khat intersect Hhat helps type these relations, but does not
remove them. Both main decisions remain Open.
