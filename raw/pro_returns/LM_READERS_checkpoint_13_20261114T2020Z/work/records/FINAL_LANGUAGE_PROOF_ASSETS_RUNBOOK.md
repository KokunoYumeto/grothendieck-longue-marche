# Language-specific proof assets and safe common assembly

## Scope

This is a storage-only addition to the ordinary three-ZIP release. `final_language_proof_assets.py` runs after the existing records policy and before checkpoint retention, privacy, archive-size and exactly-seven-PDF checks. It moves a physical PNG only when its exact hash group has one language attribution across all recorded logical aliases and validated after-proof references. A conflicting French/English attribution, missing attribution, or path outside the explicit proof scopes leaves the file in RECORDS. Reports, scripts and audit data remain there.

Each moved PNG keeps its original relative path, bytes and SHA-256. The original physical payload multiset is preserved. Only the `final_archive` value changes in exact stored/alias rows of the logical manifest. Existing full-page omission rows, alias bytes, source records and actual observations are unchanged. The packaging-generated logical manifest, policy summary and storage instructions are explicitly regenerated; the distribution report records their before/after hashes.

No native proof raster is replaced by a recipe or re-encoded by this helper. `FINAL_PROOF_ASSET_DISTRIBUTION.tsv` records each moved physical file, byte count, SHA-256, archive pair, logical alias paths and language evidence. Its JSON companion records the coverage checks and unchanged seven-PDF placement. A future unexpected logical-disposition schema fails closed.

## Proposed integration

Apply the reviewed changes in `work/layout_probes/final_language_proof_assets_callsite.patch` to the packaging owner’s current script, checking context rather than replacing that script. The three new generated control names must be excluded from fresh collection. Both `final()` and `final_size()` call the distributor immediately after `apply_records_policy`; the existing generated-record write loop then receives the updated records. Retention and final archive manifests naturally resolve each PNG to its new archive.

The separate `final_language_proof_assets_report_wording.patch` proposes the report correction. It removes the earlier claim that both duplicate proof paths are physically present without reconstruction, and states that exact aliases are restored after common assembly. Neither patch has been installed by this task.

A read-only estimate is available with:

```sh
python work/scripts/final_language_proof_assets.py estimate
```

It computes exact deterministic deflate sizes before and after distribution without writing ZIPs or installing generated packaging records. Run it only while the packaging scripts and current collected inputs are stable. Its final figures exclude the later checkpoint-retention, privacy and preflight additions; the existing final size gate must still remeasure all three completed maps. An estimate is not a release-completion claim.

## Assembling delivered archives

Keep the three ordinary archives together. Obtain `work/scripts/assemble_release.py` from the RECORDS archive in a separate tools directory, then run:

```sh
python assemble_release.py --fr LM_READERS_FR.zip --en LM_READERS_EN.zip --records LM_READERS_RECORDS.zip --output assembled_release
```

The destination must not exist and its parent must already exist. `--check-only` validates every archive and the complete alias plan without creating the destination; it also reports uncompressed physical and additional alias bytes.

Before creating the output tree, the standalone, standard-library assembler verifies complete manifest membership, CRCs, sizes and SHA-256 values for all three archives. It rejects unsafe/nonportable paths, symlinks, duplicate ZIP members, different common payloads, case or file/directory collisions, indirect aliases and unknown alias-helper code. It accepts exactly seven publication PDFs in their original language archives.

The assembler extracts into a new private directory, merges only byte-identical common paths, preserves each original manifest under `archive_manifests/`, and writes a combined `MANIFEST.tsv`. It invokes the existing `restore_file_aliases.py` only after checking its audited exact hash. That helper resolves targets across the combined tree and recreates every exact alias, including both historical and project-relative proof paths. It does not reconstruct explicitly omitted full-page rasters. An `ASSEMBLY_VALIDATION.json` report records archive pins and actual restoration counts. No publication or visual observation is regenerated.

The merged manifest inventories physically extracted payloads, the three preserved original manifests and the assembly report. Exact aliases are inventoried separately in the unchanged `FILE_ALIASES.tsv`, so the independent alias helper can be rerun to verify them. Each original archive manifest remains available byte for byte. The assembler never overwrites a pre-existing output directory or user file; it replaces only its own temporary in-progress merged manifest in the newly created tree.

## Focused controls and limits

`work/layout_probes/final_language_assembly_controls_v1.json` records 17 passing synthetic controls, including actual cross-archive alias restoration and independent helper verification. Rejected cases cover conflicting destinations/common paths, changed byte/hash pins, CRC corruption, unsafe paths, case/prefix collisions, symlinks, alias chains/missing targets, untrusted helper bytes and reserved assembly metadata. All control files are synthetic temporary fixtures; no final archive, source proof or observation is changed.

The assembler pins the audited alias helper hash in its own code. An intentional future change to that helper therefore requires a reviewed pin update and rerun of these controls. The archive manifests prove internal integrity, not external authenticity; release ZIP SHA-256 values remain the independent download identity pins. Full page-raster disposition policy and all existing release gates remain separate and unchanged.
