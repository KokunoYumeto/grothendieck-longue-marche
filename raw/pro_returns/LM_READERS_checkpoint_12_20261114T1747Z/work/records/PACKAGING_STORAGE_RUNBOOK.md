# Exact checkpoint recovery and ordinary final-record storage

## Immutable checkpoint08

Checkpoint08 remains unchanged. Its archive SHA256 is `c950e729accf62b50423e99f5a7f74c91c38add908ae436d7d40dee4ff07a81d`. The original recovery helper and descriptor inside that ZIP define its recovery process. Its independent full restoration verified14,250logical files,2,832PNGrecipes and complete coverage of14,243checkpoint07members. Later helper revisions do not replace that historical proof or its save receipt.

The current helper also accepts checkpoint08's original schema. The separate read-only compatibility check does not claim a second visual review or replace the original full restoration.

## Subsequent compact checkpoints

Wait until the seven publication PDFs are stable and the required current verification ledgers have been written. A finished-reader checkpoint also requires that reader's strict gates to pass.

```text
python work/scripts/package_release.py checkpoint --compact --source-checkpoint deliverables/LM_READERS_checkpoint_08.zip --part DESCRIPTION --finished-reader BOOK
```

The next immutable number is allocated automatically. Never reuse an existing checkpoint filename. After the next checkpoint exists, use that newer compact checkpoint as the following source.

Compact collection includes current selected-page PNG logical paths. An image becomes a recipe only when its attributed reviewed row, native900px PNG bytes, decoded dimensioned RGB, dimensions, page and exact PDF bytes agree. Unqualified images remain full payloads. Inherited recipes retain older immutable PDF, review-ledger and source-trace bytes under `work/data/checkpoint_recovery_inputs/`. Each inherited recipe is freshly rendered and compared before omission; a rebuilt `work/build/BOOK.pdf` never substitutes for its older pinned PDF object. Earlier compact control files are kept under `work/data/checkpoint_history/`.

The prior-coverage table accounts for the preceding compact logical files and its eight container-control files. Exact preservation and same-path supersession are distinct. The new archive recovers independently of the preceding archive. It is measured before creation, must fit536,870,912bytes, and must match the exact predicted size after writing. A size failure stops creation; it never silently removes additional evidence.

After creation, perform a complete independent restoration in a new directory using the helper embedded in the new archive:

```text
python restore_checkpoint.py CHECKPOINT.zip --output-dir restored_checkpoint --verify --report restore_validation.json
```

The helper refuses differing existing files and symlinked or escaping paths, renders all recipes before writing logical destinations, and rehashes every recovered file. Retain its actual full restore report and archive hash before recording a durable save receipt.

## Final ordinary ZIPs

The final deliverables remain `LM_READERS_FR.zip`, `LM_READERS_EN.zip` and `LM_READERS_RECORDS.zip`. Only the seven publication PDFs belong to the final set. Earlier recovery-input PDFs are mapped to their exact final publication replacement and are not extra finished books.

When the current PDFs and source traces are stable, the read-only size plan is:

```text
python work/scripts/package_release.py final-size
```

This reports the proposed ordinary collection and its compressed sizes. It does not write archives or visual-review claims. The final command still requires the complete strict release report and current privacy/source/PDF gates, adds file-by-file checkpoint retention, then measures every complete ZIP again.

The ordinary records policy applies these rules:

1. Reports, scripts, active audit data, actual observations and their hashes remain present. Active imports and audit-data paths remain physical files.
2. Exact duplicate payloads may be stored once. `FILE_ALIASES.tsv` lists every omitted duplicate path, canonical physical path, byte count and SHA256. `IMAGE_ALIASES.tsv` is its PNG subset. The safe alias helper reconstructs those paths and verifies their bytes.
3. A full-page PNG may be deliberately omitted only after exact reviewed-raster qualification and source mapping to the final book. Its path, bytes, SHA256, classification, original reviewed row, retained ledger, original source trace, final publication hash and current source pages are retained in `FULL_PAGE_RASTER_OMISSIONS.tsv` and `FULL_PAGE_RASTER_QUALIFICATIONS.json`.
4. Any content hash used in either curated proof namespace is protected from raster omission. Native proof bytes remain stored, although exact duplicates can use aliases.
5. Historical full pages are labelled as superseded. They are never represented as images of a changed final PDF. Their immutable compact checkpoints preserve exact historical recovery. Current full-page omissions have exact recipes for the retained current PDF.

After extracting the records ZIP into its own directory, restore aliases there:

```text
python work/scripts/restore_file_aliases.py --root . --report alias_restore_validation.json
```

This helper restores exact aliases only. It does not manufacture omitted historical images or relabel observations. `FINAL_RECORDS_LOGICAL_MANIFEST.tsv` records every collected path as stored, aliased or explicitly omitted. `CHECKPOINT_RETENTION.tsv` identifies an exact final target and reason for every earlier checkpoint path, including older recovery-input PDFs. The ordinary `MANIFEST.tsv` inventories physical ZIP files.

## Bounded validation

`work/scripts/check_packaging_storage.py` uses temporary synthetic PDFs and explicitly synthetic review rows. It checks exact ZIP sizing, compact-prior inheritance, recovery without any prior ZIP, protected proof hashes, qualified raster disposition, alias reconstruction and overwrite/path refusals. `work/data/packaging_storage_controls.json` records its result and code hashes. These controls do not substitute for a full restoration of the actual next checkpoint or for actual publication-page inspection.
