# Exact induced 3.A6 source: completed source gate

This note records the completed source calculation after the separately
frozen cover and target models. It does not yet assert the E.60 whole
CM/pentagon fibre result. The continuing fibre and signed-source work
uses new filenames and leaves this package unchanged.

## Actual base maps

Write U for the explicitly enumerated order-1080 matrix group and
T_U for its Ferrari target. All six evaluation pairs and all six B/F
cosets are retained in the actual map

    rho_U : B -> G_U <= T_U wr (B/F).

The two specified projections are the old full A6 source G_A6 and the
324-point affine-three source. The latter has order 46656. It does not
factor through G_A6: the saved relation word is the identity in the
entire old source and has affine order four. This is a comparison of
these actual homomorphisms, not a CM-fibre exclusion.

Their actual joint image B0 has order 8|G_A6|. Its complete stabilizer
chain has 873463 final Schreier relations. Adjoining the ordinary
level-twelve map q12:B->Q12 gives the same order, with all original
generator maps retained. The kernel of B0->G_A6 is an explicit Q8.
Its map to Q12 is injective: the two saved kernel words generate eight
affine values, eight modular values, and their joint graph has eight
elements. The complete eight-element multiplication table is checked.
Consequently the specified projection gives the isomorphism

    B0 = im(B -> G_A6 x Q12).

The accepted literal map G_L->Q12 therefore makes B0 an actual quotient
of the E.54 A6/G_L common source. No abstract order comparison is used
to invent a quotient map.

## Complete ternary kernel

The kernel of the ambient Ferrari projection to A6 and affine-three
has 159 coordinates per evaluation: 53 central translations and 106
cross-character coordinates. All 36 evaluations give 5724 ambient
F3 coordinates. Their group law is ordinary addition, with the exact
outer automorphism centre character retained in source conjugation.

The complete lifted presentation evaluates all 873463 base relations,
then closes their images under the actual s,r conjugations. The result
is an elementary abelian kernel K of dimension 79. It is the entire
kernel of rho_U(B)->B0: killing that normal relation image makes all
normal-form relations hold, bounds the resulting order by |B0|, and
the specified projection still surjects to B0. All original generators
occur among the strong generators used in that presentation.

An independent Python program replays all 79 saved literal B words in
both actual source maps, and checks all 158 source conjugations. The
C++ collector also agrees with 192 independently prepared group-law
controls and 318 kernel-coordinate/conjugation controls. Thus

    |G_U| = 8 * 3^79 * |G_A6|.

The literal images of x and y have 120th powers one. Their old quotient
has ordinary F abelianization (Z/120)^2. The same exponent map and
upper bound therefore give rho_U(F)^ab=(Z/120)^2, and K is contained
in rho_U(F').

## The new perfect residual and the three retained coordinates

Let C be the accepted perfect normal subgroup of the A6 source, embedded
in B0 by its identity affine coordinate, and let E be its entire
preimage in G_U. The exact C-action on K gives [C,K] of dimension 52.
Its quotient K/[C,K] therefore has dimension 27. In the central
extension E/[C,K], retain the ten literal C generator lifts and all
27 central generators. A relation R(c_i)=k gives the abelian row

    (ordinary exponent vector of R, -coordinate of k).

All ten original-to-normal-form links and all 720615 complete C
Schreier relations are evaluated. The resulting 37-column matrix has
rank 34. Its 34 independent relation words are separately replayed in
the full Python source collector and in the old faithful permutation
model, with all signs and ordinary exponent vectors checked. The first
ten columns have rank ten. It follows that

    E^ab = F3^3,       dim(K intersect E') = 76.

This conclusion is exact, not an upper bound from selected relations:
the entire presentation was exhausted. The three quotient characters,
their values on the ten literal lifts, their map on all 79 kernel
coordinates, and the induced B and H actions are saved in the replay
NPZ. The actual F-action on these three coordinates is trivial.

Every choice of lifts is retained. Replacing the ten lifts by central
shifts with matrix A in Mat_(10x27)(F3) changes the row matrix by

    [[I_10, -A], [0, I_27]].

This matrix has inverse obtained by replacing -A by A. All 270
elementary column changes are independently checked; their products
give all 3^270 choices. Thus the rank calculation does not fix a
preferred central lift in place of the full fibre.

Here E' is perfect. The following elementary argument supplies this
fact without another unproved stabilization assertion. Put D=E'.
Since E/K=C is perfect, E=KD, and abelianness of K gives

    D = D' [D,K].

Taking commutators with K and using [K,K]=1 gives
[D,K]=[D',K]. The three-subgroup commutator identity places the latter
inside [[D,K],D], hence inside D'. Therefore D=D'. Since B0/C is
solvable and E/E' is abelian, G_U/E' is solvable; E' is exactly the
kernel of the maximum solvable quotient of this specified source.

The 76-dimensional kernel of K->E^ab is retained explicitly. The
additional three-dimensional solvable layer must be included in the
next complete CM/pentagon calculation.

## Replay provenance

The initial central process was lost across the runtime transition.
Its stdout and stderr were both empty, and no result JSON existed.
Those byte-for-byte logs and their status are preserved as
`de_a6_triple_central_incomplete_runtime.*`. The unchanged program was
restarted and completed in 463.064 seconds. This is a completed new
execution, not a reconstructed claim about the incomplete process.

The complete main kernel run took 580.937 seconds. The independent
79-word replay took 22.946 seconds. The independent central relation
and all-shift replay took 10.908 seconds. Elapsed times are provenance;
the exact words, coordinate maps, relations and ranks are the claims.

The source/base/central package is described in
`DE_a6_triple_source_replay.md` and frozen by its separate manifest.
