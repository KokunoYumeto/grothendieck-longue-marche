# Independent mathematical checks: truncation, derived reconstruction, and cotensor

**Scope and status.** Research memorandum prepared after the diplomatic transcription was frozen. Nothing here changes a reading, repairs a formula in the transcription, or treats the manuscript's cancellations as established assertions. These are independent mathematical checks of explicitly stated interpretations. The proofs below carry no claim of novelty. Confidence is high for the elementary algebraic statements proved here; application at infinity is conditional on specifying an actual abelian localization. References support the general categorical results, rather than attributing the independent calculations to those sources.

## 1. The exact gap in the general derived-composition argument

Write \(\mathcal A=\mathcal M_{N_0}\), let \(\tau:\mathcal A\to\mathcal B\) be exact with right adjoint \(\varphi\), and let \(i:\mathcal C\to\mathcal A\) be exact. Put \(\sigma=\tau i\), and assume the adjunction unit gives a natural isomorphism \(i\simeq\varphi\sigma\). With enough injectives in \(\mathcal C\) and \(\mathcal B\), the missing condition is

\[
\sigma(I)\text{ is }\varphi\text{-acyclic for every injective }I\in\mathcal C.
\tag{1}
\]

Condition (1) is equivalent to the canonical comparison

\[
R(\varphi\sigma)\longrightarrow R\varphi\,R\sigma
\]

being an isomorphism on \(D^+(\mathcal C)\). Since \(\sigma\) and \(\varphi\sigma\simeq i\) are exact, this would imply \(R\varphi\,\sigma\simeq i\), including the claimed vanishing of all positive \(R^n\varphi(\sigma M)\). Exactness of \(\sigma\) alone does not imply (1). This is the precise issue with the general argument on scans 263 and 267, and consequently with arguments subsequently depending on it. See Grothendieck (1957, Theorem 2.4.1, p. 148) and The Stacks Project (2026, Tag 015M).

The adjoint directions matter. Exactness of \(\tau\) implies that its **right** adjoint \(\varphi\) preserves injectives; it does not imply that \(\tau\) preserves injectives. An additional exact left adjoint to \(\tau\) would imply the latter. Similarly, an exact right adjoint \(\kappa\) to \(i\) makes \(i\) preserve projectives, not injectives. An exact **left** adjoint to \(i\) supplies injective preservation (The Stacks Project, 2026, Tag 015Z).

If \(i\dashv\kappa\), \(i\) is fully faithful, and \(\kappa\) is exact, then \(\sigma\dashv\psi=\kappa\varphi\). The step

\[
R\psi\simeq\kappa R\varphi
\]

is legitimate because the outer functor \(\kappa\) is exact. The fully faithful derived reconstruction instead requires that the **derived unit** \(\mathrm{id}\to R\psi\,\sigma\) be an isomorphism. Its degree-zero unit is insufficient. Vanishing of every \(R^n\varphi(\sigma M)\) is sufficient; vanishing of \(R^n\psi(\sigma M)=\kappa R^n\varphi(\sigma M)\) is the weaker relevant condition. Derived adjunction itself is standard once the indicated derived functors exist (The Stacks Project, 2026, Section 13.30).

## 2. A counterexample satisfying all the later formal hypotheses

**Statement checked:** exact localization, an exact fully faithful coefficient embedding, its exact right adjoint, and the ordinary unit isomorphism do not imply the asserted higher vanishing or derived full faithfulness.

Let \(k\) be a field and \(B=k[\epsilon]/(\epsilon^2)\). Let \(\mathcal A\) be the category of triples

\[
(V,W,f),\qquad V\in\operatorname{Vect}_k,\quad W\in\operatorname{Mod}(B),
\quad f:V\to W\text{ linear with }\epsilon f=0.
\]

Morphisms are commuting pairs of maps. This is a module category for the triangular algebra

\[
A=\begin{pmatrix}k&0\\k&B\end{pmatrix},
\]

where the left \(B\)-action on the off-diagonal \(k\) factors through \(B/(\epsilon)\). Exactness is componentwise.

