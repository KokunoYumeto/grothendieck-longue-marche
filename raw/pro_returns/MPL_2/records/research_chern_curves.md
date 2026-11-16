# Chern torsion and curve/surface Riemann–Roch: research contribution

These notes were composed after the transcription was frozen, from the frozen TEX only; no source image was opened and no transcription file was edited. `context/README.md` and `context/notes/RESULTS_STATE.md` contain no neighbouring transcription and no matching settled or open research-register item; the relevant imported lead is **Hua, findings register, 2-trivial-total-chern-class**, explicitly AI-produced and unreviewed, citing this package's scans 010,012,014. The per-note searches are recorded in `records/context_search_chern_curves.md`; “no context match” below means no relevant passage in those two supplied files, not absence from the archive or literature.

## Proposed individual notes

### CC01 — Cote 2, scan 010, left square and composition — Unproved claim

The label “injectif” is supported on the sheet by `p_*i_*(x)=(pi)_*x=x`, which supplies a left inverse to the constant-section pushforward in coherent K-theory under the usual proper-pushforward conventions. This identifies the correct nonvanishing argument for the later torsion example: it uses the projection's direct image, not a claim that restriction to the section is injective (Borel & Serre, 1958, §5d). **Context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, already asserts nonvanishing; this page supplies its key step, without turning that unreviewed register row into an independently established result.

### CC02 — Cote 2, scans 010–012, Chern product and Q-polynomials — Unproved claim

The leading term `1+(-1)^{r-1}(r-1)! eta^r` and the later `Q_1^{(r)}(c^1)=-rc^1` point to two distinct factorial coefficients: the rank term has `(r-1)!`, while a rank-zero curve class contributes `r!` one degree later. An integral product expansion of the written binomial sum verifies this distinction, so the two coefficients should not be conflated by a rational Chern-character argument (derivation A below). **Context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, retains only the stronger `(r-1)!` annihilation condition; these calculations refine its sufficient criterion.

### CC03 — Cote 2, scan 012, final warning — Unpursued implication

“s'il y a de la torsion dans A(X), l'hom (i_*)_r est non injectif” needs a statement about the order and degree of that torsion relative to the actual coefficients for the fixed r. On the abstract graded ring `A=Z⊕(Z/5)α`, `α²=0`, the rank-zero part for r=2 is multiplication by 2 and is injective, so an argument based only on the presence of torsion is insufficient. This is an abstract algebraic diagnostic, not an assertion that a smooth scheme with this Chow ring occurs in the manuscript's geometric family or a geometric counterexample under its unstated conventions. **Own diagnostic confidence: high** for that limited conclusion, by the integral calculation in derivation A; **context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, supplies an explicit annihilation hypothesis that is safer than the unrestricted wording.

### CC04 — Cote 2, scan 012, first cases display — Reading question

The frozen cases display for `Q_i(---)` has no `eta^r` factor in its second branch, although the following total-class formula includes that factor and calls `Q_{i-r}^{(r)}` a coefficient polynomial. It is worth checking whether this is deliberate coefficient extraction or a dropped factor; neither interpretation licenses inserting it into the frozen transcription. **Context:** the per-note search found no `Q_i`, isobaric-weight, or eta passage in README.md or RESULTS_STATE.md, and no neighbouring scan was supplied.

### CC05 — Cote 2, scan 014, crossed upper block and live N.B. — Withdrawn in the same text

The hypersurface proposal beginning “Soit donc Y une hypersurface” is crossed out on the same sheet, whereas the live replacement uses “x=(a)-(0)” on an elliptic curve. **Context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, describes `i_!(O_Y)` and thus preserves the withdrawn setup rather than accurately identifying the final written example; a nonzero effective divisor of torsion class cannot occur on a proper smooth curve, since its degree is positive. Nevertheless, under a smooth ambient-space/effective-Cartier-divisor interpretation the register's conditional vanishing assertion can be checked by the integral calculation in derivation B, so the necessary correction is to its attribution and hypotheses, not a blanket mathematical rejection.

### CC06 — Cote 2, scan 014, live elliptic example — Unproved claim

