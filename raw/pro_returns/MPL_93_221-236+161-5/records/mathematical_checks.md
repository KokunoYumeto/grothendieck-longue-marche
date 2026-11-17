# Independent mathematical checks

## Scope and conventions

This is a support proof record, not a transcription, an emendation, or a statement of what any manuscript contains. It uses only the abstract hypotheses supplied for these checks. No manuscript, context file, or image was consulted to prepare it. References at the end are background pointers; the calculations and qualifications below are independent verification.

Complexes are cohomological: differentials have degree `+1`. The shift convention is

\[
(C[1])^n=C^{n+1},\qquad d_{C[1]}=-d_C.
\]

For complexes of sheaves of modules over a commutative ring sheaf \(\mathcal R\), write

\[
H^n=\underline{\operatorname{Hom}}_{\mathcal R}^{\,n}(K',K'')
=\prod_j\underline{\operatorname{Hom}}_{\mathcal R}(K'^j,K''^{j+n}),
\qquad
D(h)=d''h-(-1)^n h d'.
\]

Thus \(D(h)=d''h+hd'\) when \(|h|=-1\). The tensor differential is

\[
d(l\otimes x)=d_Ll\otimes x+(-1)^{|l|}l\otimes d_Kx.
\]

The construction also applies to sheaves of abelian groups, by taking \(\mathcal R=\underline{\mathbf Z}\).

## 1. An additive torsor and a canonical derived roof

### 1.1 Hypotheses and the extension attached to a torsor

Let \(G\) be a sheaf of abelian groups, let \(P\) be a \(G\)-torsor, and suppose that

\[
k:G\longrightarrow H^{-1}
\]

is additive, while

\[
u:P\longrightarrow Z^0H
\]

is a map of sheaves of sets satisfying

\[
u(p+g)-u(p)=Dk(g)=d''k(g)+k(g)d'. \tag{1}
\]

Let \(\mathbf Z[P]\) be the free abelian sheaf on \(P\), and form the following quotient in sheaves of abelian groups:

\[
\bar G=\bigl(G\oplus\mathbf Z[P]\bigr)\big/
\left\langle(-g,[p+g]-[p])\right\rangle.
\]

Write \(i(g)\) for the image of \((g,0)\), and \(j(p)\) for the image of \((0,[p])\). Then

\[
j(p+g)=j(p)+i(g).
\]

There is an augmentation \(\epsilon:\bar G\to\underline{\mathbf Z}\) with \(\epsilon i=0\) and \(\epsilon j(p)=1\). Locally choose \(p_0\in P\). The formula

\[
i(g)\longmapsto(g,0),\qquad
j(p_0+g)\longmapsto(g,1)
\]

identifies \(\bar G\) with \(G\oplus\underline{\mathbf Z}\). It follows that

\[
0\longrightarrow G\xrightarrow{i}\bar G
\xrightarrow{\epsilon}\underline{\mathbf Z}\longrightarrow0 \tag{2}
\]

is exact and that \(j\) identifies \(P\) with \(\epsilon^{-1}(1)\). The definition of \(\bar G\) uses no choice; a local section is used only to prove its properties.

### 1.2 The chain map

Define

\[
v:\bar G\longrightarrow Z^0H,
\qquad
v(j(p))=u(p),\quad v(i(g))=Dk(g).
\]

Equation (1) says precisely that these prescriptions annihilate the defining relations. They take values in cycles because \(u(p)\) is a cycle and \(D^2=0\).

Put \(L=[G\xrightarrow{i}\bar G]\), in degrees \(-1,0\). Then

\[
f:L\longrightarrow H,\qquad f^{-1}=k,\quad f^0=v
\]

is a chain map: its sole nontrivial chain condition is \(vi=Dk\). The augmentation gives a quasi-isomorphism

\[
\epsilon:L\longrightarrow\underline{\mathbf Z}[0].
\]

### 1.3 The locally split contraction and the flatness issue

On an open object where \(p_0\in P\), define

\[
s_{p_0}(n)=n j(p_0),\qquad
h_{p_0}^0(b)=i^{-1}\bigl(b-\epsilon(b)j(p_0)\bigr),\qquad
h_{p_0}^{-1}=0.
\]

Here \(s_{p_0}:\mathbf Z[0]\to L\) is a chain map, \(h_{p_0}\) has degree \(-1\), and direct computation gives

\[
\epsilon s_{p_0}=1,\qquad
d_Lh_{p_0}+h_{p_0}d_L=1_L-s_{p_0}\epsilon. \tag{3}
\]

Consequently \(\epsilon\) is locally a chain homotopy equivalence, not merely a quasi-isomorphism. After tensoring with any complex \(K\), the homotopy \(h_{p_0}\otimes1\) still satisfies (3): the two terms involving \(d_K\) cancel by the tensor signs. Therefore

\[
\epsilon\otimes1:\operatorname{Tot}(L\otimes_{\mathbf Z}K)
\longrightarrow K \tag{4}
\]

is locally a homotopy equivalence and hence a quasi-isomorphism. No flatness of \(G\), \(\bar G\), or \(K\), and no K-flat replacement, is needed for this particular assertion. This remains true for unbounded \(K\); the complex \(L\) has only two terms, so its tensor totalization has only two summands in each degree.

This is a special feature of the locally split augmentation. It is not a claim that an arbitrary quasi-isomorphism can be tensored with an arbitrary complex without a flatness condition.

### 1.4 Evaluation and the roof

Evaluation of \(f\) gives the chain map

\[
\operatorname{ev}(f):\operatorname{Tot}(L\otimes_{\mathbf Z}K')\longrightarrow K''.
\]

In degree \(n\), its formula is

\[
(b\otimes x,g\otimes y)\longmapsto v(b)(x)+k(g)(y),
\quad x\in K'^n,\quad y\in K'^{n+1}.
\]

For the second summand the chain condition is exactly

\[
v(i(g))(y)-k(g)d'(y)=d''k(g)(y),
\]

which explains the signs. Thus the desired morphism is the roof

\[
\Phi:
K'\xleftarrow[\sim]{\epsilon\otimes1}
\operatorname{Tot}(L\otimes_{\mathbf Z}K')
\xrightarrow{\operatorname{ev}(f)}K''. \tag{5}
\]

When the complexes and the values of \(u,k\) are \(\mathcal R\)-linear, the middle complex has its \(\mathcal R\)-action on the \(K'\) factor, and (5) is a roof in \(D(\mathcal R)\). The tensor product displayed here is over \(\mathbf Z\); it does not require \(L\) to be an \(\mathcal R\)-complex. Equivalently one may use \(\mathcal R\otimes_{\mathbf Z}L\), which is again locally homotopy equivalent to \(\mathcal R[0]\).

All constructions are natural under compatible morphisms of the entire torsor and complex data. A local section \(p\) gives a local inverse to the left arrow, and the resulting local representative of \(\Phi\) is \(u(p)\). Its change under translation is the specified homotopy \(k(g)\).

This does not assert that local morphisms in a derived category glue uniquely. The explicit roof, rather than such a uniqueness assertion, constructs the global morphism.

## 2. Hom, RHom, and the limits of canonicality

The ordinary internal Hom complex is enough for (5). No identification with derived internal Hom is used. To replace it by \(R\underline{\operatorname{Hom}}\), use an appropriate derived replacement and the derived tensor–Hom adjunction. A K-injective replacement of the target computes derived internal Hom. A bounded finite locally free source is another sufficient condition for its ordinary internal Hom complex to compute the derived one. Such hypotheses must not be silently assumed for arbitrary complexes.

The construction is canonical relative to \((G,P,u,k)\). Equation (1) alone does not determine \(k\): one may add an additive map

\[
z:G\longrightarrow Z^{-1}H.
\]

Moreover, such a change can change the global derived morphism. The difference of the maps \(L\to H\) factors through

\[
L\longrightarrow G[1]\xrightarrow{z}H,
\]

where the first map is the identity on \(G\) in degree \(-1\) and zero in degree \(0\).

For an explicit example, take a nontrivial \(G\)-torsor \(P\), \(K'=\mathbf Z[0]\), \(K''=G[1]\), and \(u=0\). Both \(k=0\) and \(k=\mathrm{id}_G\) satisfy (1). The former gives zero. The latter gives the connecting morphism

\[
\delta:\mathbf Z[0]\longrightarrow G[1]
\]

of (2), which is nonzero when its extension class is nonzero. For sign precision, use the mapping-cone convention

\[
\operatorname{Cone}(i)^n=\bar G^n\oplus G^{n+1},
\quad d(b,a)=(d_{\bar G}b+i(a),-d_Ga).
\]

Then \(L=\operatorname{Cone}(i)\), and its projection to \(G[1]\) is the displayed map with positive identity in degree \(-1\). This fixes the connecting-map sign without requiring a separate convention for a Čech representative of the torsor class.

Nor does (5) automatically give a quasi-isomorphism: a trivial torsor may have \(u\) equal to any chain map, including zero. If the local maps \(u(p)\) are quasi-isomorphisms, that extra hypothesis does imply that \(\Phi\) is an isomorphism in the derived category, since the cohomology sheaves of its cone then vanish locally.

A map from the coefficient unit to derived Hom is also not generally a quasi-isomorphism. For nonzero \(\mathcal R\), take

\[
K'=K''=\mathcal R^{\oplus2}[0].
\]

The identity comparison corresponds to the scalar map

\[
\mathcal R[0]\longrightarrow
R\underline{\operatorname{Hom}}_{\mathcal R}(K',K'')
=\operatorname{Mat}_2(\mathcal R)[0],
\qquad r\longmapsto rI_2,
\]

which is not a quasi-isomorphism. Thus a displayed map \(\mathcal O_X\to\widetilde{R\operatorname{Hom}}(K',K'')\) must not be strengthened to an isomorphism without an additional argument, even if a comparison \(K'\to K''\) is already an isomorphism.

## 3. Square-zero geometric application

### 3.1 Hypotheses and the coefficient category

Let \(T_0\hookrightarrow T\) be a closed immersion with base ideal \(\mathcal I\) satisfying \(\mathcal I^2=0\). Let \(X_a/T\) be smooth lifts with fixed identifications

\[
X_a\times_T T_0=X_0.
\]

Use the common underlying topological space of the nilpotent thickenings. Write

\[
\mathcal R=f^{-1}\mathcal O_T,\quad
\mathcal J=f^{-1}\mathcal I,\quad
\mathcal R_0=\mathcal R/\mathcal J,\quad
\mathcal A_a=\mathcal O_{X_a},\quad
\mathcal A_0=\mathcal O_{X_0}.
\]

Put \(K_a=\Omega^\bullet_{\mathcal A_a/\mathcal R}\) and \(K_0=\Omega^\bullet_{\mathcal A_0/\mathcal R_0}\). The differentials are \(\mathcal R\)-linear, not generally \(\mathcal A_a\)-linear: for example \(d(ax)=a\,dx+x\,da\). Thus the comparison belongs to \(D(\mathcal R)\), not automatically to a derived category of \(\mathcal O_X\)-modules.

Smoothness supplies the flatness and local formal lifting used here. Its flatness, together with the locally free modules of relative forms, identifies canonically

\[
\mathcal J K_a^n\simeq
\mathcal J\otimes_{\mathcal R_0}K_0^n.
\]

Let

\[
E=\mathcal J\otimes_{\mathcal R_0}K_0,
\qquad d_E=1\otimes d_0.
\]

There are chain maps

\[
\rho_a:K_a\to K_0,\qquad
\lambda_a:E\hookrightarrow K_a,
\qquad \rho_a\lambda_a=0. \tag{6}
\]

The chain-map assertion for \(\lambda_a\) uses that relative differentiation kills sections from the base: \(d(\mathcal J K_a)\subseteq\mathcal J K_a\). A square-zero ideal on the total space, without this differential-stability property, is not the same hypothesis.

### 3.2 The isomorphism torsor and its additive group

Let \(P_{ab}\) denote the sheaf of \(\mathcal R\)-algebra isomorphisms

\[
p:\mathcal A_a\xrightarrow{\sim}\mathcal A_b
\]

reducing to the identity of \(\mathcal A_0\). This is algebra-map notation: geometrically its maps go from \(X_b\) to \(X_a\). The local lifting property of smooth algebras gives local such maps. A lifted map inducing the identity on the common reduction is an isomorphism: it also induces the identity on the canonically identified square-zero ideals, so the short exact sequences of the two algebras prove bijectivity.

All these isomorphism sheaves are torsors under the same additive sheaf

\[
G=\operatorname{Der}_{\mathcal R_0}
\left(\mathcal A_0,\mathcal J\otimes_{\mathcal R_0}\mathcal A_0\right).
\]

The action is

\[
(p+g)(a)=p(a)+g(\bar a),
\]

using the canonical inclusion of the target ideal. The square-zero condition verifies multiplicativity. Every difference of two lifts is a derivation, and composition of infinitesimal changes is addition because such a derivation annihilates the ideal.

Let \(u_{ab}(p):K_a\to K_b\) be the induced de Rham map. Then

\[
\rho_bu_{ab}(p)=\rho_a,\qquad
u_{ab}(p)\lambda_a=\lambda_b. \tag{7}
\]

### 3.3 Contraction, its independence, and the homotopy equation

For \(g\in G\), contraction gives an \(\mathcal R_0\)-linear map of degree \(-1\)

\[
c_g:K_0\longrightarrow E,
\]

determined by \(c_g(a)=0\), \(c_g(da)=g(a)\), and the graded derivation rule. Explicitly,

\[
c_g(a_0\,da_1\wedge\cdots\wedge da_n)
=\sum_{i=1}^n(-1)^{i-1}a_0g(a_i)
\,da_1\wedge\cdots\widehat{da_i}\cdots\wedge da_n.
\]

Define the degree \(-1\), \(\mathcal R\)-linear map

\[
k_{ab}(g)=\lambda_b c_g\rho_a:K_a\longrightarrow K_b. \tag{8}
\]

Formula (8) is independent of any choice of \(p\), and is additive in \(g\). If one first chooses \(p\) and transports an infinitesimal contraction on the target, it gives the same formula. Concretely, contraction has image in \(\mathcal J K_b\) and annihilates \(\mathcal J K_b\); changing \(p\) changes \(u(p)\) by a map into that ideal, so the transported contraction is unchanged.

Let \(t_g=d_Ec_g+c_gd_0\). The first-order expansion, or the Cartan identity checked on functions and their differentials, gives

\[
u_{ab}(p+g)-u_{ab}(p)
=\lambda_b t_g\rho_a
=d_bk_{ab}(g)+k_{ab}(g)d_a. \tag{9}
\]

For completeness, the left-hand difference is a degree-zero derivation with values in the square-zero ideal of forms, where coefficients act through reduction: the quadratic difference term vanishes. The same is true of \(d_Ec_g+c_gd_0\). They agree on functions, where both give \(g\), and commute with the differential, so they agree on functions and their differentials and hence on all forms. No division or characteristic-zero assumption is involved.

Equations (8)–(9) supply the additive homotopy datum in Section 1. Since each local \(u(p)\) is a chain isomorphism, the resulting derived comparison \(\Phi_{ab}:K_a\to K_b\) is an isomorphism.

### 3.4 Transitivity: a chain-level verification

Transitivity is verified here for these actual isomorphism torsors and normalized contraction data, not for arbitrary unrelated choices of homotopies.

Composition of algebra isomorphisms gives

\[
P_{bc}\times P_{ab}\longrightarrow P_{ac},\qquad(q,p)\longmapsto qp,
\]

and

\[
(q+h)(p+g)=qp+(h+g). \tag{10}
\]

The reason is that all the isomorphisms induce the identity both on the reduction and on the identified square-zero ideal. From (6)–(8), one obtains the exact equalities

\[
u_{bc}(q)k_{ab}(g)=k_{ac}(g),\qquad
k_{bc}(h)u_{ab}(p)=k_{ac}(h). \tag{11}
\]

Every composition of two first-order maps \(k\) or \(Dk\) is zero, because the inner factor has image in \(\lambda_b(E)\) and the outer factor passes through \(\rho_b\), with \(\rho_b\lambda_b=0\). In particular,

\[
k_{bc}(h)k_{ab}(g)=0. \tag{12}
\]

Let \(L_{ab}=[G\to\bar G_{ab}]\) be the construction of Section 1. There is a chain map

\[
\mu:L_{bc}\otimes_{\mathbf Z}L_{ab}\longrightarrow L_{ac}
\]

defined as follows. In degree zero, use the bilinear map determined on generators by

\[
\begin{aligned}
j(q)\otimes j(p)&\longmapsto j(qp),\\
i(h)\otimes j(p)&\longmapsto i(h),\\
j(q)\otimes i(g)&\longmapsto i(g),\\
i(h)\otimes i(g)&\longmapsto0.
\end{aligned}
\]

These assignments respect the torsor relations by (10). In degree \(-1\), set

\[
\mu(h\otimes b)=\epsilon(b)h,\qquad
\mu(a\otimes g)=\epsilon(a)g,
\]

for \(a\in\bar G_{bc}\), \(b\in\bar G_{ab}\). In degree \(-2\), set \(\mu=0\). The degree \(-1\) chain condition follows from \(\mu(i(h)\otimes b)=i(\epsilon(b)h)\) and its other-factor analogue. In degree \(-2\), the differential is

\[
h\otimes g\longmapsto i(h)\otimes g-h\otimes i(g),
\]

whose image under \(\mu\) is zero because \(\epsilon i=0\). Also

\[
\epsilon_{ac}\mu=\epsilon_{bc}\otimes\epsilon_{ab}. \tag{13}
\]

Let \(f_{ab}:L_{ab}\to\underline{\operatorname{Hom}}(K_a,K_b)\) be the chain maps from Section 1. Ordinary composition of homogeneous maps has differential

\[
D(vw)=D(v)w+(-1)^{|v|}vD(w).
\]

Equations (11), their differentials, and (12) prove, on the displayed generators and in every degree, the strict equality

\[
f_{ac}\mu=\operatorname{comp}(f_{bc}\otimes f_{ab}). \tag{14}
\]

For example, the two mixed degree-zero cases use \(Dk_{bc}(h)u_{ab}(p)=Dk_{ac}(h)\) and \(u_{bc}(q)Dk_{ab}(g)=Dk_{ac}(g)\); the case with two \(i\)'s uses \(Dk\,Dk=0\). The degree \(-1\) cases use (11) and \(kDk=Dkk=0\), and the degree \(-2\) case uses (12).

The composite \(\Phi_{bc}\Phi_{ab}\) can be represented on

\[
L_{bc}\otimes L_{ab}\otimes K_a,
\]

with left map the two augmentations and right map successive evaluation. This is a legitimate comparison roof because each augmentation remains a local homotopy equivalence after any of these tensorings. Equations (13)–(14), after tensoring \(\mu\) with \(K_a\), give a map of this roof to the roof for \(\Phi_{ac}\). Hence

\[
\boxed{\Phi_{bc}\Phi_{ab}=\Phi_{ac}.}
\]

For \(a=b\), the identity algebra isomorphism is a global section of \(P_{aa}\); its representative is \(1_{K_a}\), so \(\Phi_{aa}=1\). This also proves that the opposite comparison is the inverse. The argument establishes equality of global derived morphisms, rather than trying to infer it from equality after restriction to an open cover.

The scope is important: fixed identifications of the special fibres, the actual composition of their isomorphism torsors, and the specified contraction homotopies are part of the data. Arbitrarily adding closed maps to the homotopies in Section 2 need not preserve this normalized comparison.

## 4. Twisting a possibly nontrivial torsor by a trivial torsor

Let \(Q\) be a right \(G\)-torsor, write \(G''=\operatorname{Aut}_G(Q)\), and let \(U\subseteq G''\). The group \(U\) acts on the left of \(Q\) and commutes with its right \(G\)-action. For a right \(U\)-torsor \(R\), use the contracted-product convention

\[
P=R\times^UQ,\qquad (ru,q)\sim(r,uq).
\]

If \(R\) is trivial, a section \(r\) gives a \(G\)-equivariant isomorphism

\[
\theta_r:Q\xrightarrow{\sim}P,\qquad q\longmapsto[r,q].
\]

Consequently

\[
\Psi_r:\operatorname{Aut}_G(P)\xrightarrow{\sim}G'',
\qquad a\longmapsto\theta_r^{-1}a\theta_r.
\]

Changing the section to \(ru\) gives \(\theta_{ru}=\theta_r u\), hence

\[
\Psi_{ru}(a)=u^{-1}\Psi_r(a)u.
\]

Thus the isomorphism with \(G''\) is noncanonical in general. Intrinsically,

\[
\operatorname{Aut}_G(P)\simeq R\times^U G'',
\]

where \(U\) acts on \(G''\) by conjugation. Local identifications by sections of \(R\) prove this formula and its stated transition rule.

No triviality of \(Q\) is needed. Triviality of \(R\) proves \(P\simeq Q\), not \(P\simeq G\). In general \(\operatorname{Aut}_G(Q)\) is the inner form determined by \(Q\), and identifying it with \(G\) needs further information. A trivialization of \(Q\) is sufficient. When \(G\) is abelian, \(\operatorname{Aut}_G(Q)\simeq G\) is canonical even for nontrivial \(Q\), because translations are equivariant and independent of a base point.

## 5. Nonabelian restriction: arbitrary subgroups first

### 5.1 Conventions

Let \(\Gamma\) act on a group \(A\) by automorphisms. A cocycle satisfies

\[
z(\gamma\delta)=z(\gamma)\,\gamma(z(\delta)),
\]

and the equivalence convention is

\[
z^a(\gamma)=a^{-1}z(\gamma)\gamma(a).
\]

For topological groups, use continuous actions and cocycles, and impose the usual quotient-topology hypotheses when passing to a quotient. Nothing in the arbitrary-subgroup argument below requires normality.

### 5.2 Neutral fibre for an arbitrary subgroup

Let \(\pi\subseteq\Gamma\) be any subgroup. Define

\[
Z^1(\Gamma,\pi;A)=\{z\in Z^1(\Gamma,A):z(n)=1\text{ for all }n\in\pi\}.
\]

Every class in the neutral fibre of restriction can be conjugated to a representative in this set: being neutral after restriction means exactly that a single element of \(A\) trivializes the restricted cocycle. If two normalized representatives differ by \(a\in A\), then on \(\pi\)

\[
1=a^{-1}n(a),
\]

so \(a\in A^\pi\). Conversely, every such \(a\) preserves the normalization. Therefore there is a natural bijection of pointed sets

\[
\boxed{
\operatorname{res}^{-1}(1)
\simeq Z^1(\Gamma,\pi;A)/A^\pi.
} \tag{15}
\]

Calling this the neutral fibre avoids treating a general nonabelian \(H^1\) as a group.

### 5.3 Every represented fibre, using twisting

Fix \(z_0\in Z^1(\Gamma,A)\), and give the underlying group \(A\) the twisted action

\[
\gamma\star a=z_0(\gamma)\gamma(a)z_0(\gamma)^{-1}.
\]

Denote this group with action by \({}_{z_0}A\). The map

\[
w(\gamma)\longmapsto w(\gamma)z_0(\gamma)
\]

is a bijection between twisted and original cocycles, respects their equivalence relations, and sends the twisted neutral class to \([z_0]\). It commutes with restriction. Thus the fibre through \([z_0]\) is, after this choice of representative, parametrized by

\[
Z^1(\Gamma,\pi;{}_{z_0}A)/({}_{z_0}A)^\pi. \tag{16}
\]

Full injectivity of restriction requires (16) to be a singleton for every represented fibre. Vanishing of (15) alone only proves that the neutral fibre is a singleton. For abelian \(A\), twisting does not change the action and restriction is a group homomorphism, so the neutral-fibre condition already implies injectivity; the distinction matters for nonabelian coefficients.

### 5.4 Inflation–restriction requires normality

Now additionally assume \(\pi\triangleleft\Gamma\), and write \(Q=\Gamma/\pi\). The group \(A^\pi\) is \(\Gamma\)-stable, and its action factors through \(Q\). If \(z\) is normalized on \(\pi\), then

\[
z(\gamma n)=z(\gamma),\qquad
z(n\gamma)=n(z(\gamma)).
\]

Because \(n\gamma=\gamma n'\) for some \(n'\in\pi\), the second expression equals \(z(\gamma)\). Hence the values lie in \(A^\pi\), and the first equality makes the cocycle descend to \(Q\). The equivalence relation descends precisely through \(A^\pi\). This proves

\[
H^1(Q,A^\pi)\hookrightarrow H^1(\Gamma,A),
\qquad
\operatorname{image}=\operatorname{res}^{-1}(1).
\]

In particular,

\[
\operatorname{res}^{-1}(1)=\{1\}
\quad\Longleftrightarrow\quad H^1(Q,A^\pi)=\{1\}. \tag{17}
\]

For full injectivity, apply the same normal-subgroup calculation to every twisted action; the corresponding condition is

\[
H^1\bigl(Q,({}_{z_0}A)^\pi\bigr)=\{1\}
\quad\text{for every }z_0\in Z^1(\Gamma,A).
\]

If \(\pi\) is not known to be normal, expressions (15)–(16) remain valid, but \(\Gamma/\pi\) need not be a quotient group, and \(A^\pi\) need not be \(\Gamma\)-stable. Knowing that \(\Gamma\) is an extension of \(\mathbf Z\) by some other subgroup \(\widetilde\pi\) does not establish normality of \(\pi\). That hypothesis must be proved separately before invoking (17).

### 5.5 Elementary counterexample and the role of Frobenius

Take \(\Gamma=\pi\times\mathbf Z\) and \(A=L^\times\), with trivial action and \(L^\times\ne\{1\}\). For every \(a\in L^\times\),

\[
z_a(\gamma,n)=a^n
\]

is a cocycle trivial on \(\pi\). Because the action is trivial and \(L^\times\) is abelian, distinct \(a\)'s give distinct classes. Thus

\[
H^1(\mathbf Z,L^\times)=\operatorname{Hom}(\mathbf Z,L^\times)
\simeq L^\times,
\]

and restriction is not injective. One may take \(L=\mathbf Q_p\) and \(a=p\). With discrete \(\mathbf Z\), these cocycles satisfy continuity automatically. This disproves any vanishing claim based only on the abstract quotient \(\mathbf Z\) and these trivial-action coefficients; it does not by itself decide a more specific arithmetic coefficient problem.

For an action of \(\mathbf Z\) generated by an automorphism \(\sigma\), a cocycle is determined by \(b=z(1)\), with equivalence

\[
b\sim x^{-1}b\sigma(x).
\]

For multiplicative field coefficients this yields

\[
H^1(\mathbf Z,L^\times)
=L^\times/\{\sigma(x)/x:x\in L^\times\}.
\]

Consequently vanishing requires surjectivity of \(x\mapsto\sigma(x)/x\). The assertion does not follow simply because \(\sigma\) is called a Frobenius or acts semilinearly. For example, if \(\sigma\) preserves a valuation \(v\), then

\[
v(\sigma(x)/x)=0.
\]

Every element of nonzero valuation gives a nonneutral class. A positive vanishing result must use the actual field, coefficient group, action, and any further restrictions on allowable classes. A Lang-type conclusion cannot be imported without its hypotheses.

## Background pointers, not manuscript evidence

- Stacks Project, [Tag 03AJ](https://stacks.math.columbia.edu/tag/03AJ): torsors under an abelian sheaf and their extension/cohomology construction.
- Stacks Project, [Tag 08J7](https://stacks.math.columbia.edu/tag/08J7): derived internal Hom and tensor–Hom adjunction.
- Stacks Project, [Tag 0FKL](https://stacks.math.columbia.edu/tag/0FKL): the sheaf-theoretic relative de Rham complex and its base-module linearity.
- Stacks Project, [Tag 01UP](https://stacks.math.columbia.edu/tag/01UP): the square-zero calculation relating differences of lifts to derivations.

These links support the surrounding standard constructions. In particular, the locally split tensor argument, the chain-level proof of geometric transitivity, the change-of-section calculation for automorphism groups, and the relative-cocycle classifications above are recorded as explicit independent arguments rather than quotations or claims about a source text.
