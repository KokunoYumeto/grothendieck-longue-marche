
## Continuation to 252 claims: exact radial topology and the full two-point kernel presentation

This checkpoint adds C.84 and F.22, both proved and independently audited. Its register has 252 claims: 221 Proved, 3 Known, 25 Refuted and 3 Open. The three open claims retain their exact original maps. C.84 supplies a complete topology comparison and a contraction on an explicitly described proper subspace. F.22 supplies a full kernel presentation and exact source-image maps; its source-surjectivity question remains unresolved.

### C.84: the original radial centralizer and its precise topology

Keep the actual radial coordinate
\[
 j(z)=\frac{z}{1+\|z\|},\qquad j^{-1}(w)=\frac{w}{1-\|w\|},
\]
and the original operator \(q=jT_{(1,0)}j^{-1}\) on the disk interior. A plane homeomorphism commuting with the unit horizontal translation has the form
\[
 F(x,y)=(x+u_F(x,y),y+w_F(x,y)),
\]
with both displacement coordinates periodic in \(x\). C.84 proves that conjugation through this very \(j\) identifies the original boundary-fixed centralizer with exactly the maps satisfying
\[
 \lim_{R\to\infty}\sup_{0\leq x\leq1,\ |y|\geq R}
       \frac{\|F(x,y)-(x,y)\|}{|y|}=0.
\]
The proof derives the inverse condition from the same original disk extension. No independent inverse-growth assumption is added to the description.

Necessity uses two labelled translates of the same point: their first coordinates approximate \(y\) and \(-y\), while periodicity leaves their output second coordinate unchanged. Their radial images approach two prescribed diagonal points on the original circle. The two output ratio limits force \(Y_F/y\to1\) and \(u_F/y\to0\). Compactness in the actual disk topology makes this argument uniform over every compact family, including its inverse family. Sufficiency combines sublinear displacement outside a horizontal band with bounded displacement on its compact periodic quotient, then uses the exact radial estimate of C.83 to extend by the identity on the original circle. The compact disk bijection has a continuous inverse.

The original map-and-inverse topology becomes the finite metric
\[
 \delta_*(F,H)=\|F-H\|_*+\|F^{-1}-H^{-1}\|_*,\qquad
 \|F-H\|_*=
 \sup_{0\leq x\leq1,\ y\in\mathbb R}
       \frac{\|F(x,y)-H(x,y)\|}{1+|y|}.
\]
Both topology maps are proved. Actual convergence gives uniform sublinear tails and ordinary coordinate convergence on compact rectangles. Conversely, for fixed \(H\), the finite constant
\[
 c_H=\sup_{(x,y)}\frac{1+|y|}{1+\|H(x,y)\|}
\]
gives the explicit bound
\[
 \sup_z\|jF(z)-jH(z)\|\leq2c_H\|F-H\|_*.
\]
The same inequality for inverses completes the original topology comparison.

Let \(\mathscr M\) be the subspace where each vertical coordinate function \(y\mapsto Y_F(x,y)\) is increasing and onto. Its contraction uses the exact factorization
\[
 V_F(x,y)=(x,Y_F(x,y)),\qquad
 H_F=FV_F^{-1}=(h_{F,y}(x),y),\qquad F=H_FV_F.
\]
Bracketing by two height values proves continuity of the vertical inverse. Periodicity forces every horizontal fiber map \(h_{F,y}\) to be increasing. Interpolate each of these genuine one-dimensional homeomorphisms with the identity and multiply the resulting two factors. The product remains in \(\mathscr M\), has identity and original-map parameter faces, and fixes the group identity. Weighted forward estimates and an explicit modulus for the inverse on the compact disk prove joint continuity in the parameter and the entire source subspace.

The proper-inclusion witness is fully specified: identical rotations in disjoint disks centered at \((k+1/2,0)\), with angle \(\pi\) on each smaller core and a linear radial taper to zero. The map and its inverse commute with the original translation and have bounded displacement. Two specified vertical heights reverse order in a core. Thus the constructed group element is outside \(\mathscr M\). A deformation of arbitrary actual families into \(\mathscr M\), or a contraction of the whole radial group, remains to be constructed.

The independent producer reruns pass 46 exact symbolic and rational checks. They audit the two-direction identities, a mixed-fiber example and its inverse, parameter faces, original operator relations and the explicit order reversal. The uniform-family and whole-space topology assertions have their written proofs.

### F.22: a presentation of the original full joint kernel