The example “a+a=0, a≠0” works over C: take a nontrivial 2-torsion line bundle L on an elliptic curve E, put `x=[L]-1` with `α=c_1(L)≠0`, and push it along a constant section into `E×P^3`. The direct integral formula `c(i_!x)=1-6αh^3=1`, together with `p_!i_!x=x≠0`, verifies the intended vanishing of all positive Chern classes without discarding torsion; x is the rank-zero divisor-class representative of the written point difference. **Context:** this checks the central phenomenon in RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, while replacing its description by the sheet's live example; no novelty or reviewed-status claim is made.

### CC07 — Cote 2, scans 012 and 014, epsilon term versus N.B. — Own idea

The N.B. assertion that all `C^i(x)` being annihilated implies vanishing after pushforward requires a rank-zero condition if `C^i` means positive Chern classes: the visible `epsilon(x)` term on012 remains. Indeed `x=[O_X]` has zero positive Chern classes, whereas `c_r(i_!x)=(-1)^{r-1}(r-1)!h^r` is nonzero for the section into a projective-space factor. **Confidence: high**, because this is the rank term of the sheet's own formula and is also verified by the Koszul resolution; **context:** Hua **2-trivial-total-chern-class** in RESULTS_STATE.md, scans 010/012/014, implicitly has rank zero through `O_Y`, but the live general sentence on 014 needs that qualification or an explicit augmented-class convention.

### CC08 — Cote 2, scans 010/012/014, zero versus unit — Reading question

The frozen text alternates formulas with initial1 and the statement `Ctilde(y)=0`; in an augmented Chern ring whose addition is multiplication of total classes, additive zero is represented by `(0,1)`, so these need not express opposite mathematical claims. Grothendieck's published construction explicitly uses `Z×(1+A_+)` with that additive convention (Grothendieck, 1958, §4,2°, pp. 147–149), but it is external comparison rather than permission to rewrite014. **Context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, writes total Chern class 1 and should identify this convention rather than silently substituting 1 for the manuscript's 0.

### CC09 — Cote 2, scans 012/014, factorial bound — Own idea

For a rank-zero line-bundle difference on a smooth curve, the exact integral coefficient is `(-1)^r r!αh^r`, so the same elliptic2-torsion construction already gives a nonzero class with trivial total Chern class on `E×P^2`. **Confidence: high**, because the finite-difference computation in derivation A is an identity over the integers before torsion specialization. **Context:** RESULTS_STATE.md, Hua **2-trivial-total-chern-class**, scans 010/012/014, says “possible only for r≥3”; this is correct for its stated stronger hypothesis `(r-1)!α=0`, but it is not a minimal-dimension claim for the underlying phenomenon, and the present observation is our extension rather than something the page asserts.

### CC10 — Cote 2, scan 041, formula(2) — Unproved claim

“Il y a alors une formule meilleure” displays a quotient by the top Chern class of a normal-type bundle, and a proof must explain both the regular-immersion hypothesis and universal polynomial divisibility before specializing the formula. An evaluated top Chern class need not be invertible and can be zero—for example for the constant section of a trivial projective-space product—so the expression cannot simply mean ordinary division in the Chow ring. The published rational theorem and its contemporary warning about stronger integral formulas give useful comparison points (Borel & Serre, 1958, §7, p. 113), but **context:** neither README.md nor RESULTS_STATE.md contains a matching immersion formula or neighbouring scan.

### CC11 — Cote 2, scan 041, E^(i) with fibre cohomology — Own idea

The assertion “E^(i) est le fibré vectoriel … dont la fibre est le iième groupe de cohomologie” requires cohomology-and-base-change hypotheses, since even a product projection with a varying vector bundle can have jumping fibre cohomology. For an elliptic curve, the Poincaré line bundle on `E×Pic^0(E)` has `h^0=h^1=1` at the trivial line bundle and 0 at all nontrivial degree-zero line bundles, so those groups do not form vector bundles of locally constant rank. **Confidence: high**, because degree-zero line bundles with a section are trivial and curve Riemann–Roch gives the stated h^1; this diagnoses a missing condition rather than disproving a suitably restricted meaning of “application fibrée” (The Stacks Project Authors, n.d., Tags0AYQ,0BDM). **Context:** no relevant cohomology/base-change passage or scan occurs in the supplied context.

### CC12 — Cote 2, scan 041, large twist — Unproved claim

