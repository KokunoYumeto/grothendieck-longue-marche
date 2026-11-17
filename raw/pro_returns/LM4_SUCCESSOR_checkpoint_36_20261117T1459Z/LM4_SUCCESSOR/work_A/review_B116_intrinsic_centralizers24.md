# Independent full-source review of B116

Reviewer: A/involutions. Read in full:
`records/proposed_B116_intrinsic_centralizers24.tex` and
`records/prefix_intrinsic_centralizers_candidate24.md`.

**Decision: PASS. No mathematical amendment requested.**

The actual regional presentation includes all ten node-edge types and
all D and integer-level translates. The inverse maps to
`A(Omega) semidirect (D times Z)` agree on every original generator
and every named graph vertex, so the calculation concerns the entire
actual regional group, before the cross quotient.

I independently reconstructed both links. For a=(T,a,0), the diagonal
and two same-height cross families give precisely the three families
`(k^m CT,U,0)`, U=a,d,e, and the same-coset a--b edge gives b=(T,b,0).
For B=(CT,b,0), its diagonal gives `(C k^m CT,b,0)`, the same-coset
edge gives (CT,a,0), and the two forward edges give the d/e families
at level1. There are no missing backward edges of b type. Free-product
normal form gives the stated intersection `{(T,b,0),(CT,a,0)}`.
The parity and height argument proves that the whole first link is
discrete; this is not a finite-height verification.

The elementary HNN centralizer argument is valid for an arbitrary
infinite graph. With stable letter x over its full link group L,
x and xy have translation length1, so their centralizers act on their
axes by integral translations with the displayed element generating
the image. For xy, the first two edge stabilizers are L and
xy L y^-1 x^-1. On their intersection x centralizes every element of
L, reducing this to L intersect y L y^-1. The second HNN splitting,
with stable y, applies because y is not in lk(x); Britton reduction
forces the conjugated element into lk(y). The common-link subgroup
commutes with x and y and fixes the initial edge, hence the whole axis.
This proves equality of the pointwise stabilizer and supplies the exact
direct product, not merely a containment. Full graph subgroup
intersections follow from the commuting deletion retractions.

For the passage back to R, abelianization of the actual graph kernel
retains every coordinate and is unaffected by inner conjugation.
Centralizing a therefore forces height0 and coarse g in T. Its
remaining kernel centralizer is exactly the already computed one;
k fixes b and shifts each of the three other link families. Eliminating
the orbit generators yields `Z_a times (Z^2_(b,k)*F(CaC,CdC,CeC))`.
For aB, the two distinct family labels cannot be exchanged by the
coarse action, so both coordinates must be fixed separately. This
forces height0 and g in `T intersect CTC=1`. The common-link formula
then gives `Z_(aB) times F(b,CaC)`.

The ranks6 and3 of the two abelianized centralizers are correct.
Their inequality excludes any discrete automorphism taking a to aB,
regardless of what happens to k. The proof does not assert a completed
centralizer formula or carry nonmembership through the cross quotient.
No unread Servatius theorem is used: the needed special case is proved
inside the source using explicit HNN normal forms.

The earlier fixed-k finite-head argument also received a complete
proof/code/output read. Its 34-vertex,96-edge period4 graph is the
actual B112 head. The nonadjacent seed vertices k0 and bar(b0), the
eight equivariant translates, and the substitution B=C b C,
f=h k^-1 give a genuine finite quotient detecting [k,aB]. The
prefix basis substitutions are literal. This review does not rerun
or mutate the root producer or its preserved output.
