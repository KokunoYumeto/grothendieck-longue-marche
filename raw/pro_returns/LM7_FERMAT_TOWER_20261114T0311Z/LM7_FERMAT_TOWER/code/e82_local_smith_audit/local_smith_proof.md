# Exact local Smith replacement for E.82

The tested input is the actual A0 congruence lattice and gauge-relation matrix exported by root as `research_e82/code/e_cusp_family_A0_kernel_input.json`. No root-owned program or result was changed.

## Algorithm and proof

All arithmetic is exact in the localization `Z_(3)`, represented by rational numbers with denominators prime to three. At stage `k`, choose a nonzero entry of minimum three-adic valuation in the remaining block and swap its row and column into position `(k,k)`. Its value is `3^v*u` with `u` a unit. Multiply row `k` by `u^-1`, so the pivot is exactly `3^v`.

Every other entry of that block is divisible by `3^v` in `Z_(3)`. Thus clearing the pivot column by row additions and then the pivot row by column additions uses coefficients in `Z_(3)`. Each operation is invertible over this ring. All earlier diagonal blocks are preserved: the pivot row and column have zero entries in earlier positions. The remaining block entries still have valuation at least `v`, since each is a difference of multiples of `3^v`. Consequently the successive pivot valuations are nondecreasing. When the remaining block is zero, the matrix is diagonal with entries `3^v` followed by zeros, and these entries divide their successors. This is the Smith form over `Z_(3)`.

The implementation tracks actual matrices `L,R` with `L*A*R=D`. A left row operation acts inversely on the columns of `L^-1`; a right column operation acts inversely on the rows of `R^-1`. Both inverse matrices are stored, not reconstructed by a precision approximation. The program independently multiplies the resulting matrices to check `L*A*R=D`, `L*L^-1=L^-1*L=I`, and both orders for `R`. It checks every denominator in all four transformation matrices is prime to three. The same maps therefore lie in the indicated general linear groups over `Z3` and supply the actual completed coordinate inverses.

## Actual A0 results

The exact 45 by 45 lattice `K` has diagonal valuations

`0^31, 1^11, 2^3`.

Its cokernel is therefore `C3^11 x C9^3`. The explicit inverse `K^-1=R*D^-1*L` was verified in both orders and satisfies `27*K^-1` integral, as required by the retained congruence bound. The matrix `K^-1*G`, for the actual gauge relations `G`, is integral entry by entry.

The exact Smith valuations of `K^-1*G` are

`0^14, 1^3, 2^4`, with 24 zero rows.

Thus the corresponding liftable family is `Z3^24 x C3^3 x C9^4`. Its own complete transformation and inverse matrices are also checked and saved. The two exact transformations took less than half a second in the observed runs, including all full inverse-pair products. Runtime is printed in stdout but omitted from the deterministic JSON certificate.

## Files

- `local_smith.py`: reusable `local_smith(A)` and the actual input runner.
- `local_smith.out`: observed successful execution.
- `local_smith.json`: exact rational transformations, inverse maps, full operation traces and the input hash.

Every matrix entry is saved as its exact rational value. No finite-precision lift or unproved integer-to-adic inference is used.
