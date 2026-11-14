# Focused audit of A.10–A.12, A.21, and E.15 integration

**Verdict:** the requested statements pass. No mathematical correction or added hypothesis is needed. The detailed arguments below check the arbitrary-cover, local-simple-connectivity, small-cofinal-presentation, and inverse-limit issues directly. Source fragments were not edited.

## A.10: the presheaf example and the two point arrows

Representables in a presheaf topos are connected projective objects. An epimorphic trivializing family for a locally constant presheaf can therefore be pulled back along any representable and split there: evaluating the family at the represented object supplies a member and a section. Consequently a locally constant presheaf restricts to a constant object on every representable slice. This makes its value maps along every arrow invertible.

Conversely, if a presheaf inverts all arrows, then its restriction to `D/x` is naturally constant: every object of that slice has its canonical arrow to the terminal object `id_x`, and the presheaf sends those arrows to isomorphisms. The representables cover the terminal object, proving local constancy. This verifies the identification of locally constant presheaves with representations of the groupoid completion rather than assuming it.

For the displayed finite category, `2` is terminal: the two maps from `0` to `1` have exactly the same composite to `2`. Every object has a unique map to `2`, so its groupoid completion is contractible. Each `D/x` likewise has a terminal object. Thus the global and representable-slice simple-connectedness claims follow.

The two point transformations are genuinely distinct. In inverse-image variance the arrows `a,b:0→1` give transformations `ev_1→ev_0`; the representable `D(-,1)` distinguishes them by applying the transformations to `id_1`. Constant presheaves send both arrows to the same identity. This proves the asserted failure of faithfulness without an ambiguity about inverse-image variance.

## A.11: the nucleus

The perfect-kernel assertions have an elementary second-countability verification. For a closed subset `F` of Euclidean space, let `P(F)` be its set of condensation points: every neighbourhood meets `F` uncountably. The set is closed, and `F\P(F)` is countable, because it is covered by the countable family of basis opens whose intersection with `F` is countable. It has no isolated points: an isolating neighbourhood would then have only countably many points of `F`. Every closed perfect subset of `F` lies in it, since a nonempty relatively open subset of a perfect Polish space is uncountable by the Baire theorem. This identifies it with the perfect kernel used in the source.

It follows directly that `P(P(F))=P(F)` and that the construction is monotone. Also

`P(F union G) = P(F) union P(G)`.

Indeed, a point outside both kernels has a neighbourhood meeting each closed set countably, obtained by intersecting the two witnessing neighbourhoods. These facts verify inflationarity, monotonicity, idempotence, and binary-meet preservation for `j(V)=R3\P(R3\V)`. Its fixed opens form the stated frame, with joins given by applying `j` to ordinary unions. The empty and full opens remain distinct.

A frame point of this quotient would give a point of the ordinary Euclidean locale. If that point is `x`, the open complement of `x` evaluates to zero there, although `j` sends it to the top element. This contradiction proves that the locale has no points. A geometric point of its sheaf topos would restrict to a frame point on subterminals, so the topos has no points either.

## A.11: arbitrary covers and connected components

Every ordinary open ball is fixed by `j`, because its closed complement is perfect. Such balls form a basis of the fixed-open frame: an ordinary union expressing a fixed open as a union of balls remains that open after applying `j`.

Suppose a family of fixed opens `V_i`, each contained in a ball `B`, covers `B` in the locale. Set `V=union_i V_i` as an **ordinary** open subset. The covering equation says `j(V)=B`, hence

`P(R3\V) = R3\B`.

Therefore the omitted set is exactly

`D = B\V = (R3\V)\P(R3\V)`.

It is countable by the single perfect-kernel decomposition, and closed relative to `B`. This argument works for an arbitrary indexing set. It does not form an arbitrary union of separate deleted countable sets, and it does not require a countable trivializing cover.

If a fixed open `W` has an ordinary connected component `W0`, that component is open. Its complement has no isolated point. An isolated complement point in another component would meet that other open component and contradict disjointness; an isolated complement point outside `W` would be isolated in the perfect complement of `W`. Thus `W0` is fixed as well.

A connected ordinary open subset of Euclidean space of dimension at least two remains path connected after removal of a relatively closed countable set. One direct proof starts from a polygonal path in the open set, covers it by finitely many convex balls, and replaces its local joins by two-segment joins through points avoiding the countably many forbidden lines. If a fixed connected open were a nontrivial coproduct of two locale opens, their ordinary union would omit one relatively closed countable set and their disjointness would disconnect that path-connected complement. This is impossible. Thus ordinary and locale connected components agree, and the connected ball basis proves local connectedness of the locale and its sheaf topos.

## A.11: simple connectedness and descent back to the locale

For `V=B\D` as above, a loop has compact image contained in the ordinary open set `V`. It therefore has positive distance from the closed complement locally along its compact image, and a sufficiently close polygonal approximation is homotopic to it within `V`.

For each polygonal edge and each point of `D`, exclude their proper affine span when choosing a cone vertex in the convex ball `B`. These are countably many affine planes or lines and cannot exhaust `B` by the Baire theorem. A point of `D` lying in a cone triangle but not on its edge would force the cone vertex into precisely the excluded affine span; the edges already avoid `D`. Hence the whole cone avoids `D` and contracts the polygon. The same argument gives a contraction in the global convex space `R3`. This proves the claimed simple connectedness. The phrase “planes determined by an edge and a point” in the source can be read as these proper affine spans; in the collinear case the span is a line, or one may choose any plane containing it. This is only an optional wording precision.

Any trivializing cover for a locally constant sheaf on the slice locale over `B` can be refined by subterminal opens, because subterminals generate a localic topos. Pullback preserves constant objects, so this remains a trivializing cover. Choose its fixed representatives `V_i`. On each fixed overlap, maps between constant sheaves are exactly families of set maps on connected components. The established component comparison identifies these with the ordinary maps of constant sheaves on the same overlap.

