# E66: exact distribution overlap and complete common-word replay

Proof: `sections/E_distribution_overlap_agent.tex`.

The 24 origins in this batch are the indexed E17 words in
`code/de_ferrari_fibres.json`, which represent the E1 CM pairs and are
retained by E62. No correction is transferred from the distinct
original E1 word list. The previously reviewed source is preserved as
`E66_initial_reviewed_draft.tex`; its only later mathematical-text
change is this exact origin citation.

Root read the complete proof and all new mathematical programs.
Geometry's independent full proof/program review is recorded in
`BC_E66_independent_audit.md`, with the reviewed source and program
hashes. The authoritative manifest protects the final source, inputs,
outputs, complete certificates, replay driver, prior draft and review.

The cyclic-three portion is already frozen in
`A_K3_authoritative_manifest.json`; its compact isolated replay is
documented in `A_K3_REPLAY.md`. Root independently replayed all five
complete K3 certificates and their mathematical outputs. Those inputs
and outputs are unchanged by this batch.

The new E6/E62 portion has this isolated entrypoint, run from LM7_PUSH:

```sh
python code/a_cm_distribution_replay.py --destination research/root_E66_distribution_replay
```

Use a fresh destination. Requirements: Python with NumPy and a C++17
compiler. The driver copies only the listed source/matrix/word inputs
and the frozen E62 PC prefix certificates into its fresh directory. It
compiles the existing complete Schreier verifier, then runs:

1. `a_cm_distribution_e62.py`: the actual 5223-point common N_B source,
   its derived image, its 4849-point projection to E62 and five E6
   coordinates, and every finite final-fibre membership.
2. `a_cm_distribution_overlap.py`: the literal index-two common
   characters, all basis products and all common strong generators.
3. `a_cm_distribution_witnesses.py`: all 288 successful memberships
   lifted through both actual word DAGs and replayed in the full source.

It compares every mathematical JSON field, every NPZ array and every
literal array in the four complete certificates. Runtime fields are
the only excluded JSON fields. Original hashes are verified before
and after. The earlier E62 inputs are never rewritten and no legacy
main program is run.

The exact binary overlap is mask175728 on E62's zero-based PC bits and
the modulo-four lower-left entry divided by two in the N=3 distribution
coordinate. All 96 E62 final values survive, each with exactly three
multiplicative coefficient tuples. These are common-word finite
identities; no generation in the new distribution refinement and no
full-GT lift is asserted.
