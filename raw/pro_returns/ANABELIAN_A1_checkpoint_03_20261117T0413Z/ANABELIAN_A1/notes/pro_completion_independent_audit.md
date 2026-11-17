# Independent audit of B.PRO1–B.PRO3

Literature auditor, 17 November 2026. Parent requested special scrutiny of compact strictification, slice effectivity, and the single-stage Kummer equality. I read the complete current `sections/B_pro_completion.tex`, focusing on these points, and found no remaining blocker in B.PRO1–3.

## Exact primary-source check

Carlson–Haine–Wolf, https://peterjhaine.github.io/files/reconstruction_of_schemes_from_etale_topoi.pdf, reopened as `turn130view0`, exact Appendix statements `turn130view1` and `turn130view2`:

* Theorem A.8: for qcqs schemes X,Y and a coherent geometric morphism X_et -> Y_et, inverse images of quasi-compact separated étale schemes are again quasi-compact separated étale schemes; the geometric morphism comes from that site functor.
* Corollary A.9: topologically noetherian X and qcqs Y suffice to make every geometric morphism coherent.

These match the proof's actual source and target hypotheses. No pinnedness is required at the individual finite levels for this application.

The prior independently verified Hoshi–Tsujimura Corollary 4.5(3) applies to every finitely generated characteristic-zero field F: spread its finite set of field generators over Z, choose a closed point in a positive-characteristic fibre of a nonempty integral model, and localize there. This is a noetherian local mixed-characteristic domain with fraction field F. Hence G_F is slim. For a connected finite-type X_E, its arithmetic image in G_E is open; the relative algebraic closure of F in the finitely generated extension E/F is finite, so the image of G_E in G_F is open as well. Thus the structural 2-cell of a relative representative over BG_F, when it exists, is unique. An absolute comparison is consequently automatically relative.

## B.PRO1: compact coherence

For qcs separated étale schemes U,V over reduced noetherian X, Isom_X(U,V) is finite. Their fibres over the finitely many generic points of X are finite étale schemes. Every component of U meets one of those generic fibres by flatness, so these fibres are dense in U. A map to the separated V is determined there, because U is reduced. This proves the required finiteness, including reducible X and nonproper étale U.

Natural isomorphisms of the two inverse-image functors form a closed subset of the product of these finite isomorphism sets: each naturality equation is a closed coordinate condition. Relative conditions and cocycle equations are likewise closed. The composition and restriction operations are continuous in these products. All categories may be replaced by small skeletons, so the compactness product is over sets.

For a finite collection of comparison and cocycle requirements, choose one target field J containing all relevant fields. Ordinary pro-compatibility supplies whole geometric-morphism comparisons of the J-representative with all the finitely many lower representatives after a common finitely generated source refinement. Their induced pairwise comparisons satisfy all those cocycles. Hence the finite-intersection property holds, and compactness produces a coherent family over k. This derives coherence instead of assuming it.

The proof's extra restriction to the closure of comparisons descending as whole functors is essential and sufficient for slicing. For a fixed target étale object V, the selected comparison component at V is one coordinate in a finite discrete isomorphism set. Any point of the chosen closure has that component equal to the component of one whole comparison descending at a finite stage. An individual chosen étale-object identification is finitely presented and therefore descends as well. After another common refinement the two components agree at that stage. The descending whole natural comparison consequently induces a comparison of the **entire slice functors**, with the fixed slice source. Naturality on all slice objects comes from that whole comparison, and does not require separately descending infinitely many components. This addresses the apparent effectivity risk.

Finite constant extension uses a finite extension L0/F0 with kL0 the desired finite extension of k. Fields F'L0 form a cofinal subsystem. Relative morphisms pull back the corresponding finite étale arithmetic object correctly; one selects the component specified by the actual embedding into kL0. Thus this operation remains in the ordinary pro-category. Open restriction and scheme precomposition cause no additional difficulty.

Finite diagrams and finite covering families in the qcs étale site descend by finite presentation. The resulting coherent inverse-image functor is left exact and covering preserving, and hence defines a geometric morphism. Its pullback on open subobjects is the original inverse-limit map. Thus the pinnedness assertion is justified without assuming any finite-level representative is pinned.

## B.PRO2: points and one field for all Kummer levels

A pinned pro-point has a closed limit point y. A finite closed subscheme containing it descends, so y_F is closed at all sufficiently large target fields. Every representative BG_E -> Y_F has precisely that underlying point. Its inverse image of the complementary open is empty, so it factors through the closed étale subtopos BG_{κ(y_F)}. Because κ(y_F)/F is finite separable, morphisms to this subtopos over BG_F are classified by F-embeddings κ(y_F) -> E, equivalently by E-rational points of that finite étale F-scheme. The uniquely specified relative structure rules out an ambiguity from absolute conjugacy. Ordinary pro-compatibility therefore makes all these representatives agree with one actual k-point, and proves uniqueness of the pro-morphism.

For the Kummer assertion, base change to kL and compose with the given point. Its actual value b belongs to kL. Choose a finitely generated target field H containing b and all earlier data. At that level the pro-point's image is the H-rational point T=b. After one source refinement it is the constant-point **geometric morphism**. Pro-compatibility with the original representative is an isomorphism of whole geometric morphisms after one common finitely generated source extension M. Pullback of every universal Kummer torsor along that single isomorphism yields equality at all n simultaneously. The argument does not use a sequence of fields M_n or equality only on G_{kL}. This is exactly the strong conclusion required later.

## B.PRO3: saturation and the relative algebraic closure

The valuation argument on a normal projective model of B over the relative algebraic closure A' of A forces all divisorial valuations of b to vanish, hence b is a global unit and belongs to A'. The root criterion makes the map from the Kummer completion of A' to that of B injective. Norm then gives d ξ equal to the class of an actual element of A.

The elementary saturation calculation is valid: if dη=0, a representative a at level nd satisfies a^d=c^(nd), so its image modulo n is represented by a d-th root of unity. Compactness of the finite set μ_d(A) gives one root representing η at every level. If dξ=κ(a), reduction modulo d first gives a=c^d; the previous torsion calculation makes ξ itself the Kummer class of an actual A-element. Injectivity over finitely generated characteristic-zero fields finishes b∈A. No false finite-generation assertion about A^times is needed.

## Two minor editorial observations sent to the parent

1. In B.PRO4's treatment of x∈X(kbar) with a chosen field L/E which may be transcendental, first refine the representative from E to L in the pro-system over kL. Then x is L-rational on X_L, so B.PRO2 applies with identity finite extension over the new source field. This makes the reuse of B.PRO2's finite-extension formulation explicit.
2. The displayed text `b in L^times,qquad` was missing the backslash on `qquad` when first read. This is typographic, not mathematical.

The parent independently owns B.PRO4–5 review. My reading of them raised no further issue, but the approval here is specifically of the compact coherence, slice effectivity, pro-point, single-stage Kummer and saturation arguments above.
