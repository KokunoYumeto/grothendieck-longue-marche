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
