# Part B work log

## Scope and status

Part B(a) has a proved geometric framed model, tensor map from flags to edges, finite free sign action, exact half-turn presentation in trivalent charts, and the correct leg quotient to the node-only link. Part B(c) is written out for all stable graphs and all boundary flags in types (1,1) and (1,2). Part B(d)'s finite numbers and orbit correction are proved from the original scan and independently enumerated. The early four-point generator dictionary is now complete in B.16–B.17. The literal global colimit of cote146/100 and complete relators/relative-dimension≤1 words for the1620 actual five-point arrows remain explicitly open in B.8 and B.15. Abstract existence of a finite colimit with fully specified algebraic word maps is proved in B.8a and is not substituted for the original index.

## Direct source checks

- Read cote146 scans3–18,27,29,31,33,43–55,81–100,103–110,114–125 in the supplied transcriptions. Administrative versos are not used as mathematical evidence. The working notes on those passages were consulted only as leads.
- Original cote146/100_a and100_b inspected: right-pointing colimit arrow, inserted μ-free wording, rigid/ordered-tree index description and leg quotient. The later trivalent presentation at115–117 is mathematically proved independently, but those folios were initially available only as transcription.
- Read the exact STRATA F.17 statement and proof. Opened Bakalov–Kirillov math/9809057; read boundary conventions and marking definitions, Remark4.3, Sections4.5,4.7,4.10, Theorem4.9 and the genus-zero proof in Section6. The comparison functor is the equivariant path groupoid to BΓ; the plain marking path groupoid alone is contractible. B.14 writes a complete five-point pentagon relation by F-move words and its homotopy.
- Opened and downloaded Labruère–Paris, AGT1(2001)73–114. Read Propositions2.10,2.12, Corollary2.11, Theorem2.13 and the specialization of Theorem3.1 to genus1, at most2 boundaries. The chain relation gives(ab)^6=z1 and(abc)^4=z1z2. Independently derived the same stack groups from monic cubic and quartic configuration quotients.
- Downloaded the original cote148 PDF from the Montpellier archive in HTTP ranges after a full transfer stalled. It has72 PDFpages. Native images of31 and33 were inspected, with central and numeric crops. This found an actual endpoint error in the supplied TikZ: γ_r^2 starts at IIIprime2, not III1. It also found the struck word orbites beside14 and the incompatible3×40 annotations in the360-arrow row.

## Exact finite computations

`code/b_finite_checks.py` enumerates all120 permutations, nine vertex coset sets and fourteen named edge families; output is `code/b_finite_checks.out`. It produces542 vertices,1620 arrows,9 vertex orbits and16 edge orbits, and certifies connectedness and free rank1079 for its endpoint realization. The subgroup calculation for the actual I6/I4 incidence gives the same connectedness argument in B.13. `code/b_diagram.json` retains every enumerated vertex and arrow; its scope states that it assigns endpoints and valencies, not geometric path classes.

The same program enumerates stable labelled multigraphs. Counts: (0,4):4; (0,5):26; (1,1):2; (1,2):5. Trivalent framed chart counts are96 objects/480 positive half-turn generators for(0,4), and1920/13440 for(0,5). These are disjoint-chart counts, not counts for an unconstructed global quotient. Node-only chart counts are6/6 and60/120. It also checks the finite coequalizer obstruction to preservation of free actions.

`code/b_braid_checks.py` evaluates all needed low-genus braid identities in the Artin action on free words. Twelve checks pass, including Δ²=δ⁴, the two-node exchange byδ², r²=δ⁴, h=ac^{-1}r, and the capping compatibility. The geometric proof establishes the maps independently; the code checks their exact words.

## Corrections and proof boundaries sent to root

1. S0 retains tangent directions at marked legs; the comparison with S_AΠM_G is a quotient, with kernel Z^I, already visible for(0,3).
2. Arbitrary finite colimits do not preserve free finite actions. A completely defined boundary-incidence interpretation at(0,5) gives the boundary3-manifold group and fails to give the open group; this does not refute an unspecified original index.
3. Low-genus pinned and mixed groups are kept distinct. In the two-edge cycle flag the graph involution swaps the smoothed and retained edges, so the chosen crossing uses the index-two stabilizer, not the whole mixed link group.
4. Cote148 has14 named families and16 actual S5-orbits. The word orbites next to14 was struck out; do not attribute the corrected claim to an unqualified surviving assertion.
5. The endpoint error for γ_r^2 and the inconsistent3×40 counts are recorded with direct scan evidence, not silently normalized.
6. Independently checked root C.8: its three point-pushing words match Artin half-twist conventions and their normal quotient is C2. Suggested distinguishing the original discrete Z images from their procyclic closures/completions.
7. Supplied the exact pure Dehn-twist generation reference (Labruère–Paris Corollary2.11(i)) to the levels agent, including its proof pages.

