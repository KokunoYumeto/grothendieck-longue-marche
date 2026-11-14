# D.7 addendum: rotation equivariance proved

The replacement `d_mu.tex` proves the affine and closed cases, and handles mixed orientation by passing to the intrinsic orientation-preserving subgroup and treating reflections separately.

## Noncompact case

The primitive orbifold cusp is the normalizer of any covering peripheral subgroup. Part A's distinctness and self-normalizer statements identify this normalizer after completion. If the covering generator is `w^n`, the loop condition gives `n a = n lambda` for the exponent of its image. Since multiplication by `n` is injective in the profinite integers, every orbifold cusp has exponent `lambda`. The abelianized orbifold relation then forces each local cone exponent to equal `lambda` modulo its cone order. Eliminating the last cusp makes this an equality in independent finite cyclic factors.

## Closed case

The exact primary input is Gareth Wilkes, *Profinite rigidity for Seifert fibre spaces*, Geometriae Dedicata 188 (2017), 141–163, Proposition 5.7; its arXiv v1 numbering is Proposition 6.6. Both the proposition and the proof were opened and read. The source is https://link.springer.com/article/10.1007/s10711-016-0209-6 and https://arxiv.org/pdf/1512.05587 . The publisher source corrects the theorem number relative to the preprint.

After removing the cone permutation by an orientation-preserving orbifold homeomorphism, Wilkes proves a single scalar `kappa` on every finite-coefficient H² with `kappa = k_j mod m_j`. The proof is a calculation for arbitrary automorphisms of the stated cone-preserving form; it does not use their origin from a Seifert-group isomorphism.

The new reduction identifies this scalar with the given surface orientation multiplier. The underlying surface orientation class pulls back to a class `eta` in orbifold cohomology. The geometric cone permutation fixes `eta`, even when it does not preserve the selected finite-index surface subgroup. Restriction of `eta` to that subgroup is `N omega`, where `N` is its index. Naturality gives `N kappa = N lambda` modulo every positive integer. Cancellation takes place in Zhat, where multiplication by N is injective, so `kappa=lambda`.

The single-cone signature is also reduced to a characteristic mod-two homology cover, with at least four cones, to avoid relying on an abbreviated single-cone step in the printed resolution proof. The no-cone case has no torsion.

## Orientation under finite covers

For a finite covering of degree d, the covariant map on the orientation line is multiplication by d. For punctured surfaces this is visible directly in the boundary-kernel model because the local degrees over each cusp sum to d. For closed surfaces it is the degree formula. A commuting square for an automorphism carrying one open subgroup to another gives `d lambda_cover = d lambda`; injection of multiplication by d in Zhat gives equality. Thus changing to a finite cover introduces no extra multiplier or undetermined local unit.

## Source readings

- Publisher full text opened as tool ref `turn86view0`; Proposition 5.7 and proof opened as `turn87view0`, `turn87view1`.
- Author's arXiv v1 PDF opened as `turn82view0`; Proposition 6.6 checked as `turn83view0`.
- Author's thesis opened as `turn78view0`; Proposition 4.3.6 and its full chain calculation read as `turn80view0`, `turn81view0`.
- Published bibliography metadata checked on the publisher page: DOI 10.1007/s10711-016-0209-6, volume 188, pages 141–163, issue year 2017.

## Approaches displaced by the proof

The integral relative H² rank-one argument fails because of its torsion summand. The direct finite-coefficient resolution and nonzero restriction to the surface orientation class supply the missing information. A separate attempt through unspecified drilling of cone points in a profinite group is unnecessary and was not used.
