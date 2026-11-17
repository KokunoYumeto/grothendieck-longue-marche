# Independent algebra checks: cote 64, scans 102–115

**Research only; frozen text unchanged.** This work began after the parent run's freeze at 2026-11-17 23:01:38 UTC. I read *context/README.md* and all of *context/notes/RESULTS_STATE.md* before writing these findings; truncated portions of the latter were reread. I did not inspect scan images or edit any transcription, inventory, or doubts file. Mathematical conclusions below concern the frozen readings and explicitly stated interpretations, and do not choose uncertain ink.

**Checker:** GPT-6 Astra Pro; effort inherited, not exposed; run *MPL_64_078-115/research_algebra*. An initial broad context search accidentally returned two lines of Hua's algebra subsection along with its headings; the independent principal-part and scaling calculations had already been made. *context/hua_project/README.md* was then read before the subsection was deliberately consulted. The subsequent comparison credits Michel Hua's AI-produced project throughout. The parent run's separate connections research treats Hua's full dossier; this record covers only the algebra in the supplied scans.

**Register scope.** *RESULTS_STATE.md* explicitly says “Our results to use and check: none listed” for this packet. No settled register theorem is reproved or assigned a new status here. Except for the limited finite geometric comparison to **LM4 D.12** in ALG08, there is no applicable exact result-register entry for the calculations below. The summaries **MPL_93_002-046 P09/E14/E16/C29/C35** do not supply an elliptic principal-part or addition-law theorem and are not used as mathematical inputs.

**Notation used in the checks.** Write \(O=0_E\), \(F_n=H^0(E,\mathcal O_E(nO))\), \(K=k(E)\), and \(T=T_{E,O}\). Unless stated otherwise, \(k\) is the algebraically closed field of characteristic different from \(2\) specified on scan 102. Let \(D_\delta\) denote the invariant vector field whose value at \(O\) is \(\delta\). This is the natural interpretation of the manuscript's \(\Theta_\delta\); the dependence on this interpretation and on \(\varepsilon_n\) is made explicit. For the later coordinate calculations, \(x,y\) are abstract coordinates satisfying the *monic* equation \(y^2=f(x)=x^3+a_1x^2+a_2x+a_3\), with \(f\) squarefree; this does not silently settle the earlier normalization issue.

## Findings for incorporation into the research notes

### ALG01 — The right quotient arrow is degree dependent

**Source:** cote 64, scan 102 (6)–(7), scan 103 (8)–(11), especially the right arrows. **Kind:** unproved claim; refined statement ALG01-R below. **Quote:** “où \(\mu_\delta\) est la multiplication par \(\delta\)” and “\(\simeq\ \mathrm{can}\)”.

For the canonical principal-part maps \(\mathrm{pp}_n:F_n/F_{n-1}\simeq T^{\otimes n}\), the induced arrow is \(-n\mu_\delta\), so in characteristic \(p\) it is zero when \(p\mid n\). More generally, a multiplicative scaling \(\varepsilon_n=c^n\mathrm{pp}_n\) changes it to \(-nc\mu_\delta\), which still depends on \(n\). In fact, all-degree unit arrows are incompatible with the stated Leibniz rule and multiplicative quotient identifications: applying the rule to the square of a degree-two leading term forces \(2=1\). This is a mathematical incompatibility under explicit algebra conventions, not an instruction to repair the frozen diagram or its uncertain bottom exponent.

**Context comparison:** searches for *Weierstrass*, *Vandermonde*, *parties principales*, *principal parts*, and *dérivation invariante* in the supplied non-Hua context found no exact competing formula; the principal-part occurrence in *MPL_142_001-093_notes.md*, N016.2 (scan 016), concerns an Artin–Schreier obstruction, a different operator and quotient. **Hua, modernised reading of cote 64**, subsection “IV. Descriptions explicites … L'algèbre des fonctions à pôle à l'origine,” modern pages 100–108, explicitly selects the ordinary leading-coefficient convention and obtains \(-n\mu_\delta\); our check **agrees under that convention** and **adds** the multiplicative scaling analysis. **RESULTS_STATE:** no applicable exact entry. **Confidence in the refined calculation:** high, because it follows by differentiating a Laurent leading term and independently by Leibniz.

### ALG02 — The kernel in positive characteristic, and the graded/filtered distinction

