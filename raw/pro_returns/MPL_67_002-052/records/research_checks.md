# Post-freeze research checks

These calculations concern the research notes. They do not alter any transcription reading. The root completed the symbolic and rational checks in `check_calculations.py` at 2026-11-18 00:54:44 UTC; `calculation_results.json` records the actual output. The explanatory arguments below were checked after that calculation. A finite matrix check certifies the displayed identities, with no claim to certify a presentation or an entire results register.

## C01 — an explicit assignment for the reflections on scan 050

Put

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
R=\begin{pmatrix}0&-1\\1&1\end{pmatrix},\qquad
r_1=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad
r_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
r_3=\begin{pmatrix}1&1\\0&-1\end{pmatrix}.
\]

Direct multiplication gives \(r_i^2=I\), \(\det r_i=-1\), \(r_1r_2=S\), \(r_2r_3=R\), and \(S^2=R^3=-I\). Thus both displayed product relations on scan 050 hold for this assignment. The dictionary for the other display is \(\sigma\mapsto S\), \(\rho\mapsto R\). Also \(S^{-1}R=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).

The supplied `LM_140-2_notes.md`, LM_P052, second-pass S01, scans 513–516, already records the \(C_4*_{C_2}C_6\) presentation check. That prior note is cited with its own status, and its presentation proof is not repeated here. The present calculation adds a concrete dictionary for the three reflections written in cote 67. In `LM_140-4_text.tex`, scans 234–236 (§53), the named reflections are \(A=\operatorname{diag}(-1,1)\), \(B=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), \(C=\left(\begin{smallmatrix}-1&1\\0&1\end{smallmatrix}\right)\); the exact conversion is \(r_1=A,r_2=B,r_3=-ACA\), with inverse \(C=-Ar_3A\). The central minus sign is retained.

## C02 — the requested action on spherical metrics

**Context credit.** Hua’s modernised cote 67, §IV, after the proposition at source page 36 (scan 037), already supplies the positive-Hermitian-ray / hyperbolic-three-space model and explicitly labels that translation as its own addition. The present check credits that model, writes the area-normalized coordinate metric and its pullback map, and verifies the particular fixed-form cases below.

### C02a. Explicit map and normalization

For a positive Hermitian matrix \(A\), set

\[
q_A(z)=(\overline z,1)A(z,1)^t,\qquad
g_A=\frac{\det A}{\pi q_A(z)^2}|dz|^2.
\]

The formula extends smoothly to the point at infinity: substitution \(z=1/w\) cancels the factor \(|w|^{-4}\) between the denominator and \(|dz|^2\). Positive scalar multiples of \(A\) give exactly the same metric. The representative \(A/\sqrt{\det A}\) has determinant one. Equality of two such metrics with determinant-one positive matrices gives equality of their positive functions \(q_A\), and hence equality of all matrix coefficients.

Writing \(A=B^*B\), the Möbius map \(f_B(z)=(B_{11}z+B_{12})/(B_{21}z+B_{22})\) gives \(g_A=f_B^*g_I\). For \(g_I=|dz|^2/[\pi(1+|z|^2)^2]\), polar integration gives total area one, and \(-\Delta\log w/(2w)=4\pi\), where \(w=1/[\pi(1+|z|^2)^2]\), gives its Gaussian curvature. This proves the stated normalization and the exact map to the Möbius orbit of the round metric.

For a holomorphic Möbius matrix \(M\), substitution into the displayed formula gives

\[
f_M^*g_A=g_{M^*AM}.
\]

