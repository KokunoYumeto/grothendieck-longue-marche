# Reconstruction over solvable closures of finitely generated fields

**Status:** independently reviewed by root and the finite-field agent; integrated as F.43 in `sections/F_solvable_closure_extension.tex`. This candidate is retained as the detailed pre-integration audit. The proposed result is a strict sufficient-field-class enlargement of F.37, not an intrinsic classification or a converse to the reconstruction theorem.

## Proposed theorem and notation

Let \(K/\mathbf Q\) be any finitely generated field, choose an algebraic closure, and let \(k=K^{\mathrm{solv}}\) be its maximal Galois prosolvable extension. For every subfield \(k_0\) of a finitely generated extension of \(k\), closed-point-preserving étale-topos reconstruction holds over \(k_0\): for all finite-type \(k_0\)-schemes \(X,Y\),
\[
 \operatorname{Hom}_{k_0}(X^{\mathrm{awn}},Y)
 \longrightarrow
 \pi_0\operatorname{Hom}^{\mathrm{cp}}_{BG_{k_0}}
       (X_{\mathrm{et}},Y_{\mathrm{et}})
\]
is bijective.

The convention is the corrected CHW closed-point-preserving convention, not the literal incomplete R27 definition refuted earlier. The result includes \(\mathbf Q(t)^{\mathrm{solv}}\), which does not embed in any finitely generated extension of \(\mathbf Q^{\mathrm{solv}}\). Thus it is strictly stronger than F.37 as a sufficient field class.

Write \(D(F^\times)=\bigcap_{n\ge1}(F^\times)^n\). All composita below are taken in fixed compatible algebraic overfields. A finitely generated field is finitely generated as a field, not necessarily as an algebra.

## 1. Constants, divisibility, and missing number fields

### 1.1 Elementary Galois compositum fact

For a Galois extension \(E/F\) and any common-overfield extension \(L/F\), restriction gives
\[
 \operatorname{Gal}(EL/L)\simeq
 \operatorname{Gal}(E/(E\cap L)).
\]
This includes infinite Galois extensions: the restriction image is compact and hence closed, and its fixed field in \(E\) is \(E\cap L\). The infinite Galois correspondence proves surjectivity. This precise statement is opened in Milne (2022), Proposition 7.15, printed p. 99, with the compatible-embedding extension Corollary 7.16 on the same page. It will be used with finite normal constant fields and with prosolvable extensions; no normality of \(K/\mathbf Q\) is assumed.

### 1.2 Exact algebraic constants of the solvable closure

Let \(C=K\cap\overline{\mathbf Q}\). It is a number field, by finiteness of the relative algebraic closure in a finitely generated extension (Stacks Project, Lemma 9.26.11, tag 030D). The extension \(K/C\) is regular. In the characteristic-zero setting needed here this can be seen directly: for any finite Galois \(N/C\) inside \(\overline{\mathbf Q}\), one has \(N\cap K=C\), and the compositum fact makes \(K,N\) linearly disjoint over \(C\).

We claim
\[
             K^{\mathrm{solv}}\cap\overline{\mathbf Q}
                         =C^{\mathrm{solv}}.                 \tag{G1}
\]
If \(N/C\) is finite Galois solvable, then \(KN/K\) has the same Galois group, so \(N\subset k\). This proves one inclusion. Conversely, let \(a\in k\cap\overline{\mathbf Q}\). Choose a finite Galois solvable extension \(E/K\) in \(k\) containing \(a\). Let \(N/C\) be the normal closure of \(C(a)/C\). Regularity says that all \(C\)-conjugates of \(a\) are also its \(K\)-conjugates. Since \(E/K\) is normal, \(N\subset E\). The group
\(\operatorname{Gal}(N/C)\simeq\operatorname{Gal}(KN/K)\)
is a quotient of the solvable group \(\operatorname{Gal}(E/K)\). Thus \(N\subset C^{\mathrm{solv}}\), proving (G1).

