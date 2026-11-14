# Cyclic cubic covers of ordinary elliptic curves in characteristic two

Status: proved and integrated as A.29h after independent reviews by root and the degeneration agent. The historical filename is retained for provenance. The proof below is geometric and uniform; its finite certificate checks the torsion-orbit decomposition and the dihedral fibre action, not a sample of elliptic parameters. The full independent review is audit/A_cubic_two_branch_independent_review.md; the exact supporting certificate is code/A_cubic_two_branch_certificate.py/.json.

## Statement

Let k be a finite field of characteristic two and let C/k be smooth proper geometrically connected of genus at least two. If C over kbar admits a cyclic Galois cover of degree three to an ordinary elliptic curve E, then its geometrically prime-to-two point-section map is injective over every finite constant extension. The same conclusion holds for any elementary abelian 3-group Galois cover of an elliptic curve. The supersingular elliptic case was already proved in A.29. Spreading gives the corresponding result over fields finitely generated over F2, and functoriality gives it for hyperbolic open subcurves.

The construction first proves a separation lemma for a two-point cyclic cubic auxiliary inside a more highly ramified ambient cover. It does not assert that an arbitrary ramified double cover of an ordinary elliptic curve satisfies A1.

## 1. A two-point cubic auxiliary and its reflection quotients

Work over kbar. Choose distinct A,B in E and a coefficient a in {1,2}. Multiplication by three is surjective on Pic^0(E). Hence there is a degree-zero divisor D for which

    a(A−B)+3D = div(f).

The cover T/E given by z^3=f is connected, cyclic of degree three, and ramified exactly at A and B, with full tame index three. Riemann–Hurwitz gives g(T)=3.

Let rho(t)=A+B−t. It interchanges A and B, and its pullback acts as minus one on Pic^0(E). Thus D+rho^*D is principal. After adjusting a constant in kbar, choose h with

    f rho^*f=h^3.

The rule tau|_{k(E)}=rho^*, tau(z)=h/z defines an automorphism of T which inverts its cubic deck generator delta. It is an involution: tau^2(z)=(rho^*h/h)z; the ratio has cube one because rho^*(h^3)=h^3, and is therefore constant. Applying rho again gives its square one, so it is one. This also follows from tau^2 being a deck transformation, both commuting with tau and inverted by tau, in a group of odd order.

There are exactly two geometric fixed points of rho on the ordinary elliptic curve E: solve [2]t=A+B, using the separable degree two of [2]. Neither is A or B. Above each, T/E is étale and tau acts as a reflection on a three-element cyclic torsor, hence fixes exactly one point. These are all fixed points of tau.

The quotient E/rho has genus zero. Its two fixed points each have different exponent two: the total different is four by Riemann–Hurwitz, while every wildly ramified quadratic point has different exponent at least two. At a tau-fixed point of T, the completed local map T→E is an isomorphism over the algebraically closed residue field and intertwines the involutions. Thus the local different exponent is again two. For H=T/<tau>, Riemann–Hurwitz gives

    2g(T)−2=4=2(2g(H)−2)+4,

so g(H)=1. The same applies to tau'=delta tau delta^{-1}.

## 2. Ambient ramification makes both elliptic quotients detect points

Let V/E be a connected abelian 3-group cover containing T, with local ramification index three at a point x satisfying

    rho(x)=x,  x not in {A,B}.

Assume also that the purported collision on V has equal E-images. Let Q be the unique tau-fixed point of T above x, and let y be its image in H. The whole fibre of T→H above y consists of Q, with local index two. Since T/E is unramified at x and V/E has index three there, every point of V above Q has index three in V/T. Therefore **every** local ramification index of V→H above y is six. A.21 applies with m=3, even though V→H need not be Galois, and forces equal H-images for any point-section collision on V. It also applies to the quotient H'=T/<tau'> using its own unique fixed point over x.

Let P_T,Q_T be the images of a collision in T. Equality in both quotients says either P_T=Q_T or

    Q_T=tau(P_T)=tau'(P_T)=delta^2 tau(P_T).

In the latter case Q_T is fixed by delta. Such a point lies above A or B, where T/E has a single geometric point. Equal E-images then imply P_T=Q_T after all. Thus both reflection quotients, together with the E-image, force equal T-images. This treats every fibre, including the branch points.

## 3. Pull back the original cover and decompose its branch vectors

Let C/E be any ramified cyclic cubic cover. It is ramified because g(C) is at least two. Pull it back along [3]:E→E and let C' be the normalization. This pullback is connected: a ramified cyclic cubic function-field extension cannot share a nontrivial subextension with an unramified isogeny extension. The map C'→C is étale of degree nine with group E[3].