## Unfinished attacks retained

The four-point notes27–33 do contain mixed/fibre/transport relations. Several indexing permutations and the selection of the finite object torsors have not yet been reconciled with the original diagrams and the later conventions90–100. The next task is to reconstruct those actual paths and transport them into the braid/marking presentation, then extend the same dictionary to the f and γ families at five points. No count-only coset model is asserted to determine homotopy classes or to solve those relations.


## 2026-11-15 10:51 UTC — complete early four-point reconstruction

B.16 gives an explicit arrangement model of the thirty objects in cote146 scan27 (folio26): six chamber Q points, twelve near-wall R points, and twelve pole P points. Four families of twelve arrows give48 essential generators; the source's auxiliary30 full turns and18 half turns expand this to96. Twelve mixed relations and six length-three half-turn equalities reduce to the six-object A2 chamber groupoid. Contracting the stated five-edge tree produces explicit words in A,F,t and exactly the relations[t,A]=[t,F]=1. The path formulas, mixed homotopies, half-turn homotopies, and braid-diagram completeness argument prove an equivalence with the fundamental groupoid of the three-line complement; projectivization kills exactlyt and givesM0,4. The positive a crossing is matched to the inverse of the source's oppositely directed a with changed index, rather than silently changing orientation.

Program code/b_four_point.py enumerates all30 objects and48 essential arrows, records all18 typed equations, verifies both endpoints and the resulting F(A,F)×Z words, and checks all12 pole full turns. JSON contains the explicit generator and relation data; the text output records30/48/96. B.17 takes the precise free-sign induction along diagonalZ→Z4 and obtains240 objects,1104 essential generators,1488 expanded generators. This is explicitly the induced early model, not an unspecified unique global object count. Canonical inversion L×→(L∨)×, v↦the functional evaluatingv to1, reverses integer inertia and fixes μ2; it tracks the opposite scalar convention.

New primary images visually inspected:146/20,27,31,33 correspond to folios19,26,30,32;146/53 isfolio52 and visibly underlines the opposite scalar action;146/100 isfolio99;146/115–117 arefolios114–116. The original115 hatted coordinate product versus bare-A cardinality annotation remains recorded, while the correct E⊔I count is proved. The original116 cocycle and117 square/full-turn relation match the independent cubical proof. B.8/B.15 updated so they no longer list the completed early four-point dictionary as unresolved. The general scan100 index/transition functors and five-point actual1620 geometric path dictionary remain explicitly open. Metadata now18 results/14 reading rows.

Primary comparison source: Salvetti–Settepanella, Combinatorial Morse theory and minimality of hyperplane arrangements, Geometry & Topology11 (2007), Section4.1, https://msp.org/gt/2007/11-3/gt-v11-n3-p14-p.pdf. The cell presentation is additionally proved directly by generic braid diagrams, so the result does not depend on a merely quoted homotopy assertion.


## 2026-11-15 11:06 UTC — exact higher-point braid dictionary

B.18 constructs a specified finite chamber groupoid for M0,n: objects are the(n−1)! real orderings, arrows adjacent positive normal half-turns, relations lifted commutations and braid equations, plus one full scalar turn killed. The program computes counts6/12/6+1 for n4,24/72/72+1 for n5,120/480/720+1 for n6. These counts are explicitly not the542-object source diagram. Every generator is conjugated along a canonical insertion-sort permutation braid, its central power is removed by linking number12, and its pure word is combed via last-strand deletion and the conjugator of the last peripheral free generator. The fibre conjugator is an isomorphism on the point-push free group; the proof identifies the actual inverse. All564 arrow words were checked exactly in Artin's faithful action; JSON records each one.