There are finite extensions of \(C^{\mathrm{solv}}\) of unbounded degree inside \(\overline{\mathbf Q}\). For each \(n\ge5\), specialize the generic \(S_n\)-polynomial over the Hilbertian number field \(C\). If \(N/C\) is the resulting \(S_n\)-Galois extension, then
\[
 N\cap C^{\mathrm{solv}}=N^{A_n}.
\]
Indeed a solvable quotient of \(S_n\) kills its stable derived subgroup \(A_n\), while its quadratic quotient already belongs to the solvable closure. The residual degree is \(|A_n|\). This uses exactly the Hilbert and finite-group inputs already opened in F.18/F.34 (Serre, 2007, Proposition 3.3.1, Theorem 3.4.1 and finite-extension preservation Corollary 3.2.2).

By (G1) and the Galois compositum fact,
\[
 [k\overline{\mathbf Q}:k]
       =[\overline{\mathbf Q}:C^{\mathrm{solv}}]=\infty.
\]
If \(L/k\) is finitely generated, its relative algebraic subfield over \(k\) is finite. Thus \(L\) cannot contain \(\overline{\mathbf Q}\). In particular there is a finite Galois **number field** \(N_0/\mathbf Q\) not contained in \(L\). This last conclusion is what is needed for the arithmetic-prime construction; a merely geometric finite extension of \(K\) would not suffice for that argument.

### 1.3 Divisible elements in all finite extensions

The field \(k\) contains every root of unity and \(k^\times\) is divisible. For \(a\in k\), put \(a\) into a finite solvable Galois \(E/K\). Adjoin the required roots of unity and \(n\)-th roots of all \(K\)-conjugates of \(a\). Over the resulting field containing the roots of unity, the radical group is abelian, and its normal closure over \(K\) remains a solvable extension. Hence every \(n\)-th root can be chosen in \(k\).

Every finitely generated field \(F/\mathbf Q\) satisfies \(D(F^\times)=\{1\}\). On a normal projective model over its finite field of algebraic constants, an infinitely divisible element and all its roots have divisor zero, so they are constants. For a number field, all finite valuations then vanish, and the unit theorem reduces the intersection of all power subgroups to that of a finitely generated abelian group, which is trivial.

Now let \(E/k\) be finite and enlarge it to \(Mk/k\), where \(M/K\) is finite Galois. Put \(B=M\cap k\). Both extensions over \(B\) are Galois and disjoint, so the restrictions to \(M\) and \(k\) commute. For a fixed \(a\in Mk\), choose a finite field \(S/K\) inside \(k\), containing \(B\), such that \(a\in F=MS\). The field \(F\) is finitely generated over \(\mathbf Q\), and is fixed before a root level is chosen.

If \(z^n=a\) with \(z\in Mk\), and \(\sigma\in\operatorname{Gal}(Mk/k)\), then for every \(\tau\in\operatorname{Gal}(Mk/F)\),
\[
 \tau z/z\in\mu_n\subset k,\qquad
 \tau(\sigma z/z)
   =\frac{\sigma(\tau z/z)}{\tau z/z}\,\sigma z/z
   =\sigma z/z.
\]
Consequently \(\sigma z/z\in F\), and \(\sigma a/a\in(F^\times)^n\). If \(a\in D((Mk)^\times)\), this holds for every \(n\); \(D(F^\times)=1\) gives \(\sigma a=a\), so \(a\in k\). The reverse inclusion follows from divisibility of \(k^\times\). Therefore
\[
                 D(E^\times)=k^\times                     \tag{G2}
\]
for every finite \(E/k\).

For a finitely generated \(L/k\), use a normal projective model over \(k\). Its global functions form the finite relative algebraic closure \(k'\) of \(k\) in \(L\). The divisor argument puts an infinitely divisible element and every one of its roots into \(k'\). Equation (G2) then gives
\[
                 D(L^\times)=k^\times.                    \tag{G3}
\]
The same conclusion holds after every finite extension of \(L\).

### 1.4 Finite-generation and normality in every descent

