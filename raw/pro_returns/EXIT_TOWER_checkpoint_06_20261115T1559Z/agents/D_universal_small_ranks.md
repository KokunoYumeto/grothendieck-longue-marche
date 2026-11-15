# Exact first two full-level ranks in every genus

Proposed next D.39 after checkpoint06. No TeX or metadata changed during the freeze.

For every stable type with d=3g-3+n>k, the full and procongruence P0 are nonempty and disconnected, and both versions of P1 have exact connectivity zero. The full-level P2 has exact connectivity one. The procongruence P2 has nonzero continuous H2 with F2 coefficients and its fundamental group is exactly K_g,n by D.32. This last pair of assertions does not evaluate that congruence kernel.

The maps and cycles are as follows.

## Rank zero

Choose two distinct pants decompositions. Their finite sets of actual curves are separated at one congruence level by the valid curve-complex embedding (Boggi Proposition3.3 and Theorem4.2). Thus they determine two distinct vertices of the inverse-limit P0, separated by a clopen function. P0 has no positive-dimensional cells. This proves nonempty disconnectedness directly for either topology. At d=0 or k>=d, retain the already specified cone instead.

## Rank one

The ordinary P1 is connected by D.5, so every finite-level quotient is connected and the compact inverse limit is connected as in D.11. A finite top-dimensional cycle can be constructed by an actual core inclusion.

For genus zero use the core S0,5 after fixing d-2 pants cuts. Its finite pentagon is the one already used in D.12. For genus one use S1,2 with d-2 fixed cuts; Luo's actual curve-complex lift from S0,5 supplies a finite loop. In both cases excess labelled points are on a rational tail decomposed into pants.

For genus at least two, leave two once-holed tori and pants. Their joined curve complexes contain a square: choose two distinct curve vertices in each torus and take their four joins. For closed genus two the sole separating cut leaves the two tori directly. In higher closed genus, two separating cuts leave a complement of genus g-2 with two boundary components, and decompose that complement into pants. With punctures the same complement carries all of them. There are precisely d-2 fixed cuts. The map is union with these fixed cuts, on vertices and on all inclusions of face posets.

This square or core loop is a nonzero finite one-cycle in the one-dimensional P1. Separate its finite curve support at one congruence level. A dual edge cochain detects its image there; pulling back yields a continuous H1(F2) class on both completions. Thus their profinite fundamental groups are nonzero. This uses the actual closed lift, not just a finite-quotient loop.

## Rank two

Leave one core of complexity three and all other components pants; fix its d-3 complementary cuts. In genus zero use S0,6; in genus one use S1,3. Both have nonzero finite top two-cycles by the sphere theorem, and the actual inclusion is union with the fixed cuts.

For closed genus two use the full C2,0. For genus two with at least one marked point, first cut a nonseparating curve, obtaining S1,n+2. When n>=2 put all n ordinary labels on one rational tail and decompose it into pants. The result leaves S1,3 and exactly n=d-3 fixed cuts, as independently checked in D.36.

For closed genus g>=3, glue all three boundary components of a genus-one three-boundary core to a connected complement of genus g-3 with three boundary components. The dual graph has two vertices and three edges, so its first Betti number is two; the resulting genus is 1+(g-3)+2=g. Put all n ordinary labels on the complement, and decompose it into pants. The complement has complexity 3(g-3)-3+(3+n)=3g-9+n. With the three attaching cuts, the total is 3g-6+n=d-3. For g=3,n=0 the complement is already a pair of pants; this construction still applies exactly.

The core S1,3 has a nonzero finite two-cycle. Its union-with-fixed-cuts image is nonzero in the two-dimensional P2, hence cannot be a boundary. Separate its finite curve support at one congruence level. A dual top-cell cocycle detects it and remains nonzero after pullback to the full and procongruence completions. This proves the stated nonzero continuous H2(F2) in every case.

D.11 gives trivial profinite Pi1 of the full-level P2 for every stable type. The coefficient sequence into Q/Z, Pontryagin duality and profinite Hurewicz used in D.35 then give Pi2 nonzero; hence exact connectivity one. The procongruence Pi1 is K_g,n by D.32, which remains the exact unevaluated group in higher genus.

All the finite-cycle separations use actual finite curve supports and the same top-cell cocycle argument already proved in D.35. No ambient goodness, all-genus CSP, or completion-preservation of an arbitrary retraction is introduced.
