# E.59 isolated replay guide

## Frozen scope

The manuscript fragment is `sections/E_sl23_ferrari_agent.tex`.
The full computation enumerates every one of512 actual corrections over
each of the24 specified E.17 G6 words. It proves4 gentle values and2
pentagon values in each fibre, with complete source/target generation.
The24 base words cover all24 admissible CM matrix pairs, including12
extra pairs, through the displayed actual frame maps. Other affine G6
points and multiplier residues are outside this count.

The immutable inventory is `research/E59_authoritative_manifest.json`.
It includes the exact code dependencies, the two old input certificates,
the new proof, all saved mathematical outputs,144 generation certificates,
and the explicitly preserved incomplete or unsuccessful attempts.

## One-command replay

From the project directory, choose a destination that does not yet exist:

```bash
python code/a_cm_sl23_replay.py --destination research/root_E59_replay
```

The driver first verifies every protected original hash. It copies only
the declared inputs into the fresh destination, recompiles the exact
Schreier source with C++17/O3, and executes all seven mathematical
programs. It also regenerates the full B, N, and N-derived chains,
independently evaluates their strong words, and replays all144 final
generation certificates. All writes stay in the new directory.

Expected runtime is approximately5--6 minutes. The authoritative slowest
stage was the complete literal-word/generation run,225.538seconds.
The exhaustive nonabelian512-element correction stage took47.601seconds.
The other mathematical stages together took less than40seconds before
the final complete certificate replays.

The final `result.json` asserts exact equality of every mathematical
JSON field and every saved NPZ array. Timing fields are ignored, as is
the hash of the independently recompiled executable; its source hash
must be unchanged. Every original protected file is hashed again at
the end. The driver rejects an existing destination and never replaces
authoritative files.

A hash-only integrity check is available without a replay:

```bash
python code/a_cm_sl23_replay.py --check-only
```

## Primary mathematical inputs

- `de_ferrari_fibres.json`: the24 exact retained E.17 words, their
  integral cusp gauges, and their original actual accessory frames.
- `de_ferrari_sl2_5_N.json`: the retained97-generator Bass--Serre source
  words, used only to verify the read-only reconstruction word for word.
- `de_ferrari_a6_source_data.py`: rebuilds the actual B, F, N_B maps and
  inverse free-word coordinates; it runs no legacy main program.
- `de_ferrari_degree4_lift.py` and `de_ferrari_mod9_lift.py`: only the
  generic actual six-coset induction methods are used here. Their
  degree-specific correction functions and legacy mains are not called.
- `de_ferrari_a6_kernel_source.py`: only its exact orbit-compression
  helper is used; every removed B-orbit has a saved s/r intertwiner.
- `de_a6_schreier.cpp` and `de_a6_schreier_certificate.py`: complete
  Schreier relations plus an independent literal-word replay.

The manifest recursively includes the local modules required to import
these helpers. No A6 arithmetic result or A6 finite-group factorization
is assumed by the SL2(F3) computation.

## Main outputs

| Output | Exact content |
|---|---|
| `a_cm_sl23_model.json/.npz` | All SL2(F3) elements, automorphisms,16 epikernels, Ferrari maps, target orders |
| `a_cm_sl23_source.json/.npz` | Original97 N images, all pair/next commutator values, scoped initial word tests |
| `a_cm_sl23_induced.json/.npz` | Complete36-coordinate source and faithful1956-point compression |
| `a_cm_sl23_corrections.json/.npz` | Entire512-element group, actual N-prime parent words, all24 complete fibres |
| `a_cm_sl23_generation.json` | All96 source/48 target generation results and literal corrected F-prime words |
| `a_cm_sl23_quaternion_projections.npz` | Actual bijective map to the three quaternion evaluation images |
| `a_cm_sl23_periodic.json` | Both literal full twists at every48 pentagon point |
| `a_cm_sl23_cm_labels.json` | Exact common-left gauges,24 distinct CM pairs,12 extra sign pairs |

The source order is48,922,361,856. The target order is43,486,543,872.
The source image of N_B has order84,934,656. Its derived image has
order512. All97 sixth powers are in that same derived image.

## Preserved failed/incomplete records

The interrupted initial correction invocation produced no claim.
The first generation invocation stopped on a Python list/tuple type
error before generation. The first label helper wrongly required the
old cusp gauge to be trivial in Q; its failed assertion and source are
preserved. The corrected helper retains the actual inner Q-action and
the common-left frame transformation. The proof's corresponding exact
Goursat step was independently read and accepted by profinite_images.
These records remain outside the authoritative successful replay chain.

The initial23 failing uncorrected words are intentionally retained as
a word-only result. They are not fibre exclusions: all their512-element
fibres were subsequently exhausted, and each has the two generating
pentagon points stated above.

## Proof and typesetting review

Profinite_images independently read the complete E.59 proof, including
the actual Q-gauge comparison and the Goursat source-generation argument,
and reported PASS. This was a proof review, not a repeat execution.
The isolated LuaLaTeX check uses a separate research directory and
does not alter the active main source or build. Its final log and the
earlier filename-overflow record are both retained.