Given finitely generated \(L/k\) and finite data over \(L\), choose generators of \(L/k\), and include the finitely many coefficients, points, maps, relations, and elements of \(k\) occurring in the data. Together with \(K\), they generate a field \(F\subset L\) finitely generated over \(\mathbf Q\), satisfying
\[
                         K\subset F,\qquad L=Fk.
\]
The extension \(L/F\) is Galois and prosolvable, as the base change of \(k/K\). Its Galois group is a closed subgroup of \(\operatorname{Gal}(k/K)\); no assertion that \(k/\mathbf Q\) is Galois is needed. Finite extensions of \(L\) and a finite set of their elements can similarly be written inside \(Mk\) for an \(M/F\) finite extension after enlarging \(F\) by finitely many algebraic elements of \(k\). Thus \(M\) remains finitely generated over \(\mathbf Q\).

## 2. Detection of finite arithmetic quotients

The conclusion of F.34 holds for every finitely generated \(L/k\). Here are the full arithmetic predicates behind that reuse.

Descend a smooth geometrically connected curve \(U/L\) and a connected finite \(G\)-torsor, including its full action and torsor identity, to \(F/\mathbf Q\) as in 1.4. If \(M/F\) is its finite Galois constant field, connectedness after base change gives \(M\cap L=F\). Write \(1\to N\to G\to P\to1\), where \(P=\operatorname{Gal}(M/F)\).

The geometric pencil of F.24 over \(F\), for unbounded degree \(n\ge5\), gives a Galois closure with group
\[
 H\subseteq(G\times_P\cdots\times_PG)\rtimes S_n.
\]
The spanning-tree gauge and the support-at-most-two commutators prove \(A_n\subset H^\infty\) and surjectivity of \(H^\infty\cap N^n\to N\) at every coordinate. These are the same discrete geometric calculations: \(F\) is finitely generated over \(\mathbf Q\), hence embeds in \(\mathbf C\), so the comparison and branch-loop arguments apply. No complete wreath-product assertion is made.

The finitely generated field \(F/\mathbf Q\) is Hilbertian by the exact rational-function and finite-extension argument of F.34. Specialize with full group \(H\), obtaining \(\Omega/F\). Since \(L/F\) is Galois prosolvable,
\[
 J=\operatorname{Gal}(\Omega L/L)\supset H^\infty.
\]
Also \(J\to P\) is onto because \(M\cap L=F\). Its coordinate stabilizer maps onto \(G\): the support-two commutators supply \(N\), and a literal even permutation moves the selected block back without changing a specified \(P\)-image. This proves that one closed point detects the entire prescribed finite arithmetic quotient. The degree-\(n\) fibre is a single point because \(A_n\) is transitive, giving unbounded degrees as well.

For smooth quasiprojective sources of larger dimension, the geometric-component-preserving Bertini reduction of F.29 applies. Each good hyperplane open has an \(L\)-point since \(L\) is infinite, and the geometric components remain irreducible while their arithmetic permutation remains transitive. This retains the entire finite arithmetic quotient on a smooth curve. Thus the detection statement used by the normalized Kummer-spanning argument holds in all the dimensions required below.

## 3. Punctured-line integrality: the normality check that changes

Let \(U\subset\mathbf G_{m,L}\) be nonempty open, with irreducible puncture polynomials \(P_0=T,P_1,\ldots,P_r\). Suppose a compatible Kummer class has actual values at every point over every finite extension of \(L\). Choose an \(L\)-point \(x_0\), an actual value \(b_0\), and write it as
\[
 \kappa(b_0)+\sum_j\lambda_j
       \bigl([P_j(T)]-[P_j(x_0)]\bigr),\qquad
 \lambda_j\in\widehat{\mathbf Z}.
\]
This uses only the unit group and vanishing Picard group of a localized principal ideal domain, not any arithmetic property of \(k\).

Choose \(F_0\supset K\), finitely generated over \(\mathbf Q\), with \(L=F_0k\) and containing the coefficients and normalizing data. Let \(t_1,\ldots,t_d\) be a transcendence basis of \(F_0/\mathbf Q\). By1.2 choose a finite Galois number field \(N_0/\mathbf Q\) not contained in \(L\). Take \(M/\mathbf Q(t_1,\ldots,t_d)\) finite Galois containing \(F_0,N_0\), and all roots of the \(P_j\). Then \(Mk/L\) is finite Galois. Choose \(\sigma\in\operatorname{Gal}(Mk/L)\) acting nontrivially on \(N_0\). It preserves \(M\) because it fixes the displayed rational function field and \(M\) is normal over that field.

