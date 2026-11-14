# Independent audit: twisted relative duality for the actual pants extension

**Result: PASS.** Reviewed the full written proof in `work/part_c/pants_twisted_duality_note.tex`, including TD.1–37 and the final, literal coefficient-transport convention. The conclusion proved is that all three section centralizers in the full free profinite kernel are trivial. The argument does not require a full profinite free-product recognition theorem or a peripheral conjugator to the standard involution.

## Actual subgroups and relative coefficient module

The peripheral extensions are the actual normalizers of the three specified full procyclic subgroups. Their maps from `Zhat semidirect C2` read both the original quotient label and the unique peripheral exponent, and their inverses are continuous. Their two local involution classes have self-normalizers. D34's triangle supplies precisely two occurrences of each of the three global section classes. The exact global normalizer is `C_i × S_i` before any assertion that `C_i` is trivial.

The map `F/L_j -> E/D_j` is a genuine equivariant homeomorphism: injectivity is `F intersection D_j=L_j`, and surjectivity is `E=FD_j`. The formula TD.8 transports the extra action with its conjugating peripheral section retained. Thus the restriction of the compact augmentation kernel `Delta` is the actual relative augmentation module of the specified pants pair.

For finite coefficients `M`, continuous linear maps `Delta -> M` form a discrete continuous module. Compactness gives finite quotient factorization and an open stabilizer. The augmentation sequence splits as compact vector spaces over the finite field, which makes the continuous-Hom sequence exact. Shapiro therefore supplies the stated long exact sequence with literal boundary restriction maps.

The ordinary Hochschild–Serre sequence is applied to this particular discrete coefficient module. In particular the proof does not invoke Wilkes's relative extension spectral sequence under an inapplicable subgroup-containment hypothesis.

## Pairings and spectral sequences: TD.13–24

Evaluation `M tensor Hom(Delta,M*) -> Hom(Delta,k)` is equivariant for the displayed dual action. Tensoring the completed bar resolution with `Delta` gives the required resolution: exactness follows from compact vector-space splitting, and untwisting the diagonal action makes its terms projective. Continuous Hom adjunction identifies the ordinary coefficient cups with the relative cups. The Alexander–Whitney diagonal also supplies the filtered product and its Leibniz identity.

The dense discrete pants pair and its full completion have the same finite-coefficient absolute and peripheral cohomology. The relative long exact sequences give the relative comparison, preserving the cups. The ordinary surface-pair duality is therefore exactly the full pair duality used in TD.15. The target orientation line is one-dimensional over F2, so its quotient action is trivial. This yields the equivariant dual row identifications in TD.17, not merely equal dimensions.

For a finite F2[C2]-module, positive cyclic cohomology is `ker(1+sigma)/im(1+sigma)`. The annihilator calculations in TD.19 show that evaluation descends to a perfect pairing with the corresponding quotient for the dual. On invariant representatives the cyclic cup is precisely that evaluation. Multiplication by the actual quotient class `u` gives the stated positive-column period.

Both ordinary extension sequences have only fibre rows zero and one. Their only possible differentials are the displayed `d2` maps. The absolute row-one class times the shifted-relative row-one class has zero fibre-row-two target. Applying the product Leibniz identity gives TD.23 in a positive column. The two pairings there are perfect, hence the differentials are adjoints and have the same rank. This proves the equality of stable absolute and shifted-relative total dimensions, with the degree shift justified by the explicit period rather than suppressed.

The actual multiplication-by-`u` maps become isomorphisms on the two surviving positive-column rows and then on their finite filtrations. The same argument applies to each peripheral extension. Consequently every degree-zero localization in TD.25 is an actual high-degree group of finite dimension.

## Boundary half-rank: TD.25–28

For the specified self-dual finite module, localizing the actual long exact sequence produces the exact cyclic sequence TD.26. The connecting arrow is divided by one copy of `u`, exactly as written. Equality of the absolute and relative dimensions and the three rank identities give that the boundary restriction has half the boundary dimension. No degeneration assumption on either transgression was made.

## Brown comparison and duplicated restrictions: TD.29–36

The full finite-coefficient Brown theorem applies: `F` is open of finite 2-cohomological dimension one, and a finite subgroup of `E` injects into `E/F=C2`, so no `C2 × C2` occurs. Finiteness of each high cohomology group follows from its two finite fibre rows. The dense Brown image is therefore closed in the Hausdorff target and is onto. The identical argument applies to each actual peripheral extension.

For every cusp endpoint the proof chooses an actual `F`-conjugator to its specified global section. TD.32 is the exact cochain transport, including its action on coefficients. The homogeneous-bar right-translation map and the prism TD.33 prove that canonical inner conjugation acts identically on group cohomology. Under these six transports the global restriction map has precisely the three duplicated components in TD.35. This is stronger than matching dimensions or conjugacy labels and is the needed naturality statement.

The rank is therefore the sum of the three restriction ranks, while the target dimension is twice the sum of their dimensions. The half-rank equality forces each individual normalizer-to-section restriction to be onto.

## Finite coefficient witness: TD.37

For any nonidentity `c in C_i`, choose an actual finite quotient with kernel contained in `F` and excluding `c`. The retained quotient to `C2` makes the section inject and keeps its intersection with the finite kernel image trivial. The coset permutation module `k[J/Sbar_i]` has its specified invariant self-duality.

Positive section cohomology has the singleton cosets as a basis: every two-element orbit is a regular module and contributes zero. The two distinct singleton cosets `Sbar_i` and `cbar Sbar_i` are exchanged by the nontrivial action of `c` on the indicated basis vector. In contrast the image of restriction from the section normalizer is fixed by `C_i`, because the literal transport

`b(g_1,...,g_n) -> c b(c^{-1}g_1c,...,c^{-1}g_nc)`

is inner on the normalizer and acts on section cohomology by the coefficient action of `c`. This is TD.33 with `a=c^{-1}`, as the final text now explicitly says. Surjectivity contradicts the moved singleton class. Thus every `C_i` is trivial in the full profinite group.

## Primary source checks and scope

The original Wilkes paper was reopened for the augmentation/Hom definition, restriction, cup compatibilities and surface-pair duality: Definition 2.1; Propositions 2.3–2.4, 2.10, 3.1, 3.5, 5.7 and 6.16. Original accepted manuscript:

https://api.repository.cam.ac.uk/server/api/core/bitstreams/85a7dfb3-ae1a-4f65-b9cf-a088742b052d/content

The original Kochloukova–Zalesskii proof was reopened for Theorem 2 and its Section 1.1 finite-source consequence:

https://mat.unb.br/~pz/arquivos/Claus3.pdf

The proof's use of ordinary cohomology with the specified Hom module avoids the extra hypotheses of Wilkes's relative extension spectral sequence. Brown is used with its full finite-coefficient hypotheses and actual normalizers. No pro-2 replacement of the centralizer is made. No finite numerical certificate is needed for this cohomological proof.

The reviewed note proves the self-centralizer assertion and the boundary restriction calculation. Any later real-projectivity corollary needs its own stated source; exhaustion of the peripheral involution conjugacy orbit still requires an additional proof.
