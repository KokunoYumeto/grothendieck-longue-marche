# E.71 complete replay

The proof is `sections/E_kn_matrix_agent.tex`. The authoritative manifest `research/E71_authoritative_manifest.json` hashes the complete mathematical batch and the accepted read-only dependencies. The root assembler, main document and register are outside this batch.

## Exact domain and result

The domain is the whole `K6 intersect F-prime`. The integral exponent matrix has image index12 and Smith factors2,6. Its explicit unimodular kernel basis supplies95 actual sixth-power words. The resulting correction image has order2^105 3^17; its commutator-only intermediate has index4. Their quotient is cyclic, identified by the actual coefficient `c2/6 mod4`.

All1152 E68 values remain. Over each, all16 compatible mod24 coefficient pairs satisfy every one of the34 literal GL2(F3)/SL2(F3) K2 and K3 equations, with exactly one finite correction value per pair. All18432 word preimages are replayed in the original11691-point source. The smaller N-prime intermediate has4608 values and is retained separately.

## Minimal execution

Run:

```sh
python code/a_cm_kn23_replay.py --destination /absolute/new/replay/directory
```

The destination must not exist. Python3, NumPy and a C++17 compiler suffice. The manifest lists the minimal copied inputs, including the19 accepted class-two prefix certificates. The driver compiles the unchanged complete Schreier engine and the small prescribed-base wrapper in the new directory only.

Nine mathematical stages run sequentially:

1. `a_cm_kn23_model.py`: all actual matrix multiplication tables,34 epikernel maps, the cyclic-cover left-right actions and97 literal source words.
2. `a_cm_kn23_source.py`: complete N and N-prime presentations and the kernel over E68, with all final Schreier relations replayed. This dominates the runtime, approximately eight minutes in the initial run.
3. `a_cm_kn23_ab_lattice.py`: integral unimodular exponent reduction, both inverse identities,95 actual kernel words and all sixth-power values.
4. `a_cm_kn23_full.py`: the entire enlarged correction image and its actual old-value kernel.
5. `a_cm_kn23_fibres.py`: all13824 old candidates and all18432 compatible coefficient/fixed-tuple queries.
6. `a_cm_kn23_witnesses.py`: substitution of every transporter into the actual97-generator word DAG, full11691-point replay, exact free exponents and N exponents modulo six.
7. `a_cm_kn23_nprime_comparison.py`: all four quotient cosets with their exact multiplication, and the smaller complete N-prime fibre counts.
8. `a_cm_kn23_coefficient.py`: the exact integral coefficient row, its gcd and the cyclic quotient map.
9. `a_cm_kn23_numeric_summary.py`: reconstruction of all printed prime-power orders from their complete certificates.

The expected total is approximately nine minutes; no single tool wait needs to block for that duration. Every stage saves stdout and stderr separately. Every mathematical JSON field and every NPZ array is compared. All six complete Schreier certificates, their original input permutations and prescribed bases are compared and independently replayed. The original batch is hash-checked before and after.

## Timing and provenance

Only elapsed-time fields are removed from mathematical equality. Each recorded input hash is first verified against its respective original or regenerated file. A hash is then omitted from mathematical equality only when it points to a generated JSON file whose elapsed time can change. Fixed input hashes, all NPZ hashes and all mathematical data remain exact.

## Preserved failed step

`research/A_Kn23_failed_elementary_quotient/` retains the initial optional quotient-structure guess, program and assertion failure. The assertion that all extra squares lie in the N-prime image is false. The corrected enumeration proves the quotient is cyclic of order4. The complete full-domain fibre run and witness replay never used the failed assertion.

## Scope

These are the exact finite maps and conditions of E71. They preserve the E17 origins and every E68 retained value. They assign neither a full-GT lift nor a new source-generation property to the finite word witnesses.
