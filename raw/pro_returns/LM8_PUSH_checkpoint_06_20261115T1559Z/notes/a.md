# Part A: evidence and continuing attacks

## Main fixed-element result

A.1 is proved by reducing to the local closed commutator subgroup, not by
reassembling maximal pro-prime quotients. The key primary source is
Mochizuki--Tsujimura, *Resolution of Nonsingularities, Point-theoreticity,
and Metric-admissibility for p-adic Hyperbolic Curves*, 30 March 2024,
Theorem A, Definition 2.2(i), Proposition 2.3(v),(ix), Proposition 2.4(vii).
The statement on printed pp.51--52 and proof p.54 were opened and read.
The uniqueness clause does not have the extra open cyclotomic-image
hypothesis of its existence clause. The proof of A.1 supplies existence
using the specified point or cusp. A second agent independently checked
the primary theorem's hypotheses before the statement was marked Proved.

For a local field of residue cardinality q, the closed commutator subgroup
maps onto a subgroup containing (q-1)Z_r in tame inertia for every r
different from the residue characteristic. It is contained in the local
intersection with the global abelian-field kernel. Thus the passage from
the local cyclotomic kernel to this smaller kernel loses none of the
uniqueness hypothesis needed here. It does lose open cyclotomic image,
which prevents use of the existence clause for an arbitrary section.

A.6 computes actual cocycles and the four geometric conjugacy classes of
sections agreeing on Delta. A.9 also decides the existence of a fixed lift
of any pro-prime fixed element of an open covering group: it must be in
the image of the actual specified inertia. This does not claim that fixed
points commute with taking quotients.

## Primary-source checks

Nakamura 1994: Theorem 2.1.1 and Lemma 2.1.2 were opened in the publisher
PDF. The former's normalizer condition is an actual cyclotomic action on
the generated subgroup. The latter explicitly allows every nonidentity
element of a free factor, including an exponent supported at one prime.
This confirms the source step of LM8 G.19/R3, conditional on its already
separate pro-prime input. Nakamura 1995: Claim 4.14.1, equation 4.14.2 and
Corollary 4.15 were opened. Tsunogai 1995 was opened at the publisher.
These pro-prime results are not needed for A.1's proof.

## Normalized-procyclic question: current attack

The full normalizer question is separate from A.1: the normalizer need
not contain an arithmetic section. The configuration in LM6 A.62 has
geometric kernel P times C, with P pro-l and C pro-prime-to-l. A pro-l
Sylow subgroup over a pro-l local Galois subgroup gives a splitting
through C. At a place of residue characteristic p different from l,
the local pro-l subgroup has tame Z_l and open l-cyclotomic image, so
the existence clause of MT Proposition 2.4(vii) produces a primitive
valuation. At a good place, the action on P is unramified; uniqueness
for tame inertia then puts P in its geometric stabilizer. The remaining
step is to control this stabilizer well enough to force horizontal cusp
inertia. A primitive valuation need not already be horizontal. This step
is not established, and is not inferred from A.1.

## Attribution correction for R30

The attached October 2026 p-adic section preprint's Section 8 was read in
full. It has no Corollary 7.10 or Porowski density argument. LM6 D.6
explicitly discusses an unnumbered corollary after Corollary 7.10 of a
different supplied 2026 source (identified nearby as Porowski). R30
misattributes that density issue to the attached local-section preprint.
No result A.1, A.6, A.8 or A.9 uses either preprint or the density step.
The underlying density intersection inference is considered separately;
failure of an inference is not a counterexample to the curve theorem.


## First-cover audit, 10:35 UTC

All three S3, all three D8, and unique Q8 covers are written in A_first_covers.tex. The independent symbolic/group/point-count program passed. An initial hand expectation for the minus D8 quartic at7 was12 points; execution gave4, now correctly recorded. Both traces are nonzero modulo7, so the ordinary-vs-supersingular exclusion is unchanged. F/G/H agent independently checked all maps, isogeny decompositions, exact cusp-divisor Smith presentations, and the absence of a genus-two quotient for the Fermat Q8 cover.

The TeX binary initially had no installed format or packages. A minimal local TeX Live runtime is being bootstrapped from checksum-verified public packages; scripts and package inventory are retained, third-party package archives are excluded from deliverables. LuaLaTeX now reads the manuscript; routine source syntax corrections are underway.


## Independent second-hour audits

A.22 was read in full and independently checked by the root agent: finite-index
IA fixed-group invariance uses torsion-free separated lower-central pieces;
the pro-l topology comparison is valid precisely for l-group Galois closure.
A.24 was read in full and independently checked: the two-cusp first Johnson
matrix is symplectically self-adjoint, its determinant pencil is the square
of a cubic Pfaffian, and the all-degree jet-index kernel proof gives the
actual fixed subgroup after subtracting an integral cusp power. The
one-cusp degree-two pencil has at most countably many exceptional twists.
The l=2 transfer uses an actual pro-2 open embedding; it is not asserted
for odd primes. These are generic results and do not decide a named
exceptional packet.

The root agent read the supplied local section preprint's entire Section7
and Section8, as well as the introduction and Theorem1.1. Its main local
theorem remains a professional-preprint input in A.17/A.23 and D.23/D.24,
not a theorem proved by the present return. A.1 remains independent of it.

## A.25 independent root audit

The full stable-reduction and monodromy argument was read independently. The relative fibre identity, exclusion of smooth reduction by the cyclic/S3 cubic Galois closure, exclusion of component degree (3,0) away from the node, and the rational conjugator normalization were checked separately. Betts–Dogra, Definition3.1.5 and Theorem3.1.6, were opened in the primary arXiv:1909.05734 source by the root. The proper Lie quotient obstruction is nonzero under a->x,c->-x,b->y,d->y. A.25 supersedes the earlier open odd-prime stable-D3 sentence; no claim about arbitrary finite covers follows.

## D.25–D.26 independent root audit

The finite-set primewise coherence proof and genus-zero S-unit reduction were independently read. Mochizuki Theorem19.1 was opened in the primary source. The common pro-p neighborhoods and cusp separation, the exact rational 2-isogeny descent, and all eight Q(i)-points were checked. The local valuations are compared as integers, not as interchangeable completed cusp tangents. The infinitely mixed genus-zero case remains explicitly open.

A.26 root audit: the local Frobenius–tame commutator lies in the required global derived subgroup, and its separating monodromy scalar(q−1)m is nonzero. The proper first-layer contradiction therefore applies to every packet, including all exceptional twists. The three reflection maps are jointly injective on proper rational homology, and the remaining boundary lattice is primitive. Higher fixed layers are still open.
