# C. Finite coverings

Throughout this part, all automorphisms of profinite groups are continuous. A peripheral structure means the full collection of conjugacy classes of maximal cusp inertia subgroups, with one common orientation multiplier. We write $\Gamma(S)$ for the orientation-preserving mapping class group with punctures permitted to permute, and $P\Gamma(S)$ for its pure subgroup. Its geometric closure in the appropriate outer automorphism group is denoted by $\Sigma(S)$. We use the established LM3 statements B.9, B.12, B.13 and E.7, without repeating their proofs. The new comparisons below concern §28, folios 179–183, scans 355–363; scans 355 and 356 were inspected, whereas scan 363 is available only in the supplied transcription.

### C.1. Refuted — Characteristicness of the index-two test covering

Let $G=\widehat F(x,y)$ be the tripod group, with peripheral classes $x,y,(xy)^{-1}$. The subgroup
$$
 V_2=\ker(G\longrightarrow C_2),\qquad x\longmapsto1,\quad y\longmapsto0,
$$
which corresponds to $z\mapsto z^2$, is normal but is not characteristic under loop-preserving automorphisms. The restriction homomorphism must therefore have source $\operatorname{Aut}_{\rm lac}(G;V_2)$, the open stabilizer of $V_2$. In contrast,
$$
 V_4=\ker(G\longrightarrow G^{\rm ab}/2G^{\rm ab})
$$
is characteristic. Its rank is five and its punctured-sphere type is $(0,6)$.

**Proof.** Interchanging the peripheral classes of $x$ and $y$ carries $V_2$ to the distinct kernel of $x\mapsto0,y\mapsto1$. This interchange is induced by an orientation-preserving homeomorphism of the tripod. The assertion about $V_4$ follows from functoriality of abelianization. Schreier's formula gives ranks $1+2(2-1)=3$ and $1+4(2-1)=5$. There are respectively four and six cusps, because the ramification indices above the three omitted points are $(2,1,2)$ and $(2,2,2)$; the Euler-characteristic formula then gives genus zero. All three nonzero maps $H_1(G,\mathbf F_2)\to C_2$ lie in one geometric $S_3$ orbit. Thus the stabilizer correction loses no cosets in the non-strict prediscretization comparison: every loop-preserving automorphism can first be adjusted by a geometric automorphism to stabilize $V_2$. This explains why Grothendieck expressly says “sans supposer $\pi'$ caract.” in the index-two example of scan 363. The characteristic hypothesis in the prompt cannot be imposed on that particular cover. $\square$

### C.2. Proved — The correctly typed deck-normalizer theorem

Let $V$ be an open normal subgroup of a center-free profinite surface group $G$, and suppose $C_G(V)=1$. Put $D=G/V$, viewed as a subgroup of $\operatorname{Out}(V)$ by conjugation. Then restriction gives an isomorphism
$$
 \operatorname{Aut}(G;V)\xrightarrow{\sim}
 \{a\in\operatorname{Aut}(V):[a]\in N_{\operatorname{Out}(V)}(D)\},
$$
and, after passing to outer automorphisms, an isomorphism
$$
 \operatorname{Out}(G;V)\xrightarrow{\sim}
 N_{\operatorname{Out}(V)}(D)/D.                         \tag{C.1}
$$
The same statements hold with loop-preserving automorphisms for the two covers in C.1, with the induced peripheral structures. Thus the prompt's normalizer modulo $D$ describes the **outer source**, not the image of a homomorphism with target $\operatorname{Aut}(V)$.

**Proof.** Conjugation identifies $G$ with a subgroup of $\operatorname{Aut}(V)$, by the centralizer hypothesis. This subgroup is exactly the inverse image of $D$ under $\operatorname{Aut}(V)\to\operatorname{Out}(V)$: both contain $\operatorname{Inn}(V)$ and have quotient $D$. An automorphism $a$ of $V$ normalizes this inverse image precisely when its outer class normalizes $D$. Conjugation by $a$ then defines the unique extension to $G$. Uniqueness also follows directly: if an automorphism of $G$ is the identity on $V$, then $g^{-1}\alpha(g)$ centralizes $V$ for every $g\in G$. The construction and its inverse are continuous. Quotienting by $\operatorname{Inn}(G)$ gives (C.1), because its restriction maps onto $D$ modulo $\operatorname{Inn}(V)$.

For the peripheral assertion, the inertia subgroups upstairs are the nontrivial intersections of conjugates of downstairs inertia with $V$. Downstairs inertia is recovered as the normalizer in $G$ of each such intersection. Boggi and Zalesskii (2019, Proposition 3.6) prove the required self-normalizer statement even for nonzero profinite powers of an algebraically simple element. Hence a peripheral automorphism upstairs which extends necessarily permutes the recovered downstairs inertia; the common exponent agrees under restriction. The same argument works for free pro-$2$ groups. $\square$

### C.3. Known — Coset injectivity holds for both test coverings

