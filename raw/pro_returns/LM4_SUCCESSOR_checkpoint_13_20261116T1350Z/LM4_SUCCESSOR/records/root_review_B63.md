# Root review: B.63, the actual first 3-adic lift

Reviewed 16 November 2026, approximately 06:15–06:20 UTC. Accepted
after reading the complete formal proof and both direct certificates.
The independently authored root program is
`code/verify_B63_first_lift.py`, with actual passing output beside it.

The root implementation uses the integral invariant-covector hyperplane
instead of the discovery fixed-line quotient. It independently forms
the nineteen geometric braid matrices, enumerates the two mod-three
images, constructs new Schreier transversals, and computes their full
mod-nine identity-fibre spans. The orders 144 and 1440, edge counts
1872 and 8640, dimensions six and nine, and combined rank twelve
all agree. The upper bounds are exhaustive images of source-kernel
generators, not reductions of integral homology constraints.

It then evaluates all six actual tetrahedral normal-kernel words,
all nine cyclic words, and all three short matched pairs. Literal
substitution e11=e6^-1 e5 e6 makes every tetrahedral word freely
trivial, proving membership in the normal closure of the stated h.
Their ambient integral homology is zero. The cyclic words have
exact zero source abelianization. The respective bases span the
entire previously bounded fibres, so these source restrictions do
not reduce the first-lift image. The three matched pairs have source
lengths 38/16, 94/54 and 88/54 and span the full intersection.

The root check also verifies all displayed matrix Lie brackets, the
two-dimensional abelian derived ideal, the explicit nonnormality
witness under e1, and the factor indices 3888 and 1049760. It compares
the discovery coordinates only at the end through the integral basis
change. The source table labels cyclic generators 0 through 5, while
signed word certificates use 1 through 6; the independent code makes
that conversion explicit. An initial local verifier attempt omitted
this conversion; correcting it resolves the indexing mismatch without
changing any mathematical certificate.

The profinite deduction is in the correct direction. B.62 first
kills the mod-three image of every actual k in K. Membership in both
completed subgroup closures then puts its mod-nine image in both
identity fibres. Thus the actual image is contained in the proved
three-dimensional subgroup W9. The preimage M9 is an open subgroup
of P and is strictly smaller than N3; it need not be normal and the
explicit conjugation test shows it is not. The B.52 factorization
ambiguity lies in K, hence in each finite-index subgroup containing
M9. This proves the stated closed products for both refinements.

The matrix Lie bracket is distinguished from the group commutator in
the abelian mod-nine fibre. The solvable Lie algebra is not asserted
to identify the full integral A5 centralizer. Matched source words
in one finite quotient are not an actual common element of the two
closed subgroups. No nonzero element of K and no higher-level
compatible family is constructed.
