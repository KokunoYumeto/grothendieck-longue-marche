# Independent root review of the formation-closure extension

Date: 14 November 2026, approximately 14:11 UTC.

Reviewed the complete candidate
`audit/F_proformation_reconstruction_candidate.md`, the full geometric
monodromy argument in F.24, the arithmetic extensions F.34–F.36,
and the integrated F.43 proof. Verdict: the mathematical extension is
approved, subject to the independent review and the stated wording
repairs being incorporated. F.9 remains unresolved.

## The exact class of groups

The hypotheses are that C is an isomorphism-invariant proper subclass
of all finite groups, contains every finite cyclic group, and is closed
under subgroups, quotients and extensions. “Proper class” should be
replaced by this wording to avoid its unrelated set-theoretic meaning.
Finite-product closure follows from extension closure. Finite quotients
of closed subgroups of a pro-C group are quotients of subgroups of
finite C-quotients, so all the profinite closure statements used are
valid.

Properness plus subgroup closure excludes every sufficiently large
alternating group. Indeed an excluded finite group embeds regularly
in a symmetric group, then in an alternating group using two extra
letters and the parity correction. Padding by fixed letters embeds
it in every larger alternating group. This argument does not require
the classification of finite simple groups. The theorem consequently
has a uniform bound after which its alternating factors survive.

## Constants and divisibility

Regularity of K over its number-field constants identifies the normal
closure of an algebraic constant over those constants with its normal
closure after base change to K. A finite C-Galois extension of K
containing that constant contains the normal closure. Its constant
Galois group is a quotient of a C-group. Conversely a finite C-Galois
constant extension remains such after the regular base change. This
proves the asserted equality of constant fields in both directions.

For a sufficiently large symmetric Galois extension of the constant
number field, its intersection with the maximal C-extension is
exactly the alternating fixed field. The intersection is normal;
the quotient in C must kill the simple alternating subgroup, and
the sign quotient already lies in C. Its remaining degree is |A_n|.
Those degrees are unbounded, so a finitely generated L over K^C
misses a finite Galois number field. The argument supplies a missing
number field, not merely a missing extension of K.

Radical closedness uses a finite normal C-extension containing the
element, then the roots of unity, then roots of all its conjugates.
The latter extension is abelian after adjoining roots of unity;
extension closure keeps its normal Galois group in C. No assumption
that its group is solvable is needed.

The fixed-field proof of D(E*)=(K^C)* for finite E/K^C is independent
of solvability. It fixes one finitely generated F=MS containing the
element before the root level varies. The automorphisms commute on M
and K^C separately; the root ratio therefore lies in F for every
level. The ordinary finitely generated field has D(F*)=1 by divisors
and the number-field unit theorem. The normal proper model argument
extends this to finitely generated L and every finite extension of L.

## The changed finite-quotient argument

This is the substantive change from F.43. The quotient H/J belongs
to C because L/F is Galois pro-C. The simple literal A_n has trivial
image in that quotient: a nontrivial image would embed A_n in a
finite C-group, contradicting subgroup closure and its exclusion.
Thus A_n is contained in J. One must not assert H-infinity is
contained in J, and the candidate expressly does not do so.

The spanning-tree gauge in F.24 supplies literal S_n and base
elements of support at most two whose labels generate the full
geometric group N. For such a base element u and a coordinate i in
its support, an even permutation can place an unused coordinate at i.
The commutator [u,tau] lies in J by normality, lies in the base group,
and has coordinate u_i. Conjugation by literal S_n preserves J and
transports these labels to each chosen coordinate. Therefore the
projection of J intersect N^n onto each N is surjective. This is the
needed projection statement; it does not assert that N^n itself is
contained in J.

The constant-field intersection still makes J map onto P. An even
permutation moves any chosen block image back without altering this
constant image. Hence each coordinate stabilizer J_i maps onto the
entire arithmetic quotient G, not just N. Transitivity of A_n makes
the specialized fibre a single closed point. The allowed pencil
degrees remain unbounded beyond the exclusion bound. None of these
steps requires perfectness of P, J or G.

## The remaining reconstruction predicates

The Gauss-valuation proof fixes a normal finite extension M over a
rational function field over Q. A nontrivial automorphism on a missing
number field moves its constant primes. Its restriction preserves M;
the other automorphisms preserve K^C because they fix K and K^C/K
is normal. The same fixed field MS0 is finite over M, so the norm
valuation converts profinite unit exponents to integers. No group
solvability enters this calculation.