Put \(C_M=M\cap\overline{\mathbf Q}\). This is a finite Galois number field over \(\mathbf Q\), by the same normality argument as in F.35, and \(\sigma|_{C_M}\ne1\). Thus the arithmetic split-prime/Gauss construction of F.35 applies verbatim to \(M\): a normal finite étale model over
\[
 \mathcal O_{C_M}[S^{-1}]
       [t_1,\ldots,t_d,1/f],\qquad f\in\mathbf Z[t_1,\ldots,t_d],
\]
may be chosen \(\sigma\)-stable, with the required polynomial derivatives and resultants units. Choose distinct rational primes completely split in \(C_M\), excluding the finite bad set. At a prime over each, an unramified Gauss prolongation \(v_i\) has \(v_i(p_i)=1\) and is distinct from \(\sigma^{-1}v_i\), because the two restrictions to the completely split constant field differ. For \(d>0\) its residue field is infinite; for \(d=0\) use primes larger than the finite root-count bound.

In the resulting semilocal Dedekind ring, CRT imposes
\[
 \alpha\equiv r_i+p_i\pmod {\mathfrak p_{v_i}^2},\qquad
 \alpha\equiv c_i\pmod {\mathfrak p_{\sigma^{-1}v_i}},
\]
where \(r_i\) is a root of \(P_i\) and \(c_i\) avoids every reduced \(P_j\)-root. Because \(\sigma\) fixes all coefficients, though it may permute roots, Taylor expansion gives
\[
 v_i(P_j(\alpha))=\delta_{ij},\qquad
 v_i(P_j(\sigma\alpha))=0.
\]
Thus \(R_j=P_j(\sigma\alpha)/P_j(\alpha)\) has \(v_i(R_j)=-\delta_{ij}\), and \(\alpha\in U(Mk)\).

Let \(b_\alpha\in Mk\) be the actual prescribed value. Choose a finite extension \(S_0/K\) contained in \(k\) such that \(F=MS_0\) contains \(b_\alpha\). Now \([F:M]<\infty\), \(F/\mathbf Q\) is finitely generated, and \(F\) is fixed independently of every radical level. It is also \(\sigma\)-stable.

For \(z^n=a\in F^\times\), \(z\in Mk\), and \(\tau\in\operatorname{Gal}(Mk/F)\), one has \(\tau z/z\in\mu_n\subset k\). The two automorphisms commute: on \(M\), \(\tau\) is the identity and \(\sigma\) preserves \(M\); on \(k\), \(\sigma\) is the identity and \(\tau\) preserves \(k\). The last assertion follows because \(\tau\) fixes \(K\subset M\) and \(k/K\) is Galois. This is the precise replacement for the earlier use of normality over \(\mathbf Q\). Therefore \(\sigma z/z\in F\), since \(Mk/F\) is Galois, and \(\sigma a/a\in(F^\times)^n\).

Applying this to the Kummer evaluation relation gives, for integer representatives \(a_{j,n}\) of \(\lambda_j\bmod n\),
\[
 \frac{\sigma b_\alpha}{b_\alpha}
       \prod_jR_j^{-a_{j,n}}\in(F^\times)^n.
\]
The integer characters \(v_i\circ N_{F/M}\) yield
\[
 [F:M]\lambda_i
   =-(v_i\circ N_{F/M})(\sigma b_\alpha/b_\alpha)\in\mathbf Z
       \quad\hbox{inside }\widehat{\mathbf Z}.
\]
Hence \(\lambda_i\in\mathbf Q\cap\widehat{\mathbf Z}=\mathbf Z\). The class is the actual unit
\[
 h(T)=b_0\prod_j
       \left(P_j(T)/P_j(x_0)\right)^{\lambda_j}.
\]
At every finite-extension point its prescribed value differs from \(h\) by an element of \(k^\times\), by (G3). This proves the full replacement for F.35.

## 4. Generalized Albanese: the same finite arithmetic span, with the new base checked

