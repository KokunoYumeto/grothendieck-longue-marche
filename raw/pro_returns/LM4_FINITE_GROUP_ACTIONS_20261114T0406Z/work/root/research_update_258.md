## Continuation to 258 claims: whole cyclic centralizers, the exact general boundary image, the remaining negative fixed group, and the full based source tests

This continuation adds C.85–C.88, D.78 and F.23. The resulting register has 258 claims: 227 Proved, 3 Known, 25 Refuted and 3 Open. The report remains INCOMPLETE. These additions retain the original groups and topologies, the original peripheral data and the original source image. They settle the two specified cyclic disk-centralizer examples completely, identify the actual general discrete-operator boundary image, determine the pro-two and odd-kernel structure of the remaining negative torus fixed group, and prove two exhaustive finite-target image comparisons for the actual signed source maps. The general C.12 kernel, the full D.12 recognition equations and the full F.7 source-membership problem remain on the obligation register.

### C.85: a continuous cutoff for every original radial centralizer element

Use C.84's actual plane group \(\mathscr P\), obtained by conjugating the boundary-fixed centralizer through \(j(z)=z/(1+|z|)\). Its elements commute with \(T_1(x,y)=(x+1,y)\), and their displacement is sublinear uniformly on a periodic strip. Its topology is the proved weighted map-and-inverse metric \(\delta_*\).

For a height \(R\), write
\[
m_R(F)=\max_{0\leq x\leq1}|F(x,R)-(x,R)|,\qquad
B=2m_R(F)+4,\qquad L=100B .
\]
The curve \(\Gamma=F(\mathbb R\times\{R\})\) has actual upper complementary component \(\Omega=F(\mathbb R\times(R,\infty))\). Exponentiation \(E(z)=\exp(2\pi iz)\) carries it to a Jordan curve of winding one about zero. Its bounded Jordan domain \(D\) satisfies \(E^{-1}(D\setminus\{0\})=\Omega\).

The normalized Riemann map \(f:\overline{\mathbb D}\to\overline D\) has \(f(0)=0\) and \(f(1)=E(F(0,R))\). For \(g(w)=f(w)/w\), the logarithm is anchored by \(\log g(1)=2\pi iF(0,R)\). It defines the actual lift
\[
\phi(z)=z+(2\pi i)^{-1}\log g(Ez).
\]
The proof gives its inverse from \(f^{-1}\) and the uniquely determined integer, and proves \(\phi(z+1)=\phi(z)+1\). The boundary parametrization is \(\phi(x)=F(\beta(x),R)\), where \(\beta\) is the unique increasing degree-one lift fixing zero. Its inverse \(\alpha\) has displacement at most one.