The generalized-Albanese argument requires normality of G_L in the
finitely generated descent field's Galois group, arithmetic detection,
and actual point values descending to a finitely generated field.
All three are established. The finite-span conjugation calculation
therefore precedes the application of Jannsen's integral Tate-Hom
theorem over a finitely generated field, as it must. The residue norm,
transverse-curve and integral divisor-matrix arguments are unchanged.

The scalar ambiguity is exactly the fixed field (K^C)*. The high-degree
point proof uses membership in that fixed subfield, not algebraicity
over Q or solvability. Missing constants provide the finite extension
needed in its constant-unit case. The resulting geometric-point
function is used through the precise CHW Theorem 4.18(5), retaining
the closed-point-preserving convention and full étale-chart comparison.

## Subfields, equivalent description and strictness

For an arbitrary subfield k0 of L, the finite transcendence basis and
relative algebraic-closure argument places k0 in C0^C for a finitely
generated C0. That extension is algebraic, so F.32 applies. Descent
along a possibly transcendental compositum is not used.

For the converse description of the sufficient class, let C'/F0 be
the finite normal closure of the auxiliary finite field C/F0. Write
the composita C' times each conjugate of C^C explicitly: each is
Galois pro-C over C'. Their compositum has a group embedded in the
finite product of their pro-C groups. This proves virtual pro-C for
the normal closure. It characterizes the sufficient embedding class,
not all fields with reconstruction.

For the strict example, composition factors of subgroups are controlled
by intersecting with an ambient composition series and refining the
resulting series. Thus the nonabelian-composition-factor order bound
does define a subgroup-, quotient- and extension-closed class.
The family x^5-x has four simple finite critical points and distinct
critical values. Its regular Galois group is S5. Full-group Hilbert
specialization after any prescribed finite constant extension supplies
jointly linearly disjoint S5-extensions. Their compositum gives the
product of S5 groups as a quotient. Every open subgroup maps to an
open subgroup of that product and still surjects to an S5 factor.
Consequently no open subgroup is prosolvable, even after replacing Q
by any number subfield. This excludes the field from F.43's class.

## Primary source independently reopened

Serre, J.-P. (2007). *Topics in Galois theory* (2nd ed.). A K Peters.
https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf

Root read Proposition 3.3.1 (printed p.23), Proposition 3.3.3 and
Corollary 3.3.4 (p.24), and Theorem 4.4.1 with its Morse hypotheses
(p.39). Web records: turn789view0; turn791view0, turn791view1,
turn791view2. The first permits non-geometrically irreducible Galois
covers; the disjointness statement adds absolute irreducibility,
which the regular S5 family satisfies. The theorem is used with
exactly those different hypotheses in the two places.

The remaining opened sources and their original scopes are recorded
in the root F.43 review and the existing source register. No
necessary-and-sufficient field classification or priority claim follows
from this sufficient-class extension.

## Cofinal alternating-subquotient formulation

The proposed additional formulation is also approved. For m at least
five, let C_m consist of the finite groups with no A_m subquotient.
Subgroups and quotients preserve this condition. To check extensions,
suppose N is normal in G and H/L is an A_m subquotient of G. The
image of H intersect N in the simple group H/L is normal and is
therefore either trivial or all of H/L. In the first case A_m is a
subquotient of G/N; in the second it is a subquotient of N. This
proves extension closure. Cyclic groups satisfy the condition, and
A_m itself does not, so C_m meets every theorem hypothesis.

Conversely, an excluded group G0 for any allowed proper class C
embeds in some A_m. If a C-group had an A_m subquotient, quotient
and subgroup closure would put both A_m and G0 in C, a contradiction.
Thus C is contained in C_m. The union of the theorem's sufficient
classes can consequently be described by an algebraic model over a
finitely generated field whose normal-closure Galois group has an
open subgroup with one A_m absent from all finite-quotient subquotients.
This is an arithmetic sufficient criterion and an equivalent
description of that union; no necessity for reconstruction is proved.

## Independent exact calculations

`code/F_proformation_group_checks.py` and its JSON output verify
19,200 semidirect-product commutators using the nonabelian label group
S3, across all 275 one- or two-coordinate base vectors on five blocks.
They check the coordinate equality by actual multiplication and
inversion, not by substituting the claimed formula. All 36 products
in the parity-correcting embedding S3 into A5 are checked. The
strictness family's discriminant is exactly 3125*t^4-256, with simple
critical points and the critical-value relation -4*x/5.

The same program checks the abstract example H=A5 times S6,
J=1 times A6. The quotient belongs to C_60, but the stable derived
group has order 21,600 and is not contained in J of order 360. This
confirms that retaining the earlier solvable-residual containment
would be wrong. It is an abstract group countermodel, not an asserted
geometric pencil realization. All checks passed.
