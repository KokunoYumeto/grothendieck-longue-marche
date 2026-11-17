# Supplementary helper execution status

- `export_central_replay.py` is a serialization helper. It was executed and generated `check_central_certificate_replay.g`; its current stdout is retained in `export_central_replay.out`. This generation alone proves no group-theoretic claim.
- `check_central_certificate_replay.g` is an optional replay from the saved PC presentation. An earlier run was interrupted before completion after a slow generic group/automorphism operation. No completed replay output exists, and no replay PASS is claimed. It is not used by the proof. The complete original finite-source calculation and the parent's independent archived-path rerun supply the proof certificates.
- `probe_gap_central_extensions.g` only checks whether named GAP functions are bound. It has been executed; stdout is in `probe_gap_central_extensions.out`. It supplies no finite-group result.
- The generic Schur-cover experiment was stopped without a result and is not used.
- `next_central_two_function.g` defines the optional next-source central-two test. It has now been invoked in the live next-source session; its execution is logged in `check_second_pullback_zero_target_interactive.out`. The H2 calculation is running and no result from this helper is yet claimed.