For $V_2$ use $A=\operatorname{Aut}_{\rm lac}(G;V_2)$ and let $B$ be the closure in $A$ of the corresponding discrete orientation-preserving stabilizer. For $V_4$ use the full loop-preserving group and its geometric closure. Let $A'=\operatorname{Aut}_{\rm lac}(V)$ and $B'$ be its geometric closure, including inner automorphisms. Then, for both test coverings,
$$
                         f^{-1}(B')=B.                 \tag{C.2}
$$
Consequently the restriction map on the oriented prediscretization coset spaces is injective.

The same injectivity statement holds for both free pro-$2$ test coverings, with geometric closure taken in the pro-$2$ outer automorphism group. More generally, the finite-$p$-subgroup normalizer equality used below holds in the genus-zero geometric pro-$p$ closure.

**Proof and reduction to the cited theorem.** The substantive external input is Boggi and Zalesskii (2025, Theorem A(iii), equivalently Theorem 4.3 in the version read): in the profinite completion of a residually finite, good group of finite virtual cohomological type, the normalizer of a finite $p$-subgroup is the closure of its discrete normalizer. Apply this with $p=2$ to the genus-zero mapping class group of the upstairs surface and the deck subgroup $D=C_2$ or $C_2^2$. The needed goodness follows inductively from the pure genus-zero Birman extensions by finitely generated free groups; these groups and their finite extensions have finite virtual cohomological type. This genus-zero application is also included in the source's discussion preceding §6.1. Genus-zero congruence identifies this completion with $\Sigma(V)$, so
$$
 N_{\Sigma(V)}(D)=\overline{N_{\Gamma(V)}(D)}.           \tag{C.3}
$$
The discrete normalizer descends to the discrete geometric stabilizer downstairs. To see this without assuming a choice of equivariant representatives, apply the discrete version of the proof of C.2. The extension preserves the oriented peripheral classes, so Dehn–Nielsen–Baer identifies it with a geometric mapping class downstairs. Conversely every liftable geometric mapping class lifts to this normalizer. Thus (C.1) identifies $N_{\Gamma(V)}(D)/D$ with the geometric stabilizer downstairs. Taking closures and using (C.3) proves that an element of $A$ whose restriction is in $B'$ already lies in $B$. The reverse inclusion follows by continuity of restriction. Finally apply LM3 B.13 to obtain coset injectivity.

For the pro-$p$ assertion, we check the completion issue explicitly. Put $G=\Gamma_{0,n}$ with labels allowed to permute, $P=P\Gamma_{0,n}$, and let $R$ be its geometric closure in $\operatorname{Out}(F_{n-1}^{(p)})$. Boggi (2020, Corollary 5.4(ii)) identifies the closure of $P$ with its full pro-$p$ completion $P^{(p)}$; his notation $\Gamma(S)$ is pure throughout that paper. The label action on the cusp classes is faithful, so
$$
 1\to P^{(p)}\to R\to S_n\to1
$$
is exact. The map $G\to R$ is injective because $P$ is residually $p$ and the label action detects every nonpure element.

The maps $P\to P^{(p)}$ induce cohomology isomorphisms for every finite continuous $\mathbf F_p[P^{(p)}]$-module. Here is the required goodness argument rather than an appeal to full profinite goodness. Induct on the number of punctures using the free Birman extensions, whose completed pro-$p$ sequences are exact by Boggi's Corollary 4.7 and Corollary 5.4(ii). A finitely generated free group and its free pro-$p$ completion have the same cohomology for these coefficients: both have cohomological dimension one, and a crossed homomorphism to a finite $p$-module extends continuously, since its graph lies in a finite $p$-group extension. The Lyndon–Hochschild–Serre comparison then proves the induction; the kernel cohomology modules are finite and carry the continuous quotient action supplied by the completed extension. A second comparison across the common finite quotient $S_n$ proves
$$
 H^i(R,M)\xrightarrow{\sim}H^i(G,M)
$$
for every finite continuous $\mathbf F_p[R]$-module $M$ and every $i$. The pure groups have finite classifying complexes and $G$ is virtually of that type, hence of type $\mathrm{FP}_{\infty}$. Group cohomology therefore commutes with filtered unions of these finite modules. Continuous profinite cohomology does also; every discrete $\mathbf F_p[R]$-module is the union of its finite-dimensional $R$-stable submodules. Thus the comparison holds for all discrete modules required by Boggi–Zalesskii (2025, Theorem A, or Theorem 4.3), not only finite ones. The same finite-type argument verifies finite virtual $p$-cohomological type.

That theorem applies to this arbitrary dense embedding $G\hookrightarrow R$, and gives $N_R(H)=\overline{N_G(H)}$ for every finite $p$-subgroup $H\subset G$. Taking $p=2$ and the relevant deck subgroup gives the pro-$2$ analogue of (C.3). Discrete descent and continuity now prove the asserted pro-$2$ injectivity, and also show that every geometric pro-$2$ normalizer of a deck subgroup descends geometrically. $\square$

The normalizer theorem is not a statement that every outer automorphism upstairs can be adjusted geometrically to normalize the deck group. That is the separate surjectivity condition below.

### C.4. Proved — A degree-three obstruction in the rational graded comparison

Let $\mathfrak o_r$ be the graded Lie algebra of special outer derivations of the free Lie algebra on $r$ generators over a characteristic-zero field. For the index-two cover, the degree-three deck-fixed subspace and geometric subspace satisfy
$$
 \dim\mathfrak o_{3,3}=6,\quad
 \dim\mathfrak o_{3,3}^{C_2}=4,\quad
 \dim\mathfrak p_{0,4,3}=2,\quad
 \dim(\mathfrak o_{3,3}^{C_2}+\mathfrak p_{0,4,3})=5.
                                                               \tag{C.4}
$$
For the degree-four cover,
$$
 \dim\mathfrak o_{5,3}=50,\qquad
 \dim\mathfrak o_{5,3}^{C_2^2}=17,\qquad
 \dim\mathfrak p_{0,6,3}=30,
                                                               \tag{C.5}
$$
so the corresponding sum has codimension at least three. These are statements about graded vector spaces; they do not assert a factorization theorem or its negation for the full pro-$2$ automorphism groups.

**Proof and computation.** Let $W$ be the standard $r$-dimensional representation of the permutation group on the $r+1$ punctures. In degree $n\geq2$, the exact special-derivation complex, after quotienting inner derivations, gives the virtual character
$$
 [\mathfrak o_{r,n}]=[W\otimes L_n(W)]-[L_{n+1}(W)].   \tag{C.6}
$$
The character of a free Lie power is
$$
 \operatorname{tr}(g\mid L_n(W))=
 \frac1n\sum_{d\mid n}\mu(d)\operatorname{tr}(g^d\mid W)^{n/d}.
$$
For the index-two cover, the deck involution fixes two punctures and interchanges the other two. For the degree-four cover, each nonidentity deck element fixes two punctures and interchanges the other four in two pairs. Thus the trace on $W$ is one in both cases; its even powers have trace $r$. Equations (C.6) and character averaging give (C.4)–(C.5), except for the sum rank in (C.4), which was independently checked by rational matrices in `ceh_checks.py`, using the independent Lyndon implementation of Part A. The deck action on the six-dimensional degree-three space has matrix
$$
 \begin{pmatrix}
0&0&1&0&0&0\\0&1&0&0&0&0\\1&0&0&0&0&0\\
0&0&0&0&-1&0\\0&0&0&-1&0&0\\0&0&0&0&0&1
\end{pmatrix}.
$$
Adjoining the two point-pushing columns to its four-dimensional fixed subspace gives rank five. The pure sphere Lie dimensions used here are $\sum_{j=2}^{r-1}\dim L_n(\mathbf Q^j)$, obtained from the iterated free Birman extensions. The other computed values are:

| Upstairs type | Degree | Special outer | Deck-fixed | Geometric |
|---|---:|---:|---:|---:|
| $(0,4)$ | 2 | 1 | 0 | 1 |
| $(0,4)$ | 3 | 6 | 4 | 2 |
| $(0,4)$ | 4 | 6 | 2 | 3 |
| $(0,6)$ | 2 | 10 | 1 | 10 |
| $(0,6)$ | 3 | 50 | 17 | 30 |
| $(0,6)$ | 4 | 126 | 27 | 81 |

All ranks are exact over $\mathbf Q$. $\square$

### C.5. Refuted — Surjectivity for the index-two pro-$2$ cover

For the index-two covering in C.1, after replacing both geometric fundamental groups by their free pro-$2$ completions, the coset map is **not surjective**. In particular,
$$
 \operatorname{Out}_{\rm lac}(V_2^{(2)})
 \ne N_{\operatorname{Out}_{\rm lac}(V_2^{(2)})}(D)\,
       \Sigma(V_2^{(2)}),\qquad D=C_2.                 \tag{C.7}
$$
This conclusion follows from an actual finite characteristic $2$-group quotient and a special automorphism of the full free pro-$2$ group. It does not use rational averaging or a comparison of dimensions alone.

**The group, deck action, and lift.** Write the downstairs group as $F^{(2)}(a,b)$, with $a\mapsto1,b\mapsto0$ in $C_2$, and use the Schreier basis
$$
 x=aba^{-1},\qquad y=a^2,\qquad z=b
$$
of $V_2^{(2)}$. Its four peripheral classes have generators $x,y,z,P^{-1}$, where $P=xyz=(ab)^2$. Conjugation by $a$ induces the deck representative
$$
 \delta(x)=yzy^{-1},\quad\delta(y)=y,\quad\delta(z)=x,
 \qquad\delta^2=\operatorname{Inn}(y),\quad
 \delta(P)=x^{-1}Px.                                  \tag{C.8}
$$
Let
$$
 R=\mathbf F_2\langle X,Y,Z\rangle/(\text{words of length }\ge5),
 \qquad J=(X,Y,Z),
$$
and let $Q$ be the image of $V_2^{(2)}$ under $x\mapsto1+X$, $y\mapsto1+Y$, $z\mapsto1+Z$. The group $1+J$ has order $2^{120}$, so $Q$ is a finite $2$-group. Its kernel is fully characteristic: substitution of $X,Y,Z$ by arbitrary elements of $J$ preserves the ideal of words of length at least five. This argument also proves that every endomorphism under consideration induces the asserted endomorphism of $Q$; no identification with a differently indexed filtration is needed. Ordinary fifth commutators map to $1$ in $Q$.

Take the integral special derivation whose conjugators are
$$
 a_x=[[X,Y],Y],\qquad a_y=[X,[X,Y]],\qquad a_z=0.
$$
Jacobi gives $[a_x,X]+[a_y,Y]=0$. By A.1 this lifts to an actual special automorphism $\alpha$ of $V_2^{(2)}$ fixing $P$. Begin the lift with the group commutators $A_x=[[x,y],y]$, $A_y=[x,[x,y]]$, $A_z=1$. All subsequent corrections change generator images only in $\gamma_5$, so they disappear in $Q$. Hence the induced automorphism is exactly
$$
 \alpha(X)=X+h,\qquad\alpha(Y)=Y+h,\qquad\alpha(Z)=Z,
 \qquad h=X^2Y^2+Y^2X^2.                              \tag{C.9}
$$
It is an involution on this finite quotient. The finite candidate is therefore realized in the required infinite pro-$2$ automorphism group.

**The full geometric comparison.** The pure four-puncture geometric group is generated, modulo inner automorphisms, by the two adjacent pair twists
$$
 t_1:(x,y,z)\longmapsto
 ((xy)x(xy)^{-1},(xy)y(xy)^{-1},z),
$$
$$
 t_2:(x,y,z)\longmapsto
 (x,(yz)y(yz)^{-1},(yz)z(yz)^{-1}).                    \tag{C.10}
$$
These are the usual squares of the adjacent Artin generators; the pure three-strand braid group modulo its central full twist is generated by their outer classes. Thus their finite image gives the entire pure geometric image relevant here. Exact closure under these two generators in $\operatorname{Aut}(Q)$ has order $128$; its conjugation orbit of $\delta$ has $64$ elements.

It suffices to compare this pure image. The permutation of the four cusp labels induced by $\delta$ is $(xz)$. If $\alpha D\alpha^{-1}=\sigma D\sigma^{-1}$ for a geometric $\sigma$, then the label permutation of $\sigma$ centralizes $(xz)$. This centralizer is generated by $(xz)$ and $(y\infty)$. Both have geometric representatives commuting with $D$: in the original cover coordinate $w$ these are $w\mapsto-w$ and $w\mapsto1/w$. Multiplying $\sigma$ by a suitable such representative makes it pure without changing its deck conjugate. This accounts for every geometric label permutation.

**The finite certificate.** For each of the $64$ geometric deck conjugates $\beta=t\delta t^{-1}$, the program tests the necessary condition for inner equality
$$
 c\,\beta(x_i)=(\alpha\delta\alpha^{-1})(x_i)c
 \quad(i=1,2,3),\qquad
 c=1+\sum_{1\le |w|\le3}c_w w.                       \tag{C.11}
$$
There are $39$ unknowns $c_w\in\mathbf F_2$. Every group conjugator belongs to $1+J$; its degree-four terms commute with all generator images modulo $J^5$ and can be omitted. Therefore inconsistency even for arbitrary units of the displayed form rules out every inner group conjugator.

All $64$ systems are inconsistent. The C++ search records an explicit sum of coefficient equations giving $0=1$ for each system. An independent Python program reconstructs the automorphisms from group commutators using sets of literal words, verifies the whole geometric orbit and its closure, and checks each recorded sum by addition only. It does not reuse the C++ Gaussian elimination. To make the certificate interpretable, write $\rho_i(w)$ for the coefficient equation of the word $w$ in the $i$th equation of (C.11). The $64$ certificates use just the following five patterns; the sum of the listed equations has zero left side and right side one.

| Equations added | Number of geometric deck conjugates |
|---|---:|
| $\rho_x(XZ),\rho_y(XY)$ | 32 |
| $\rho_x(XXZ),\rho_y(XXY)$ | 16 |
| $\rho_x(XZ),\rho_x(XYZ),\rho_y(XYY)$ | 8 |
| $\rho_x(XXZ),\rho_x(XXYZ),\rho_y(XXYY)$ | 4 |
| $\rho_x(XXZZ),\rho_y(XXZY)$ | 4 |

For example, for $\beta=\delta$ the three equations in the fourth row are $c_{XX}=0$, $c_{XX}+c_{XXY}=0$, and $c_{XXY}=1$, an immediate contradiction. The file `ceh_pro2_certificates.json` specifies a twist word and the applicable certificate for every orbit element. The search also tested all $64$ sums of the six integral special degree-three basis vectors supplied in Part A; exactly $32$ have no intertwiner to any geometric deck conjugate. Only the explicit witness (C.9) is needed for the theorem.

If $\alpha$ belonged to $\Sigma N(D)$, its conjugate of $D$ would be geometrically conjugate to $D$, contrary to (C.11). Inversion gives failure of $N(D)\Sigma$ as well; the finite image of $\alpha^{-1}$ is the same involution. By C.2 this is precisely the failure of covering coset surjectivity. This proves (C.7). The reproducible programs are `ceh_pro2_cover.cpp` and `ceh_pro2_verify.py`; their exact outputs and all dual certificates accompany the paper. $\square$

### C.6. Proved — Arithmetic-image quotients are unchanged over the field of definition

Let $Y\to X$ be a finite étale cover of affine hyperbolic curves defined over a number field $K$, and use compatible geometric base points, allowing inner ambiguity. Write $\Gamma^{\rm arith}_{X,K}$ and $\Gamma^{\rm arith}_{Y,K}$ for the §29 arithmetic-image quotients with arithmetic group $G_K$. Under the geometric/arithmetic intersection theorem used in LM3 C.5 and E.2, restriction identifies both quotients with $G_K$, and the comparison is the identity of $G_K$.

**Proof.** In the downstairs arithmetic-image group, first take the stabilizer of the chosen geometric covering. Its geometric subgroup is the liftable subgroup of $\Sigma_X$, and its quotient still maps onto $G_K$: the cover defined over $K$ supplies the compatible $G_K$ action. Restriction carries this geometric subgroup into $\Sigma_Y$ and the arithmetic action to that of $Y$. We do not restrict every element of the full geometric mapping class group unless it stabilizes the cover. The exact sequences
$$
1\to\pi_1(X_{\overline K})\to\pi_1(X)\to G_K\to1,
\qquad
1\to\pi_1(Y_{\overline K})\to\pi_1(Y)\to G_K\to1
$$
form a commutative diagram induced by the cover. Conjugation gives the compatible outer actions, and hence the compatible arithmetic-image groups. Hoshi–Mochizuki (2011, Corollary 6.4), with the reduction already proved in LM3 C.5, says that quotienting those images by their geometric parts loses no element of $G_K$. Thus the map on the quotients is precisely the common map to $G_K$ in the diagram, namely its identity. Changing compatible base points changes representatives by geometric inner automorphisms and disappears in the quotient. If the cover is defined only over $K$, one must restrict the downstairs arithmetic group to the corresponding open subgroup $G_K\subset G_{\mathbf Q}$; there is no assertion that $G_{\mathbf Q}$ stabilizes that chosen covering. Both test covers admit models over $\mathbf Q$, so they give the full $G_{\mathbf Q}$ comparison. This proves the arithmetic-image version of scan 355, formula (6), and scan 356. $\square$

### C.7. Open — The §26 comparison requires an additional normalizer assertion

For the two tripod covers, the already established §26 groups are $\widehat{\mathrm{GT}}_0$ downstairs and $\widehat{\mathrm{GT}}$ upstairs. Restriction from the stabilizer of the covering is defined at the level of loop-preserving automorphisms by C.2. To descend it to the normalizer quotients, one must prove that a downstairs automorphism normalizing $\Sigma(G)$ restricts to an automorphism normalizing **all** of $\Sigma(V)$, rather than merely its subgroup $N_{\Sigma(V)}(D)$. C.3 proves the intersection condition but does not prove this enlargement. The smallest undecided assertion is exactly this implication for $D=C_2$ and $V=V_2$. It is the distinction Grothendieck himself isolates at scan 362. Thus no map $\widehat{\mathrm{GT}}_0\to\widehat{\mathrm{GT}}$ is manufactured by citing the separate identifications of its putative source and target.

### C.8. Proved — Two corrections to the readings at scans 361–363

In the normalizer expression at scan 361, the deck group $D$ acts on the upstairs group, so the ambient outer automorphism group must be the one belonging to $\pi'_0$. The alternative downstairs symbol cannot type the displayed normalizer. At scan 363, for $\nu\geq1$, the dimension of mod-two homology is $2g+\nu-1$, so the sign in $2g\unsure{+|-}\nu-1$ is supported as plus. These are mathematical constraints on the transcription, not claims of palaeographic certainty. At $(0,3)$ the minus alternative would give exponent $-4$ and cannot represent the displayed finite elementary abelian deck group; the plus alternative gives the required exponent two. Formula (C.1) also explains why a quotient by deck transformations appears only after passing to outer automorphisms.

### C.9. Open — The exact remaining covering cases

For the full profinite groups, covering surjectivity remains undecided here for both $V_2$ and $V_4$. In the notation of C.3, the exact assertion is $A'=f(A)B'$, equivalently $\operatorname{Out}_{\rm lac}(V)=N(D)\Sigma(V)$. The negative pro-$2$ answers are C.5 and C.10. A.1 does not lift the automorphism of C.5 from the free pro-$2$ group to the free profinite group, so those answers do not settle the full profinite cases. An exact remaining route is to realize a full profinite special automorphism whose pro-$2$ image has the finite obstruction (C.9), or to construct another obstruction directly in full finite quotients. We have supplied neither such realization nor a full profinite factorization theorem.

### C.10. Refuted — Surjectivity for the degree-four pro-$2$ cover

For the characteristic degree-four cover $W=V_4^{(2)}$ of the tripod, with deck group $D_4=C_2^2$, one likewise has
$$
 \operatorname{Out}_{\rm lac}(W)\ne
 N_{\operatorname{Out}_{\rm lac}(W)}(D_4)\Sigma(W).
                                                               \tag{C.12}
$$
This is a transfer of the concrete certificate in C.5, using the pro-$2$ geometric-normalizer descent proved in C.3. No direct enumeration in rank five is claimed.

**Proof.** Use the intermediate tower
$$
 W\subset V=V_2^{(2)}\subset G=F_2^{(2)},\qquad
 E=V/W\subset D_4=G/W.
$$
The automorphism $\alpha$ of C.5 acts trivially on abelianization, so preserves $W$, which is the kernel in $V$ of the mod-two character $x\mapsto1$, $y\mapsto0$, $z\mapsto1$. Let $\alpha_W$ denote its restricted outer class. It normalizes $E$ by C.2.

Suppose that $\alpha_W=n\sigma$ with $n\in N(D_4)$ and $\sigma\in\Sigma(W)$. Then
$$
 \sigma E\sigma^{-1}=n^{-1}En=:E',
$$
where $E'$ is another order-two subgroup of $D_4$. The geometric normalizer of $D_4$ acts transitively on its three order-two subgroups: every downstairs tripod permutation lifts because this cover is characteristic, and its action on $D_4=H_1(G,\mathbf F_2)$ is the full $\mathrm{GL}_2(\mathbf F_2)=S_3$. Choose $t\in N_{\Sigma(W)}(D_4)$ with $tEt^{-1}=E'$. The factors
$$
 n'=nt,\qquad \sigma'=t^{-1}\sigma
$$
both normalize $E$; moreover $n'$ still normalizes $D_4$. The quotient isomorphism of C.2 for $W\subset V$ now descends $n'$ to an outer automorphism of $V$ normalizing $D_4/E$, while C.3 descends $\sigma'$ to an element of $\Sigma(V)$. Their product is the outer class of $\alpha$. Since $D_4/E$ is exactly the index-two deck group of C.5, this is the factorization ruled out there. The contradiction proves (C.12). $\square$

# E. Elliptic types, coherence, and the whole outer tower

This part concerns the proposed type-independence in §§30–33 bis, notably folios 188–202, scans 371, 376, 395–400, and the modular constructions of §26, folios 165–166 (the latter reading is doubtful), scans 326–329. We keep the distinction between a natural automorphism of an outer group-valued functor and a coherent automorphism of boundary categories with specified paths and clutching data.

### E.1. Proved — The exact remaining $(1,2)$ inertia condition

Put $E=\widehat{P\Gamma}_{1,3}$ and let $A\subset\operatorname{Out}(E)$ be the subgroup of LM3 E.11: it preserves the universal-curve fibre $\widehat\pi_{1,2}$, its two cusp classes with one exponent, and normalizes the transposition of the two original marks. Let $A^I$ be the subgroup which in addition preserves the conjugacy class of a nonseparating twist subgroup. Then
$$
 A^I/S_2\cong\widehat{\mathrm{GT}}.                    \tag{E.1}
$$
Consequently the requested equality $\Gamma^{\rm norm}_{1,2}=\widehat{\mathrm{GT}}$ is equivalent to $A=A^I$ under the known normalizer reduction and the known tower inclusion.

**Proof.** Genus-one congruence lets us replace $E$ by its procongruence completion. Boggi (2026, Theorem 3.12) turns preservation of nonseparating twist inertia into preservation of all twist inertia; his Theorem A(ii), applied to $(1,3)$, identifies the resulting outer group with $S_3\times\widehat{\mathrm{GT}}$. The condition of preserving the chosen fibre singles out the stabilizer of the third label, namely $S_2$, in the permutation factor. Normalizing the transposition imposes no further condition inside that stabilizer, and the GT factor commutes with it. Quotienting gives (E.1). Conversely the GT action in Boggi's Theorem 6.7 is compatible with the relevant forgetting maps and preserves all peripheral twist subgroups, hence gives the known inclusion into $A/S_2$. Thus equality can fail only through an element of $A$ outside the inertia-preserving subgroup. $\square$

The equality $A=A^I$ is the separate open assertion E.9. The proved identification (E.1) does not establish that automatic-inertia assertion.

### E.2. Proved — The automorphism 2-group of the open elliptic forgetting arrow

Consider the diagram of one-object profinite groupoids
$$
 B G_2\xrightarrow{Bq}B G_1,
\qquad
G_2=\widehat{P\Gamma}_{1,2},\quad G_1=\widehat{P\Gamma}_{1,1},
$$
where $q$ forgets the second mark. Automorphisms mean invertible pseudonatural transformations, modulo modifications. Its automorphism 2-group has
$$
 \pi_0\cong\widehat{\mathrm{GT}},\qquad \pi_1=1.       \tag{E.2}
$$

**Proof.** For a general epimorphism $q:G_2\to G_1$, a pseudonatural automorphism is represented by automorphisms $\phi_2,\phi_1$ and $h\in G_1$ with $\phi_1q=\operatorname{Inn}(h)q\phi_2$, up to the corresponding inner modifications. Choose a lift of $h$ in $G_2$; modification by it makes the compatibility strict. We obtain
$$
 \pi_0\cong\operatorname{Out}(G_2;\ker q),\qquad
 \pi_1\cong Z(G_2),
$$
the second isomorphism sending a central modification $z_2$ to $(z_2,q(z_2))$.

Now $G_2$ is the profinite central quotient of $B_4$. Minamide–Nakamura (2022, Theorem 4.3 and Corollary C) identify its outer automorphism group with GT. Their Proposition 3.2(iii) makes the orbifold fibre $C_2\amalg C_2\amalg C_2$ characteristic. Inside that fibre, the genuine punctured-elliptic fibre is the unique index-two subgroup in which all three involution classes map nontrivially to the quotient: its kernel is free of rank two. This description is invariant under automorphisms, so $\ker q$ is characteristic. Finally $Z(G_2)=1$ by genus-one congruence and Boggi (2020, Theorem 4.4), while $Z(G_1)=C_2$. Hence (E.2). The center at the target creates nonunique representatives of a compatibility isomorphism, but not a surviving $\pi_1$ of this arrow diagram. $\square$

### E.3. Proved — The center does not create a $\pi_1$ for the elliptic boundary pair

Use the completed stable-curve transporter categories of LM3 F.15 for $(1,1)$ and $(1,2)$, together with a forgetting functor. The automorphism 2-group of this decorated pair has trivial $\pi_1$. This remains true after adjoining the other forgetting map, relabellings, and the boundary clutching functors.

**Proof.** A natural automorphism of the identity on a transporter category has an open-stratum component in the center of its open group. Once that component is specified, naturality with the smoothing arrow from any stratum to the open stratum determines its component there: postcomposition embeds the transporter Hom-set into the open Hom-set. This is the same transporter argument as LM3 F.12, and does not require trivial centers. For $(1,2)$ the open center is trivial, so the whole natural automorphism is the identity. Compatibility with forgetting then forces the open component at $(1,1)$ to be the identity, because $q$ is onto. The transporter argument forces all its boundary components to be the identity as well. Adding more compatibility requirements takes a subgroup of this already trivial modification group. $\square$

For clarity about $\pi_0$, two *unrelated* forgetting arrows with the same target center $C_2$ would produce two compatibility signs, modulo a common target modification, and hence one residual $C_2$. Coherent relabelling of the two source marks identifies the two signs and kills that residual choice. The finite computation in `ceh_checks.py` verifies these two orbit counts, two and one. This computation explains why the precise morphisms and their relations must be retained; it does not settle every clutching coherence equation.

### E.4. Open — The elliptic boundary and orbifold normalizer comparisons

What remains after E.2–E.3 is the following exact assertion. For every $F\in\widehat{\mathrm{GT}}$, its automorphism of $G_2$ must extend to the two transporter categories with induced automorphisms on all normalization factors, with compatibility isomorphisms for forgetting and clutching satisfying their relations; and every such system inducing the identity on $G_2$ must be coherently isomorphic to the identity system. The first step, extension to each individual boundary category, follows once the twist-incidence data are preserved. The remaining step is comparison of the induced genus-zero action at the nonseparating boundary with the prescribed action on its four-point normalization, including the branch-exchange involution, and coherence with the rational-tail boundary carrying $G_1$.

Our attack removes the proposed $\pi_1=C_2$ obstruction and computes the open-arrow 2-group, but does not supply a complete presentation of these remaining clutching relations. In particular, the outer-tower theorem E.7 below cannot by itself be upgraded to a theorem about this finer 2-group. Under the explicitly named **boundary coherence hypothesis** consisting of the preceding existence and uniqueness assertion, one obtains $\pi_0=\widehat{\mathrm{GT}}$ and $\pi_1=1$. Without it, only the latter equality and (E.2) have been proved here.

There is a second, distinct comparison required by Part E(c). In the notation of E.5, put $n_3=1$, $n_4=2$ and
$$
 \widetilde N_r=\{\phi\in\mathcal A_r:
 [\phi]\in N_{O_{0,r+1}}(\Sigma_{0,r+1})\},
 \qquad r\in\{3,4\}.
$$
The quotient and restriction construction gives a genuine homomorphism $\rho_r:\mathcal A_r\to\operatorname{Aut}_{\rm lac}(K_r)$. What remains to prove is the **full geometric-normalizer comparison**
$$
 [\rho_r(\widetilde N_r)]\subseteq
 N_{O_{1,n_r}}(\Sigma_{1,n_r}),
$$
together with descent through the geometric equivalence relations and independence of the choices used to stabilize the distinguished infinity and to lift through the deck quotient. After those steps, the induced comparison of the §26 normalizer quotients must be shown to retain the same GT pair $(\lambda,f)$ under the standard genus-zero and elliptic identifications. Normalization of the deck subgroup, proved in E.5, does not establish normalization of the full elliptic geometric subgroup. Nor does an abstract isomorphism of both quotients with GT establish that their specified comparison is the identity.

For $(1,2)$ the identification of the target quotient with GT is additionally conditional on the automatic-inertia assertion E.9. For $(1,1)$ that identification is already known from LM3 E.10; thus the orbifold comparison between $(0,4)$ and $(1,1)$ is the smallest remaining comparison in this audit. The analogous same-pair comparison for the elliptic filling $(1,2)\to(1,1)$ also remains conditional on E.9 and on construction of its normalizer comparison. The ordinary genus-zero filling is covered by the known comparison recalled in E.5. These residual assertions, rather than the formal descent maps alone, are the unresolved part of E(c).

### E.5. Proved — The orbifold quotient and parity-kernel restriction maps

There is no ordinary degree-two étale covering of punctured surfaces $(1,1)\to(0,4)$ or $(1,2)\to(0,5)$. The corresponding elliptic quotients have cone points. For $(1,1)$ the quotient has one cusp and three cone points of order two; its orbifold Euler characteristic is $-1/2$. For two punctures exchanged by the elliptic involution, the quotient has one cusp and four cone points of order two, of orbifold Euler characteristic $-1$. Deleting the cone points produces the four- or five-punctured sphere but also changes the upstairs surface.

For $r=3,4$, the correctly typed group construction is
$$
 F_r=\widehat F(x_1,\ldots,x_r),\qquad
 P=x_1\cdots x_r,\qquad
 J_r=\overline{\langle\!\langle x_1^2,\ldots,x_r^2\rangle\!\rangle},
$$
$$
 q_r:F_r\twoheadrightarrow
 Q_r=F_r/J_r=\underbrace{C_2\amalg\cdots\amalg C_2}_{r\text{ factors}},
 \qquad c_i=q_r(x_i),\quad c=c_1\cdots c_r,
$$
where $\amalg$ denotes the profinite free product. Define
$$
 \epsilon_r:Q_r\twoheadrightarrow C_2,\quad
 \epsilon_r(c_i)=1,\qquad K_r=\ker\epsilon_r.
$$
Then $K_3\cong\widehat\pi_{1,1}$ and $K_4\cong\widehat\pi_{1,2}$, with their induced oriented peripheral structures. Let $\mathcal A_r$ be the subgroup of $\operatorname{Aut}_{\rm lac}(F_r)$ preserving the distinguished infinity class $[\langle P^{-1}\rangle]$. There are continuous homomorphisms
$$
 \mathcal A_r\xrightarrow{q_*}\operatorname{Aut}(Q_r;K_r)
 \xrightarrow{\operatorname{res}_{K_r}}\operatorname{Aut}(K_r),
 \qquad
 \rho_r=\operatorname{res}_{K_r}\circ q_*,
$$
and $\rho_r(\mathcal A_r)\subseteq\operatorname{Aut}_{\rm lac}(K_r)$ with the same orientation multiplier. These are quotient followed by restriction maps, not restriction along an inclusion of the ordinary punctured-sphere group into the elliptic group.

**Proof.** The Euler characteristics of $(1,1),(0,4)$ are $-1,-2$, and those of $(1,2),(0,5)$ are $-2,-3$. They cannot satisfy $\chi(\text{upstairs})=2\chi(\text{downstairs})$. On an elliptic curve, the involution has four fixed points. In the one-puncture case the removed origin accounts for one of them, leaving three order-two cone points. In the exchanged-puncture case no fixed point is removed and the two punctures give one cusp downstairs. Applying the orbifold formula gives the values stated.

The discrete orbifold group is the free product of $r$ copies of $C_2$. Its parity kernel is a torsion-free subgroup of index two, free on the Schreier generators $c_1c_i$ for $2\leq i\leq r$. Finite-index subgroups carry the topology induced by the full profinite topology, so completion identifies this kernel with $K_r$. Its Euler characteristic is $2(1-r/2)=2-r$. When $r=3$, $c$ has odd parity, so the cusp lifts once and its inertia in $K_3$ is generated by $c^2$. When $r=4$, $c$ has even parity, so the cusp lifts twice, with inertia classes generated by $c$ and $c_1cc_1^{-1}$. The formula $2-2g-n=2-r$ now gives $(g,n)=(1,1)$ and $(1,2)$, respectively.

For $\phi\in\mathcal A_r$, there are $\sigma\in S_r$, $v_0,\ldots,v_r\in F_r$ and a common $\lambda\in\widehat{\mathbf Z}^{\times}$ such that
$$
 \phi(x_i)=v_i x_{\sigma(i)}^{\lambda}v_i^{-1},\qquad
 \phi(P)=v_0P^{\lambda}v_0^{-1}.
$$
Every $\phi(x_i^2)$ belongs to $J_r$; applying the same argument to $\phi^{-1}$ gives $\phi(J_r)=J_r$. Hence $\phi$ descends uniquely to an automorphism $\bar\phi$ of $Q_r$. Since $\lambda$ is odd modulo two, each $\bar\phi(c_i)$ is conjugate to $c_{\sigma(i)}$, and $\epsilon_r\bar\phi=\epsilon_r$. Thus $\bar\phi$ preserves $K_r$ and can be restricted to it. These constructions commute with composition and are continuous.

Write $u=q_r(v_0)$. For $r=3$ the image of $c^2$ is $u(c^2)^{\lambda}u^{-1}$. If $u$ has odd parity, replace this conjugator by $uc$, which has even parity and gives the same conjugate. This is therefore conjugacy in $K_3$, with exponent $\lambda$. For $r=4$, conjugation by an even $u$ preserves the first cusp class, while an odd $u$ takes it to the second. The image of the second generator $c_1cc_1^{-1}$ has conjugator $\bar\phi(c_1)u$, of the opposite parity. Thus the two cusp classes are permuted, again with their common exponent $\lambda$. This proves the asserted loop preservation.

There is also a precise outer form. Let $\delta_r$ be the outer involution of $K_r$ induced by conjugation by $c_1$, and put $D_r=\langle\delta_r\rangle$. It is nontrivial: on the Schreier generators it sends $c_1c_i$ to $(c_1c_i)^{-1}$, hence acts as $-1$ on their abelianization. Because $\bar\phi(c_1)$ has odd parity, the outer class of $\rho_r(\phi)$ normalizes $D_r$. Replacing $\phi$ by $\operatorname{Inn}(g)\phi$ changes this outer class by conjugation by $q_r(g)$, which is trivial or $\delta_r$ according to its parity. Consequently the well-defined outer homomorphism has target
$$
 \mathcal A_r/\operatorname{Inn}(F_r)
 \longrightarrow
 N_{\operatorname{Out}_{\rm lac}(K_r)}(D_r)/D_r.
$$
This proves quotient and restriction descent, including the necessary deck ambiguity. It does not supply the full geometric-normalizer comparison isolated in E.4. $\square$

For the ordinary genus-zero filling $(0,5)\to(0,4)$, the known normalizer identifications of LM3 E.7 identify the comparison with the identity of GT: the standard braid action restricts with the same pair $(\lambda,f)$, and faithfulness at the detecting level forces this identification. The same formal argument applies to $(1,2)\to(1,1)$ **if** E.9's automatic-inertia assertion and the asserted normalizer comparison map have first been proved. Separate abstract identifications of four groups with GT do not prove that a specified covering induces that map.

### E.6. Known — What the refined quilt theorems actually give

Let $\mathcal G_{\rm NS}$ be the subgroup of GT defined by Nakamura–Schneps (2000, Definition 1.1), imposing $(\mathrm{III}')$ and $(\mathrm{IV})$ with their Kummer cocycle $\rho_2$. Their Theorem 1.2 gives $G_{\mathbf Q}\subset\mathcal G_{\rm NS}$. Theorems 1.3–1.4 give genuine actions after a quilt is fixed, independent outer actions after forgetting it, and compatibility for inclusions of unions of pants. Hatcher–Lochak–Schneps (2000, Theorems A–C, respectively Lemma 7, Theorem 4 and Theorem 5 of §3) give the analogous action of their subgroup $\Lambda\subset\widehat{\mathrm{GT}}^1$ defined by relation $(R)$.

**Reduction to Grothendieck's formulation.** Replace each surface by its profinite mapping class group and each pants inclusion by the induced continuous homomorphism. Theorem 1.4 supplies a commutative square for every such arrow with the selected quilt restrictions. The change-of-quilt formula in Nakamura–Schneps §10, equations (10.1)–(10.4), says precisely that replacing those choices changes the action by a specified inner automorphism. Quotienting by these inner automorphisms therefore gives a natural transformation of the outer tower. Its restriction to any detecting genus-zero component has the original parameter $(\lambda,f)$, so every comparison in this restricted tower is the identity on $\mathcal G_{\rm NS}$. In the Hatcher–Lochak–Schneps formulation the same argument uses Theorem C, with $\lambda=1$ and the extra relation $(R)$.

This proves compatibility for the arrows actually present in those theorems. Their hypotheses do not include arbitrary finite covering maps. For the explicit genuine elliptic/quilt formulas, relation $(\mathrm{IV})$ and the $\rho_2$ correction remain part of the theorem being used; replacing $\mathcal G_{\rm NS}$ by all of GT in those formulas requires a separate proof of those relations or a comparison with a different action. In particular the Hatcher–Lochak–Schneps subgroup does not contain all of $G_{\mathbf Q}$: its arithmetic subgroup fixes all roots of unity and all roots of two. This restriction is stated on page 3 of the supplied paper. $\square$

### E.7. Known — Derivation of the whole procongruence outer-tower statement

Let $\mathcal S$ be Boggi's category of oriented hyperbolic surfaces with boundary and embeddings which may fill punctures, and let
$$
 \check{\mathfrak T}^{\rm out}(S)=\check{P\Gamma}(S,\partial S)
$$
with continuous homomorphisms modulo target inner automorphisms. Then
$$
 \operatorname{Aut}(\check{\mathfrak T}^{\rm out})\cong
 \widehat{\mathrm{GT}}.                                \tag{E.3}
$$
There is a faithful compatible action of GT on the corresponding full profinite outer tower. Equality of its automorphism group with GT follows if the congruence subgroup property holds for every component.

**Proof of the reduction, using Boggi (2026, Theorem 6.23 and Corollary 6.24).** We spell out why this is a statement in the manuscript's terms. Filling a boundary circle by a punctured disc kills exactly its procyclic twist subgroup. A natural automorphism of the tower preserves that kernel. Every interior simple closed curve is a boundary circle of an embedded subsurface, so naturality also preserves every interior twist-inertia subgroup. This is the argument of Boggi's Lemma 6.25; it makes inertia intrinsic to the full tower even though it need not be intrinsic to a single group. His Theorem 6.1 then identifies each sufficiently large component's permissible outer automorphisms with a permutation factor times GT. The individual boundary-filling maps distinguish the labelled boundary circles, eliminating the permutation factor. The restriction maps retain the same GT parameter, and the construction in Theorem 6.7 supplies its converse action. This proves (E.3), with the precise source category and outer ambiguity stated.

There is a natural quotient transformation $\widehat{\mathfrak T}^{\rm out}\to\check{\mathfrak T}^{\rm out}$. If all congruence kernels vanish, it is objectwise an isomorphism and therefore identifies the two automorphism groups. Without that assumption, Corollary 6.24 gives an injection of GT into the full profinite tower automorphism group, but not surjectivity; the latter is Boggi's Conjecture 6.21. Neither equation (E.3) nor that injection computes the normalizer quotient attached to an isolated arbitrary type without the automatic-inertia condition. $\square$

### E.8. Known — The modular-topos exact sequence and its correction

For the stack of unordered marked hyperbolic curves $\mathcal M_{g,[n]}/\mathbf Q$, with geometric base point, the étale fundamental group fits in
$$
1\to\widehat\Gamma_{g,n}\to
 \pi_1^{\rm et}(\mathcal M_{g,[n]})\to G_{\mathbf Q}\to1. \tag{E.4}
$$
Passing through universal geometric monodromy replaces the left term by its procongruence image $\Sigma_{g,n}$, with congruence kernel as the discarded kernel. The arithmetic-image quotient of §29 is $G_{\mathbf Q}$, as in LM3 E.2. For $(0,3)$, the stack is $BS_3$, and (E.4) is the split sequence with middle group $S_3\times G_{\mathbf Q}$.

**Reduction.** Boggi (2026, §7.1, equation (29)) states (E.4) for the moduli stack, and §2.8 identifies the relevant relative groups with geometric étale groups of the logarithmic formal boundary objects. The map to the geometric fibre's outer automorphism group is the universal monodromy map. Its geometric kernel is exactly the definition of the congruence kernel. The intersection theorem of Hoshi–Mochizuki used in LM3 C.5 ensures that killing this geometric kernel introduces no extra arithmetic kernel after quotienting the image by $\Sigma$. At $(0,3)$ there is one geometric isomorphism class with automorphism group $S_3$, defined over $\mathbf Q$, giving the displayed product. This proves the stack-based exact sequence of scans 326–329. The coarse moduli space is a point and would lose $S_3$; it cannot replace the stack. Nor does (E.4) identify the arithmetic image with the entire normalizer in $\operatorname{Out}_{\rm lac}$: that additional assertion is precisely the §26 conjecture, not a formal consequence of the exact sequence. At scan 328 the folio alternative $166|168$ has no mathematical consequence, and we do not select one as a reading. $\square$

### E.9. Open — Automatic nonseparating inertia for the elliptic normalizer

With $E$, $A$, and $A^I$ as in E.1, the precise remaining assertion is
$$
 A=A^I,
 \quad\text{equivalently}\quad
 a(I_\gamma)\text{ is conjugate in }E\text{ to }I_\gamma
 \text{ for every }a\in A,
$$
where $I_\gamma=\overline{\langle\tau_\gamma\rangle}$ is the subgroup of a nonseparating Dehn twist. The condition is independent of the representative of the outer automorphism. Under the normalizer reduction in E.1, this is exactly the unresolved implication needed for $\Gamma^{\rm norm}_{1,2}\cong\widehat{\mathrm{GT}}$.

**Attack and remaining obligation.** Boggi–Funar (2023, Theorem 4.11 and Corollary 4.12) and Boggi (2026, Theorem 2.8) identify centralizers of already recognized multitwists with curve stabilizers. These theorems do not characterize all nonseparating twists among arbitrary elements solely by the isomorphism type of their centralizers. Boggi's 2026 introduction explicitly retains automatic inertia in positive genus as unresolved. The precise converse still required here is an intrinsic recognition of $I_\gamma$ among subgroups of $E$ using the specified universal-curve fibre, its two cusp classes with their common exponent, and the transposition. An automorphism carrying the centralizer of $I_\gamma$ to an isomorphic centralizer does not supply that converse. The smallest unresolved case is this very group $\widehat{P\Gamma}_{1,3}$ with those decorations. We have neither proved the restricted recognition assertion nor constructed an element of $A\setminus A^I$.

# H.1. The genus-three congruence kernel

### H.1. Proved — A centralizer exactly measuring the closed genus-three kernel

Let $P=\widehat\pi_{3,0}$ and let
$$
1\to P\to E=\widehat{P\Gamma}_{3,1}\xrightarrow{q}
\widehat\Gamma_{3,0}\to1
$$
be the profinite Birman sequence. The restriction of $q$ gives an isomorphism
$$
 C_E(P)\xrightarrow{\sim}C_{3,0},
\qquad
C_{3,0}=\ker(\widehat\Gamma_{3,0}\to\operatorname{Out}(P)).
                                                               \tag{H.1}
$$
In particular, genus-three congruence is equivalent to $C_E(P)=1$.

**Proof.** Conjugation on $P$ gives a homomorphism $E\to\operatorname{Aut}(P)$ and, after quotienting $P$, the usual outer monodromy of the closed genus-three surface. Thus an element of $C_E(P)$ maps into $C_{3,0}$. The restriction is injective because $C_E(P)\cap P=Z(P)=1$. If $c\in C_{3,0}$, choose $e\in E$ above it. Its action on $P$ is inner, say by $p\in P$. Then $p^{-1}e$ centralizes $P$ and maps to $c$. This proves surjectivity and the asserted equivalence. All maps are continuous; compactness makes the bijection a profinite isomorphism. The procongruence Birman sequence in Boggi (2020, Corollary 4.7, with Proposition 2.4(ii)) identifies this kernel with the one after adding or removing further punctures, as already proved in LM3 C.4. $\square$

### H.2. Proved — What centrality and torsion-freeness would require

Boggi's procongruence center theorem does not establish that $C_{3,0}$ is central or torsion-free in the full profinite completion. What it does imply is
$$
 Z(\widehat\Gamma_{3,0})\subseteq C_{3,0},
$$
because $Z(\check\Gamma_{3,0})=1$ by Boggi (2020, Theorem 4.4). Likewise, the full kernel lies in the centralizer (H.1), not necessarily in the center of $E$.

**Proof and conditional sharpening.** The image of a central element under a surjection is central, giving the inclusion. A centralizer of a normal subgroup need not centralize the whole ambient group; the implication that would prove centrality is missing. If a torsion-free finite-index congruence subgroup $\Gamma_{3,0}[3]$ is good and its completion has finite cohomological dimension at every prime, then $C_{3,0}$ is torsion-free: it is contained in that completion, and a nontrivial finite cyclic subgroup of order $p$ would force infinite $p$-cohomological dimension. The point is that torsion-freeness of the discrete level group alone is insufficient to deduce torsion-freeness of its completion. We do not prove the additional completion hypothesis here. Thus centrality and torsion-freeness of the full genus-three kernel are retained as unresolved assertions in this audit, rather than imported from the procongruence center formulas. $\square$

### H.3. Proved — Finite-cover homology representations are congruence representations

Let $\pi=\pi_1(S_3)$ and let $K\triangleleft\pi$ be characteristic of finite index. For $m\geq2$, put $L=[K,K]K^m$. Then $L$ is characteristic and of finite index in $\pi$, and the action of $\Gamma_3$ on the cover and on $H_1(K,\mathbf Z/m)$, with its unavoidable deck ambiguity, factors through
$$
                       \Gamma_3\longrightarrow\operatorname{Out}(\pi/L).
                                                               \tag{H.2}
$$
Every finite quotient obtained this way is therefore a congruence quotient. The same conclusion holds for a finite orbit of noncharacteristic covers after replacing their subgroups by a characteristic finite-index core.

**Proof.** Characteristicity of $L$ follows by applying every automorphism of $\pi$ to the characteristic subgroup $K$, its commutators and its $m$th powers. The quotient $K/L$ is the finite module $H_1(K,\mathbf Z/m)$, and $\pi/L$ remembers both this module and the deck quotient $\pi/K$. Thus an automorphism of $\pi$ trivial modulo $L$ is trivial on the indicated data. Changing a based representative by an inner automorphism acts by a deck transformation on the module, exactly the ambiguity named in the statement. For finitely many covers, there are only finitely many subgroups of each given index in the finitely generated group $\pi$; intersect their full automorphism orbits to obtain a characteristic finite-index subgroup $K$. Its subgroup $[K,K]K^m$ lies in the corresponding subgroup $[V,V]V^m$ for each cover subgroup $V$, giving the asserted factorization. $\square$

### H.4. Proved — An explicit finite congruence representation beyond base homology

Take $K=\ker(\pi_3\to H_1(S_3,\mathbf F_2))$ and $L=[K,K]K^3$. Then
$$
                       |\pi_3/L|=64\cdot3^{258}.        \tag{H.3}
$$
The congruence representation $\Gamma_3\to\operatorname{Out}(\pi_3/L)$ does not factor through the action on $H_1(S_3,\mathbf Z)$: a separating Dehn twist has nontrivial image.

**Proof and reproducible certificate.** Write
$$
\pi_3=\langle a_1,b_1,a_2,b_2,a_3,b_3\mid
[a_1,b_1][a_2,b_2][a_3,b_3]=1\rangle.
$$
The degree-64 characteristic cover has genus $1+64(3-1)=129$, whence $\dim H_1(K,\mathbf F_3)=258$, proving (H.3). To detect a twist, it suffices to use the double cover with monodromy $a_1\mapsto1,a_2\mapsto1$ and the other four generators mapping to zero. It has genus five. The twist about the curve $c=[a_1,b_1]$ is represented by conjugating $a_1,b_1$ by $c$ and fixing the other four generators. It fixes the defining surface relation and acts trivially on base homology.

The program `ceh_checks.py` computes signed lifted edge paths, equivalently evaluated Fox derivatives, over $\mathbf F_3$. For the cellular complex of the double cover it obtains
$$
(\dim C_0,\dim C_1,\dim C_2)=(2,12,2),\quad
\operatorname{rank}d_1=\operatorname{rank}d_2=1,
$$
and therefore $\dim H_1=10$. The induced operator $T$ satisfies
$$
\operatorname{rank}_{H_1}(T-1)=1,\qquad (T-1)^2=0,
\qquad T^3=1,\quad T\ne1.
$$
The complete $12\times12$ chain matrix is in `ceh_checks.json`; the program checks the chain-map identities and all displayed ranks by exact elimination modulo three. This homology action factors through $\pi_3/L$, since $K$ is contained in the double-cover subgroup. An inner automorphism of $\pi_3/L$ acts on the latter cover's abelianization through its deck group of order two. The nontrivial operator $T$ has order three, so it cannot arise from an inner automorphism. Thus the separating twist survives (H.2). Since it is in the Torelli group, (H.2) does not factor through the ordinary symplectic representation. $\square$

### H.5. Open — Genus-three kernel triviality, centrality, and torsion-freeness

The three residual assertions, for $C=C_{3,0}$, are
$$
 C=1,\qquad
 C\subseteq Z(\widehat\Gamma_{3,0}),\qquad
 C\text{ has no nontrivial element of finite order}.
$$
We have not proved or refuted any of these three assertions in this audit. Triviality would imply the other two. H.2 proves a center inclusion in the opposite direction and a conditional torsion-freeness criterion, but neither settles the corresponding residual assertion. For centrality the remaining implication is that the centralizer identified in H.1 centralizes the entire one-point mapping class group; for torsion-freeness it is the required control of finite subgroups in the full profinite completion, or the additional finite-cohomological-dimension hypothesis stated in H.2.

The finite quotients in H.3–H.4 are congruence by an explicit characteristic subgroup, and the calculation demonstrates information beyond the base symplectic quotient. It cannot detect a nontrivial $C_{3,0}$, because every quotient used factors through the very action defining congruence. No quantum representation quotient was constructed here. The smallest remaining structural assertion is $C_{\widehat\Gamma_{3,1}}(\widehat\pi_{3,0})=1$ in (H.1). A finite quotient witnessing failure would require a finite quotient of $\Gamma_3$ which does not factor through any characteristic finite quotient of $\pi_3$; calculations on homology of finite covers alone cannot provide one. Conversely, proving that all such cover-homology quotients are congruence, as we have done, supplies no cofinality statement among all finite quotients of $\Gamma_3$. This is the exact obstruction left after our attack.
