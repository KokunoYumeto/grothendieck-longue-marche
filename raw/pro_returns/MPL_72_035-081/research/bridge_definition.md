# Definition over a ring and the exact modular comparison

Post-freeze research for MPL 72, scans 035–081. This note uses the frozen TeX, the three supplied context files, primary mathematical sources, and the reproducible calculation in `bridge_compute.py`; no manuscript image was opened and no transcription, record, inventory, doubt, or progress-log file was changed. The author of this note read `context/README.md`, `context/LM2_CONGRUENCE_ROWS.md`, and `context/notes/RESULTS_STATE.md` in full before writing.

## Answer and evidential boundary

The pages describe an algebraic realization of a regular incidence object: a marked action by reflections or pseudo-reflections on a projective bundle, together with an admissible pinned flag, its orbit, a distinguished hyperplane, and a centre. In the finite-centre chart of scans 073–077, this becomes a rank-
\(n+1\) module with specified rank-one operators and a pinned vector; the reflection specialization also carries a quadratic form. The ring enters through these modules, operators, quadratic equations, invertibility conditions, and base change.

For the **principal-congruence Farey family**, the level-\(N\) triangular map is precisely the Farey tessellation descended to \(X(N)\): the identification of darts is reduction of integral matrices modulo \(N\), and it intertwines the two marked rotations. Sections C–E prove this identification and give an actual morphism to the marked flag action of an explicit family of the form written in scan 073. In this explicit family, the map on darts has kernel \(\mu _2(\mathbf Z/N)/\{\pm1\}\); at level 15 its degree is two, exhibited by the matrix \(4I\). The subsequent maps from labelled edges and triangles to their affine supporting subspaces have additional fibres: at level 15, the 360 labelled edges map onto 180 lines and the 240 labelled triangles onto 80 planes, with exact degrees 2 and 3 proved in E.4.

The supplied pages do not specify a family called “the polyhedron of level \(N\),” its marked generators, or its congruence kernel. The explicit family constructed below is therefore named by its actual parameters, \(n=2,\beta=(1,4),\rho=-2\), throughout; this note supplies no attribution of those parameters to an unidentified manuscript level family. The particular missing datum for B5 is the map from that intended family's marked flag action to the marked matrix quotient in C, including its kernel.

## A. Short research items

The source path convention is `MPL_72_035-081_work/pages/MPL_72_035-081_72_scanNNN.tex`; the scan number is the original archive image number, and the printed manuscript number is one lower in this range. Each item below is separate from the longer proofs.