Choose a Kummer equation w^3=F(t) for C'/E. Every original branch point has an inverse image G=t_0+E[3], a nine-point coset. Its branch coefficient a modulo three, either one or two, is constant on G. Different original branch points give disjoint cosets. On each G choose its representative t_0. In the free F3-module on G one has the exact identity

    a sum_{g in E[3]} [t_0+g]
      = sum_{0 != g in E[3]} a([t_0+g]−[t_0]).             (1)

At t_0 the right-hand coefficient is −8a=a modulo three. All other coefficients are visibly a.

For every nonzero g, form a two-point cyclic cubic auxiliary T_g/E with opposite residues a at A=t_0+g and −a at B=t_0, as in Section1. Its reflection has a fixed point

    x=t_0−g,

since 2x=2t_0+g=A+B and 3g=0. The point x belongs to the same branch coset G and differs from A and B. Thus C'/E ramifies with index three at x, but T_g/E is unramified there.

Let V be the connected common Kummer cover obtained by adjoining all the cubic roots for these auxiliaries, as well as w. It is abelian of exponent three over E. At each point its tame local inertia has order at most three, because the residue field is algebraically closed. It has exactly order three at every branch point of C' and no new branch point. Consequently V→C' is étale, by the tame local ramification calculation.

The composite V→C also has odd geometric Galois closure. Indeed C'→C is an E[3]-torsor. Adjoining all conjugates of the finitely many cubic Kummer extensions under that group gives a normal extension whose kernel is an elementary abelian 3-group and whose quotient is E[3]. Thus A.3 allows any alleged collision on C to lift to a collision on V after a finite extension of constants.

## 4. Recover the original character, including the unramified residual part

The map V→E is Galois and has full index three along the nonempty branch set. By A.21, the lifted collision has equal E-images. For each auxiliary T_g, the point x from Section3 has precisely the ambient ramification required in Section2. Therefore both elliptic reflection quotients force equal T_g-images.

Let f_g be the Kummer functions chosen for all the auxiliaries. Identity(1), over every branch coset, says that

    R=F / product_g f_g

has all valuations divisible by three. Its cubic root defines an unramified cyclic cover H_0/E or a split trivial cover. Take a connected component; it has genus one. This cover is already a subcover of V. Since H_0/E is unramified and V/E ramifies with index three, V→H_0 has a fibre all of whose ramification indices are divisible by three. A.21 gives equal H_0-images too.

A distinct pair on C has distinct images on C', since C'→C is a morphism. If their common E-image were a branch point of C', the full cubic ramification would give a single C'-point, impossible. We may therefore compare all the Kummer characters in their common unramified fibre. The character of C' is the product of the auxiliary characters and the residual character. All auxiliary and residual images have just been proved equal, so the C'-images are equal, a contradiction. This proves A1 for C over every finite constant extension.

This also proves the original exact-order-three branch family directly: for D={0,d,2d}, take residue vectors (1,−1,0) and (0,−1,1), whose sum is (1,1,1) modulo three. Each omitted point is fixed by the corresponding reflection. This smaller construction needs no multiplication pullback. The finite-packet results A.29c–A.29g remain correct independent evidence, but their remaining high-order case is unnecessary for A1 in that family once this construction is accepted.

## 5. Elementary abelian covers and spreading

Let C/E have group G=(Z/3)^r and genus at least two. For each nontrivial character chi:G→Z/3, its quotient C_chi/E is cyclic cubic. If it is ramified, its genus is at least two and the cyclic theorem gives equal quotient images. If it is unramified, C_chi has genus one and C→C_chi is ramified Galois with all branch indices three, so A.21 gives the same equality. The original map C→E likewise gives equal E-images.

Fix P,Q in the same G-orbit and write Q=gP, with inertia I=Stab(P). Equality in each quotient means g lies in ker(chi)I. Characters of the elementary abelian quotient G/I separate its elements, so g lies in I and P=Q. This includes branch fibres without an assumption that the product of quotient maps is a closed immersion.

Over a field finitely generated over F2, first make a finite extension of the base field to define all maps and the action; this extension need not be a constant extension. Spread over a finite-type base and shrink to preserve smoothness, genera, the tame group action, and ordinariness when the ordinary proof is used. A.8 specializes a collision to a finite-field fibre, where the proved theorem excludes it. For an open hyperbolic subcurve, functoriality to the compactification finishes.

## Scope and the next exact limitation

The crucial genus calculation uses cubic degree. A two-point cyclic e-cover of an ordinary elliptic curve, with e any odd prime, has genus e and the same reflection calculation gives quotient genus (e−1)/2. When e>3 this quotient need not be elliptic or supersingular, so A.21 alone no longer gives equality of its images. The proof does not settle all odd-degree covers of ordinary elliptic curves, all cyclic 3-power covers, or all characteristic-two hyperelliptic curves. It settles every cyclic degree-three and elementary abelian exponent-three elliptic cover. The earlier universal A1 remainder must be updated with this positive subclass, not removed.
