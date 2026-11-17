# Actual negative-GT0 V4 identities and the canonical Fox defect

Research, checkpoint27. This is a focused return to the full Main-A marked generation gate. It uses the actual full negative-GT0 canonical word, not a generic ring solution or a finite-head example. The joint identities below give a stronger description of the actual obstruction module, but do not prove its vanishing or the Fox unit. No claim is made for a general P-involution without canonical swap duality.

## 1. Exact actual data and coefficient scope

Let F=hat F(x,y), let alpha be the actual pure negative involution, and retain the actual f and its canonical u:

alpha(x)=x^-1, alpha(y)=f^-1 y^-1 f,
alpha(f)=f^-1, u=f alpha(u).

For a negative GT0 involution the established canonical duality is iota(u)=u^-1, where iota interchanges x and y. Set

w=u^-1 y u,
psi(x)=x, psi(y)=w,
v=Inn(u^-1) iota,
tau=alpha v.

The already proved group identities give

v²=alpha²=tau²=1, alpha v=v alpha,
v(x)=w, v(w)=x,
alpha psi=psi c, v psi=psi iota, tau psi=psi(c iota),

where c inverts both free generators. Thus V=<alpha,v> is the actual Klein four group: their three nonidentity integral homology actions are respectively -I, swap and negative-swap. We use this action on F and on H=closure<x,w>. In particular H is stable under the whole V.

Fix any coefficient prime p and Lambda=Z_p[[F]], with the full group F retained. Every map below is continuous. Finite V-stable group heads are cofinal, by intersecting the finitely many V-translates of an open normal subgroup. Nothing is replaced by the maximal pro-p quotient of F.

Use continuous left Fox derivatives and row Jacobians:

g-1=g_x(x-1)+g_y(y-1),
(gh)_i=g_i+g h_i,
J_phi=(partial_j phi(x_i))_(i,j),
J_(phi composed with rho)=phi(J_rho) J_phi.

The augmentation ideal is free as a compact left Lambda-module on x-1,y-1. Coefficient row vectors therefore act by right multiplication by these matrices.

## 2. Full joint Fox identities

Write a=u_x, b=u_y, and put

A_f=1+(y-1)f_y,
B=1+(y-1)b,
P=u^-1(y-1)a,
D=u^-1 B,
E=u^-1(1+(x-1)a),
Q=u^-1(x-1)b.

Direct differentiation gives the actual matrices

J_psi = [[1,0],[P,D]],
J_v = [[P,D],[E,Q]],
J_alpha = [[-x^-1,0],[-f^-1 y^-1(y-1)f_x, -f^-1 y^-1 A_f]],
J_tau = alpha(J_v) J_alpha.

The duality and canonical-word equations additionally give, with no division by a Fox entry,

iota(a)=-u^-1 b, iota(b)=-u^-1 a,
(a,b)=(f_x,f_y)+f alpha((a,b)) J_alpha.

The entire equivariance system is

alpha(J_psi) J_alpha = diag(-x^-1,-w^-1) J_psi,
v(J_psi) J_v = [[0,1],[1,0]] J_psi,
tau(J_psi) J_tau = [[0,-w^-1],[-x^-1,0]] J_psi.

The third equation is the product of the first two with the actual semilinear coefficient actions; it is not an independent relation that may be multiplied as if coefficients commuted. The actual commuting-action identity is

alpha(J_v) J_alpha = v(J_alpha) J_v.

Since v and alpha are automorphisms, their full matrices are units; for example v(J_v)J_v=I. The swap equation includes the two exact identities

v(P)P+v(D)E=1,
v(P)D+v(D)Q=0.

These make essential use of all four entries. They do not make D a scalar unit. Similarly triangular invertibility of J_alpha proves A_f is a unit, and the lower-right entry of the alpha equation is precisely

B=theta(B) A_f,
theta=Inn(yf) alpha,
theta²=1, theta(A_f)A_f=1.

