# E.67 authoritative replay guide

The four authoritative programs and all current outputs are listed, with SHA256 values, in `E67_authoritative_manifest.json`. The statement is `sections/E_orbifold_CM_agent.tex`.

## Minimal isolated input set

Copy the four programs sharing `code/bc_orbifold_CM_` with suffixes `characters.py`, `six.py`, `linear.py`, `export.py`, together with these three read-only dependencies:

- `code/bc_hyperelliptic_sewing.py` (imported word and matrix functions; its main is not run).
- `code/bc_cm_literal_words.json` (the original 97 N_B words and original E.1 representatives).
- `code/de_ferrari_fibres.json` (the distinct E.17 representatives used by E.62/E.66).

Python 3 and NumPy suffice. No compiled group program or GAP invocation is used in these four scripts.

## Dependency order

1. `python bc_orbifold_CM_characters.py`: approximately 1 second. Exact two quotient maps, universal Mordell sign, four Gaussian finite actions, literal single-pair correction preimages and retained original-word failures.
2. `python bc_orbifold_CM_six.py`: approximately 83 seconds. All 4656 commutators and all 97 conjugations; exact rank-nine source; literal original-E1 corrections; complete finite norm fibres.
3. `python bc_orbifold_CM_linear.py`: under 1 second. Both inclusions for the displayed product-space formula, zero Mordell homogeneous norm kernel, and exact Gaussian whole-F-prime comparison.
4. `python bc_orbifold_CM_export.py`: approximately 203 seconds. All literal right-action permutations, all 97 generator replays, both independently evaluated origin families and their complete four-target fibres. Produces the reusable NPZ.

Each script writes its output beside its own source, so the isolated copy should contain a writable code directory. Redirect stdout to its corresponding `.out` file if desired. All literal word witnesses are replayed, including their unchanged values in the other specified factors.

## Comparison rules

Compare every mathematical JSON field and every named NPZ array exactly. The `seconds` fields vary. The linear/export provenance includes the byte hash of the newly generated six-output JSON, whose elapsed-time field varies; verify those recorded hashes against the actual isolated input bytes, then compare the underlying mathematical data. The source hashes and all fixed input hashes must match the manifest. This is the same explicit provenance treatment used in prior independent project replays; no mathematical field is dropped.

The original E.1 and E.17 origin arrays must remain separate. No G6-lineage assertion connects their correction vectors. The exported convention is `p(gh)=p(h)[p(g)]`, with affine right action `t -> A^{-1}(t-v)`. Before joining another source, compare the 97 literal words letterwise on that source, and evaluate its actual origin words again.

## Scope and retained attempts

The complete correction image is M × G with dimensions 3 and 6. There are four norm-compatible finite evaluation vectors per origin in each list. Actual profinite word fibres are the stated cosets of the full evaluation kernel; the four-point count is a count of images. The two-factor target has the actual order-1944 generating map. No larger joint-source generation, K3/E6 common quotient, or full-GT lift is inferred.

The initial fixed-word probe and the first six-evaluation run are preserved under `BC_orbifold_initial_probe/` and `BC_orbifold_six_initial_probe/`. The latter retained all Mordell values; the final run additionally corrects the original Mordell three-cycle failures and records both tests. The six program no longer contains the initial redundant basis-word assertion; its complete final basis replays remain unchanged in purpose.
