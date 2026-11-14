# D66: the actual quadratic compact source correction

The proof is `sections/D_quadratic_compact_source.tex`. It constructs the actual marked class-two quotient, its small comparison, the two source conjugator lifts through S57, and the exact new quotient X66. The original full profinite realization remains unresolved, with the explicit nonzero remaining kernel retained.

## Replay

Use Python 3 with NumPy. The ten immutable inputs and their original source hashes are listed in `input_manifest.json`.

The complete copied-input author replay is `audit/d66_replay.py`. It starts with only those ten inputs and the nine copied programs. Every program is executed, and its entire JSON and stdout are compared with the retained result, excluding only elapsed_seconds values. Each freshly generated result is retained under `audit/copied_replay/fresh_outputs`; after that complete comparison its original raw result is restored for the next consumer, retaining exact declared input hashes. No mathematical or input-hash field is excluded.

Run the following programs in order, retaining actual stdout under the same basename with `.out`:

1. `d_old_compact_integral.py`
2. `d_old_compact_secondary.py`
3. `d_old_compact_relaxation.py`
4. `d_old_compact_tate_action.py`
5. `d_old_compact_all_isometries.py`
6. `d_old_compact_source_cochain.py`
7. `d_old_compact_quadratic_source.py`
8. `d_old_compact_relative_correction.py`
9. `d_old_compact_global_kernel.py`

The first five programs preserve the completed integral/secondary-norm tests and complete isometry classification. The last four give the actual projective edge cochain, full quadratic source group, relative integral corrections with the small class-two map, and exact induced norm-kernel module.

The unsuccessful helper/syntax runs and the successful earlier global-kernel run remain in `code/history` with their actual outputs. `audit/setup_failure.txt` records an initial replay-directory setup failure before any mathematical program ran. They are provenance, not final successful certificates.

The source finite quotient has cusp order twelve; the retained arithmetic source still has cusp order 36. The complete source involution, the image of t^18, all 36-factor repairs, and the actual maps between them are proved in the section.
