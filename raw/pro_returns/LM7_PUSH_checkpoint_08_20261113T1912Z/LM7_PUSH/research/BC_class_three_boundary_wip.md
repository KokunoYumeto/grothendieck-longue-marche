# Class-three boundary refinement — work in progress after checkpoint05

The checkpoint05 sources and certificates remain unchanged.  This exploration
starts from the actual groups `H normal F normal B`, the ten signed Schreier
generators of E.26, and the complete E.24 common source `D23`.

## First representation selected

The first target is `B/(gamma_4(H) H^3)`.  It retains the actual quotient
`B/H` of order 54.  The exponent-three class-three geometric quotient has
coordinates of dimensions 10, 45 and 120.  The last term is obtained from
the restricted Magnus degree-three term (ordinary Lie dimension 330 plus
ten generator cubes) by the complete 220-dimensional central cube span.
The actual projection on a triple `i<j<k` is the coefficient of `ijk`
minus that of `jik`.  This kills every cube and sends
`[eta_i,[eta_j,eta_k]]` to the corresponding unit vector.

The new module `code/bc_fermat_class_three_burnside.py` records this quotient,
the literal based `s,r` substitutions, the comparison to E.33, and explicit
cube-span preimages.  No class-three lifting conclusion is asserted before
the exact norm and source-image calculation is complete.

## Exact source-image route

E.33 supplies actual source-kernel words mapping to every degree-two
commutator.  Bracketing each such word with an actual `H` generator gives
all 120 triple directions.  Because the source kernel is normal, these
brackets remain in it.  Fourth powers clear its exponent-two binary
image while preserving the exponent-three target.  Therefore the new
source image can be proved to be the full inverse image of the E.33
source image.  The planned certificate retains the old normal-relator
provenance and the new bracket word preimages.

For each of the nine E.33-admissible target abelian vectors, the remaining
norm equations are linear in its ten old central parameters and the 120
new triple coordinates.  This permits a complete finite calculation over
all 432 retained multiplier-one source points without enumerating a
3^175 group.

## Executed first result: E.44 draft, outside checkpoint05

All three new programs pass.  The exact triple norm matrix has rank 98
and nullity 22.  In each of the nine abelian cases the combined matrix
on the ten old central parameters plus 120 new coordinates has rank
103 and is affine-solvable.  Thus all 432 source points survive, each
with 3^28 correction images.  Exactly 3^6 of its 3^11 E33 images lift.
The source kernel has the full new central image, by actual brackets
with the previously certified integral adjusted relators in `H'`.

The comparison with the entire E37 tower gives joint rank six for
the old two and new five conditions.  Four independent congruences
remain on the eight free E37 Smith residues.  Their three 4-by-8
matrices depend only on the actual source residue c; all nine right
sides are printed in the new certificate and E.44 draft.  Each source
retains 3^5 of its 3^9 E37 reduction points and 3^27 compatible new
class-three images.  Its complete compatible three-adic fibre has
the explicit parametrization `Z3^10 x F3^22`.

The specific E37 point `u=w=0`, `Y37=1`, `Y38=...=Y44=0`, over actual
source row0 parameters(0,0;0), has integral class-two norm zero at
every precision but fails the new first equation `Y37=0 mod3`.
The exact central vector and an annihilating norm functional are saved.
This is a new obstruction after the full class-two tower, not merely
a repetition of E37's nonlifting P3 point.

The new triple corrections have actual word preimages in
`ker(B->D23) intersect gamma3(H)`.  Therefore they preserve every
class-two factor integrally.  Three-supported continuous powers
retain the new finite target and preserve every full pro-p H factor
for p different from three.  The actual common-source generation
proof retains the rank97 Frattini quotient and the stable two-primary
lower-central image, as in E41/E42.

Draft: `sections/E_class_three_boundary_agent.tex`, statement E.44.
It is not included in the main manuscript and awaits root audit.

New executed files, each with `.out`, `.json`, `.npz`:

- `code/bc_fermat_class_three_burnside.py` (0.880 seconds).
- `code/bc_fermat_class_three_norms.py` (0.952 seconds).
- `code/bc_fermat_class_three_tower_comparison.py` (0.251 seconds).

No discarded numerical approach was needed: the full ordinary
330-dimensional Lie centre was explicitly reduced by the actual
220-dimensional cube span before solving.  The initial finite E33
comparison was retained, and the stronger integral-H-prime word
preimages were added for simultaneous tower compatibility.
