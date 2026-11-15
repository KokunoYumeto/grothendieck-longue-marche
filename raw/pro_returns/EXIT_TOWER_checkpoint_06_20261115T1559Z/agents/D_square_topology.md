# Framed adjacent squares: a proposed complete topology proof

Status: independent argument submitted for root audit; not yet a numbered Proved result. It uses the already proved pinned normalization/clutching comparison at a retained multicurve, E.29 for crossings to an open object, E.32 for adjacent flags and their full stabilizers, and E.33 for rational-tail crossings. It does not assume that completion commutes with an arrow category.

## 1. Discrete square and its exact framed transporter

Start with a bordered core and put a rational tripod on each of its labelled external boundaries. Give every tripod two new, distinct external puncture labels; these labels are disjoint from every original label and from the labels of other tripods. Let t be the set of tag curves. Interior core multicurves are essential and not parallel to an external core boundary. Consider adjacent core multicurves gamma0 = gamma1 union {d}, and set

A0 = t union gamma0, A1 = t union gamma1, B0 = gamma0, B1 = gamma1.

Let eta_i:A_i→B_i be the chosen crossing smoothing exactly the tag nodes. A framed adjacent arrow is a commutative square with vertical maps eta0,eta1. Its two horizontal arrows have representatives u:A0→A1 and v:B0→B1. Commutativity says that their representatives agree modulo Delta_t Delta_gamma0 in the transporter from A0 to B1.

Every transporter A0→A1 preserves each tag curve individually. It must carry the curve enclosing the fixed pair of new labels of a tag to a curve with exactly that pair. Among the source curves there is only that tag: an interior core curve enclosing just that attached pair would be boundary-parallel in the core, which is excluded. This also excludes a rational-tail curve already in gamma0; its old label set cannot equal the two newly created tag labels. Consequently u has a representative c in C_t=Stab(t). Equality of the composites makes the representative of v differ from c by an element of Delta_t Delta_gamma0, all of which lies in C_t. Thus v is a framed transporter and determines u uniquely by quotienting out Delta_t. Conversely any such framed transporter gives the square. The exact discrete comparison is

Trans_(C_t)(gamma0,gamma1)/Delta_gamma0 → Squares(eta0,eta1),

c Delta_gamma0 ↦ (c Delta_(t union gamma0), c Delta_gamma0).

It is bijective, with inverse taking the bottom arrow's framed representative. This is an equality of actual transporter sets, not only of automorphism groups.

## 2. End groups and the total composite

Write G_i=Aut(B_i), H_i=Aut(A_i). The automorphism group C_i of eta_i is the framed end group Stab(t,gamma_i)/Delta_gamma_i. In the normalization at gamma_i it is the rational-tail stabilizer, component by component. E.33 therefore gives its full completion and an embedding

C_i-hat → G_i-hat × H_i-hat,

with first projection injective and second projection onto, kernel Delta_t-hat. It also identifies the completed vertical crossing and its endpoint actions. Components with no tag contribute unchanged full groups; finite component and branch permutation groups can be retained after first making all pinnings, then inducing over the finitely many pinning choices.

For the total composite z0:A0→B1, normalize at the retained curves gamma1, keeping every branch pinning. In the resulting product of cut-component exit categories, B1 is the open object and A0 has precisely the residual curves t union {d}. The permitted pinned normalization/clutching comparison identifies this convex portion of the category with the indicated cut-component diagram. E.29 applies there to identify

Hom(A0,B1) on its chosen incidence orbit = (G1-hat × H0-hat)/K-hat,

where K is the discrete stabilizer of that composite, namely Stab(t,gamma0,gamma1)/Delta_gamma1. All finite permutation choices are retained; no use of a two-object nonconvex completion assertion is made.

Both intermediate curve sets B0 and A1 are intrinsically determined inside the source-to-target residual set: B0 drops exactly the distinguished tag curves, while A1 drops the one remaining core curve d. Therefore every automorphism of the composite preserves both intermediate sets. There are no residual swaps between d and a tag because of the new-label argument in Section1. The discrete automorphism group of either specified two-step factorization projects isomorphically onto K. At the discrete transporter level the intermediate automorphism is the same mapping class modulo the appropriate intermediate twist lattice. It exists because the intermediate curve set is preserved, and is unique because the two adjacent/crossing actions have the indicated diagonal stabilizer. Equivalently the full pinned flag stabilizer and the endpoint-pair stabilizer are the same Stab(t,gamma0,gamma1)/Delta_gamma1.

