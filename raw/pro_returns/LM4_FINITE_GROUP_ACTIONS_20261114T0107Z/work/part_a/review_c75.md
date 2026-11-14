# Independent audit of C.75

**Result: PASS for the current written proof and corrected statement.** I read `work/part_b/c75.tex` and `c75_result.json` in full, reread the actual principal-bundle and component-coordinate construction in C33, and reread the complete C62 excursion triangle and closed-zero-set argument. The current statement has the three distinct endpoint-character alternatives requested by root; the previous ambiguous “Otherwise” is absent.

## Actual coordinates and source paths

On the specified plane, C33's actual product principal bundle has neither a circle fibre nor a circle base, since either would contribute a nontrivial fundamental-group factor. Thus its two coordinates are real lines. Commutation with the labelled fibre translations gives the exact skew-product form, composition and inverse formulas. The generator paths ensure that every base map is increasing.

The symmetric compact set of generator values and inverse values is path connected and contains the identity. Each finite product is compact and path connected. Formula C75.7 gives a continuous path to each original finite word, with all original source factors retained. Consequently no element or path from a larger closure is needed.

The common fixed set of the base generators is closed and is the fixed set of the generated base group. Each nonfixed base orbit is an interval: its compact finite-word evaluation images are increasing connected intervals. A path moving a point and its inverse give orbit points on both sides, making the orbit open. Every finite endpoint is fixed by every increasing map preserving that orbit. These facts identify the orbit with the exact complementary component of the common fixed set.

## The word triangle in the product plane

C62's winding proof uses only a genuine product plane, proper real horizontal fibres, increasing base maps and an exact equality of the endpoint levels. These are all present here without an open-orbit assumption. On each excursion, the two displayed tracks lie strictly on opposite sides of the fibre, and the actual word triangle has nonzero boundary winding about every interior point of the horizontal interval. The closed-zero-set interpolation supplies the full interval, including accumulation of excursions.

For a path of source words in `P^m`, all triangle values are in `P^(3m)`. In particular the interval inclusion is an assertion about actual source words fixing the selected base point, not a connectedness inference about a potentially nonclosed stabilizer.

## Strip classification and topology

The fibre-displacement stabilizer is an additive subgroup. Conjugating by an actual source map taking one base point to another preserves the real displacement, because the skew-product translations cancel. It is therefore constant on each base orbit. The word triangle makes a nonzero displacement give a full interval of displacements; additivity then makes the subgroup all of R. Base transitivity gives the entire open strip as an orbit.

In the zero case each horizontal fibre contains exactly one point of the selected orbit. The resulting graph is continuous for the following precise reason. A compact finite-word evaluation image maps bijectively to its compact base interval, hence homeomorphically. Those intervals increase and exhaust the open base interval. Every point is interior to one of them after choosing two neighbouring base points and a sufficiently large finite-word bound. Thus the inverse projection is continuous locally everywhere. The proof does not replace the actual orbit topology by an assumed graph topology.

Horizontal translations commute with the source group, so the translated graphs are all its other strip orbits. Their invariance gives the displayed coboundary equation for the skew translation. The two coordinate maps are inverse and conjugate the effective image exactly to `id_R × beta`. Both directions are continuous for maps and inverse maps on compact sets, by the explicit product map and section evaluation. No quotient-topology assertion for the original restriction map is made.

Each graph is a proper embedded line in its stated strip: it is closed there and projects homeomorphically to the base interval. At a common fixed base point the shift evaluation is a continuous homomorphism from the path-connected original group, so its image is zero or R. This proves all of the listed orbits and the precise horizontal frontier of every open strip.

## Endpoint character and source-label comparison

Evaluation at the fixed endpoint gives the continuous additive character `c_a`. The comparison action `T_a(g)(z,t)=(z+c_a(g),beta_g(t))` is a literal homomorphism with the written kernel. The original finite-word paths map to its actual paths, so the same strip proof applies to its image without any assumed closedness, faithfulness or local compactness of that image.

Its fibre stabilizer is exactly `c_a(G_t)`, giving zero or R. In the full case the proof produces actual source elements fixing the specified base point with every real endpoint displacement. It does not assert a continuous choice of those elements.

In the zero case the graph gives the functional equation C75.11. A nonzero character has full real image by path connectedness, so the graph function is onto R. The injectivity argument is sound: two equal values force an interval of constancy or an interior local extremum. Base transitivity transports such local constancy or local extremality to every point. In the extremum case, every image value is the maximum or minimum on one rational compact interval in its corresponding local neighbourhood; hence the image is countable, contradicting its connected, surjective real image. Thus the function is an actual interval-to-R homeomorphism. This proves exactly the three alternatives now stated.

## Component operators and remaining scope

C33 supplies the actual cyclic component operator when it exists. The stated affine formula and inverse give the exact transport in both directions, including negative fibre scaling. Direct composition with a source skew product gives C75.13; the retained constant translation cancels. The common fixed set, strip type and endpoint character therefore transport as claimed.

The final qualifications are necessary and accurate. Properness of the graph was proved only in its open strip. Neither an endpoint extension of that coordinate, a continuous selection of correcting words, nor a contraction at the original outer circle is obtained. C74's obstruction remains compatible with this orbit classification. No numerical certificate or new external theorem is required for this qualitative proof beyond the explicitly checked C33 and C62 inputs.