The claim “E^(i)=0 pour i>0 … E(n) … n grand” is justified by relative Serre vanishing when the twist is relatively ample, the morphism proper, and the sheaf coherent over a Noetherian base. Calling the surviving `f_*E(n)` a vector bundle additionally needs the relevant flatness/base-change condition; for a sheaf flat over the base, higher-direct-image vanishing yields finite local freeness (The Stacks Project Authors, n.d., Tags02O1,0BDM). **Context:** the search in README.md and RESULTS_STATE.md found only an unrelated GT-character occurrence of “vanishes,” with no relevant item or source scan.

### CC13 — Cote 2, scan 042, restriction of the Todd class — Unproved claim

The passage from `C_Z(i^*T_X)` to `C_Z(T_Z)` is explained for a fibre of a smooth morphism between smooth varieties by the exact tangent sequence, whose quotient is the constant vector space `T_yY` tensored with `O_Z`, and therefore has trivial positive Chern classes. It is not an equality of the two tangent bundles themselves, and a singular fibre or a nonsmooth morphism requires a different, usually virtual, tangent argument. **Context:** no matching tangent/Hirzebruch/fibre passage or neighbouring scan appears in README.md or RESULTS_STATE.md; the published fibre-integration discussion is a useful independent comparison (Borel & Serre, 1958, §17).

### CC14 — Cote 2, scans 042–043, higher components and eventual polynomiality — Unpursued implication

The observation that the positive-degree components contain information absent from numerical Hirzebruch–Riemann–Roch leads to the underlined claim that the “classe de Chern modifiée” of `f_*E(n)` “dépend polynomialement de n.” In the smooth projective setting with relative dimension d, the displayed exponential gives `ch_j(f_!E(n))` as a rational polynomial of degree at most d+j, and relative Serre vanishing identifies `f_!E(n)` with `f_*E(n)` for large n; the ordinary Chern components are then polynomial after tensoring with Q by the universal conversion formulas, without the same automatic degree bound or an assertion about integral torsion (The Stacks Project Authors, n.d., Tags02O1,02UM). **Confidence: high for this rational consequence**, because the degree bound follows by selecting the codimension d+j term before pushforward. **Context:** no polynomiality or Chern-character passage or source scan is supplied in README.md or RESULTS_STATE.md, so this adds a concrete subject beyond the title-based RR placement rather than settling a listed open ID.

### CC15 — Cote 2, scan 043, boxed curve-to-curve formula — Unpursued implication

The half-canonical expression for `f_!(n,d)` follows in `Pic(Y)⊗Q`, but it does not uniquely determine a Picard class when2-torsion is present. An integral formulation records the actual line bundle `det(f_*O_X)` and uses `det(f_*E)=Nm_f(det E)⊗det(f_*O_X)^n`, thereby retaining the information that a choice-free division by 2 would lose. **Own extension confidence: high** in the finite-flat smooth-curve setting, because this determinant identity can be checked after local trivialization and the rational class agrees with the displayed RR formula; **context:** no Picard, determinant, or canonical-divisor entry or neighbouring scan is present in the two supplied context files.

### CC16 — Cote 2, scan 044, “séparable ou non” — Unpursued implication

The parenthesis “séparable ou non” is compatible with the rank and degree calculation for a finite nonconstant morphism of smooth proper curves: such a map is finite flat, and neither Euler-characteristic preservation nor the rational RR expression requires separability. As a direct check, relative Frobenius of a smooth curve of genus g in characteristic p has rank p and `deg(F_*O_X)=(p-1)(g-1)`, matching the displayed half-canonical degree formula. **Own diagnostic confidence: high**, from the degree–Euler-characteristic identity and finite-flatness criteria (The Stacks Project Authors, n.d., Tags0AYQ,0BXX); **context:** no separability, ramification, or Frobenius passage or source scan was found.

### CC17 — Cote 2, scan 044, curve-to-surface calculation — Unproved claim