Let \(X/L\) be smooth, geometrically connected and affine, with an \(L\)-point \(x_0\). Suppose a compatible Kummer class has actual multiplicative values over all finite-extension points. We prove that it is the class of an actual regular unit. The reduction of F.36 uses only the hypotheses verified below.

After a finite extension splitting the boundary of a smooth compactification, descend \(X,x_0\), its generalized Albanese \(A\), and all needed finite data to a finitely generated \(F/\mathbf Q\) containing \(K\), with \(L=Fk\). The integral comparison of Spiess–Szamuely used in F.30 applies in characteristic zero:
\[
 H^1(X_{\bar L},\mathbf Z_\ell(1))
       \simeq\operatorname{Hom}(T_\ell A,\mathbf Z_\ell(1)).
\]
Its finite geometric-abelian-fundamental-group kernel is annihilated by Hom into the torsion-free target, so there is no integral saturation assumption here. Smooth projective compactification and the integral comparison do not require a number-field base.

Put \(H=G_L\triangleleft G_F\) and \(W=(V_\ell A)_H\). Its lattice is the image of \(T_\ell A\). Because \(\mu_\infty\subset k\subset L\), the normalized geometric functional defines an arithmetic homomorphism on the split fundamental-group extension, with zero value on the section at \(x_0\). The projected point Kummer homomorphisms span \(W\): otherwise an annihilating nonzero integral functional would give a nonzero finite quotient of \(\pi_1(X)\) trivial on every closed-point decomposition group, contradicting Section 2.

Choose finitely many such point images spanning \(W\). Their coordinates, normalizing value \(b_0\), and actual values \(\beta_i\) lie in a finitely generated field \(M/\mathbf Q\) finite over the chosen descent field after adjoining finitely many elements of \(k\). This uses 1.4; those elements are algebraic over the fixed finitely generated \(K\). On restriction to \(G_{Mk}\), the rational spans are unchanged because this group has finite index in each selected point group and the projected Kummer maps are homomorphisms.

For \(g\in G_M\) and \(h\in G_{Mk}\), the projected conjugation identities are
\[
 c_i(ghg^{-1})=g c_i(h),\qquad
 \kappa(\beta_i/b_0)(ghg^{-1})
       =\chi(g)\kappa(\beta_i/b_0)(h).
\]
They hold because the points and values are defined over \(M\); the coboundary term in the first cocycle identity vanishes in the \(H\)-coinvariants. Normality of \(G_L\) in \(G_F\) preserves this quotient. Equality of the normalized pullback with the point evaluations makes the functional \(G_M\)-equivariant on the spanning images and therefore on all of \(W\).

Jannsen's integral Tate-Hom theorem for 1-motives over the finitely generated field \(M\) now applies, exactly as in F.36. The opened original is Theorem 4.3(ii), p.676, not the different numbering in a later citation. Applied to \([0\to A]\) and \([0\to\mathbf G_m]\), it identifies the functional with
\(\operatorname{Hom}_M(A,\mathbf G_m)\otimes\mathbf Z_\ell\).
After the boundary is split, its normalized geometric unit lattice is defined over the descent field: a fixed divisor and value 1 at \(x_0\) determine the unit. The Albanese universal property thus places the compatible Kummer class in this fixed lattice tensored with \(\widehat{\mathbf Z}\), plus its actual constant value at \(x_0\). This removes the Picard-Tate component of this particular point-theoretic class. It does not say the entire Picard-Tate module vanishes.

On a curve, the Riemann–Roch norm-to-a-punctured-line construction of F.27 isolates each boundary residue. The finite-map norm preserves actual point values, and Section 3 makes the residue an ordinary integer. Residue degrees, not ramification indices, are used; the selected rational boundary point contributes degree 1. The injective integral divisor matrix of a unit basis then makes every unit exponent an integer.

In higher dimension, choose a transverse smooth complete-intersection curve through a smooth point of each boundary component, avoiding the other components. At each finite level a local Kummer class is represented after étale localization by \(u z^a\); transversality carries \(z\) to a uniformizer and preserves that residue. The curve result therefore makes all global residues integral, and the same divisor matrix proves integral unit exponents.

