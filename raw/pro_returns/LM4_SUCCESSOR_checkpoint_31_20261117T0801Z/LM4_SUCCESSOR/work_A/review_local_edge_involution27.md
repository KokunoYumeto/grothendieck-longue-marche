# Independent local-involution corollary review

Reviewer A, checkpoint 27. This is a proof of the optional local corollary requested by DE, not a new statement about the actual post-filling base. Its input is Section 5 of `work_DE/next_marginal_source/unfilled_edge_map_structure27.md`, SHA256 `44ab5dfe0a76ff981c20a787bfe6010c5314e959bc7b86eb6f46f2c398ce8f28`.

Let E1 be the actual B117 group, K1 its indicated free rank-five retract, and eta1 the actual order-two prefix-reflection automorphism. The local group Dloc is the two-copy amalgam over K1, with the second marking twisted by eta1; kappa exchanges the copies and acts on their common subgroup by eta1. Folding the exchanged edge gives

    Dloc semidirect<kappa> = E1 *_(K1) Q1,
    Q1=K1 semidirect_(eta1)<kappa>.

The actual prefix basis of K1 is inverted by eta1. Therefore Q1 is the free product of six order-two groups, with kappa one of the literal factors. The ordinary factor-centralizer theorem gives C_Q1(kappa)=<kappa>. In the ordinary amalgam tree, kappa fixes the Q1 vertex and no edge, since K1 is torsion-free. Its fixed subtree is consequently that one vertex. Hence C_(Dloc semidirect kappa)(kappa)=<kappa>, and Dloc^kappa=1.

For the compact assertion properness must be justified, not inferred just from the abstract folding. Given prescribed finite vertex kernels A in E1 and B in Q1, choose an eta1-invariant finite-index normal subgroup L of K1 contained in A intersect K1 and B intersect K1. This is possible by intersecting their two eta1 translates. Combine E1/A with the actual retraction E1->K1/L. The combined finite kernel restricts to exactly L on K1. Combine Q1/B with Q1->(K1/L) semidirect C2; this likewise has exact edge kernel L. The resulting two finite vertex groups have a common finite embedded edge. Their amalgam has a finite permutation quotient injective on both vertices, by matching finite regular actions. These targets are cofinal in the prescribed finite vertex topologies. Thus the completion of the folded group is the proper full profinite amalgam of the two vertex completions over K1hat. The finite-index subgroup Dloc has its full induced topology in this folded group.

The free profinite K1hat has no involutions. Thus kappa fixes no edge in the standard profinite tree. The prime-order fixed-tree theorem at the already audited B122 dependency supplies a nonempty connected pro-two fixed subtree. With no edges, it has only one vertex: otherwise its reduced degree-zero F2 homology is nonzero. Its unique vertex is the displayed Q1hat vertex. Every element centralizing kappa preserves it, so the centralizer lies in Q1hat. The full free-profinite-product centralizer theorem used throughout B108/B112 gives C_Q1hat(kappa)=<kappa>. Intersecting with Dlochat proves

    (Dlochat)^kappa=1.

No torsion-freeness assertion for E1hat is needed. All compact-tree and free-product dependencies are used at their already verified formal scope; this note does not claim a fresh primary-source retrieval. Most importantly, the map from Dloc into V_* may have a nontrivial kernel, and the local fixed-group calculation gives no fixed-point lifting or centralizer statement after that quotient. The actual matching-kernel invariance remains open.

## Final owned source binding

The complete newly saved DE proof `work_DE/next_marginal_source/local_edge_involution_fixed_subgroup27.md`, SHA256 `e3b78c188839d24b2468e59e9dcd43e6ba2e9ce6fb2b80ec257c7f3bc87734c5`, was subsequently read in full at 2026-11-17T03:39:59.724076+00:00. All folded maps, exact finite kernels, selected factor and fixed-tree scope match the preceding proof. PASS; no correction requested.
