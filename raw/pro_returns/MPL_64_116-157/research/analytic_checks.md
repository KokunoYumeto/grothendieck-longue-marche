# Analytic and linear-algebra verification appendix

Author: GPT-6 Astra Pro, root research track; inherited effort, runtime effort value not exposed; 2026-11-17 UTC.

These are post-freeze mathematical checks, not additional readings of the ink. They do not alter an uncertain character or prove an arithmetic assertion by analogy with the complex calculation. The executable certificate is analytic_certificates.py, with exact output in analytic_certificate_output.json.

## AC01 — The two exact sequences on scan 119

Let \(X=\mathbb P^1_k\), \(L=\mathcal O_X(1)\), \(t\in X(k)\), \(V=H^0(X,L)\), and \(F=\ker(V\to L_t)\).
Evaluation gives
\[
0\longrightarrow F\longrightarrow V\longrightarrow L_t\longrightarrow0.
\]
The evaluation map \(F\otimes_k\mathcal O_X\to L\) has simple zero at \(t\), and identifies \(L\otimes F^\vee\) canonically with \(\mathcal O_X(t)\).
For a generator \(f\) of \(F\), the identification sends \(v\otimes f^\vee\) to \(v/f\); changing the generator changes its dual reciprocally.
Tensoring the evaluation sequence by \(F^\vee\) therefore gives
\[
0\longrightarrow k\longrightarrow H^0(X,\mathcal O_X(t))
\longrightarrow L_t\otimes F^\vee\longrightarrow0.
\]
The last term is \(T_{X,t}\): a principal part \(a/w\) in a local parameter corresponds to \(a\,\partial/\partial w\), and parameter changes transform these in the same way.
This proves the canonical comparison in scans 119(78)–(81), with the determinant/orientation twists retained in the manuscript's notation; it does not settle the separate square normalization on scan 121.

## AC02 — Proportionality on scans 123–126

For pairwise distinct \(\zeta_i\), set
\[
\ell=(\zeta_2-\zeta_3,\ \zeta_3-\zeta_1,\ \zeta_1-\zeta_2).
\]
Direct expansion gives
\[
\sum_i\ell_i=0,\qquad
\sum_i\zeta_i\ell_i=
\zeta_1\zeta_2-\zeta_1\zeta_3+
\zeta_2\zeta_3-\zeta_1\zeta_2+
\zeta_1\zeta_3-\zeta_2\zeta_3=0.
\]
The matrix with rows \((1,1,1)\) and \((\zeta_1,\zeta_2,\zeta_3)\) has rank two because \(\zeta_2-\zeta_1\ne0\), so its kernel is exactly \(k\ell\).
This proves scan 123's uniqueness up to invertible scalar, without fixing the quadratic scaling condition deferred on scan 121.

## AC03 — Orientation in the first construction

Use exactly the conventions of scans 131–137: \(z=x+iy\), \(y>0\), \(L_z=\mathbb C(z,1)\), and transport multiplication by \(-i\) through \(\varphi=\operatorname{Re}:L_z\to\mathbb R^2\).
For \(\lambda=a+ib\),
\[
\varphi(\lambda(z,1))=(ax-by,a),\qquad
J_z=
\begin{pmatrix}
-x/y&(x^2+y^2)/y\\
-1/y&x/y
\end{pmatrix}.
\]
The certificate checks \(J_z^2=-I\) and
\[
\det(e_1,J_ze_1)=-1/y<0.
\]
Thus the complex orientation is opposite to the ordered real basis for \(z\) in the upper half-plane, verifying the withdrawal in the margin of scan 135 and the discussion on scan 139.
This calculation does not resolve uncertain bars in scan 138 or the opening of scan 139.

## AC04 — Holomorphic families and the first theorem

The displayed family on scan 139 has period ratio \(w(z)=-\bar z\), with \(\operatorname{Im}w>0\).
The periods \(1,w(z)\) define a continuously framed family of complex tori, but
\[
\frac{\partial w}{\partial\bar z}=-1,\qquad
\frac{\partial w}{\partial z}=0.
\]
A holomorphic framed family would have holomorphic period ratio (Hain, 2021, Proposition 2.3, whose local proof was checked).
Consequently the formula cannot define the asserted holomorphic framed family on the displayed upper-half-plane base.
Scans 143–149 use the holomorphic period ratio \(\tau\) and are not affected by this objection.
Changing the base to its conjugate complex structure is a possible mathematical interpretation, not a correction to insert in the frozen transcription.

## AC05 — Actions, conventions, and the semidirect product

For \(g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbb Z)\), put
\[
g\tau=\frac{a\tau+b}{c\tau+d},\quad
j(g,\tau)=c\tau+d,\quad
T_g(\tau,z)=(g\tau,z/j(g,\tau)).
\]
Exact rational-function calculations verify
\[
g(h\tau)=(gh)\tau,\qquad
j(g,h\tau)j(h,\tau)=j(gh,\tau),
\]
and hence \(T_gT_h=T_{gh}\).
For \(T_v(\tau,z)=(\tau,z+m+n\tau)\), \(v=(m,n)^t\), define
\[
\rho(g)=\begin{pmatrix}a&-b\\-c&d\end{pmatrix}.
\]
If \((m',n')^t=\rho(g)v\), then
\[
(m'+n'g\tau)(c\tau+d)=m+n\tau,\qquad
T_gT_vT_g^{-1}=T_{\rho(g)v}.
\]
Thus \(T_{g,v}=T_vT_g\), matching scan 149(15), has product
\[
(g,v)(h,w)=(gh,v+\rho(g)w).
\]
The conjugated representation \(\rho(g)=\operatorname{diag}(1,-1)g\operatorname{diag}(1,-1)\) is forced by these translation coordinates; using \(g\) itself on translation columns requires a different convention.