The resulting unit \(h\) is normalized by \(h(x_0)=b_0\). A finite Galois descent extension used in these constructions introduces no gap: the quotient of a conjugate unit by \(h\) has zero divisor on a proper completion, hence is constant, and equals 1 at \(x_0\). Thus \(h\) descends. At every finite Kummer level the remaining class is geometrically zero, so the low-degree Hochschild–Serre sequence makes it a constant class; evaluation at \(x_0\) kills it. This proves \(\xi=\kappa(h)\) over \(L\).

## 5. Point functions and the full CHW criterion

For a pinned relative map from a smooth affine curve to \(\mathbf G_m\), the preceding result and (G3) give
\[
                   \phi(x)=c_x h(x),\qquad c_x\in k^\times.
\]
The constants here need not be algebraic over \(\mathbf Q\). That is harmless: the pole-degree argument of F.28 requires only that they belong to the fixed subfield \(k\subset L\).

If \(h\) is nonconstant, pull back \(T-1\) on the nonempty inverse-image open and obtain an actual unit \(h_1\) by Section 4. A closed point of degree over \(L\) greater than the pole bound, available by Section 2, makes
\(c_xh-d_xh_1-1\) vanish identically. Hence \(h_1=Ah+B\) with \(A,B\in k^\times\). At every point with \(h(x)\notin k\), comparison of the two coefficients gives \(c_x=-A/B\), independent of \(x\). For each \(b\in k^\times\), repeating this argument on the inverse-image open of \(T-b\ne0\) gives \(h_b=e_b(ch-b)\). If \(h(x)\in k\), take \(b=ch(x)\ne0\). Were \(\phi(x)\ne b\), the point would lie in that open while the regular unit \(h_b\) vanished there. Thus the same equality holds at these remaining points. Nonconstancy of the point function ensures the opens used are nonempty, exactly as in F.28.

If the Kummer unit \(h\) is constant, all point values lie in \(h k^\times\subset L^\times\). By1.2 a proper finite extension can be chosen containing a \(\beta\) with \(\beta/h\notin k\). All preceding arguments are stable under that extension. The values avoid \(\beta\), so \(T-\beta\) pulls back on the entire curve. Its actual unit \(h_\beta\) evaluates in the base field at every closed point, since both the value and the residual scalar lie there. Points of degrees exceeding the degree of a nonconstant rational function force \(h_\beta\) to be constant. Comparing its values at \(x\) and \(x_0\) gives
\[
              \frac{\phi(x)-\beta}{\phi(x_0)-\beta}\in k.
\]
Since \(\beta/h\notin k\), this implies \(\phi(x)=\phi(x_0)\). The closed-subtopos argument excludes a generic-point-only exception: the inverse image of the excluded closed target point is closed, and any nonempty closed subset of a noetherian curve has a closed point.

For higher-dimensional \(X\), after making a given geometric point rational by a finite extension choose a smooth geometrically connected curve through it and \(x_0\). The curve's point-function unit and the restriction of \(h\) have the same Kummer class. Their quotient has zero divisor, hence is constant on a proper completion, and its normalized value at \(x_0\) is1. The two units agree. Consequently the complete geometric-point function of \(\phi\) is that of a unique regular unit. Finite-extension descent follows from uniqueness. Dimension zero is the field-source statement; dimension one was treated above.

This is exactly CHW Theorem 4.18(5): a regular affine connected finite-type source with a rational point and a pinned relative map to \(\mathbf G_m\) has an algebraic geometric-point function. In characteristic zero such a source is smooth; connectedness and the rational point give geometric connectedness. No amenability assumption belongs to that theorem. The theorem therefore gives the full all-scheme Hom statement over every finitely generated \(L/k\). This use of CHW, rather than point-function equality alone, supplies the full étale-chart comparison.

## 6. Arbitrary subfields: a separate relative-constants descent

There is an actual change from F.37 at this step. If \(K\) has positive transcendence degree and \(k_0\subset L\), the extension \(k_0K^{\mathrm{solv}}/k_0\) need not be algebraic. Applying F.32 to that compositum would therefore be invalid. The following argument avoids it.

