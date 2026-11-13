# Independent audit of Part 1

The complete criterion draft was read before the environment outages. The core tubular, crossing, inertia and bar-obstruction arguments were found sound after the following corrections, which were communicated to and applied by the root author.

1. A normal-circle kernel presented as Z^r / image(partial) is a group, not necessarily a lattice. The conic in P2 gives Z/4. Calling it a lattice incorrectly excludes torsion.

2. The local closed-cover nerve is compared with incidence data after barycentric flag refinement. Arbitrary intersections of members of an ordinary cover are not automatically the named single strata.

3. Strict rank flags form a semisimplicial object. Repeated ranks and identity arrows must be inserted if a full simplicial nerve with degeneracy maps is used.

4. In the reconstruction theorem T is the refined open-stratum/iterated-link diagram, or an equivalent closed-face presentation. Unqualified closed intersections must not be used as though their asphericity followed from asphericity of the open strata.

## Checked primary sources

David A. Miller, Popaths and holinks, Journal of Homotopy and Related Structures 4(1) (2009), published Theorem 4.9. The theorem compares holinks and popaths for arbitrary two distinct strata and is endpoint-preserving. Original PDF: https://tcms.org.ge/Journals/JHRS/xvolumes/2009/n1a13/v4n1a13hl.pdf . Opened ref turn54view0.

Mikala O. Jansen, arXiv:2308.09550v3, 16 May 2024. Proposition 3.16 and Corollary 3.17 supply atlas descent; Proposition 3.24 supplies exodromy; Corollary 3.23 identifies groupoid completion. The finite codimension stratification satisfies the ascending-chain condition needed there. https://arxiv.org/pdf/2308.09550 . Opened refs turn54view1, turn57view3–4. Older search snippets used different numbering and were not relied on.

## Connectivity and bar obstruction

The map q from the crossing infinity-category to its homotopy category is 2-connected on classifying spaces. More generally, (r−1)-connected mapping-space components give an (r+1)-connected q. The bar filtration shows the shift: the first possible relative mapping-space contribution has internal degree r+1 and positive bar degree one, hence total degree r+2.

On the universal-cover relative bar spectral sequence, the only first-degree contribution is in bar degree one; its incoming d1 comes from bar degree two. The obstruction is therefore the stated cokernel. Higher differentials cannot reach it because the earlier internal rows vanish. Relative Hurewicz identifies that first relative homology group with the corresponding homotopy group, and the long exact sequence gives the displayed fibre degree. This computes the first possible obstruction. If its cokernel vanishes, it is not legitimate to assert a first actual failure without examining the next degree.

The categorical-to-topos distinction also remains necessary: the ordinary constructible topos determines ordinary exit-category data, whereas the enhanced reconstruction uses the full derived/space-valued diagram. Replacing the enhanced diagram by unqualified ordinary sheaves would erase the higher mapping data that the obstruction measures.

## Additional morphism audit, 12 November 2026

Conditional on the root's established good-implies-Mori-hyperbolic argument and Svaldi's nefness theorem, a proper birational morphism f:(Y,E)->(X,D) between smooth projective good SNC pairs is log étale. In fact the discrepancy step only needs Y good and X SNC.

Let A=K_Y+E−f*(K_X+D), with E the full reduced inverse-image boundary. The SNC pair (X,D) is log canonical, so A is effective and f-exceptional. Since K_Y+E is nef, A is f-nef. Negativity gives A<=0, hence A=0. The determinant of f*Omega_X^1(log D)->Omega_Y^1(log E) is the corresponding nonzero section with divisor A. It is nowhere zero: a nonzero section of a line bundle on smooth Y cannot have a nonempty zero set supported only in codimension two. Thus the logarithmic differential is an isomorphism.

Here is a chart proof of the remaining implication, without assuming a sharp-characteristic chart is enough. At y write D=(x1...xr=0), E=(y1...ys=0), f*xi=ui times product_j yj^aij for i<=r, and f*xi=gi for i>r. At y the log Jacobian has blocks [A B;0 C]; invertibility implies rank A=s<=r. Choose s pivot rows I with det A_I nonzero. Choose local logarithms of the units and set zj=yj exp((A_I^{-1}log u_I)_j). Then f*xi=z^ai for i in I, and f*xi=z^ai hi for i not in I, with hi units. The log-Jacobian condition implies that z1,...,zs, the r−s units hi centred at their nonzero values, and g_{r+1},...,gn form ordinary local coordinates. The morphism is consequently a monomial toric map times the identity in the remaining coordinates.

The fs chart is N^r -> N^s plus Z^{r−s}. Its exponent matrix consists of A and an identity matrix on the nonpivot rows. Its determinant is plus or minus det A_I, so its group-completion map is injective with finite cokernel, of invertible order in characteristic zero. The induced chart-base-change map is classically étale by the coordinates above. Kato's chart criterion proves log étaleness. Algebraically the required roots of units are obtained étale locally. It is important to include the unit Z-factors: the map of sharp characteristic groups alone can have positive-rank kernel even for a usual toric blow-up.

Primary source: Kazuya Kato (1989), Logarithmic structures of Fontaine–Illusie, in Algebraic Analysis, Geometry and Number Theory, pp.191–224, Theorem (3.5), published p.202. Original scan https://math.uchicago.edu/~drinfeld/p-adic_periods/Kato_log-structures.pdf , opened turn132view0, p.202 screenshot turn133view0; alternate original scan https://www.math.brown.edu/dabramov/LOGGEOM/Kato-log.pdf , opened turn134view0. The theorem's log-étale clause is precisely finite invertible-order kernel and cokernel plus classical étaleness of the chart-base-change map.

This proves toroidalness of the morphism and permits toroidal weak factorization. It does not prove that every morphism is a direct composition of stratal blow-ups, which would be a stronger factorization assertion.

For a rational map with both endpoint log canonical divisors nef, a common SNC resolution has effective discrepancies A_1,A_2. The general negativity lemma applied to A_1−A_2 over the first endpoint (it is relatively nef and has nonpositive pushforward) gives A_1<=A_2; reversing endpoints gives equality. The common effective discrepancy need not vanish, because the common resolution need not have nef log canonical divisor. Thus this observation establishes log crepancy but does not supply a common good resolution or a toroidal factorization of an arbitrary rational map.
