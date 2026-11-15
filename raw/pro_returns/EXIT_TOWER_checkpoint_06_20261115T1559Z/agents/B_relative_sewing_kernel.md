# Whole-arrow sewing and the adjacent kernel

Status: proof memo for root integration after E.40. The middle-chain extension and the 04-to-11 construction have been independently checked by the D agent. This note supplies exact categories, maps and a generator argument; it does not infer faithfulness merely from the individual endpoint groups.

## 1. The framed core category

Let S be one bordered surface, or a disjoint pair, with two selected labelled parametrized boundary circles a,b. Every interior multicurve is essential, nonperipheral, and has no parallel repeated components. Let P be its framed exit category:

Hom_P(gamma0,gamma1) = {p in Gamma^boundary(S): p gamma0 contains gamma1}/Delta_gamma0.

For two disjoint cores take the product category. Other external boundaries retain their labelled tripod tags. Smooth sewing of a to b is the topological surface operation using the fixed orientation-reversing boundary parametrizations. Its image of every interior multicurve remains essential and without duplicates: the inclusions of the cores into the sewn surface are the usual injective amalgam/HNN maps, and only curves parallel to a sewn boundary could become parallel through the collar; those were excluded. The functor we recover below is this actual smooth sewing on the full exit category.

Attach a tripod to a and one to b. On each choose one external leg for clutching; call the other external leg its companion. The companions are new distinct labels, different from all other labels. Clutch the two chosen legs, giving a middle node m, and call the two original core-interface nodes i,j. Let T={i,m,j}. For each core multicurve gamma, consider the actual two-step flag

T union gamma -> {m} union gamma -> gamma.

The first arrow smooths the two interfaces; the second smooths m. Its composite smooths all three nodes. Keep the middle companions throughout. Let L be the category of these flags and commutative natural-transformation diagrams whose horizontal arrows may be noninvertible core generizations. Retain each actual pin and, on passing to a skeleton, transport it with E.145.

## 2. Why the chain is intrinsic

Each of the two companion-labelled vertices is a stable (0,3) vertex. For any stable contraction producing a vertex v from a connected subgraph H,

d(v) = sum_{w in H} (3g(w)-3+val(w)) + number of contracted edges.

Every summand is nonnegative. A target (0,3) vertex therefore cannot arise after any nonempty contraction. Since its companion label is unique, it is the same surviving tripod vertex. The edge joining the two such vertices is m; their remaining incident node edges are i and j. Thus every transporter between the specified source flags preserves i,m,j individually. This argument also covers self-sewing and nonseparating interface curves; it uses actual stable graph contractions rather than separating label partitions.

Consequently a natural transformation of the displayed flags restricts to a framed transporter p of the cores, together with an independent integer middle-annulus twist n. Conversely extend p over the two fixed tripods and put n twists on the middle collar. These are inverse constructions.

For completeness the group presentation before the core multicurve quotient is exact. A core contributes Gamma^boundary(S), each tripod contributes three central boundary twists. Identify each inner tripod twist with t_a or t_b, kill each companion boundary twist by its ordinary marked cap, and identify the two clutched-leg twists with one t_m. Elimination leaves exactly Gamma^boundary(S) times Z_m. The inverse extends core maps by the identity and realizes t_m in the middle annulus. Interior multitwists Delta_gamma lie wholly in the first factor. Therefore, on every actual Hom set,

Hom_L(gamma0,gamma1) = Hom_P(gamma0,gamma1) times Z_m,

and composition is (p1,n1)(p0,n0)=(p1p0,n1+n0).

## 3. The two intrinsic projections, including noninvertible arrows

The functor q:L->P omits the last, middle smoothing. The remaining flag is exactly the clutching of the two input tripod flags (or the corresponding self-clutching). Normalizing at m gives the input framed core category recovered by E.40; the retained m twist is killed. In the explicit coordinates, q(p,n)=p.

