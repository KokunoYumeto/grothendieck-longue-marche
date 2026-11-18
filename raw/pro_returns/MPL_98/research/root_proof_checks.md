# Additional proof checks by the root

**Run:** MPL_98, 18 November 2026. **Researcher:** GPT-6 Astra Pro, effort inherited/unspecified, root. These are research arguments written after the transcription freeze. They do not modify or certify the readings. The main notes have the manuscript and context locators; the longer norm, boundedness, and cohomology memoranda contain the other proofs and their precise limitations. None of the examples below is claimed to be new.

## N04 — The first-order term of the norm

Locally let a finite locally free algebra \(B/A\) have basis of size \(r\), and write \(M_b\) for multiplication by \(b\). Over \(A[\epsilon]/(\epsilon^2)\), multiplication by \(1+\epsilon b\) is \(I+\epsilon M_b\). In the determinant expansion, the identity permutation contributes \(1+\epsilon\sum_i(M_b)_{ii}\); every other contributing permutation moves at least two indices and therefore contributes a term divisible by \(\epsilon^2\). Thus
\[
N_{B/A}(1+\epsilon b)=1+\epsilon\operatorname{Tr}_{B/A}(b).
\]
The calculation needs no division by \(r!\), works over any commutative base ring, and glues because determinant and trace are basis independent. This checks the infinitesimal link in N04, not the arithmetic norm-image entries in RESULTS_STATE.

## N15 — Why the covering model does not cover ramification

For a field \(k\), \(B=k[\epsilon]/(\epsilon^2)\) is finite free of rank two over \(k\), but is not étale: its geometric fibre remains nonreduced. A nonempty faithfully flat base change preserves the nonzero free basis vector \(\epsilon\), so it cannot turn this algebra into the constant two-point étale algebra. Consequently an argument that trivializes a principal finite covering as a finite set does not by itself establish the norm construction for this example. The determinant construction does handle it, as N03 and the norm memo show. This is a scope check on a proposed method, not a refutation of the manuscript’s finite locally free model.

## B11 — Dependence of a tensor operation on relative embeddings

Let \(\Omega\) be an algebraically closed overfield of \(k\) containing two distinct elements \(a,b\), and put \(R=\Omega[x]\). For the point modules,
\[
R/(x-a)\otimes_R R/(x-b)\simeq R/(x-a,x-b).
\]
If \(a=b\), this is the same point module. If \(a\ne b\), the ideal contains the nonzero constant \(a-b\), so it is the unit ideal and the tensor product is zero. Taking \(a,b\) transcendental over \(k\) realizes the aligned and independently embedded representatives of the same geometric-class inputs described in B07–B11. The relative positions are data of a compositum witness; separate input classes do not determine them.

## B12 — Reduced support after an inseparable extension

Assume \(\operatorname{char}(k)=p>0\) and \(a\notin k^p\). The polynomial \(x^p-a\) is irreducible over \(k\), so \(R=k[x]/(x^p-a)\) is a field and in particular reduced. For \(K=k(a^{1/p})\),
\[
R\otimes_kK\simeq K[x]/((x-a^{1/p})^p).
\]
The class of \(x-a^{1/p}\) is nonzero and nilpotent. Hence scalar extension of the reduced support and reduction of the scalar-extended support differ. This checks the boundary example only; the positive finite-type assertion over an algebraically closed field is the usual geometric-reducedness fact and is not a claimed new proof.

## B13 — A varying embedded primary component

In \(k[x,y]\), let \(Q_a=(x^2,y-a x)\). Its quotient is \(k[x]/(x^2)\), so \(Q_a\) is \((x,y)\)-primary. Moreover
\[
(x)\cap Q_a=(x^2,x(y-a x))=(x^2,xy).
\]
To check the nontrivial containment, write an element of \(Q_a\) as \(x^2u+(y-a x)v\). If it lies in \((x)\), reducing modulo \(x\) gives \(y\,v(0,y)=0\), hence \(v\) is divisible by \(x\). The displayed equality follows. For distinct \(a\), the ideals \(Q_a\) are distinct, since their linear parts span different lines. Thus the embedded primary component need not be canonical even though the isolated component \((x)\) is fixed. This does not assert that the manuscript claimed otherwise.

## B15 — The local Hom base-change mechanism

On an affine chart, a finite presentation
\[
B^p\longrightarrow B^q\longrightarrow M\longrightarrow0
\]
gives
\[
0\longrightarrow\operatorname{Hom}_B(M,N)\longrightarrow N^q
\xrightarrow{d}N^p.
\]
The same presentation after any scalar extension computes the new Hom module as the corresponding kernel. On a stratum where \(N\) and \(\operatorname{coker}(d)\) are flat over the parameter ring, the image of \(d\) is flat: use the exact sequence with middle term \(N^p\) and flat quotient. Tensoring the exact sequence ending in that image then preserves its kernel. This proves the desired kernel base change.

