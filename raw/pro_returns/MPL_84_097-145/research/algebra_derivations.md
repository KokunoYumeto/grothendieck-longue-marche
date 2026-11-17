# Algebra derivations supporting A01–A40

These are independent mathematical checks prompted by the frozen text, not changes to that text. The page attributions, exact quotations, supplied-context comparisons, and limitations are in `algebra_notes.md`. Every displayed algebra below is commutative and unital. The calculations concern local algebra and the specifically stated descent argument; they make no literature-priority claim or identification of the entire category of \(\chi\)-trivialized extensions.

## 1. Relative norm for the rank-four tensor algebra

**Supports A07, A11–A13.** The product relation and trace agree with the supplied C84 items L172.1/L172.5; the additional calculation here is the relative quadratic form and its identities.

Let
\[
 A_1=R[u]/(u^2+b_1u+c_1),\qquad
 A_2=R[v]/(v^2+b_2v+c_2),\qquad B=A_1\otimes_R A_2,
\]
and put
\[
 C=b_1^2c_2+b_2^2c_1-4c_1c_2,\qquad
 A=R[t]/(t^2+b_1b_2t+C).
\]
The map in frozen scan 104 is
\[
 i:A\longrightarrow B,\qquad
 t\longmapsto w=2uv+b_1v+b_2u.
\]
In particular the relation has **plus** \(b_1b_2t\), consistently with the frozen input relations; no sign correction is needed.

Write \(\bar u=-b_1-u,\ \bar v=-b_2-v\), and let \(\bar{\ }\) on \(B\) act on both factors. The source's relative trace is the \(R\)-linear map
\[
 q(x_0+x_1u+x_2v+x_3uv)
 =2x_0-b_1x_1-b_2x_2+(t+b_1b_2)x_3.
\]
For \(\xi=x_0+x_1u+x_2v+x_3uv\), define
\[
\begin{aligned}
 N(\xi)={}&x_0^2+c_1x_1^2+c_2x_2^2+c_1c_2x_3^2\\
 &-b_1x_0x_1-b_2x_0x_2+(t+b_1b_2)x_0x_3\\
 &-t x_1x_2-b_2c_1x_1x_3-b_1c_2x_2x_3 .
\end{aligned}
\tag{1}
\]

### Why these are the required coefficients

The four diagonal values are \(N(1)=1,\ N(u)=c_1,\ N(v)=c_2,\ N(uv)=c_1c_2\), as on scan 103. The six mixed coefficients come from \(q(e_i\bar e_j)\), where \((e_0,e_1,e_2,e_3)=(1,u,v,uv)\):

| \(ij\) | \(q(e_i\bar e_j)\) |
|---|---|
| 01 | \(-b_1\) |
| 02 | \(-b_2\) |
| 03 | \(t+b_1b_2\) |
| 12 | \(-t\) |
| 13 | \(-b_2c_1\) |
| 23 | \(-b_1c_2\) |

For example,
\[
q(u\bar v)=q(-b_2u-uv)=b_1b_2-(t+b_1b_2)=-t,
\]
and
\[
q(u\overline{uv})=q(u\bar u\,\bar v)=c_1q(\bar v)=-b_2c_1.
\]
The diagonal polar values are \(q(e_i\bar e_i)=2N(e_i)\). Thus direct expansion gives
\[
 N(\xi+\eta)-N(\xi)-N(\eta)=q(\xi\bar\eta).
\tag{2}
\]
No halves of polar coefficients are taken, so this construction works over bases with two-torsion.

### The trace is \(A\)-linear

It suffices to check multiplication by \(i(t)=w\) on the \(R\)-basis of \(B\). Reduction by the two input relations gives
\[
\bigl(q(w),q(wu),q(wv),q(wuv)\bigr)
 =(2t,-b_1t,-b_2t,-C).
\]
These are exactly \(t\,(2,-b_1,-b_2,t+b_1b_2)\), since \(t(t+b_1b_2)=-C\) in \(A\). Therefore
\[
 q(i(a)\xi)=a\,q(\xi)\qquad(a\in A).
\tag{3}
\]
The two source trace identities \(iq(\xi)=\xi+\bar\xi\) and \(qi(a)=2a\) also follow on the same bases. The diagonal involution fixes \(i(A)\); the involution on either one input factor induces the canonical conjugation \(t\mapsto-b_1b_2-t\) of \(A\).