Thus the transition data define an ordinary locally constant sheaf on the ordinary open `V=union_i V_i`. This is an ordinary covering space: `V` is open in Euclidean space and is locally contractible. Its connectedness and simple connectedness make that covering constant. Restrict the resulting trivialization to the **original** `V_i`; the same component comparison makes these compatible locale sheaf maps. Effective descent for the original locale cover glues them over `B`.

No step regards `V` as a fixed open or an object of the locale. The source explicitly makes the correct descent-back step. Every ball slice and the whole locale therefore have only constant locally constant objects. The connected ball generators prove local simple connectedness, and the global envelope is `Set` as asserted.

## A.12: the neighbourhood limit and its size

For a covariant set-valued functor `p*`, the category of its pointed objects has arrows `(V,v)→(W,w)` given by maps carrying `v` to `w`. There is the density presentation

`p* = colim_{N_p^op} Hom(V,-)`.

The evaluation at an object `X` sends a representative `(v,f:V→X)` to `p*(f)(v)`. Every element is represented using `(X,x,id_X)`, and the pointed-object arrows impose exactly the required identifications. Applying natural transformations into `r*` gives the displayed limit over `N_p` in the source, with the correct variance.

A small initial subcategory is available. Choose a small full generating category of the Grothendieck topos, and retain all its pointed objects. Every pointed object receives a map from one of these, because the generating family gives an epimorphism and `p*` preserves epimorphisms. Two such presentations of the same pointed object admit a common refinement: take their fibre product over it and cover that fibre product by generators, choosing a lift of the indicated point. Parallel arrows are similarly equalized by a generator covering their equalizer. The relevant comma categories are therefore nonempty and cofiltered. This proves initiality for limits and justifies the source's small-presentation qualification.

Restriction to locally constant objects is evaluation at the universal pointed locally constant cover. Its injectivity and surjectivity are therefore exactly faithfulness and fullness. The connected-component criterion for the other functor also passes: connected components of the terminal object are locally constant subterminals, so they agree with the components in the envelope. A geometric point selects one such component; any point on that component hits the corresponding connected groupoid component up to isomorphism. Hence existence of a point in each component is precisely the stated condition, and enough points is correctly identified as stronger.

## A.21: the bicategorical limit is genuinely componentwise

Write `E_n = beta(C_n)` and let `B_N = Set^N` be the fixed discrete component topos. Every stage and every transition map is over `B_N`.

For an arbitrary test Grothendieck topos `T`, a geometric morphism `T→B_N` is a partition `1_T = coproduct_k U_k` by disjoint subterminals. It decomposes `T` as the coproduct of its slice topoi `T/U_k`. A map `T→E_n` over that partition is exactly a family of maps

`T/U_k → beta(Z/p^min(n,k))`.

A coherent cone to the tower has one common partition, since the transition maps induce the identity on the component index. Its groupoid is consequently the product over `k` of the cone groupoids for the component towers. Products commute with these limits. For a fixed `k`, the tail `n≥k` is cofinal and the corresponding tower is constant with value `beta(Z/p^k)`. Thus the cone groupoid is exactly the groupoid of maps `T→beta(D)`, naturally in every `T`, including its transformations. This proves the claimed inverse limit in all ordinary topoi.

The use of a different tail for each component is legitimate **after** commuting the two limits. It does not assert that there is a single uniform stage at which all components have stabilized.

## A.21: the pro-object is nevertheless not constant

A map from the pro-groupoid `(C_n)` to a constant groupoid `D` is represented, up to coherent homotopy, by one functor `C_n→D`, because mapping into a constant target is the filtered colimit of the stage mapping groupoids. Every source vertex group of this representative has exponent at most `p^n`.

If this pro-map had an inverse, its composite with the stage component of that inverse would be equivalent to the identity of `D`. At a vertex with automorphism group `Z/p^k`, for `k>n`, the composite homomorphism factors through a group of exponent at most `p^n`, so it cannot be an automorphism. Relabelling components does not alter this bound. Thus no such inverse exists.

One can see the same distinction at the level of objects. The regular action supported on the `k`th component descends to stage `k`, but the coproduct of all these regular actions descends to no uniform stage. The limit topos contains it, while the category of representations split at a single stage does not. This is exactly the difference the example is designed to exhibit; it is compatible with the intrinsic fundamental groupoid of `beta(D)` being the constant groupoid `D`.

The separate `Z ←times2 Z ←times2 ...` example is also correct. Its stated zero limit is the ordinary inverse-limit **group**. Maps of the progroup into constant `Z` form `Z[1/2]`, so the progroup is nonzero. No claim that the homotopy inverse-limit groupoid is the trivial groupoid is made. The final filtered-union assertion is valid because nerve simplices and the simplicial tests for homotopy groups use finite data; inverses and each finite test occur at a finite stage.

## E.15 integration check

The E.15 fragment in `deliverable/sections/E.tex` agrees exactly with `work/foundations/E_additional_reconstruction.tex` after normalizing the intentional `cite` to `citep` change. The integrated result register contains exactly one E.15 row, with canonical status `Proved`. The two required bibliography keys `FA_LurieHTT2009` and `FA_LurieHA2017` each occur exactly once in the integrated bibliography.

The enhancement, specified-constant-functor, and specified-evaluation qualifications are retained. The final paragraph still confines the open qualification to bare ordinary homotopy categories, and does not incorrectly extend it to the ordinary groupoid-presheaf topoi already reconstructed in A.8.

No source edits were made, and no additional optional mathematical testing was required. The integration comparison and register/bibliography presence checks were executed directly.