Under the noetherian finite-type assumptions, the finitely many modules involved are finite over the chart algebra, and generic flatness followed by noetherian induction supplies finitely many suitable strata. On each stratum the presentation and coefficient family are first restricted, and the Hom construction for that restricted family commutes with further base change. This does not assert that restriction of the original Hom module already gives that newly computed Hom: for \(A=k[t]\), \(M=A/(t)\), \(N=A\), the original Hom is zero but the Hom of the two restricted modules at \(t=0\) is \(k\). The newly computed Hom families suffice to parameterize the fibrewise Hom outputs. A finite affine cover allows a common refinement of those strata, and the canonical local maps agree on restrictions within each stratum. This explains the source’s local-lemma request; it does not replace a written coefficient symbol in the transcription.

## B25 — Why the Ext comparison maps glue

Use the flatness and finite-resolution hypotheses identified in B22–B24. Work with full projective resolutions when constructing comparison maps, even if only a finite cohomological range is subsequently retained. A map between modules lifts to a chain map of projective resolutions, and any two lifts are homotopic. The natural map
\[
\operatorname{Hom}_B(P^\bullet,N)\otimes_A A'
\longrightarrow
\operatorname{Hom}_{B'}(P^\bullet\otimes_A A',N\otimes_A A')
\]
commutes with restriction and with such chain maps; for finite free terms it is the ordinary finite direct-sum identification. The flatness assumptions make the extended resolution compute the required new module in the asserted range. Thus the induced cohomology maps are independent of the local resolution and agree on intersections. The resulting maps glue for the claimed \(p\le N\) Ext range. This is a check of canonicity, not an assertion that an arbitrary truncated last term computes the next Ext group.

## B30 and B31 — Two short boundedness checks

For B30, if \(T_i\) with coherent family \(\mathcal F_i\) parameterizes each of finitely many bounded families, then \(\coprod_iT_i\) and the sheaf restricting to \(\mathcal F_i\) on each component parameterize their union. A finite disjoint union preserves the required finite-type/noetherian conditions.

For B31, the global map \(\mathcal O_{\mathbf P^1}^{\,2}\to\mathcal O_{\mathbf P^1}(n)\) defined by the sections \(X^n,Y^n\) is surjective: at every point at least one coordinate is nonzero. The sheaf is pure of generic length one on its support. For \(n>0\),
\[
\operatorname{Hom}(\mathcal O(n),\mathcal O)
=H^0(\mathbf P^1,\mathcal O(-n))=0.
\]
There is therefore no nonzero map, and in particular no inclusion into the structure sheaf of the support. This verifies a concrete obstruction to the tentative generic-length-one step, conditional on the interpretation of the pale pencil argument. The bounded-cycle counterexample itself is developed in the boundedness memo.

## T02 — Restricting a quotient map

Let \(f:X\to Y\) be a quotient map and \(A\subseteq X\). The restriction \(g:A\to f(A)\), with the subspace topology on the target, is always a continuous surjection. It is a quotient map precisely when, for every relatively saturated open \(B\subseteq A\), its image \(f(B)\) is relatively open in \(f(A)\). Indeed \(B=g^{-1}(g(B))\), while every inverse image \(g^{-1}(U)\) is relatively saturated. This is exactly the definition of a quotient map applied to \(g\). Taking complements gives the equivalent closed-set criterion.

When the criterion holds, write \(f(B)=O\cap f(A)\) with \(O\subseteq Y\) open and put \(D=f^{-1}(O)\); then \(D\) is saturated and open, \(f(D)=O\), and the relevant trace is on \(f(A)\). This explains the proposed repair of the typescript’s repeated \(f(B)\). It does not prove that the restriction of every quotient map is quotient.

## T14 and T13 — Positive gluing hypotheses and a counterexample

For compatible pairwise identifications, assume all overlap subsets are open in both pieces. Saturating an open subset of one piece has open trace in every other piece: the trace is transported through an overlap homeomorphism from an open subset of an open overlap. Hence its saturation is open in the disjoint union and its image is open in the quotient. This proves that each piece has its original topology as a subspace. The same argument with closed subsets proves the result when all overlaps are closed in both pieces. The compatibility conditions are needed to prevent further unintended identifications.

To see why overlap homeomorphisms alone do not suffice, take \(X_1=\{a,b\}\) discrete; \(X_2=\{a,c\}\) with opens \(\varnothing,\{c\},\{a,c\}\); and \(X_3=\{c,b\}\) with opens \(\varnothing,\{b\},\{c,b\}\). Identify the equal labels on their singleton overlaps. The identifications are homeomorphisms and the triple compatibility conditions are vacuous. A subset of the quotient is open exactly when its intersection with each piece is open. Checking the eight subsets gives
\[
\varnothing,\quad \{b\},\quad \{b,c\},\quad \{a,b,c\}.
\]
Its trace on \(X_1\) is \(\varnothing,\{b\},\{a,b\}\), which omits the original open set \(\{a\}\). The canonical map of \(X_1\) is injective and continuous but is not an embedding. This answers the exercise with an independently checked finite example; the norm researcher’s separate review records the same calculation.

For the product assertions in T03, finite intersections of coordinate inverse images of open sets form the product basis. Pulling back those basis elements proves the coordinatewise continuity criterion; applying that criterion in both directions proves regrouping homeomorphisms. For \([0,1]\to\mathbb R/\mathbb Z\), a closed subset of the compact interval has a locally finite union of closed integral translates in \(\mathbb R\), yielding the asserted quotient topology. These checks do not identify the author or edition of the reused text.

## T04, T05, and T09 — Extent of the abelian-variety comparison

The inspected modern comparator is Milne (1986/2022), Propositions 8.1, 9.1–9.2, Remark 7.3, and the paragraph following Proposition 9.2; Milne (2008), I, Proposition 6.3 supplies the point/tangent separation distinction. Exact source witnesses and inspection limits are in primary_sources.md.

For T04, pulling \(m^*L\simeq p_1^*L\otimes p_2^*L\) back along \((\alpha,\beta)\) gives the additive pullback formula. Induction gives the multiplication formula for positive integers, the zero map gives the neutral class, and inversion gives negative integers. This checks the inference from the cited Picard-zero identity.

For T05, a homomorphism \(A\to A^\vee\) with finite kernel has image of dimension \(\dim A\); the dual has the same dimension. Properness makes the image closed, so it is all of the connected abelian variety \(A^\vee\), giving the isogeny criterion. The zero-map criterion \(\phi_L=0\iff [L]\in\operatorname{Pic}^0(A)\) is a separate inspected literature statement, not a consequence of finite kernel. No proof of the source’s entire postponed chapter is claimed.

For T09, Proposition 9.1 is applied with the nonzero-section/effectivity hypothesis, and Remark 7.3 gives a very ample tensor power. Theorem 7.1 independently states projectivity of every abelian variety. The historical phrase “birationnelle et biholomorphe” is retained in the transcription; the comparison does not replace it with an anachronistic definition.

## T06–T08, T11, and T12 — Coefficient flags and literal formula defects

Let \(V\ne0\) be finite dimensional over \(K\), with an injective expansion into a sequence of coefficients, and suppose the coefficient functionals \(\ell_0,\ell_1,\ldots\) are \(K\)-linear. Put \(V_j=\bigcap_{i<j}\ker\ell_i\). The chain is decreasing, every step drops dimension by at most one, and injectivity gives \(\bigcap_jV_j=0\). A decreasing chain in a finite-dimensional space stabilizes; its stable value must therefore be zero. At the final nonzero step the dimension is one. Since the space and maps are defined over \(K\), that line has a nonzero \(K\)-vector. This proves the mechanism in T06 under its explicit hypotheses.

Write \(C_{i\mu}\) for the coefficient of the \(\mu\)-th monomial in \(f_i\). The unknown coefficient vector has the fixed length \(n+1\), and the equations are \(\lambda^T C_{\mathrm{prefix}}=0\); it is this left kernel whose dimension is \((n+1)-\operatorname{rank}(C_{\mathrm{prefix}})\). In T07, taking the prefix through the first full-rank column therefore cannot give a nonzero solution up to scale. The preceding prefix has rank \(n\), since adjoining one column changes rank by at most one, and consequently gives a one-dimensional solution space in the same coefficient variables. With basis \(1,t\), the full coefficient matrix already contains the \(2\times2\) identity, making the error explicit. T11 is a separate mismatch: expanding \(\sum_{i=0}^n\lambda_i f_i\) cannot generally discard the \(i=0\) coefficient.

For T08, order monomials by increasing total degree, with an arbitrary order within each degree. The series whose first \(j\) coefficients vanish form an ideal: multiplying any surviving monomial by a positive-degree monomial moves it to strictly larger degree and hence a later position, while constants preserve it. The written lower summation limit \(\infty\) is a separate literal anomaly and is unchanged.

For T12, a rational function belongs to the multiplicative function group, whereas its principal divisor belongs to the divisor group. Applying the divisor homomorphism to the displayed product would give a well-typed equality. This is a proposed reading-level correction only; no unrecorded outer operator has been inserted into the frozen formula.

## Source-comparison checks

The research-stage comparisons in R09, R12, and R13 were made against the frozen page fragments and Hua98. They establish a difference between those two textual records: input flatness is present on scan 039; scan 043 says A-flat; scan 028 already states the required extension direction. They do not constitute another image audit or an independent palaeographic witness. In particular, the earlier root event describing B19 as an omitted-hypothesis counterexample has been corrected in the final ledger: the counterexample checks the necessity of a hypothesis already present.
