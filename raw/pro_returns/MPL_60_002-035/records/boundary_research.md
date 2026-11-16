# Boundary duality, determinants, and curve extension: post-freeze research memo

**Scope and provenance.** Research performed after the transcription freeze at 2026-11-16 00:17:03 UTC. Inputs were the frozen TEX for scans 007, 009, 011, 013, 015, 017, 019, 021, 023, 025, 027, 029, 031, 033, 035 and the supplied context README, transcription, notes, and RESULTS_STATE. No manuscript image or crop was inspected; no frozen page or combined fragment was changed. Quotations below reproduce the frozen transcription, including its uncertainty where relevant. The computations are modern checks, not proposed replacements of manuscript readings.

## Conventions and primary anchors

Throughout, the base is \(\mathbf F_p\), \(\ell\ne p\), and \(F\) is geometric Frobenius, acting on \(\mathbf Q_\ell(1)\) by \(p^{-1}\). For a bounded finite-dimensional Frobenius complex \(V\), use

\[
\chi(V)=\sum_i(-1)^i\dim H^i(V),\qquad
\delta(V)=\prod_i\det(F\mid H^i(V))^{(-1)^i},\qquad
L_V(t)=\prod_i\det(1-tF\mid H^i(V))^{(-1)^{i+1}}.
\]

Deligne (1973), §§10.3–10.8, treats determinant identities, global duality and the curve-local calculation; Deligne (1974), §§2.8–2.12, gives the compact/ordinary pairing and the pairing for underived \(j_*\) on curves explicitly. Deligne (1980), §§1.2.1–1.2.5, defines purity, and Theorem 3.4.1(iii)/3.4.9 gives **geometric** semisimplicity of pure lisse sheaves. These statements have distinct hypotheses; purity, rationality, self-duality and polarization must not be silently identified.

## BR01 — Reciprocal determinant: a rank-one test resolves the sign algebraically

**Witness:** scan007: the uncertain argument \(P_f(\unsure{-t^{-1}|t^{-1}})\), followed by the boxed \(P_{\check f}(t)=(-t)^{\varepsilon(f)}\det(f)^{-1}P_f(t^{-1})\).

**Finding (own verification).** For \(f=a\) on a line, the boxed formula gives \(1-t/a\), as required; the alternative argument \(-t^{-1}\) gives \(-1-t/a\). For dimension \(r\), factor each \(1-\alpha^{-1}t=(-\alpha^{-1}t)(1-\alpha/t)\). Multiplying and then applying alternating products proves

\[
L_{DV}(t)=(-t)^{-\chi(V)}\delta(V)L_V(t^{-1}).
\]

This confirms the later box without resolving the earlier handwriting alternative. The rational-function restriction in scan007 is essential: substitution \(t\mapsto t^{-1}\) is not an operation on an arbitrary formal series at zero. **Primary locator:** Deligne (1973), §10.3.4–10.3.5, pp. 582–583.

## BR02 — Boundary duality has shift \([-1]\) for the cone actually used

**Witness:** scan025: “à vérifier si c'est \(1\) ou \(-1\) !” beside the displayed \([1]\).

**Finding (own derivation).** Specify

\[
A(E)=Rf_!E,\quad B(E)=Rf_*E,\quad C(E)=\operatorname{Cone}(A(E)\longrightarrow B(E)),
\]

so the triangle is \(A(E)\to B(E)\to C(E)\to A(E)[1]\). Verdier duality gives \(DA(E)=B(DE)\), \(DB(E)=A(DE)\). The dual triangle is

\[
DC(E)\longrightarrow A(DE)\longrightarrow B(DE)\longrightarrow DC(E)[1],
\]

and hence

\[
\boxed{DC(E)\simeq C(DE)[-1].}
\]

For an open compactification \(i:U\hookrightarrow\bar X\), closed complement \(j:Z\hookrightarrow\bar X\), the equivalent local statement is \(Rj^!i_!DE\simeq j^*Ri_*DE[-1]\). This follows by applying the two localization triangles to \(i_!DE\). A derived enhancement supplies a functorial cone; the bare triangulated statement is an isomorphism compatible with these triangles.

If \(U\) is smooth of pure dimension \(n\) and \(E^\vee\simeq E(\rho)\), the full derived expression is

