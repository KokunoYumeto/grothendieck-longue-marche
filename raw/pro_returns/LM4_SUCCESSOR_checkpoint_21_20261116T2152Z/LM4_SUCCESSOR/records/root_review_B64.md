# Root review: B.64, the entire common 3-adic image

Reviewed 16 November 2026, approximately 06:27–06:30 UTC. Accepted
after reading the complete proof, the full integral centralizer
program, the exact output, and CE's independent audit. Root reran
the exact program successfully; output is records/root_B64_rerun.out.
The lower-bound word calculation was already independently rebuilt
in the root B.63 verifier.

The twelve-strand closed-cover model is the correct integral lattice:
ker(epsilon)/Z·1, of rank ten. Capping removes the primitive boundary
class. The actual certified periodic braid matrices, with the stated
sign correction, generate an honest A5 of order sixty and have
character twice the irreducible degree-five character. The latter
has a rational realization as the augmentation of the six-point
action. The change from this geometric marking to B.61's marking
uses the proved discrete conjugacy and hence an integral symplectic
isomorphism, not an unproved congruence comparison.

The exact commuting algebra has rational dimension four. The
displayed I,H,E,F are independent modulo three in the ambient matrix
lattice and satisfy the complete multiplication and adjoint identities.
Thus they are a primitive Z3 basis of the saturated commuting order.
They identify it with the level-three Eichler order and identify the
symplectic adjoint norm with the two-by-two determinant. Projective
centralizers add no sign-twisted elements because A5 has no nontrivial
character to C2.

The filtration is handled correctly. Ambient congruence modulo three
means 1+3O, not ordinary entrywise congruence in the two-by-two model.
The resulting lower-left coordinate is divisible by nine. The group
of norm one is exactly the displayed three-parameter principal group.

The all-level lower bound uses the connected DERIVED algebraic
centralizers of A4 and C5, of dimensions six and nine. The source
words are actual commutators or differences of conjugates, so their
linear images lie in those derived groups. Squaring removes possible
projective signs while multiplying the first vectors by the unit two.
The independently checked six and nine vectors form full bases
modulo three of the respective saturated Lie lattices.

The logarithm comparison does not assume an integral decomposition
into multiplicity factors at the bad prime. If g=I+3X is integral,
the eigenvalues of X are algebraically integral. Every block
determinant therefore lies in 1+3O_K, even if its projectors have
denominators divisible by three. Scalar logarithm is injective there;
conjugacy-invariant convergence gives the block determinant/trace
comparison. Symplectic and centralizer equations commute with log
and exp. Hence the actual principal groups are exp(3L), and their
successive congruence fibres are exp(3^r L).

Successive cube approximation proves generation directly. Cubing
exp(3^r X) gives exp(3^(r+1) X), and the initial basis consequently
spans every successive quotient. Matching an arbitrary element one
level at a time gives a convergent product in the closed generated
subgroup. Thus the squared source words generate the entire two
derived principal groups in their respective 3-adic images.

The common A5 centralizer SL2 lies in both derived groups, giving
the lower bound. The upper bound needs only that the two source
closures centralize A4 and C5, which generate A5. It does not infer
the absence of deeper torus directions in either individual full
monodromy image from a first-layer rank computation. This precise
scope avoids that potential gap.

The resulting equality is a representation-level intersection with
separately compatible source lifts at all powers of three. The
tetrahedral source remains in the closed rigid normal kernel and
both sources in their closed commutator subgroups. The two lifts
need not coincide in the full mapping class completion. Consequently
the actual image of K is only known to be contained in this group;
neither K=1 nor a nontrivial element of K follows.
