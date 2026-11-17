# Abstract annulus disk with prescribed lifts

Research lemma and scope audit, 2026-11-16, checkpoint21. The abstract lemma is true. It does not supply the common-support comparison needed to transfer all five actual necks.

## Statement

Let p:A_t→A_y be the connected two-sheeted cover of an annulus, represented by p(t)=t². Let 1 be a retained puncture in the interior of A_y, and let y_1,...,y_5 be five distinct further interior points. Prescribe one of the two lifts of each y_i. There is an embedded closed disk D in A_y minus {1}, with every y_i in its interior, such that one component of p^{-1}(D) contains precisely the five prescribed lifts.

## Complete construction

First choose a finite embedded tree in the annulus minus {1}, containing all five points, and take a sufficiently small closed regular neighborhood D_0. One way to obtain the tree is to triangulate a compact connected subsurface containing the five points and avoiding1, put those points among its vertices, and take a finite tree in its connected one-skeleton. A regular neighborhood of an embedded tree in an oriented surface is a disk. The cover over D_0 is trivial. Choose one component, which specifies an initial lift of each y_i.

For each i whose initial lift disagrees with the prescription, choose a loop gamma_i based at y_i, in the annulus minus {1,y_j:j≠i}, with winding one around its core. Such a loop is obtained by joining y_i to a core circle avoiding the finite marked set, traversing it once, and returning along the same path. Smooth it if desired. Its cover character is one in C2.

There is an ambient isotopy Phi_{i,s}, starting at the identity, that moves y_i along gamma_i and fixes the boundary,1,and every y_j with j≠i throughout. This needs no unproved support assertion: the loop has compact image disjoint from those fixed sets, so choose a positive-radius neighborhood staying disjoint from them. A time-dependent bump vector field supported in a small disk about gamma_i(s), equal to gamma_i'(s) at its center, has a compactly supported flow with exactly the required track. The endpoint Phi_{i,1} fixes y_i as well, because the track closes.

Lift this ambient isotopy to A_t, starting at the identity. The lift over each other marked point stays constant, since that point's entire track is constant. The track over y_i switches sheets, since its winding has odd covering character. The lift at the endpoint covers Phi_{i,1}; this is the specific lift fixed by the isotopy, so no uncontrolled global deck choice is present.

Compose the finitely many endpoint homeomorphisms and their lifted isotopies. The composition Phi fixes all marked points and1. It switches exactly the chosen subset of lift pairs. Put D=Phi(D_0). This is still an embedded disk avoiding1 and containing all five y_i. The image of the chosen component of p^{-1}(D_0) under the composed lift is a component of p^{-1}(D) containing precisely the prescribed lifts.

The construction in fact works for any finite number of marked points. It does not require disjoint supports for the different point pushes; each push fixes all other marked points throughout, which is the required independence.

## Actual support restriction: why this does not settle all necks

The abstract construction allows point pushes in the entire punctured annulus. It does not require a single transported pure class to be realizable with both of the different supports in the actual inner and outer comparison.

For a track contained in |y|>1, its windings about0 and1 coincide: the two centers lie in the same omitted disk, or equivalently y/(y−1) has zero winding there. For a track contained in |y|<1, its winding about1 is zero. Therefore, if the same actual transported track class admits both support descriptions, its two winding invariants satisfy

    wind_0 = wind_1 = 0.

In particular its double-cover character wind_0 mod2 is zero. Such a common admissible point push cannot perform an independent sheet switch. This is exactly the restriction reported by CE; it blocks the proposed simultaneous-use argument, not the abstract disk lemma.

No global fixed-source equality, all-neck transfer, or impossibility of another geometric comparison is concluded. The already established first-neck comparison remains separate.