The final live boxed expression is algebraically consistent with `ch_2=(c_1²-2c_2)/2`: for rank n and degree-class d on the source curve, one obtains `ch_1=nδC` and `ch_2=f_*d-(n/2)f_*K_X+(nδ/2)CK_Y`. Thus `c_2=(n²δ²/2)C²-(nδ/2)CK_Y-f_*d+(n/2)f_*K_X`, an equality in `CH²(Y)⊗Q` matching the written live formula, while the quadratic Todd terms crossed out earlier cannot contribute because the pushforward has rank zero on a surface. **Context:** neither supplied context file contains this surface calculation or a neighbouring source scan; the conversion formula is independently fixed by The Stacks Project Authors (n.d., Tag 02UM), and this is an algebraic consistency check, not a retrospective repair of crossed ink.

### CC18 — Cote 2, scan 045, first display and normalization sentence — Own idea

The written `C²(O_C)` is followed by “de la normalisée,” but the preceding044 calculation actually applies to `f_*O_{\widetilde C}` for the normalization map, which differs from `O_C` at singular points. For a reduced Cartier curve in a smooth surface, the integral exact sequence `0→O_C→ν_*O_{\widetilde C}→Q→0` gives `c_2(O_C)=c_2(ν_*O_{\widetilde C})+[Q]`, while the divisor resolution gives `c_2(O_C)=C²`; here `[Q]` is the 0-cycle of normalization defects (The Stacks Project Authors, n.d., Tags0C44,0ESY). **Confidence: high** under these stated hypotheses, because the two exact sequences fix the sign and identify the missing finite-length term. **Context:** no normalization or `O_C` item or neighbouring scan was found in README.md or RESULTS_STATE.md; the issue is an additional diagnostic, not a correction to the frozen wording.

### CC19 — Cote 2, scan 045, numerical genus formula — Own idea

A rational nodal plane cubic gives an explicit test of the displayed expression `1/2(C²-CK_Y)+g-1`: in `Y=P²`, `C=3H`, `K_Y=-3H`, and normalization genus g=0, it gives 8, whereas `c(O_C)=1/(1-3H)` gives `deg c_2(O_C)=9`. The difference 1 is precisely the node's normalization defect, and 8 is the value for the normalization pushforward instead. **Confidence: high**, because this calculation is integral in `CH^*(P²)=Z[H]/(H³)` and is consistent with the normalization exact sequence (The Stacks Project Authors, n.d., Tag 0C44); **context:** neither context file supplies a singular-curve/genus comparison or prior source scan.

### CC20 — Cote 2, scans 041/043/044, target subscripts — Reading question

The frozen text has `C_Y^q(T_{Y/X})` in041, `varphi_X(f_!(xi))` in043, and “f_*(O_X) … sur X” in044, despite the displayed morphism `f:X→Y`. These are source-level type or notation questions: the published direction of coherent direct image suggests target Y in the latter two expressions, but the first additionally depends on what the written relative-normal notation denotes. **Context:** no corresponding formula or neighbouring scan was supplied in README.md or RESULTS_STATE.md, so literature gives a type-checking reason to ask the question rather than authority to alter a reading (Borel & Serre, 1958, §5d).

## Calculation and evidence appendix for primary review

### A. Integral finite-difference calculation for the live elliptic example

Let E be a smooth elliptic curve over C, choose a nontrivial line bundle L of order2, and write `α=c_1(L)` in `CH^1(E)=Pic(E)`, so `α²=0` and `2α=0`. On `E×P^r`, write `h=c_1(O(1))`, `H=[O(-1)]`, and `x=[L]-1`; the Koszul resolution of a point of `P^r` gives

\[
y=i_!x=x(1-H)^r=\sum_{j=0}^r(-1)^j\binom rj\bigl([L\otimes O(-j)]-[O(-j)]\bigr).
\]

Ordinary total Chern classes are therefore computed **integrally** by

\[
c_t(y)=\prod_{j=0}^r\left(\frac{1+(\alpha-jh)t}{1-jht}\right)^{(-1)^j\binom rj}
=1+\alpha t\sum_{j=0}^r\frac{(-1)^j\binom rj}{1-jht}.
\]

The second equality is valid over a ring with torsion: every product containing two α factors vanishes, and raising `1+αu` to any positive or negative integer m gives `1+mαu`. Expanding the geometric series and using `h^{r+1}=0` yields

\[
\sum_{j=0}^r(-1)^j\binom rj j^m=0\quad(m<r),\qquad
\sum_{j=0}^r(-1)^j\binom rj j^r=(-1)^r r!,
\]

hence

