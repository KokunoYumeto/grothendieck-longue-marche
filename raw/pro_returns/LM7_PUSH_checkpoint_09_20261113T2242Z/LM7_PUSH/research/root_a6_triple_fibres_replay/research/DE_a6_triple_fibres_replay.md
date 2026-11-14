# E60: complete signed 3.A6 fibres and joint targets

The authoritative file list is `code/de_a6_triple_fibres_manifest.json`.
The proof is `sections/E_a6_triple_agent.tex`; the detailed group maps
and correction argument are in `DE_a6_triple_fibres.md`.

This package continues the separately frozen cover/model and source
packages. Those earlier packages already have complete parent replays.
Their original files are unchanged and their manifest hashes are checked
by the new manifest. The new claims are the whole signed kernel, the
rank-three stable commutator image, every old CM fibre, and the exact
common four-strand target. The result retains the full old E57 inverse
system. It does not assert the full profinite pentagon for an extra pair.

## Exact map register

| Map | Complete new information |
|---|---|
| `X -> B0=im(B -> G_A6 x Q12)` | Prior frozen kernel `K=F3^79`; base kernel to `G_A6` is the specified `Q8` |
| `im(B -> X x G_L) -> J` | Every one of the same79 kernel coordinates remains available; the actual source is `X x_(B0) J` |
| `E -> C`, with `D=E'` | Prior frozen `E_ab=F3^3`, `D` perfect, relative kernel76 |
| Stable six-dimensional old module to `E_ab` | All15 commutators evaluated; three actual values have determinant4 modulo3 |
| `I=gamma5(N) intersect R_nil(H)` | Full preimage of the old stable image; kernel over the whole old source maps onto all79 new coordinates |
| Uniform and E59/E62 retention | The actual old image has no `C3` quotient, including its finite-two-group extension; the full79-dimensional kernel can be corrected while retaining those maps |
| `T_new -> Sigma=S_L x ASL2(F3)` | Complete specified quotient of order20736 with perfect kernel |
| `T_new -> T_(L,A6)` | Actual solvable kernel of order `8*3^108`; exact uniform/A96 target independence persists |

No order coincidence replaces a specified projection. All word and array
comparisons below use those actual projections.

## Isolated replay setup

Copy the manifest's `records` paths into a separate directory retaining
the `code/` layout. Copy its `documents` separately for proof inspection.
Run the commands in the copied `code` directory. Do not execute any legacy
module's `main()` merely because its file belongs to the import closure.
The `load_data()` API is read-only. Do not run the search driver
`de_a6_triple_target_continue.py` on the supplied final chains; it is a
preserved discovery program and deliberately rejects existing outputs.

Compile the complete engine and query evaluator:

```sh
g++ -O3 -std=c++17 de_a6_schreier.cpp -o e60_schreier
g++ -O3 -std=c++17 de_a6_triple_query.cpp -o e60_queries
```

The query header is an exact slice of the frozen source collector;
the independent query replay checks this byte comparison explicitly.
The compiled executables are reproducible and are not authoritative
inputs to the mathematical certificates.

## Signed source: full lower bound, matching exact upper bound

```sh
python de_a6_triple_signed_base_prepare.py
./e60_schreier --replay de_a6_triple_signed_base.bin
python de_a6_triple_signed_replay.py
```

The complete base has degree11334 and1159255 final relations. Its old
degree11010 block is retained literally; its index over that actual old
source is two. The new affine coordinates are appended, not inferred from
the level-twelve map alone.

The saved `de_a6_triple_signed_kernel.json` contains79 actual source words.
The Python replay evaluates every one in both the full cover source and
the actual signed base, verifies all158 source conjugates, and gives an
invertible79-by-79 transition to the previously certified entire kernel.
This is already a complete lower-bound/upper-bound proof: the new kernel
contains all79 old coordinates and is contained in that old79-dimensional
kernel. It does not require repeating the full signed relation search.

The entire1159255-relation signed enumeration is nevertheless preserved
and can be independently rerun with:

```sh
g++ -O3 -std=c++17 de_a6_triple_kernel.cpp -o e60_full_kernel
./e60_full_kernel de_a6_triple_signed_kernel_model.bin de_a6_triple_signed_base.bin de_a6_triple_signed_kernel.json
python de_a6_triple_signed_replay.py
```

The original enumeration took613.705seconds. The literal independent
replay took6.766seconds. The latter is the sufficient exact shortcut for
this new claim because the earlier upper bound has already been fully
replayed.

## Entire stable commutator image