E.32 identifies the completed full flag stabilizers and these projections. The just-described discrete isomorphisms consequently remain isomorphisms after full completion. If the tag smoothing has more than one edge, retain a full ordered flag of its single-node smoothings first; its stabilizer is unchanged since all tag curves are individually distinguished. The result is independent of that order by the natural flag projections of E.32.

## 3. Why completed factorization spaces have no extra orbits

For any fixed finite object list, its discrete composable-arrow tuples have finitely many orbits under the product of endpoint and intermediate automorphism groups. Their types are precisely the finite labelled contraction flags (the matching-flag enumeration of A.13). Each such orbit representative is an actual discrete flag.

The corresponding profinite group orbit is compact and hence closed in the finite product of completed Hom sets. Every discrete tuple lies in one of these finitely many closed orbits, and the discrete product is dense in the completed product. Therefore these finitely many profinite orbits cover the entire completed factorization space. E.32 computes each orbit stabilizer as the full completion of its discrete flag stabilizer. This proves the needed orbit description; it is not an appeal to density of an unspecified equalizer.

Put E=G1-hat × H0-hat. For the factorization A0→B0→B1, its orbit is

(E × G0-hat)/Graph(K-hat→G0-hat),

where the graph also includes K-hat's known embedding in E. Its composition map to E/K-hat is projection to E. The other factorization A0→A1→B1 similarly has orbit

(E × H1-hat)/Graph(K-hat→H1-hat).

These formulas follow from the isomorphic projections of flag stabilizers to K-hat in Section2. In particular the factorization fibre over a fixed composite is exactly the middle endpoint group, with the stated action. These are explicit compact homogeneous spaces and maps.

## 4. The actual completed square equalizer

Take a completed commutative square and call its common composite z. Choose e=(g1,h0) in E carrying the canonical composite z0 to z. In the first factorization orbit choose a middle coordinate x in G0-hat. The two arrows are

(g1 alpha x^-1, x eta0 h0^-1),

where alpha:B0→B1 is the chosen canonical horizontal arrow. Requiring its first crossing to be the fixed eta0 means exactly

(x,h0) ∈ C0-hat,

the full diagonal vertical stabilizer. In the other factorization orbit choose y in H1-hat. Its arrows are

(y alpha_top h0^-1, g1 eta1 y^-1).

Requiring its last crossing to be the fixed eta1 means exactly

(g1,y) ∈ C1-hat.

Thus every profinite square is obtained by the endpoint action of a pair in C1-hat × C0-hat on the canonical discrete square. Its stabilizer is the full completion of the framed adjacent stabilizer

S = Stab(t,gamma0,gamma1)/Delta_gamma1,

embedded diagonally in C1 × C0. The residual smoothing kernel is the cyclic d-twist, with its full topology in the target framed group because it already has that topology in the cut-component target group. The diagonal-topology argument of E.32 therefore gives the full profinite topology of S in C1 × C0. All maps are the actual inclusions and quotients.

Consequently the completed equalizer is exactly

(C1-hat × C0-hat)/S-hat,

with a finite disjoint union when all incidence/pinning choices are retained. This is also the full categorical completion of the discrete framed transporter orbit: every finite equivariant quotient factors through a finite quotient of the product endpoint groups, and conversely such quotients give finite two-object framed categories. The discrete square set is dense, because C1 × C0 is dense in its completed product and its image is the entire displayed compact homogeneous space.

This proves completion on these specified adjacent commutative-square Hom sets. It also identifies both coordinate projections, so it is stronger than merely computing their automorphism groups.

## 5. Intended application and remaining work

The result supplies the framed exit category, on adjacent arrows, inside the completed square category obtained by smoothing the rational-tail tags. A next step is to extend E.35's two-coordinate sewing section (q,r) to these Hom sets. Its group version is already exact; the present orbit/equalizer formula supplies the missing full-topology and density statement for noninvertible squares. One must still prove that the zero-middle-coordinate section is jointly determined on the square Hom sets, and then that local04/11 crossing images generate every global adjacent crossing through this actual smooth-sewing functor. This note does not yet assert whole-exit faithfulness.
