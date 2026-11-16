# Independent audit: A152, A153, A154 bound, A155, A156

Date: 2026-11-16. Auditor: local_preprint. Parent owns integrations.

## A152: local Prym Kummer injection

Source: `sections/harmonic_prym_dyadic_injection.tex`. Full proof and
`code/harmonic_prym_dyadic_injection_certificate.py` independently checked.
The literal duplication formula gives the stated negative-valuation
recursion, and the exceptional valuation-one branch has the two exact
unit-square alternatives used in the source. Every nonzero image under
`[2^n]` has x-valuation at most `2-4n`; the n=1 computation also excludes
the nonzero two-torsion point from the image. Thus the intersection of
all images is zero, proving the asserted Kummer injection. Odd torsion
would belong to every image; higher two-power torsion would make the
nonzero two-torsion point a double. This proves the final strengthened
local torsion statement. The proper quotient fibres over the two
torsion points are exactly the four stated boundary points. The
section consequence retains the hypothesis of ordinary localization
at two and does not infer any conclusion from a single local cusp.

## A153: persistence after enlarging a finite support set

Source: `sections/two_prime_finite_support_persistence_agent.tex`.
The relative cyclotomic residue-degree calculation embeds the unique
unramified cubic extension at every newly controlled prime after the
stated depth. Existing support primes were already split in the
fixed cubic extension. Thus the same nontrivial Artin quotient remains
split on the enlarged support, with the literal ideal-norm transitions.
The retained certificate was independently rerun: 1,955 exact residue
orders at 302 primes, all passed. No target norm obstruction is inferred
from this nontrivial class quotient.

## A154: independent full two-Selmer upper bound

Complete proof is in `sections/harmonic_prym_second_descent_bound.tex`,
with exact arithmetic in
`code/harmonic_prym_isogeny_pairing_certificate.py` and retained output/data.
The six displayed conic points are directly substituted. The tangent
divisor class is the actual rational kernel point on the Jacobian of
the psi-cover, as proved by the two involutions and their deck
translation. The local quaternion evaluations yield a rank-four
pairing matrix on the six-dimensional isogeny Selmer group. The exact
finite coefficient sequence has a two-element kernel after the
rational boundary class is removed. Isogeny adjointness puts its image
in the two-dimensional radical, so the full two-Selmer order is at
most eight. This proof uses no Selmer-order or class-group-completeness
output from Magma. Legendre, birational, and root independently
audited the exact maps and rank bound.

The final A154 main source `sections/harmonic_prym_rank_zero.tex` and
its literal Fisher input were subsequently read in full. All three
Fisher maps/local/ELS certificates were independently rerun and passed.
The covariant map has four unramified poles above the origin and
degree four. Its branch-origin kernel is the full geometric
two-torsion; the unique factorization of the induced Jacobian map
through multiplication by two descends over K because the Hom group
has no torsion. The displayed torsion translation is exact.
The independent nonzero pairing and upper bound give rank zero and a
nondegenerate two-dimensional Sha[2]. Bilinearity excludes an element
of order four, hence all higher two-primary torsion and the inverse
Tate module. The finite zero-cochain compactness argument gives the
actual injectivity needed for continuous Kummer classes. The dyadic
ordinary-point exclusion follows from the literal proper fibres;
the source correctly retains ordinary odd-place points in small
formal neighborhoods with trivial two-primary Kummer class.

Cassels's original adjointness source is retained in
`sources/cassels1965_isogenies.pdf` (printed180--199) and the smaller
`sources/cassels1965_isogeny_adjointness_extract.pdf`
(printed181,182,183,187,188). Printed187 was visually checked: equation
(2.2) is the required adjointness; (2.5)--(2.9) prove it with actual
torsor maps, pulled-back functions, and compatible local points.
The extraction is reproducible by `code/extract_cassels1965_source.py`.

## A155: exact balanced ideal-class criterion

Source: `sections/balanced_class_norm_criterion_agent.tex`, final version
retaining all coefficient precisions. Full audit passed.

The normalized unramified character is canonical. Every base cyclic
three-character at 2,11,59 is unramified. The global three-character
group ramified only at three maps isomorphically onto the three-adic
inertia character group. Restriction to the pure local field at three
is injective, and its cyclotomic compositum is totally ramified.
Subtracting the unique global inertia character therefore produces
one unramified ideal-class character, independent of the chosen lift.
The residue-degree-one branch makes the remaining local character
conditions exactly `[P]-f_P[P_0]`, with no extra condition at three.

The positive sign is literal: `d(-h cup B)=h cup dB`, and the chosen
local primitives give
`w cup dB+h cup B=chi cup b+d(w cup B)`.
The local-minus-global Poitou--Tate convention therefore gives
`+sum inv(chi cup kappa(-2))=+h(e_n)/3^r` for arithmetic Frobenius.
Finite duality, the finite coefficient Mittag--Leffler argument,
integral Kummer, and the actual Shapiro augmentation identify vanishing
with the completed S-unit norm fibre. The ideal-norm relations are
literal; compactness of the closed fibres gives a compatible family
from nonemptiness at every height without transition-surjectivity.
The order bound on e_n is correctly separated from precision of
character detection inside the ambient group.

Independent rerun passed: 3,321 local labels, 57 prime-norm relations,
66,420 coefficient adjoint identities, 363 character tests, both
cochain sign identities, and the C9/e=3 precision regression.

## A156: literal integral norm-two generator

Source: `sections/two_inert_norm2_generator_agent.tex`. Full proof passed.
The new independent program
`code/two_inert_norm2_independent_audit.py` starts with the literal TeX
tables, reconstructs all 36 base-10^40 blocks and nine signs, and
computes the characteristic polynomial by integer Newton identities
and the determinant by fraction-free Bareiss elimination. It verifies
all ten divisibilities, exact annihilation, and the three-coordinate
relative norm `alpha-1`. This agrees coefficient by coefficient with
the author's separately retained data.

The root equations give the actual cubic extension and tower
embeddings. Eisenstein at three proves the field degrees. The odd
polynomial discriminant and its mod-two factor degrees 1,2,6 prove
that there is precisely one prime of norm two. The monic integral
annihilator proves integrality independently of a maximal-order
calculation, and norm two then identifies the principal ideal with
that prime. Negation gives the stated compatible beta_2 and beta_1.
Thus e_2=0 follows in the exact balanced quotient. No extension to
higher levels or class-group-completeness assertion is used.
