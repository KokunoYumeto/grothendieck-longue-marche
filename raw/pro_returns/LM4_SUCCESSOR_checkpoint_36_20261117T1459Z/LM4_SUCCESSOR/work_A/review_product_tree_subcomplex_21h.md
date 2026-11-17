# Independent review: countable product-tree subcomplexes

Reviewed `work_CE/subcomplex_product_trees_freeness_21h.txt` in full on 2026-11-16. Verdict: **PASS**, solely for genuine cubical subcomplexes with the stated weak CW topology.

For one finite leaf-strip extension, each new square has its own distinct outer edge as a free face. The elementary collapses are therefore relative to the previous rectangle. The remaining new graph meets that rectangle only in vertices; inner edges of a new square already belong to it by the subcomplex condition. The graph-of-components van Kampen argument gives the actual based free-factor inclusions even when old components merge.

Countable finite-subtree exhaustion consequently gives nested component groups with compatible free bases. Compact loops and null-homotopies in a CW complex lie in a finite subcomplex, so their groups form the required direct limit. This proves freeness, rather than merely local freeness. The same finite-stage argument kills all higher homotopy, and the map from a wedge of circles realizing the compatible basis is a homotopy equivalence by CW Whitehead.

The final scope boundary is essential and correctly retained. The actual transported node disk cannot be replaced by all the elementary squares in its abelian boundary chain. An outer-boundary relation of two squares kills their product, while filling both square disks kills the two generators separately. No simultaneous Tietze comparison for the complete actual orbit family is supplied. B105 also rules out a homotopy equivalence of the unchanged actual E-cover with a graph. Thus the lemma proves neither actual M freeness nor kappa vanishing.