**Source:** cote 64, scan 103, deduction after (11) and (12); compare scan 105 (20), (22)–(25). **Kind:** unproved claim. **Quote:** “\(\operatorname{Ker}\Theta_\delta=\mathcal F_1=k.1_E\)”.

For \(\delta\ne0\), the equality with constants holds on \(F_\infty\) and each \(F_n\) in characteristic zero, while in characteristic \(p>0\) over the given perfect field the exact answer is \(\ker(D_\delta|F_n)=\{g^p:g\in F_{\lfloor n/p\rfloor}\}\). Thus the first failure is at pole order \(2p\), witnessed by \(x^p\), and even an integer \(n\) prime to \(p\) need not give constant kernel once lower steps have crossed \(2p\). The equality also needs \(\delta\ne0\); and, on the **graded** algebra \(\bigoplus F_n\) rather than \(F_\infty\), the characteristic-zero kernel is \(k[S]\), containing a distinct constant section in every degree. These failures do not invalidate the nonzero image \(D_\delta F_2=F_3^-\) used later, since the leading coefficient \(-2\) is invertible under the stated characteristic restriction.

**Context comparison:** searches for *noyau.*dériv*, *ker.*theta*, *puissances.*p*, and *p.th powers* found no exact earlier result. *MPL_146_001-099_notes.md*, **R079**, scan 063, **differs**: it gives a Frobenius obstruction to divisibility of principal units in a tangential construction, not the present function-field kernel. **Hua, modernised reading of cote 64**, the same algebra subsection, correctly notices that \(p\)-th powers obstruct the unrestricted claim, but its intervening statement “Pour \(n\) inversible … \(\operatorname{Ker}\Theta_\delta\cap\mathcal F_n=k\)” is **contradicted** by \(n=2p+1\) and \(x^p\in F_{2p}\); the separate connections report records this comparison in full. **RESULTS_STATE:** no applicable exact entry. **External input:** The Stacks Project, Lemma 10.158.2, Tag [031W](https://stacks.math.columbia.edu/tag/031W), identifies the kernel of the universal differential over a perfect field with \(K^p\); the passage to this filtration is proved below. **Confidence:** high for the stated perfect-field theorem and explicit counterexamples.

### ALG03 — The monic equation is convention sensitive, not unconditionally a factor-four error

**Source:** cote 64, scan 105 (22)–(25); scan 106, equality of \(\varepsilon_6\)-values and (28); scan 115, opening normalization. **Kind:** reading question and own idea (explicit alternative convention). **Quote:** “\(\wp'=\Theta_\delta(\wp)\qquad\text{donc }\varepsilon_3(\wp')=\delta^{\otimes3}\)” and “\(\wp'^2=\wp^3+\cdots\)”.

If \(\varepsilon_n\) means ordinary principal part and \(D_\delta\) has value \(\delta\) at \(O\), then \(\varepsilon_2(\wp)=\delta^2\) gives \(\varepsilon_3(D_\delta\wp)=-2\delta^3\), and the leading cubic coefficient is \(4\). However, the multiplicative convention \(\varepsilon_n=(-1/2)^n\mathrm{pp}_n\) makes all three displayed normalizations \(\varepsilon_2(\wp)=\delta^2\), \(\varepsilon_3(D_\delta\wp)=\delta^3\), and the monic cubic hold simultaneously; its quotient arrow is \((n/2)\mu_\delta\), not the unit arrow in (9)/(11). Consequently the normalization is an unresolved convention unless the canonical meaning of \(\varepsilon_n\) is established, while ALG01's all-degree problem remains. The choice in (22) must be nonzero for the bases in (25), as the explicit word “base” on scan 115 later makes clear.

**Context comparison:** the same principal-part searches give no non-Hua convention specifying \(\varepsilon_n\) for this elliptic calculation. **Hua, modernised reading of cote 64**, algebra subsection, chooses ordinary principal parts and replaces the ordinate by \(y=-D_\delta\wp/2\); our canonical-convention calculation **agrees**, while the multiplicative rescaling **adds an alternative** that keeps the manuscript's equality \(\wp'=D_\delta\wp\). Neither alternative is promoted to an intended authorial convention. **RESULTS_STATE:** no applicable exact entry. **Own-idea confidence:** high for the algebraic equivalence; undetermined for the author's intention, because (6) supplies an exact sequence but no explicit Laurent formula for \(\varepsilon_n\).

