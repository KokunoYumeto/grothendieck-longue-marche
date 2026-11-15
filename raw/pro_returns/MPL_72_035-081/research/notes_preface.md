# Research notes — MPL 72, scans 035–081

## Reading guide and principal findings

The transcription was frozen at **2026-11-15 00:37:12 UTC** and the context was opened at **00:37:18 UTC**. These notes were written afterwards from the frozen text, the three supplied context files, primary mathematical references, and the explicit calculations included here. Research comparisons, alternative formulas, proofs, and counterexamples have not been inserted into the transcription.

The package contains 47 scans: 36 mathematical text sheets, 6 reused typed sheets, 4 covers, and 1 cancelled draft. The element inventory has 1,052 rows, each marked transcribed; the second reading is logged for every scan. The handwritten page numbers in this range are 34–80, with two inscriptions of 60 on scan 061.

### The definition question

In the coordinate formulation actually supplied by these pages, a pinned regular realization over a ring consists of a finite locally free module or its projective bundle, marked rank-one operators
\[
T_i(v)=v+\phi_i(v)a_i,
\]
their direction lines and fixed hyperplanes, the recorded unit and incidence conditions, and an admissible pinned flag whose translates supply the realization. On the finite-centre chart of scans 073–074, the basis is \(a_0,\ldots,a_n\), the diagonal pairings are \(\phi_i(a_i)=\lambda_i-1\), the predecessor pairings are \(1\), the successor pairings are \(\beta_i\), and all further pairings vanish; \(\lambda_i\) is a unit. The reflection specialization \(\lambda_i=-1\) has the invariant quadratic form proved below, with \(q(a_0)=1\), \(q(a_i)=\beta_0\cdots\beta_{i-1}\), and the displayed adjacent polar coefficients.

The definition appendix supplies the base-change maps, the full-to-centred equivariant isomorphism, the projective convention, and the marked flag construction. It also records the literal inclusion on scan 074 that evaluates to \(1\) under the subsequent normalized pairing, and the normalization on scan 075 that fails on the explicit isotropic pinned line below. The general categorical equivalence stated on scan 077 therefore remains attached to those exact reading and descent questions.

### Bridge B5: what is proved, and the missing source marking

For the principal-congruence Farey family, the level-\(N\) triangular map is the Farey map on \(X(N)\), by the explicit bijection
\[
H_N\backslash\operatorname{PSL}_2(\mathbf Z)
\longrightarrow
G_N=\operatorname{SL}_2(\mathbf Z/N)/\langle-I\rangle,
\qquad H_Ng\longmapsto\bar g.
\]
The proof tracks the two marked rotations and the edge involution, and gives the vertex, edge and face cosets. The primary sources and their precise uses are cited in the definition appendix.

The manuscript-shaped reflection specialization
\[
n=2,\qquad(\beta_0,\beta_1)=(1,4),\qquad\rho=-2
\]
has an explicit change of basis to trace-zero \(2\times2\) matrices over \(\mathbf Z[1/2]\), with \(T_i=-\operatorname{Ad}(R_i)\), \(q=-\det\), and pinning \(s_0=-E_{12}\). Its marked dart map is \(G_N\to\operatorname{Ad}(G_N)\), with proved kernel \(\mu_2(\mathbf Z/N)/\langle-1\rangle\) at odd levels. At \(N=15\), \(4I\) gives a degree-two map: 1,440 Farey darts map to 720 adjoint darts, 96 cusp vertices map to 48 nilpotent vertices, and further projectivization gives 24 conic points.

The labelled adjoint map has 360 edges and 240 triangles at that level. The explicit supporting-subspace maps have further fibres of sizes two and three, giving 180 affine lines and 80 affine planes; the full geometric flag orbit still has 1,440 elements. These fibre computations specify exactly how the combinatorial and geometric data are related.

The supplied 47 scans give no marked family named “the polyhedron of level \(N\)” and no congruence kernel identifying that intended family. Consequently the established comparison here is for the parameter family just displayed; the archival comparison still needed for B5 is its map to the intended level family's marked generators and kernel.

### Two direct checks on the Hua context entries

For **Hua, findings register, 72-automorphisms-deform-gm-to-ga**, the notes prove the group law
\[
t*s=t+s+\rho ts,\qquad
U_\rho=\operatorname{Spec}R[t,(1+\rho t)^{-1}],
\]
the explicit specialization maps, the complete labelled linear centralizer \(cI+t\,w\pi\), and its projective quotient. They also compute the subgroup preserving the quadratic form, including two concrete characteristic-two fibres and the identity-section qualification on scan 043.

For **Hua, findings register, 72-invariant-subspaces-string**, the notes prove the invariant-subspace classification in the recorded chain frame, compute its exact count, and check all subspaces in six finite-field parameter grids. The 178 parameter choices require 24,012 subspace tests; every computed classification and exact-count comparison agrees with the proof, while 24 choices fail the literal minimum criterion read on scan 081. The smallest displayed characteristic-two counterexample has \(n=2\), all \(\mu_i,\beta_i=0\), and precisely
\[
0,\quad\langle a_2\rangle,\quad
\langle a_1,a_2\rangle,\quad
\langle a_0,a_1,a_2\rangle,\quad E.
\]
These conclusions concern the explicit frame; the excerpted Hua entry is truncated, and its full formal admissibility predicates have not been inspected.

### The calculation folders and the second bridge

The enumeration sections catalogue determinant permutations, gap coordinates, continuant and parity polynomials, pairing matrices, dual bases, vectors, norms, centred coefficients, and documentary lists. Their scripts retain formal polynomial inputs and literal-reading residuals separately; the source-ordered register records the exact passages, including sign, exponent, index and normalization questions. Numbered prose cases and parameter families have their own 31-row catalogue, with totals and concrete evaluated dimensions.

For the split conic \(x^2+yz=0\) arising in the matrix example, the B12 appendix supplies explicit inverse maps to \(\mathbf P^1\), an isomorphism of its even Clifford algebra with \(M_2(R)\), the matrix-unit proof of the Azumaya action map, and the inverse correspondence with rank-two right ideals. This resolves the split construction used here; the planning question about all twisted forms still needs its general descent data.

## How to navigate the complete notes

The following sections include the short research items and their full proof appendices, so this file is usable without opening its component drafts. Each short item gives a scan, a brief source quotation, its kind, and its relation to the supplied context; longer proofs are labelled as appendices or calculations. The context-search CSV records the per-item searches, while the bibliography gives primary-source URLs and sections.

1. **Steps marked unverified by the author:** ten literal question marks, the opening doubt, and the parity-unification request.
2. **Documentary sheets and titles:** all four covers, page-number counts, six reused sheets, and concrete follow-up tasks.
3. **Definition and modular comparison:** B5, exact maps, kernel and support fibres, finite counts, and context statuses.
4. **Source-ordered research register:** individual findings from scans 035–081.
5. **Enumeration catalogue and proofs:** every listed calculation, the 31 prose-case rows, and the exact polynomial conventions.
6. **Automorphisms and quadrics:** ring-level proofs, characteristic-two examples, and their reading consequences.
7. **Invariant subspaces:** classification, coincidences, exact count, finite enumeration, and the five-space counterexample.
8. **Split Clifford and conic calculation:** the explicit B12 maps.
9. **Reproduction and validation:** commands, computational scope, and the limits of mechanical checks.

All prior-run statuses retain their supplied attribution. A cancellation records a change in the manuscript; it does not by itself prove a mathematical assertion false, and the cancelled irreducibility passage on scan 081 is explicitly checked on that basis.