### A universal argument proves identities even when \(i\) later has a kernel

Expansion of (1), with \(t=w\), proves
\[
 i(N(\xi))=\xi\bar\xi.
\tag{4}
\]
To deduce the remaining identities without making an invalid cancellation over a degenerate base, first work over the **universal integer polynomial ring** in \(b_1,b_2,c_1,c_2\) and all coordinate variables under consideration. Both algebras are free over that ring. If \(i(a+dt)=0\), its tensor-basis coordinates are
\[
 (a,db_2,db_1,2d)=(0,0,0,0);
\]
the universal ring has no two-torsion, so \(d=a=0\), and \(i\) is injective there.

Over that universal ring,
\[
\begin{aligned}
i(N(\xi\eta))
 &=\xi\eta\,\overline{\xi\eta}\\
 &=(\xi\bar\xi)(\eta\bar\eta)
 =i(N(\xi)N(\eta)),
\end{aligned}
\]
hence \(N(\xi\eta)=N(\xi)N(\eta)\). Similarly, because \(\overline{i(a)}=i(a)\),
\[
i(N(i(a)))=i(a)^2,
\qquad\text{so}\qquad N(i(a))=a^2.
\]
These equalities are polynomial identities in the free rank-two target with its monic relation, hence specialize to **every** commutative \(R\), including those for which \(i\) ceases to be injective. This proves multiplicativity and
\[
 N(i(a)\xi)=a^2N(\xi)
\tag{5}
\]
without cancelling \(i\) after specialization. Combining (2), (3), and the fact that conjugation fixes \(i(A)\) also proves \(A\)-bilinearity of the polar form, so \(N\) is an \(A\)-quadratic map.

For a pure tensor \((a+bu)(c+dv)\), substitution
\[
(x_0,x_1,x_2,x_3)=(ac,bc,ad,bd)
\]
in (1) cancels the \(t\)-terms and gives
\[
 N((a+bu)(c+dv))
 =(a^2-b_1ab+c_1b^2)(c^2-b_2cd+c_2d^2),
\]
the required product of input norms.

### Transitivity and the scope of the source proof

Let \(\sigma_1,\sigma_2\) be the two factor involutions and \(\sigma_3=\sigma_1\sigma_2\). The absolute rank-four norm is the product of the four conjugates:
\[
 N_{B/R}(\xi)=\xi\,\sigma_1(\xi)\,\sigma_2(\xi)\,\sigma_3(\xi).
\]
This determinant identity can itself be checked universally, or by successively taking the two ordinary quadratic norms. Equivariance of (1), first over the universal ring by (4) and injectivity and then by specialization, gives
\[
N(\sigma_1\xi)=\overline{N(\xi)}=N(\sigma_2\xi).
\]
Applying \(i\) to \(N(\xi)\overline{N(\xi)}\) therefore gives the same product of four conjugates, proving
\[
 N_{A/R}(N(\xi))=N_{B/R}(\xi).
\tag{6}
\]
In the actual rank-two-input setting, the final quantities in (6) lie in \(R\), and \(R\to B\) is injective because \(B\) is locally free of positive rank. Thus the source's scalar comparison can also be justified directly without assuming \(i:A\to B\) injective; only the intermediate notation \(N(\xi)=\xi\bar\xi\) suppresses \(i\).

The formula is uniquely determined locally by the four diagonal values and the polar form. Once the intrinsic product \(A\) and trace \(q\) in the source construction are given, that uniqueness ensures that the local norm formulas agree on overlapping choices of input bases. This does not supply associators, symmetry constraints, or every compatibility for the wider extension category.