\[
\boxed{c_t(i_!([L]-1))=1+(-1)^r r!\alpha h^r t^{r+1}.}
\]

For r=3 the sole possible positive term is `-6αh³`, and for r=2 it is `2αh²`; both vanish. The class y is nevertheless nonzero: determinant sends x to the nontrivial L, and `p_!i_!x=x` since `p∘i=id`. This proof does not infer integral Chern vanishing from rational-character vanishing; that inference would be invalid for precisely the torsion being studied. It also shows why the rank term in 012 cannot be omitted when x is not rank zero.

The source's point difference has the same rank-zero determinant data on the curve; alternatively one may compute it directly as `[O(-0)]-[O(-a)]`, obtaining the same answer since products of any two divisor classes on E vanish. There is no assertion here that every elliptic curve over every field has the required rational 2-torsion point: the validation is over C, and the manuscript itself explicitly chooses such an a.

### B. Narrow verification of the imported hypersurface condition

Assume X smooth quasi-projective, Y an effective Cartier divisor, `M=O_X(Y)`, `α=c_1(M)`, and r≥1. Then `x=[O_Y]=1-[M^{-1}]`, which is nonzero if α is nonzero because `det x=M`; putting `y=i_!x` gives

\[
c_t(y)=\prod_{j=0}^r\left(\frac{1-jht}{1-(\alpha+jh)t}\right)^{(-1)^j\binom rj}.
\]

A calculation in the torsion-free universal ring `Z[α,h]/(h^{r+1})`, completed in t, gives

\[
\boxed{c_t(y)=1+(-1)^r h^r\sum_{k\ge1}\frac{(r+k-1)!}{k!}\alpha^k t^{r+k}.}
\]

One can derive it over Q by taking logarithms, using finite differences to keep only the `h^r` terms, and then descend the identity to Z: the coefficient `(r+k-1)!/k!` is the integer `(r-1)! binom(r+k-1,r-1)`, and the universal ring is torsion-free. Thus the resulting **integral polynomial identity** may be specialized to a Chow ring with torsion, proving `c_t(y)=1` whenever `(r-1)!α=0`; nonvanishing still follows from `p_!y=x`. This verifies the imported conditional under explicit regularity and Cartier hypotheses; it does not identify it as the live example on 014.

For a proper smooth curve, a nonzero effective divisor cannot have torsion class, because its degree is positive. If a geometric realization of the imported conditional is desired on a nonproper smooth curve, take `X=E\{0}` and `Y={a}` for the same 2-torsion point: `Pic(X)=Pic(E)/Z[0]`, so the effective divisor Y represents the nonzero torsion class of `(a)-(0)`. The condition `(r-1)!α=0` with α nonzero indeed forces r≥3, while the weaker exact curve coefficient `r!α=0` allows r=2; these are different statements.

### C. Missing-rank diagnostic

For `x=1` all positive Chern classes vanish, but the Koszul expression for the section gives

\[
c_t(i_!1)=1+(-1)^{r-1}(r-1)!h^rt^r.
\]

Already taking X to be a point proves that the general N.B. on 014 cannot mean “positive Chern classes alone” without a rank restriction. The source's particular elliptic divisor difference has rank zero, so this caveat does not invalidate it.

### D. Polynomiality and tangent restriction

For a projective morphism between smooth finite-dimensional varieties of pure relative dimension d and a relatively ample L with `ξ=c_1(L)`, GRR gives

\[
\operatorname{ch}(f_!(E\otimes L^n))
=\operatorname{td}(Y)^{-1}f_*(\operatorname{td}(X)\operatorname{ch}(E)e^{n\xi}).
\]

Only finitely many powers of ξ survive; the codimension-j component is polynomial in n of degree at most d+j over Q. Conversion to ordinary Chern classes likewise gives rational polynomiality, not an integral conclusion about torsion. For large n relative Serre vanishing removes the higher direct images; local freeness of the remaining sheaf needs flatness over the base, or other adequate cohomology-and-base-change hypotheses. For a fibre Z over y of a smooth morphism between smooth varieties, the sequence `0→T_Z→T_X|_Z→T_yY⊗O_Z→0` accounts for equality of the Todd classes on Z, rather than equality of tangent bundles.

### E. Curve pushforward and inseparability