B.19 independently derives the exact P5c2/P5c3 presentations from split configuration fibrations, verifies all6 and26 relations by their braid words, constructs inverse fibre automorphisms by inverse-braid conjugation, and checks the24 base-relator actions on F4. An initial attempt to use a mirrored-word convention without accounting for composition order failed; it was replaced with direct exact inverse conjugation and both inverse identities were checked. No failing mathematical claim entered the paper.

Opened the original Fadell–Neuwirth paper through the journal's migrated download URL https://journals.msp.org/mscand/article/download/2674/2673/2705 ; visually read Theorem1 on p111 and its local-triviality/section proof on p112. The old mscand.dk URL now returns404. Download and two rendered proof pages retained. Also opened Luo's arXiv:math/9904020 Lemma2.1(a) for the levels agent: the actual branched-cover curve-complex map C0,5→C1,2 is a disjointness-preserving bijection.


## 2026-11-15 11:14 UTC — geometric five-point core

The untranscribed original148 leaves1–28 were sampled directly, including18,21,24,27: these continue the four-point polyhedral and sewn models. They did not supply the missing five-point path labels. Original scans38–39 (folios37–38) were then inspected. The involution family has quartic z^4−μz²+1; its discriminant16(μ²−4)² corrects the extra exclusionμ=0 on original39 for the stated framed moduli problem.

B.20 realizes all60 f_B,s incidences by K(r)=(∞,−ir,ir,−1,1),1/√3≤r≤1. The initial bipyramid is transformed by(z+1)/(z−1), the terminal configuration is square-pyramidal, and the common involution gives the exact S5/D3←S5/C2→S5/C4 endpoint diagram used earlier. b_quartic.py verifies all transformations and60 coset paths over exact algebraic numbers. The source has not stated enough path data to identify this realization with every unstated convention for the other1560 arrows.

An exact computation of this core's braid images is in progress: rational-curve to polygon homotopies are certified by half-plane/Sturm tests, and all projection crossings use Q(√3) arithmetic. This is an attack on generation and relators for the actual core incidence, not a substitution of the chamber object set.


## 2026-11-15 11:48 UTC — complete geometric core and one-node extension

B.21 gives all11 core cycle words, their exact images in a,b,x,y,z, the short inversea=g11,b=g11^-1g3g2^-1,x=g2g6^-1g2^-1,y=g2g4^-1g2^-1,z=g2, and12 defining relators. All60 rational paths have a one-chord collision-free homotopy. A uniform analytic proof bounds the argument by6 arctan(2/11)<π/2;360 exact Sturm pair-difference certificates verify it independently. Weighted Stallings folds independently find the full F2 base and F3 fibre. The core comparison is an equivalence, with a proved inverse, not only a surjection.

B.22 supplies a one-node extension: q=ε=1/10 andiε represent right/left square–triangle objects in the plumbing zv=q; real erasureto√5−2 yields a regularpentagon, imaginaryerasuretoi/√3 yields the bipyramid, andpositivequarterrotation givesτ. The120f_Q,a paths are explicitlydefined as imaginaryerasure then an other-apex corepath. This convention is not equated with any unrecorded directpathhomotopy. The resulting182objects/360arrows have179freecycles and180complete relators. All path images and every new relation were computed exactly; the remaining1260 source arrows are not assigned.

B.23 proves the actual four-point relation: q²=lambda is a two-sheeted cover ofM04, and z²=w branchedat0,infinity, retaining thefourlifts plusinfinity and forgettingtheunmarkedbranchpoint0, givesV(q) inM05. It computes the three meridians as σ2²,σ1²σ3²,σ2σ1²σ3²σ2^-1 and their normalizedpurewords. This realizes everyarrowof the360subdiagram through liftedfourpointpaths; it does not silently identify thatcoveringfunctor with an unspecifiedsewing-onlyinterpretation.

The original148scans19,20,22,23,25,26,28 were inspected: theydevelopfourpointpolyhedra,ellipticcovers,andmarkedpants;22isadministrative. Original54 and59–60 definegommageandsewing on full marked surfaces, but do not yet resolve the finiteIII1→II1 threefoldchoice or all its path words. This is the current main obstruction.

## 12:05 UTC — verified two-node extension

B.24 and code/b_second_tier.py complete a specified 422-object, 1020-arrow realization, with 599 graph cycles and 600 relators. All 660 new path images, 724 strict-half-plane rational subintervals and 420 new relations passed exact checks. The lower triple-triangle twist in original scan31 supports one quarter; two independent readers compared its glyph with the upper quarter. The supplied one-third alternative remains in the reading register.

