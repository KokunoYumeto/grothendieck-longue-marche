# Native v5 lossless replay audit for checkpoint 11

**PASS.** The entire immutable 19:38 native-v5 capture was regenerated and compared **byte for byte**, not merely by sampling or by checking its final proof node. It contains 20,689,236 records and 1,695,013,300 decoded bytes, SHA256 `58b8deedbdc07df5591b5b2455ee7d59f5a94cf78d01ddaa51bcc509acf68739`. The comparison completed in 349.711 seconds. The old live basis is still paused; checkpoint 10 was not modified. **C.31 remains Open.**

## Retained data and exact reconstruction

Every original source and leaf record is retained verbatim: 24,471 records, including 8,813 identity rows. Their exact lossless `PBC_LEAF01` payload is 6,678,876 bytes, SHA256 `e953ffb87bfe70e8e4b98ae0115e26d3b69de642dcddaa2b34ff1fffde14a5d3`. Its independent decode reproduces the retained raw source/leaf file's complete hash. The original target, extra frame rows, modulus/coordinate rows, original source hash, and all identity metadata and coefficients are retained.

The deterministic reducer regenerates every `sub`, `mul`, and `neg` record with its original integer coefficient and node references. It stops at the exact original record count, including a prefix ending inside a reduction. The recorded prefix ends before the first additional phase-boundary target check; its every-250-identity cadence agrees with the replay. The complete-byte comparison is the acceptance gate, so this observation is not used as an unverified compression assumption.

The original 623,395,620-byte gzip wrapper has SHA256 `3ff34a65c39484e2cee272d997188a528dc0371526c57f5121540de79e105a37`. As in the already audited checkpoint-09/10 codecs, the wrapper is superseded by a new valid gzip serialization, while every decompressed proof byte is preserved exactly and the old wrapper's count/hash remain in the recipe. The original workspace capture and earlier immutable checkpoints remain untouched.

## Arithmetic optimization and independent audit

The replay cache represents dense coefficients modulo `2^146 * 3^30` by three binary limbs and one residue modulo `3^30`. The low 146-bit product contains every required limb term; the middle carry uses 128-bit arithmetic and overflow in the upper limb is harmless modulo `2^18`. The two-limb borrow formula and odd-modulus multiplication use bounded unsigned operations. CRT reconstruction gives the unique representative in `[0,N)`.

Every pivot division and emitted proof quotient still uses the original GMP integer. Initial signed or unreduced entries remain marked dirty until their first coordinate-reducing update, so the optimization does not silently change the quotient in a proof record. Basis caches are rebuilt after every swap. The implementation first passed 10,000 deterministic randomized comparisons against GMP. Root independently audited these arithmetic and cache invariants before the final complete-byte comparison; that audit passed. The full comparison then verified every emitted byte against the immutable capture.

## Self-contained restoration

The accepted recipe is `code/pbc_v5_replay_recipe.json`; the generic packager ledger is `checkpoint11_replay/pbc_v5_replay_transform.json` outside the report tree. Its additional payload is archived as `code/pbc_v5_original_source_lines.leaf.xz`. The restore command uses `code/pbc_restore_trace_replay.py` and the recipe. It verifies and decodes the leaves, reconstructs and checks the identity-input DAT file, runs the included exact reducer, and checks the entire decoded output hash.

The included reducer is `code/pbc_trace_replay_v5_crt.cpp` and its compiled executable. Its only local include is `code/pbc_positive_collector_core.hpp`, whose hash is also retained and checked. Source, executable, original DAT and payload hashes were rechecked after recipe generation. The helper resolves all operational paths relative to the extracted archive; old absolute capture paths are provenance only. It needs Python's standard library and the included Linux executable, or C++17/GMP/zlib to compile the included source if execution permissions or platform require rebuilding. No GAP, network, old workspace or unarchived mathematical input is needed for restoration.

The source generation, complete comparison, leaf-codec logs, recipe, executable/source hashes and final audit data are retained in `code/pbc_build_crt_replay.py`, `code/pbc_build_v5_replay.py`, `code/pbc_verify_v5_replay.py`, `code/pbc_finalize_v5_replay.py`, their output ledgers, and `notes/pbc_checkpoint11_v5_replay_audit.json`. This reduces the v5 stored payload from about 300.9 MB to about 6.7 MB without discarding any proof record.