### ALG04 — The derivative and polynomial readings can be tested without resolving the ink

**Source:** cote 64, scan 108 (31)–(33). **Kind:** reading question. **Frozen quote:** `\wp^{\unsure{'|''}}=\tfrac12(3\wp^2+2a_1\wp+a_2)`; the source records the prime as an alternative, not an editorially supplied second derivative.

For the displayed monic equation and \(D x=y\), differentiating its relation gives \(D y=D^2x=f'(x)/2\), exactly the operator formula (32). The single-prime interpretation of (33) fails at every finite branch point: there \(y=0\) but \(f'(x)/2\ne0\); the double-prime interpretation agrees. Likewise, keeping \(a_2P^2\) in (31) while keeping (32) produces the nonzero residual derivative \(a_2(1-2P)P'\) in general, whereas \(a_2P\) gives zero. These are conditional algebraic tests of the frozen alternatives, not a second paleographic pass or an alteration of the transcription.

**Context comparison:** searches for *Weierstrass*, *dérivation*, and *loi d'addition* found no exact earlier source; **Hua, modernised reading of cote 64**, algebra subsection, **differs in editorial presentation** by writing a normalized \(Y\)-coordinate and an unambiguous second derivative. Our check **adds** a branch-point counterexample and a polynomial residual that isolate the two uncertainties without resolving them. **RESULTS_STATE:** no applicable exact entry. **Confidence:** high; both identities are symbolically certified in *verify_algebra.py*.

### ALG05 — What the inverse construction actually needs

**Source:** cote 64, scan 109 (34)–(37), and scan 114 sentence following (57). **Kind:** unproved claim. **Quote:** “on vérifie que les formules précédentes définissent une courbe elliptique”; the Proj subscript is frozen as the alternative \(*|\infty\).

A squarefree monic cubic over a field of characteristic different from \(2\) gives the smooth projective plane cubic \(Y^2Z=X^3+a_1X^2Z+a_2XZ^2+a_3Z^3\), with rational origin \([0:1:0]\) and genus one. The filtered affine algebra \(F_\infty=k[x,y]/(y^2-f(x))\) needs its pole filtration to reconstruct \(E\); its graded section ring is the weighted ring displayed in the proof below, and taking Proj of an ungraded affine algebra has not specified that construction. The degree-two map has four branch values, the three roots and infinity; scan 109 lists the finite ones, and scan 114 explicitly includes infinity. This supplies the omitted verification and distinguishes an abbreviated construction from a proposed change to the uncertain subscript.

**Context comparison:** searches for *quadratique*, *ramifi*, and *courbe elliptique* found only broader covering/moduli discussions among the supplied LM files, with no identical section-ring reconstruction. **Hua, modernised reading of cote 64**, end of the algebra subsection, **agrees** on the elliptic curve and all four branch points; our record **adds** the homogeneous ring and the local smoothness/ramification checks. **RESULTS_STATE:** no applicable exact entry. **External input:** the plane-curve genus formula in The Stacks Project, Section 53.9, especially Lemma 53.9.3, Tag [0BYA](https://stacks.math.columbia.edu/tag/0BYA); the cubic's smoothness and branch indices are checked directly below. **Confidence:** high for this explicit construction.

### ALG06 — The distinctness problem is already corrected in the manuscript

**Source:** cote 64, scans 110–111, Proposition 3, (41)–(45), insertion “tous distincts” and left NB. **Kind:** self-flagged; withdrawn in the same text. **Quote:** “Si deux parmi les \(x,y,z\) sont égaux, (42) est tjrs vérifié”.

The active proposition for three distinct points different from \(O\) is correct: a vanishing determinant gives a nonvertical line whose section has zero divisor exactly \(x+y+z\), hence sum \(O\). If repeated points were allowed, the determinant would forget the required contact multiplicity; on \(y^2=x^3-x\), the triple \((0,0),(1,0),(0,0)\) has determinant zero and sum \((1,0)\ne O\). The insertion, marginal NB, and converse proof on scan 111 already repair this, so the withdrawn version should not be counted as an unresolved error. A repeated-point statement instead uses tangent/contact multiplicities, as in ALG07.

**Context comparison:** the *corde*, *loi d'addition*, and *points.*distincts* searches located no exact earlier determinant proposition outside Hua. **Hua, modernised reading of cote 64**, “La loi d'addition (pages 109 à 112),” **restates** the corrected distinct-point proposition; the present frozen text preserves the correction and self-criticism more explicitly. **RESULTS_STATE:** no applicable exact entry. **Primary comparison:** Andrew V. Sutherland, *18.783 Elliptic Curves*, Spring 2021, Lecture 2, §§2.1–2.2, [lecture notes](https://math.mit.edu/classes/18.783/2021/LectureNotes2.pdf); our proof follows the manuscript's divisor argument, not an appeal to a picture. **Confidence:** high.

### ALG07 — The true secant domain and the tangent extension

**Source:** cote 64, scans 112–113 (47)–(51), especially the NB after (47), (50), and final paragraph. **Kind:** unpursued implication; own idea (precise hypothesis package and tangent continuation). **Quote:** “Par principe de prolongement” and “dès que \(x_0\ne y_0\)”.

Formula (51) computes \(z=-(x+y)\), including the displayed sign of its ordinate, on the entire domain \(x_0\ne y_0\); the additional exclusions \(y\ne-2x\) and \(x\ne-2y\) are needed only in the initial argument selecting a distinct third root. Condition (50) by itself omits \(y\ne-x\), but the earlier NB explicitly retains \(x_0\ne y_0\); for example \((3,5)\) and \((3,-5)\) on \(y^2=x^3-2\) satisfy (50) alone while the denominator vanishes. For doubling at \(P=(u,v)\) with \(v\ne0\), the same formulas use \(\lambda=f'(u)/(2v)\), \(\mu=v-\lambda u\), and \(z_0=\lambda^2-a_1-2u\); if \(v=0\), then \(2P=O\). These refinements are exact in characteristic \(3\) as well: the computations divide by \(2v\) or \(x_0-y_0\), never by \(3\).

**Context comparison:** the searches above give no exact pre-existing addition-law statement in the LM files. **Hua, modernised reading of cote 64**, “La loi d'addition,” **restates** the final secant domain and the removal of the initial exclusions; this record **adds** the explicit (50)-alone counterexample and the tangent factorization. **RESULTS_STATE:** no applicable exact entry. **Primary comparison:** Ben Lynn, “Explicit Addition Formulae,” [Stanford-hosted author notes](https://crypto.stanford.edu/pbc/notes/elliptic/explicit.html), presents the general Weierstrass secant/tangent formulas; his conventional coefficient indices differ from those in this manuscript. **Confidence:** high, because the factorizations are checked as rational identities before specializing.

### ALG08 — Completion and verification of the final Möbius involution

**Source:** cote 64, scan 115, paragraph after (60), ending with the formula for \(b\). **Kind:** unproved claim; own idea (explicit matrix certificate). **Quote:** “Déterminons l'autom involutif” and “s'identifie à l'autom déduit par passage au quotient”.

For distinct roots \(\xi_i,\xi_j,\xi_h\), put \(A_i=(\xi_i-\xi_j)(\xi_i-\xi_h)\); the written final coefficient gives \(\sigma_i(z)=\xi_i+A_i/(z-\xi_i)\). Its representing matrix has square \(A_iI\) and determinant \(-A_i\ne0\), proving that it is a nonidentity involution exchanging exactly the stated pairs; translation by the nonzero two-torsion point descends because it commutes with negation, and its action on the branch points identifies the same map. The three maps satisfy \(\sigma_i\sigma_j=\sigma_h\), giving the finite geometric Klein four action in explicit coordinates. This provides a local geometric example relevant to the orientation of **LM4 D.12**, but does not classify torsion in the full profinite groups or change that open register row.

**Context comparison:** searches for *Möbius*, *involuti*, *Klein*, and *quatre points* locate *MPL_142_094-122_notes.md*, **B01**, scan 108 (the Klein-four model \(z,-z,1/z,-1/z\)), and *MPL_147_003-047_notes.md*, **Appendix B**, the four-point set \(\{0,\infty,1,3\}\); the present formula **adds** the elliptic translation interpretation and arbitrary branch roots, rather than identifying these distinct moduli constructions. **Hua, modernised reading of cote 64**, “Les involutions \(\sigma_i\) et les points d'ordre \(4\) (pages 113 à 117),” **agrees** with the formula and supplies the factorized fixed-point equation beyond this packet's endpoint; that factorization is Hua's project's explicitly credited reformulation, not new manuscript text on scan 115. **RESULTS_STATE:** **LM4 D.12** remains open; no settled row is reused. **Confidence:** high for the matrix and descent checks; no claim about the full profinite comparison.

## Proofs and reproducible calculations

### ALG01-R: local symbol and the multiplicativity obstruction

Choose a local parameter \(u\) at \(O\), and put \(e=(du)_O^\vee\). If \(\delta=d\,e\) and \(f=a u^{-n}+O(u^{-n+1})\), the invariant vector field is \((d+O(u))\partial_u\), so

\[
D_\delta f=-na d\,u^{-n-1}+O(u^{-n}),\qquad
\mathrm{pp}_{n+1}(D_\delta f)=-n\,\delta\otimes\mathrm{pp}_n(f).
\]

The quotient identification is independent of the choice of \(u\): if \(v=b u+O(u^2)\), the leading coefficient becomes \(ab^n\), while \((dv)_O^\vee=b^{-1}e\). Its tensor with that vector to the \(n\)-th power is unchanged. Multiplying Laurent series also proves the multiplicativity of these canonical identifications.

For any scalar identifications \(\varepsilon_n=c_n\mathrm{pp}_n\), the quotient arrow is \(-n(c_{n+1}/c_n)\mu_\delta\). If the identifications are multiplicative for all nonzero graded pieces, \(c_{m+n}=c_mc_n\) for \(m,n\in\{2,3,4,\ldots\}\). In particular \(c_2^3=c_3^2\); setting \(c=c_3/c_2\) gives \(c_2=c^2,c_3=c^3\), and the remaining scalars are \(c_n=c^n\). The arrow is therefore \(-nc\mu_\delta\).

An independent contradiction avoids choosing \(c\). Suppose the quotient arrows are all multiplication by a fixed nonzero \(\delta\), and the quotient identifications preserve products. Choose \(f\in F_2\) with nonzero symbol \(a\). Applying the degree-four unit arrow to \(f^2\) gives \(\delta a^2\), while applying Leibniz and the degree-two unit arrow gives \(2a(\delta a)=2\delta a^2\). The two are unequal over every field because \(\delta a^2\ne0\). This refutes the *simultaneous* unit-arrow/multiplicativity/derivation package, not arbitrary unrelated identifications of one-dimensional quotients.

### ALG02-R: exact kernel and first failure

For a smooth geometrically integral curve, \(\Omega_{K/k}\) is one-dimensional over \(K\). A nonzero derivation \(D_\delta:K\to K\) is a nonzero \(K\)-linear functional on this space, hence \(D_\delta f=0\) exactly when \(df=0\). For perfect \(k\) of characteristic \(p>0\), Tag 031W gives \(df=0\iff f\in K^p\). If \(f=g^p\in F_n\), then \(p\operatorname{ord}_Q(g)=\operatorname{ord}_Q(f)\ge0\) for every \(Q\ne O\), and \(p\operatorname{ord}_O(g)\ge-n\); hence \(g\in F_{\lfloor n/p\rfloor}\). The converse follows by taking powers. This proves the asserted formula and the dimension

\[
\dim_k\ker(D_\delta|F_n)=\max\{1,\lfloor n/p\rfloor\}.
\]

The dimension statement uses the manuscript's Riemann–Roch dimensions on scan 102 and perfection of \(k\), which makes the Frobenius image a \(k\)-subspace with the same dimension. In characteristic zero a nonconstant \(f\in K\) defines a separable map to the projective line, so \(df\ne0\); the constant field of this geometrically integral proper elliptic curve is \(k\). If \(\delta=0\), the invariant derivation is zero and its kernel is the full space instead.

For the graded interpretation set \(R=\bigoplus_{n\ge0}F_nT^n\subset F_\infty[T]\), and \(S=T=1\cdot T\in R_1\). The degree-one derivation is \(D_R(fT^n)=D_\delta(f)T^{n+1}\). Its characteristic-zero kernel is \(k[S]\), not a single copy of \(k\); in positive characteristic it is \(R^p[S]\). Indeed each homogeneous kernel element \(g^pT^n\), with \(g\in F_{\lfloor n/p\rfloor}\), is the \(p\)-th power of \(gT^{\lfloor n/p\rfloor}\) times \(S^{n-p\lfloor n/p\rfloor}\). This distinction is required only if (12) is read as a statement about the graded algebra introduced on scans 102–104.

**Actual computation:** on the smooth curves \(y^2=x^3-x\) over \(\mathbf F_p\), for \(p=3,5,7,11\), the script constructs the exact matrix of \(Dx=y,\ Dy=(3x^2-1)/2\) on every pole space through \(F_{3p+2}\). Its basis is \(\{x^i:2i\le n\}\cup\{x^jy:2j+3\le n\}\). Modular row reduction returns the formula above in every case; in particular the dimensions at \(2p-1,2p,2p+1\) are \(1,2,2\). These finite checks supplement the proof; they do not establish its universal quantifier by sampling.

### ALG03-R: a complete conditional normalization calculation

Assume multiplicative \(\varepsilon_n=c^n\mathrm{pp}_n\), take \(\delta\ne0\), and choose \(u\) dual to \(\delta\). The condition \(\varepsilon_2(x)=\delta^2\) is

\[
x=c^{-2}u^{-2}+O(u^{-1}),\qquad
D_\delta x=-2c^{-2}u^{-3}+O(u^{-2}).
\]

It follows that

\[
\varepsilon_3(D_\delta x)=-2c\,\delta^3,
\qquad
\frac{\text{leading coefficient of }(D_\delta x)^2}
{\text{leading coefficient of }x^3}=4c^2.
\]

Thus \(\varepsilon_3(D_\delta x)=\delta^3\) forces \(c=-1/2\), which also makes the cubic monic and \(\varepsilon_6(x^3)=\varepsilon_6((D_\delta x)^2)=\delta^6\). The ordinary principal-part convention \(c=1\) instead gives the coefficient \(4\). In characteristic \(3\), \(-1/2=1\) and \(4=1\), so these particular two conventions coincide; this does **not** cure the all-degree arrow or kernel problem. Any attempt to remove the degree factor by unrelated \(c_n\)'s abandons the multiplicativity just used in the leading-term comparisons, and in characteristic \(p\) cannot turn the zero arrow at \(n=p\) into an isomorphism.

There are consequently two transparent consistent coordinate choices: (i) ordinary principal parts, \(x\) normalized to \(\delta^2\), and ordinate \(y=-D_\delta x/2\), as in Hua's modernisation; or (ii) scaled principal parts \((-1/2)^n\mathrm{pp}_n\), \(x\) normalized accordingly, and ordinate \(y=D_\delta x\), as the manuscript writes. Neither makes (11)'s all-degree right arrow the canonical unit map. A third formal possibility rescales the map \(\delta\mapsto\Theta_\delta\) itself; if its value at \(O\) is \(q\delta\), the same computation uses \(qc\) instead of \(c\), and the two normalization conditions still force the right arrow \(n/2\). No such rescaling is assumed without being stated.

### ALG04-R: differentiation in the monic coordinate algebra

In \(A=k[x,y]/(y^2-f(x))\), \(f\) squarefree of degree three and \(2\in k^\times\), the rule

\[
Dx=y,\qquad Dy=\tfrac12 f'(x)
\]

preserves the relation because \(D(y^2-f(x))=2y(f'/2)-f'y=0\). Conversely, differentiating the relation for a derivation with \(Dx=y\) gives \(y(2Dy-f')=0\); the algebra is an integral domain and \(y\ne0\) as a function, so cancellation is legitimate even though \(y\) vanishes at some points. Hence \(D^2x=f'/2\). At any branch point \(P=(e,0)\), squarefreeness gives \(f'(e)\ne0\), so \(Dx(P)=0\) differs from \(D^2x(P)=f'(e)/2\).

If the uncertain squared term in (31) is retained instead, let \(G=y^2-(x^3+a_1x^2+a_2x^2+a_3)\). The same written derivation has \(DG=a_2(1-2x)y\), a nonzero normal form modulo \(G\) for \(a_2\ne0\). The script verifies both residual identities symbolically. This only tests compatibility between (31) and (32); it does not decide how the uncertain exponent was written.

### ALG05-R: smooth completion, graded presentation, and all branch points

The affine curve \(y^2=f(x)\) is smooth because a singular point would have \(2y=0\), \(f'(x)=0\), and \(f(x)=0\), contrary to \(2\ne0\) and squarefreeness. In the projective cubic

\[
Y^2Z=X^3+a_1X^2Z+a_2XZ^2+a_3Z^3,
\]

the only point with \(Z=0\) is \(O=[0:1:0]\); the partial derivative with respect to \(Z\) there is \(1\). The curve is geometrically integral: over an algebraic closure, \(f(x)\) has a simple zero and so cannot be a square in \(\bar k(x)\); hence \(y^2-f(x)\) is irreducible. The smooth plane-cubic genus formula gives genus one, and \(O\) is rational. This proves the claimed elliptic completion without omitting the point at infinity.

On the chart \(Y\ne0\), set \(u=X/Y,\ v=Z/Y\). The equation is

\[
v=u^3+a_1u^2v+a_2uv^2+a_3v^3.
\]

The partial derivative in \(v\) is \(1\) at \(O\), so \(u\) is a local parameter and \(v=u^3+\text{higher terms}\). Therefore \(x=u/v\) has pole order \(2\) and \(y=1/v\) has pole order \(3\). The graded section ring has the concrete presentation

\[
R=\frac{k[S,X_2,Y_3]}{Y_3^2-X_2^3-a_1X_2^2S^2-a_2X_2S^4-a_3S^6},
\qquad \deg(S,X_2,Y_3)=(1,2,3).
\]

Here \(S=T,\ X_2=xT^2,\ Y_3=yT^3\). Reduction to monomials with \(Y_3\)-exponent at most one gives exactly the pole-order bases; hence this is the section ring, not merely a putative homogenization. Its third Veronese is generated by \(S^3,X_2S,Y_3\) and gives the ordinary plane cubic above, so \(\operatorname{Proj}R\simeq E\). Specializing \(S=1\) recovers the affine algebra \(F_\infty\), but loses the grading needed in that Proj statement.

At a simple root \(e\), \(y\) is a local parameter and \(x-e=y^2/f'(e)+\text{higher terms}\), so the ramification index of \(x:E\to\mathbf P^1\) is \(2\). At \(O\), \(1/x\) has a double zero, giving the fourth ramification point. Away from \(y=0\) and \(O\), the derivative \(2y\) is invertible and the quadratic cover is étale. This confirms the explicit four-point statement on scan 114.

### ALG06-R and ALG07-R: divisor proof and exact factorizations

For three distinct affine points \(P,Q,R\), a zero determinant means that \(1,x,y\) have a nontrivial linear dependence after evaluation. The columns \(1,x\) are independent: otherwise all three \(x\)-values would coincide, impossible for three distinct points in a degree-two fibre. The coefficient of \(y\) can therefore be normalized to one, giving \(g=y+\alpha x+\beta\) with a pole of exact order \(3\) at \(O\). Its three distinct prescribed zeros exhaust its degree-three zero divisor, so \(\operatorname{div}(g)=P+Q+R-3O\). The elliptic identification \(E\simeq\operatorname{Pic}^0(E)\), \(P\mapsto[P-O]\), gives \(P+Q+R=O\); the converse follows from the same divisor equivalence. This independently checks the proof actually supplied on scans 110–111, including the place where distinctness is used.

For \(P=(u,r),Q=(v,q)\) with \(u\ne v\), put

\[
\lambda=\frac{r-q}{u-v},\qquad
\mu=\frac{qu-rv}{u-v},\qquad
w=\lambda^2-a_1-u-v.
\]

Using only \(r^2=f(u)\) and \(q^2=f(v)\), exact polynomial division gives

\[
f(t)-(\lambda t+\mu)^2=(t-u)(t-v)(t-w).
\]

The third point is \((w,\lambda w+\mu)=-(P+Q)\), with intersection multiplicities permitted. This proof works even when \(w=u\) or \(w=v\), and thus justifies the manuscript's prolongation without assuming a third *distinct* root. The exclusions \(P\ne Q, Q\ne-2P,P\ne-2Q\) in (50) alone do not exclude \(P=-Q\), as the rational example in ALG07 shows; the NB \(u\ne v\) must remain part of the hypotheses.

When \(P=Q=(u,r)\) with \(r\ne0\), substitute \(\lambda=f'(u)/(2r)\) and \(\mu=r-\lambda u\). The same calculation yields

\[
f(t)-(\lambda t+\mu)^2=(t-u)^2(t-w),
\qquad w=\lambda^2-a_1-2u.
\]

The point on the tangent is \(-2P\); negating its ordinate gives \(2P\). If \(r=0\), the tangent is vertical and \(P=-P\), so \(2P=O\). The script proves both rational factorizations by solving/substituting the point equations and reducing the resulting symbolic expression exactly to zero. It does not attempt to infer group associativity from a finite sample.

### ALG08-R: matrix and translation check

Let \(b_i=\xi_j\xi_h-\xi_i(\xi_j+\xi_h)\). Then \(\xi_i^2+b_i=A_i=(\xi_i-\xi_j)(\xi_i-\xi_h)\ne0\), and

\[
M_i=\begin{pmatrix}\xi_i&b_i\\1&-\xi_i\end{pmatrix},
\quad M_i^2=A_iI,
\quad\det M_i=-A_i.
\]

Its Möbius map is \(\xi_i+A_i/(z-\xi_i)\), sends \(\infty\leftrightarrow\xi_i\), and sends \(\xi_j\leftrightarrow\xi_h\) by substitution. It is nonidentity, hence has order two. The compositions of the three displayed double transpositions give \(\sigma_i\sigma_j=\sigma_h\); alternatively the script checks this as an exact rational identity.

If \(e_i\in E[2]\setminus\{O\}\), the translation \(\tau_{e_i}\) satisfies \([-1]\tau_{e_i}(P)=-P-e_i=-P+e_i=\tau_{e_i}[-1](P)\), so it descends to \(E/\{\pm1\}\). On \(E[2]\) it swaps \(O,e_i\) and the other two nonzero elements. Its quotient action and \(M_i\) therefore agree on three distinct projective points and are the same projective automorphism. This proves the geometric assertion at the supplied endpoint without importing a continuation as manuscript text.

Hua's modernisation explicitly credits to its own reformulation the factorization of the fixed-point equation as \((z-\xi_i)^2=A_i\). It is compatible with this matrix check, but the supplied manuscript stops before writing that equation. If used in the main notes, it should be identified as a contextual continuation/independent consequence, not quoted as scan 115.

## Verification artifacts and limits

- *records/verify_algebra.py*: executable exact SymPy identities and modular matrix checks; no input from images or transcription modifications.
- *records/verify_algebra_output.json*: successful output of the actual run, including the tested characteristics and pole ranges.
- *records/check_events_algebra.tsv*: only proof checks and computations actually performed here. Context reading by itself is not logged as a proof check.

These checks do not determine the intended normalization of \(\varepsilon_n\), choose the uncertain prime/exponent/subscript readings, or validate every claim in the supplied results register. They do distinguish a false all-degree symbol statement, the precise positive-characteristic kernel, a consistent alternative normalization, valid later algebra after specifying coordinates, and an error the author already withdrew.

## Primary external references actually consulted

1. The Stacks Project Authors. Lemma 10.158.2, **Tag 031W**, “Formal smoothness of fields.” [Source](https://stacks.math.columbia.edu/tag/031W). Used only for \(\ker(d:K\to\Omega_{K/k})=K^p\) over a perfect field; local filtration consequences proved here. Opened and cross-checked in this run on 2026-11-17.
2. The Stacks Project Authors. Section 53.9, **Tag 0BYA**, especially Lemma 53.9.3, “Plane curves.” [Source](https://stacks.math.columbia.edu/tag/0BYA). Used for the genus of a smooth plane cubic; smoothness and explicit completion checked here. Opened on 2026-11-17.
3. Sutherland, Andrew V. (2021). *18.783 Elliptic Curves*, Lecture 2, “Elliptic curves as abelian groups,” §§2.1–2.2. [Source](https://math.mit.edu/classes/18.783/2021/LectureNotes2.pdf). Primary author lecture notes for the chord/tangent rule, sign, and affine cases; its convenient characteristic-\(\ne2,3\) presentation is not used to remove characteristic \(3\) from the manuscript. Opened on 2026-11-17.
4. Lynn, Ben. “Explicit Addition Formulae,” *Elliptic Curves* author notes. [Source](https://crypto.stanford.edu/pbc/notes/elliptic/explicit.html). General Weierstrass addition/doubling comparison; the manuscript's \(a_1,a_2,a_3\) denote cubic coefficients, not Lynn's standard five-coefficient notation. Opened on 2026-11-17.

**External context credit:** Michel Hua's project, *context/hua_project/64.modern.tex*, the three named subsections above. This is an AI-produced interpretation supplied as context, not a primary manuscript or a reviewed mathematical authority. Its ordinary principal-part convention is stated explicitly; no long passage has been reproduced.
