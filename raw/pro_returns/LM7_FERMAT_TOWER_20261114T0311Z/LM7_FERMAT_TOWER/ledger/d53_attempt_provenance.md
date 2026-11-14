# D.53 execution provenance

The three source programs and their companion stdout/JSON files were executed in `D53_EXPERIMENTS/code`. The graph program is a new exact reconstruction of the actual Q graph. The same-action obstruction program reconstructs the separate order1080 graph and consumes the immutable D52 coefficients. The full-word program is the D52 class-two construction adapted to a prescribed same-action parameter; it writes the new basename `d_cm_same_action_word`, and does not overwrite the frozen D52 input.

The final source/input copies were independently executed by the author in `author_fresh_run`; `verify_author.json` records exit codes, full certificate equality after removing only elapsed time, and TeX lint. These are author reproduction checks, not the separately requested parent or peer audits. No failed D53 execution or omitted attempted source is claimed.

Frozen input provenance:

- `code/d_cm_full_class2_search.json`: frozen D52 output, used as coefficient data only.
- `code/d_cm_symplectic_search.json`: frozen D52 pairing-preserving parameter and action.
- `code/d_class2_diagnostic.json`: frozen D51 intersection and class-two diagnostic data.