\[
DC(E)\simeq C(E)(n+\rho)[2n-1].
\]

The omitted even shift \([2n]\) matters in the derived category, although it disappears from \(K_0\) and from \(L\). Both candidate shifts \([1]\) and \([-1]\) induce the same sign in \(K_0\), so the later determinant identities cannot decide between them. **Primary anchor:** Deligne (1973), §§10.5–10.7, pp. 583–586; the cohomological cone convention is explicit in Stacks Project, Definition 13.9.1, tag 014D.

**Degree test.** For \(U=\mathbf A^1\), \(E=\mathbf Q_\ell\), \(C\) has \(H^0=\mathbf Q_\ell\), \(H^1=\mathbf Q_\ell(-1)\). Its dual lies in degrees \(-1,0\), exactly as \(C(E)(1)[1]\), and not in degrees \(-3,-2\) as the alternative \(C(DE)[1]\) would require.

## BR03 — The compact/ordinary normalized determinants are reciprocals

**Witness:** scan027: \(\delta\delta'=q^{\chi(E)}\), followed by the box \(\varepsilon=\delta q^{-\chi/2}=\delta' q^{-\chi/2}\).

**Finding (own derivation).** Assume smooth pure dimension \(n\), lisse \(E\), and an isomorphism \(E^\vee\simeq E(\rho)\). Put \(q=p^{n+\rho}\), \(\delta_c=\delta(Rf_!E)\), \(\delta_*=\delta(Rf_*E)\). Duality and the even shift give

\[
\chi_c=\chi_*=: \chi,\qquad
\delta_c\delta_*=q^\chi.
\]

Consequently, if \(\varepsilon=\delta_cq^{-\chi/2}\), then

\[
\boxed{\delta_*q^{-\chi/2}=\varepsilon^{-1}},\qquad
\delta_\infty=\delta_*/\delta_c=q^\chi\delta_c^{-2}=\varepsilon^{-2}.
\]

The second equality in the manuscript's normalized-determinant box is therefore not valid generally. It holds when \(\varepsilon^2=1\), in particular in the proper case, where \(Rf_!=Rf_*\). This is a mathematical inconsistency between displayed formulas, not a license to edit the frozen text. No Weil bounds or resolution of singularities are needed for this formal consequence of the stated self-duality.

## BR04 — Complete affine-line and multiplicative-group checks

**Witness:** scans021, 025, 027, 029: the boundary factor \(A(t)\), \(\delta_\infty=\varepsilon^{-2}\), and the involution \(t\mapsto1/(qt)\).

**Finding (own computations).** With constant coefficients, \(n=1,\rho=0,q=p\):

| Object | \(\chi\) | \(\delta_c\) | \(\delta_*\) | \(\varepsilon\) | \(\delta_\infty\) | \(L_c(t)\) | \(L^\infty(t)\) |
|---|---:|---:|---:|---:|---:|---|---|
| \(\mathbf A^1\) | 1 | \(p\) | 1 | \(\sqrt p\) | \(p^{-1}\) | \((1-pt)^{-1}\) | \((1-pt)/(1-t)\) |
| \(\mathbf G_m\) | 0 | \(p\) | \(p^{-1}\) | \(p\) | \(p^{-2}\) | \((1-t)/(1-pt)\) | \(((1-pt)/(1-t))^2\) |

For \(\mathbf A^1\), \(H_c^2=\mathbf Q_\ell(-1)\), \(H^0=\mathbf Q_\ell\); for \(\mathbf G_m\), \(H_c^1=\mathbf Q_\ell\), \(H_c^2=\mathbf Q_\ell(-1)\), \(H^0=\mathbf Q_\ell\), \(H^1=\mathbf Q_\ell(-1)\). Thus these calculations check the determinant and boundary identities directly.

For the affine line,

\[
A(t)=L^\infty(1/(pt))^{-1}=\frac{1-pt}{p(1-t)},\qquad
L_c(1/(pt))=A(t)p(-t)L_c(t)=-\frac{t}{1-t}.
\]

