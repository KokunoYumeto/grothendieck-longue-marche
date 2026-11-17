# Root audit of the ordinary centralizer image

Review and fresh replay completed at approximately 06:41 UTC on 17 November 2026, after the integrated checkpoint07 proof freeze. The result remains outside that checkpoint's paper and ledger; it is queued as A.4.38 for the next manuscript revision.

## Proof read in full

The root read `work/main_sphere10_ordinary_centralizer_image.tex` and all three underlying programs in full. The quotient map is the same actual map from the ten-point sphere group used in A.4.32; the geometric Klein four is the marked source subgroup of A.4.36.

The two quartet paths descend under `u=(z^2+1)^2/(4z^2)` to nested based Jordan loops. The first has the exact ellipse parametrization with semiaxes 17/16 and 15/16. The second is injective away from its reciprocal endpoints because the other three points in each quotient fibre lie outside the open first quadrant. Its winding around 1 is one and around 0 is zero. The full preimage of the ellipse is the pair of circles of radii 2 and 1/2; the second path stays strictly between them and has the interior test value 16/25. The resulting nested loops are a free basis. The lifted isotopies fix the six ramification labels and commute with the deck group. This proves the direct-product source splitting and generation used by the computation.

The full finite centralizer is computed through the actual 174 state orbits. An allowed value at an orbit representative is transported by conjugation, and the stabilizer equation is precisely the independence of that choice. The verified orbit table gives 168 Heisenberg factors and six central cyclic factors. The mod-four invariant equations have 23 unit pivots and one two-pivot; all 32 colored permutations are tested, with exactly 16 explicit lifts. The centralizer projection through the relative ternary kernel is onto by two explicit coprime averaging steps, first in the quotient by its center and then in its center.

For the ordinary image, all 4096 two-motion states and 8192 Schreier edges are retained. In the right-action wreath convention, multiplication by the inverse target representative evaluates its inverse weight at the original coordinate, which agrees with the implemented Schreier formula. The change from Heisenberg central coordinate k to k+2ij gives the exact alternating half-commutator product in characteristic three. Thus the span of the Schreier vectors and their brackets computes the whole generated kernel. The 198 noncentral directions and 104 final central directions give exponent 302; the initial central rank is 98 and six retained brackets supply the extra directions. The source-label permutations prove that the two-motion image intersects the geometric deck group trivially.

## Fresh root replay

The driver `code/run_ordinary_centralizer_reproduction.py` copied the three programs and the already independently reproduced input certificates to `notes/reproduced/ordinary_centralizer/`. It ran the path and fixed-kernel checks independently in parallel, then the dependent image census. Every exit code was zero.

| Program | SHA256 | Runtime seconds |
|---|---|---:|
| check_sphere10_centralizer_motion.py | fa06779ffc807e87e04a85c807eb1caf6e31f8d9f7fc3dc96af669311d93aaf8 | 1.033 |
| check_sphere10_geometric_fixed_kernel.py | 02c62dd1944ee5ea3172e78317c9ff2cd662af5b592da536a002c56c0bcb6e5a | 0.576 |
| check_sphere10_ordinary_centralizer_image.py | cc5a4239374d075ca83e449f4464dd50a3d42e24f13b883240fa80c777ac92a0 | 9.846 |

The exact source paths have 22 and 12 crossings, yielding marked words of lengths 74 and 64. Their four commutators with the two geometric Klein-four generators vanish in every one of the 630 coordinates. The verified finite centralizer has order `2^27 * 3^510`; the verified actual ordinary image has order `2^14 * 3^302`, with index `2^13 * 3^208`. All actual outputs, source words, matrix archives and hashes are retained beside the fresh-copy programs.

The index is a statement about this specified output quotient. The finite centralizer-recognition refinement from A.4.34 has a stronger input and projects its centralizer to the ordinary image. These two statements use the displayed projection and are compatible.
