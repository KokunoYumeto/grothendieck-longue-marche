# D52 attempted-program provenance

All files under raw_trials are actual preserved source/output versions.

- pairing_only contains the initial invariant-equation test before the exhaustive moving modulo-four corrections were added. It completed normally and reported that the equation was not solvable.
- class2_success_first contains the first successful full quadratic search and direct complete class-two word verification, before the complete homology continuation and exponent-eight residual word were added.
- continuation_unaveraged contains an exploratory continuation that failed with exit code1. Its stdout was empty; the companion .out preserves the actual terminal stderr verbatim, and status.json records that no new JSON was written. The failure arose because the higher parity lifts had not been projected by the integral odd-deck idempotent. The final source fixes that operation and passes.

The original commands ran the corresponding program in D52_EXPERIMENTS/code, redirecting stdout to the matching .out. The sources were copied here after those executions. Runtime data are the immutable D51 pairing certificate and the owned intermediate symplectic-search JSON in code. Historical output elapsed times are retained; no historical output was recreated.
