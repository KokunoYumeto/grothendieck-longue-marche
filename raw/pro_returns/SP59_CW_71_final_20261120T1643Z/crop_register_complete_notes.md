# Crop register provenance

Generated 2026-11-20 16:43:36 UTC from text metadata only.

- 236 distinct documented original-image boxes.
- 236 tight-crop register rows; 0 with unrecovered coordinates.
- 6 supplied-half transformations, listed separately.
- 3 rotations of an existing crop, listed as derivative aliases, not additional boxes.
- 0 coordinate/name/transformation conflicts or association gaps.
- 0 documented crop rows are not yet cited by box in the current changes.md.

Coordinates are copied as exact tuples from the root reader's per-page records and changes log, the older audit register, direct crop.py argument records, or explicit root confirmations. This consolidation reads text metadata and filenames only. Separately authorized numerical geometry recovery is documented in its own provenance reports. The existing complete register is retained as an additional source on later runs so previously documented tuples cannot disappear silently.

Filename association is separate from coordinate provenance. Legacy associations match descriptive filenames to documented places; they are labelled accordingly and are not asserted to be recovered shell commands. Direct argument-ledger entries and root-confirmed numerical recoveries are distinguished in name_association_basis.

Empty rotation or mirror fields mean that transformation was not explicitly recorded; they do not assert zero rotation or absence of mirroring. The three mirrored scan-024 strips are supplied by an explicit record. The current crop.py ledger has no mirror column, so its rotation records alone do not settle mirroring.

The two failed scan-008 correlation searches remain historical and their rejected candidate coordinates are excluded. The later SIFT/RANSAC registration and unique byte-identical pipeline replay recovered (980,950,1240,1155), with reproducing rotation -34 degrees; root explicitly accepted this provenance. See metadata/crop008_recovery_history.md and metadata/crop008_exact_replay.md. No new image reading or transcription change was made.

## Unrecovered tight crops

None.

## Recorded boxes not currently in changes.md

None.

## Regeneration

Run `python output/scripts/consolidate_crop_metadata.py` after further pages are recorded. Add `--append-changes` to update only the marked metadata table in CHANGES_EXTRA.md while preserving all other prose. Run records.py build to incorporate that appendix in changes.md. The consolidator reads text files and image filenames only, writes metadata files, and never modifies pages, readings, per-page records, or audit events.
