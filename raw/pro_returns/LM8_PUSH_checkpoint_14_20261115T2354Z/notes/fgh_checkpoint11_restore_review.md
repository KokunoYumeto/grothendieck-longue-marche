# Checkpoint11 restoration and self-containment audit

**Result: PASS for the inspected storage design, with no release blocker found.**

Auditor: FGH; completed 2026-11-15T20:47:48.381075+00:00. This is a dependency/order and exact-record audit, not a new mathematical proof audit. The final checkpoint11 storage plan was not yet present when this review began; the inspected proposed replacement is `checkpoint11_replay/pbc_v5_replay_transform.json`.

## Scope checked

I read the complete current packager/generated restore script, the complete trace replay helper, the complete legacy prefix helper, the old checkpoint10 plan's non-PNG transformations and prefix/wrapper entries, and the full pending v5 recipe/transform. I checked the shared QA restoration helper and all its referenced PDFs for late-deduplication dependencies.

1. **Prefix ordering is correct.** All transforms finish before either legacy prefix is reconstructed. The v1 prefix consumes the restored boundary trace, and v4 consumes the restored v5 trace. The current optional `restore_command` branch formats archive/destination/target paths correctly and still performs decoded-byte verification when supplied. The legacy helper independently verifies the complete prefix length/hash and the next partial-record prefix.
2. **The v5 replacement is self-contained.** Its original compressed identity and decoded identity exactly match the checkpoint10 transform. The retained leaf payload, DAT, replay C++ source, executable, and sole local header all exist and match their recorded SHA256 values. The leaf payload is explicitly listed as an additional archive payload. The restore helper uses archive-relative paths; the old absolute capture/command paths in the recipe are provenance only. A missing/nonexecutable archived binary triggers compilation from the included source/header, with ordinary system dependencies C++17, GMP and zlib.
3. **No early dependency is deferred to duplicate restoration.** Every PDF used by `qa/reconstruction_manifest.json` is a literal retained file, and so is the v5 DAT. Thus restoration of QA PNGs or v5 proof records does not depend on the final exact-file-copy loop.
4. **Interrupted records remain accounted for.** Both separately retained partial-record files exist and match their recorded hashes. Original incomplete gzip wrapper bytes are explicitly superseded; the promised recoverable object is the complete decoded record stream plus the separate partial record, not the historical compressor's byte stream. C31 stays Open.
5. **The plan must be refreshed consistently.** Checkpoint11 must replace the old v5 binary transform with the verified replay transform and update the shared QA-manifest hash for every inherited PNG transform, as well as new PNG entries. Stale hashes cause the packager to stop rather than silently accept different bytes. I notified root of this integration requirement.

## Independent executed checks

- Decoded the entire retained v5 leaf payload: **84,109,186 bytes**, SHA256 `24accdd2d3cdb4a989e0e3838e4860c368ef9d2af7e27e6b99c987114f4732a7`, PASS.
- Reconstructed the complete v4 prefix from the current captured v5 source in a fresh target: **959,651 records / 76,192,487 bytes**, SHA256 `0acf3436e6ed2067c89c7655c66ab2d57328780358c20d4ba38569ff5e1479a7`, PASS; the following 48-byte partial record also matched.
- Independently hashed the v5 DAT, replay source/executable/header and encoded leaf payload against the recipe, all PASS.
- The full 1,695,013,300-byte v5 operation stream was previously replayed and compared by PBC; I read that recorded verification and checked its identities, but did not repeat the roughly six-minute replay in this deadline-limited audit.

## Operational qualifications

Restore into a clean destination. Existing targets are skipped without hash verification; this is safe for non-overwriting behavior but is not a repair/resume verifier for a corrupt pre-existing file. Ordinary files stay in the extracted archive when `--destination` points elsewhere; that option relocates reconstructed files, not the entire package. PNG reconstruction requires the recorded PyMuPDF 1.26.6 renderer for byte identity, and the helper explicitly rejects a renderer mismatch in the resulting bytes. These are documented tooling constraints, not missing research payloads.

No canonical source or registered metadata was changed for this audit.

## Reviewed file identities

- `code/package_compact_checkpoint.py` — `545a663cd8575c1fbc510f2515001a11930659274786d770efb1ac24b2482fd8`
- `code/pbc_restore_trace_replay.py` — `4241378df6f4bd32046acd855843126d57abc7a4b7e5f95093f17b93875f43b6`
- `code/pbc_trace_reconstruction.py` — `85453ab5f47d458e1e32dd1a2b168818e6eac88ea7c79d243cdde0d900b3864e`
- `code/pbc_v5_replay_recipe.json` — `c112eb60f032fde829c3d59c9a9eecef22b65ff1f4ae8ca0663720575f8a133d`
- `code/pbc_compact_trace_reconstruction.json` — `b1381488b562368ef00df445b585ad3718be827e6f99ab37a92a0bb9a48e3899`
- `notes/checkpoint10_storage_plan.json` — `4575809d49667547beca51b23026e41f1fdcc71a12f971cbe5f47662672a3ec5`

## Final assembled-plan addendum (20:49 UTC)

I subsequently inspected the complete `code/prepare_checkpoint11_storage.py` and the assembled `notes/checkpoint11_storage_plan.json`, SHA256 `76e5404529408c90f4509425738a7372c60bcca271be4ae4c4201be1387842f4`. It contains 283 transforms (three exact replays, six binary traces, 274 PNGs) and three prefix reconstructions. Every PNG transform uses the current shared manifest hash; the old v5 entry is replaced, and v4 points to the new recipe.

The additional smallmod-v2 replay has its source DAT, source, executable and sole local header present with matching recorded hashes. Its leaf payload is explicitly included. The smallmod-v1 portable prefix helper and recipe are ordinary retained archive files; I read the helper completely. It consumes the restored v2 source under the chosen destination and verifies exact decoded length, newline count, final newline and SHA256. The current generated prefix branch dispatches this command correctly and then independently checks the gzip-decoded target again. No external capture path is required. The builder checks all encoded payload hashes and rejects duplicate original paths.

**Final assembled-plan verdict: PASS; no reconstruction/self-containment blocker found.** Existing clean-destination and system-library qualifications above remain applicable. No further broad restoration run is needed for this structural audit; the full v2 and v1 byte-comparison runs are recorded separately by their owners.