For finite flat `f:X→Y` of degree δ between smooth proper curves,

\[
\operatorname{rk}f_*E=\delta n,\qquad
c_1(f_*E)=f_*c_1(E)+\frac n2(\delta K_Y-f_*K_X)
\quad\text{in }\operatorname{Pic}(Y)\otimes\mathbf Q.
\]

The determinant-norm version in CC15 is integral and retains the distinguished determinant line. For Frobenius of degree p on a genus-g smooth curve, finite pushforward preserves Euler characteristic and gives `deg F_*O_X=χ(O_X)-pχ(O_Y)=(p-1)(g-1)`, which agrees with the rational formula; using a separable ramification divisor is unnecessary for this check.

### F. Surface calculation and normalization defect

For a nonconstant map f from a smooth complete curve X to a smooth surface Y, image C and generic degree δ, write ξ for a K-class of rank n and divisor class d. The positive-codimension terms of GRR, in the Chow groups tensored with Q, are

\[
\operatorname{ch}_1(f_!\xi)=n\delta C,\qquad
\operatorname{ch}_2(f_!\xi)=f_*d-\frac n2f_*K_X+\frac{n\delta}2CK_Y,
\]

and conversion to c2 yields exactly the live 044 formula recorded in CC17. With `f=j∘ν` the normalization of a reduced integral Cartier curve C followed by its inclusion, put `Q=ν_*O_{\widetilde C}/O_C`; its cycle has degree `Δ=\sum_x δ_x[k(x):k]`. Then

\[
c_2(j_*O_C)=C^2,\qquad
c_2(f_*O_{\widetilde C})=C^2-[j_*Q].
\]

These identities are integral, by the divisor resolution and the normalization exact sequence. The source's expression with canonical class of the normalization is the rational-GRR value of the second expression, and its degree is `C²-Δ`; its label `O_C` therefore misses the correction when Δ≠0. For a rational nodal plane cubic over C, `Δ=1`, `C²=9`, and `C K_{P²}=-9`, making the discrepancy 8 versus 9 explicit. Nothing in the supplied context resolves this issue, and the frozen TEX remains untouched.

## Primary references and retrieval evidence

- Borel, A., & Serre, J.-P. (1958). Le théorème de Riemann-Roch. *Bulletin de la Société Mathématique de France, 86*, 97–136. https://doi.org/10.24033/bsmf.1500 . Full original: https://www.numdam.org/article/BSMF_1958__86__97_0.pdf . Relevant §5d (pp.110–111), §6 (pp.111–112), §7 (p. 113), §12 (p.125), §17 (pp.135–136). The cited original text supplies the rational-torsion qualification. No quotations from this paper were used beyond title/technical formulas.
- Grothendieck, A. (1958). La théorie des classes de Chern. *Bulletin de la Société Mathématique de France, 86*, 137–154. https://doi.org/10.24033/bsmf.1501 . Full original: https://www.numdam.org/article/BSMF_1958__86__137_0.pdf . Relevant §4, 2° (pp. 147–149), augmented ring and additive-zero convention.
- The Stacks Project Authors. (n.d.). *Normalization of one dimensional schemes* (Tag 0C44, especially Lemma 33.41.2). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/0C44 .
- The Stacks Project Authors. (n.d.). *Applications* (Tag 0BDM, especially Lemmas 36.32.1–4). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/0BDM .
- The Stacks Project Authors. (n.d.). *Lemma 30.16.2* (Tag 02O1). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/02O1 .
- The Stacks Project Authors. (n.d.). *Curves and function fields* (Tag 0BXX, especially Lemmas 53.2.3–4). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/0BXX .
- The Stacks Project Authors. (n.d.). *Degrees on curves* (Tag 0AYQ). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/0AYQ .
- The Stacks Project Authors. (n.d.). *The Chern character and tensor products* (Tag 02UM). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/02UM .
- The Stacks Project Authors. (n.d.). *Chern classes and the derived category* (Tag 0ESY). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/0ESY .

The two original 1958 articles are used as primary historical comparison, and the Stacks Project's own text supplies current formal statements. The imported Hua finding was assessed only as supplied in RESULTS_STATE.md; its repository, Lean card, and external search status were not independently reviewed, so none is cited as proof or evidence of novelty.
