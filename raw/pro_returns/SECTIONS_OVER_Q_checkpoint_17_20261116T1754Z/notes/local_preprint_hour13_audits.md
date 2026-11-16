# Independent arithmetic and section audits, checkpoint 13

All paths below are relative to `work/`. The main manuscript integrations and
checkpoint archive are owned by the root agent. No parent files were edited.

## A171–A172: full metabelian fibres

The complete saved A171 source, including the rational tripod-frame append,
passed an independent mathematical audit. The author added the requested
explicit lift of the abelian conjugator before the common finite section.
The exact generalized-Jacobian twists, finite maps, Stoll boundary argument,
and compact conjugator sets were checked.

`sections/tripod_cuspidal_metabelian_fibres.tex` (A172) passed in full,
including the order-27/class-two quotient, both degree-three isogenies,
the actual cyclotomic preimage and character `(chi9^2-1)/3`, and the
all-finite-local-field pro-three separator. The Heisenberg multiplication,
central difference classes, restriction equation forcing `z=k/24`,
inertia-coboundary normalization, and number-field transfer all check.
The full certificate `code/tripod_cuspidal_metabelian_certificate.py`
was independently rerun after the final append.

## A173–A176: the two finite class groups and exact support repair

`sections/two_inert_level2_class_group.tex` (A173) passed its full saved-source
audit. The local cube checks for `11(1+6 alpha)` and `649`, the persistent
anti-class pairing, complete unit norm index, cohomological ambiguous-class
formula, and nilpotent-operator recovery of the entire class group were
checked. The complete descending-radical source argument retains the
outside-S divisor map and local-three Kummer plane.

`sections/two_inert_order_nine_balance_reduction.tex` (A174) passed in full.
Its certificate independently passed 6,561 homogeneous norm/residue cases
and 13,924 finite-Nakayama regressions. The order-nine character factors
through actual principal relations, with the stated fractional ideal maps.

The A175 source is `sections/two_inert_level3_norm_indices.tex`, with literal
anti-unit supplement `sections/two_inert_level2_anti_coefficients.tex`.
The three new roots satisfy exact cubic and involution identities in the
degree-eighteen field. Their five residue rows prove complete anti-unit
generation modulo cubes. The full unit norm matrix has rank five; the
fourteen-column S-unit matrix has rank ten. All discarded local components
have strictly positive valuation. The proof derives the S-ambiguous formula
from its actual divisor and unit exact sequences, proving the ordinary
ambiguous order 81 and the vanishing of the three-primary S-class group.
Both other agents and root gave complete proof clearance.

Executed certificates and data:

- `code/two_inert_level2_anti_cube_root_certificate.py`
- `code/two_inert_level2_unit_norm_certificate.py`
- `code/write_two_inert_level2_anti_coefficients.py` — all 54 coefficients,
  468 two-block rows, reconstructed exactly.

`sections/two_inert_level3_support_repair.tex` (A176) passed in full.
Its support repair is an actual cyclic ideal-Hilbert-90 correction, followed
by the exact quadratic transfer `b3=gamma^2/b2`. The resulting divisor gives
`P=-3 R59`; all S-prime classes are then fixed by the cyclic group.
The group-order, norm-surjectivity and order-nine arguments give the stated
full degree-54 class group and the cyclic pure degree-27 class group.
Its independently rerun certificate passed 1,681 orbit-divisor identities,
134 support-correction exponent checks and 1,206 three-primary divisor
equations.

## A177–A179: all-height closure

The A177 source is `sections/two_inert_all_height_split_classes.tex`.
It proves ordinary three-class generation by the six changed primes and
S-class vanishing at every finite height. The fixed ten-element tame
character matrix has rank six at every height by the actual norm projection
formula. A prime-to-three principal power supplies each independent
two-place valuation direction. Cyclic Hasse norm and the proved upper
S-class vanishing supply an auxiliary norm with split-orbit coefficients
whose sum is a three-adic unit. The resulting polynomial in the cyclic
operator is invertible modulo three and kills the entire remaining class
quotient. The auxiliary norm target is not asserted to preserve a separately
prescribed earlier norm representative.

`code/two_inert_all_height_split_certificate.py` passed the exact fixed
character matrix, thirteen residue-degree and norm-index cases, and 367,920
literal polynomial invertibility cases. The final source also includes the
binomial proof of `ord_(3^j)(2)=2*3^(j-1)`. Root, Birational and Legendre
passed the complete saved proof; both peers independently reran its certificate.

`sections/two_inert_all_height_balanced_vanishing.tex` (A179) passed its full
independent audit. The central order-nine class extension is split by its
actual inertia at three; its tau-stable complementary line gives the exact
anti-Kummer radical. The persistent two-character matrix forces all changed
prime valuations divisible by three. The local-three Kummer plane eliminates
the ramified radical component. Consequently every plus cubic class
character descends through the actual norm map, preserving three-rank one.
The nonzero genus value makes `R59` a generator of the cyclic pure class
group, and that literal balanced relation kills the whole balanced quotient.

The completed norm-family conclusion uses compact finitely generated
S-unit completions and the exact A155 criterion. The passage to an actual
finite chain uses the finite quotient `U0/N Un`, killed by `3^n`; it makes
no compactness assertion about the discrete actual unit groups.
The independent certificate rerun passed the central/inertia and Kummer
maps, 2,186 cyclic-generator tests, 66 finite-group rank tests and 1,295
finite-primary cokernel tests.

All source delimiter and literal spacing-command checks passed before the
final root integration. No higher assertion about a prescribed actual
infinite norm chain, an ordinary completed pair, or a full metabelian
section follows merely from these one-variable norm calculations.
