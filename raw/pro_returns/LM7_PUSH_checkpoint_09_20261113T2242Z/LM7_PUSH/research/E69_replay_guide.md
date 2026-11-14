# E.69 exact replay guide

The frozen proof is `sections/E_gaussian_central_agent.tex`. Its complete mathematical source, outputs and read-only inputs are hashed in `research/E69_authoritative_manifest.json`.

## Order and dependencies

The four programs share `code/bc_gaussian_heisenberg_` and must run in this order:

1. `model.py`: the actual order-108 triangle, all associativity triples, all 36 frames and four automorphisms; about one second.
2. `source.py`: the identical 97 N_B words, all 4656 commutators, full normal and bracket closure, rank12, exact E67 projection and 288 central-layer correction words; about six seconds.
3. `structure.py`: both graph inclusions, its actual derived subgroup and E67 abelianization, whole-F-prime Gaussian image and the exact central frame equation; less than one second.
4. `joint.py`: the accepted E68 Schreier and word certificates, six generic preimages, three exact central commutators, all3456 common-word preimages and their original twelve-group replay; about six seconds.

The manifest gives the minimal import closure (twelve Python modules including the four new programs) and every fixed data dependency. Python3 and NumPy suffice. No new compilation, group-order search or GAP run occurs. The accepted E67/E68 programs and data are read only.

Run `python code/bc_gaussian_heisenberg_replay.py --directory /absolute/fresh/directory` for a complete isolated replay. This copies exactly the hashed code/data files, executes the four programs sequentially, compares every mathematical JSON field and every named NPZ array, and verifies all protected original hashes before and after. It refuses to reuse an existing replay directory.

## Provenance rule

Only top-level elapsed time varies mathematically trivially. Later JSON files hash earlier generated JSON bytes, so those input hashes can also differ after an independent run. The replay driver checks each original recorded hash against its original file and each replay recorded hash against the actual replay input before excluding the provenance dictionary from the mathematical comparison. Source hashes and all other mathematical fields are compared exactly. No group value, target, word, array or field is omitted.

## Exact retained scope

The source image is `C3^3 × Heis3^3`, of order3^12, and the displayed map to E67 is exactly its abelianization. E68 then proves the common E66 quotient is trivial. The 3456 count concerns correction-image targets in the actual E17 fibres, with full word fibres given by the joint kernel cosets. It does not assert a full-GT lift or generation of an uncomputed larger source. The Mordell group remains the order54 quotient of E67.

The initial exploratory files are preserved under `research/E69_initial_gaussian/`. The only model cleanup removed a redundant empty loop; the group law and all checks are unchanged. The standalone proof compiled to three pages, all viewed individually, without warnings or overfull boxes. The two initial environment failures (default TeX format/search path) are preserved; the successful build uses the existing explicit project TeX environment and format.
