# E68: exact E66/E67 common source and 1152 word preimages

Proof: `sections/E_distribution_orbifold_agent.tex`.

Run the isolated replay from LM7_PUSH, with a fresh destination:

```sh
python code/a_cm_distribution_orbifold_replay.py --destination research/root_E68_replay
```

Requirements are Python with NumPy and a C++17 compiler. The driver copies only the minimal files listed by `E68_authoritative_manifest.json`. All older E62/E66 inputs and the peer's E67 exports are read-only. No legacy main program is executed.

## Exact source retained

The first program joins the literal E66 5223-point source and E67's 108-point source on the identical 97 words of N_B. It checks the word lists letter by letter and replays every word in the exported E67 free-generator permutations. It computes the complete common derived image before restricting the cyclic covers to their coordinate-zero blocks.

The new correction image on 4957 points has order 7,011,906,707,722,862,592, exactly the product of E66's order 356,241,767,399,424 and E67's order 19,683. Both projections are the actual unchanged quotient maps. It tests all 1152 combinations of the four E62 corrections, three E66 tuples and four E67 targets above each of the 24 E17 origins.

The E17 words come from `de_ferrari_fibres.json`. Each word is reevaluated in E67's twelve maps. Its absolute target difference is computed from that value. No correction is carried across from E67's distinct original E1 word family.

The second program produces an actual word preimage for every combination by composing the complete projected and derived-source word DAGs. It replays all 24,363 ancestors on the full 5331-point source, retaining each exact Ferrari, distribution and orbifold value. The full preimage DAG has 26,479 nodes; every preimage belongs to N_B-prime by its derived-source construction.

## Replay gates

The driver rebuilds the complete Schreier verifier and runs both new programs. It compares every mathematical JSON field (only runtime fields are excluded), every NPZ array and every array in all four complete group certificates. It independently replays all retained literal strong words. Every protected original hash is checked before and after.

The witness JSON records the preceding JSON's byte hash, which also depends on its measured runtime. The driver verifies each recorded hash against the exact authoritative or regenerated input bytes, then excludes only this single timing-dependent hash from mathematical equality. Every fixed input hash is still compared exactly. The initial replay and its precise diagnosis are retained in `E68_self_replay` and `E68_replay_diagnosis.*`; they verified equal mathematical outputs and arrays but stopped on this runtime-dependent input hash. The original driver and manifest are preserved separately, as is an unexecuted intermediate driver considered before adopting this narrower check.

The four certificates have suffixes `_N`, `_N_derived`, `_projected` and `_orbifold` after the program prefix `a_cm_distribution_orbifold`. The output is an exact common-source finite comparison and its complete fibres inside each f_i N_B-prime. It makes no assertion of generation in the enlarged distribution source or of a full-GT lift.