Here (yf)alpha(yf)=1, so theta is the stated actual ring involution. This recovers the original full-head Fox equation inside the joint V4 system. It does not change it into a norm-one equation for B.

These formulas can also be derived without a matrix convention by differentiating alpha(w)=w^-1, v(w)=x and v(y)=u^-1xu individually. The displayed chain-rule convention fixes every product order. No arbitrary u or noncanonical derivative assignment is used.

## 3. The precise actual obstruction module carries the whole V action

Let

L_H=Lambda(x-1)+Lambda(w-1) in I_F,
C_p=I_F/L_H=ker(Z_p[[F/H]]->Z_p).

The last is the actual reduced compact coset module. H is closed, so this is the full profinite coset space, not a finite approximation. The free source Lambda² for the two marked columns has a genuine semilinear V action:

alpha(e_x)=-x^-1 e_x, alpha(e_w)=-w^-1 e_w,
v(e_x)=e_w, v(e_w)=e_x.

The relations alpha²=v²=[alpha,v]=1 follow literally from alpha(x)=x^-1, alpha(w)=w^-1 and v(x)=w. Sending these basis vectors to x-1,w-1 is equivariant, and its matrix is J_psi. Thus C_p has the actual quotient V action. Neither injectivity nor surjectivity of this marked map is assumed.

As already proved in the Fox baseline, the following are equivalent for even one chosen p:

B is a unit in the full Lambda;
J_psi is invertible;
C_p=0;
H=F.

Direct finiteness at the finite coefficient-ring heads converts a one-sided matrix inverse into a genuine inverse. The joint V action has not changed this criterion.

## 4. All three involutions have only the base coset fixed

This gives a new uniform strengthening of the earlier alpha-only coset test.

First H is a closed subgroup of the full free profinite F, hence projective. Its abelianization is exactly Zhat²: the map F_ab->H_ab from the two marked generators is onto, and its composite with H_ab->F_ab is the identity. Thus both maps are inverse. On H_ab the v and tau actions are respectively swap and negative-swap; their mod-two actions are the regular F2[C2] module.

For t=v or tau put E_(H,t)=H semidirect<t>. The actual ambient E_t=F semidirect<t> has self-centralizing involutions. For tau this is the established regular-pants result C43. For v it follows directly from v=Inn(u^-1)iota: the map sending the generator v to u^-1 iota identifies E_v with E_iota; the latter has the explicit full free-product presentation C2*Zhat. The full free-product involution/centralizer theorem gives the assertion. Every closed subgroup E_(H,t) inherits the real-projectivity property used in A82, with the same prescribed-class lifting consequence.

The split Lyndon--Hochschild--Serre calculation for H->E_(H,t)->C2 has only q=0,1 rows. The q=1 row is the regular two-dimensional mod-two module, so all its positive cohomology vanishes. The possible transgression into H²(C2,F2) is zero because the extension has the specified section. Therefore

dim_F2 H²(E_(H,t),F2)=1.

To turn this into a section count, take any finite list of distinct involution classes in E_(H,t). The prescribed-class real-projective lifting argument from A82 supplies degree-one characters taking independently chosen bits on those classes. The squares of the characters selecting individual classes restrict to independent nonzero degree-two classes on the corresponding C2 subgroups. They are therefore linearly independent in H²(E_(H,t),F2). Its dimension one permits at most one involution class; the displayed t gives one. This avoids assuming a proper embedding-problem solution or a free-product recognition theorem for E_(H,t).

For alpha, the existing canonical-image proof gives exactly three classes in E_(H,alpha), mapping bijectively to the three ambient classes. Its argument uses the three actual generating involutions and the same prescribed-class lifting property; it remains unchanged.

Now let t be alpha,v or tau and suppose gH is t-fixed in X=F/H. Then g^-1 t(g) belongs to H, and (g^-1 t(g))t is an involution of E_(H,t) lying in the ambient class of t. The preceding class comparison makes it H-conjugate to t. Adjusting g by that H-conjugator gives an element of the actual F-centralizer of t. That centralizer is trivial in all three cases. Consequently