To define r, replace the displayed middle-last flag by its middle-first flag, retaining i,j and all core curves. This replacement is the actual matching flag specified by the same individually distinguished nodes; the equality of composites is the corresponding E.38 smoothing diamond. Normalize at i,j and select the component consisting of the two middle tripods. It is the standard labelled four-point sphere with its one-node crossing. Every noninvertible core arrow disappears under this normalization; the induced morphism of that four-point crossing is exactly the n-th power of its middle twist. Thus r:L->B Z_m has r(p,n)=n. The object in B Z_m is the selected genus-zero crossing, with its fixed pin and positive angular generator. No normal-coordinate section is chosen.

The explicit comparison is (q,r):L->P times B Z_m, with inverse on morphisms (p,n) given by extension over the fixed tripods plus n middle twists. It is a functor with a literal inverse in compatible actual-object coordinates. After passage to any finite skeleton the transports give the specified natural equivalence.

## 4. Full completion and the unique zero-coordinate section

The middle-chain version of E.40 is valid with the intrinsic-node proof in Section2. For a coarse vertical chain crossing E.29 gives the full diagonal completion; for its full adjacent flag E.32 gives the same full completion. Their projection is the completion of the identity of the discrete stabilizer. Thus no injectivity of the projection to the single open endpoint, and no equality between intersections of closures, is required.

For an adjacent core arrow, write P_i for its framed endpoint groups and S_P for its actual incidence stabilizer. The chain endpoint groups are P_i times Z_m and its incidence stabilizer is S_P times Z_m, with the same n in the two endpoint factors. Its completed homogeneous square space is therefore

[(P_1-hat times Z-hat) times (P_0-hat times Z-hat)] / [S_P-hat times diag(Z-hat)]

= [(P_1-hat times P_0-hat)/S_P-hat] times Z-hat.

The map is [(p1,n1),(p0,n0)] -> ([p1,p0],n1-n0); its inverse uses n0=0,n1=n. It agrees with q,r, including both endpoint actions. For a general deleted core set D=gamma0 minus gamma1, the same homogeneous-factorization proof applies: the chain T remains intrinsic, so both coarse intermediate subsets (drop T, or drop D) are intrinsic even if the curves of D are permuted. The residual diagonal kernel is the full multitwist lattice Z^D, whose full topology is E.29. If ordered adjacent flags are used, retain all finite D orders/pinnings and induce over their permutation orbit; this restores the whole incidence stabilizer. Thus the displayed product formula holds on every Hom set. Its composition is already the coordinate addition formula and is preserved after completion; E.38 supplies the same complete relation verification. Alternatively, the finite-congruence completion of a finite-object category P times B Z is exactly P-hat times B Z-hat: for every finite target functor, take the least common multiple of the orders of the finitely many images of the central Z at the objects; its kernel contains a product congruence from the restriction to P and this finite-index subgroup of Z. These product congruences are cofinal.

Accordingly (q,r) is the actual full completed product comparison. In the compatible chosen object coordinates its zero-coordinate section s is uniquely specified, on objects and every Hom set, by q s=id and r s=identity. In the full isomorphism-closed category use the fibre over the fixed genus-zero middle crossing, including its specified identification: q on the zero-r fibre is fully faithful and essentially surjective. Hence its inverse section is unique up to the unique natural isomorphism commuting with q and the r identification. This is the invariant formulation, so a tower equivalence need not preserve arbitrary skeletal representatives. The section is extension-by-identity on the middle annulus. The uniqueness on Hom sets is stronger than uniqueness on isotropy groups.

## 5. Recovering smooth sewing on all framed exit arrows

Forget the two companion labels and stabilize. The three-node chain becomes the single sewn node, and on collar parameters q_e=q_i q_m q_j. On twists the map is (u_i,u_m,u_j)->u_i+u_m+u_j. Applied to s, the middle displacement is zero. The bottom endpoint of the resulting flag is the smoothly sewn core. On a core arrow represented by p, restriction/extension shows that the resulting arrow is precisely its actual sewn representative; on each interior Dehn twist it is the same twist in the sewn surface. Thus this gives the actual sewing functor P-hat -> framed_exit(sewn S)-hat on noninvertible arrows as well as groups.

