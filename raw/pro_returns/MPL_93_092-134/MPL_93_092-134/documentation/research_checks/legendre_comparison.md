# A concrete S20 comparison: Legendre periods and the three-punctured line

Run: MPL_93_092-134/integral_schwarzian_check. Model: GPT-6 Astra Pro (inherited); effort setting not exposed. This is additional post-freeze research. No manuscript image or OCR was used and no frozen transcription was changed. The root's proposed three-cusp coefficient is the comparison input; the calculations below independently check its equality with a geometric Picard–Fuchs projective connection.

## Result

For the Legendre family

\[
E_z:\quad y^2=x(x-1)(x-z),\qquad z\in\mathbf P^1(\mathbf C)\setminus\{0,1,\infty\},
\]

the periods of \(\omega=dx/y\) over locally transported closed cycles satisfy

\[
L\Pi:=z(1-z)\Pi''+(1-2z)\Pi'-\tfrac14\Pi=0.
\]

Writing this as \(\Pi''+P\Pi'+Q\Pi=0\) gives

\[
P=\frac{1-2z}{z(1-z)},\qquad Q=-\frac1{4z(1-z)},\qquad
\mu=2P'+P^2-4Q=-\frac{z^2-z+1}{z^2(z-1)^2}.
\]

Thus its projective coefficient in the manuscript's \(G=-2S\) normalization is exactly the coefficient determined by the root's three-cusp calculation. This supplies one explicit geometric comparison for S20. It does not assert that the manuscript identifies this family, that every uniformizing connection arises in this way, or that an uncomputed p-curvature vanishes. The earlier P05 calculation was not repeated.

## Exact relative differential certificate

Put \(f=x(x-1)(x-z)\), \(g=x(x-1)\), and \(h=x-z\). Holding \(x\) fixed while differentiating the relation \(y^2=f\) with respect to \(z\) yields

\[
\partial_z\omega=\frac{1}{2h}\omega,\qquad
\partial_z^2\omega=\frac{3}{4h^2}\omega.
\]

Consequently

\[
L\omega=
\left(\frac{3z(1-z)}{4h^2}+\frac{1-2z}{2h}-\frac14\right)\omega
=\frac{-x^2+2x-2xz+z}{4(x-z)^2}\omega.
\]

The following identity is exact on the curve's rational function field:

\[
\boxed{\quad L\omega=d_x\left(\frac{y}{2(x-z)^2}\right)
=d_x\left(\frac{x(x-1)}{2(x-z)y}\right).\quad}
\]

Indeed, writing \(R=g/(2h)\), the coefficient of \(\omega\) in \(d_x(R/y)\) is

\[
R_x-\frac{R f_x}{2f}
=\frac{g'h-3g}{4h^2}
=\frac{-x^2+2x-2xz+z}{4h^2}.
\]

This proves the asserted Picard–Fuchs equation for periods: locally in parameter space, represent a transported cycle by contours avoiding the branch points, differentiate under the integral, and integrate the exact rational differential to zero. Equivalently, the displayed identity is the corresponding relation for the Gauss–Manin derivatives of the de Rham class of \(\omega\); the rational primitive and its derivative may have poles, which do not affect the closed-cycle calculation. The identity itself is defined over \(\mathbf Q(z)\); the period interpretation here is in characteristic zero.

## Projective normalization

Locally set \(u=\exp(\tfrac12\int P\,dz)\Pi=\sqrt{z(1-z)}\,\Pi\). Then

\[
u''=\left(\tfrac12P'+\tfrac14P^2-Q\right)u=\frac\mu4u.
\]

The scalar gauge does not change the ratio \(\tau=\Pi_1/\Pi_2=u_1/u_2\) of two independent solutions. The usual solution-ratio identity gives \(S_z(\tau)=-\mu/2\), hence \(G(z,\tau)=-2S_z(\tau)=\mu\). The companion script verifies the exact rational simplification of \(\mu\) and the relative differential identity above, rather than relying on numerical agreement.

## Primary source checked

J. Harnad, *Picard–Fuchs Equations, Hauptmoduls and Integrable Systems*, arXiv:solv-int/9902013 (1999), [author preprint](https://arxiv.org/pdf/solv-int/9902013), §1, equations (1.9)–(1.12), printed pages 2–3, states the period equation and inverse Schwarzian equation. Equations (1.18)–(1.19), page 4, use \(y^2=4x(x-1)(x-\lambda)\); rescaling \(y\) by the constant 2 does not change the differential equation. These locations corroborate the comparison independently certified above. The remaining paper is not being certified.

Retrieval reference: `turn525768337view0`, lines 93–170 and 291–305. Root must open the source itself before using that citation reference in its answer. An attempted opening of a different research PDF at pure.mpg.de returned HTTP 403; nothing from that inaccessible full text is used.

## Context relation

| Context location | Relation of this check |
|---|---|
| `context/README.md`, lines 18–22, S20 | Adds a specified geometric example comparing a Gauss–Manin period equation with the uniformizing projective coefficient. The catalogue-level general hypothesis remains broader than this example. |
| `context/same_cote_93/MPL_93_002-046_notes.md`, P08, lines 499–505 | Adds an actual family, differential, exact differential certificate, and normalized coefficient to the previous comparison leads. No claim that P08 had already established this equality. |
| Same file, P09, lines 507–513 | Meets its requested normalization/comparison test in this one example; does not supply the absent cotes 159 and 64 or identify their constructions. |
| Michel Hua, modernised reading of cote 93, X “Régularité à l'infini”, lines 1657–1700 | Adds a concrete coefficient to the fixed-leading-term interpretation at lines 1662–1668. The general statements about genus-zero regular connections at lines 1692–1694 require the qualifications already discussed by root; the present example has nonzero coefficient in the z-coordinate. |
| `context/notes/RESULTS_STATE.md`, opening relevance instructions and P08/P09 entries at lines 378 and nearby | Uses the earlier entries as leads and records this explicit comparison as a this-run proof, not an inherited settled result. |

## Suggested compact note (root assigns final id)

**A geometric example realizes the three-cusp connection.** **Kind:** own idea; **confidence:** high for the exact comparison, without an attribution of this identification to the manuscript. For \(E_z:y^2=x(x-1)(x-z)\), the identity \([z(1-z)\partial_z^2+(1-2z)\partial_z-1/4](dx/y)=d_x[y/(2(x-z)^2)]\) proves the period equation, and normalization gives \(\mu=2P'+P^2-4Q=-(z^2-z+1)/(z^2(z-1)^2)\). This agrees with the three-cusp coefficient and gives a concrete S20 comparison beyond MPL_93_002-046 P08/P09; Harnad §1 (1.9)–(1.12) independently states the period/Schwarzian relation. The example neither identifies the manuscript's intended family nor proves a general geometric-realization or p-curvature claim.