### Reproducible symbolic verification

Run from the workspace root:
```bash
python MPL_84_097-145/scripts/research_relative_norm.py
```

The saved report is `research/relative_norm_checks.json`. Seven checks are true: (4), (2), multiplicativity, \(A\)-linearity of \(q\), pure-tensor norms, restriction \(N\circ i=a^2\), and norm transitivity. The script reduces expressions using the monic relations over an integer polynomial coefficient ring; it never inverts a scalar parameter and never reads a scan or transcription file.

## 2. Fixed algebras on the two-factor and three-factor good loci

**Supports A06 and A29–A30.** These proofs concern the invariant-ring assertions of scans 102 and 117. They do not assert that the stated good locus is necessary point by point.

### Two factors

In the notation above, an element \(x=a+p u+q v+r uv\) is fixed by \(\sigma_1\sigma_2\) exactly when
\[
 2p=b_2r,\qquad 2q=b_1r,\qquad
 b_1p+b_2q=b_1b_2r.
\tag{7}
\]
The coordinates of \(i(a+dt)\) are \((a,db_2,db_1,2d)\). If two is a unit, take \(d=r/2\). If \(b_1\) is a unit, take \(d=q/b_1\); (7) then yields \(r=2d\) and \(p=b_2d\). The analogous choice works when \(b_2\) is a unit. In each case \(d\) is unique, so \(i\) identifies \(A\) with \(B^{\sigma_1\sigma_2}\).

For an actual quadratic algebra, the étale locus in a monic presentation is \(D(\delta_i)\), \(\delta_i=b_i^2-4c_i\); at a prime containing two, étaleness is equivalent to \(b_i\) being a unit in the local ring. Consequently scan 102's hypothesis gives the open cover
\[
 D(2)\cup D(b_1)\cup D(b_2).
\]
The preceding computations hold after arbitrary base change on these unit loci, establishing the NB's universal injectivity and image assertion. If desired, étaleness here is seen directly from the derivative \(2u_i+b_i\): its square is \(\delta_i\), so it is invertible precisely on \(D(\delta_i)\).

### Three factors when two is invertible

Write
\[
 B=A_1\otimes_R A_2\otimes_R A_3,\qquad
 \Gamma=\{(\epsilon_1,\epsilon_2,\epsilon_3)\in\mathbf F_2^3:
 \epsilon_1+\epsilon_2+\epsilon_3=0\}.
\]
Let \(v_i=2u_i+b_i\). Then \(\sigma_i(v_i)=-v_i\), and when two is invertible the eight monomials \(v_S=\prod_{i\in S}v_i\), \(S\subset\{1,2,3\}\), form an \(R\)-basis of \(B\). The character carried by \(v_S\) is trivial on \(\Gamma\) exactly for \(S=\varnothing\) or \(S=\{1,2,3\}\); for each other \(S\) an element of \(\Gamma\) negates the coefficient, and its being invariant forces that coefficient to vanish because two is a unit. Thus
\[
 B^\Gamma=R\cdot1\oplus R\cdot(v_1v_2v_3).
\]

Using the source's two-factor map twice, the iterated product generator \(z\) maps to
\[
\begin{aligned}
w_{123}={}&4u_1u_2u_3
 +2b_1u_2u_3+2b_2u_1u_3+2b_3u_1u_2\\
 &+b_1b_2u_3+b_1b_3u_2+b_2b_3u_1.
\end{aligned}
\]
The identity
\[
 v_1v_2v_3=2w_{123}+b_1b_2b_3
\tag{8}
\]
shows that \(1,w_{123}\) is also a basis of \(B^\Gamma\). The natural map from the rank-two contracted product to \(B^\Gamma\) is therefore an isomorphism.

### Three factors when two inputs are étale

