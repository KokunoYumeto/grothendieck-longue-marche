# The actual ordinary star amalgam and its single remaining cross relation

Research after B120–B123, checkpoint25. All markings are actual; no
statement about the centralizer after the last relation is made.

## 1. Change the order of the actual two fillings

Let R be the complete regional group of B112, with adapted involution C,
ordinary index-two subgroup R^0, selected cone c=a C a^-1, neck
K=F(a,B,d,e,f), B=CbC, and k=f^-1 h. The complete source/generic
relations include [k,a]=1, C h C=h, and C k C=h k h^-1.
Let eta be the actual based neck reflection, and

    Q=K semidirect_eta C2(j).

Before the two cross commutators, the whole mirror extension is the
proper ordinary amalgam

    A=R *_K Q.

The actual final mirror extension is A modulo [j c j,k]. Its
j-conjugate is the other actual cross relation. In this presentation
ALL FIVE prefix inversion equations already hold in Q, and every
regional node/base relation already holds in R. This is the other
order of the exact operations used in B120: impose the whole mirror
neck first, then the cross relation.

Extend the original ordinary character epsilon of R by epsilon(Q)=0.
Thus epsilon(C)=1 and epsilon(j)=0. The ordinary kernel A^0 is the
proper star amalgam

    A^0 = Q_0 *_K R^0 *_(C K C) Q_1,
    Q_0=Q,   Q_1=C Q C.

Its two leaf-edge maps are the literal inclusions K and C K C into
R^0. This follows directly from the quotient of the ordinary
Bass–Serre tree by the index-two kernel: there is one R^0 vertex,
two Q vertices, and the two indicated edges. Equivalently the
two-coset rewriting introduces j_0=j and j_1=CjC, with all five
inversion relations on K and C K C respectively and no relation
between j_0,j_1. This gives inverse presentation maps without any
assumption about subgroup survival in the final quotient.

## 2. One cross relation, not two independent ordinary relators

Write A_1=C a C and K_1=C k C. Define

    t_0=j_0 a A_1^-1 j_1,
    j_0'=a^-1 j_0 a,
    j_1'=A_1^-1 j_1 A_1,
    g=j_0' j_1'.

The selected opposite cone is exactly

    tau=j c j=t_0 C,
    t_0=a g A_1^-1.

Conjugation by C on A^0 swaps j_0,j_1, a,A_1 and k,K_1.
The free-product identity C t_0 C=t_0^-1 follows by cancellation;
it is also forced by tau^2=1. The actual cross relation is

    r_0=t_0 K_1 t_0^-1 k^-1=1.

Its C-conjugate is exactly t_0^-1 r_0^-1 t_0. Therefore its normal
closure in A^0 is already stable under C. This proves, with no
missing sheet of the cross relator, that the final original-parity
kernel X^0 is

    X^0=A^0 / normal_closure_(A^0)(r_0).

The actual regional commutations [k,a]=[K_1,A_1]=1 give

    r_0 = a (g K_1 g^-1 k^-1) a^-1.

For a complete universal verification of this last use of relations,
put alpha=A_1^-1 K_1 A_1 K_1^-1 and
beta=a^-1 k^-1 a k. Before imposing either commutation, the difference
between r_0 and the displayed conjugate is exactly

    (a g) alpha (a g)^-1
       * (a g K_1 g^-1) beta (a g K_1 g^-1)^-1.

Both factors vanish in the actual regional group. Finally K_1=h k h^-1,
so with z_*=g h the whole final ordinary presentation becomes

    X^0 = (Q_0 *_K R^0 *_(C K C) Q_1)
             / normal_closure([z_*,k]),
    z_*=(a^-1 j_0 a)(A_1^-1 j_1 A_1)h.

This is a single specified commutator quotient of a genuine star
amalgam. It is not an HNN extension obtained by declaring z_* to be
an independent stable letter: z_* is the entire displayed existing
word, and its defining relation cannot be omitted.

## 3. The star has proper full completion

The ordinary regional retraction r:R^0->K is the actual complete
detector of B112/B114. Its companion zeta=r Ad(C)|K kills a,B,d,e
and fixes f. Thus for x in K,

    r(x)=x,       r(C x C)=zeta(x).

Let prescribed finite-index normal kernels be A_R in R^0 and A_i in
Q_i. Identify the second leaf's K with K by C-conjugation. Choose a
finite-index normal N in K contained in all four required edge
kernels: K intersect A_R, K intersect C A_R C, A_0 intersect K,
and the pullback of A_1 intersect C K C.

There is a finite-index fully invariant subgroup L of K contained in
N. Explicitly, take the intersection of the kernels of ALL
homomorphisms K->K/N. There are finitely many because K is finitely
generated and the target is finite, and the quotient map is one of
them. Precomposition proves full invariance. In particular L is
stable under zeta and under eta and eta^-1.

Let psi:R^0->R^0/A_R. Use the finite product homomorphism

    Phi(x)=(psi(x), r(x) mod L, r(C x C) mod L).

Its exact edge kernel on K is L: the second coordinate forces L,
the first kills L by its choice, and the third kills L by zeta
stability. Its exact edge kernel on C K C is C L C, by the same
argument with the two retraction coordinates interchanged.
Its total kernel refines A_R.

Each leaf Q_i is a semidirect product of its free K edge with its
reflection. Since L is eta-stable, the canonical finite semidirect
quotient (K/L) semidirect C2 has exact edge kernel L. Combining it
with the prescribed finite leaf quotient refines A_i without
changing that edge kernel, because L was chosen inside its
restriction kernel. We have therefore produced compatible finite
quotients of all three star vertices, refining arbitrary targets,
with the exact two edge quotients K/L.

The resulting finite graph of finite groups has a finite permutation
quotient injective on every vertex. Choose free actions on one set
whose cardinality is divisible by all three vertex orders. Align
each leaf action independently with the central action on its edge;
the underlying graph is a star, so these two alignments have no
cycle compatibility condition. The induced map of the amalgam
retains all finite vertices.

Thus every vertex has its full induced topology in A^0, and the
universal property on finite targets gives the proper full profinite
star amalgam. This proves no vertex embedding after [z_*,k] is
imposed. In particular the target source/fixed-group problem is
still in the actual one-relator quotient, not in this pre-cross star.

## 4. Exact source and action scope

The five whole selected regional source words s_i of B120, including
the selected-gap a conjugation, give the five outer source words
j_0 s_i j_0 in this star. Together with k they are the same six
actual source prelifts retained in B120/B121. Their images in X^0
are the actual six source words. No free-source conclusion follows.

The outer original-cone action is conjugation by tau=t_0 C, not
merely C-conjugation and not the mirror involution. Although the
two sheets of the one cross relation are redundant as proved above,
all regional relations remain in R^0, all five mirror-prefix
relations remain in both Q_i, and the word z_* retains both leaf
reflections and the actual h. No relation has been replaced by its
abelianization or by a finite-depth orbit calculation.

## 5. Exact word certificate and remaining issue

`work_A/code/check_ordinary_star_cross25.py` verifies the universal
free-product identities and the explicit commutator-relator
factorization. Its genuine output and complete words are retained
adjacent to it and in `work_A/ordinary_star_cross25.json`.

The normal form before the final commutator is established. A
normal-form or fixed-subgroup theorem for the quotient by this
specified existing-word commutator has not been proved. Neither
full regional survival nor the selected-source centralizer equality
is inferred. The alternative presentation may allow a relative
annulus/folding analysis, but it does not itself supply one.