X^alpha=X^v=X^tau={H}.

Thus the actual V4 action is free on X minus its selected base point. This assertion is about the full compact coset space; extra fixed points in a finite coset quotient are not being mistaken for full fixed cosets.

## 5. An induced compact V4 module, with the exact limitation

The preceding fixed-point statement yields a more explicit description than Tate acyclicity. F is finitely generated, so it has only countably many open normal subgroups, and X is compact metrizable. Choose decreasing V-invariant clopen neighborhoods U_n of the base point, with U_0=X and intersection the base point. Every shell U_n minus U_(n+1) is a compact zero-dimensional free V-space. It has a clopen transversal: choose disjoint translates of a small clopen neighborhood at each point, pass to the finite cover of the quotient, and refine that cover to a finite disjoint clopen partition before selecting a sheet.

Choose one such transversal T_n in each shell and let Y be the base point together with their union. Its complement is the union of the other open sheets, so Y is closed in X and is itself profinite. Multiplication gives a pointed V-equivariant homeomorphism

(V times Y)/(V times {base point}) -> X.

The map is a continuous bijection from a compact space to the Hausdorff X; every non-base orbit has exactly one selected representative. Let D_p=ker(Z_p[[Y]]->Z_p), with augmentation split by the base point. The universal property of free compact modules now gives

C_p is isomorphic, as a compact Z_p[V]-module, to
Z_p[V] tensor_(Z_p) D_p,

g tensor(y-base point) maps to gy-base point.

The finite V factor makes the tensor a finite direct sum of compact modules. This is an induced/coinduced module from the trivial subgroup. Its Tate cohomology vanishes in every degree for V and for all its subgroups. The description applies to the actual C_p and actual joint action, not to a manufactured ring example. At p=2 it strictly extends the earlier single-involution Tate statement.

The displayed transversal is not F-stable. The induced description is therefore over the constant finite-group ring Z_p[V], not over Lambda or the completed semidirect-product ring. It gives no Lambda-linear splitting and does not say D_p=0. The exact remaining unit statement is that this particular actual transverse module D_p vanishes, equivalently Y is only the base point, equivalently H=F. None of the section counts or the joint Jacobian identities above proves that conclusion.

## 6. Third-cusp information is retained, not replaced

Let z=(xy)^-1 be the actual third cusp. The swap component has the exact transport

v(z)=(xu)^-1 z (xu).

The corrected element e_v=(xu)v in E_v centralizes z and satisfies

e_v²=xy=z^-1.

This square is important: e_v is not an involution to which the one-section argument can simply be applied. Under E_v=E_iota it becomes x iota, exactly its full standard primitive loop. The product tau inverts the actual third cusp up to its genuine transported conjugator, as in the regular-pants theorem. None of these identities identifies xw with a unit power of the actual third cusp. In particular membership z in H would already imply H=F since x is in H; it is not an innocuous extra marking hypothesis.

Thus the actual third-cusp transport and V4 constraint remain present, but the missing marked generation/third-cusp implication is not inserted into the argument.

## 7. Assessment at the exact scope

The actual joint V4 action forces the canonical Fox cokernel to be an induced compact finite-group module and provides the complete coupled full-ring Jacobian identities. This is a genuine strengthening of the necessary obstruction structure. It does not prove B is a unit, construct a nonunit canonical u, or settle either main problem. It also does not extend the V4 conclusion to arbitrary pure P involutions lacking the proved GT0 canonical duality.

Dependencies are the established full proofs C35/C43, A82--A84, the exact canonical Fox baseline `work_A/actual_marked_Fox_unit_gate_15h.md`, and the alpha-only comparison `work_A/canonical_image_section_test_boundary21.md`. The real-projectivity/prescribed-class and free-product centralizer dependencies are used exactly at the already audited scope. No new recognition theorem, finite-group census, or pro-p substitute has been used.
