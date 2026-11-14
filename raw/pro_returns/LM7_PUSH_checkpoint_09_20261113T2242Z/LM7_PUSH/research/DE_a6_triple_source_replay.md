# 3.A6 induced source and perfect-residual replay

This frozen batch proves the exact source, the specified level-twelve
base map, the full 79-dimensional ternary kernel, and its new perfect
residual. It does not assert the still-running E.60 CM/pentagon fibre
calculation. The mathematical map and the complete central-shift proof
are in `DE_a6_triple_source.md`.

## Frozen and continuing files

`code/de_a6_triple_source_manifest.json` is authoritative for this batch.
The separate cover/target batch has already passed the parent’s full
isolated replay; its original files remain unchanged. The new files
whose names contain `signed` are continuing work and are excluded from
this source manifest. Future fibre calculations likewise use new names.

Use an isolated copied `code` directory. Compile the unchanged exact
engine and the following new evaluators with C++17 and optimization:

```sh
g++ -O3 -std=c++17 de_a6_schreier.cpp -o de_a6_schreier_fast
g++ -O3 -std=c++17 de_a6_triple_affine.cpp -o de_a6_triple_affine
g++ -O3 -std=c++17 de_a6_triple_kernel.cpp -o de_a6_triple_kernel
g++ -O3 -std=c++17 de_a6_triple_central.cpp -o de_a6_triple_central
```

The central collector header is a byte-for-byte slice of the executed
main kernel collector; the preparation program checks this equality.
No accepted older C++ source was edited.

## Actual affine and ordinary level-twelve comparison

```sh
python de_a6_triple_affine_prepare.py
./de_a6_triple_affine de_a6_schreier_full_ordered.bin de_a6_triple_affine.input de_a6_triple_affine_factor.json
python de_a6_triple_base_prepare.py
python de_a6_triple_modular_prepare.py
./de_a6_schreier_fast --replay de_a6_triple_modular.bin
```

The affine factorization evaluator preserves a literal negative witness:
the affine map does not factor through the old A6 map alone. It stops
at that witnessed failure of factorization, not at an unverified rank
bound. The independent preparation replays the word in both maps.

The supplied complete new base is `de_a6_triple_base.bin`, degree 9786.
Its complete replay also occurs at the start of the kernel evaluator
below. The supplied complete joint modular chain is
`de_a6_triple_modular.bin`, degree 10362. Both have 873463 final
relations and the same order, eight times the old A6 source order.
Every original and strong-generator word is replayed. The two seed
files are explicitly incomplete seeds; do not substitute them for
either complete chain.

Repeating discovery is unnecessary. For a full discovery reproduction,
compile `de_a6_triple_base.cpp` and apply it to the corresponding seed
and final binary filenames. The original discovery took 135.174 and
134.306 seconds, respectively. Discovery is distinct from replay.

## Entire relative ternary kernel

```sh
python de_a6_triple_kernel_prepare.py
./de_a6_triple_kernel de_a6_triple_kernel_model.bin de_a6_triple_base.bin de_a6_triple_kernel.json
python de_a6_triple_kernel_replay.py
```

This evaluates every one of the 873463 relations in the full 36-factor
source, closes the image under both source generators, and obtains
dimension 79. It retains a literal word for every basis vector. The
independent Python replay verifies all 79 words, all 158 source
conjugations, and the actual ten C lifts. It also retains the H-action
and proves that the source x,y have 120th powers one.

The complete run took 580.937 seconds; the independent Python replay
took 22.946 seconds. Neither is a noncofinal-to-profinite inference.

## Entire C-preimage abelianization and all lift freedoms

```sh
python de_a6_triple_central_prepare.py
./de_a6_triple_central de_a6_triple_kernel_model.bin de_a6_triple_central_model.bin de_a6_schreier_residual_derived.bin de_a6_triple_central.json
python de_a6_triple_central_replay.py
python de_a6_triple_source_certificate.py
```

The central evaluator first completely replays the accepted C chain.
It then uses ten source lifts and 27 independent central coordinates.
All ten original-to-normal-form links and all 720615 Schreier relations
are evaluated. The result is rank 34 in 37 columns, giving a genuine
three-dimensional abelian quotient. There is no early-stop shortcut in
this execution. Its derived subgroup is perfect by the explicitly
proved abelian-kernel commutator lemma, and its relative kernel has
dimension 76.

The independent replay checks every one of the 34 selected literal
relations in both actual maps, all signs, and all 270 elementary
generator-shift changes. It saves the quotient map on the entire
79-dimensional kernel, the ten lift values, and the B and H quotient
actions. It took 10.908 seconds. The complete central run took
463.064 seconds.

The final source certificate checks the entire eight-element quaternion
map to Q12, all 64 products, its explicit quaternion presentation, and
the specified level-twelve projection. It combines these literal maps
with the complete chain orders to identify the base with
`im(B -> G_A6 x Q12)`. The accepted literal `G_L -> Q12` comparison is
the exact old source map used for the subsequent signed-source work.

## Comparisons and preserved incomplete execution

Compare every mathematical JSON field and every NPZ array exactly.
Elapsed times, and hashes of freshly regenerated files containing those
times, may change. Strong-generator and literal-word arrays in this
batch are deterministic and must be equal. Keep all original artifacts
read-only and write replay stdout under separate names.

The original central process had no result when its runtime session
became unavailable. Its two empty logs are preserved with a status and
hash record under `de_a6_triple_central_incomplete_runtime.*`. The
completed output belongs to the later unchanged-program execution.
The incomplete process is not represented as a completed certificate.

Do not invoke legacy imported programs’ main entrypoints merely because
they occur in the dependency closure. The supplied `load_data()` API is
read-only. Existing E.48/E.54 and cover/target root replays cover their
unchanged inputs; the new lifted relation evaluations above are the new
claims requiring a complete replay.
