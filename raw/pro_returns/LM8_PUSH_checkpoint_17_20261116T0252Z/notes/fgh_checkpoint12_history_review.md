# Checkpoint 12 history and restoration audit

Status: PASS after the targeted resumed-root metadata fix. Reviewed 2026-11-15 before the 21:40 source freeze. No archive was created by this audit.

## Scope and evidence

I read all four complete scripts: `prepare_final_history.py`, `materialize_checkpoint_history.py`, `restore_checkpoint_history.py`, and `package_compact_checkpoint.py`, including the new current-file-first and external-payload deduplication branches. The materialized index covers checkpoints 01–11: 8,391 historical entries, 1,761 content-addressed objects, 169 exact current restoration dependencies and three individually documented superseded compression encodings. The independent structural check is `notes/fgh_checkpoint12_history_check.json`.

Every snapshot entry has one unique destination. Every object and exact-current reference has matching size/hash metadata, and none of the three decoded replacement destinations collides with an exact historical entry. The historical accounting filename is unused by all original snapshots. I inspected the actual successful restoration logs: checkpoint 09 restored 1,469 exact entries plus two explicitly recorded decoded replacements; checkpoint 11 restored all 1,657 entries exactly. Those complete restoration runs were performed by root, not rerun or claimed as my own execution.

## Inventory and reconstruction

The inventory includes old ZIP metadata as actual historical entries, including entries absent from the old manifest's own list. Materialization verifies each source archive hash and every entry's exact bytes and SHA-256 before accepting a content-addressed object or a current exact dependency. The three omitted encodings are not described as byte-identical old wrappers: their retained full mathematical payloads or exact decoded prefixes have separate byte counts and SHA-256 values. The old ZIP container itself is explicitly not recreated. This is an honest distinction between exact historical files and the three fully accounted serialization substitutions.

The history restorer refuses an existing destination, confines paths within the selected roots, preflights dependencies, follows outer exact-copy aliases with cycle detection, and verifies every copied file. Superseded encodings restore the original mathematical source path; after that, the original historical restore helper skips that existing source and does not require the omitted encoding. The outer restore must run first when transformed raw dependencies are not yet materialized. This order is documented and sufficient; no outside saved ZIP or absolute original workspace path is needed by the actual historical reconstruction.

## Deduplication and the fix

Ordinary operational files are considered before history objects. Every history object is eligible for exact-hash deduplication, irrespective of size. The later pass deduplicates only history objects against verified external stored payloads, preserving operational inputs. Alias chains are flattened and cycles rejected; every final alias points to a literal archive entry. The 169 historical exact-current dependencies are rechecked against their original size and hash at every capture.

I checked the actual current PNG reconstruction manifest: each referenced source PDF is its first ordinary exact-hash representative, hence is literal before image reconstruction. The current paper PDF precedes its duplicate build output. The recipe and decoder scripts remain operational literals. The external payload phase cannot silently replace different ordinary bytes at the same path: a new exact-hash assertion rejects that collision.

One real future-resume issue was found and fixed with root authorization. Extracted root `PACKAGE_MANIFEST.json`, `CHECKPOINT_COMPRESSION_MAP.json`, `ORIGINAL_PACKAGE_MANIFEST.json`, or `RESTORE_LARGE_LOGS.py` could previously enter the hash representative table, even though the writer later regenerates those paths. A historical object could then refer to different bytes after packaging. The capture loop now excludes these four generated names before deduplication, records any present resumed copy's old size/hash/reason in `replaced_root_packaging_metadata`, and explicitly accounts the omission. Payload and literal-source assertions reject collisions with these regenerated names. Historical metadata objects remain untouched and exact. None of the four stale root files exists in the current workspace, so the fix does not remove a current mathematical artifact.

I executed the actual patched capture-loop source against a synthetic resumed root. The test confirms that old root metadata is excluded and its hash recorded, its historical exact object remains literal, the operational PDF remains literal, and its historical duplicate aliases the operational PDF. No archive was created. The result is retained in the independent check JSON. All four scripts parse successfully after the patch.

## Limits

This audit establishes reconstruction dependencies and the reviewed actual-input ordering. It does not claim byte-identical recreation of old ZIP wrappers or the three superseded encodings. Final archive CRC, complete manifest verification, and upload-size checks remain the packager/root's capture gates. Future storage plans must continue supplying verified payload hashes; unknown files are not presumed reconstructable.

## Reviewed script hashes

- `prepare_final_history.py`: `227be2fe15e344e97f7a03d20da7fef8212615a1aa13c745797930e58d1f8151`
- `materialize_checkpoint_history.py`: `4f05230849c787d10b418fe6092b9919d41e610fd016071ce64b45f177416fe7`
- `restore_checkpoint_history.py`: `a438370ede354d7eb7de995e8ceb8df46126380ab66231f1174bd538cc5cdef3`
- `package_compact_checkpoint.py`: `4d2da6baed2aa9fee232c34b6c6f27773f61d935f518dcb1729a191963d163bd`
