# Independent review of the complete inner bad regional presentation

DE full proof review, checkpoint22: **PASS at the stated slit and annular
presentation scopes.** Inputs read completely:

- `work_CE/inner_bad_regional_presentation_22h.txt`;
- `work_CE/code/inner_bad_orbifold_braids22.py` and the retained complete
  path/word records;
- `work_CE/code/certify_inner_bad_deformation22.py`, its genuine output,
  and `inner_bad_deformation22.json`;
- both exact cone normalization producers and their full records.

## Actual geometric family and common marking

The substitution (z=1/t, y=z^2) gives the actual bad orbifold disk,
with cone (0), ordinary branch (q), and four (h_i^2) punctures.
At a zero of (h_i), the cone is removed from that critical fiber.
The proof retains this phenomenon as a cone-contact block; it does not
treat it as an ordinary transverse node in the quotient plane.

The stated radial plane-to-disk function is continuous, strictly
increasing from radius \(\rho\) to (1), fixes all radii at most
\(\rho\), and varies continuously with (q). It fixes the cone and
all moving punctures and also applies at their critical coincidences.
Thus the far plane section is a genuine extending section of the
actual disk family, with a fixed continuous lift to the ordinary
double cover.

The uniform compact-path comparison is explicit: all parameter paths
have \(|q|<19/20\), all four Blaschke centers have norm below (3/5),
and hence \(|h_i|<155/157\). Therefore all six points lie inside
radius (49/50), with a strict deformation margin. The radial
connector from that radius to (10/\mathrm{ROT}\) lies in an empty
annulus. This is one shared based connector.

The initial marking has an additional independent exact check:
`check_inner_bad_initial_marking22.py` verifies the physical order
\([h_1^2,0,h_4^2,h_2^2,h_3^2,q]\), every adjacent projected gap
greater than (1/100), all four (h_i) coordinates greater than

\(1/4\), and all five ordinary projected heights greater than

\(1/4\). These gaps are far larger than the uniform deformation
error. The upper-comb disk avoids the cone. Its analytic square-root
branch therefore selects exactly the four (h_i) and the first-quadrant
branch, simultaneously. The first-neck (K\) is literally the five
ordinary initial generators, with the one stated connector.

For the radial comparison to the first unit-circle neck,
\(\operatorname{Im}Q\ge100/29\), \(c_j<7/5\), and
\(\lambda_j>2/3\) imply
\(\operatorname{Im}A_j>1\). Thus every (h_j\) stays in the same
first quadrant. Opposite-sign node or cone collisions are impossible
on this path; same-sign and branch collisions occur only at the
excluded fifth-root boundary. The regular common lift is preserved.

## Critical completeness and deformation

I checked the four rational factor identities for arbitrary parameters.
They exhaust cone contacts, pair coincidences, branch contacts and
poles. They give precisely four cone contacts and six ordinary quotient
nodes at nine filled base values. The simultaneous (14/23\) value
contains two disjoint nodes, with exact order

\[
2\sqrt5-5 < (\sqrt5-3)/2 < (2\sqrt5-5)/5 < 0.
\]

Thus the retained branch lies between them. Their separation exceeds

\(2/5\). The old value (q=0\) is separately retained.

The independent Fraction path audit covers all fifty segments and the
distinguished-lasso system, including the thin corner-to-center
triangles. It proves \(|q|^2<9/10\) and rounded-critical-center
distance at least (10^{-4}\), and excludes other critical centers
from every triangle. The true-center rounding and coefficient errors
are below (1/400000\), safely smaller than these margins.

For the coefficient deformation, the exact radical intervals give
Euclidean error below \(\varepsilon=2\cdot10^{-30}\). True pole
norms exceed \(\sqrt3\), so denominators remain above (7/10).
The smallest critical denominator \(|u_i+u_j-1|\) is
\((3-\sqrt5)/2>3/8\), so along the deformation it remains above

\(3/10\). Subtracting the rational expressions gives the claimed

\(5\varepsilon\) alpha and \(32\varepsilon\) beta bounds.
The extra split old roots remain within (10^{-27}\) of the unit
circle, outside every path. The split (14/23\) values remain inside
their one assigned square. These statements use the complete
factorization, not a selected numerical list of collisions.

The numerator and denominator variations in (h\) are bounded by

\(4\varepsilon\) each. With the (7/10\) denominator margin and

\(|h_{\mathrm{true}}|<1\), the stated bound
\(|h_{\mathrm{deformed}}^2-h_{\mathrm{true}}^2|<100\varepsilon\)
is conservative. It also preserves the empty outer collar and the
initial order/lift margins.

## Actual word and van Kampen conventions

`verify_inner_bad_words22.py` is a separate implementation using
chronological left substitution. It checks every positive push,
negative inverse, boundary product, and actual local back transport:
ten actions, 120 inverse identities, all ten full relation words,
and both twelve-entry Nielsen compositions.

The positive base relation is exactly
\(g^{-1}xg=\mathrm{push}(x)\). The geometric push for a chronological
word (W\) is \(\operatorname{art}(\mathrm{reverse}(W))\), and
the back transport is \(\operatorname{art}(-W)\). The existing
independent implementation confirms this convention rather than
assuming the old right-composition formula.

An ordinary node supplies one transported commutator. A cone contact
supplies \([p,c'pc'^{-1}]=1\), with \((c')^2=1\). This is exactly
the full fourth-twist variation: it says \((c'p)^2=(pc')^2\), hence
both local generators centralize the square; conversely its cone
variation already implies this commutator. At the simultaneous value
the standard local supports are disjoint, so both commutators remain
separate. The actual far section extends over all inserted disks.
The resulting slit presentation therefore has precisely the ten
relations; no fiber injectivity is assumed.

The annular presentation retains the actual (q=0\) base generator
and its six based push relations. Its fiber quotient uses the normal
closure of every signed (q=0\)-translate of the ten node relations.
The proof correctly does not assert that the finite ten-relator
quotient is already invariant under this operator.

## Cone normalization and exact limits

The same-sheet triangular basis change is explicitly invertible and
normalizes the four cone contacts. It need not preserve the natural
first-neck (K\), which is explicitly stated. The separate exact
free-product replay verifies the three failures of the specified
untwisted product target. These are failures only of that marked map,
not an abstract nonisomorphism theorem.

The actual fixed-cone source identification is proved separately in
`inner_fixed_source_identification22.md`, using the same raw pushes and
one common Borel whisker. All files here concern the actual regional
models. No whole-base, all-neck, or main marginal-kernel conclusion is
silently added.
