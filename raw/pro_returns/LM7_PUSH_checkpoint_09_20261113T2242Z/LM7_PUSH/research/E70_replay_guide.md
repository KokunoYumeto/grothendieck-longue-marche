# E70: exact full Gaussian pro-three source

The authoritative statement is `sections/E_gaussian_pro3_agent.tex`. Its scope is the actual six-coordinate Gaussian pro-three image, all twelve abelian characters, the complete common image with the finite E66 and Mordell sources, and compatible whole-tower lifts of all 3456 E69 targets. It makes no full-GT lift claim.

## Dependency order

1. `bc_gaussian_pro3_maps.py` checks the integral class-two covariance identities, the literal free-kernel and source words, and all four unrestricted integral norm-frame families. It uses only Python and SymPy.
2. `bc_gaussian_pro3_frattini_model.py` constructs the characteristic order-2187 class-three quotient using four literal upper-unitriangular matrix maps; checks all Hall values, the actual order-four action, and all 97 source words; and exports the six induced permutation maps. Input: `bc_cm_literal_words.json`.
3. `bc_gaussian_pro3_frattini_common.py` adjoins the Gaussian maps and the six unchanged Mordell maps to the actual 5223-point E66 source, then computes the actual image of N and its derived image before making any retained projection. It produces six complete Schreier certificates and runs a second complete word-and-relation replay for each. Inputs are the preceding model, the frozen E67 export, the frozen E66 source JSON/NPZ, and the shared exact Schreier implementation.
4. `bc_gaussian_pro3_frattini_characters.py` decodes the generated Gaussian certificate into the twelve actual Frattini coordinates, checks all 2187 automorphism images and generating products, and checks every saved character word DAG.

The isolated driver `code/bc_gaussian_pro3_replay.py` copies only the frozen input files and the four programs, compiles `de_a6_schreier.cpp` with `g++ -O3 -std=c++17`, and runs this order. Expected total execution time is about 55 seconds, including compilation, on the current workspace machine.

Run from the project root:

```bash
python code/bc_gaussian_pro3_replay.py --directory research/E70_independent_replay_NAME
```

The directory must be fresh. The authoritative manifest is `research/E70_authoritative_manifest.json`.

## Exact comparisons

The driver verifies every protected original hash before and after execution. For every output it compares all mathematical JSON fields recursively and every NPZ array. It omits only elapsed-time fields and input-provenance hashes; each omitted provenance hash is first checked against the actual bytes on its own side of the comparison. Source hashes remain part of the mathematical comparison. The six generated `.input` and `.bin` certificates must also be byte-identical to the authoritative originals. Every regenerated certificate is independently replayed by the C++ verifier as part of the mathematical program.

The six certificate prefixes are `bc_gaussian_pro3_common_` followed by `N`, `N_derived`, `projected`, `Mordell_Gaussian`, `Gaussian`, and `E66_Gaussian`.

The expected Gaussian image has order 3^27; the Mordell/Gaussian image has order 3^30. All three tested common-quotient orders are 1. The Gaussian character certificate has rank 12, including the six weight-three characters. These are the exact finite inputs to the pro-three Frattini and Goursat arguments in the proof.

## Layout and preservation

The five-page standalone proof is in `research/E70_standalone/`. All five rendered pages were viewed. There are no overfull boxes or undefined-reference warnings. The source before the purely typographical repairs is preserved as `research/E70_reviewed_before_layout.tex`. The repairs supply missing mathematical spacing commands, split two displays, and shorten one inline coordinate description; they do not change a mathematical assertion or map.

The four mathematical programs and their authoritative outputs are frozen with the manifest. Subsequent exploration must use new names.
