# Exact-evidence carry for the canonical pagination and generated-heading audits

## Purpose and limits

`work/scripts/carry_canonical_audit.py` transfers an existing, attributed actual observation from the completed `revision578_final_discovery` snapshot only when its precise source or witness identity and every cited image remain unchanged. It does not inspect images, create an actual-view observation, modify a queue, or issue publication approval.

The helper is separate from `carry_native_closure.py`. Native finding closure retains its own source-local inspection and rendering requirements. Master editions also retain their independent complete, current apparatus/master pixel comparisons; this helper excludes master candidates.

## Required order

1. Preserve the completed discovery snapshot at `work/data/audit_history/revision578_final_discovery/SNAPSHOT_COMPLETE.json` before rebuilding. Its canonical queues, original actual observation files, and preserved image references are the historical inputs.
2. Finish the new publication build and declare its PDFs stable.
3. Run `verify_pagination_final.py prepare` and `verify_generated_heading_final.py prepare` for the new build. Carry must use those newly prepared queues and their registered evidence.
4. Run the carry helper into **new output and report paths**. Existing paths are never overwritten. Use either the complete canonical queue or one of its hash-bound per-book queues.
5. Actually inspect every item listed in the carry report's `pending` array. Do not fabricate a current observation from a source patch, an old page number, or similar-looking text.
6. Supply the carry output and the separately recorded actual pending-item observations to the corresponding canonical finalizer. Supply each item exactly once. Do not include the old revision578 observation files as current observations.
7. Complete the independent master comparisons and all other publication gates. A carry report, even with zero pending primary items, is not a release PASS.

## Example commands

These destinations are examples for a new carry attempt. Choose unused names if they already exist.

```bash
python work/scripts/carry_canonical_audit.py \
  --snapshot work/data/audit_history/revision578_final_discovery/SNAPSHOT_COMPLETE.json \
  --queue work/data/pagination_verification_queue.json \
  --kind pagination \
  --output work/data/canonical_carry_next/pagination_observations.json \
  --report work/data/canonical_carry_next/pagination_report.json

python work/scripts/carry_canonical_audit.py \
  --snapshot work/data/audit_history/revision578_final_discovery/SNAPSHOT_COMPLETE.json \
  --queue work/data/generated_heading_verification_queue.json \
  --kind generated-heading \
  --output work/data/canonical_carry_next/generated_heading_observations.json \
  --report work/data/canonical_carry_next/generated_heading_report.json
```

For a per-book attempt, replace `--queue` with the freshly prepared file under `work/data/pagination_final_queues/` or `work/data/generated_heading_final_queues/`. The helper verifies that its items exactly match the cited current canonical queue. Give each per-book attempt separate new output/report paths.

The output object has an `observations` list, which both existing canonical observation loaders accept. It intentionally is not written over the existing `*_final_*observations.json` files. The parent workflow may use it explicitly as an additional finalizer input or perform a separately verified, duplicate-free merge.

## Carry conditions

Every transferred item must satisfy all of these conditions:

- It has the same exact item ID, reader, and audit role as its frozen predecessor. There is no cross-reader, cross-ID, nearby-page, or fuzzy-text matching.
- A known pagination item has the identical immutable source record, unique exact binding identity, associated display source, and applied old/new hashes. A known generated heading has the identical immutable source-qualified historical witness and first-entry anchor or scan range.
- A fresh scanner candidate has the exact same source-anchored boundary witness, including its ID, page, bounding box, scan contexts, and extracted surrounding content. A moved or ambiguously identified candidate remains pending.
- The historical observation already has the precise permitted status for that role: `RESOLVED_ON_FINAL_PDF` for a known witness or `CLEARED_ON_FINAL_PDF` for a fresh candidate. Defect, open, detached, failed, unresolved, or pending observations are never promoted to clearance. Contradictory structured defect flags also prevent carry.
- Every historical cited image is registered in its historical item and frozen in the snapshot. It has exactly one match among the current item's registered evidence. The PNG bytes and decoded RGB dimensions/pixels must both be identical. Re-encoded PNGs with identical pixels still fail the byte-identity condition.
- Image page-role metadata provides a consistent, injective mapping for every structured observed page. No observed display, title, separator, or content page may be inferred from an unviewed image.
- Both the historical observation, rebased only to preserved image paths, and the proposed current observation pass the existing canonical `check_observation` validator. The helper additionally checks actual current PDF hashes/page counts and valid physical page numbers. The narrow fully-cancelled-display retained-tag classification still requires its existing exact-source validator.
- All files read for the decision retain their hashes until the output is written.

Any failed or uncertain per-item condition produces a pending reason. An invalid input envelope, stale current PDF, tampered frozen record, duplicated historical observation, or attempt to overwrite an existing output rejects the run. No existing input file is changed.

## Provenance and attribution

The transferred observation retains its original `reviewer`, `observation`, and successful status byte-for-byte as JSON strings. Its structured page fields, PDF hash, and image references are mapped only to current registered evidence. The original note is not rewritten to substitute new page numbers.

`exact_canonical_image_carry` records the snapshot and queue hashes, frozen original observation file, complete original actual observation, source/witness identity and digest, old/current page mapping, and each PNG/RGB identity proof. Its basis explicitly says that no new visual observation was made and that page numbers inside the preserved prose refer to the historical PDF.

The report lists carried IDs, all pending reasons, and excluded master IDs. Its status is `COMPLETE_CARRY_ATTEMPT_NOT_RELEASE_APPROVAL`.

## Targeted synthetic controls

```bash
python work/scripts/check_canonical_carry.py \
  --output work/data/canonical_carry_controls_second_run.json
```

The controls create and remove temporary synthetic PDFs, sources, snapshots, queues, and images. They never use a synthetic observation as publication evidence. The completed first run is recorded in `work/data/canonical_carry_controls.json` and binds the helper/test script hashes.

The30 controls cover successful transfers for both audits, fresh-candidate and per-book membership checks, preservation of the original reviewer/note, mapped page fields, no-overwrite behavior, same RGB with different PNG bytes, changed pixels, duplicate image matches, a changed second cited image, cross-reader rejection, changed binding/source/anchor/context, missing or ambiguous localization, missing frozen evidence, invalid/out-of-range pages, a retained-tag claim without source proof, explicit OPEN flags and defect statuses, stale current PDFs, tampered snapshot records, and unchanged input files.