Indeed \(q_A(f_M(z))=q_{M^*AM}(z)/|M_{21}z+M_{22}|^2\), and \(f'_M(z)=\det(M)/(M_{21}z+M_{22})^2\). For the antiholomorphic map \(z\mapsto f_M(\bar z)\), the corresponding pullback is \(g_{\overline{M^*AM}}\). These formulas answer the action question attached to scan 037 without changing its statement or filling its missing invariance qualification in the transcription.

The linear coordinate map

\[
(t,x,y,z)\longmapsto
\begin{pmatrix}t+x&y+iz\\y-iz&t-x\end{pmatrix}
\]

has determinant \(t^2-x^2-y^2-z^2\). Positive determinant-one matrices therefore have the exact coordinates \(t>0\), \(t^2-x^2-y^2-z^2=1\). This is the hyperboloid description of the three-parameter space of metrics in scans 038–039. The determinant/action comparison was also checked against Richard Borcherds, course 261 notes 18, pp. 58–59: <https://math.berkeley.edu/~reb/courses/261/18.pdf>.

### C02b. Three fixed-metric calculations

Write \(A=\left(\begin{smallmatrix}a&u+iv\\u-iv&d\end{smallmatrix}\right)\), with real entries \(a,d,u,v\) in this notation.

* The map \(z\mapsto-z\) pulls \(A\) back to \(\left(\begin{smallmatrix}a&-u-iv\\-u+iv&d\end{smallmatrix}\right)\). Its fixed positive forms have \(u=v=0\), precisely the same diagonal forms fixed by every rotation \(z\mapsto e^{i\theta}z\). Their positive-ray parameter \(d/a\) maps to the circle \(|z|=\sqrt{d/a}\); this circle is the equator with poles \(0,\infty\) for \(g_A\).
* Conjugation \(z\mapsto\bar z\) fixes the real-symmetric positive forms, \(v=0\). An explicit inverse parameterization by \(p=s+it\), \(t>0\), is \(A_p=t^{-1}\left(\begin{smallmatrix}1&-s\\-s&s^2+t^2\end{smallmatrix}\right)\). This matrix has determinant one, and \((\bar p,1)A_p(\bar p,1)^t=0\), so the points \(p,\bar p\) are orthogonal lines, hence opposite poles for its round metric. Conversely, determinant-one real-positive \(A\) gives \(s=-A_{12}/A_{11}\), \(t=1/A_{11}\). This supplies the exact map from the conjugate pair in scans 034 and 037 to a metric.
* The antipodal map \(z\mapsto-1/\bar z\) pulls \(A\) back to \(\left(\begin{smallmatrix}d&-u-iv\\-u+iv&a\end{smallmatrix}\right)\). Fixed positive forms satisfy \(a=d,u=v=0\), and therefore give a single positive ray and a single normalized metric.

These checks address concrete cases of the author’s “à vérifier” on scan 033 and his linear-algebra request on scan 037. They do not record a proof check of every compact subgroup case in his proposition.

### C02c. The correction “C’est l’inverse!”

For \(u_\theta(z)=\theta z\), \(|\theta|=1\), and the actual maps \(s_a(z)=a\bar z\), \(t_b(z)=b/\bar z\), with \(a,b\in\mathbb C^*\), direct composition gives

\[
s_a u_\theta s_a^{-1}=u_{\theta^{-1}},\qquad
t_b u_\theta t_b^{-1}=u_\theta,\qquad
s_a^2(z)=|a|^2z,\qquad t_b^2(z)=(b/\bar b)z.
\]

Thus the pole-fixing formula carries the inversion action and the pole-exchanging formula carries the trivial action. These identities check the manuscript’s own correction from scan 034 through scans 035–036, including the location of the action in the extension. They do not identify these finite-dimensional groups with any profinite completion in the results state.

### C02d. Two normalization checks

The map \(w\mapsto e^{2\pi i w}=z\) sends \(|dw|^2\) to \(|dz|^2/(4\pi^2|z|^2)\); its unit circle has length one, exactly the chosen normalization in scan 030. A free degree-two quotient \(p:\widetilde X\to X\) with \(p^*g_X=g_{\widetilde X}\) has \(\int_{\widetilde X}dA=2\int_XdA\); consequently an upstairs area-one normalization gives downstairs area one-half, which specifies the side of the normalization in scans 029 and 031.

For the sphere, a metric preserved up to a scalar by all Möbius maps has scalar one for each map, by integration of its finite nonzero total area. The particular map \(z\mapsto2z\) would then satisfy \(4g(0)=g(0)\), contrary to positivity. This concrete derivative calculation supports the obstruction stated in scans 031 and 038.

## C03 — a numerical witness to Hua’s orange-slice obstruction

**Credit and scope.** The obstruction by extremal length is already supplied in `context/hua_project/67.modern.tex`, §III, subsection “Le modèle des quartiers d’orange,” footnote in the subsection labelled pages 18–21 (the manuscript model is on cote 67 scans 019–020). It is an argument of that modernised commentary, explicitly credited there to its authors. The present run checks it with an explicit annulus and the one pair of pants \(C(32,0,0)\). The target is the fixed orange-cell containment asserted by the proposed model, with the two degenerate discs admitted in the letter. The independent questions about admissible radii and capping fibers retain their own status.

### C03a. The metric and the cell

The positive matrix \(A_0=\left(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\right)\) has determinant \(3/4\). Both matrices for \(z\mapsto1-z\) and \(z\mapsto1/z\) preserve \(A_0\), by multiplication; these maps generate the six permutations of the three labels \(0,1,\infty\). Thus the metric \(g_{A_0}\) realizes the equidistant-label sphere used in Hua’s explicit interpretation of the letter.

Represent the three marked points by \(v_0=(0,1)\), \(v_1=(1,1)\), \(v_\infty=(1,0)\); their squared \(A_0\)-norms are all one. For \(z=x+iy\), the differences of the squared Hermitian overlaps with \(v_0\) and the other two vectors are

\[
|1-z/2|^2-|(z+1)/2|^2=\tfrac34(1-2x),
\qquad
|1-z/2|^2-|z-1/2|^2=\tfrac34(1-|z|^2).
\]

Under \(B^*B=A_0\), the usual round-sphere angular formula for two complex lines uses the normalized absolute Hermitian overlap, so these inequalities give the closed spherical cell

\[
Q_0=\{z:|z|\leq1,\ \operatorname{Re}z\leq1/2\}.
\]

Its two vertices are \(e^{\pm i\pi/3}\). McMullen’s course notes give this same explicit cell, p. 44, §4, providing a separately located geometric comparison: <https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/219/course/course.pdf>.

### C03b. A fixed conformal annulus

On this cell,

\[
|z+1/2|^2=|z|^2+\operatorname{Re}z+1/4\leq7/4.
\]

The round annulus

\[
\mathcal A=\{z:4/3<|z+1/2|<7/5\}
\]

lies outside \(Q_0\). The point \(1\) is at distance \(3/2\) from its center, and \(\infty\) is outside; the exact inequalities are \(\sqrt7/2<4/3<7/5<3/2\). A core circle therefore separates the entire cell, and every subdisc of it containing \(0\), from \(1,\infty\). The annular core family has extremal length

\[
\operatorname{Ext}_{\mathcal A}=\frac{2\pi}{\log((7/5)/(4/3))}=\frac{2\pi}{\log(21/20)}.
\]

For completeness, the annulus is the flat cylinder of circumference \(2\pi\) and height \(\log(21/20)\) via logarithm modulo \(2\pi i\). The constant density gives the displayed ratio. For an arbitrary density, integrating the lengths of horizontal circles and applying Cauchy–Schwarz gives an upper bound of that same ratio for the infimum of core lengths squared divided by area. This proves the equality used here.

### C03c. The actual pair of pants and the contradiction

Take the hyperbolic pair of pants \(P=C(32,0,0)\), with one geodesic boundary of length 32 and two cusps. Mirzakhani’s §3, printed p. 190, specifies \(C(x_1,x_2,x_3)\) and includes vanishing lengths; her §2 identifies zero boundary length with a cusp: <https://www.labri.fr/perso/vdelecro/toprint/mirzakhani1-pdf2up.pdf>. Gauss–Bonnet on cusp truncations gives \(\operatorname{Area}(P)=2\pi\), since \(\chi(P)=-1\), the actual boundary is geodesic, and the two horocycle boundary contributions tend to zero.

Here is the actual conformal cap for this pants. Put the lifted boundary axis on the positive imaginary axis in the upper half-plane, with deck map \(\zeta\mapsto e^{32}\zeta\), and write \(\log\zeta=t+i\theta\). Choose the collar side inside the pants as \(\theta<\pi/2\). The coordinate
\[
w=\exp(\pi^2/32)\exp(2\pi i\log\zeta/32)
\]
is invariant under the deck map, has \(|w|=1\) on the boundary, and identifies the pants collar with an annulus on the \(|w|>1\) side. Along the axis, hyperbolic arclength is \(dt\), and its boundary value \(w=e^{2\pi it/32}\) identifies normalized arclength with the disc's circle action. Attaching \(|w|\leq1\) extends this complex chart; a rotation of \(w\) gives the same pointed filling up to the specified boundary identification. Filling the two cusps by the centers of their punctured-disc charts then gives a compact genus-zero conformal surface, normalized to the sphere by its three labeled centers. This construction supplies the particular admissible cap used in the check, without assuming the proposed global retraction or its fibers.

Normalize its three labels as \(0,1,\infty\), with this actual cap \(D_0\) at \(0\). The proposed orange model assigns \(D_0=\lambda_0Q_0\subset Q_0\), with degenerate discs at \(1,\infty\). That specific assignment embeds \(\mathcal A\) conformally in the interior of \(P\); the annular region between a core circle and the nested disc \(D_0\), containing no other puncture, identifies that core with the free homotopy class \(\Gamma\) of the actual geodesic boundary.

The definition of extremal length gives \(\operatorname{Ext}_P(\Gamma)\leq\operatorname{Ext}_{\mathcal A}(\text{core})\): every density on \(P\) restricts to the annulus; the infimum over \(\Gamma\) is no larger than the infimum over its annular subfamily, while total area is no smaller than annular area. On the other hand, use the actual hyperbolic density on \(P\). Every representative of \(\Gamma\) has length at least 32: its lift joins a point to its translate under the boundary deck transformation, whose translation length is 32. Therefore

\[
\frac{1024}{2\pi}\leq\operatorname{Ext}_P(\Gamma)
\leq\frac{2\pi}{\log(21/20)}.
\]

These bounds conflict. Indeed \(\log(21/20)>1/21\) by integration of \(1/t\) on \([1,21/20]\), and

\[
1024\log(21/20)>1024/21>4(22/7)^2>4\pi^2.
\]

The symbolic calculation checked the rational inequalities exactly. Thus the cap of this particular \(C(32,0,0)\) cannot have the model’s claimed containment in \(Q_0\). This is a checked witness for Hua’s objection to the stated model with degenerate discs. The letter itself asks Bers about the model; it does not supply this refutation or withdraw the model in the packet.

For the extremal-length definitions and the embedded-annulus comparison, see Weber–Hoffman–Wolf, *An embedded genus-one helicoid*, Annals of Mathematics 169 (2009), §2.5, printed pp. 368–369, Definition 5, Example 5 and Proposition 5: <https://math.rice.edu/~mwolf/whw09.pdf>. Only these definitions/comparisons are used here.

## C04 — scope of two post-freeze reading questions

At \((g,\nu)=(0,1)\), the plus alternative in scan 040 gives \(2g+2+\nu\geq1\), while the following displayed \(2g+\nu\geq3\) is false. This exact substitution identifies a consequential sign question; the frozen `+|-` is unchanged.

For the particular inclusion \(X=\mathbf P^1\setminus\{0,1,\infty\}\subset X'=\mathbf P^1\), the literal set \(X\setminus X'\) in scan 045 is empty, whereas \(X'\setminus X=\{0,1,\infty\}\). Hua’s §IV writes the latter order. This records the precise set-theoretic change suggested by context, without editing the manuscript reading or treating the whole classification as checked here.

## C05 — an explicit peripheral-marking example

The letter’s scan 016 says “a homotopy equivalence.” For a pants spine with generators \(a,b\), take the graph map \(\varphi(a)=ab,\varphi(b)=b\). Its inverse is \(a\mapsto ab^{-1},b\mapsto b\), so composition with a deformation retraction to the spine gives an actual self homotopy equivalence of the pants. The peripheral classes are represented by \(a,b,(ab)^{-1}\); the last is sent to \((ab^2)^{-1}\), with abelianization \((-1,-2)\), which differs from all of \(\pm(1,0),\pm(0,1),\pm(1,1)\). Conjugation preserves abelianization, so this class is not any peripheral conjugacy class, even allowing inversion. This supplies an explicit map for the qualification already raised by Hua §III, footnote at the start of the letter; no claim about all outer automorphisms is needed.

## C06 — a coordinate-level comparison for the normal propagator

For the node smoothing \(xy=t\), write \(x=r_x\zeta_x\), \(y=r_y\zeta_y\). The actual polar map is

\[
((r_x,r_y),(\zeta_x,\zeta_y))\longmapsto
(r_xr_y,\zeta_x\zeta_y).
\]

This is the example in Nakayama–Ogus, *Relative rounding in toric and logarithmic geometry*, Geometry & Topology 14 (2010), pp. 2189–2190: <https://msp.org/gt/2010/14-4/gt-v14-n4-p09-p.pdf>. For \(a,b\in\mathbb C^*\), under the coordinate change \(x'=ax,y'=by\), the parameter becomes \(t'=ab\,t\) and the tangent bases become \(\partial_{x'}=a^{-1}\partial_x,\partial_{y'}=b^{-1}\partial_y\); hence

\[
t'\partial_{x'}\otimes\partial_{y'}
=t\partial_x\otimes\partial_y.
\]

This is the explicit tensor transformation matching the branch-tangent description in Hua §X, pages 73–81, later than the supplied scans. It gives a local comparison for the “propagateur normal” of scans 048–049. The supplied packet and this calculation do not construct the manuscript’s global \([Y,N]\), its arithmetic fundamental group, or its Galois comparison; those items remain recorded under their open or unchecked register entries.

## C07 — the orbit map in the Borel display

The action map \(g\mapsto g[1:0]\) from \(\mathrm{SL}_2(\mathbb Z)\) has stabilizer
\[
\left\{\pm\begin{pmatrix}1&n\\0&1\end{pmatrix}:n\in\mathbb Z\right\}.
\]
Indeed the lower-left matrix entry is zero at a stabilizer, and integral determinant one forces both diagonal entries to be the same sign. For a rational line choose a primitive integral column \((p,q)^t\); Bézout supplies \(r,s\) with \(ps-qr=1\), giving the required matrix. Two such matrices carrying the same line differ on the right by the displayed stabilizer. Reduction of a primitive column modulo 2 is nonzero, and its projective class is unchanged by the sign of that column. This verifies the particular quotient and reduction maps on scan 051, without using the register’s three-cusp rank theorem as a substitute.

## C08 — the two source groups for the half-plane map

Use \(q(x+iy)=x+i|y|\) to represent the quotient of \(\mathbb C\) by conjugation as the closed upper half-plane. Commutation with conjugation forces the coefficients of a holomorphic affine map \(az+b\) to be real, with \(a\ne0\), and gives the same real coefficients for an antiholomorphic affine map \(a\bar z+b\). Both maps descend to
\[
F_{a,b}(x+iy)=ax+b+i|a|y.
\]
For \(a>0\) this is \(az+b\) on the upper half-plane, and for \(a<0\) it is \(a\bar z+b\). Its identity fiber in the full conformal centralizer is exactly the two maps \(z\) and \(\bar z\): the restriction to the real boundary forces \(a=1,b=0\). Thus restriction to the holomorphic affine centralizer is injective, while quotienting the full conformal centralizer by \(\{1,\mathrm{conj}\}\) gives the same induced maps. This is the exact morphism accounting for the source wording in scan 043 and Hua’s added “modulo celle-ci”; it identifies no kernel from a profinite result register.


## Review incorporation record

The independent coordinate review records the hash of the version it read. After that review, the root made the already-used nonzero domains in C02c and C06 explicit; no displayed identity was changed. The independent orange review supplied the explicit cap paragraph incorporated above and corrected McMullen’s section locator to §4. Both reviews are retained beside this file.