Choose a transcendence basis \(B\) of \(k_0/\mathbf Q\). It is finite because \(L/\mathbf Q\) has finite transcendence degree. Put \(F_0=\mathbf Q(B)\subset k_0\). Choose a finitely generated \(F\subset L\) containing \(K,B\) and generators of \(L/k\); then \(L=Fk\) is Galois prosolvable over \(F\). Let \(C\) be the relative algebraic closure of \(F_0\) in \(F\). It is finite over \(F_0\), hence finitely generated over \(\mathbf Q\), and \(F/C\) is regular.

For \(a\in k_0\), let \(N/C\) be the normal closure of \(C(a)/C\) inside the algebraic closure of \(F_0\) in a common overfield. Since \(a\) is algebraic over \(F_0\), this is finite. One has \(N\cap F=C\), because every element of the intersection is algebraic over \(F_0\) and hence belongs to the chosen relative algebraic closure \(C\). The conjugates of \(a\) over \(C\) are therefore also its conjugates over \(F\). Normality of \(L/F\) puts \(N\) inside \(L\). Now
\[
 \operatorname{Gal}(N/C)
       \simeq\operatorname{Gal}(FN/F)
\]
is a finite quotient of the prosolvable group \(\operatorname{Gal}(L/F)\). It is solvable. Therefore every \(a\in k_0\) lies in \(C^{\mathrm{solv}}\), so
\[
                k_0\subset C^{\mathrm{solv}}.
\]
This latter extension is algebraic, because both fields are algebraic over \(F_0\subset k_0\). The core theorem, already proved for the finitely generated base \(C/\mathbf Q\), gives reconstruction over \(C^{\mathrm{solv}}\). Algebraic-extension descent F.32 now gives reconstruction over \(k_0\). This proves the proposed arbitrary-subfield theorem without any transcendental-base-change assertion for pinned maps.

## 7. An arithmetic description of the enlarged sufficient class

The class in the proposed theorem is equivalently described as follows:

> There is a finitely generated subfield \(F_0\subset k_0\) such that \(k_0/F_0\) is algebraic and the Galois group of its normal closure is virtually prosolvable, meaning that it has an open prosolvable subgroup.

This is a sufficient arithmetic condition, not the claimed necessary-and-sufficient classification in F.9.

In one direction, let \(N/F_0\) be the normal closure and \(H\subset\operatorname{Gal}(N/F_0)\) an open prosolvable subgroup. Its fixed field \(C=N^H\) is finite over \(F_0\), and \(N/C\) is Galois prosolvable. Hence \(k_0\subset N\subset C^{\mathrm{solv}}\), and the core theorem plus F.32 applies. This also places \(k_0\) in the proposed embedding class.

Conversely Section 6 places any field in the proposed embedding class inside \(C^{\mathrm{solv}}\), where \(C/F_0\) is finite and \(F_0\subset k_0\) is finitely generated. Let \(C'/F_0\) be the finite normal closure of \(C\). There are only finitely many \(F_0\)-conjugates of \(C^{\mathrm{solv}}\), because it is normal over \(C\). Their compositum \(E/F_0\) is Galois and contains \(C'\). After adjoining \(C'\), each conjugate gives a Galois prosolvable extension of \(C'\), and their finite compositum is prosolvable: its group embeds as a closed subgroup of the product of their prosolvable groups. Thus \(\operatorname{Gal}(E/F_0)\) has an open prosolvable subgroup. The normal closure of \(k_0/F_0\) is a subextension of \(E/F_0\), so its group is a quotient of this virtually prosolvable group, and is itself virtually prosolvable. This proves the equivalence of the two descriptions of the sufficient class.

## 8. Strict enlargement of F.37

Take \(K=\mathbf Q(t)\) and \(k=K^{\mathrm{solv}}\). Its multiplicative group is divisible by 1.3, and \(t\) is transcendental over \(\mathbf Q\). If this field embedded in a finitely generated extension \(F/\mathbf Q^{\mathrm{solv}}\), the image of every element of \(k^\times\), including \(t\), would belong to \(D(F^\times)\). But the already proved F.33 gives \(D(F^\times)=(\mathbf Q^{\mathrm{solv}})^\times\), whose elements are algebraic over \(\mathbf Q\). A characteristic-zero field embedding fixes \(\mathbf Q\) and preserves transcendence, a contradiction. Thus this positive example is genuinely outside the old sufficient embedding class.

