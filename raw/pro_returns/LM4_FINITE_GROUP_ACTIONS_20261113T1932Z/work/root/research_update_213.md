## Five further proved claims: controlled localization, frontier kernels, torus covers, and the reflection equalizer

This update registers C.64, C.65, D.66, D.67 and F.12. Every one has a
complete proof in the paper and an independent proof audit. The report
remains INCOMPLETE: C.12, D.12 and F.7 retain the exact unresolved general
claims. The new statements prove the maps and subcases described below;
they do not change those remaining statuses by inference from finite
computations.

### C.64: one compact controlling family and actual localized contractions

We retain the original global plane maps, every selected original cover,
all deck labels, and the full operator restrictions in a closed compatible
Polish group. The group of based paths in its generated closure acts
transitively on each selected original open orbit by endpoints. The open
evaluation theorem already checked in C.30 applies to this exact action.
The needed compact lifting assertion is proved directly: nested source
balls of shrinking diameters, together with compact target shrinkings,
give a finitely branching compact tree of choices. Completeness gives
the branch limit in the actual source, continuity gives its prescribed
target, and the resulting compact family covers the chosen compact
target set. No continuous local section of endpoint evaluation is assumed.

A countable exhaustion and path neighborhoods converging uniformly to
identity give one compact path-connected family K of actual labelled
global maps. At every selected orbit point x, K K^{-1}(x) contains a
neighborhood of x in the same original orbit. On open orbits whose full
local centralizer has dimension zero, the effective stabilizer is a
discrete free proper group. We choose locally finite, pairwise disjoint
operator orbits of small disks, with representatives from distinct
operator orbits. The operator restriction kernel acts identically on
the whole orbit, so conjugating a disk map to every translate is
independent of the chosen representative.

The proof supplies the actual topological group embedding from the
product of the boundary-fixed disk homeomorphism groups into the global
operator centralizer. All values of its maps and inverses satisfy the
same compact four-letter evaluation bound (K K^{-1})^2(x), uniformly over
the entire product. At a G-fixed frontier point that family fixes the
point, proving joint continuity through every accumulation. Restriction
is the continuous inverse on the image. The displayed Alexander formula
and its exact inverse contract the resulting global subgroup. An
arbitrary original loop has not been factored into this subgroup, and
simultaneous edge/configuration extension is still an obligation.

### C.65: exact nonmetabelian frontier comparison and small planar fillings

For a one-dimensional principal open orbit we keep both the actual
principal-base action beta and the actual intrinsic action on a nonopen
frontier orbit B. Endpoints of finite original-word paths which fix the
whole principal base at every time form a normal subgroup. Their
frontier image is path connected and abelian. A nontrivial such image
would be free and transitive on B. Closing it in the intrinsic topology
and applying the already proved orbit comparison identifies it with
the actual translation or rotation group. The full frontier image
would normalize that group and hence be metabelian. Consequently the
endpoint subgroup is trivial on every nonmetabelian B. Two specified
finite-word paths with the same whole principal-base path have exactly
the same frontier restriction at every time.

For the full kernel of beta, commutator paths with an arbitrary original
finite-word path lie in the preceding endpoint subgroup. The full
kernel's frontier image therefore centralizes the full frontier action.
C.38 identifies the latter's centralizer as closed discrete cyclic in
the actual intrinsic topology. The graph image E_B in the product of
the principal and frontier homeomorphism groups has the exact central
kernel Delta_B={1} times this cyclic group. Its quotient map is an actual
covering: an identity neighborhood U with U^{-1}U intersect Delta_B={1}
has precisely the disjoint sheets U delta. Finite-word paths make E_B
path connected, so the whole deck group is Delta_B. The induced map
E_B/Delta_B to beta(G), with the actual induced image topology, is a
continuous bijective homomorphism. Its inverse continuity remains
unproved. Membership of a proposed deformed base map in beta(G) is
also required before this covering can lift that map.

Separately, the proof establishes injectivity of pi_1(U) to pi_1(V)
for a component U of the intersection of any open planar V with an
open Euclidean disk. A polygonal regular neighborhood is enlarged by
filling precisely the holes lying in V. One excluded point in each
remaining hole yields a punctured plane which retracts explicitly
onto the enlarged neighborhood by radial Schoenflies homotopies.
The original null-homotopy, composed with this retraction, gives a
based filling inside U. Original ambient-null evaluation loops
shrinking to a fixed frontier point therefore have fillings inside
their original orbits with vanishing diameter. The construction chooses
each filling individually; no continuous choice or equivariant
fragmentation has yet been proved.

### D.66: the exact scalar-cover norm computation

For every remaining scalar coordinate of an actual cubic or quartic
torus action, the proof constructs the exact invariant cyclic-q cover
of type (1,q), the quotient extension C_q semidirect C_d, the actual
order-d section inside the retained extension, and all cusp labels.
Deck averaging splits primary homology into the actual filled handle
module and the boundary module. The scalar action permutes the deck
maps, so the averaging idempotent is equivariant; it is not necessary
that the action commute with each deck map. Eliminating the actual
total boundary relation identifies the boundary summand with
(q-1)/d copies of the regular Z_p[C_d] module, with both inverse maps
written in the proof.