The six endpoint maps retain their exact relabelling permutations. One prospective linear erasure crossed the retained central node; it was replaced before use by a real-chamber path with a retained disc of radius1/4 and separation greater than12/25. The combined marking erasure in gamma_r^2 and the simultaneous two-cut path are explicit conventions, not inferred from counts. The three tetrahedron-triangle families remain.


## 12:52 UTC — complete specified 542-object model and strict colimit

B.25 completes all 542 objects and 1620 generating paths in the specified realization. The graph has 1079 independent cycles, and 1080 explicit relators give its full fundamental groupoid. Forty-three universal exact determinant certificates cover all 600 newly added path images under all 120 label permutations. The 480 new relators pass faithful Artin-action checks. The earlier per-permutation Bernstein run is retained as an explicitly aborted work file; the optimized universal-certificate program b_third_tier.py is the executed result. The original direct-fQa, retained-pin and three-tetrahedral-pin choices remain separate comparison questions. B.26 proves that 1080 relators are minimal for this fixed generating graph, using H1=Z5 and H2=Z6.

B.27 gives an actual strict finite colimit of framed groupoids, with the full finite face-occurrence category, explicit pseudofunctor cocycle, finite strictification, and functor/inverse through the action-path groupoid. Its primitive types are (0,3),(0,4),(0,5),(1,1),(1,2). The external half-turn action stays free because the strictified colimit objects retain their initial block and sign. Genus-zero indexing is the finite reduced-labelled-tree poset. This closes the corrected five-type geometric reconstruction; the original stronger sphere-three/four-only geometric factorization remains in B.8.

B.28 supplies the exact capped genus-zero sewing dictionary: parenthesized pants, four-hole F moves and cherry half turns give 12 objects/18 arrows/7 relators for M04 and 120 objects/264 arrows/169 relators for M05. Explicit mutually inverse chamber functors are verified in b_parenthesized.py. Every B.21--B.25 based braid word therefore has an explicit F/B replacement. This statement does not identify unrecorded original tangent-ray transports or elliptic S-move coherence.

The genus-two companion programs b_genus2_checks.py and b_genus2_faces.py verify respectively 21 literal B6 identities and all 42 face maps (178 generator images) of the 19-cell P2 model. The 24 coherence triangles have exactly one nonidentity conjugating twist, v on DBN--BN--N. These proofs and six stabilizer presentations are owned by D.27; no duplicate B result is claimed.


## 13:14 UTC — sphere covers and complete elliptic framing dictionary

B.29 and b_sphere_covers.py complete the cubic and quartic covering functors, their inverse constructions, and the finite mixed sphere presentations. Their counts are 2 objects/3 arrows/1 relation and 5 objects/11 arrows/7 relations. All seventeen displayed braid and flag identities pass faithful Artin-action checks. The cubic framing correction is essential: the disk full twist h=(ab)^3 satisfies elliptic boundary z=h²; the free ray model has positive half turn τ=hω with the natural deck arrow ω of order two. The S cut change is aba, with S²=h and S⁴=z. The quartic induction sends its full twist to z1z2 and retains both independent half turns.

Independent checks for D's full (1,3) model are retained in b_d4_tail and b_d4_parabolic. The latter extracts exact parabolic words by orthogonal positive-fraction reduction and checks every returned word. I checked the mixed-B4 nonseparating cut model, all six generator images, the tail lantern conjugator q2 D1 q2^-1=D0 D3^-1 D2^-1, the three previously missing coherence words, all 28 local group types, and the puncture/edge-position table. Loop branch flips are retained inside the local groups despite acting trivially on edge masks.


## 13:23 UTC — explicit sphere-only colimit on elementary blocks

B.30 replaces the large free-group placeholder in B.8a by an actual finite diagram whose blocks are only induced three- and four-point models. Variable blocks have a specified idempotent killing a dummy generator; multiplication blocks impose each prefix product; terminal maps impose the exact central relator value. Every arrow targets a rank-two free group and is explicitly t↦u, v±1, uv, or a central winding. These functors are realized by the concrete two-loop spine of M04 and the identity on the framing torus. Elimination gives an exact inverse to the geometric group, and identity sign-object maps prove freeness. The low-type programs verify 99/40/63 four-point blocks for05/11/12, including cubic/quartic nonzero framing vectors. A finite-coproduct pushout gives a genuine three-object ordered index. B.8 is now narrowly the unidentified individual assignment in the original reduced-tree phrase, not the finite-colimit existence statement or elliptic coherence.