Keep the F.19 base configuration, the seven old finite labels and the two moving points \((p,n)\). Filling four old labels changes the punctured plane \(S'\) to \(S\). The original full joint kernel is
\[
 D^+=\ker\!\left(
 \widehat{\pi_1(\operatorname{Conf}_2(S'),(p,n))}
 \longrightarrow
 \widehat{\pi_1(\operatorname{Conf}_2(S),(p,n))}
 \right).
\]
A disk containing all seven old points and \(p\), while excluding \(n\), supplies compatible based point-pushing sections of the two positive-point projections. The disk inclusions induce the original punctured-plane fundamental-group isomorphisms before and after filling. All basepoint comparisons here are the constant path at \((p,n)\).

In the retained geometric free coordinates, put
\[
 R_+=\ker(\widehat F_7\to\widehat F_3),\qquad
 R_1=\ker(\widehat F_8\to\widehat F_4).
\]
The four filled old meridians are exactly the killed generators in both maps. The actual fiber inclusion \(\iota\), section \(\sigma\) and positive-point projection \(p_+\) give inverse continuous maps
\[
 (b,g)\longmapsto\iota(b)\sigma(g),\qquad
 d\longmapsto\left(\iota^{-1}(d\sigma(p_+d)^{-1}),p_+d\right)
\]
between \(R_1\rtimes R_+\) and \(D^+\). The action is the actual conjugation by this section.

The proof supplies all seven Artin point-pushing words and their actions on the eight-generator fiber. The erased last-meridian conjugator gives the same cocycle convention as F.20. Its geometric kernel coordinates form a triangular substitution whose square is the identity. This proves the action formula and both filling maps in the stated coordinates. The affine normalization and its inverse connect these coordinates to the original normalized moduli groups; no base configuration or labelled puncture is replaced without its map.

For a compact profinite generator space \(T\), the proof constructs \(\mathfrak F(T)\) from exactly the finite quotient homomorphisms whose generator maps are continuous. Its universal property concerns continuous maps from that \(T\). In these terms,
\[
 R_+\cong\mathfrak F(\widehat F_3\times\{1,2,3,4\}),\qquad
 R_1\cong\mathfrak F(\widehat F_4\times\{1,2,3,4\}).
\]
The maps send \((q,j)\) to the retained lift of \(q\), the corresponding old meridian, and the inverse lift. Both inverse homomorphisms are given. Joint continuity of the indexing-group action is proved using finite-valued generator maps, their finite translation orbits, and the resulting invariant open quotient kernels. The topology of this generator space remains part of the presentation.

Let \(p_-\) be the other actual one-point forgetting and \(R_-\) its corresponding old-filling kernel. The joint map is onto:
\[
 1\longrightarrow W\longrightarrow D^+
       \xrightarrow{(p_+,p_-)}R_+\times R_-\longrightarrow1.
\]
Here \(W\) is precisely the intersection of the old-filling kernel and the positive-puncture-filling kernel inside the actual eight-generator fiber. Retaining the three common letters gives a free profinite product on two compact clopen generator pieces: four old meridians and the positive puncture meridian \(t\). The two fillings are the two factor retractions. Their joint kernel is the closed normal closure of
\[
 [\eta(q,U_j),\eta(q',t)],\qquad
 \eta(q,e)=s_-(q)e\,s_-(q)^{-1}.
\]
Quotienting by these exact commutators and multiplying the two commuting factors gives the displayed inverse map to their direct product. Translation of the two indices proves that the same normal closure is obtained in the actual ambient fiber.

The element \([U_1,t]\) generates a full closed copy of \(\widehat{\mathbb Z}\) in \(W\). For every modulus \(m\), the explicit map to \(\operatorname{UT}_3(\mathbb Z/m)\) sends it to \(I+E_{13}\), and its exponent \(z\) to \(I+(z\bmod m)E_{13}\). These maps detect every nonzero profinite exponent. This proves the full procyclic assertion. Its membership in \(K^+\) is not determined by that detection.

### The source map and its two exact marginal images

The original rank-27 source has the eleven retained free meridians and sixteen collision meridians. The same compact-generator construction identifies its filling kernel with \(\mathfrak F(L\times\Delta)\). The actual source image is therefore
\[
 \Lambda:\mathfrak F(L\times\Delta)\longrightarrow D^+,
 \qquad (l,d)\longmapsto j(l)\nu_dj(l)^{-1},
 \qquad\operatorname{im}\Lambda=K^+.
\]
Its coordinates are the explicitly proved inverse semidirect-product coordinates. Both sections \(j\) and \(\sigma\) occur with their actual roles.

Partition the sixteen collisions into eight positive and eight negative ones. The corresponding rank-19 signed source groups retain precisely the old eleven meridians and their eight signed collision meridians. Their filling kernels have images
\(\mathcal K_\pm=p_\pm(K^+)\). Forgetting the positive point removes each positive collision; the remaining rational configuration extends over that point. The opposite statement holds for negative collisions. These killed-coordinate identities persist under conjugation by \(j(l)\) through the full forgetting maps on the ambient group \(G\). Those full maps are used because \(j(l)\) need not lie in the two-point kernel \(J\).

The two compact signed source images independently lift the two marginal coordinates. Multiplying those lifts gives the exact row
\[
 1\longrightarrow K^+\cap W\longrightarrow K^+
       \longrightarrow\mathcal K_+\times\mathcal K_-\longrightarrow1,
\]
with its actual inclusions into the \(D^+\) row. Equality of either marginal with \(R_\pm\), surjectivity of \(\Lambda\), and the original residual source-membership equation remain unresolved.

The independent F.22 producer reruns pass 926 exact checks, including all seven point-pushing action words and inverses, both filling squares, the triangular coordinates in ranks eight, seven and four, and thirty finite unitriangular-group instances. Its output SHA-256 is `b795dfc5adeb9b7e8e337d7c2e3d8bbe4ed3ec64b58e5f8734ace1077db4b819`. The compact-generator and full group conclusions follow from the written inverse maps and all-moduli argument.

### D.75: exact correspondence between the two labelled solution spaces

The separate continuation record retains the unique original transporter \(g\), cusp \(c\), and both formulas \(a_{\mu,i}\). For the actual closed solution spaces
\[
 T_i=\{(\mu,k):k(c^{-\mu}a_{\mu,i})k^{-1}=a_{\mu,i}\},
\]
it proves inverse continuous maps
\[
 \begin{aligned}
 T_1&\longrightarrow T_0,&
 (\mu,k)&\longmapsto(-\mu,c^{-(\mu+1)/2}kg),\\
 T_0&\longrightarrow T_1,&
 (\nu,l)&\longmapsto(-\nu,c^{(1-\nu)/2}lg^{-1}).
 \end{aligned}
\]
Root independently checked the equations and both composites. Setting \(d=(\mu+1)/2\) and \(b=a_{-\mu,0}=c^{-d}g\) changes the first equation, by conjugation and inversion, to the second with conjugator \(c^{-d}kg\). The inverse formula reverses those operations. Division by two on the indicated even profinite exponents is the same continuous operation already established in D.75. This preserves the original cusp throughout and reduces neither equation to homology or a maximal pro-2 quotient. Nonemptiness remains unproved.

### Controlled-support continuation and current validation

The unnumbered continuation note proves that filling a compact carrier is natural under the original operator maps and remains inside the same \(d_Q\)-ball. It also proves that small carriers can have a large connected saturation: for the radial translation model, radius-one planar disks centered at \((0,n^2)\) have \(d_Q\)-diameter at most \(4/n^2\), whereas their integer-translate saturation contains a complete horizontal line and has original disk diameter two. A controlled lift still requires a bound on its trajectories inside that saturation.

The report retains the exact operator-label test against the displayed Fabel motion, with the primary construction checked on printed pages 5–6 of arXiv:math/0202163v1. The original evaluation equations force moved labels to be a union of operator orbits. The single-point motion does not satisfy those equations for a free infinite operator group. No isotopy-extension theorem from that source is imported into C.84.

The source rechecks accompanying the D continuation preserve their stated hypotheses and record the missing maps to the actual full profinite transporters. They have supplied no further peripheral recognition or scalar cubic exclusion.

The first 252-claim build stopped at an unbraced TeX accent argument in three occurrences of the F.22 profinite-integer notation. Adding the required braces changes no mathematical expression. The original failed log, before/after proof hashes and repair record are retained. Final build, image review and archive verification are recorded after completion below.

### Final 252-claim build and page review

The final four-stage LuaLaTeX/BibTeX build succeeds with 541 pages and PDF SHA-256 `e800e9df3409ec395850f9d078d6bd5701cb04d0c09984480ae196b6f7fdca33`. The exact source hashes are retained in the build record. The final log has zero overfull boxes, zero missing glyphs, zero unresolved references or citations, and zero fatal errors. The inherited Tukia number-without-volume warning retains the actual Series A I, number504 metadata. The luaotfload fallback and one underfull first-page table cell are also recorded.

Seventy-one final-layout page images were reviewed: root opened twenty-one, the independent reviewer opened twenty-one, and twenty-nine more were proved byte-identical to images actually inspected at the preceding checkpoint. All eleven historical overflow passages, every page of C.84 and F.22, the revised obligation overviews and a spread across all six parts were checked. The separate image hashes and exact PDF hash are in `verification/render_review.json`; no clipping, overlapping equation tags, missing text or footer collision was found.

The registered total is 252 claims: 221 Proved, 3 Known, 25 Refuted and 3 Open. The 39-obligation register remains at the start of the INCOMPLETE report. C.85, D.78 and the continuing source-braid investigation are staged research beyond this checkpoint and have not been added to its proved-claim register.