It does not contradict F.40–F.42: the solvable closure here is not being replaced by a henselian algebraic-power-series field, and no claim is made that arbitrary infinite algebraic extensions preserve reconstruction. The intrinsic converse problem of F.9 remains.

## 9. Audit against every arithmetic use in F.33–F.37

| Earlier use | Replacement verified here | Precise limitation |
|---|---|---|
| F.33: divisible scalar field; \(D(E^\times)\) for finite extensions | Section 1.3 and (G2) | Radical descent uses \(k/K\) normal and roots of unity, with a fixed finitely generated \(F=MS\); it does not need \(K\) a number field. |
| F.33: \(D(L^\times)\) for finitely generated extensions | Normal projective model and (G3) | Every root has zero divisor and lies in the finite relative algebraic subfield. |
| F.33: missing finite Galois number field | Constants equality (G1), unbounded alternating residual degrees, Section 1.2 | A missing number field is explicitly supplied; a missing geometric extension alone would not separate arithmetic Gauss places. |
| F.33/F.34: finite data descend with prosolvable normal scalar extension | Section 1.4, always keeping \(K\subset F\) | Normality over \(\mathbf Q\) is not asserted. |
| F.34: full arithmetic quotient detection | Section 2 | Finitely generated \(F/\mathbf Q\) remains Hilbertian; the geometric balanced-wreath proof and Bertini component preservation are unchanged. |
| F.35: distinct conjugate valuation pairs | Section 3 | The finite model \(M\) is Galois over \(\mathbf Q(t_1,\ldots,t_d)\), and the chosen automorphism moves its number-field constants. |
| F.35: commuting radical descent and fixed norm field | Section 3 | \(\tau\) preserves \(k\) because it fixes \(K\subset M\), without needing \(k/\mathbf Q\) normal. The field \(MS_0\) is finite over \(M\) and fixed for every \(n\). |
| F.36: normal coinvariants, finite spanning points, Tate-Hom | Section 4 | \(G_L\triangleleft G_F\), the finite point/value field is finitely generated over Q, and Jannsen 4.3(ii) applies there. No Kummer-faithfulness assumption is inserted. |
| F.36: Picard-Tate removal, integrality, residual constants | Sections 4–5 | Only the given point-theoretic class has its Picard component removed; residual scalars may be transcendental over Q but lie in fixed k. |
| F.37: exact CHW hypothesis | Section 5 | Uses Theorem 4.18(5), including finite-extension stability and actual point functions; it is not a generic-functor-only claim. |
| F.37: arbitrary subfield descent | Section 6 | Replaces the invalid possibly transcendental compositum with a genuinely algebraic extension \(C^{\mathrm{solv}}/k_0\). |

## 10. Primary sources and verification scope

All substantive geometric, Hilbert, Albanese and Tate-Hom sources are the already opened originals listed with F.24 and F.29–F.37. No theorem is being extended outside its published base-field hypotheses: Jannsen is applied over a finitely generated characteristic-zero field; Hilbert specialization is over such a field; smooth Bertini and the integral Albanese comparison use characteristic-zero geometry; CHW 4.18 has precisely the hypothesis checked in Section 5.

Newly reopened exact elementary field sources:

- Milne, J. S. (2022). *Fields and Galois theory* (Version 5.10, September). Proposition 7.15 and Corollary 7.16, printed p. 99. https://www.jmilne.org/math/CourseNotes/FT.pdf . These give the full Galois-compositum statement, including infinite normal extensions and compatible field embeddings.
- The Stacks Project Authors. (2026). *Transcendence*, Lemma 9.26.11, tag 030D. https://stacks.math.columbia.edu/tag/030D . This gives finiteness of every relative algebraic closure used in Sections 1 and6.

The candidate is a general proof; it contains no numerical assertion requiring a finite computation. The reviewed theorem is now integrated, with its result row in `audit/F_results.json`. The claimed enlargement is supported by the strictness argument in Section 8, rather than by an unverified claim that some particular number-field solvable closure differs from \(\mathbf Q^{\mathrm{solv}}\) by infinite degree.
