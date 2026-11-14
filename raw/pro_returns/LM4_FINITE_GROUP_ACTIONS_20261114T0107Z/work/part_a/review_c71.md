# Independent audit of C.71

**Verdict: PASS on the current corrected source.** I read the full proof, metadata and producer, then reran the producer successfully: 34,194 exact checks. Captured output is in work/part_a/c71_audit_stdout.txt.

One scope correction was requested and has been made by B. The cyclic example is an action on the actual closed disk whose **interior image** is closed, discrete, free and proper. The generator fixes boundary arcs, so these qualifications apply to its interior restriction. I reread the corrected claim paragraph. The proof already had that exact scope.

## Two-dimensional operator group

The C.33 input gives the actual Lie-group structure. Proper free evaluation embeds each identity-component orbit; invariance of domain makes the two-dimensional orbits open. Connectedness gives transitivity, and freeness then forces every component of Q to be its identity component. Proper evaluation identifies Q with the disk, so it is simply connected.

The two Lie algebra possibilities, their simply connected group integrations, and the stated exponential formula are correct. Evaluation identifies the interior centralizer with right translations, including its compact-open and inverse topology; inversion supplies the stated comparison with the opposite group.

For each endpoint of the based sphere family, a path from the sphere basepoint supplies the C.37 two- or three-letter fractional-power representation. Since n is positive, such a path always exists. Every letter belongs to the same compact set P, independently of the selected path. No continuous selection of paths is needed.

The restriction of P cubed to the dense disk interior is an injective continuous map from a compact space to a Hausdorff space. Its inverse on its image is therefore continuous. The entire interior logarithmic homotopy has its image in that compact restriction image, so it lifts jointly continuously as a family of the original closed-disk homeomorphisms. This verifies the original boundary condition and inverse topology. The conclusion is about each based sphere family; it does not claim that the entire relative group has a globally chosen contraction.

The equality with the relative centralizer of A follows by continuity of commutation on the interior and density of the interior in the closed disk. It does not require A to fix the boundary.

## Actual rectangular compactification

The radial square-to-disk formula and its inverse are inverse on each ray, continuous at zero, and send the square boundary to the circle. The two coordinate compactifications transport the real translation to exactly the displayed closed-square homeomorphism.

The integer action is free and proper on the plane and closed discrete in its actual homeomorphism topology. Evaluation detects its integer parameter; transport through the actual interior coordinate preserves all these assertions.

The fixed boundary set is precisely the two full horizontal edges. Any closed-disk conjugacy would send that set bijectively to the fixed boundary set of the cyclic Fuchsian generator. The latter has one or two points, as follows directly from the parabolic or hyperbolic Möbius form. This is an obstruction for the exact proposed conjugacy, with both coordinate maps specified.

The partial space is the actual strip with its vertical edges. Its quotient and deck coordinate are the displayed closed annulus. Horizontal translation commutes with the generator and fixes the retained vertical edges, but moves points of the omitted horizontal edges. Density makes any extension unique, so no boundary-fixed extension exists. This proves the asserted failure of surjectivity of the specific restriction map.

## Exact cyclic centralizer and topology

For a commuting boundary-fixed map, integer translation equivariance makes the first real coordinate periodic in the second. Taking integer translates towards the actual fixed top edge forces the first coordinate to be x itself. Fiberwise bijectivity and the integer translation equation then give increasing real homeomorphisms F_x. The vertical edge condition is exactly the stated uniform vanishing of their periodic displacements.

Conversely those conditions give bounded global displacement and jointly continuous fiber inverses. The bounded displacement extends the maps and their inverses across the horizontal edges; uniform vanishing gives the required extension at both vertical edges and the corners. This establishes the group isomorphism with the actual relative centralizer.

The topology proof checks both directions. The forward implication uses the Lipschitz compactification coordinate. For the inverse implication, restrict real y to one period. The limit family has a single bounded range there for all x. Uniform convergence after compactification places all approximating values in a common larger compact real interval, where the inverse coordinate is uniformly continuous. Periodicity then supplies the full supremum norm. The same argument applies to inverse families.

Interpolation remains increasing, proper, integer equivariant, and uniformly trivial at the x-ends. Uniform inverse continuity follows from the uniform continuity of the limiting increasing inverse in the fiber variable, uniformly in x. That uniformity follows by extending the displacement continuously to the two x-ends and using periodicity in y. Hence the interpolation is a contraction in the specified group topology.

All maps preserve x. Compactly supported vertical translations move any specified point to any other point on its vertical line. Thus the exact interior orbits are those lines, and there is no open centralizer orbit in this example.

## Source reinspection and certificate

I reread C.33 and the exact C.37.2 word estimate. I also reopened these original author sources:

https://web.math.princeton.edu/~jpardon/manuscripts/08_hilbertsmith.pdf

Pardon's introduction and Theorem 1.5 give the locally compact faithful-action Lie conclusion in dimension three, with the product-with-a-line reduction explicitly stated. The actual product action used in C.33 satisfies that continuity and faithfulness requirement.

https://people.idsia.ch/~grandoni/Pubblicazioni/GRSZ13mp.pdf

Theorem 4.7 explicitly includes nonatomic signed measures; in dimension two it gives one circular interval. The Section 4.3.2 argument supplies the signed-measure version. This is the precise two-coordinate input used in C.37. Polygonal approximation and compactness of interval endpoints give its arbitrary continuous-path version, and the two displayed affine charts preserve the stated group-word order.

The C.71 executable checks the rational compactification, translation law and inverse, boundary and partial-strip witness, and nonlinear periodic fiber examples and their interpolation/inverse identities. All 34,194 checks passed. It makes no numerical claim to replace the topological proofs above.
