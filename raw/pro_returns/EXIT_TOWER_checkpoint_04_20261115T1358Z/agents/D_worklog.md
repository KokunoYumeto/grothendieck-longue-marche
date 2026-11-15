# Part D work log

Started 15 November 2026. Files read: attached EXIT_ONE_TYPE review §4 (Theorem R); original levels.tex results P5b2/P5b4/P5c1 and proofs; LM5 F.40–42; LAMBENCY_IN_AG_20261114.md. All are treated as claims.

## Current verified calculations

For a nonempty multicurve σ on S_(g,n), let v0 be the number of genus-zero components of the cut surface. The link is the join of the curve complexes of its components, and Harer's sphere dimensions give link sphere dimension 2g−3+n−v0. This exact formula warns that the proposed connectivity bound requires more than the rank deletion estimate asserted in the prompt.

The compactification-independent archimedean end system is established directly by N ↔ X\N: compact Hausdorffness identifies punctured neighborhoods with U\K for compact K⊂U. Oriented-blow-up collars identify a constant homotopy model for normal crossings pairs.

## Searches run

Web searches: curve complex rank selection / truncated pants complexes / Harer sphere dimensions. Primary sources to open next: Harer 1986; Hatcher pants decompositions; Boggi–Farb–Lochak procongruence curve complexes; Svaldi Mori hyperbolicity; toroidal factorization.

## Pending

Check Theorem R dependencies and low genus connectivity; derive exact boundary comparison; finite stable-graph/tropical map; run 23 modular dessins computation with primary CDH data; all unresolved claims remain unproved.

## Verified checkpoint

D.1--D.15 now written. The end comparison and low types, all four requested rank-selected cases, the corrected uniform link bound, projective Theorem R, finite-level completion, the complexity-two counterexample to the printed Kent range, all 23 lambencies, and the complete low-strata enumeration have been worked through. Primary sources and exact opened statements are recorded in D_references.bib. All listed computations were executed and their outputs saved under code/d_*.out and code/d_*.json.

The all-genus stronger rank-selected claim remains open in D.7: the first unresolved type is P_3 for (3,0). The exact boundary map between the rank-one and rank-two link Steinberg modules, rather than the incorrect dimension estimate, is the remaining issue. No general equality is inferred from a finite quotient.

A separate source audit found the finite-centralizer assertion in Boggi, Congruence topologies, Lemma 6.7 false for the characteristic mod-two homology subgroup. code/d_hyperelliptic_counterexample.py computes the resulting elementary-abelian centralizer. A different closed genus-two transfer through Proposition 2.4(ii) and Corollary 4.7 is being checked independently of that lemma.

Still being added: reconstruction from the complete face/collar diagram, five explicit depth-three complex-of-groups cases, graph/tropical comparison maps, and the source-audit correction just described.

## Reconstruction and comparison checkpoint

D.16 proves the given collar/face reconstruction by the actual angular quotient, including all four requested examples and both relevant fundamental-group filtrations. D.17 gives the five depth-three stratum tables, the node-normal bundles and Euler classes, flag stabilizers, and transport twisting words; it states the remaining five-/six-point finite word dictionary as open in B.8/B.15. D.18 constructs the graph-category homotopy-colimit map to the symmetric boundary complex and volume-one tropical space and computes its actual point fibres. Both CGP primary definitions and Theorem 6.1's proof have been opened.

Theorem R now explicitly proves the supporting-prime purity statement on a general transverse slice, contraction of every non-Rees exceptional subtree, intersection of monomial valuation ideals at a special triple point, and weak factorization relative to the endpoint Y.

The additional exact quotient-poset homology computation d_rank_quotients.py was executed. At (3,0), k=3, the finite type-poset has cells (34,148,208,93) and mod-two Betti numbers (1,0,0,0); it cannot detect the proposed actual rank-selected second-homology obstruction. The remaining genus-three map is being reduced to an incidence-system colimit of genus-two Steinberg modules.

## Independent low-genus completion proof

D.19 now proves the closed genus-two congruence transfer using HM2011 Theorem 6.1 (FC-admissible configuration restriction at n=1), the full configuration exact sequence, and Boggi2009 open CSP. The lift is adjusted by an element of the configuration group to centralize that group; its once-pointed image acts trivially on the punctured-surface group and is killed by open CSP. Agent E checked the exact morphisms. Neither Boggi2020 Corollary 4.3 nor Lemma 6.7 is used.

D.20 gives two exact counterexamples to those printed claims: the mod-two homology-cover finite centralizer, and the unequal-weight two-twist product whose handle swap changes its mod-three homology matrix. The program was rerun with both examples. D.21 transfers the profinite pentagon obstruction to (1,2) via Luo Lemma 2.1(a), whose map and proof were opened, and the explicit index24 pure-braid subgroup from B.9. All genus-at-most-two finite-level/procongruence comparisons and their connected one-type ranges are now settled. Higher profinite connectivity is not asserted.