## 13:38 UTC — all path choices compared with explicit inverses

B.31 proves the exact change-of-path theorem. The1068 arrows outside the fixed60-arrow core and541-edge tree are parameterized by independentΓ05 difference loops. Core normal forms give invertible Nielsen substitutions and their exact inverses; all1080 relators are transported. Tree transports extend the comparison to changed incidence endpoints or pins. B.15 is now Proved in this choice-independent sense, with the additional gommage-equation test stated explicitly.

The executed b_path_change program supplies a concrete second S5-equivariant realization by inserting the positive q=0 meridian into all120 f_Qa arrows. Sixteen universal determinant intervals certify all60 source meridians; each has nonzeroH1. Every displayed fractional-twist arrow and endpoint germ remains fixed. All1620 generator inverses and1080 transported relators are checked. This demonstrates nonuniqueness for precisely the listed diagram data and makes no claim that an additional unrecorded marking-forgetting equation is preserved.

## 13:52 UTC — E.38 and source-status closure

Saved `sections/E_adjacent_presentation.tex` and its B-register row. The all-multicurve category has an explicit adjacent-deletion/endpoint presentation with a right-coset normal form and inverse. Skeletal descent transports every actual pin. Finite endpoint/biset assignments with transported diamond equations are exactly image finite categorical quotients; this proves the universal profinite comparison. Root independently audited the proof. Corrected the E.148 set brace and E.149 roman subscript and split E.147 before compilation. B.8 and B.15 now record proved mathematical constructions; remaining historical assignment uncertainty is retained in the reading register.

## 14:48 UTC — E.44 finite subgroup descent

Saved E.44 with tags E.210–E.219, full proofs and metadata. The ten-point V4 construction supplies two actual finite-choice forgetting maps to the same effective four-point orbifold. Their coordinates and surjectivity prove J=id. The source p=2 theorem was independently read by root/E/D; its application is to the whole V4 subgroup. Both pure conjugacy classes are retained, with their difference killed by forgetting C1,C2. The centralizer comparison is proved by the actual F9-normal-in-F3 covering extension and punctured DNB, then the explicit generic-four cross-ratio. Executed b_branch_descent.py; all finite permutation/rational checks passed. Source PDFs for Schneps2006 and LNS2026 saved; Kerckhoff primary pp236–237 opened and visually inspected.


## 15:30 UTC — E.49 and the exact CM parity restriction

Saved E.49 (tags E.254–E.269), now Proved after independent root/E/D audits. The construction uses a free C3² translation orbit, successive order-two lift groupoids, the actual twelve-point elliptic / eight-point sphere centralizer, and the named E44 five-point comparison. The monic division quartic preserves its two ordered poles under every affine coordinate change and root relabelling. Its rigidified source and CM target are explicitly isomorphic stacks. The source commutator module and the named target pointpush generator fix the signed normalization and reduce the comparison to one global C6 exponent. This proves Delta|GT=0 and excludes the E46 witness from GT. All algebraic and module certificates passed. A standalone six-page LuaLaTeX check has no overfull boxes; its expected missing bibliography warnings are confined to this syntax-only build. The initial XeLaTeX attempt could not find its runtime format and made no mathematical check; the installed project Lua runtime completed successfully. Provisional proof/memo copies are retained under agents/history.

Independently audited E_finite_lifting_candidate Sections1–4: finite implementer extensions, modular torsion source maps, the scalar character count, all-subgroup transport, Möbius inversion, compactness, and the actual E58 frame construction all pass. This audit proves the GT0 witness and does not infer its pentagon from a finite quotient. E49 supplies its exclusion by a separate exact comparison.


### Exact witness membership tests

For E46, rho=0,T=5I,W=I forces source M=I mod4 and identity on its minus-eigenline mod3. The E49 homological naturality equation requires one k in C6, but its mod4 specialization forces even k and its mod3 line forces odd k. This is an explicit failed finite shadow of the named torsion-configuration diagram. Consequently the pentagon and full ordinary-tower extension fail, while inertia/S3/multiplier1/peripheral-H1 tests pass. Vanishing of Delta has not been claimed sufficient for GT membership.