The right/left conversion on scan 148 is
\[
\sigma(g)=\tau_\infty g^{-1}\tau_\infty
=\begin{pmatrix}d&b\\c&a\end{pmatrix},\qquad
\tau_\infty=\operatorname{diag}(-1,1),
\]
and satisfies \(\sigma(gh)=\sigma(h)\sigma(g)\).
The period action on scan 151 is the homomorphism
\[
R(g)=\begin{pmatrix}d&c\\b&a\end{pmatrix}
=P gP,\qquad P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The certificate checks both identities and distinguishes their order properties.

## AC06 — Explicit generators for the outer action requested on scan 140

Let \(F=\langle x,y\rangle\), \(c=[x,y]=xyx^{-1}y^{-1}\), and
\[
\widetilde S:x\mapsto y,\ y\mapsto x^{-1},\qquad
\widetilde T:x\mapsto x,\ y\mapsto xy.
\]
On the column basis \(([x],[y])\), their abelianization matrices are
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Exact free reduction proves
\[
\widetilde S(c)=x^{-1}cx,\quad
\widetilde T(c)=xcx^{-1},\quad
\widetilde S^4=1,\quad
(\widetilde S\widetilde T)^3
=\operatorname{Inn}(yx^{-1})\,\widetilde S^2.
\]
These outer classes satisfy
\(\mathrm{SL}_2(\mathbb Z)=\langle S,T\mid S^4=1,\ S^2=(ST)^3\rangle\), the standard presentation checked in Hain (2021, p.10).
They therefore define a homomorphism into peripheral-conjugacy-preserving outer automorphisms, whose composition with abelianization is the identity, proving its injectivity.
To identify its image with the full orientation-preserving outer automorphism group still uses \(\operatorname{Out}(F_2)\simeq\mathrm{GL}_2(\mathbb Z)\), carried from Bux et al. (2011, §1, author-PDF p.3); no independent proof of this full identification is claimed.
The chosen lifts preserve the conjugacy class of \(c\), not the based word \(c\), which explains the inner factor in the presentation relation.
These generators are normalized by their stated homology matrices; matching them to a particular deck-action convention requires the change of basis and left/right convention recorded in AC05.
This calculation does not establish a profinite GT or congruence-kernel assertion.

## AC07 — Rank and the meaning of universal cover

A once-punctured torus deformation-retracts onto a wedge of two circles, hence \(\Pi\simeq F_2\) and \(H=\Pi_{\mathrm{ab}}\simeq\mathbb Z^2\).
This directly refutes scan 140's rank-one parenthesis; scan 150's restatement is compatible with rank two.
The fiber inclusion in the torus family over the contractible upper half-plane gives \(\pi_1(\mathcal X_{\mathfrak H})\simeq\mathbb Z^2\), so the total space is not the simply connected covering object.
The precise mathematical interpretation of the universal-cover assertion in scans 139 and149 is the framed moduli base \(\mathfrak H\) mapping to the automorphism-retaining quotient \([\mathfrak H/\mathrm{SL}_2(\mathbb Z)]\); scan 149's literal wording predicates it of the displayed family, so this distinction is interpretive.
This agrees with the supplied cote 140-2, scans 259–263, on the modular topos, and Hain (2021, §3); it is not a free-covering assertion about the coarse quotient.

## AC08 — The cancelled free-action assertion on scan 152

Write \(v=(z_1,z_2)\), where its entries are a positively oriented real basis of \(\mathbb C\).
If \(R(g)v=v\), real linear independence gives \(g=I\); if \(v/\lambda=v\), nonvanishing gives \(\lambda=1\).
The separate group actions are therefore free.
Their product contains \((\lambda,g)=(-1,-I)\), which fixes the period vector and sends the fiber coordinate to \(-z\), with fixed locus
\[
E[2]=\tfrac12(\mathbb Zz_1+\mathbb Zz_2)/(\mathbb Zz_1+\mathbb Zz_2).
\]
These are four points, three nonzero, so removing only the zero section does not make the action free.
This verifies the author's marginal counterexample and the cancellation, without deciding any additional intended meaning of the exclamation-mark exponent.

## Sources used in this appendix

Bux, K.-U., Ershov, M. V., & Rapinchuk, A. S. (2011). The congruence subgroup property for Aut \(F_2\): A group-theoretic proof of Asada's theorem. *Groups, Geometry, and Dynamics, 5*(2), 327–353. https://doi.org/10.4171/GGD/130

Hain, R. (2021, November 13). *Lectures on moduli spaces of elliptic curves* [Revised author manuscript]. https://sites.math.duke.edu/~hain/teaching/mth790/hain_final_rev_2021.pdf

The sources establish the expressly identified background facts; AC01–AC03, AC05, AC06's free-word identities, and AC08 are independent calculations supplied here.

