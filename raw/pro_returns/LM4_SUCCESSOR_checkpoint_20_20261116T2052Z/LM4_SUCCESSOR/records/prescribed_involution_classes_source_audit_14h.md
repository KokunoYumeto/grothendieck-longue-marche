INCOMPLETE

# Prescribed involution classes: exact primary-source audit

This reading follows the checkpoint14 formal-paper freeze. The resulting
proof is retained as reviewed research and has not been inserted into
the frozen247-statement paper.

## Sources opened at the application step

Haran, D. (1990). Closed subgroups of G(Q) with involutions.
*Journal of Algebra,129*,393–411.
https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf

Verified: we opened Definition1.1(4), printed394, Remark1.2(b),
printed395, and Proposition2.3 with its proof, printed397–398.
The allowed set consists of whole conjugacy classes of involutions
in the finite lifting group. A solution lifts the specified quotient
map and sends all source involutions into that set. The implication
from real projectivity invokes an auxiliary finite cover in the
following earlier paper. We checked that invocation rather than
replacing the allowed-class problem by ordinary weak solvability.
Retrieval:turn757view0; the bibliography continuation is turn758view0.

Haran, D., & Jarden, M. (1985). The absolute Galois group of a pseudo
real closed field. *Annali della Scuola Normale Superiore di Pisa,
Classe di Scienze, Serie4,12*(3),449–489.
https://www.numdam.org/item/ASNSP_1985_4_12_3_449_0.pdf

Verified: the archive metadata and Corollary6.2 with its proof,
printed466–467, were opened. This constructs a finite cover whose
nontrivial involution images are precisely the prescribed union
of classes. Several formulas are absent in the text extraction;
we independently reconstruct the compact-set argument as follows.
Map a free profinite product of the chosen C2 factors and enough
free generators onto the finite target. The free-product torsion
theorem puts every involution above an allowed element. The closed
preimage S of the forbidden nonidentity target elements is compact
and contains no element whose square is one. Its square-image is
therefore compact and avoids one. An open normal subgroup inside
the map's kernel can avoid that image. The resulting finite
quotient has no involution above a forbidden element and retains
every allowed class. This is the exact auxiliary-cover conclusion
required in Haran's later proof. Retrieval:turn759search6,
turn760view0/1. No assertion depends on a stronger real-free
recognition theorem for the actual group E.

## Actual-group application checked independently

For each finite E-module A we refine its action head so that the
three actual involution classes remain distinct and the finite
centralizers project into the corresponding actual order-two
centralizers on A. Compactness proves the existence of this head;
it is not an assertion about every finite centralizer. The allowed
classes of three arbitrary local cocycles in A semidirect Q then
give one global cocycle. The refined centralizer condition ensures
that finite conjugacy changes only a local coboundary. Thus H1
restriction is onto for every finite coefficient module.

The full note also proves H2 restriction injective, actual compact
module projectivity at every prime, and the split induction counit
sequence. At two, the orientation twist vanishes modulo two;
finite Krull–Schmidt cancellation, compatible finite bases, and
compact Nakayama prove R2 is free of rank two over Z2[[E]].
Root and CE read the complete argument and passed it, with the
inverse-limit basis wording corrected to retain induced compatible
bases rather than arbitrary prescribed bases at several levels.

Proof:work_A/actual_dyadic_augmentation_projectivity_14h.md.
Independent review:work_CE/review_actual_dyadic_augmentation_14h.txt.
The actual odd orientation-twist ambiguity, finite quotient graph,
and peripheral generation remain unresolved. No full conjugacy
decision is inferred from this module theorem.
