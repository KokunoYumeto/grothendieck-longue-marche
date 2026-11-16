# Independent full-source review of B.97 and B.98

Status: PASS, 2026-11-16. This is an internal proof review, not another
formal statement or a claim about the full old-source orbit sum.

## B.97

Read `sections/b_cross_sheet_block.tex` completely. Re-extracted the actual
old q=1 operator from `work_A/old_base_augmented_row_action.json`:
its retained action fixes y1,y2,y3 and takes y4,y5 to their conjugates by
y1 inverse. The eight A heads have y1 exponent parity0; all eight B heads
have parity1. The displayed row formula follows with the stated beta
identification, and the inverse heads give the same parity change.

The128 selected augmentation rows are therefore distinct. The ordered
left-coefficient argument over the separated two-sided E-augmentation
filtration proves independence; it does not invert the minor. Both
summands are the actual F-stable modules already identified in B94/B96.
Their cohomology and source image follow by direct sum.

The returned b-squared source operator differs from alpha_b squared by
an inner G-unit. This identifies its image of the negative odd block
with the positive odd block as actual Omega-submodules, and the two-coset
description gives the full returned-source orbit formula. The distinction
between the sum of individual cohomology images and the cohomology of the
sum is maintained. No homogeneous full-chain parity grading is asserted.

## B.98

Read `sections/b_coefficient_domain_counterexample.tex`, its complete
document producer `code/write_B98_counterexample19.py`, stdout, and
`records/B98_displayed_counterexample19.json` completely.

The shift semidirect product R semidirect T is explicitly free of rank13;
the inverse on all x_(g,i) follows by conjugating the eight original
generators. The beta-twisted embedding into two copies of that free group
is injective and respects the actual multiplication. The finite-rank
integral Magnus map is faithful by the maximal-block monomial argument;
degree/lex first coefficients give an invariant order. Unique maximal
support products then prove the integral group ring is a domain on both
sides.

The complete displayed conjugators, of lengths83 and85, reproduce the
actual592-letter transformed commutator. The printed factorized semantic
G element agrees with the previously collected coefficient-1 in row
(2,2,1). The original column occupies only row(5,5,1). This refutes the
unit-multiple implication in the actual marking. The producer correctly
does not describe itself as a fresh Fox-chain solver: the independent
complete chain checks were already retained.

The private-row argument over the domain proves independence of each
specified two-column pair for all integral group-ring coefficients.
Even-source normalization gives the same fixed/other-cone coefficient
type in each pair, so the cohomology assertions follow. These16 pairs do
not determine any64-column-block intersection or whole orbit overlap.

No mathematical correction requested in either source.
