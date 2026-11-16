# Independent review of the product-of-two-trees lemma

Checkpoint21, 16 November 2026. **PASS** in the stated actual countable
CW scope. I independently derived the relative collapse before reading
the complete `work_CE/subcomplex_product_trees_freeness_21h.txt`, and
have now read that complete note.

For a leaf strip e x B, the edge at the new leaf above each B-edge is
incident to exactly one square and lies outside the preserved inner
subcomplex. The chosen free edges are distinct. Collapsing the squares
along those edges fixes all shared rungs and all inner edges. Graph
edges exposed in earlier strips do not affect this free-face condition:
they add no second incident two-cell. The relative collapse therefore
leaves the old subcomplex plus a graph whose intersection with it is
only a set of vertices.

The graph-of-components van Kampen argument gives the actual based
free-factor inclusion for each old component, even when components
merge. Successive finite leaf additions in each factor establish the
assertion for all nested finite rectangles. These are stronger data
than merely knowing that every finite-stage group is free.

For countable trees, finite connected subtrees give a cofinal sequence
of rectangles. At the chosen base vertex, every stage component group
is a free factor of the next. A compatible increasing choice of free
bases therefore exists. Every loop and null-homotopy is contained in
a finite subcomplex, so the union basis freely generates the full
component group. Local finiteness and finite valence are not required.

The same argument also shows that every higher homotopy group is zero:
a sphere map factors through a finite rectangle intersection, whose
component collapses to a graph. Thus each component is homotopy
equivalent to a graph, by the CW Whitehead theorem after realizing a
free basis. This optional strengthening is an abstract statement
about genuine cubical subcomplexes, not the actual nodal complex.

The warning in Section5 is essential. On the existing one-skeleton of
two adjacent squares, the two square loops are independent. Attaching
one disk along their outer boundary kills their product (up to the
specified whisker); attaching both squares kills both generators.
The equality of their cellular boundary sum does not identify these
nonlinear quotients. No actual node disk is replaced by all squares
of its chain support.

Consequently the missing actual comparison remains a simultaneous
graph/Tietze change carrying the whole transported node family to
unit-square relations, with complete based words and redundant
relations treated. Individual primitive elements and the faithful
linear boundary representation do not supply it. B105's actual
spherical pair shows that a homotopy equivalence of the present
two-complex with a graph cannot be asserted; a pi1 comparison may
still be possible after separately accounting for the redundant
two-cells. No actual M freeness or fixed-cone conclusion follows yet.
