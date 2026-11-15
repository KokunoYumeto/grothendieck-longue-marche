# Final review of lettering and O01–O07

## Scope and verdict

Read-only review of the integrated MPL_11_002-042_notes.md, limited to Question 1, CL01–CL04, and O01–O07. Existing partition and scalar-gauge reviews were retained; the present check follows the displayed maps, coefficients and source domains without broadening their claims. No frozen transcription, manuscript image or integrated main file was edited, and no additional web research was performed.

**Verdict:** no concrete map, type or coefficient error was found in the lettering calculations or O01–O05/O07. The one source-domain qualification identified in O06 has been applied to the source JSON by the root agent for inclusion in the final rebuild; no further mathematical problem is flagged within this review's scope.

## Correction identified and resolved in the source JSON

**O06, third sentence:** the phrase “the general smooth proper case” omits the cited Corollary 5.12's stated hypothesis \(X(k)\ne\varnothing\). The supplied Oda PDF, PDF page 70 / printed page 131, says: “Let X be a smooth and proper k-scheme such that X(k) is non-empty”; its preceding sentence fixes a perfect field \(k\) of characteristic \(p\).

Suggested local replacement: “Oda's next corollary, for a smooth proper \(k\)-scheme with \(X(k)\ne\varnothing\) over the stated perfect field, specifies a canonical injection from the dual Dieudonné module of p-torsion in the Picard scheme and identifies its image.” This restores the source's stated domain; the review makes no assertion about extending that source result after removing its hypothesis. Corollary 5.11's preceding abelian-variety map and the image of \(VM({}_pX)\) agree with the cited page.

**Resolution:** the root agent confirmed that O06's source JSON now says “smooth proper case with \(X(k)\ne\varnothing\) over the stated perfect field,” and that the final rebuild will carry this wording into the integrated notes. The mathematical correction is resolved at the source-entry stage; this review did not edit the main file.

## Checks and their exact mathematical content

| Item | Check | Result |
|---|---|---|
| Draft C / K68 B | With \(V=H^i(X)\), \(W=H^{2n-i}(X)\), the types are \(u:W\to V\), \(v:V\to W\), \(w=uv:V\to V\), and \(w^{-1}u:W\to V\). The two displayed compositions prove \(w^{-1}u=v^{-1}\). | Correct; the source's \(i<n\) is retained, and the additional printed \(i=n\) inverse is the identity represented by the diagonal. |
| Lowering coefficients | \(D\) multiplies the input summand \(L^jP^i\) by \(j(n-i-j+1)\), and equals 1 on \(P^i\); thus the written order \({}^c\Lambda=\Lambda D\), \(\Lambda={}^c\Lambda D^{-1}\) cancels the correct input coefficient. The product of the \(m\) lowering coefficients is \((m!)^2\). | Correct, including \(m=0\); the comparison remains attached to K68's inverse-map criterion and its stated setting. |
| CL01–CL04 and table scope | The table preserves the unlocated standalone draft B/D definitions, the index qualification, the products, the induced polarizations and the universal statement. | No complete four-letter permutation is promoted to a verified result. |
| O01 | Integrating the middle variable in \(v(t_2,t_3)u(t_1,t_2)\) gives the four coefficients displayed; applying the inverse linear map to \(\rho(v)\rho(u)\) gives those same coefficients. The images of \(t_1,t_2,t_1t_2,1\) are \(E_{11},E_{22},E_{21},E_{12}\). | Correct convolution order and matrix entries. CT16/017's five-element basis, together with CT16/015's multiplication, gives kernel \(\mathbf Q\pi_1\) for the stated \(n=1\) map. |
| O02 | \(\delta_*(1)=1\otimes t+t\otimes1\), \(\delta_*(t)=t\otimes t\) satisfy the displayed adjunction on the basis. Both coassociative iterates on 1 have the three stated terms, and on \(t\) have the single stated term. | Correct coefficients; all degrees in this example are even, so no omitted Koszul sign enters these calculations. |
| O03 | Pullback of partitions has the stated contravariant order; pushforward of the characteristic function of \(t_J\) is the characteristic function of \(t_I\). Thus both components of the indicated natural transformation commute with every finite-set map. | Agrees with the earlier independent review. The two-point rank obstruction and the diagonal tensor map are correct; the text expressly excludes this example from the retrieved special-object claim. |
| O04 | Each arrow has the ratio \(\lambda/\mu\); the square has both composite pushforwards equal to 2. The lift \(q^{-1}u\) is well typed, has both required composites, and is unique because \(q\) is invertible. | Agrees with the earlier independent review. Both exchange comparisons have values 1 and 2, and the stated scope stays in the abstract gauge category. |
| O05 | The two commutations contribute \(ij+j(i+\delta)=2ij+\delta j\), hence the sign \((-1)^{\delta j}\). | Correct for the recorded left projection-formula convention and the degree-zero pullback; the even-degree restriction removes precisely this factor. |
| O06 | Supplied Oda Corollary 5.11 gives the stated degree-one map and filtration subspace. Corollary 5.12 has the additional rational-point hypothesis recorded above. | Correct displayed map; the source JSON now restores the qualification in the third sentence for the final rebuild. |
| O07 | CT47/003 records the derived pullback, tensor with the line-bundle kernel, and derived pushforward. Passing to its recorded K-class gives the displayed \(p_{2*}([\mathcal L]p_1^*[F])\). | Correct source, target and order of operations within the written relative setting; no derived/correspondence-category equivalence is asserted. |

Local evidence used: the integrated notes; the supplied context transcription at CT16/015–017 and CT47/003–004; the already verified K68 normalization formulas and inverse-map criterion; records/partition_counterexample_review.md and records/gauge_basechange_review.md; and context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf, PDF page 70 / printed page 131. The Oda wording was checked directly by text extraction from that supplied PDF.

## Root integration resolution

2026-11-15 20:14:49 UTC — Root integration resolution: O06 now includes X(k)≠∅ over the stated perfect field in both its source JSON and the rebuilt main notes.
