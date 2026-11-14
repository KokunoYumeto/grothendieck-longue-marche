# Isolated replay: cyclic-three source-map batch

This unnumbered research batch is separate from E65 and E62. Its proof
and scopes are in `A_E3_cyclic_core.md`. It computes the single cyclic
map, its three based coordinates, and the complete six-coset B-core on
the exact retained N_B source. The resulting correction image has
abelianization C3, and its actual joint image with E62's binary C is
therefore the direct product. No extra-coordinate equation or full-GT
character value is asserted.

From LM7_PUSH, run:

```sh
python code/a_cm_kummer3_replay.py --destination research/root_K3_source_replay
```

The destination must not exist. Required tools are Python with NumPy,
and a C++17 compiler. The driver copies only the manifest's nine input
files into a fresh directory, rebuilds the existing complete Schreier
verifier, executes all three new programs, compares every mathematical
JSON field and NPZ array, and compares/replays all five complete group
certificates. It verifies the original hashes before and after.

The failed initial attempt is preserved with its own manifest in
`A_K3_core_initial_attempt/`. It attempted a second-derived calculation
using 4,600 generators and was killed by the memory limit. The final
program first certifies a 16-generator subset and succeeds. The failed
attempt is not repeated by the replay driver.

The proof-bearing files are the three new programs, the exact source
helper, and the complete Schreier verifier. The old matrix/source inputs
are copied read-only. No legacy main program is executed. The final
complete core certificates have 12,512, 9,544, 131,016, 1,752 and 2,104
Schreier relations respectively, with all derived normality checks
retained.
