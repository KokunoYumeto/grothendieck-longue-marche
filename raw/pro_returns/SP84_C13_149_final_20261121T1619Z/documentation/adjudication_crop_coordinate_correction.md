# Adjudication evidence-coordinate correction

2026-11-21 16:01:13 UTC

The main reader approved this metadata-only correction after the read-only checklist identified a mismatch.

- Record: `second/149_scan017_adjudications.tsv`, b11.
- Evidence image: `crops/149_scan017_audit_b11_full.png`.
- Historical incorrect evidence rectangle: `(1070,1892,1633,2056)` (the original neutral box).
- Current correct evidence rectangle: `(1325,1850,1640,2000)`, from `documentation/audit_scope_crops.tsv` and the current c09 report.

Only the coordinate string changed in the adjudication TSV. All reading fields, evidence prose, flags, page text, report counts, neutral box coordinates, first/second readings and comparison inputs remain unchanged. The log preserves both values and file hashes. No aggregate assembly was run.

The helper now accepts an explicit `pixel_box` choice and checks it against known manifests. The read-only validator uses direct original-coordinate manifests, recorded supplements and explicit full-extent derivation links; it does not infer coordinates from file names. Rotation-only evidence retains the original source rectangle. All existing crop overrides were checked; their exact comparisons are in the JSON log.

## Focused validation checks

Five isolated metadata fixtures passed in scripts/test_crop_coordinate_metadata.py: stale default rejection, explicit supplement acceptance, invalid override rejection, explicit same-extent derivation, and conflicting-manifest rejection. All fixture comparison inputs remained unchanged. No actual image was opened. The real validator also rejected the original017 mismatch before correction and passed afterward with327 evidence rectangles verified and no unmapped evidence crop.
