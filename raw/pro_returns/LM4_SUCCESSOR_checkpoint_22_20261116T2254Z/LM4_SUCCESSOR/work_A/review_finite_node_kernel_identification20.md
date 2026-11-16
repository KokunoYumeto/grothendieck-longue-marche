# Independent review of the actual finite node-kernel comparison

Reviewed 16 November 2026. Complete source:
`work_CE/research_finite_node_kernel_identification_20h.txt`.

## Verdict

PASS. The additional actual finite equivariant model closes the earlier
presentation-comparison gap between B96's external old-orbit kernel
and B102's actual second homology. It supplies no obstruction vanishing.

## Unique completion

The prefilled graph bundle is K(W semidirect S,1), since its universal
cover is the tree of contractible fiber covers over the free base tree.
Its actual P_even-cover corresponds to N_gen, a subgroup of the free
group W. That cover is K(N_gen,1), and N_gen is free. Thus its second
homology vanishes and the source-face boundary A is injective. Its
first homology is exactly P=N_gen_ab with the genuine larger deck action.

For the actual node boundary B, a node-coordinate chain c has zero
class in P exactly when Bc lies in im A. There is then a unique source
chain a with Aa=-Bc. Projection to node coordinates consequently gives

    0 -> Z2 -> Lambda^128 -> P -> M_ab -> 0.

The actual F preserves the source-face subcomplex and the node summand.
Therefore the unique completion is F-equivariant. This uses the actual
geometric face construction and does not substitute an arbitrary lift
of the one-chain map.

## Exact source/old indexing

Under s^-1 x s=psi_s(x), the left deck action is sigma_s=psi_s^-1.
For t=eta(s) in the actual even old-base subgroup B0, the returned-source
formula psi_s=Inn(h_t^-1) alpha_t gives

    sigma_s = alpha_t^-1 Inn(h_t).

Multiplication by the actual G unit h_t preserves every Omega-submodule
in question. The first and second coordinate blocks therefore have
images M_(t^-1) and M_(b^-1 t^-1), respectively. In particular

    alpha_t^-1 alpha_b^-1 = alpha_(b^-1 t^-1),

because the far push convention is alpha_uv=alpha_v alpha_u. The side
and the inverse are both necessary. The two resulting index sets are
the disjoint exhaustive partition B=B0 union b^-1 B0.

The left Omega basis decomposition Lambda=sum_s Omega*s matches these
coordinate blocks. B94 and B97 give their actual injectivity. Thus each
copy can be identified with its actual image M_w, with no identification
of two distinct summand tags merely because their images may intersect.
F fixes every source lift and preserves each actual block. Its action
under this identification is forced by injectivity and its action in P.
This proves the claimed actual equivariant isomorphism with D_old, and
hence K_old is identified with Z2 by the unique source-face completion.

## Residual map and scope

The reduced prefilled cellular complex has only P in homological
degree one. Its canonical equivariant derived homology comparison,
together with the actual attaching map of the node cells, identifies
the connecting Tate maps by naturality. This retains the full node
words and their source corrections. No assertion is made about a
kernel basis, finite generation, simultaneous primitive relators,
vanishing of kappa, or any completed coefficient comparison.