## Rank-selected conjecture resolved by a retraction

The previous genus-three coefficient-system investigation has been superseded. For every g≥1,n≥2, filling one puncture gives an order retraction from P_(d−2) onto the curve complex of S_(g,n−1), with section obtained by adjoining the fixed boundary of a twice-punctured disk. At most one curve of a multicurve can be killed: disjoint such disks would be nested, either forcing three punctures in the outer disk or giving isotopic boundaries. Thus every multicurve with at least two members has nonempty image. All one-curve links have dimensions h or h−1, proving the lower bound h−2; the retract has nonzero H_(h−1), proving exactness. The corrected min(k,h)−1 conjecture is false for every g≥2,n≥2 at k=d−2, first at (2,2,3). D.7 is now Refuted; exact replacement proved.

The earlier finite quotient computations remain useful evidence: the (2,2),k3 quotient has no reduced mod-two homology despite the actual complex's split infinite-rank H2. The investigated genus-three Steinberg-module cokernel was not evaluated and is no longer necessary to decide the proposed bound. No claim about its value is made.

Second independent attack on Theorem R checked the logarithmic discrepancy identity, the normalized-graph ampleness/finiteness argument, possible nonmonomial centers contained in boundary, non-Rees surface subtrees, possible finite monodromy of Rees fibres, special triple points, and the relative-to-Y weak factorization. No further obstruction was found. The ray-extraction Euclidean descent and the ordered-path monodromy argument have been made explicit in D_projective.tex.

## Final direct facsimile and definition check

Viewed MPL150 scans 32, 34, 35 and MPL147 scan 60 individually. The intersection formula on scans 34--35 is explicitly the union over all common lower indices, not a single infimum. Scan 60 explicitly identifies the four modular-dimension-at-most-two elementary types and qualifies the proposed general extension as an impression. Added precise reading records, retaining overwritten labels as unresolved. Clarified the opening definition in D_projective.tex to include U among the aspherical strata, exactly as the attached original definition requires; this is needed when invoking Mori hyperbolicity and Svaldi. Reopened Matsuki erratum section 2: it explicitly states that all intermediate embeddings are toroidal over Y, and gives the relative fan construction, confirming the goodness transfer through blow-down steps.

## Independent E audits

The full audits of E.13, E.18, E.T6 and E.20 are saved in D_E_cross_audit.md. The E.13 Hurwitz fibres and subgroup-reconstruction maps check; the exact Ivanov finite-index rigidity theorem was read in the facsimile; the unpointed elliptic torsor calculation checks; and the real genus-three centralizer proof checks after spelling out the intrinsic real-cusp normalizers, their two section flags, and the degree-one local maps in covers pulled back from the filled surface. BZ Theorem A and the order-two proof were independently reopened. The algebraic moduli-stack automorphism audit and exact M1,2 double-cover inverse were saved separately. The Earle--Kra--Krushkal metric source was opened and its checked retrieval saved.

## Complete finite P2 dictionaries in three requested cases

New d_p2_genus_zero.py uses rooted labelled trees, depth-first order, positive permutation braids and zero-rotation cabling. The pure round-system stabilizer is the product of vertex pure braid groups, modulo one global diagonal centre on the sphere. The inverse cabling algorithm deletes all but one strand per block, strips the outer cable, then recurses. It gives each sewing injection in the named target generators. All maps are verified with the faithful Artin action, and B.18 combing gives their exact P5c2/P5c3 words.

Executed output: M0,5 has26 vertices,55 arrows,30 triangles,91 local generators,175 generator-image maps,54 zero-transporter arrows and a25-edge maximal tree using only them. M0,6 has235 vertices,840 arrows,630 triangles,1110 local generators,3570 generator-image maps,789 zero-transporter arrows and a234-edge maximal tree using only them. The pair-divisor node generators are exactly the five/nine compact generators, so the inverse comparison is literal. All261 diagonal central identities were checked. The complete JSON includes the630 open-stratum tetrahedral twisting identities.

New d_p2_elliptic_two.py gives all15 barycentric orbit cells for M1,2: five original vertex orbits, seven edge orbits and three triangle orbits. It lists32 face arrows,18 face triangles and68 generator images. CN and CNO use the index-two group A=<a,c>, preserving the second branch through the C action. Every transport and twisting element is identity. All local relations, injections and composites were checked in B4 modulo its central full twist. The face-cone contraction and the three named generator inclusions give the explicit inverse to the open presentation.

D.22 and D.23 record these proofs; D.24 is the numbered Open row for the full (1,3),(2,0) word dictionaries. The parent additionally identified a precise higher-dimensional task that remains: the630 cocycle identities have been expressed as equal ambient words, but not yet as Peiffer expressions in the26 compact relators with an inverse comparison to the24 identity basis. That remaining chain-level dictionary is retained in D.24. Source freeze was confirmed for the parent’s second checkpoint; no D TeX or metadata is changed during that interval.

