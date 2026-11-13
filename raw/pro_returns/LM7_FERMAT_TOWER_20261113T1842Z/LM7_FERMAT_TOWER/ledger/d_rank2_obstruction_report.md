# D45: exact exclusion of the recorded action, and an elliptic lift

The actual D39 action projects through `T3=B/D9(K)` to both rank-two quotients. The source map is literal: the four graph words and the integral determinant -27 are recorded. The full relative pro-two sphere and elliptic sources have exact common quotient C2, and the rank-four map has the closed normal mixed-commutator kernel proved in the section.

## Negative sphere branch

The recorded action on `B/D9(F)` cannot lift peripherally with multiplier one to `B/D10(F)`. All112 central correction columns have rank47; all38 complete lower s-centralizer columns leave that rank unchanged. The sum of degree-nine coefficients at words `000011011`, `000010111`, `001001111`, `000101111` vanishes on every correction and equals1 on the target. Every alternative conjugator is normalized into F using the exact S3 centralizers. All remaining lower centralizer cosets are computed; coprime order-three centralizers lift and add no missing obstruction columns.

The infinite retained Fhat abelianization forces the full multiplier to be exactly1. Therefore the entire recorded normalized D39 action, and each D40-D44 extension retaining it, has no genuine full profinite GT0 lift. This result does not exclude a replacement action with the same prescribed CM pair.

## Positive elliptic branch

The complete lower elliptic centralizer has rank50. Its defect columns enlarge correction rank38 to56. The exact corrected words have lengths3386495 and3109533 in B; all six cusp targets vanish through degree nine. Their generator substitutions retain the whole lower action moduloD9 and their Frattini action is identity, proving a genuine automorphism of the finite elliptic quotient. No full simultaneous D39 homology compatibility is inferred.

## Reproduction

Use Python3 and a C++17 compiler `g++`. Run in this order, with `--source-code /absolute/path/LM7_FERMAT_TOWER/code` on the first two scripts that accept that flag:

1. `d_cm_solvable_even_boundary.py --source-code ...`
2. `d_cm_rank2_boundary_test.py --source-code ...`
3. `d_cm_rank2_degree9.py`
4. `d_cm_rank2_centralizers.py`
5. `d_cm_rank2_boundary_test.py --source-code ... --elliptic-correction --output-stem d_cm_rank2_elliptic_corrected`

The helper is compiled in a temporary directory and removed. It is independently checked against108 tuple-monomial Cauchy evaluations. Previous executable programs are never run during reconstruction: the required pure definitions are loaded by AST, and the one read-only reconstruction module has a main guard. The source word hashes are verified before evaluation.

All six D44/D45 commands passed fresh copied-source execution. Entire JSON certificates match after removing only `elapsed_seconds`. Parent independent audit is pending.

## Completed independent verification

Root read the full proofs and all six mathematical programs; six fresh commands from copied sources and fifteen copied inputs passed. Complete JSON equality holds after removing only summary.elapsed_seconds. A separate root program verified the four-term separator and both elliptic correction masks. See root_d44_d45_audit.json and root_d44_d45_comparison.json.