Put \(d(z)=\phi(z)-z-iR\). The maximum principle and the Cauchy estimate give \(|d|\leq B\) and \(|d'(z)|\leq2B/\operatorname{Im}z\). With the displayed cubic cutoff \(\chi\), define
\[
\widetilde\phi(z)=z+iR+\bigl(1-\chi(\operatorname{Im}z/L)\bigr)d(z).
\]
Below height \(L\) this is the original conformal map. Above that height its derivative differs from the identity by at most \(4B/L=1/25\). The image lies above \(\Gamma\). Properness, local invertibility and the unique preimage of every sufficiently high target point prove that it is a one-sheeted covering of \(\Omega\). The boundary comparison proves the homeomorphism assertion on the closed half-plane.

The auxiliary homeomorphism
\[
A(x,y)=\bigl((1-\min(y,1))\alpha(x)+\min(y,1)x,\ y\bigr)
\]
corrects the bottom parametrization. Its horizontal inverse is proved by bracketing. Composing with \(\widetilde\phi\), reflecting for the lower half-plane, and retaining \(F\) between the two original height lines gives \(\mathcal C_RF\). This map agrees with \(F\) on the middle strip, is the identity outside a bounded strip, commutes with the original translation, and fixes the identity element throughout the construction.

The parameter proof uses Radó's original theorem on conformal maps of variable Jordan domains [C_Rado1923Variable, §1, pp.182–186]. Root inspected the theorem and its proof on the actual printed pages. Fréchet convergence of the boundary curves supplies closed-disk convergence of the normalized maps. The marked boundary normalization, the anchored logarithm, the real boundary inverse and the actual disk inverse are then tracked separately in the proof. These comparisons establish joint continuity in \(F\) and finite \(R\).

For a compact original family \(K\), C.84 gives the common tail function \(a_K(R)\to0\). The actual estimate is
\[
\|\mathcal C_RF-F\|_*
\leq3a_K(R)+\frac5{1+R},\qquad F\in K.
\]
The compact-disk inverse modulus turns this into convergence in the full original map-and-inverse topology, uniformly on \(K\). Thus the cutoff is also jointly continuous at \(R=\infty\). Every positive based sphere family deforms into a common compact quotient annulus. C.81's actual filling and the locally constant deck label then fill that sphere with its original based lift. The program audits 145 exact formulas and parameter faces; the infinite-family continuity is proved in the text.

### C.86: an exact comparison with the original spiral group

Retain the literal spiral compactification
\[
p(z)=\frac{z}{1+|z|}\exp(i\log(1+|z|)).
\]
The global estimate
\[
|p(z+v)-p(z)|\leq\frac{4|v|}{1+|z|}
\]
is proved by splitting the range at \(|v|=(1+|z|)/2\). It supplies the sufficient boundary extension estimate and the forward topology bound.

Necessity retains the original compact disk family. For points \((x,y)\) in the periodic strip, write \(U=(X_F-x)/y\), \(V=Y_F/y\). Two integer translates whose horizontal coordinates approximate \(0\) and \(y\) first exclude unbounded \((U,V)\): their spiral images have a fixed nonzero phase separation, whereas the proposed unbounded outputs would coalesce. For a bounded limiting pair, all real translates give the literal circle-valued identity
\[
\Psi(c+U+iV)=\Psi(c+i),\qquad
\Psi(w)=\frac{w}{|w|}\exp(i\log|w|).
\]
Differentiating this circle-valued identity on its domain, with no angle branch selected, yields
\[
\frac{c+U-V}{(c+U)^2+V^2}
=\frac{c-1}{c^2+1}.
\]
Its polynomial coefficients imply \(U=0\), \(V=1\). The argument includes the possible zero of the left denominator by working on its nonzero domain before taking the polynomial identity. It is uniform on compact actual families, and also applies to their inverse families.

Consequently conjugation by the given \(p\) identifies the spiral horizontal relative centralizer with exactly \(\mathscr P\), with both directions of the original topology proved. The fixed rotation \(R(z)=iz\) gives the map to the original C.72 vertical spiral operator. The resulting group isomorphism has explicit interior formula
\[
\Theta(h)=pRj^{-1}\,h\,jR^{-1}p^{-1}
\]
and boundary value the identity. The coordinate map \(pRj^{-1}\) itself has the two stated incompatible limits along \(e^{2\pi k}-1\) and \(e^{(2k+1)\pi}-1\); the group-topology comparison is supplied by the preceding exact estimates. The producer passes 63 exact checks. C.85's sphere fillings transfer through this very \(\Theta\).

### C.87: contractions of the full centralizers of the two cyclic actions

Let \(A=(\mathbb R/\mathbb Z)\times[-1,1]\), and let \(\mathcal H\) be its orientation-preserving homeomorphism group fixing both boundary circles pointwise. The unique strip lift fixing the lower boundary has upper-boundary translation by an integer \(\tau(b)\). The proof establishes continuity and additivity of \(\tau\), and its section \(b_k([x],y)=([x+k(y+1)/2],y)\).

The equality \(\ker\tau=\mathcal H_0\) is proved using the actual lift of a spanning arc, Epstein's relative arc theorem, a monotone rectangular correction, and the Alexander contraction after cutting the annulus. The source checks include Epstein [C_Epstein1966, Theorem 3.1 and Appendix A1–A2 with their proofs]. The appendix's printed statement and the PL step inside its proof are recorded separately; no stronger printed statement is attributed to it.

The subgroup \(\mathcal E\subset\mathscr P\) consisting of maps equal to the identity for \(|y|\geq1\) descends continuously and bijectively to \(\mathcal H_0\). The inverse is the canonical lower-fixed lift extended by the identity. Both topology maps are proved on a compact periodic rectangle. Yagasaki [C_Yagasaki2000, Lemma 2.1(ii)] supplies a contraction of this exact compact-annulus identity component. Multiplication by the inverse of the contraction's identity track makes it fix the group identity. Transport through the two explicit maps gives a contraction \(\widehat\Gamma\) of the entire \(\mathcal E\).

For \(w>0\), vertical dilation \(D_w(x,y)=(x,wy)\) normalizes the translation. The conjugation \(N_wF=D_wFD_w^{-1}\) satisfies
\[
\delta_*(N_wF,N_wH)\leq\max(w,w^{-1})\delta_*(F,H).
\]
The proof gives the exact closed radial disk normalizer and its inverse and establishes joint continuity for all positive \(w\).

The cutoff width determines a continuous \(W(F)\) large enough that
\[
G(F)=N_{1/W(F)}(\mathcal C_1F)\in\mathcal E .
\]
On the first half of the homotopy parameter use \(\mathcal C_{1/(2s)}F\), with the value \(F\) at \(s=0\). On the second half use
\[
N_{W(F)}\bigl(\widehat\Gamma_{2s-1}(G(F))\bigr).
\]
The middle values agree literally. The endpoint is the identity, the original identity is fixed at every parameter, and all maps are jointly continuous on the whole source group. C.84 and C.86 transport this contraction to the original radial and spiral centralizers. The exact producer passes 42 checks. Root and a second reviewer independently audited the whole proof and the cited primary source passages.

The C.84 final scope paragraph and its metadata were updated to point to C.85–C.87. The change record preserves both old files and before/after hashes. C.84's claim and proof were retained.

### C.88: the exact boundary image for general discrete operators

Retain all C.81 hypotheses: the original closed disk, its compatible metric \(d\), its actual interior \(O\), a closed discrete free proper operator group \(Q\), and a transitive subgroup of the boundary-fixed centralizer. The original covering is \(\pi:O\to N=O/Q\), and its invariant metric is \(d_Q(x,y)=\sup_{q\in Q}d(qx,qy)\). For every actual equivariant interior homeomorphism set
\[
\delta_h(\pi x)=d_Q(hx,x),\qquad
\mathscr V_Q=\{h\in C_{\operatorname{Homeo}(O)}(Q):\delta_h\in C_0(N)\}.
\]
The functions are continuous by the proved metric topology and descend by the actual quotient. The identities
\[
\delta_{h^{-1}}=\delta_h\circ\bar h^{-1},\qquad
\delta_{hk}\leq\delta_h\circ\bar k+\delta_k
\]
prove that this is a group.

Restriction from the original disk centralizer has inverse the literal identity extension over the original circle. Both maps are group isomorphisms and isometries for the sums of uniform map and inverse distances. No separate uniform-continuity condition is imposed: it follows by applying each extended map's compact-disk modulus to all pairs \((qx,qy)\).

The proof also gives an exact compact-parameter criterion. For a compact metric parameter space \(P\), retain actual equivariant interior homeomorphisms with joint interior evaluation. Their identity extensions and inverse extensions form a continuous original disk family exactly when
\[
\forall\epsilon>0\ \exists K\subset N\text{ compact}:
\quad
\sup_{\substack{p\in P\\\pi x\notin K}}d_Q(h_px,x)<\epsilon.
\]
Necessity follows from uniform original boundary displacement: outside the projection of a common interior compact set, every \(qx\) is in the region of the same small estimate.

For sufficiency, a sequence approaching the original circle has a subsequence whose quotient images escape every compact set or remain in one compact core. The escaping subsequence is controlled by the displayed tail. Lift the compact core to a compact \(C\subset O\); the joint interior images of \(P\times C\) form a compact \(C'\). C.81's actual transitive-source comparison expresses all translated images in one compact family of boundary-fixed maps. It therefore makes \(q_jC'\) converge uniformly to the original limit of \(q_jc_j\). This proves joint boundary continuity in the other case.

The resulting map of \(P\times\overline D\), with first coordinate retained, is a continuous bijection of compact Hausdorff spaces. Its inverse supplies joint inverse continuity. The inverse family then satisfies the same common tail condition. Thus even an initial assumption of joint interior inverse evaluation is unnecessary in this exact criterion.

The remaining cutoff must deform arbitrary original sphere families to a common compact quotient support while retaining this uniform tail, the actual interior continuity and every operator equation. C.88 proves the exact image and topology against which that construction must be checked; the construction itself remains unresolved.

### D.78: the actual other negative fixed group and its remaining odd kernel

In the two-section negative once-punctured torus extension, retain
\[
F=\widehat F_2,\quad c=[x,y],\quad E=F\rtimes\langle v\rangle,
\quad S=\langle v\rangle,\quad T=\langle w\rangle,\quad B=C_F(w).
\]
D.75 gives \(C_F(v)=1\) and the actual cusp transporter. D.60's character \(\chi:E\to\widehat{\mathbb Z}\) restricts surjectively to \(B\). Choose the actual \(a\in B\) with \(\chi(a)=1\), and set \(A=\overline{\langle a\rangle}\), \(K=\ker(\chi|_B)\). D.78 proves
\[
A\simeq\widehat{\mathbb Z},\qquad
B=K\rtimes A,\qquad K\text{ is pro-odd}.
\]
The displayed inverse coordinates are \(b\mapsto(ba^{-\chi(b)},\chi(b))\).

The proof begins with the actual absolute, peripheral and relative cochain complexes. D.75's transposed differentials give the two mixed perfect pairings. Their filtrations, the relative orientation trace and the actual cup product prove the full localized duality. The Brown idempotent supported at the \(T\)-class kills the peripheral restriction. The resulting relative-to-absolute isomorphism transports the trace to the actual summand for \(N_E(T)=B\times T\).

For every finite \(E\)-set \(X\), the high cohomology of its permutation module has \(T\)-fixed basis \(Q_X=\mathbb F_2[X^T]\). The actual \(B\)-stable complement is free over \(T\). Since \(\operatorname{cd}_2B\leq1\), the localized normalizer term has its explicit two-degree decomposition. Its degree-one summand is isotropic. Perfect duality therefore bounds \(\dim H^1(B,Q_X)\) by \(\dim H^0(B,Q_X)\).

Each \(B\)-orbit stabilizer has a nonzero mod-two character obtained from its image under \(\chi\). Shapiro's map then forces equality one orbit at a time. Every open \(B_0\) is realized by the displayed actual coset \(E\)-set, so
\[
\dim_{\mathbb F_2}H^1(B_0,\mathbb F_2)=1
\]
for every open \(B_0\leq B\). Two independent characters of a Sylow pro-two subgroup would extend to a common open subgroup, contradicting this equality. The actual \(A_2\) already maps isomorphically to \(\mathbb Z_2\), so it is the whole Sylow pro-two group. The kernel of \(\chi_2\), and hence \(K\), is pro-odd.

For every finite two-primary \(B\)-module \(Q\), finite odd-quotient averaging kills positive \(K\)-cohomology. The actual Hochschild–Serre inflation is
\[
H^n(\widehat{\mathbb Z},Q^K)\;\xrightarrow{\sim}\;H^n(B,Q).
\]
Restriction to the named \(A\) is exactly the coefficient inclusion \(Q^K\hookrightarrow Q\), with the prescribed action. Finally the family of maps
\[
Q_X^B\longrightarrow Q_X^A,\qquad Q_X=\mathbb F_2[X^T],
\]
detects the entire remaining kernel. For every nonidentity \(k\in K\), the proof constructs a finite actual coset \(E\)-set whose distinguished coset is fixed by \(A,T\) and moved by \(k\). Thus surjectivity of all these specific invariant maps is the exact remaining test for \(B=A\). No vanishing of \(K\) is claimed.

Root and an independent reviewer checked the full cochain trace, actual filtration, coset construction and Sylow argument. This is a written cohomological proof; no finite calculation is presented as its substitute.

### F.23: all based maps for the nine-strand source and two exhaustive image tests

The new source basis lives in the original \(Y^\dagger\): the eleven finite old punctures and the sixteen finite collision punctures are surrounded by disjoint rational squares, with their literal straight tails from \(s_*=2+2i\). Exact distance comparisons and a Rouché estimate prove one designated puncture per square, avoid every other square, and prove the tails form an embedded star. The 27 counterclockwise square lassos are therefore an actual free basis. Filling the collision punctures retains the original eleven-generator quotient.

The source configuration has finite labels
\[
(0,1,v_1,v_\zeta,v_{\zeta^2},v_{\zeta^3},v_{\zeta^4},a,-a).
\]
The projection \(Pz=(1+0.371i)z\) has a simultaneous event for the unperturbed collinear triple \(0,a,-a\). That stopped attempt is retained. The accepted computation uses the explicitly labelled offsets \(\delta_i=10^{-14}i^2/P\). For each pair and each path segment, an exact polynomial inequality proves that the entire straight offset homotopy is collision-free. Root isolation, nonzero height and derivative signs, separation of crossing intervals, adjacency and final strand permutations certify every crossing word.

The primary run contains 137 forward segments, 4,932 pair checks and 1,412 crossings. Its exact number-field sign routine is called 846,769 times. The five additional standard-chart segments have ten crossings, and the endpoint comparisons include 10,224 exact projection checks.

The paths \(G\) and \(T\) have the literal endpoints in the text. The endpoint offset whiskers stay in one projection-order chamber. Their homotopy boundary gives the exact based equality
\[
G*T*\gamma*T^{-1}*G^{-1}
=H_{\rm std}*(G_1*T_1*\gamma_1*T_1^{-1}*G_1^{-1})*H_{\rm std}^{-1}.
\]
The graph-straightening map has a displayed inverse and commutes with the retained fillings. The original F.20 path \(\eta\) lies in \(Y^\dagger\); an additional independent exact-field audit verifies its fifteen required comparisons. The path \(\Xi=\mathcal N(G*T*\Phi^\dagger(\eta)^{-1})\), with the actual affine normalization \(\mathcal N\) of F.22.14, identifies the original source map with the computed map by literal path cancellation. Every constituent path fixes the first two coordinates at \(0,1\), so this normalization fixes every remaining coordinate pointwise along these paths and retains the literal endpoints.

The new geometric section and F.19's original section differ by the actual source-kernel cocycle
\[
c(l)=\Phi^\dagger(i_{\rm geo}(l)i(l)^{-1}).
\]
The coordinate changes \((d,l)\mapsto(dc(l)^{-1},l)\) and \((e,l)\mapsto(ec(l),l)\) are inverse and preserve the original subgroup \(K^+\).

The braid calibration is fully specified. The positive producer letter is the displayed clockwise adjacent geometric exchange: its squared radius is everywhere positive and its argument derivative is strictly negative. The lower-whiskered clockwise last-strand lassos \(\beta_i\) map to the exact triangular words \(\tau_i\); the inverse sends \(X_i\) to \(\tau_i(\beta)\), and \(\tau^2=1\). The crossed identity \(u_{bc}=u_b\alpha_b(u_c)\) then derives the actual section action and general pure-braid action \(v\mapsto u_b\alpha_b(v)u_b^{-1}\). Filling compatibility is proved on actual pure generators.

The F.20 and F.22 passages were repaired to state these geometric coordinates and inverse maps explicitly. No computed crossing letter, word or finite output changed. The repair record retains both former sources, exact replacements and before/after hashes. The supplementary calibration producer passes 2,473 exact checks.

The finite scans quantify over every continuous homomorphism of the actual ambient group \(V_\pm\) to the indicated finite group. Their conclusion is
\[
\rho(\mathcal K_\pm)=\rho(R_\pm)
\quad\text{for every }\rho:V_\pm\to S_3
\quad\text{and every }\rho:V_\pm\to A_4.
\]
F.21's actual normal-generation map reduces a possible proper marginal image to a conjugate \(C_2\) in \(S_3\), or a conjugate \(C_3\) in \(A_4\). The primitive local divisor calculation proves the restrictions on the four deleted-generator values. The exact decorated Artin recurrence evaluates the full recorded source action without expanding its intermediate free words. The positive and negative coordinates use their proved triangular conversions.

| Target | Candidate generating tuples per sign | Tuples passing all eight collision seeds | Tuples surviving one source-generator closure step |
|---|---:|---:|---:|
| \(S_3\) | 54,720 | 624 | 0 |
| \(A_4\) | 11,327,040 | 15,552 | 0 |

The eleven actual old source generators act by permutations of the finite tuple set. The pruning computes the largest forward-invariant subset of the seed-good set; finiteness makes this invariant under inverse generators as well. Thus it tests the entire source action. The A4 candidate count is independently checked by the exact formula \(12^3(9^4-1)-4\cdot3^3(3^4-1)\), and the actual subgroup lattice is reproduced.

Separately, \(h(s)=\zeta^2/s\) exchanges the signs. The proof retains the original source basepoint and the explicit three-segment path \(\lambda:s_0\to h(s_0)\). The source automorphism \(g\mapsto\lambda h(g)\lambda^{-1}\), its inverse and its inner square are all written out. The matching labelled target permutation and \(w=\Phi^\dagger(\lambda)\) give a commuting based square. On the marginal groups the resulting isomorphism \(R_-\to R_+\) carries \(\mathcal K_-\) exactly onto \(\mathcal K_+\). The 64 exact symmetry checks reproduce the stated paths and identities.

An independent reviewer reran the complete source pipeline in an isolated directory. All 35 outputs are byte-identical, including all 27 meridians and both exhaustive scans. The 49-file input manifest, reproduction comparison, calibration snapshot and additional eta audit are retained. The former interrupted expanded-word attempt supplies no accepted completed output. Full marginal equality, \(K^+=D^+\), and the original residual-source equation remain unresolved.

### New primary-source checks and exact remaining obligations

The Radó, Epstein and Yagasaki source PDFs, page inspections and file hashes accompany the proof audits. Their precise theorem uses are stated above. Two additional primary-source searches were made before drawing any further recognition conclusion.

Wykowski's *Profinite subgroup accessibility and recognition of amalgamated factors*, Groups Geom. Dyn. 20 (2026), 1071–1097, DOI 10.4171/GGD/851, was read at the publisher PDF, including Theorems 1.1–1.2 [R-WykowskiAccessible2026]. The first starts with a specified accessible subgroup in a finite graph of profinite groups; the second starts with a finitely generated discrete virtually free group and a specified discrete subgroup. The actual LM4 extension still needs its own required graph and peripheral comparison. No such decomposition is imported from these source statements.

Collas's *Action of the Grothendieck–Teichmüller group on torsion elements of full Teichmüller modular groups in genus zero*, JTNB 24(3) (2012), 605–622, DOI 10.5802/jtnb.813, was checked in the author's primary PDF and the Numdam journal record [R-CollasTorsionAction2012]. Theorems A–B concern prime-order torsion in the completed mapping class groups and the specified outer action on it. The acting group's definition includes the pentagon. Applying these theorems to the D.12 candidate requires a map placing that candidate in the stated torsion target and a proof that the required peripheral equation transfers. Such a map is not supplied by this source check.

C.12 still asks for the original general admissible-surface level-zero kernel, including controlled arbitrary-family deformation for discrete operators, arbitrary-frontier lifting and nonfixed-frontier pasting. D.12 retains the literal pants equation D.74.40, the negative torus equation D.75.5 and the scalar cubic decision. The two labelled negative solution spaces have the proved inverse continuous correspondence; their nonemptiness is unresolved. D.78 additionally retains its exact finite-invariant test for the pro-odd kernel. F.7 retains the original source image and its residual membership equation, with the whole marginal images and the interaction kernel still to be determined.

The new build and visual review records below govern this exact checkpoint. The older continuation records remain as dated research history; their earlier scope sentences are superseded by the current 39-obligation table and the explicit C.85–C.88, D.78 and F.23 results.

### Sealed 258-claim build and typesetting record

The current registers contain 258 claims: 227 Proved, 3 Known, 25 Refuted and 3 Open. The 39-obligation table remains the governing completion register. There are 36 doubtful-reading records and 81 bibliography entries; 77 entries are used in the paper. The successful four-stage LuaLaTeX/BibTeX build produces 567 pages and 3,824,433 PDF bytes, with SHA-256 `5924d78e3b9162accc82097e84064634e6abd5ffab1127aaf80745836ed5a5d4`.

The historical build diagnostics contain eleven overfull boxes, with widths 13.68645, 3.45642, 55.68105, 76.02393, 37.09235, 36.24559, 13.30484, 2.94995, 8.79562, 13.04182 and 7.59178 pt. Each was repaired in its source. The final build has **zero overfull boxes**, including zero above 2 pt, and zero missing-character, unresolved-reference, unresolved-citation or fatal diagnostics. The first 258-claim attempt also stopped at the C.88.2 display: its two alignment-column pairs required `aligned` in place of `split`. That source repair and the stopped log are retained. A later generated-provenance punctuation repair removes duplicate terminal periods without altering the manuscript metadata or mathematical text. Neither successful 258-claim build had an overfull box.

The complete 1,879-line initial successful log was read, and all changes in the final log were read; only the run timestamp and PDF byte count changed. The final BibTeX log was read. The inherited nonfatal notices are the font-loader fallback followed by successful T1 Latin Modern embedding, one underfull cell on the notation page, and BibTeX's number-without-volume notice for Tukia's Series A I, number 504. No invented volume was supplied.

Visual review covers 92 exact final-PDF pages, including every historical overflow location, all pages of C.85–C.88, D.78 and F.23, the repaired F.20/F.22 coordinate passages, all updated unresolved-overview pages, and a spread through the paper and bibliography. Root actually viewed 22 changed or new final images; the independent reviewer actually viewed four changed final images. The remaining 66 images were checked byte for byte against images actually viewed in the sealed preceding review. The initially truncated display of pages 554–555 was not counted; both were reopened and actually inspected. The final image hashes, provenance chains and review assignments are retained in `verification/render_review.json`, with all 92 final PNGs included. No clipping, overlap, missing glyph or outstanding punctuation issue was observed. The current PDF hash is checked again before packaging, so this review cannot certify a different build.