## D.26: additional source defect, executed

Read Boggi2014 v5 Lemma5.12 and its proof on printed p26, including the exact preceding invocation in Lemma5.10. Constructed A=diag(I2,-I2), B=block swap in Sp4(Z,diag(J,J)). Eigenlattice-sum indices1,4 obstruct integral conjugacy. Explicit Q has det16, Q^tOmegaQ=4Omega, BQ=QA, so conjugates modulo3. Executed code/d_symplectic_involutions.py and saved JSON/output. Numbered result D.26 Refuted; no inference that separate singleton normalizer conclusions are false. E owner pursuing an independent low-genus peripheral/free-factor proof. Thm4.5 cutting proof is independent of this later defect.

## D.27: full genus-two second-level dictionary

B agent independently derived all6 stabilizers, including the actual central W lifts, the B exchange square and action, and the corrected dumbbell exchange. The19-cell orbit diagram has42 arrows and24 triangles. Its only nontrivial twist isv onDBN→BN→N. B code checks178 local generator images using sphere outer action plusSp4; own d_p2_genus_two.py executes all134 relators in11 local presentations, the18-edge zero-transporter maximal tree, the5 literal inverse generators, graph-rank counts(1,2,2,2), and24 open-cone identities. All data saved, full LaTeX proof D.27 included. D.24 narrowed to(1,3) and compact higher-identity comparisons; no Peiffer basis comparison is claimed for these cone identities.

## D.28: exact(1,3) foundation and partial stabilizers

Opened Soroko2019 primaryPDF Prop8/Cor9 complete proofs and Fig2; exactGamma13=A(D4)/Delta with named twists and capping maps. Opened Dehornoy--Paris1999 Sections7--8/Lemma8.4 full greedy proof. Implemented d_artin_d4.py with192 simples,36864 gcds, exactcentralquotient. Computed22/53/33 flagorbits (108 objects,304 arrows,198 triangles). Four explicit stabilizer families give10 of22 vertices. Verified all pair half-twist squares, exchanges and star comparisons. Also executed the proposed mixedB4 node-sewing homomorphism:11PB relations,6 half-conjugations, central node, fulltwist=a^-2. Full304 namedmaps remainsOpenD.24; no fullN identification claimed at this checkpoint.

## D.29: complete three-pointed-torus dictionary

Completed all22 vertex stabilizers. B independently verified the zero-framed mixed-B4 sewing model ofN, the tail D2,D3 basis from Soroko Fig2, the exact q2/q3 lantern conjugators, and the boundary-retaining Li stabilizers. The full program d_p2_elliptic_three.py enumerates all108 flag objects and304 face transports, then rewrites each injection into the named target alphabet. All922 generator images,126 defining relators of28 complete presentations,198 coherence triangles on594 generators, and198 open-cone tetrahedra execute successfully. Exactly7 twists are nonidentity; their six global values have short local words, including the twoN words hD2^-1,hD3^-1 and the S1 word a3^-1 b^-1 a3^-1 a2 b a3. A107-edge identity-transport tree and the four literal inverse global generators are supplied. Complete readable dictionary and JSON saved. D.29 full proof written; D.24 now retains only compact crossed-module/Peiffer comparisons in the three dimension-three cases.

E.28 independent audit also completed and saved in D_E_cross_audit.md: actual first-strand cabling, orbifold descent, five-point action, permutation elimination and involutivity all pass in the stated scope; J=id on allGT remains open.

## D.30: six-point cellular and Peiffer comparison

Built d_p5c3_fill.py, an exact relator-valued two-stage semidirect normalizer. All26relators,52signed-action inverse checks and20seeded finite contextual checks executed. An earlier optional100word/length18 stress run was stopped when free-word growth became excessive; no claim is based on that interrupted run. The actual8371source-relator certificates all complete and freely verify.

Constructed the complete source groupoid2-presentation (236vertices,2194oriented1cells,8371relators), with235crossing-tree edges and1959generators after collapse. There are1027distinct compact26-relator certificates containing26483factors. All630tetrahedral source identity sequences and all6395boundary2cell prism sequences freely reduce in the fullsource alphabet; mapped identities are literalT T^-1. All24openprism identities mapidentically. Root/B independently audited the scope: the matrix[0|I24] is on630cone+24open selected3cells; local3cells and otherprismaticfamilies remain in the fullmodel.

The decisive geometric model is explicit: L=EΓ×ΓP2, actual Borelcone=M_p forp:L→BΓ. The executed cellular mapf:L→K6 has the exact stated1/2data and extends by K6 asphericity. Its mapping cylinderM_f realizes the same fullcone diagram. Canonical retractionF(z,t)=f(z) forces allprism3cells intoK6² and fixesopenK6, so simultaneous zero choices follow from oneactualmap. D.30written/included andD.24narrowed topositive-genus compact higheridentities.
