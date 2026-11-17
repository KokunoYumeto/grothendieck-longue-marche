# Final mathematical review: N30–N43

Read-only review of the main notes and frozen transcription; no image inspected and no main-notes or transcription file changed. Checked against the supplied Oda PDF's extracted printed text, including Definitions 3.5 (p. 82), 5.5–5.8 (pp. 121–124), the normal-case statements (pp. 125–126), and Corollaries 5.11–5.12 (p. 131).

## Necessary precision corrections

1. **N30: specify the site.** Write “global sections of the **Zariski quotient sheaf** \(\mathcal O_X^*/\mathcal O_X^{*p}\)” (the étale quotient also works on this reduced X). On the fppf site the p-th-power map on \(\mathbf G_m\) is locally surjective and has kernel \(\mu_p\), so this quotient and the displayed short exact sequence would not have the intended meaning. This qualification can be added in the existing second sentence without changing the argument.

2. **N40: retain the exact field and variety hypotheses.** Add “for an abelian variety A over a perfect field of characteristic p” to the statement of Oda's Corollary 5.11. The comparison is \(M(A[p])\simeq H^1_{\mathrm{dR}}(A)\) in Oda's contravariant convention; its Hodge identification \(\ker F=\operatorname{im}V\) is correct. No dual should be inserted into this corollary's formula.

3. **N41: restore the perfect-field hypothesis and specify the operator convention.** Its second sentence should say “For smooth proper X **over a perfect field k of characteristic p**, with a k-point...”. Retain the dual Dieudonné module, ideally written explicitly as \(D M(\operatorname{Pic}_{X/k}[p])\): Oda's \(D\), Definition 3.5, p. 82, is the module duality \(\operatorname{Hom}_{W(k)}(-,C(k))\), with \((F\alpha)(m)=\sigma(\alpha(Vm))\) and \((V\alpha)(m)=\sigma^{-1}(\alpha(Fm))\); silently replacing \(DM\) by \(M\) would change conventions. The image formula should be described as the classes “whose successive Cartier iterates remain closed, written \(\bigcap_{n\ge1}\ker(d\circ V^n)\) in Oda's iteratively defined sense”: on general X, \(V:H^1_{\mathrm{dR}}(X)\to H^0(X,\Omega^1)\) need not land in closed forms, so \(V^{n+1}\) is defined only after imposing the preceding closedness conditions (Definitions 5.6–5.8, pp. 122–124), rather than being an endomorphism of all \(H^1_{\mathrm{dR}}(X)\).

The Oda bibliography can consequently add Definition 3.5, p. 82, and Definitions 5.6–5.8, pp. 122–124, to its checked locators. No corrections are needed to the cited Cartier/SGA3 bibliography or to the related standing-question/status rows.

## Explicit check requested by the parent: N34 is valid over a perfect nonclosed field

No algebraic-closedness or k-point hypothesis is required for N34. On the Zariski site of a smooth X over a perfect field k of characteristic p, Oda's local p-base logarithmic criterion gives

\[
1\longrightarrow\mathcal O_X^*\xrightarrow{u\mapsto u^p}\mathcal O_X^*
\xrightarrow{d\log}\ker(C-1:Z\Omega^1_{X/k}\to\Omega^1_{X/k})\longrightarrow0.
\]

For proper X the ring \(A=H^0(X,\mathcal O_X)\) is a finite reduced k-algebra, hence a product of finite extensions of the perfect field k and therefore perfect. The associated cohomology sequence is

\[
0\longrightarrow A^*/A^{*p}\longrightarrow
H^0\bigl(X,\ker(C-1)\bigr)\longrightarrow\operatorname{Pic}(X)[p]
\longrightarrow0,
\]

and \(A^*/A^{*p}=0\). This proves precisely the asserted additive-group identification; the fixed group is naturally an \(\mathbf F_p\)-vector space, generally not a k-vector space, so N34's wording “additive group” is appropriate. Cartier is understood in Oda's absolute/\(\sigma^{-1}\)-semilinear convention after identifying the relevant Frobenius twist over perfect k.

## Other checked claims

N31–N33 keep the normal/smooth boundary correctly; N32's omitted p-th-power quotient is detected by the stated regular local example. N35–N36 correctly distinguish the derivation p-power from a degree-p homogeneous polynomial operation under variable coefficients. N37–N39 maintain the needed finite locally free/flat restrictions; N38's commutativity deduction is valid within that dictionary. N42 remains explicitly a proposed diagnostic, and N43 makes no dating claim from the printed source.