The negative sum of one representative in each nonzero boundary orbit
has cyclic norm equal to the distinguished boundary class, integrally
at every primary precision. The handle has zero invariants and zero
norm, with determinant(T-1)=p. The full primary homology module M
therefore has H^2(C_d,M)=0 and H^1(C_d,M)=C_p. The retained cusp exponent
and this explicit norm preimage give both inverse maps splitting the
actual primary abelianized extension. This proves precisely why that
invariant-character norm obstruction does not remove the remaining
scalar cases. It does not construct a full scalar action or lift
every abelianized section to the original nonabelian extension.

The exact producer torus_scalar_cover_norm_d66.py was read and rerun
independently. The prime test uses integer square roots. It passed
44 scalar cases, 2,084 section labels, 2,040 inverse-basis checks,
2,040 deck-conjugacy checks, 2,040 deck-average checks, 44 norm-preimage
checks, 550 factor-set checks, 2,090 primary-unit checks, both handle
types, and 820,992 coordinate checks. The proof supplies the infinite
and all-precision conclusions separately from these finite checks.

### D.67: the complete standard normalizers and specified finite overgroups

The actual quarter-turn R:X maps to Y, Y maps to X^{-1}, together
with B:X maps to X, Y maps to Y^{-1}, realizes a geometric D8. The
proof gives every inner adjustment relating these representatives
to the cusp-normalized standard negative involutions. The full
normalizers of both standard Klein-four centralizers are this same
D8. Conjugation fixes the unique nonidentity multiplier-one element
of each Klein group, bounding the quotient of its normalizer by its
centralizer by two; the quarter-turn realizes the nontrivial exchange.
The first Klein group is exactly the mod-two kernel on D8, which
also proves that D8 is self-normalizing. Its full centralizer is its
order-two center.

For the specified standard two-section negative involution b0, every
finite overgroup is exactly its C2, the computed Klein group, or this
D8. The full nine-type list of D.55 and the proved multiplier signs
leave only the possible S3 and D12 exclusions to check. In either,
the negative involution inverts a cubic element. The matrix of b0
modulo two is identity, while every cubic element has exact order
three there, giving the contradiction through the actual homology
map. Thus D8 is the unique maximal finite overgroup of this b0;
the exact conjugation maps transport the list throughout its already
known conjugacy orbit. Recognition of arbitrary negative involutions
has not been proved. The discrete torus identification is cited at
its correct location, A.13.

The exact producer standard_negative_overgroups_d67.py was read and
independently rerun. It passed 156 word-generator equalities, 64
word products, 64 homology products, 12 mod-two conjugation pairs,
and six cubic inversion pairs. Both the producer and the root and
independent outputs are included.

### F.12: the exact common-reflection equalizer

Six specified winding characters of the F.11 seven-point map pull
back to the six source puncture characters. They give an integral
left inverse on abelianizations and the same left inverse after
full completion. The residual A5 centralizer therefore lies in
the source commutator subgroup and in the actual double cover
t=s^2, whose source is Y=P1 minus {0,infinity,+/-mu5}.

The common involution has quotient Q_s(z)=((z-s)/(z+s))^2. Its two
branch values are 0 and infinity, the pole pair has value 1, and
the five other pair values are ((zeta^j-s)/(zeta^j+s))^2. These
give the actual map phi:Y to M_0,8. On full completed fundamental
groups this map is injective: it is the restriction of the actual
common-involution descent map, whose only finite deck kernel is
the named involution, and that involution has nontrivial original
puncture permutation, so meets the pure subgroup trivially.

The second involution beta=(13)(45) commutes with the common one
and, together with D10, generates A5. Its exact quotient permutation
and actual Mobius map produce the based involution
R(v)=(v2/v3,v2,v2/v1,v2/v5,v2/v4). The residual A5 centralizer is
exactly the image of the equalizer of phi-hat and R_* phi-hat in
the full rank-eleven free profinite source. Both implications use
the retained injective descent map; no unidentified base path
occurs in R.

On the anti-invariant source homology module, the twenty target
winding equations reduce exactly to a0-a1+a2=0 and
-a1+a3+a4=0, with the displayed integral rank-three kernel basis.
Equality of that linear kernel with the image of the full group
equalizer is not asserted. The lifted F.11 common-kernel word has
homology e_{1,-}-e_{1,+} and first winding defect 4. Its full
profinite power has defect 4u; multiplication by 4 is injective
on Zhat, excluding every nonzero power from the actual equalizer.
The exact equalizer's triviality remains the unresolved F.7 step.

The complete producer c5_common_reflection_f12.py was read and
rerun independently. It checks the original labels and matrices,
six splitting characters, the twenty-by-twelve divisor matrix,
the involution's action on all twenty winding characters, the
anti-invariant restriction equations and their integral basis.
The unrestricted source divisor matrix has rank ten, the
difference matrix rank six and Smith factors 1,1,1,1,2,10; the
specified word has defect 4. These are the actual exact finite
calculations used in the proof.
