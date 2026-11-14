# Independent audit of C.66

**Result: PASS.** I read the entire proof, metadata, and bibliography; reopened the exact admissible-surface definition and C.32 input; and independently reopened the primary paper and publisher metadata. No mathematical correction is required.

## Finite disjoint Jordan-disk covers

The construction works for an arbitrary compact zero-dimensional planar subset, including non-locally-connected examples. Finite clopen partitions have positive separation between their nonempty compact pieces. Choosing a sufficiently fine finite grid cover and a small polygonal regular neighborhood therefore prevents any connected component from joining two partition pieces. Each component remains within a prescribed small coordinate neighborhood of one small piece. The regular neighborhood can be taken to contain the deleted set in its interior and have boundary disjoint from it.

Filling the bounded holes up to each outer Jordan boundary does not enlarge the coordinate diameter: the resulting disk lies in the convex hull of that component. Distinct outer curves have disjoint boundaries, so their disks are disjoint or nested. Keeping maximal disks yields pairwise disjoint closed disks, preserves coverage, and preserves the diameter bound. Since each retained disk meets the compact deleted set, a sufficiently small uniform diameter also places it inside the initially specified neighborhood. The chosen bounded coordinate chart makes the passage from coordinate diameter to the fixed sphere metric uniform. Thus the asserted arbitrarily small finite disk covers are justified.

The connectedness arguments use these actual covers. On the sphere, remove their interiors and join the two points through the resulting connected finite planar surface. Inside a Jordan disk, cover the compact deleted portion by smaller disks entirely inside it, avoiding the two chosen points, and use the corresponding finitely connected disk complement. No local connectedness of the deleted set is used.

## Exact end compactification

The successive covers may be chosen inside the preceding disk interiors. Their complements are connected compact surfaces in M, are nested through interiors, and exhaust M because each shrinking disk meets the deleted set. The exhaustion is also cofinal on compact subsets, by the interior nesting and compactness.

Every component of the complement of a compact core is exactly a punctured disk interior from that stage; it is connected by the preceding argument and is not relatively compact in M. A compatible sequence of components therefore gives nested closed disks of vanishing diameter. Its unique limit belongs to the deleted set. Every deleted point gives exactly one such sequence. The end neighborhoods are carried to the actual disk interiors, proving both directions of the topology comparison, including neighborhoods of the deleted points.

The extension of a homeomorphism is constructed from this cofinal component system using properness. Applying the construction to its inverse gives an inverse extension. Density of M gives uniqueness and the exact composition and inverse formulas. Thus the full restriction map is an algebraic bijection between the stated setwise stabilizer and Homeo(M), not a map defined only on an identity component.

## Compact-open and inverse topology

The crucial compactness assertion C.66.5 is valid. The convergent sequence of inverse homeomorphisms together with its limit is a compact parameter space in the homeomorphism-group topology. Joint evaluation on that compact parameter space times the chosen compact core is continuous, hence its image is compact in M. This provides a single larger compact core controlling all inverse images of the smaller one.

Each image of a complementary component of that larger core avoids the smaller core and hence lies in one target component. A reference point in each of the finitely many source components determines the correct parent component for all sufficiently large sequence indices. The extension maps every deleted point in that component into the same small parent disk. All remaining points lie in the larger compact core, where the original sequence already converges uniformly. This proves uniform convergence on the whole sphere. Applying the same reasoning to the inverse sequence proves inverse convergence as well.

Both stated groups are metrizable, so this sequential proof establishes continuity at identity. The exact group homomorphism then gives continuity everywhere. Restriction is continuous in the other direction. The resulting isomorphism of topological groups consequently gives joint continuity for any continuous parameter family, including its inverses.

The pointwise conclusion for a connected based family follows from the continuous evaluation map into the zero-dimensional remainder: its connected image is a singleton. It does not alter the setwise definition of the full group in C.66.1.

## The plane-loop application

The actual loop-generated group is path connected through finite word paths, so its orbits are path connected. Every orbit in the zero-dimensional nonopen locus is a singleton. The one-point compactification of the closed zero-dimensional planar set is again zero-dimensional: compact clopen neighborhoods give a compact clopen exhaustion, whose complements form the required basis at infinity. This includes the empty-locus case.

The complement of that compact remainder is connected by the proved disk-cover argument. Since it is a disjoint union of open generated-group orbits, it is exactly one open orbit. Every original commuting operator preserves the actual orbit partition, hence this open orbit and the nonopen locus.

The closure of the actual restricted operator image is a closed subgroup of C.30’s full locally compact proper local centralizer. It remains free and proper. The restricted original loop is null by the precise ambient-null statement in C.32. C.33 then gives the required intrinsic disk in its exact centralizer.

The proved extension isomorphism extends the whole disk, not just each individual homeomorphism. Connectedness and the identity parameter make the extension fix every deleted point, including the specified infinity. It therefore yields a disk of original plane homeomorphisms with continuous inverses. Commutation with every original operator follows by equality on the dense open orbit and continuity on the plane. The same density argument preserves the exact original boundary loop. The actual restriction kernel is retained, and no assumption on an abstract topology of the given operator group is added.

## Universal-cover descent and punctures

The admissible connected surfaces in C.1 all have plane universal cover, including the permitted elementary types. An ambient-null disk, composed with the universal covering, lifts as a based family on the product of the disk with the plane. Lifting the inverse family and using uniqueness proves that these lifts are homeomorphisms and that their inverses vary continuously. Its boundary is an actual closed ambient-null based plane loop.

For each original lift of each surface operator, including every deck transformation, the two boundary compositions lift the same surface family and agree at the identity parameter. Uniqueness of lifting on the connected parameter product makes them equal. Thus the plane theorem uses all original lifted labels at once.

The resulting centralizer filling commutes with the full deck group, which gives the stated exact descended maps. The product of the parameter disk with an open covering map is an open quotient, so the descended maps and inverses are jointly continuous. Every original operator commutation relation descends literally. The connected based family on a finitely punctured compact surface extends through its finite ends by the same compact-core argument; the ends are fixed individually. Thus it is a filling in the specified original identity-component intersection, with no change of the operator action.

## Primary-source check and exact scope

I independently opened the EMS publisher page:

https://ems.press/journals/jems/articles/16819

It verifies the three authors, title, JEMS volume 22 (2020), issue 6, pages 1971–2046, DOI 10.4171/JEMS/960, and publication date 20 March 2020.

I also independently opened the primary arXiv PDF:

https://arxiv.org/pdf/1610.00686

The first-page stamp identifies version 2. Proposition 1.5 is on printed page 7 and treats the equivalence of the relative and complementary isotopy properties for a totally disconnected closed set. Appendix A.1 on printed page 71 recalls the end compactification and the topology of its remainder. These are correctly cited as background. The full topological-group isomorphism and uniform family/inverse control needed here are proved in C.66 itself rather than attributed wholesale to that proposition.

The final scope is correct: this proves the requested equivariant filling in the zero-dimensional-frontier case. It makes no claim to extend arbitrary intrinsic fillings across a positive-dimensional fixed set or a nonfixed line/circle frontier, so the retained general Open problem C.12 is unchanged.
