# E.56 — exact integral symplectic targets

## Result and exact maps

The first three original column transvections generate the entire vector stabilizer of `c=e1+e3` over every modulus prime to six. The stabilizer is the displayed Heisenberg group on `(w,z)`, with multiplication

\[
(w,z)(w',z')=(w+w',z+z'+\langle w,w'\rangle),
\]

semidirect by the actual `SL2` action on `W=<e1,e2>`. The fourth transvection generates the whole `Sp4`. The proof gives elementary elimination over each local ring and actual CRT-supported transvection words for arbitrary moduli. Compactness retains the full product of all p-adic levels.

The original saved model is not silently changed. Its column matrices are `T_i`; its right-permutation ordinary matrix coordinates are `M_i=T_i^t`. The exact conjugation is

\[
J^{-1}M_iJ=T_i^{-1}.
\]

On the source this is the actual braid mirror automorphism. The first three right matrices fix the row `c^t`, and, in E.52's column form `Omega=J^{-1}`, fix the column `Jc=-e4`. The proof names both stabilizers and the conjugating map.

## Common quotients

The vector stabilizers and full symplectic groups are perfect. Their actual maps to `PSL2(F_p)` and `PSp4(F_p)` have solvable kernels, including the complete principal-congruence and scalar kernels. Every proper normal subgroup is contained in the specified kernel: a normal subgroup projecting onto the simple target would leave a solvable quotient of a perfect group. Thus every nontrivial quotient retains the actual specified simple quotient.

For the vector stabilizer, a nontrivial common quotient with `T_L` would force one literal projective matrix map through `T_L`. The exact level-five and level-seven product certificates exclude those two primes. At every larger prime, the target order has a prime divisor absent from `T_L`. The checked exact factorization is

\[
|T_L|=2^{117}3^{36}5^{31}7^2.
\]

This proves the full actual product with `T_L` at all prime powers and mixed moduli. The solvable kernel of the old `T23` comparison retains its precise fibre product over `S_L`.

The proof supplies an elementary simplicity argument for `PSp4(F_p)`: the projective line stabilizer has orbits of sizes `1,p^2+p,p^3`, giving primitivity by the explicit block-size divisibility test. Its normal abelian transvection subgroup has conjugates generating the group. The normal-subgroup argument then proves simplicity. The group orders exclude `A96` from every simple quotient in the two symplectic families. Therefore the literal Hurwitz map supplies the full extra direct factor at every finite level and in the complete inverse limit.

The final statement includes generation for the E.55 corrected words. Their new matrix, `T_L`, and Hurwitz components are one actual Galois precomposition; the separately retained `T23` map is handled through its specified solvable quotient. No finite source-kernel invariance is asserted.

## Authoritative files and replay

- Fragment: `sections/E_symplectic_integral_targets_agent.tex`.
- Single replay program: `code/bc_symplectic_integral_targets.py`.
- Outputs: the same prefix with `.out` and `.json`.
- Manifest: `research/E56_authoritative_manifest.json`.

The program imports only Python's standard library, NumPy, and SymPy. Its four data dependencies are the two saved p5/p7 model NPZ files and the two complete p5/p7 target JSON certificates listed in the manifest. It does not execute a previous output-writing program.

The authoritative run passes in **2.393 seconds**. It checks exact polynomial identities, every one of the 12,096 saved permutation entries, complete elimination of all 624 and 2,400 nonzero vectors over the two fields, and 112 independent symplectic-basis matrix factorizations over `5,7,25,49,35,175,245`. Each modulus retains a full word witness in the original four transvections. All protected originals are unchanged.

The section compiles independently to five pages with no overfull or underfull boxes. The preliminary formatting fragment and the initial missing-system-format attempt are preserved under `research/E56_format_preserved/` and `research/E56_build_check/`. The successful standalone check uses the existing project format and isolated auxiliary directories. The earlier complete positive certificate, before the additional exact `T_L` order-factorization check, is preserved under `research/E56_initial_certificate/`.

## Audit coordination

The geometry agent's full E.55 proof audit is recorded separately in `research/BC_integral_fibres_audit.md`, including the exact source SHA-256. The profinite agent independently checked the simple-quotient reduction and the Iwasawa/projective-line argument while this fragment was being written. A full fragment read and the root isolated replay remain separate audit steps.
