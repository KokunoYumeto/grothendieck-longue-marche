# E.48: exact source maps and independent replay

The statement is in `sections/E_a6_full_agent.tex`. Its proved common source is the actual image of B in D23 × G_A6. The full simultaneous G_L comparison is a subsequent task. The same scalar label is now verified on every retained old word, but that equality is not used as a substitute for a combined-source morphism.

## Mathematical map

All maps begin with the same B = C2 * C3, with x = (r^-1 s)^2 and y = (s r^-1)^2. The six Ferrari evaluations are induced through all six B/F cosets. The original degree38160 representation is faithfully compressed to degree9462 with actual pointwise B-set intertwiners.

Write P = image(N), E = image(F'), E1 = image(F''), and C for the certified perfect normal subgroup. The exact layers are:

| Map | Actual kernel/quotient |
|---|---|
| G → S3 | image(F) |
| image(F) → (Z/120)^2 | E; ordinary ordered x,y exponent sums |
| E → F3^9 | E1; nine literal commutator-word generators |
| E1 → F2^6 | C; six literal nested derived words |
| G → G/C | C perfect and normal; quotient order108839116800 |
| E → E/P' | F3^3 via the printed 3×9 matrix Q3 |
| ker(D23) ∩ F' → G | entire P' = image(gamma5 N) |

The last equality is proved by the complete old kernel presentation, the six literal squared relators, the full binary gamma5 preimages, the exact N′ order, and perfectness of C. Its proof does not identify a quotient by order without its map.

On the complete norm space Q3(f) = (2,1,0) c2(f) modulo3. The actual double-cover coefficient has c2([x,y]) = -1. Nakamura–Schneps §2 equation(2.4), Lemma2.3 gives c2(f_sigma) = +kappa2(sigma), in the positive-root convention. The actual Kummer character is onto modulo3 on the cyclotomic kernel. This gives the Galois choice used in the full correction.

The common-source generation proof uses the actual epimorphisms B → D23 and B → G. Only the explicitly presented solvable quotient G/C is proved invariant under the48 finite norm maps. No invariance of ker(B → D23), ker(B → G), or the four-strand target kernel is assumed.

## Stable model and source inputs

Read-only data reconstruction is `code/de_ferrari_a6_source_data.py`. It checks the97 N words against the previous exact source certificate and executes no legacy main program.

The following Python programs have authoritative `.out`, `.json`, and where used `.npz` outputs with the same stem:

1. `de_ferrari_a6_kernels.py`: the accepted E45 53 epikernels and their actual Aut(A6) transporters.
2. `de_ferrari_a6_model.py`: full1060-point target, all composition checks, and its exact free image.
3. `de_ferrari_a6_source_verified.py`: all36 induced components, every compression intertwiner, final point reordering, and comparison with the literal source certificate.
4. `de_ferrari_a6_N_quotient.py`: the exact Q576 → G/P map, all1152 generator edges, and the exponent lattice.
5. `de_ferrari_a6_abelian_compare.py`: literal S120 and D23 → S24 maps.
6. `de_ferrari_a6_target_derived.py`: full target derived image and its maximum solvable braid-parity quotient.

`de_ferrari_a6_source.py` contains the source construction and compression. Its initial SymPy group-order search was interrupted after the complete compression had been saved. The authoritative source order is the C++ certificate below, not that interrupted search. The source-verification program reconstructs the complete model without rerunning the slow SymPy search.

## Exact group engine and certificates

Compile `de_a6_schreier.cpp` with C++17 and optimization. The resulting executable is conventionally named `de_a6_schreier_fast`. Its `--replay certificate.bin` mode verifies every original-word DAG value, every stabilizer transversal and every complete final Schreier relation. Derived mode additionally proves both derived-group inclusions through its source membership flags, original commutators and normality checks.

The right-permutation convention is (p*q)[i] = q[p[i]]. The independent NumPy implementation in `de_a6_schreier_certificate.py` uses the same convention and compares full arrays.

| Certificate stem | Exact group | Complete final Schreier checks |
|---|---|---:|
| de_a6_schreier_full_ordered | G |865049|
| de_a6_schreier_N | P |787039|
| de_a6_schreier_Fprime | E |633288|
| de_a6_schreier_Fprimecompact | same E, nine selected actual generators |669694 in fresh replay|
| de_a6_schreier_Nprime | P' |731289|
| de_a6_schreier_Fprimeprime | E1 |704272|
| de_a6_schreier_residual | C |718488|
| de_a6_schreier_residual_derived | derived group of ten literal C words, equal C |720615|

The full G, P, E, E1, C and final C-derived chains have already been replayed independently in this session; the source calculations retain their original complete checks for every listed chain. Root can replay all `.bin` files in an isolated copy. The E-compact certificate retains all276 candidate generators by membership; its selected nine are linked to the full E word certificate.

The two deterministic mixture-input files record every signed strong-generator word. Mixtures are only used to choose input words. Perfection follows from the actual derived-word inclusion and the independently certified equal order.

`de_ferrari_a6_residual_certificate.py` independently reconstructs both nested mixture lists, compares them with the exact next certificate originals, replays all word DAGs, and prints the successive kernel map and input hashes. It does not replace the complete C++ stabilizer-chain replay.

The additional exact C++ tools are:

| Program | Inputs / purpose |
|---|---|
| de_a6_subgroup_checks.cpp | replay C, check normality under the exact G s,r; output residual_normal.json |
| de_a6_quotient.cpp | exact full-permutation canonical cosets, with complete normality checks; used for G/P72 and E1/C64 |
| de_a6_module.cpp | replay E-compact and E1, identify the actual F3^9 quotient and its S/R/X/Y actions |
| de_a6_binary_module.cpp | replay C and E1, verify all64 actual cosets and the full F2^6 action, and construct the literal odd complement |

Exact invocations, run from the copied `code` directory:

```sh
./de_a6_subgroup_checks de_a6_schreier_residual.bin de_a6_schreier_full_ordered.input de_a6_schreier_residual_normal.json normal
./de_a6_quotient de_a6_schreier_N.bin de_a6_schreier_full_ordered.input de_a6_source_mod_N.json 72
./de_a6_module de_a6_schreier_Fprimecompact.bin de_a6_schreier_Fprimeprime.bin de_a6_schreier_full_ordered.input de_a6_module_basis.input de_a6_module.json
./de_a6_quotient de_a6_schreier_residual.bin de_a6_schreier_Fprimeprime_all.input de_a6_residual_quotient.json 64
python de_a6_residual_module_prepare.py
./de_a6_binary_module de_a6_schreier_residual.bin de_a6_schreier_Fprimeprime.bin de_a6_binary_module_basis.input de_a6_schreier_full_ordered.input de_a6_schreier_Fprime_compact.input de_a6_binary_module_V.input de_a6_binary_module.json
```

All input permutation entries are range-checked and validated as permutations by the new comparison tools. The actual source inputs also pass the independent NumPy validation. Canonical-coset hashes only select buckets; equality always compares the complete permutation arrays.

## Small complete-fibre replay, in dependency order

Run the following Python programs after the finite quotient data above. Their existing names are authoritative and their successful outputs have the same stems. Each program is read-only on the accepted earlier D/E certificates.

```sh
python de_ferrari_a6_residual_certificate.py
python de_ferrari_a6_metabelian.py
python de_ferrari_a6_metafibres.py
python de_ferrari_a6_metageneration.py
python de_ferrari_a6_metawords.py
python de_ferrari_a6_solvable.py
python de_ferrari_a6_solvable_lift.py
python de_ferrari_a6_solvable_endomorphisms.py
python de_ferrari_a6_common.py
python de_ferrari_a6_common_words.py
python de_ferrari_a6_kummer_labels.py
```

These retain all6668 old normal-relator values, the entire exact correction image, all864 old records, all27 ternary norm points, every binary norm lift, every compatible multiplier residue, all48 full-presentation automorphisms of G/C, six actual squared relators, six actual gamma5 words, the quotient/scalar matrices, and the explicit equality of the two positive-root labels on every old fibre.

Observed runtimes for the small end of the package: metabelian0.627s; complete old fibres7.265s; literal B/norm/generation2.929s; first literal old-source replay12.905s; full solvable collector0.635s; all final norm lifts6.105s; full-presentation checks1.020s; common-kernel/Kummer comparison1.926s; gamma5 old-source replay15.579s. Elapsed-time fields are provenance and may change on replay; mathematical arrays and records must agree.

## Preserved attempts and scope

Earlier interrupted discovery logs and metadata-field failures are retained as described in `DE_a6.md`. No negative mathematical assertion was inferred from them. The new complete norm calculations retain all parameter spaces; the restriction to the identity value would cover288 of864 points and is not used.

The previously completed A6/A5 joint source order is in `de_a6_a5_common_source.bin` and `de_a6_a5_common_source_order.out`. It is a separate actual joint-image calculation, with common quotient order291600000. It has not been promoted to a simultaneous G_L lifting result. New joint-source work will use a separate prefix so the E48 replay inputs remain stable.