Both examples satisfy \(L^\infty(t)L^\infty(1/(pt))\delta_\infty=1\). The affine line falsifies the equality of the two normalized determinants in BR03, while \(\mathbf G_m\) makes especially transparent that nonproper \(\varepsilon\) need not be a sign. These examples do not contradict the manuscript's explicit restriction “\(=\pm1\) si \(X\) … propre.”

## BR05 — The middle-degree eigenvalue must be normalized

**Witness:** scan017: “multiplicité … de la valeur propre \(1\) (\(-1\)) de \(f\) sur \(H^n\),” leading to \(\varepsilon'=(-1)^{e_1}\).

**Finding (own countertest and repair at the level of interpretation).** Let \(X=\mathbf P^2\), \(E=\mathbf Q_\ell\). Then \(n=2,\rho=0,\chi=3,\delta=p^3,q=p^2\), so \(\varepsilon=1\) and \(\varepsilon'=-1\). Frobenius on \(H^2\) is \(p\); the multiplicity of its **raw** eigenvalue 1 is zero. The literal raw-eigenvalue formula would incorrectly give \(+1\).

Instead set \(F_0=p^{-(n+\rho)/2}F\). In the orthogonal case its spectrum is stable under \(\lambda\mapsto\lambda^{-1}\); if \(e_{\pm1}\) denote algebraic multiplicities for \(F_0\), then \(b_n\equiv e_1+e_{-1}\pmod2\), \(\det F_0=(-1)^{e_{-1}}\), and \(\varepsilon'=(-1)^{e_1}\). For \(\mathbf P^2\), \(F_0=1\) on \(H^2\), giving the required \(-1\). The manuscript's insertion of “multiplicité” should be respected: generalized multiplicity is the relevant notion, without assuming Frobenius semisimple. **Primary comparison:** Deligne (1974), §2.6, p. 282, gives the standard middle-cohomology sign formula with the central Frobenius eigenvalue.

## BR06 — Half-powers and parity of poles

**Witness:** scans015, 029, 031, 035: \(\xi(t)=t^{\chi/2}L(t)\).

**Finding (own clarification).** If \(\chi\) is odd, this is naturally a function of \(u=t^{1/2}\), with involution \(u\mapsto q^{-1/2}u^{-1}\), after choosing the required square roots; it need not be rational in \(t\). The formal calculation nevertheless gives \(\xi(1/(qt))=(-1)^\chi\varepsilon A(t)\xi(t)\).

In the proper case, at the fixed point \(t=q^{-1/2}\), \(\varepsilon'=-1\) forces **odd order**, which may be a zero or a pole. For \(\mathbf P^2\), \(L(t)=((1-t)(1-pt)(1-p^2t))^{-1}\) has a simple pole at \(1/p\). Thus a central-zero statement would require a holomorphy hypothesis not present in these formulas.

## BR07 — Purity does not supply all the motivic sign hypotheses

**Witness:** scan009: “\(\rho\) impair \(\Longrightarrow n\) pair”; scan017: odd middle weight gives an alternating form and \(\varepsilon'=1\); scan023: odd \(i\) gives \(\varepsilon_i=+1\). The adjacent text expressly invokes a motif, Lefschetz, and/or standard conjectures.

**Finding (own scope counterexamples).** The following are continuous representations of \(\operatorname{Gal}(\overline{\mathbf F}_p/\mathbf F_p)\); matrices in \(\mathrm{GL}_r(\mathbf Z_\ell)\) define such representations by their compact procyclic closures.

1. A rank-one \(\mathbf Q_7\)-character with Frobenius a primitive cube root \(\zeta_3\in\mathbf Q_7\) is pure of weight 0, but has determinant \(\zeta_3\notin\{\pm1\}\) and is not self-dual. Purity alone does not imply either determinant sign or \(E^\vee\simeq E(\rho)\).
2. Over \(\mathbf F_2\), Frobenius \(\sqrt2\in\mathbf Q_7\) defines a pure weight-1 rank-one sheaf: both complex conjugates have absolute value \(\sqrt2\). Thus odd weight does not force even rank without further hypotheses. Its characteristic polynomial is not rational, although its eigenvalue is algebraic; \(2\) is a square modulo 7, so the indicated \(7\)-adic square root exists.
3. Even rational characteristic polynomial and self-duality do not force the odd-weight positive sign. On a point over \(\mathbf F_p\), take

\[
F=\begin{pmatrix}0&p\\1&0\end{pmatrix},\qquad
B=\operatorname{diag}(1,p).
\]

Then \(F^tBF=pB\), so \(E^\vee\simeq E(1)\), while \(\det(x-F)=x^2-p\), \(\det F=-p\). It is pure weight 1 of rank 2 with \(\varepsilon'=\varepsilon=-1\). Its self-duality is symmetric; an alternating pairing of the prescribed parity is the missing hypothesis.

These examples delimit extrapolation from the manuscript's motivic setting to arbitrary lisse sheaves; they are not counterexamples to a polarized motivic assertion. **Primary definitions:** Deligne (1980), §§1.2.1–1.2.5, pp. 153–155. The symplectic determinant assertion itself is elementary linear algebra once the alternating form is given.

## BR08 — Underived \(i_*\) on curves: duality is sound, with an even shift

**Witness:** scan033: \(D(E)=i_*(\check E_y)(1)\), and \(L^*_{\check E_y}(1/(pt))=(-t)^{\chi^*(\check E_y)}\delta^*(E_y)L^*_{E_y}(t)\).

**Finding.** Assume the generic representation extends to a lisse sheaf \(L\) on a nonempty open \(j:U\hookrightarrow X\), where \(X\) is a smooth projective curve. Its underived extension has stalk \((j_*L)_{\bar x}=L_{\bar\eta}^{I_x}\). The derived duality statement is

\[
D_X(j_*L)\simeq j_*L^\vee(1)[2].
\]

Equivalently \(j_*L[1]\) is the perverse middle extension and is stable under duality in that normalization. Deligne (1974), §§2.11–2.12, pp. 282–283, explicitly gives the resulting perfect cohomological pairing; §2.14(E) traces it to SGA 4, XVIII (3.2.5). Deligne (1973), §10.8, p. 587, is the direct local antecedent. The omitted \([2]\) in scan033 is significant at derived level but harmless in \(K_0\), determinants and \(L\).

**Exponent check (own derivation).** Put \(M=j_*L\). From BR01,

\[
L_{D M}(t)=(-t)^{-\chi(M)}\delta(M)L_M(t^{-1}).
\]

Since \(L_{D M}(t)=L_{j_*L^\vee}(t/p)\), substitution \(t\mapsto t^{-1}\) gives

\[
L_{j_*L^\vee}(1/(pt))=(-t)^{\chi(M)}\delta(M)L_M(t).
\]

Duality gives \(\chi(j_*L^\vee)=\chi(M)\). Thus the **positive** exponent in scan033 is correct. A finite ramification/spreading-out hypothesis is appropriate when starting with an arbitrary generic \(\ell\)-adic representation; it should not be replaced by an unexamined assertion that every such representation has the needed constructible extension.

## BR09 — Exact sequence correction: support need not ramify in the quotient

**Witness:** scan035: “ce n'est pas additif”; \(Q\) “est concentré … [en] … pts de ‘ramification’ de \(E''_y\)”; \(L^*_{E_y}=L^*_{E'_y}L^*_{E''_y}L_Q^{-1}\).

**Finding (explicit local counterexample).** At a degree-one point, choose a tame \(\ell\)-adic inertia coordinate \(u\in\mathbf Z_\ell\), put

\[
N e_2=e_1,\quad N e_1=0,\qquad
T(u)=1+uN,\qquad F=\operatorname{diag}(1,p).
\]

These satisfy the geometric-Frobenius relation \(F T(u)F^{-1}=T(u/p)\). Hence they define a continuous tame local representation with exact sequence

\[
0\longrightarrow\mathbf Q_\ell\,e_1\longrightarrow V
\longrightarrow\mathbf Q_\ell(-1)\longrightarrow0.
\]

Both end terms are unramified. Yet \(V^I=\mathbf Q_\ell e_1\) maps to zero in \((V'')^I=\mathbf Q_\ell(-1)\), and

\[
Q=\operatorname{coker}(V^I\longrightarrow(V'')^I)
=\mathbf Q_\ell(-1)\ne0.
\]

Thus the stated restriction to ramification of the **quotient** is false in this generality. The exact description is the locus where taking inertia invariants fails to be surjective; it is contained in the ramification locus of the middle representation. The kernel expression struck out in scan035 is what the long exact sequence supplies: \(Q_x=\ker(H^1(I_x,V')\to H^1(I_x,V))\).

The correction's direction is right: \([j_*V]=[j_*V']+[j_*V'']-[Q]\), so

\[
L(j_*V)=L(j_*V')L(j_*V'')\prod_x\det(1-F_x t^{\deg x}\mid Q_x).
\]

The local factor in this example is \(1-pt\). At a closed point of degree \(d\), the exponent is \(t^d\), unless the notation \(P_{Q_x}(t)\) already incorporates induction to the base field. **Primary structural anchor:** Deligne (1973), §§10.7–10.8, pp. 584–587, on the local inertia calculation. The representation and all counterexample calculations here are independent constructions.

## BR10 — Global realization and the precise purity exception

**Witness:** the same scan035 multiplicativity claim.

**Finding (own example).** The preceding representation extends over \(\mathbf G_m/\mathbf F_p\), using its tame fundamental group, and is the appropriate Tate twist of the Kummer extension of the coordinate. Compactify by \(j:\mathbf G_m\hookrightarrow\mathbf P^1\). At both 0 and \(\infty\), the quotient remains unramified, the middle representation has nonzero unipotent monodromy, and \(Q_x=\mathbf Q_\ell(-1)\). Interior Frobenius eigenvalues at a degree-\(d\) point are \(1,p^d\), independently of the extension class. Therefore

\[
\begin{aligned}
L_{\mathbf P^1}(j_*V,t)&=\frac1{(1-t)(1-p^2t)},\\
L_{\mathbf P^1}(j_*V',t)&=\frac1{(1-t)(1-pt)},\\
L_{\mathbf P^1}(j_*V'',t)&=\frac1{(1-pt)(1-p^2t)},
\end{aligned}
\]

and the missing factor is precisely \((1-pt)^2\).

This extension is mixed, with weights 0 and 2. If the original sequence splits on the geometric fundamental group, its inertia invariants are exact; finite inertia image in characteristic zero also gives exactness by averaging. In particular a pure lisse middle object on a normal finite-field variety is geometrically semisimple by Deligne (1980), Theorem 3.4.1(iii)/3.4.9, p. 209, and the displayed mixed counterexample is excluded. This says neither that all mixed sequences split nor that every pure sheaf is arithmetically semisimple.

## BR11 — Tate target wording and a historical terminology check

**Witness:** scan015 says the two cohomology groups are “duaux à valeurs dans \(\mathbb Q_\ell(n)\)”; scans011, 017, 019 use uncertain “c\(^{\mathrm t}\)/ct tordu.”

**Finding.** With the Tate convention above, the unshifted Poincaré pairing takes values in \(\mathbf Q_\ell(-n)\), or in \(\mathbf Q_\ell\) after twisting the second factor by \((n)\); the displayed \(+n\) target is not consistent with the other conventions. Its positivity-based determinant-sign conclusion is unaffected by this sign in the target twist. Deligne (1974), Theorem 2.8, p. 282, supplies the normalized trace pairing. Separately, Deligne (1980), introduction, p. 138, explicitly uses “lisse (= constant tordu, dans une autre terminologie)”: this is useful historical terminology evidence in research notes, not permission to settle frozen abbreviations from context.

## Context comparison and limits

The supplied README calls its own material first-pass claims and identifies Book II, II.8, rank 13. These scans strongly confirm the L-function/functional-equation theme; the reviewed portion contains no construction of a height or local-symbol pairing. The relevant supplied-context anchors are **C16/14** (alternating form), **C16/18** and **C16/23** (duality programmes), **C16/25** (forms), **C16/48–50** (duality, omitted twist, conditional semisimplicity and Weil strategy), and **C44/2, C44/8–9** (dual abelian varieties and polarization). These are analogies and leads; none supplies the missing boundary-cone or inertia proof.

In RESULTS_STATE, **WG2 §2.4 #3**, **WG2 §2.3 #7**, **WG2 §2.2 #4**, and **WG2 §6. #9** are unchecked planning items. **MPL_14_087-132 M09** concerns numerical versus conditional cohomological semisimplicity; **MPL_14_002-044 M29a** is a first-pass mixed-extension scope test. BR07 and BR10 add independent local-system tests to that distinction. **MPL_15_195-228+18_002-017 M03/P09** concern grading and Tate conventions; BR02/BR11 add separate degree/twist checks. **MPL_14_002-044 A36** is an autoduality lead. **WG H9** and **WG2 §2.3 #12** concern height/polarization expectations but are not proved by these L-function pages. **LM7 E.23** and the reviewed **LM7_PUSH D.44** address other arithmetic problems and have no demonstrated implication here.

Targeted searches used `Frobenius|Weil|alternée|polar|poids|fonction L|semi-simple|dualité` in the supplied context, with scan-local inspection of matches. The boundary weight/type bound in scan021 was not independently established in this memo; its “type” terminology should not be identified with a modern invariant without further evidence. The local-global epsilon-factor product formula is also not proved by the computations here.

## References and retrieval record

Deligne, P. (1973). Les constantes des équations fonctionnelles des fonctions L. In P. Deligne & W. Kuijk (Eds.), *Modular functions of one variable II* (Lecture Notes in Mathematics, Vol. 349, pp. 501–597). Springer. https://doi.org/10.1007/BFb0066719 . Author-hosted primary PDF: https://publications.ias.edu/sites/default/files/Number20.pdf . Publisher metadata: https://link.springer.com/book/10.1007/978-3-540-37855-6 . **Locators:** §§10.3.4–10.3.5 (determinants); §10.4 (Euler product); §10.5 (duality/functional equation); §§10.6–10.8 (local calculation and underived extension). The PDF text extraction omits some displayed formulas, especially §10.8; the underived curve pairing was therefore separately checked against Deligne (1974), §2.12.

Deligne, P. (1974). La conjecture de Weil. I. *Publications Mathématiques de l’IHÉS, 43*, 273–307. https://doi.org/10.1007/BF02684373 . Primary PDF: https://publications.ias.edu/sites/default/files/Number23.pdf . Canonical journal metadata: https://www.numdam.org/item/PMIHES_1974__43__273_0/ . **Locators:** §1.5.4 (cohomological determinant expression), §2.6 (sign), Theorem 2.8 and §§2.9–2.10 (Poincaré duality/curves), §§2.11–2.12 (underived \(j_*\) pairing), §2.14(E) (SGA 4 XVIII 3.2.5 attribution). The author's publication list gives 273–308; the journal record and 35-page PDF end at 307, followed here.

Deligne, P. (1980). La conjecture de Weil. II. *Publications Mathématiques de l’IHÉS, 52*, 137–252. https://doi.org/10.1007/BF02684780 . Primary PDF: https://publications.ias.edu/sites/default/files/Number40.pdf . Canonical journal metadata: https://www.numdam.org/item/PMIHES_1980__52__137_0/ . **Locators:** introduction p. 138 (terminology); §§1.2.1–1.2.5 (purity); §3.3 (weights); Theorem 3.4.1(iii)/3.4.9 p. 209 (geometric semisimplicity). The canonical volume is 52; an IAS metadata page incorrectly lists 42.

The Stacks Project Authors. (n.d.). *Cones and termwise split sequences* (§13.9, Definition 13.9.1; tag 014D). Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/014D . Used only to pin down the cohomological cone convention, with the dual-cone computation supplied explicitly above.

Milne, J. S. (2013). *Lectures on étale cohomology* (Version 2.21). https://www.jmilne.org/math/CourseNotes/LEC.pdf . **Backup locator:** Theorem 24.1, p. 144 (smooth Poincaré duality). Author's notes were consulted, but the direct primary Deligne references above suffice for the main conclusions.

**Web retrieval handles for parent verification:** Deligne 1973 PDF `turn2view1`/`turn9view1`; Deligne 1974 primary §2 `turn19view0`–`turn19view2`, metadata `turn22view1`; Deligne 1980 PDF `turn9view0`, purity `turn12view1`, semisimplicity `turn11view1`; Stacks `turn22view0`; publisher bibliographic metadata `turn23search0`. These handles are retrieval aids, not standalone citations. All source quotations are short; substantive counterexamples and computations are independent analyses.
