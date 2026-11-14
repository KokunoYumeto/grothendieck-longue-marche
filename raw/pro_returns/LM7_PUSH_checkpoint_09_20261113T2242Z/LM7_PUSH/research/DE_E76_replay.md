# E76: complete nonlinear S3/S4 surface-cover replay

The frozen proof is `sections/E_wajnryb_surface_covers_agent.tex`.
The independent proof/code read is
`research/A_Wajnryb_nonlinear_independent_audit.md`.
The complete file inventory and exact hashes are in
`code/de_wajnryb_surface_manifest.json`.

The authoritative successor makes the range `g in {2,3,4}` explicit
in the first sentence. The preceding proof and manifest are preserved
in `research/E76_genus_scope_initial/`; the exact scope note is
`research/DE_E76_scope_addendum.md`. The mathematical programs and all
certificate outputs are unchanged. Both the author's complete replay
(19.521 seconds) and the root complete replay (19.532 seconds) passed
the predecessor batch before this printed domain clarification.

From the project root, use a new destination:

```sh
python code/de_wajnryb_surface_replay.py --destination research/E76_independent_replay
```

The driver copies the complete local Python import closure, the five
explicit old data inputs, every new source/model/fibre certificate, the
proof and the retained initial attempts. It does not execute old legacy
entrypoints. It repeats the ten new programs sequentially in the copied
tree: the free-group/capping model, the S3 models in genera two and three,
their two full induced sources and two complete fibre tests, then the S4
genus-two model, source and fibre test. The total expected runtime is
about twenty seconds on the original machine; timing is not a gate.

Every mathematical JSON field is compared exactly. Only `seconds` and
the input-provenance dictionaries are omitted from this equality.
Before omitting an `input_sha256` dictionary, the driver checks every
entry against the actual original or regenerated file bytes in its
own tree. Bare filenames route explicitly to `code/`; explicit paths
retain their path. Missing paths are failures, with no basename fallback.
Every NPZ array is compared in key, shape, dtype and literal value, and
each exported permutation-group input is compared byte for byte.
The driver retains new stdout/stderr for each step; elapsed-time stdout
is not byte-compared. The final guard checks every protected original
file against its manifest hash. Failures retain the full isolated tree.

## Exact finite maps and exhaustive gates

The free model retains both inverse maps, all Wajnryb relations in
genera two through four, the positive boundary-twist identity, and the
integral homology comparison. Each surface model enumerates every
tuple, tests the literal capped boundary word and epimorphism condition,
and takes the quotient by the entire verified automorphism group.
All original tuple/orbit maps and target permutations are retained.

The induced source uses all six actual B/F cosets and every required
pair `(y_i,a_i^2)`. Its compression is accompanied by all explicit
B-set intertwiners. It checks all 97 N-basis sixth powers and all 4,656
pair commutators. Their identity values prove that this entire source
kills `N' N^6`; this is the actual G6 factorization.

The fibre test checks every one of the 24 literal E17 words and all 37
old/homogeneous correction generators. The source factorization retains
the complete fixed-G6 word fibres, including all 864 E24 points. Every
Wajnryb relation is checked after substitution. Generation is proved by
saved simultaneous point intertwiners, together with the literal
inclusion of the corrected generators in the old target. The S4
certificate retains both point orbits, of sizes 540 and 360.

## Preserved attempts and metadata

The first negative boundary-twist sign guess failed a reduced-word
assertion. Its source and actual logs remain unchanged in
`research/E72_nonlinear_initial_boundary_sign/`. The corrected positive
equality is verified in all three genera in the frozen free model.

The S4 engines were initially generated from the S3 engines. Their
construction record is `code/de_wajnryb_s4_engines_prepare.json`; its
output hashes refer to the retained initial versions in
`research/E74_S4_initial_engine_metadata/`. The driver verifies that
exact historical routing in both trees. The current files explicitly
use S4 metadata, exponent period twelve, and both target orbits. Those
changes preceded the first S4 fibre run. The directory's historical
E74 name is not a statement assignment; the result is E76.

## Scope

This replay proves the stated finite source/fibre results. It preserves
the actual maps from the original B and F groups and the complete old
word fibres. It does not infer a full-GT lift from these finite tests.
The subsequent A5 surface-cover computations use separate files and
are excluded from this frozen batch.