For several sewings use one independent middle coordinate for each pair. The unique section is characterized by all r_e s=identity. Each order of sewing gives this same section, and stabilization multiplies the same collar parameters. Hence the comparison is associative, respects self-sewing and disjoint sewing, and is compatible with every retained core multicurve. Source and target endpoint maps are the same sewing and capping maps of E.35--36, now on full Hom sets. Relabelling acts on the fresh tags and node coordinates; undoing a pin uses the actual finite relabelling groupoid, not a presumed split group extension.

Ordinary marked caps and forgetting are already operations of the original tower. A bordered unmarked disc cap is realized by forgetting both external labels of that boundary's rational tripod and stabilizing; its interior curve effects are exactly those of E.36. This is therefore an intrinsic functor on the recovered framed exit category. Boundary-parallel, peripheral, or coincident images are stabilized using the actual C.1 lattice map.

## 6. Actual local generation by the four-point crossing

Fix an adjacent actual generization sigma=tau union {c}->tau. First normalize at tau and retain every branch pin. On the component containing c choose a pants decomposition refining c. The support of c is either the union of two pants, a four-holed sphere, or one self-adjacent pant, a one-holed torus. Every other auxiliary pants cuff is smoothly sewn back. The tau branches are capped as marked points and clutched to retain precisely tau. On actual objects and representatives, this operation sends the one-node crossing in that support to the specified sigma->tau; identity extension sends its pin to the given pin. Full endpoint translates give the entire adjacent biset.

The one-holed-torus crossing is itself generated by the four-holed-sphere crossing. Label the two sides of its source node c by boundary pairs {a,a0} and {b,b0}. Smoothly self-sew a to b, then cap b0 by an unmarked disc. On the source, the two pants join along the new smooth collar into one genus-zero component; the two branches of c lie on this same component. After capping b0 it has the one external boundary a0 and the two branches of c. Thus c is exactly the nonseparating node of the one-holed torus. On the target the operation changes (0,4) to (1,2) and then to (1,1). Positive local plumbing at c is untouched, so the crossing and its meridian map without an extra winding. This is an explicit operation comparison, not an identification based only on group presentations.

Hence the actual four-point crossing, smooth boundary sewing, ordinary clutching and capping generate every adjacent arrow, with all retained flags and endpoint transports specified.

## 7. Consequence for the whole-arrow kernel

Let an equivalence of the labelled completed exit system have coherently trivial genus-zero restriction. E.35 and E.27 identify its action on the full bordered sewing groupoids with the identity, with one coherent endpoint comparison for each marked-pants object. E.40 makes the framed core categories intrinsic, and Sections3--5 make their whole-arrow sewing intrinsic: q,r are preserved by every system equivalence, and the unique simultaneous zero-coordinate section is therefore preserved. The comparison at a boundary-stratum endpoint is built as follows: normalize its actual stable graph, apply the coherent sewing-operad identity on every cut component, and then apply the actual nodal clutching with all branch pins fixed. Coherence for relabelling descends this comparison through the finite graph-permutation groupoid. This construction depends only on that endpoint graph and its transported marking. The source and target comparisons in the middle-chain construction are precisely its capping and sewing instances, by the explicit q/r product maps. Therefore the component at an endpoint is the same for all incident crossings; it is not chosen separately for each biset.

Choose the coherent endpoint comparisons just obtained. In their coordinates, the actual four-point crossing is fixed by genus-zero triviality. Section6 expresses each adjacent crossing through that crossing and intrinsic operations, so it is fixed in the same endpoint coordinates. Independence from auxiliary pants refinements follows either from the functorial intrinsic sewing construction, or by comparing two refinements through pants moves within the retained components, whose morphisms and operations already have their coherent identity comparison. Every endpoint translate is fixed by equivariance. E.38 then fixes every arrow and every composition. Undoing the chosen endpoint coordinates yields a natural identity of the entire completed system, with its operation comparisons.

This argument does not infer monicity of composition with a full smoothing arrow. In particular it uses no unproved map Hom(sigma,tau)->Hom(sigma,empty) on completions, and no arbitrary completed multicurve-normalizer equality. The noninvertible square topology and the exact two-coordinate section supply the needed whole-arrow naturality.