Define

\[
\tau(V,W,f)=W,
\qquad
\varphi(W)=(\operatorname{Hom}_B(k,W),W,\mathrm{ev}).
\]

Here evaluation identifies \(\operatorname{Hom}_B(k,W)\) with \(\ker(\epsilon:W\to W)\). Directly, a morphism \((V,W,f)\to\varphi(W')\) is uniquely determined by its \(B\)-linear component \(W\to W'\), proving \(\tau\dashv\varphi\). The counit \(\tau\varphi=\mathrm{id}\) proves that \(\varphi\) is fully faithful. Thus \(\tau\) is an exact localization; its kernel consists of the triples \((V,0,0)\). Indeed the kernel and cokernel of the unit \((V,W,f)\to\varphi W\) both belong to this kernel. Even \(\tau\) has an exact left adjoint, namely \(W\mapsto(0,W,0)\).

Now put

\[
i(V)=(V,V,\mathrm{id}),\qquad \epsilon V=0,
\qquad \kappa(V,W,f)=V.
\]

The functor \(i\) is exact and fully faithful. A map \(i(V)\to(V',W',f')\) is determined uniquely by its first component \(V\to V'\), so \(i\dashv\kappa\), and \(\kappa\) is exact. Also \(\varphi\tau i=i\) through the ordinary unit.

Nevertheless, componentwise evaluation of an injective resolution gives, for \(n>0\),

\[
R^n\varphi(W)=(\operatorname{Ext}^n_B(k,W),0,0).
\]

The exact free resolution

\[
\cdots\xrightarrow{\epsilon}B\xrightarrow{\epsilon}B
\xrightarrow{\epsilon}B\longrightarrow k\longrightarrow0
\]

becomes a complex with zero differentials after applying \(\operatorname{Hom}_B(-,k)\). Hence \(\operatorname{Ext}^n_B(k,k)=k\) for every \(n\geq0\), and

\[
R^n\varphi(\tau i(k))=(k,0,0)\neq0\quad(n>0).
\]

Moreover \(\sigma=\tau i\) is the inclusion of vector spaces as \(B\)-modules annihilated by \(\epsilon\). It cannot be fully faithful on derived categories: \(\operatorname{Ext}^1_k(k,k)=0\), whereas \(\operatorname{Ext}^1_B(k,k)=k\). This example concerns the abstract inference, not the special divided-power ring below.

## 3. The binomial rigidity statement and the stronger ordinary unit

### 3.1 Precise setting

Let \(k\) be any commutative ring, and let

\[
S=\Gamma_k(T)=\bigoplus_{n\geq0}kT^{(n)},\qquad
T^{(a)}T^{(b)}=\binom{a+b}{a}T^{(a+b)}.
\]

Let \(\mathcal M_0\) be **all nonnegatively graded** \(S\)-modules and \(\mathcal M_N\) all modules supported in degrees at least \(N\), where \(N\geq0\). Truncation \(\tau_{N,0}\) deletes the components below \(N\); its right adjoint is \(\varphi_{0,N}\). These statements concern ordinary modules and ordinary graded tensor products, without a completion or a finiteness restriction.

The elementary arithmetic fact used throughout is

\[
\binom{p^r-1}{a}\equiv(-1)^a\pmod p\quad(0\leq a<p^r).
\tag{2}
\]

For completeness, in \(\mathbf F_p[X]\), \((1+X)^{p^r}=1+X^{p^r}\); division by \(1+X\) yields (2). Thus these coefficients are units after tensoring with \(\mathbf Z_{(p)}\). Localizations at all integer primes detect zero in any abelian group.

### 3.2 Constant families: ordinary full faithfulness

Suppose \(x_n\) belong to an arbitrary abelian group and satisfy

\[
\binom{j}{n}(x_j-x_n)=0\qquad(j>n\geq N).
\]

For two fixed indices \(m,n\) and any prime \(p\), choose \(q=p^r-1\geq m,n\). Both \(\binom qm\) and \(\binom qn\) are units after localization at \(p\). Hence \(x_m=x_q=x_n\) there. As this holds at every prime, the original family is constant.

A degree-zero map between \(\tau_N(M\otimes S)\) and \(\tau_N(M'\otimes S)\) is a family in the abelian group \(\operatorname{Hom}_k(M,M')\) with exactly these compatibilities. Therefore

\[
\operatorname{Hom}_{\mathcal M_N}
(\tau_N(M\otimes S),\tau_N(M'\otimes S))
\simeq\operatorname{Hom}_k(M,M').
\]

This proves the ordinary full-faithfulness component of **Hua, findings register, 136-shadow-full-faithfulness**, under the displayed hypotheses.

### 3.3 Weighted families: the full nonnegative unit

Full faithfulness checks only degree zero. To prove the stronger unit, fix \(\alpha\geq0\) and a lower bound \(L\geq0\). A homogeneous map of degree \(\alpha\) from \(S_{\geq L}\) to \(P\otimes S\) corresponds to elements \(h_n\in P\), \(n\geq L\), satisfying

\[
\binom jn h_j=\binom{j+\alpha}{n+\alpha}h_n
\qquad(j\geq n\geq L).
\tag{3}
\]

Set \(a_n=\binom{n+\alpha}{\alpha}\). We prove that there is a unique \(x\in P\) with \(h_n=a_nx\) for all \(n\geq L\).

Fix a prime \(p\) and finitely many relevant indices. Choose \(j=p^r-1-\alpha\) at least as large as all of them. Both \(a_j\) and \(\binom{j+\alpha}{n+\alpha}\) are units in \(\mathbf Z_{(p)}\). The identity

\[
\binom jn a_j=\binom{j+\alpha}{n+\alpha}a_n
\]

together with (3) gives \(h_n=a_n a_j^{-1}h_j\) after localization at \(p\). Consequently \(a_mh_n=a_nh_m\) after every such localization and hence over \(k\) itself.

The integers \(a_n\), \(n\geq L\), have gcd one: for each prime \(p\), an index \(n=p^r-1-\alpha\geq L\) gives a coefficient prime to \(p\). A finite subset consequently admits a Bézout relation \(\sum c_na_n=1\). Define \(x=\sum c_nh_n\). The preceding cross-relations imply \(a_mx=h_m\), and the same Bézout identity proves uniqueness.

For the adjunction unit, the degree-\(\alpha\) component below \(N\) is precisely restriction

\[
\operatorname{Hom}^{\alpha}_S(S,P\otimes S)
\longrightarrow
\operatorname{Hom}^{\alpha}_S(S_{\geq N-\alpha},P\otimes S).
\]

The weighted argument proves it is an isomorphism for \(0\leq\alpha<N\). In degrees \(\alpha\geq N\), the unit is already an isomorphism by the truncation adjunction. Therefore

\[
P\otimes S\xrightarrow{\sim}\varphi_{0,N}\tau_{N,0}(P\otimes S)
\quad\text{in }\mathcal M_0.
\tag{4}
\]

**Register assessment.** The stronger claim in Hua's register is correct in this interpretation, but it needs the weighted argument, not merely the constant-family lemma. Scan 252 lists equivalences; scan 265 uses the ordinary unit conditionally; scan 279 contains a related coefficient compatibility in the negative-degree dual discussion. None of this licenses treating a full proof as literally present on those pages. Also (4) is deliberately a statement in \(\mathcal M_0\): extension of the right adjoint to all \(\mathbf Z\)-graded modules introduces negative components, for which the argument has made no assertion.

This restriction is substantive. For a field of characteristic zero, identify \(\Gamma_k(T)\) with \(k[T]\). The right adjoint to truncation from **all** \(\mathbf Z\)-graded modules to degrees at least one sends \(S_{\geq1}\) to \(k[T,T^{-1}]\). Its unit from \(S\) is not an isomorphism in negative degrees. Truncating that right adjoint back to \(\mathcal M_0\) recovers precisely the nonnegative statement above.

## 4. An exact-left-adjoint repair specific to \(\Gamma_k(T)\)

Define \(i:\operatorname{Mod}(k)\to\mathcal M_0\) by \(i(M)=M\otimes S\). It has an exact **left** adjoint as well as its familiar exact right adjoint \(P\mapsto P_0\). Here is a direct construction and proof, independent of the manuscript's general inference.

For \(P\in\mathcal M_0\), define

\[
\mathscr L(P)=
\left(\bigoplus_{n\geq0}P_n\right)
\Big/
\left\langle
[T^{(m)}x]_{n+m}-\binom{n+m}{n}[x]_n
\ :\ x\in P_n,\ m,n\geq0
\right\rangle.
\tag{5}
\]

The relations are precisely the conditions for a graded \(S\)-linear map \(P\to M\otimes S\). Thus \(\mathscr L\dashv i\).

To check exactness, localize at an integer prime \(p\), and write \(n_r=p^r-1\). Then

\[
\mathscr L(P)_{(p)}\simeq
\varinjlim_r (P_{n_r})_{(p)},
\tag{6}
\]

where the transition from \(n_r\) to \(n_s\), \(s\geq r\), is

\[
\binom{n_s}{n_r}^{-1}T^{(n_s-n_r)}.
\tag{7}
\]

The coefficient in (7) is invertible by (2). The divided-power multiplication identity verifies composition of these transition maps. For any \(n\leq n_r\), relation (5) expresses \([x]_n\) as \(\binom{n_r}{n}^{-1}[T^{(n_r-n)}x]_{n_r}\). These expressions are compatible as \(r\) increases and respect all the relations in (5), proving (6), rather than merely suggesting a cofinality analogy.

Evaluation at each degree, localization, and filtered colimits of modules are exact. Thus (6) makes \(\mathscr L\) exact after every integer-prime localization, and therefore exact. It follows that \(i\) preserves injectives.

At finite \(N\), the exact inclusion \(j_N:\mathcal M_N\hookrightarrow\mathcal M_0\) is left adjoint to \(\tau_{N,0}\), as the frozen text on scans 244–246 explicitly states. Hence \(\tau_{N,0}\) also preserves injectives. Therefore \(\tau_{N,0}i\) carries injective \(k\)-modules to injectives of \(\mathcal M_N\), supplying condition (1). Together with (4), this proves the concrete finite-\(N\) vanishing and the bounded-below derived comparison.

There is also a clean derived full-faithfulness argument: \(\mathscr L j_N\dashv\tau_{N,0}i\), both functors are exact, and the right adjoint is fully faithful by Section 3. Their exact adjunction descends to derived categories and keeps its counit isomorphism. Consequently this particular finite-truncation embedding is fully faithful even on unbounded derived categories. This stronger conclusion uses the explicitly constructed exact adjoint; it does not validate the manuscript's unrestricted general argument.

## 5. Two genuinely different problems at infinity

### 5.1 Uniformly bounded modules: \(\mathrm{Neg}_\infty\)

Scan 256 defines an \(\infty\)-negligible module to have \(P_n=0\) for all sufficiently large \(n\). This class is Serre, since subobjects, quotients, and extensions preserve an upper degree bound. It is not closed under arbitrary coproducts: take one copy of \(k\), with positive-degree \(S\)-action zero, concentrated in each degree \(n\geq0\). Each summand is bounded above; their direct sum is not.

The Serre quotient by this class exists. Its quotient functor cannot have a right adjoint: a left adjoint to any right adjoint preserves coproducts, so its kernel must be closed under coproducts. More explicitly, if \(Q\dashv R\), then \(Q(\bigoplus X_a)\) represents the coproduct of the \(QX_a\) by the adjunction, whether or not coproducts of the quotient category had previously been constructed. Thus a section-functor treatment of this particular quotient requires a change of category or hypotheses. The warning on scan 254 about filtered colimits belongs to this problem; it should not be erased by silently passing to a different negligible class.

### 5.2 Elementwise negligible modules: \(\mathrm{Neg}\)

The second class in scan 256 consists of modules such that every element is killed by some sufficiently high-degree tail \(S_{\geq N}\). For \(S=\Gamma_k(T)\), this class need not be extension-closed, so in this generality it cannot be the kernel of an exact functor.

Take \(k=\mathbf F_p\) and \(I=S_{>0}\). Consider

\[
0\longrightarrow I/I^2\longrightarrow S/I^2\longrightarrow k\longrightarrow0.
\tag{8}
\]

The ideal \(I\) annihilates both ends, so both are elementwise negligible. But \(T^{(p^r)}\notin I^2\) for every \(r\): every product of positive degrees summing to \(p^r\) has coefficient \(\binom{p^r}{a}=0\) in \(\mathbf F_p\), \(0<a<p^r\). Hence the class of \(1\) in \(S/I^2\) is not killed by any high-degree tail. The middle term is not negligible. This proves the failure directly, without relying on a structure theorem for divided-power algebras.

If \(S\) is instead a polynomial ring in one positive-degree variable, as happens for \(\Gamma_k(T)\) when \(k\) is a \(\mathbf Q\)-algebra, the elementwise class is ordinary variable-torsion and is localizing. The characteristic-\(p\) example shows why that familiar situation cannot simply be imported into the integral divided-power setting.

### 5.3 A conditional, explicitly different repair

One can choose the **localizing Serre subcategory generated by the bounded-above modules**, call it \(\mathcal T\), and take the genuine Gabriel quotient \(Q:\mathcal M_0\to\mathcal M_0/\mathcal T\), with fully faithful right adjoint \(R\). This changes the definition and must be stated as such. In particular, (8) forces \(S/I^2\) into this closure, although it is not in the literal elementwise class.

For completeness, the divided-power repair behaves well in this specified quotient. An object \(i(I)\), with \(I\) injective over \(k\), is injective in \(\mathcal M_0\) by Section 4. It has no nonzero maps from bounded-above modules: in each source degree the coefficients \(\binom{n+m}{n}\), for arbitrarily large \(m\), have gcd one by (2), so an element of \(i(I)\) annihilated by a tail must be zero. The class of objects having no maps to this injective is a localizing Serre subcategory. It therefore contains \(\mathcal T\). Thus \(i(I)\) is a \(\mathcal T\)-local injective; \(Qi(I)\) is injective in the quotient and \(RQi(I)=i(I)\).

Applying this to an injective resolution of any \(k\)-module \(M\) gives no positive derived correction: more precisely \(\mathbf R R\,Q i(M)\simeq i(M)\). In particular the ordinary unit is also an isomorphism for every \(i(M)\).

This argument justifies a repaired infinity theorem for this **specified** localizing closure. It does not prove that the manuscript's \(\mathcal M_\infty\) was defined this way, nor identify the closure with its literal \(\mathrm{Neg}\). The usual abelian quotient construction and the necessity of the Serre condition are recalled in The Stacks Project (2026, Section 12.10); Gabriel (1962) is the foundational reference for localizations with section functors.

The proof was deliberately given in \(\mathcal M_0\). It does not assert that \(i(I)\) is injective in the entire category of \(\mathbf Z\)-graded modules. If one takes the localizing Serre closure of bounded-above modules in that entire category, the quotient reduces to the nonnegative version: the exact truncation \(P\mapsto P_{\geq0}\) has bounded-above cokernel in its inclusion into \(P\), so that inclusion becomes an isomorphism in the quotient. Truncation sends the generators of the full localizing closure to bounded-above objects of \(\mathcal M_0\), identifying the two corresponding quotients. This is a reduction for the explicitly chosen closure, not an assertion about an unspecified \(\mathcal M_\infty\).

## 6. Boundedness and multiplication

The general injective-resolution comparison in Section 1 is a \(D^+\) statement. A bounded-below complex of acyclic objects can be used to compute the right derived functor; an arbitrary unbounded complex with acyclic terms does not automatically have this property. The same caution applies to interpreting the hypercohomology spectral sequence on scan 271 as convergent for an unrestricted complex. General unbounded claims require suitable K-injective resolutions or another explicit argument.

There is also a distinct issue even for bounded complexes: **acyclicity of the cohomology objects** is not the same as **acyclicity of the individual terms**. The former can collapse a hypercohomology spectral sequence, but does not say that applying the underived functor termwise computes its derived value. For the functor \(\psi=\operatorname{Hom}_B(k,-)\) of Section 2, take the acyclic bounded complex

\[
0\longrightarrow k\xrightarrow{1\mapsto\epsilon}B
\longrightarrow k\longrightarrow0.
\]

All its cohomology objects are zero and therefore \(\psi\)-acyclic. But applying \(\psi\) gives, under the natural identifications,

\[
0\longrightarrow k\xrightarrow{\sim}k\xrightarrow{0}k\longrightarrow0,
\]

which has a nonzero last cohomology group, whereas its right-derived value is zero. Thus the cohomology-acyclicity condition explored in the cancelled material on scan 271 cannot alone justify replacing \(R\psi(L^\bullet)\) by \(\psi(L^\bullet)\).

For the finite-\(N\), one-generator divided-power setting, Section 4 provides such another argument through an exact adjunction, so no unbounded obstruction is asserted there. In the specifically repaired quotient of Section 5.3, \(\mathscr L\) kills \(\mathcal T\) and factors as an exact functor \(\overline{\mathscr L}\) on the quotient. The established locality of \(i(M)\) gives \(\overline{\mathscr L}\dashv Qi\); this too permits an exact-adjunction argument if an unbounded embedding is desired. None of this removes the need to specify the quotient in the first place.

Finally, additive or triangulated full faithfulness does not by itself prove the phrase “compatible avec multiplication” on scan 273. One must specify a monoidal structure on the localized category, its relation to the indicated tensor product, and coherent compatibility of the reconstruction with multiplication and the unit. Fixed positive truncation removes degree zero and does not automatically preserve the original monoidal unit. Derived tensor products require appropriate flat or K-flat replacements when coefficients are not flat. No claim about strict commutative differential graded algebras, divided-power operations, or completed multiplicative structures follows solely from the additive argument.

### Conditional interpretation of a complex with the Cartan weight pattern

This paragraph analyzes a hypothesis; it does not independently resummarize the primary Cartan theorem. For the actual theorem and its source verification, see the coordinating notes N54 and the separate literature memorandum.

Suppose a weighted complex \(G\) has, for each cohomological degree \(n\geq0\), weight cohomology \(H^n(G)_r=M_n\) for \(r\geq n\) and zero for \(r<n\), and suppose the action of \(T^{(s)}\) from weight \(r\) to weight \(r+s\) is multiplication by \(\binom{r+s}{r}\). Then

\[
H^n(G)\simeq\tau_{\geq n}(M_n\otimes\Gamma_{\mathbf Z}(T))
\]

as graded modules. If \(M_n=H^n(X;\mathbf Z)\), this is exactly the finite-tail coefficient pattern that motivates the truncation calculation. A genuine exact quotient killing bounded weight differences identifies this cohomology module with the image of \(H^n(X;\mathbf Z)\otimes\Gamma_{\mathbf Z}(T)\). This provides a precise conditional explanation of the reconstruction strategy, while retaining the distinction between the two negligible classes and their localizing closure.

An identification of cohomology modules alone is not a specified chain comparison, and does not determine coherent multiplication. With an appropriate comparison and the monoidal compatibilities just listed, one could transport multiplication to a ring object in \(D(\mathbf Z)\). Such a conclusion would not impose divided powers on its ordinary cohomology ring. For example, the cup-product ring of \(\mathbf{CP}^2\) has a primitive square \(x^2\), whereas strict divided powers on that class would require \(x^2=2\gamma_2(x)\). The existence of an ordinary ring object in the derived category does not assert this divisibility. Thus the proposed derived interpretation is compatible with that strict divided-power obstruction, and supplies neither a strict divided-power equivalence nor an \(E_\infty\) equivalence by itself. No historical identity between the unpublished construction and a published model is claimed here.

## 7. Cotensor: the counit proof and its actual limitations

**Ordinary-comodule interpretation.** Let \(s\) be a counital coassociative coalgebra over a commutative ring \(k\), and \(C\) a left \(s\)-comodule with coaction \(\lambda:C\to s\otimes C\). Give \(M\otimes s\) its cofree right-comodule structure. Then, for every \(k\)-module \(M\),

\[
(M\otimes s)\mathbin{\Box_s}C\simeq M\otimes C.
\tag{9}
\]

No flatness assumption on \(M\), \(C\), or \(s\) is required for this particular identity. A three-line proof is:

\[
f=1_M\otimes\lambda:M\otimes C\longrightarrow(M\otimes s)\Box_s C,
\qquad g=(1_M\otimes\epsilon\otimes1_C)|_{\Box_s};
\]

\[
gf=1\quad\text{by the counit identity};
\]

\[
(1_M\otimes\Delta\otimes1_C)z=(1_M\otimes1_s\otimes\lambda)z
\ \Longrightarrow\ z=fg(z)
\quad\text{after applying }1_M\otimes\epsilon\otimes1_s\otimes1_C.
\]

This equalizer is split by the counit. Tensor need not preserve an arbitrary equalizer without flatness—for example tensoring the injective map \(\mathbf Z\xrightarrow{2}\mathbf Z\) with \(\mathbf Z/2\) destroys its zero kernel—but that generic warning does not invalidate (9).

Consequently the “NON” on scan 281 must be preserved, but cannot be explained merely by claiming that (9) fails for nonflat \(M\). Before applying (9) to that page, one must establish that \(\boxtimes_s\) really denotes this module equalizer, that the first factor really has the cofree coaction, and that the maps live in the category being discussed. In particular:

- Ordinary grading alone does not invalidate the proof when all maps have the appropriate degree.
- A cotruncation deleting degree zero can remove the counit and the cofree structure; then the displayed proof no longer applies to the truncated object.
- Coalgebra structures, divided powers, representable functors, and additional algebraic structures require their own compatibility checks. An arbitrary module \(M\) does not furnish a coalgebra structure on \(M\otimes s\) merely by being a module.
- For completed or topological tensor products, continuity and the existence of the indicated maps and equalizer must be checked. If the counit splitting exists in that category, the same splitting argument can still work; completion alone is not a proof of failure.

The exact intended obstruction on scan 281 is not settled by this memorandum, and no reading of its ink is proposed.

## References and retrievable source anchors

Gabriel, P. (1962). Des catégories abéliennes. *Bulletin de la Société Mathématique de France, 90*, 323–448. https://doi.org/10.24033/bsmf.1583 . Official record: https://numdam.org/articles/10.24033/bsmf.1583/ . Used as a foundational localization reference, without asserting an unverified proposition number.

Grothendieck, A. (1957). Sur quelques points d'algèbre homologique. *Tohoku Mathematical Journal, Second Series, 9*(2), 119–183. https://doi.org/10.2748/tmj/1178244839 . Theorem 2.4.1 is on printed p. 148 and explicitly assumes that the inner functor sends injectives to objects acyclic for the outer functor. Official record: https://www.jstage.jst.go.jp/article/tmj1949/9/2/9_2_119/_article . Readable primary text: https://people.math.osu.edu/anderson.2804/teaching/grothendieck_tohoku.pdf . This citation is to the first published part containing the theorem, not the combined 119–221 pagination of both parts.

The Stacks Project Authors. (2026). *The Stacks Project*.

- Lemma 13.22.1, Tag 015M, composition criterion: https://stacks.math.columbia.edu/tag/015M .
- Lemma 13.22.2, Tag 015N, Grothendieck spectral sequence: https://stacks.math.columbia.edu/tag/015N .
- Lemma 12.29.1, Tag 015Z, injectives and exact left adjoints: https://stacks.math.columbia.edu/tag/015Z .
- Section 13.30, Tag 0FNC, deriving adjoints: https://stacks.math.columbia.edu/tag/0FNC .
- Section 12.10, Tag 02MN, Serre subcategories and abelian quotients: https://stacks.math.columbia.edu/tag/02MN .