**BD.1 — Ring-valued definition.** **Scans 038, 073–074; quote:** “hyperpolyèdre régulier … épinglé sur \(S\)” and “\(\tau_i=\operatorname{id}+a'_i\otimes a_i\)”; **kind:** unpursued implication — definition reconstruction. The local input consists of the marked pseudo-reflections, their direction lines and fixed hyperplanes, and the pinning; equations B.1–B.3 below give the exact coordinate data and their base-change maps. **Context relation:** `context/README.md`, Book IV.4 definition request and B5; Grothendieck's *Esquisse*, §4, pp.252–253, independently describes reconstruction by the orbit of the distinguished flag.

**BD.2 — Finite-centre chart.** **Scans 073–074; quote:** “\(c\notin C\) … i.e. \(\rho\) inv” and “il n'y a plus de \(a_{-1}\)”; **kind:** unpursued implication — exact coordinate morphism. The full-to-centred map in B.2 is equivariant and has an explicit inverse, thereby accounting for the disappearance of \(a_{-1}\). **Context relation:** B5 definition; `research/invariant_subspaces.md`, Appendices A1/A4, independently proves the full-module calculation from scans 059 and 074.

**BD.3 — A frozen internal incompatibility.** **Scan 074; quote:** “\(L_i\subset H_{i+1}\)” and “\(\langle a_i,a'_{i+1}\rangle=1\)”; **kind:** reading question. The inclusion makes that pairing zero, whereas its displayed normalization is one; scan 076 explicitly has “\(h_i\notin H_{i+1}\).” **Context relation:** B5 definition and B12 projective formulation; the transcription stays frozen and the coordinate construction below uses the displayed pairings, with this incompatibility recorded.

**BD.4 — Projective formulation and its stated status.** **Scans 076–077; quote:** “\(V\) déterm. mod \(\otimes L\)” and “est équivalente”; **kind:** unproved claim, with a proved coordinate dictionary. The pages state an equivalence with triples \((C,Q_C,\varphi_G^C)\), with the margin \(n\geq2\); B.4 proves the elementary tensor-line and quadratic-zero-locus identifications, while E gives a fully explicit split conic. **Context relation:** `context/README.md`, B12; the pages supplied do not contain the general Azumaya/descent proof posed in that planning question.

**BD.5 — Uniqueness needs the recorded qualification.** **Scans 035, 077; quote:** “Peut-être faux” [uncertain transcription] and “unique hyperquadrique fixe”; **kind:** reading question concerning the supplied proof. Scan 035 questions an invariant-conic uniqueness statement, and scan 077 states uniqueness again in its finite-centre formulation; the exact split example E proves its own equations and maps, without importing a general uniqueness theorem from these lines. **Context relation:** B12; no general invariant-quadric classification is added here.

**BD.6 — B5 with marked generators.** **Scans 038, 073; quote:** “invariants \(\mu_i\) … et \(\beta_i\)” and “\(\lambda_i=-1\)”; **kind:** unpursued implication — external identification and explicit calculation. C gives the principal-congruence Farey map on \(X(N)\), and D identifies the scan-073-shaped specialization \(\beta=(1,4)\) with \(-\operatorname{Ad}(R_i)\) by the displayed change of basis. **Context relation:** B5; `LM2 C.d1` and `LM2 C.r5` remain the unreviewed claims recorded in `context/LM2_CONGRUENCE_ROWS.md`, and this calculation supplies marked finite quotients, not an arithmetic GT action.

**BD.7 — The actual composite-level kernel.** **Scans 073, 076; quote:** “\(\varphi_G^V\)” and “\(\varphi_G^C\)”; **kind:** unpursued implication — proved comparison and finite enumeration. D–F compute the central kernel \(\mu_2(\mathbf Z/N)/\{\pm1\}\), and \(4I\) at \(N=15\) proves the nontrivial fibre on darts, flags, and vertices. **Context relation:** `LM2 C.a16`, `LM2 C.r1`, `LM2 C.r2`, `LM2 C.r3` concern linear/outer congruence action conventions; their statuses are recorded in G, and none of those arithmetic claims is assumed to compute this kernel.

**BD.8 — Vertices and the conic.** **Scans 073, 075–076; quote:** “\(\tau_0^Vs_0=s_0+a_0\),” “\(f_V-\lambda=0\),” and “\(Q_C\)”; **kind:** unpursued implication — proved morphisms. The pinning is \(s_0=-E_{12}\), and the maps are primitive columns modulo sign \(\longrightarrow\) nilpotent vectors \(\longrightarrow Q_C(\mathbf Z/N)\), with both fibres computed in E. **Context relation:** B5 and the split part of B12; at \(N=15\), the three vertex sets have respectively 96, 48, and 24 elements.

**BD.9 — Automorphism context retained as a claim.** **Scans 038–040; quote:** “\(U_\rho=\operatorname{Spec}\mathcal O_S[T]_{(1+\rho T)}\)” and “\(D_0^{**}\) … torseur”; **kind:** unpursued implication — context linkage. The source supplies the group law and the rank-one centralizer action relevant to **Hua, findings register, `72-automorphisms-deform-gm-to-ga`**, whose supplied status is “conjecture (unsearched) | Lean card: partly proved”; its full verification belongs to the companion automorphism calculation. **Context relation:** `context/notes/RESULTS_STATE.md` cites scans 038–039 and Hua's later pp.87–88, which are outside this frozen package.

**BD.10 — Enumeration scope.** **Scans 073–077; quote:** “\((\tau_i^V)_{0\leq i\leq n}\)”; **kind:** unpursued implication — additional exact computation. `bridge_compute.py` enumerates levels \(2,3,4,5,6,7,8,9,10,12,15\) from the displayed integral matrices, records the generator cycles and the kernel, and exports all counts to `bridge_counts.csv` and `bridge_computation.json`; at every odd listed level it also computes every supporting affine line and plane and every geometric flag triple in the group orbit. **Context relation:** `context/README.md` requests reproducible calculations; these files label their new inputs and contain no transcription-derived enumeration falsely attributed to a scan.

## B. Definition appendix: the algebra that the pages actually supply

### B.1 Local pinned operators

Work on an affine chart \(S=\operatorname{Spec}R\). In the finite-centre chart, \(V\) has basis \(a_0,\ldots,a_n\), and scan 073 gives the covectors

\[
\begin{aligned}
\phi_0&=(\lambda_0-1)a_0^*+\beta_0a_1^*,\\
\phi_i&=a_{i-1}^*+(\lambda_i-1)a_i^*+\beta_i a_{i+1}^*
\quad(1\le i<n),\\
\phi_n&=a_{n-1}^*+(\lambda_n-1)a_n^*.
\end{aligned}
\]

The operator is \(\tau_i(v)=v+\phi_i(v)a_i\), its direction is \(Ra_i\), its fixed hyperplane is \(\ker\phi_i\), and its determinant is \(\lambda_i\). Thus \(\lambda_i\in R^\times\) gives the displayed automorphism; the reflection specialization is \(\lambda_i=-1\), with \(\tau_i^2=1\) by direct multiplication. For \(|i-j|>1\), both cross-pairings vanish and \(\tau_i\tau_j=\tau_j\tau_i\).

Scan 074 asks for the direct-sum decompositions by the direction lines and by the annihilator lines of the hyperplanes. Its pinning is a basis \(s_0\) of \(D_0=\bigcap_{i=1}^n\ker\phi_i\), normalized by \(\phi_0(s_0)=1\); it follows directly that \(\tau_0s_0=s_0+a_0\) and \(\tau_is_0=s_0\) for \(i\ge1\). The frozen inclusion in condition 3 is incompatible with the subsequent normalized pairing, as recorded in BD.3.

Every ring map \(R\to R'\) sends these data to \(V\otimes_RR'\), the same matrices with their entries mapped to \(R'\), and \(s_0\otimes1\). This is the explicit meaning of specialization in this coordinate chart. It also records exactly why the inverses used in a chart must remain units under the chosen base change.

### B.2 Full projective module and the finite-centre map

The full coordinate model has \(E=Ra_{-1}\oplus V\), with the extra value \(\phi_0(a_{-1})=1\) and \(\phi_i(a_{-1})=0\) for \(i>0\) (scan 059; see the companion proof). Let \(\pi:E\to R\) extract the \(a_{-1}\)-coordinate and let the common invariant vector be

\[
q=\sum_{j=-1}^n q_ja_j,
\quad q_n=1,\quad q_{n-1}=-\mu_n,\quad
q_{i-1}=-\mu_iq_i-\beta_iq_{i+1}\quad(0\le i<n),
\quad\mu_i=\lambda_i-1.
\]

Put \(d=q_{-1}\). On the actual localization \(R[d^{-1}]\), the vector \(c_0=q/d\) satisfies \(\pi(c_0)=1\), and the maps

\[
E\longrightarrow Rc_0\oplus V,
\qquad x\longmapsto\bigl(\pi(x)c_0,\ x-\pi(x)c_0\bigr),
\qquad (tc_0,v)\longmapsto tc_0+v
\]

are mutually inverse. Since \(\tau_i c_0=c_0\) and \(\pi\tau_i=\pi\), they intertwine every marked \(\tau_i\). On the affine chart \(\pi=1\), this is exactly translation to the centre \(c_0\); its tangent module is \(V\), giving the covectors of scan 073 without \(a_{-1}\). In the reflection specialization the companion proof identifies \(d\) with \(\rho\).

For the full coordinate flag, let \(F_i\) be the projective span of \(a_{-1},a_0,\ldots,a_{i-1}\). The displayed matrices preserve \(F_i\) for \(j\ne i\), while \(\tau_i(a_{i-1})=a_{i-1}+a_i\) changes its rank-\(i\) member. Transport of this flag by the generated group realizes the incidence data; D.3 verifies the complete flag stabilizer for the concrete family used in the modular comparison.

### B.3 Quadratic form

For \(\lambda_i=-1\), scan 073 normalizes the quadratic form by

\[
q(a_i)=\beta_0\cdots\beta_{i-1},\qquad
b_q(a_i,a_{i+1})=-\beta_0\cdots\beta_i,
\qquad b_q(a_i,a_j)=0\quad(|i-j|>1),
\]

with \(q(a_0)=1\) and \(b_q(u,v)=q(u+v)-q(u)-q(v)\). The affine circumscribed equation in scan 075 is \(q(v)-q(s_0)=0\). Formula D.2 checks these statements directly for the example rather than relying on a general uniqueness claim.

### B.4 Projective and quadratic conventions over a base ring

Here \(\mathbf P_{\rm lines}(V)\) parametrizes rank-one locally direct summands, so it is \(\operatorname{Proj}(\operatorname{Sym}V^\vee)\). The Stacks Project uses the quotient-line convention \(\mathbf P(\mathcal E)=\operatorname{Proj}(\operatorname{Sym}\mathcal E)\); the dictionary is \(\mathbf P_{\rm lines}(V)=\mathbf P(V^\vee)\), obtained by dualizing a line inclusion. Over a general ring, the line in an \(R\)-point need not have a global generator; for \(R=\mathbf Z/N\), the Chinese remainder decomposition into local rings makes every invertible module free, and the primitive-column description is valid.

A quadratic equation over an arbitrary ring is a homogeneous degree-two polynomial section \(q\in\operatorname{Sym}^2(V^\vee)\otimes M\), with \(M\) invertible; equivalently, it is the corresponding homogeneous quadratic polynomial law. Its vanishing scheme in \(\mathbf P_{\rm lines}(V)\) is the quadric. The map \(L_0\mapsto L_0\otimes L\) gives a canonical isomorphism \(\mathbf P_{\rm lines}(V)\to\mathbf P_{\rm lines}(V\otimes L)\), and the transported equation is the section corresponding to \(q\) under

\[
\operatorname{Sym}^2((V\otimes L)^\vee)\otimes(M\otimes L^2)
\simeq\operatorname{Sym}^2(V^\vee)\otimes M.
\]

These maps identify the zero schemes. Multiplication of a local equation by a unit generates the same ideal. This polynomial-section formulation and the tensor-line identification work in characteristic 2 as well; they give the precise dictionary for the ambiguities written on scan 076.

## C. The marked Farey map of the principal modular curve

### C.1 Groups, matrices, and the dart bijection

Fix an integer \(N\ge2\) and set

\[
\Gamma=\operatorname{SL}_2(\mathbf Z)/\{\pm I\},\qquad
H_N=\ker\bigl(\Gamma\longrightarrow
G_N:=\operatorname{SL}_2(\mathbf Z/N)/\langle-I\rangle\bigr).
\]

Thus \(H_N\) is the image of the principal congruence subgroup of \(\operatorname{SL}_2(\mathbf Z)\); a class belongs to it exactly when an integral lift reduces to \(I\) or \(-I\). The denominator \(\langle-I\rangle\) is the **single global sign subgroup**. Define

\[
X=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\qquad
Y=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
S=XY=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Their classes satisfy \(X^3=S^2=1\), and \(Y\) has order \(N\) in \(G_N\). The oriented Farey darts are indexed by \(\Gamma\), and the descended darts by \(H_N\backslash\Gamma\); the actual bijection is

\[
H_N\gamma\longmapsto\overline\gamma\in G_N.
\]

It sends right multiplication by each of \(X,Y,S\) to right multiplication by its displayed reduction. Consequently triangle boundaries, vertex rotations, and edge reversals are all preserved, not merely their counts. This is the algebraic regular-map construction used by Stanier, pp.1–3, and the Farey quotient on \(X(N)\) described by Singerman–Strudwick, pp.39–42.

For completeness, the reduction is surjective. A primitive first column \((a,c)\) over \(\mathbf Z/N\) admits \(t\) with \(a+tc\) a unit: for each prime dividing \(N\), one avoids the single forbidden residue when \(c\) is nonzero and uses the Chinese remainder theorem. Elementary row operations then reduce an arbitrary determinant-one matrix to \(\operatorname{diag}(u,u^{-1})\); this last matrix is a product of elementary matrices because

\[
W(u)=E_{12}(u)E_{21}(-u^{-1})E_{12}(u)
=\begin{pmatrix}0&u\\-u^{-1}&0\end{pmatrix},\quad
W(u)W(-1)=\operatorname{diag}(u,u^{-1}).
\]

Every elementary matrix lifts integrally, and \(Y\) and \(S=XY\) generate them. The kernel and the dart bijection above are therefore exact.

### C.2 Surface, cells, and dessin convention

The Farey tessellation lives in \(\mathfrak H\) with ideal vertices in \(\mathbf P^1(\mathbf Q)\). Taking the quotient by \(H_N\), and filling its cusp punctures by those vertices, gives

\[
X(N)=H_N\backslash\bigl(\mathfrak H\cup\mathbf P^1(\mathbf Q)\bigr)
\]

with the usual cusp charts. This is the compact principal modular curve in Milne's definition, and the same quotient operation gives its Farey triangular map. Its vertices, edges, and faces are respectively the coset sets

\[
G_N/\langle Y\rangle,\qquad G_N/\langle S\rangle,
\qquad G_N/\langle X\rangle,
\]

where \(g\langle h\rangle\) denotes a left coset and the cycles on darts are right multiplication. A full flag has one additional choice of side of a dart; there are twice as many flags as darts.

The associated clean dessin is obtained by joining each triangle centre to the centres of its three edges. On the same dart set its black and white permutations are right multiplication by \(X^{-1}\) and \(S\), and their product, read in the order applied for this right action, is right multiplication by \(Y\); the inverse face permutation is therefore \(Y^{-1}\). This gives the exact conversion: dessin black vertices are Farey triangles, white vertices are Farey edges, and dessin faces surround Farey cusp vertices.

### C.3 Counts proved from these sets

There are \(N^2\prod_{p\mid N}(1-p^{-2})\) primitive columns, by the Chinese remainder theorem. Each primitive first column has exactly \(N\) determinant-one second columns: the solutions of \(ad-bc=1\) form one translate of the cyclic free module generated by \((a,c)\). Hence

\[
|\operatorname{SL}_2(\mathbf Z/N)|
=N^3\prod_{p\mid N}(1-p^{-2}).
\]

Write \(\epsilon_N=|\langle-1\rangle|\), equal to 1 at \(N=2\) and 2 at \(N>2\). Then

\[
D=\frac{N^3}{\epsilon_N}\prod_{p\mid N}(1-p^{-2}),\quad
V=D/N,\quad E=D/2,\quad F=D/3,\quad
g=1-\frac{V-E+F}{2}.
\]

These formulas also follow directly from the three marked cycle decompositions, which the code checks independently for every listed level.

## D. A fully verified realization of the scan-073 form

### D.1 Integral reflections and change of basis

Work over \(A_0=\mathbf Z[1/2]\) and put \(V=\mathfrak{sl}_2(A_0)\). Define

\[
R_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
R_1=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\quad
R_2=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
T_i=-\operatorname{Ad}(R_i),
\]

All three matrices have determinant \(-1\) and square \(I\), and

\[
R_0R_1=X,\qquad R_1R_2=Y,\qquad
T_0T_1=\operatorname{Ad}(X),\quad
T_1T_2=\operatorname{Ad}(Y).
\]

Take the ordered basis

\[
a_0=R_0,\qquad a_1=-R_1,\qquad a_2=2R_2.
\]

In coordinates \(B=\begin{pmatrix}x&y\\z&-x\end{pmatrix}\), its column matrix is

\[
P=\begin{pmatrix}0&1&-2\\1&-1&0\\1&0&0\end{pmatrix},\qquad\det P=-2.
\]

Direct conjugation gives

\[
[T_0]_a=\begin{pmatrix}-1&1&0\\0&1&0\\0&0&1\end{pmatrix},\quad
[T_1]_a=\begin{pmatrix}1&0&0\\1&-1&4\\0&0&1\end{pmatrix},\quad
[T_2]_a=\begin{pmatrix}1&0&0\\0&1&0\\0&1&-1\end{pmatrix}.
\]

These are exactly the scan-073 covector formulas with \(n=2\), \(\lambda_i=-1\), \(\beta_0=1\), \(\beta_1=4\). Their covector matrix

\[
A=\begin{pmatrix}-2&1&0\\1&-2&4\\0&1&-2\end{pmatrix}
\]

has determinant 2; both direct-sum conditions hold over \(A_0\), and the adjacent normalized pairings are 1. The positive-diagonal recurrence gives \(\rho=8-2(1+4)=-2\). The change of basis and the centre chart are thus both valid over every odd residue ring.

### D.2 The pinning and source metric

The recurrence for the last-column coefficients gives \(\zeta=(0,2,1)\), so the scan-073 pinning is

\[
s_0=-\rho^{-1}(0a_0+2a_1+a_2)
=a_1+\tfrac12a_2=-E_{12}.
\]

Equivalently \(A(0,1,\tfrac12)^t=(1,0,0)^t\); hence

\[
T_0s_0=s_0+a_0,\qquad T_1s_0=T_2s_0=s_0.
\]

The invariant quadratic form is

\[
q(B)=-\det(B)=x^2+yz
=u_0^2+u_1^2+4u_2^2-u_0u_1-4u_1u_2
\quad(B=\textstyle\sum u_i a_i).
\]

It satisfies \(q(a_0)=q(a_1)=1\), \(q(a_2)=4\), \(b_q(a_0,a_1)=-1\), \(b_q(a_1,a_2)=-4\), and \(b_q(a_0,a_2)=0\). The polar matrix has determinant \(-8=(\beta_0^2\beta_1)\rho\), agreeing with scan 075. Conjugation preserves the determinant, as does the scalar \(-1\) on a quadratic form, so every \(T_i\) preserves \(q\); also \(q(s_0)=0\).

In the projective completion \(\mathbf P(A_0\oplus V)\), the circumscribed equation is therefore \(q(B)=0\), a cone with vertex \([1:0]\); its intersection with the infinity hyperplane \(t=0\) is the smooth conic \(Q_C\subset\mathbf P(V)\). The intersection inclusion and the projection \([t:B]\mapsto[B]\) away from the cone vertex are explicit morphisms. Thus the finite-centre example has a smooth infinity conic while its circumscribed cone has a singular vertex; the smoothness requirement involving \(\sigma'\) in scan 075 is not being assumed for this example.

### D.3 Flags in the actual geometric realization

In affine \(V\), put \(s_1=s_0+a_0=E_{21}\) and \(s_2=s_1+a_1=E_{21}+\operatorname{diag}(1,-1)-E_{12}\). The base flag consists of the vertex \(s_0\), the affine line through \(s_0,s_1\), and the affine plane through \(s_0,s_1,s_2\); the latter has equation \(x+y-z=-1\). The matrices \(T_0,T_1,T_2\) change respectively the vertex, edge, and face member, preserving the other members, by the coordinate identities above.

Over \(\mathbf Z/N\) for odd \(N\), the subgroup of even words is \(\operatorname{Ad}(G_N)\). An element of it fixing \(s_0\) has a lift whose first column is \(u(1,0)^t\) with \(u^2=1\), by E.1; it is therefore \(\operatorname{Ad}(Y^t)\) for a unique \(t\bmod N\). Now

\[
\operatorname{Ad}(Y^t)(E_{21})=
\begin{pmatrix}t&-t^2\\1&-t\end{pmatrix}.
\]

Membership in the base edge forces its \(x\)-coordinate \(t\) to be zero, so the oriented stabilizer of the base vertex and edge is trivial. Conjugation on \(\operatorname{End}(A_0^2)=A_0I\oplus\mathfrak{sl}_2(A_0)\) has determinant one and fixes the scalar summand, so \(\det(\operatorname{Ad}(g))=1\) and \(\det(T_i)=-1\). The full group therefore has two parity cosets, and \(T_2\) fixes that vertex and edge but sends the face equation to \(-x+y-z=-1\); these planes are different since 2 is a unit. Thus the full geometric flag stabilizer is trivial, giving exactly \(2|\operatorname{Ad}(G_N)|\) flags and \(|\operatorname{Ad}(G_N)|\) oriented darts.

## E. The actual morphism, its kernel, and the split conic

### E.1 Vertices: primitive columns to nilpotent vectors

A Farey vertex \(g\langle Y\rangle\) is exactly the first column \(v=(a,c)^t\) of a determinant-one matrix, modulo simultaneous sign. Indeed, the second columns of two such matrices with the same first column differ by a multiple of it, which is right multiplication by \(Y^t\). Its geometric image is

\[
M(v)=\operatorname{Ad}(g)(-E_{12})
=\begin{pmatrix}ac&-a^2\\c^2&-ac\end{pmatrix}.
\]

This formula proves independence of the second column and sign. More generally, for any invertible \(2\times2\) matrix \(g\),

\[
M(gv)=\det(g)\,gM(v)g^{-1}.
\]

To check the identity, write \(M(v)=v(c,-a)\) and use \(((gv)_2,-(gv)_1)=\det(g)(c,-a)g^{-1}\). For the determinant-one rotations it is equivariance under \(\operatorname{Ad}\); for each \(R_i\) it is equivariance under \(T_i=-\operatorname{Ad}(R_i)\). This is a map of the marked vertex actions, with the flag/dart map supplied in E.2.

Its fibres are exact. The image module of \(M(v)\) is \(Rv\), because the row \((c,-a)\) is unimodular; equality \(M(v)=M(w)\) therefore gives \(Rw=Rv\), hence \(w=uv\) for a unit \(u\). The entries of \(M(v)\) generate the unit ideal, so \(M(uv)=u^2M(v)=M(v)\) gives \(u^2=1\). Consequently the nilpotent vertex orbit is precisely

\[
\operatorname{Prim}((\mathbf Z/N)^2)/\mu_2(\mathbf Z/N),
\]

and each fibre from the Farey vertices has size \(|\mu_2(\mathbf Z/N)|/\epsilon_N\).

### E.2 Darts and the central kernel

The actual marked dart map is

\[
G_N\longrightarrow\operatorname{Ad}(G_N),\qquad[g]\longmapsto\operatorname{Ad}(g).
\]

It intertwines right multiplication by \(X,Y,S\) with right multiplication by \(T_0T_1,T_1T_2,T_0T_2\), respectively. A matrix in its kernel commutes with \(E_{12}\) and \(E_{21}\); writing out these two commutators forces its off-diagonal entries to vanish and its diagonal entries to agree. The determinant condition then says \(g=uI\), \(u^2=1\), proving

\[
\ker\bigl(G_N\to\operatorname{Ad}(G_N)\bigr)
=\mu_2(\mathbf Z/N)/\langle-1\rangle.
\]

For odd \(N\), the full flag map is equally explicit. Set

\[
\widehat G_N=\{g\in\operatorname{GL}_2(\mathbf Z/N):\det g\in\{1,-1\}\}/\langle-I\rangle,
\qquad\kappa(g)=\det(g)\operatorname{Ad}(g).
\]

The base Farey flag is the vertex \(\infty\), edge \((\infty,0)\), and triangle \((\infty,0,1)\); its three column representatives are \(e_1,e_2,e_1+e_2\), and their images are exactly \(s_0,s_1,s_2\) from D.3. The map on every flag is \([g]\mapsto\kappa(g)\cdot(s_0\subset\overline{s_0s_1}\subset\overline{s_0s_1s_2})\), and \(\kappa(R_i)=T_i\) proves that it intertwines each of the three flag changes. The determinant separates the two cosets, so \(|\widehat G_N|=2|G_N|\); D.3 and the scalar-kernel calculation prove that every flag fibre has size \(|\mu_2(\mathbf Z/N)|/2\). The support maps send an edge to the affine span of \(M(ge_1),M(ge_2)\), and a triangle to the affine span of those two points and \(M(g(e_1+e_2))\). Writing \(A_N=\operatorname{Ad}(G_N)\), their exact factorizations are

\[
\begin{aligned}
G_N/\langle S\rangle&\longrightarrow
A_N/\langle\operatorname{Ad}S\rangle\longrightarrow
\{aL:a\in A_N\},\\
G_N/\langle X\rangle&\longrightarrow
A_N/\langle\operatorname{Ad}X\rangle\longrightarrow
\{aP:a\in A_N\},
\end{aligned}
\]

where \(L=\overline{s_0s_1}\), \(P=\overline{s_0s_1s_2}\), and E.4 computes the fibres of the second arrows.

No nonidentity element of the adjoint kernel lies in \(\langle X\rangle\), \(\langle Y\rangle\), or \(\langle S\rangle\): the nontrivial powers of \(X\) and \(S\) have a unit off-diagonal entry, and \(Y^t\) is scalar exactly at \(t=0\bmod N\). Thus each map between the labelled coset cell sets has the same degree as the dart map; these are the first arrows in the displayed support factorizations. Equivalently, the adjoint map is the Farey quotient by the explicitly defined larger subgroup

\[
H_N^{\rm ad}=\{\gamma\in\Gamma:
\gamma\bmod N=uI\text{ for some }u^2=1\},
\qquad H_N\subset H_N^{\rm ad},
\]

and the corresponding compact surfaces are related by the actual quotient covering \(X(N)\to H_N^{\rm ad}\backslash\mathfrak H^*\). For odd \(N\), D gives its marked geometric realization. The adjoint matrix map itself is integral and the finite calculation is valid at even levels too; the basis change \(P\) used in D has determinant \(-2\), so D's manuscript-coordinate identification is stated over \(\mathbf Z[1/2]\) and its odd reductions.

### E.3 Projectivization and a verified split B12 morphism

The formula

\[
\nu:\mathbf P^1_R\longrightarrow
Q_C=\{[x:y:z]:x^2+yz=0\}\subset\mathbf P^2_R,
\qquad[a:c]\longmapsto[ac:-a^2:c^2]
\]

defines an isomorphism over every base ring \(R\), in particular over \(\mathbf Z[1/2]\). Its inverse on \(D(y)\) is \([-y:x]\), and its inverse on \(D(z)\) is \([x:z]\); the relation \(x^2+yz=0\) proves that these maps compose to the identity and agree on their overlap. These two opens cover the conic, since \(x\) is nilpotent on the closed locus \(y=z=0\). This proof is scheme-theoretic, so it includes rings with nilpotents.

For \(R=\mathbf Z/N\), the map from Farey vertices to \(\mathbf P^1(R)\) divides primitive columns by all units; it factors through the nilpotent orbit just computed. Its total fibre has size \(|R^\times|/\epsilon_N\), and the second stage has size \(|R^\times|/|\mu_2(R)|\). The displayed formula for \(M(gv)\) proves projective equivariance under every \(g\in\operatorname{GL}_2(R)\). This gives the requested concrete relation among cusp vertices, the nilpotent orbit, and the split conic; a general descent equivalence with all rank-four Azumaya algebras is not asserted from the supplied pages.

### E.4 Labelled map cells and their geometric supports

Write \(A_N=\operatorname{Ad}(G_N)\), and continue at odd levels so that D gives the source-shaped realization. Its labelled edges and triangles are \(A_N/\langle\operatorname{Ad}S\rangle\) and \(A_N/\langle\operatorname{Ad}X\rangle\). For the base line \(L=\overline{s_0s_1}\) and plane \(P=\overline{s_0s_1s_2}\), the maps to their actual supporting affine subspaces are

\[
a\langle\operatorname{Ad}S\rangle\longmapsto aL,
\qquad
a\langle\operatorname{Ad}X\rangle\longmapsto aP.
\]

These are the maps to \(A_N/\operatorname{Stab}(L)\) and \(A_N/\operatorname{Stab}(P)\) induced by the displayed subgroup inclusions. Their fibres can therefore be computed exactly, with the marked full flag orbit still identified with the geometric flag triples by D.3.

At \(N=15\), Chinese remainders give \(A_{15}=\operatorname{PSL}_2(\mathbf F_3)\times\operatorname{PSL}_2(\mathbf F_5)\). Over either field, the base line is \((x,y,z)=(0,t-1,t)\), and its nilpotent points satisfy \(t(t-1)=0\); a stabilizer permutes its two endpoints, and its endpointwise stabilizer is trivial by D.3. Since \(\operatorname{Ad}S\) swaps those endpoints, the local line stabilizer is \(C_2\), and \(\operatorname{Stab}_{A_{15}}(L)=C_2\times C_2\) contains the diagonal \(\langle\operatorname{Ad}S\rangle\) with index 2.

The base plane has equation \(x+y-z=-1\). Its normal functional is \(B\mapsto\operatorname{Tr}(KB)\), where

\[
K=\begin{pmatrix}1/2&-1\\1&-1/2\end{pmatrix}=\tfrac12I-X.
\]

The trace pairing is nondegenerate over both fields, so its stabilizer in \(\operatorname{Ad}(\operatorname{SL}_2)\) is the centralizer of \(X\), modulo sign. Every matrix commuting with \(X\) is \(aI+bX\), of determinant \(a^2+ab+b^2\); the determinant-one solutions over \(\mathbf F_3\) and \(\mathbf F_5\) are exactly \(\{\pm I,\pm X,\pm X^2\}\). Thus the local plane stabilizer is \(C_3\), and \(\operatorname{Stab}_{A_{15}}(P)=C_3\times C_3\) contains the diagonal \(\langle\operatorname{Ad}X\rangle\) with index 3.

Actual additional stabilizers are

\[
g_L=\begin{pmatrix}6&10\\5&6\end{pmatrix},\qquad
g_P=\begin{pmatrix}6&10\\5&1\end{pmatrix}\pmod{15}.
\]

Both have determinant 1; their reductions modulo 3 and 5 are respectively \((S,I)\) and \((X,I)\). The resulting support counts are \(720/4=180\) lines and \(720/9=80\) planes, with the exact labelled-cell fibres 2 and 3. The base supporting line has four orbit vertices, at \(t=0,1,6,10\); the two nontrivial idempotents exhibit the extra geometric coincidences directly. The map's genus in F is calculated from its labelled cycle sets, while these support counts record the further explicit quotient maps.

## F. Exact finite calculations

The script enumerates every determinant-one matrix modulo each listed level, quotients by global sign, verifies generation by \(X,Y\), and computes all three cycle decompositions. It independently enumerates primitive columns, unit orbits, nilpotent images, adjoint matrices, and the central kernel; it also checks all marked intertwining identities and the symbolic basis, pinning, metric, and general vertex-equivariance identities above. For odd levels it computes each supporting line as its complete finite point set, each supporting plane by its normalized affine equation, the fibres of the labelled-cell maps, and all orbit flag triples. The complete outputs are in `bridge_counts.csv` and `bridge_computation.json`; the genus columns in the following table concern the marked regular maps.

| \(N\) | Farey darts | Farey vertices | Farey genus | Adjoint kernel | Adjoint darts | Nilpotent vertices | Adjoint genus | \(\mathbf P^1(\mathbf Z/N)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 6 | 3 | 0 | 1 | 6 | 3 | 0 | 3 |
| 3 | 12 | 4 | 0 | 1 | 12 | 4 | 0 | 4 |
| 4 | 24 | 6 | 0 | 1 | 24 | 6 | 0 | 6 |
| 5 | 60 | 12 | 0 | 1 | 60 | 12 | 0 | 6 |
| 6 | 72 | 12 | 1 | 1 | 72 | 12 | 1 | 12 |
| 7 | 168 | 24 | 3 | 1 | 168 | 24 | 3 | 8 |
| 8 | 192 | 24 | 5 | 2 | 96 | 12 | 3 | 12 |
| 9 | 324 | 36 | 10 | 1 | 324 | 36 | 10 | 12 |
| 10 | 360 | 36 | 13 | 1 | 360 | 36 | 13 | 18 |
| 12 | 576 | 48 | 25 | 2 | 288 | 24 | 13 | 24 |
| 15 | 1,440 | 96 | 73 | 2 | 720 | 48 | 37 | 24 |

At \(N=15\), the scalar square roots of one are \(1,4,11,14\). The exact matrix \(4I\) has determinant \(16=1\pmod{15}\), represents a nonidentity element modulo the global sign \(\{I,14I\}\), and acts trivially by conjugation. The vertices \((1,0)\) and \((4,0)\) represent distinct Farey vertices, and both map to \(-E_{12}\). The complete map counts are:

| Marked map at \(N=15\) | Flags | Darts | Vertices | Labelled edges | Labelled triangles | Genus |
|---|---:|---:|---:|---:|---:|---:|
| Principal-congruence Farey map | 2,880 | 1,440 | 96 | 720 | 480 | 73 |
| Marked map of the \(\beta=(1,4)\) reflection operators | 1,440 | 720 | 48 | 360 | 240 | 37 |

The quotient between these marked maps has degree two on every listed cell type, and \(73-1=2(37-1)\) verifies its unramified surface-covering Euler relation. The geometric support maps are recorded by their actual fibres:

| \(N\) | Labelled adjoint edges → supporting lines | Edge fibre | Labelled adjoint triangles → supporting planes | Triangle fibre | Orbit flag triples |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 → 6 | 1 | 4 → 4 | 1 | 24 |
| 5 | 30 → 30 | 1 | 20 → 20 | 1 | 120 |
| 7 | 84 → 84 | 1 | 56 → 56 | 1 | 336 |
| 9 | 162 → 162 | 1 | 108 → 36 | 3 | 648 |
| 15 | 360 → 180 | 2 | 240 → 80 | 3 | 1,440 |

At \(N=8\), the scalar roots \(1,3,5,7\) yield the same kernel size two for the integral adjoint comparison; its interpretation through the root basis D is excluded by that basis's recorded determinant, not inferred from an abstract category label. For odd prime powers, \((u-1)(u+1)=0\) and the coprimality of \(u-1,u+1\) imply \(u=\pm1\); the marked adjoint dart map at those levels is bijective, with the supporting-plane map at level 9 still having its recorded degree 3.

## G. Context statuses and exact cross-references

These are the supplied run claims, not newly reviewed results. The original Longue Marche scans have not been opened in this subtask.

| Context ID | Supplied status | Original passage listed in context | Relation to this note |
|---|---|---|---|
| LM2 C.a16 | Proved, return's claim | §39, fols.298v–301, cote140-3 scans021–026; §41, fols.315–316v, scans054–057 | Exact linear matrix group and adjoint quotient are specified here; no GT conjugating matrix is computed. |
| LM2 C.r1 | Proved, return's claim | §39, fols.299–300, scans022–024 | Unit and scalar-square quotients in E are actual finite maps; arithmetic outer-image equality remains the context claim. |
| LM2 C.r2 | Refuted, return's claim | §39, fols.300v–301, scans025–026 | Exact source/target conventions are retained; the context's corrected multiplier statement is not used as a premise. |
| LM2 C.r3 | Proved, return's claim | §§39,45, fols.299–301,387–388, scans022–026,176–178 | The linear-to-adjoint morphism and its kernel are proved directly. |
| LM2 C.d1 | Known, return's claim | §39 scans021–030; §44 scans150–168; §46 fols.398–400,409, scans198–202,218–219 | The two kernels \(H_N\) and \(H_N^{\rm ad}\) are explicitly defined; preservation by GT is not investigated. |
| LM2 C.r5 | Proved, return's claim | §§45–46, fols.384–391, scans170–184 | No injectivity claim for an infinite arithmetic action is drawn from finite counts. |
| LM7_PUSH D.44 | Proved; supplied referee checked the parts used by D.50/E.58 | D.2 in the cited register | The integral marking \(S^2=X^3=1\) is given directly; no profinite descent result is needed for C. |
| LM8 E.2 | Proved; intake CONSISTENT | C4 scans231–234, equations(14)–(25) | The global \(-I\) convention is explicit; no braid-lift conclusion is imported. |
| Hua, findings register, 72-automorphisms-deform-gm-to-ga | Conjecture (unsearched); Lean card partly proved | Their pp.37–38,87–88; supplied cross-reference scans038–039 | The source scheme and pinning data are recorded in BD.9; companion note handles proof. |
| Hua, findings register, 72-invariant-subspaces-string | Conjecture (unsearched); Lean card partly proved | Their pp.79–82; supplied cross-reference scans080–081 | `research/invariant_subspaces.md` supplies the independent audit and the full-to-centred map used in B.2. |

The context names these source paths relative to its records' Documents folder:

- LM2: `longue_marche_pro_pilot_20261104/answers/LM2_LOOP_EQUATIONS/LM2_LOOP_EQUATIONS/LM2_LOOP_EQUATIONS_results.csv`.
- LM7_PUSH: `longue_marche_pro_pilot_20261104/answers/LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped/LM7_PUSH/LM7_PUSH_results.csv`.
- LM8: `longue_marche_pro_pilot_20261104/answers/LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped/LM8_LIE_APPROXIMATIONS/LM8_LIE_APPROXIMATIONS_results.csv`.
- Hua: the findings register of `github.com/Commutator-IO/grothendieck-project`, as excerpted in `context/notes/RESULTS_STATE.md`; no additional finding was promoted from that project.

## H. Primary sources

The following primary sources were opened. Durable URLs and the relevant sections are supplied below. Mathematical calculations in B–F are proved here through their explicit maps and stabilizers.

1. **Alexandre Grothendieck, *Sketch of a Programme* / *Esquisse d'un Programme*, §4, printed pp.251–255.** Author's primary account; geometric realizations over rings are on p.252, reconstruction by the marked flag and universal parameters on p.253, pseudo-reflections on pp.254–255. [PDF](https://matematicas.unex.es/~navarro/res/esquisseeng.pdf).

2. **David Singerman and James Strudwick, “The Farey maps modulo n,” *Acta Mathematica Universitatis Comenianae* 89(1) (2020), 39–52.** Farey tessellation, its congruence quotient on \(X(n)\), and primitive-column vertices: printed pp.39–42. [Journal record](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/913), [PDF](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/download/913/785/). The extracted group-definition line on printed p.41 contains a determinant-sign inconsistency; C fixes determinant one explicitly and proves the needed reduction statement.

3. **M. Stanier, “Regular coverings and parallel products of Farey maps,” *Acta Mathematica Universitatis Comenianae* 91(1) (2022), 1–18.** The exact \((G,x,y)\) map, cell cosets, and the two marked Farey matrices are on pp.1–3. [PDF](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/download/1723/916/). This note uses that construction only: the unrestricted covering-degree expression in Lemma 2.1, pp.6–7, gives 27 for \(6\to2\), whereas the verified dart ratio is \(72/6=12\); no degree formula from that lemma is assumed.

4. **J.S. Milne, *Modular Functions and Modular Forms*, version 1.31 (2017).** Definition of \(\Gamma(N),Y(N),X(N)\): introduction, printed p.6; quotient/cusp charts: §2, pp.35–38. [PDF](https://www.jmilne.org/math/CourseNotes/MF.pdf).

5. **The Stacks Project, §27.21, “Projective bundles,” tag 01OA / definition 01OB.** Used solely to pin down the quotient-line convention and its dualization in B.4. [Section](https://stacks.math.columbia.edu/tag/01OA).

6. **Université de Montpellier, official Grothendieck archive catalogue.** Its cote 79 is titled “2-polyèdres réguliers triangulés, et modules libres de rangs 2 sur les anneaux Λ=Z/nZ et Λ=Z” (296 pages, catalogue dating after 1980). [Catalogue](https://grothendieck.umontpellier.fr/archives-grothendieck/). This title identifies a concrete archival follow-up for the missing B5 level marking; the contents of cote 79 were not opened or asserted here.

7. **Caleb Ji, “A note on regular polyhedra over finite fields,” arXiv:2304.03345v1 (2023).** Author's mathematical preprint, expressly presented as a partial interpretation and containing a discussion of a parameter discrepancy; it supplies no substitute for the frozen manuscript's precise normalization. [Record](https://arxiv.org/abs/2304.03345), [PDF](https://arxiv.org/pdf/2304.03345), [HTML](https://arxiv.org/html/2304.03345v1). No result from it is used in the proofs above.

## I. Reproduction

Run `python3 research/bridge_compute.py` from the extracted package root. The script writes only its companion `bridge_counts.csv` and `bridge_computation.json`, uses Python's standard library plus SymPy, and reads no source manuscript file. The archived output reports all symbolic checks and every listed finite-level check passed; the assertions verify exact equalities, so no numerical tolerance or probabilistic test is involved.