Suppose \(A_1,A_2\) are étale. After the faithfully flat finite-free base change \(R'=A_1\otimes_R A_2\), both split. One can see the splitting directly for a quadratic étale algebra: its two roots in itself differ by the unit \(2u_i+b_i\), so the two evaluation maps identify its self-base-change with a product of two copies.

It is consequently enough to take \(A_1=A_2=R\times R\), use presentations \(u_i^2-u_i=0\), and write
\[
 B\cong \prod_{(i,j)\in\mathbf F_2^2} A_3.
\]
The element \((\epsilon_1,\epsilon_2,\epsilon_1+\epsilon_2)\in\Gamma\) translates the pair of indices by \((\epsilon_1,\epsilon_2)\) and conjugates the \(A_3\)-entry \(\epsilon_1+\epsilon_2\) times. An invariant tuple is therefore determined by its \((0,0)\)-entry \(a\), the other entries being \(\sigma_3^{\,i+j}(a)\). Evaluation at \((0,0)\) is an algebra isomorphism \(B^\Gamma\cong A_3\).

For these split inputs \(b_1=b_2=-1,\ c_1=c_2=0\), their product has \(b_{12}=1,c_{12}=0\), and its product with \(A_3\) has the same monic equation as \(A_3\). Evaluation of \(w_{123}\) at \(u_1=u_2=0\) gives \(u_3\). The natural map to the invariants is thus the identity under these identifications.

Finally, invariants under this finite group are the kernel of the linear map
\[
 B\longrightarrow\prod_{\gamma\ne1}B,\qquad
 b\longmapsto(\gamma b-b)_{\gamma\ne1},
\]
so they commute with this flat base change. An isomorphism is detected after faithfully flat base change by testing its kernel and cokernel. This descends the split calculation and proves the invariant assertion on
\[
 D(2)\ \cup\ D(\delta_1\delta_2)\
 \cup\ D(\delta_2\delta_3)\
 \cup\ D(\delta_3\delta_1),
\tag{9}
\]
which is precisely the complement of the exceptional set stated on scan 117.

## 3. Five axioms without multiplicative norm

**Supports A14, A19–A20.** This is an example about scan 110's five displayed axioms. It does not alter the definition or assert that the author's intended complete axioms were necessarily the same as the earlier list.

Let
\[
 k=\mathbf Z/4,\qquad A=\mathbf F_2[e,f]/(e^2,f^2),
\]
with the reduction scalar map \(\alpha:k\to A\). Write
\[
 x=a+be+cf+d\,ef,\qquad a,b,c,d\in\{0,1\},
\]
and set
\[
 t(x)=2a\pmod4,\qquad n(x)=a+2d\pmod4.
\tag{10}
\]

### Direct verification of the five axioms

The trace is additive because twice the binary sum and the ordinary sum agree modulo four. It is \(k\)-linear: an even scalar acts by zero on \(A\) and kills \(2a\), while an odd scalar acts by the identity on \(A\) and fixes \(2a\). Also \(t(1)=2\).

Since \(\alpha(t(x))=0\), conjugation is \(\bar x=-x=x\) in the characteristic-two algebra \(A\). It is thus an involutive algebra automorphism fixing one. Every nonconstant basis monomial squares to zero and cross terms cancel, so
\[
 x^2=a.
\tag{11}
\]

For scalar homogeneity, if \(\lambda\) is even then \(\lambda x=0\) and \(\lambda^2=0\) in \(k\); if \(\lambda\) is odd then \(\lambda x=x\) and \(\lambda^2=1\). Hence \(n(\lambda x)=\lambda^2n(x)\).

For \(y=a'+b'e+c'f+d'ef\), use
\[
 a\mathbin{\mathrm{xor}}a'=a+a'-2aa',\qquad
 2(d\mathbin{\mathrm{xor}}d')=2d+2d'\pmod4.
\]
It follows that
\[
 n(x+y)-n(x)-n(y)=2aa'=t(xy)=t(x\bar y).
\tag{12}
\]
Finally \(n(1)=1\), and (10)–(11) give
\[
 \alpha(n(x))=a=x\bar x.
\]
This verifies all five axioms by hand.

Nevertheless
\[
 n(e)=n(f)=0,\qquad n(ef)=2,
\]
so \(n\) is not multiplicative. The failure also occurs on units: \((1+e)^2=(1+f)^2=1\), but
\[
 n((1+e)(1+f))=n(1+e+f+ef)=3
 \ne1=n(1+e)n(1+f).
\tag{13}
\]
Thus the five displayed axioms strictly weaken the earlier axiom system containing scan 108(b); the multiplicativity condition is not redundant when \(\alpha\) may have a kernel.

### The example is a quadratic law, not merely a finite-point anomaly

Let \(S\) be **any** commutative \(k\)-algebra. Then \(4=0\) in \(S\) and
\[
 A_S=A\otimes_k S
 \cong (S/2S)[e,f]/(e^2,f^2).
\]
For \(x=a+be+cf+d\,ef\) with coefficients in \(S/2S\), choose lifts \(\widetilde a,\widetilde d\in S\), and define
\[
 t_S(x)=2\widetilde a,\qquad
 n_S(x)=\widetilde a^{\,2}+2\widetilde d^{\,2}.
\tag{14}
\]
Changing a lift by \(2s\) changes its square by \(4s\widetilde a+4s^2=0\); the same argument applies to the \(d\)-term. Both maps are therefore independent of the lifts, and the formulas are natural in \(S\).

Formula (14) is homogeneous of degree two, with polar form
\[
 n_S(x+y)-n_S(x)-n_S(y)
 =2\widetilde a\,\widetilde a',
\]
since the polar contribution from \(2\widetilde d^{\,2}\) is \(4\widetilde d\widetilde d'=0\). The trace is \(S\)-linear, \(\bar x=x\), and
\[
 \alpha_S(n_S(x))=a^2=x^2,\qquad
 t_S(x\bar y)=2\widetilde a\,\widetilde a'.
\]
The unit conditions also persist. At \(S=\mathbf Z/4\), every binary lift satisfies \(\widetilde a^2=a\) and \(2\widetilde d^2=2d\), recovering (10). Thus the counterexample remains valid even when “quadratic” is understood as a natural quadratic polynomial law rather than only a quadratic map on the original finite set.

### Reproducible finite verification

Run:
```bash
python MPL_84_097-145/scripts/research_algebra_checks.py
```

The `quasiquadratic_five_axioms` section of `research/algebra_checks.json` records all nine elementary checks used to represent the five axioms, over all four scalars and sixteen algebra elements. All checks pass. Among all 256 ordered pairs, 96 fail norm multiplicativity, including both (13) and the nonunit witness \(e,f\). The enumeration corroborates the proof; it is not the sole justification.

## 4. A large fixed algebra with scalar contracted-product image

**Supports A31–A32.**

Over \(k=\mathbf F_2\), set
\[
 A=k[e,f]/(e^2,f^2),\quad
 A_1=k[e],\quad A_2=k[f],\quad A_3=k[e+f].
\]
Each \(A_i\) is a dual-number algebra. Every pair generates \(A\), with bases
\[
 (1,e,f,ef),\quad (1,e,e+f,ef),\quad
 (1,f,e+f,ef),
\]
so every pair tensor map is an isomorphism.

In particular \(A/A_1\) is quadratic with basis \(1,f\) and relation \(f^2=0\); the analogous statements hold for the other two subalgebras. All these quadratic structures have trace zero and norm \(x\mapsto x^2\). A general element \(x=a+be+cf+d\,ef\) squares to \(a\in k\), so the norms land in each \(A_i\), their restrictions agree with the input norms, and the relative involutions are all identities. All the required cross-trace, cross-norm and involution compatibilities therefore hold; in fact both the input and relative algebras are actual free rank-two algebras here.

The resulting \(\Gamma\)-action is trivial, and
\[
 A^\Gamma=A,\qquad \dim_k A^\Gamma=4.
\]
On the other hand, each input has parameters \(b_i=c_i=0\) in characteristic two. The source's product equation gives the contracted triple algebra \(k[t]/(t^2)\), while the iterated generator map sends \(t\) to zero. Its image in \(A\) is exactly \(k\), and \(t\mapsto0\) supplies the desired section.

This distinguishes two statements: \(A^\Gamma=k\) fails, while the particular contracted-product map has scalar image. The former was only a sufficient condition on scan 118, so this example illustrates the author's qualification without refuting the desired section statement. The script checks each of the three pair bases by enumerating its span and verifies the square formula.

## 5. A finite surjective universal map that is not flat

**Supports A38–A39.**

Take three independent dual-number inputs over \(k=\mathbf F_2\). The full tensor algebra and contracted triple algebra are
\[
 B=k[e,f,g]/(e^2,f^2,g^2),\qquad
 B_0=k[t]/(t^2).
\]
The source's iterated generator formula has every coefficient zero in this specialization, so \(B_0\to B\) sends \(t\) to zero. Thus \(B\), of \(k\)-dimension eight, is finite over \(B_0\). Both rings are nonzero local Artin rings with one-point spectra, so the morphism of spectra is surjective.

Let \(I=(t)\subset B_0\). As a \(B_0\)-module, \(I\simeq B_0/(t)=k\), whereas \(tB=0\), and hence
\[
 I\otimes_{B_0}B\simeq B/tB=B\ne0.
\]
Tensoring the injection \(I\hookrightarrow B_0\) with \(B\) gives the multiplication map
\[
 I\otimes_{B_0}B\longrightarrow B,\qquad
 t\otimes b\longmapsto tb=0.
\]
It is the zero map from a nonzero module and therefore is not injective. This proves that \(B\) is not flat over \(B_0\).

The fibre of the universal morphism over the section \(t=0\) is
\[
 B\otimes_{B_0}k=B,
\]
of dimension eight, whereas a free rank-four \(B_0\)-module would have four-dimensional fibre. Equivalently, multiplication by \(t\) has rank zero on this eight-dimensional \(k\)-space, while on \(B_0^{\,4}\) it would have rank four. The script records the eight monomials, the fibre dimension, and this action.

The example substantiates scan 122's nonflatness warning. It does not disprove the proposed quasi-quadratic structures, because the author explicitly removed flatness and local-freeness requirements on scan 107; their trace/norm constructions are separate unfinished requirements.

## 6. The transitive-subschema lemma: two independent tests

**Supports A35–A36.** These tests use the frozen first reading, not a visual rereading.

1. **Ambient target.** For \(J=\{\ast\}\), trivial group action, \(k=\mathbf Z\), and \(\mathcal X=\operatorname{Spec}\mathbf F_2\subset X_J=\operatorname{Spec}\mathbf Z\), the map \(k\to\Gamma(X_J,\mathcal O)=k\) is injective and the subscheme is stable, yet \(\mathcal X\ne X_J\). Thus the ambient target on scans 120–121 cannot be the condition needed by the ideal argument.
2. **Closedness.** Even replacing that target by \(\Gamma(\mathcal X,\mathcal O)\), the stable open subscheme \(D(2)\subset\operatorname{Spec}\mathbf Z\) has injective global scalar map and is proper. Arbitrary subschemes do not satisfy the asserted conclusion.

For a **closed** \(\Gamma\)-stable subscheme \(\mathcal X\subset\bigsqcup_{j\in J}\operatorname{Spec}k\), let its component ideals be \(I_j\). Transitivity and the specified action on the components identify all \(I_j\). The kernel of
\[
 k\longrightarrow\Gamma(\mathcal X,\mathcal O_{\mathcal X})
 =\prod_{j\in J} k/I_j
\]
is \(\bigcap_j I_j\); if this map is injective, the common ideal is zero, and every component equals \(\operatorname{Spec}k\). This is the argument the source writes. In its original application the generation hypothesis on scan 119 already gives a closed immersion, so the standalone lemma's imprecision does not eliminate that hypothesis from the application.