```sh
python de_a6_triple_commutator_prepare.py
./e60_queries de_a6_triple_kernel_model.bin de_a6_triple_central_model.bin de_a6_schreier_residual_derived.bin de_a6_triple_commutator_queries.bin de_a6_triple_commutator_queries.json
python de_a6_triple_commutator_replay.py
python de_a6_triple_deep_certificate.py
```

Preparation keeps the nine actual old module words, their six binary
complement corrections, their fourth powers, and all six actual stable
columns. It checks actual Q12 identity and affine-linear identity of the
module lifts. It retains their possible affine translations. Only the
nine cubes and51 commutator queries are required and checked to have
entire affine identity.

The evaluator completely replays the old C chain before sifting all60
queries. It divides the permutation and cover value by the same literal
transversal words. The final quotient value is `L(k)+h(e)`, with the
positive exponent sum of those divided words. The independent Python
replay checks every original word, all9743 used normal-form ancestors,
all residues, all exponents, all15 stable values, and the determinant4
minor. The prior query run took97.7538seconds; the independent Python
replay took14.978seconds.

The perfect bridge, every lower-central term, and the compact intersection
are proved in E60.15--18 using these full images. No enumeration of only
one representative in a CM fibre is substituted for that argument.

## Full target, all literal quotient maps and every derived subgroup

```sh
python de_a6_triple_target_prepare.py
python de_a6_triple_target_quotient.py
python de_a6_triple_target_old_maps.py
python de_a6_triple_target_complete_replay.py
python de_a6_triple_target_certificate.py
```

The complete replay program recompiles the exact engine and verifies the
six supplied binary chains. It repeats every final Schreier relation,
every strong word, every required derived membership, and every original
conjugation in the final normality gate. The six final relation counts
are530615,593363,398786,655402,406798,559770:3144734 in total.
The completed fresh six-chain replay took84.233seconds, including its
fresh compilation, and protected every original input and discovery log.

The independent final Python certificate reconstructs every nested input
word from the preceding chain and compares its actual105-point quotient
value. The resulting indices are

    1,6,72,2304,20736,20736.

They agree with the entire small derived series. The last retained word
inclusion is `H5 <= H4' <= H4`; equal orders prove the full kernel perfect.
The proof never assumes that the sixteen selected mixture words generate
their large parent. The full target order is

    2^406 * 3^271 * 5^117 * 7^8 * 11^3 * 13^2.

The target quotient and old-map programs check the complete20736-element
Cayley closure, all1536 binary values and edges, and the two actual
ring maps from T23. The result is the exact fibre product over the
specified `S_L x ASL2(F3)` quotient. Its solvable kernel over the old
target is proved from the full coordinate law, giving the uniform and
Hurwitz direct factors in E60.24.

## Exact output comparison and preserved failures

Compare every NPZ key, shape, dtype and value exactly. Compare all
mathematical JSON data exactly. Elapsed times and hashes of regenerated
files that include those times are provenance. For the complete C++
chain reports retain the exact order, all orbit lengths and bases, all
strong and DAG counts, derived flag and final relation count. The
discovery scans and selected discovery indices are separate provenance.

The normal-conjugation counter in a discovery run includes exploratory
closure scans as well as its final check. A replay's exact final count is
`number_of_original_generators * number_of_final_strong_generators` in
derived mode, and zero otherwise. The wrapper requires that equality
and retains both raw counters. This compares the entire gate rather than
discarding a mathematical check because a progress counter differs.

All of these unsuccessful attempts remain preserved:

- `de_a6_triple_commutator_prepare_failed_affine_identity`: the rejected
  assertion that Q12 identity would force the entire affine value one.
- `de_a6_triple_query_failed_include`: a compile-only nested-main macro
  error; no evaluator ran.
- `de_a6_triple_target_derived2_failed_once_mixtures`: a valid completed
  smaller subgroup with index144. Its ten once-per-generator mixtures
  had only half the required small quotient image. No parent-generation
  claim survived that check.
- `de_a6_triple_target_complete_replay_failed_legacy_log`: the ordinary
  discovery log used an older report schema. The modern complete replay
  added `derived_mode=false` and zero normal-conjugation checks; every
  existing mathematical field agreed.
- `de_a6_triple_target_complete_replay_failed_discovery_normal_count`:
  discovery reported1735 total conjugation scans for stage one, whereas
  its complete replay correctly reported867=3*289 final checks. The
  corrected wrapper verifies the exact rectangular gate at every stage.

Original program versions, stdout, stderr and relevant first-replay logs
are retained with those prefixes. None of these failures changes a
previously accepted certificate or is represented as a successful run.

The parent and arithmetic agent have independently read the complete
source bridge and intersection proof. Arithmetic also independently read
E60.19--24 and the enlarged target statement. Their reports distinguish
proof/code reading from a new large numerical replay.
