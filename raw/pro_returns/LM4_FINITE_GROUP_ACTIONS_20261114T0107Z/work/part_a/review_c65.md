# Independent audit of C.65

**Result: PASS.** I read the complete proof and metadata, and checked the exact inputs in C.28, C.30, C.32, and C.33. Both assertions are proved with the stated maps. No mathematical correction is required.

## Finite-word paths and intrinsic restrictions

Products, inverses, and conjugation by a fixed word preserve the displayed finite-word kernel-path condition. Reparametrization proves that every intermediate point remains in N. Thus the subgroup, normality, and path-connectedness assertions are justified for this exact N.

On an intrinsic line orbit, C.28's nested compact sets are arcs, and the intrinsic arc between any two of their points is unique. Consequently any compact intrinsic interval lies in some one of these sets. A word of a fixed finite length takes the interval into a single larger compact arc. The ambient joint-continuity argument therefore gives the required intrinsic compact-open continuity, including inverses. There is no appeal to intrinsic continuity of arbitrary sequences of unbounded words.

Every element of G is intrinsically orientation preserving because the generators have continuous paths from the identity in the intrinsic homeomorphism group. This applies to the whole boundary restriction image, not just N.

## The principal kernel and the boundary image

The C.33 principal product has the actual translation action of the connected local centralizer. Every original g commutes with this action. An element inducing the identity on the entire base therefore has the exact fibre-translation form in C.65.5, and any two such restrictions commute. Their global commutator is identity on O and hence, by continuity, on its entire closure. This proves abelianness of the boundary image without identifying the two different kernels.

For the normal subgroup T of the transitive intrinsic boundary image K, its common fixed set is K-invariant. Nontriviality therefore makes that fixed set empty. Path-connectedness of T makes each orbit path connected; each is nontrivial, contains an open arc, and can translate that arc to a neighborhood of any chosen starting point. Thus all its orbits are open, and connectedness of B makes T transitive.

The intrinsic closure is still abelian, connected, and transitive, hence free. Its full centralizer is itself by evaluation at one point and propagation through transitivity. C.30's evaluation proof applies verbatim to the intrinsic one-manifold: the intrinsic homeomorphism group is Polish, the orbit map is open, and inverse evaluation continuity uses compact intrinsic intervals. Its evaluation image is all of B, so the closure is locally compact and homeomorphic to B.

The product action on B times the plane is faithful and continuous on a connected three-manifold. It meets the exact Hilbert–Smith hypothesis already checked in C.33. The resulting connected one-dimensional Lie group is the line or circle. The evaluation identification is the actual conjugacy of its action with translations or rotations.

K normalizes this closure. On the line the conjugation parameter is a continuous additive automorphism, giving a positive affine map through evaluation. On the circle it is a continuous group automorphism of degree +1, hence the identity, and the normalizer element is a rotation. These groups are metabelian, as are their subgroups. This proves the contradiction for a nonmetabelian boundary image.

Finally the path comparison uses \(h_s=p_s q_s^{-1}\) and equality of the whole principal-base homeomorphism at each time. It does not weaken this to equality at a single moving point.

## The small-disk injection

The planar argument is valid for an arbitrary open V and any component U of V intersected with the specified open Euclidean disk.

A based polygonal approximation can be made within U, fixing the basepoint and with a based homotopy there. Its finite connected planar graph has a compact planar regular neighborhood M contained in U. The bounded region enclosed by its outer Jordan boundary lies in the convex hull of that boundary. This hull is a compact subset of the original open Euclidean disk. Hence every inner complementary disk lies in that same disk.

Filling exactly the inner disks contained in V leaves a compact planar surface M' inside the same component U. Every unfilled disk contains a point outside V in its interior, since its boundary already lies in M and hence in V. The inclusion of M' into the plane with these finitely many points deleted is indeed a strong deformation retract:

- use a Schoenflies coordinate centered at the chosen deleted point in each inner disk;
- retract its punctured radius to the boundary;
- use the exterior Schoenflies coordinate and the same radius formula outside the outer boundary;
- keep M' fixed.

The formulas agree on all boundary circles. The finitely many pieces are closed in the punctured plane, so the product homotopies paste continuously. No control at an added point at infinity is needed, since that point is outside the space being retracted.

A null-homotopy in V avoids every selected deleted point. Applying this actual retraction and then the original polygonal homotopy gives a based filling in M', hence in U. This proves the asserted fundamental-group injection and the controlled filling.

## Application and scope

For the original ambient-null plane loop from the hyperbolic setup, C.32 supplies the required null-homotopy in each invariant open orbit. Uniform continuity of the original compact time family makes evaluation tracks approaching a G-fixed frontier point shrink uniformly. Taking disks with radii tending to zero and using the proved injection gives individual fillings with vanishing ambient diameter.

The statement already calls these shrinking evaluation loops null. As a minor expository clarification, the last application paragraph could say “original ambient-null evaluation loops” when invoking C.32: its restriction theorem uses the ambient-null hypothesis present in the original setup. The small-disk injection itself has exactly the separately stated null-in-V input.

The proof does not provide a continuous choice of fillings, a lift of an arbitrary base path, intrinsic continuity for unbounded word limits, or a global equivariant fragmentation. Its concluding scope and the retained Open status of C.12 are correct.

## Addendum audit: the full kernel and graph-image covering

**Result: PASS for the strengthened text.** I separately read the new claim paragraph, the full addendum beginning “The full kernel and its exact discrete ambiguity,” and the updated metadata. I reopened C.38 in full and checked the actual principal charts in C.33. The earlier optional application wording has also been incorporated.

For any fixed element k of the full principal kernel and any g of G, writing g as a finite original word and scaling its finitely many time parameters gives the actual path g_s. The commutator path with k is still one finite word, is based at identity, and has identity whole-base action at every time. Thus it is covered by the already proved endpoint-subgroup comparison. Its endpoint proves that the entire boundary image of the full principal kernel centralizes the boundary image of G.

C.38 applies to that transitive nonmetabelian, hence nonabelian, orientation-preserving intrinsic image. Its full centralizer is closed and discrete, with the asserted cyclic description. Every subgroup of a closed discrete subspace is closed in the ambient intrinsic homeomorphism group. This establishes the full-kernel image assertions without assigning or transferring a topology to the abstract principal kernel.

The graph image is an actual topological subgroup with the stated induced product topology. First-coordinate projection has precisely the displayed discrete central kernel. For its topological group quotient, discreteness gives an open identity neighborhood U with U inverse U intersecting the kernel only at identity. Its kernel translates are pairwise disjoint, exhaust the inverse image of q(U), and each maps homeomorphically onto q(U), because the group quotient is open. Translation supplies the required evenly covered neighborhoods everywhere. This proof does not require local compactness or closedness of the whole graph image in the product.

The finite-word paths give path connectedness of the graph image. Frontier compact-open continuity was proved earlier in C.65. For the base factor, the actual principal chart and its local sections give joint evaluation on compact sets, and the inverse word supplies inverse convergence. Thus the graph-image path argument uses the specified image topologies.

A deck transformation of this connected covering is determined by one value: the equality set with a competing deck map is both open and closed by local covering coordinates. Kernel translations reach every point of each fibre. Hence they are the complete deck group, not merely a subgroup of it.

Finally the induced quotient-to-base-image map is a continuous bijective homomorphism by the actual quotient universal property. The text correctly stops there and makes no inverse-continuity claim. The strengthened statement and its metadata are mathematically sound as written.
