# Scan 008 crop-metadata recovery history

Updated 2026-11-20 16:42:18 UTC. Root reviewed the successful exact replay and explicitly accepted its coordinates and reproducing rotation. This is numerical image-geometry provenance only; no OCR, image display, new reading crop, semantic reading, audit event, or transcription change was made.

## Accepted result

`008_slanted.jpg` is reproduced exactly from source box **(980,950,1240,1155)**, with **rotation −34 degrees** and no mirroring, using the recorded crop pipeline. The original box is 260 × 205 pixels; its expanded rotation canvas is 332 × 317, then resized to 2400 × 2292.

- Existing crop and replay JPEG SHA-256: `20147642b901c8f08f8981f39469d965a2cdbebf06378bc1e77469a42f0f7b98`.
- Source SHA-256: `4b56f6736ada508943f8379c0a74365d5e5ff9eed14b8c4f7b08326ee8c501ba`.
- Eighteen SIFT/RANSAC models each had 64–100 inliers, with source-pixel RMSE 0.47–0.64; their rotation estimates agreed near −34 degrees.
- All **200** nearby integer boxes compatible with the bounded geometric search and exact saved output dimensions were replayed. **Exactly one** produced identical JPEG bytes; decoded-pixel RMSE was **0.0**. The next-ranked box did not match.
- `crop008_exact_replay.md` records the search bounds and the distinction between an exactly reproducing rotation and the unavailable original shell command's spelling. Root approved this verification as sufficient and requested no further matching.

## Earlier searches: historical and superseded

| Record or method | Result at the time | Current status |
|---|---|---|
| Per-page scan-008 records, `scripts/read008.py`, `scripts/audit008.py`, changes/doubts/notes/progress text, prior audit and consolidated registers | The crop's existence was recorded, but its source box and rotation were absent. | Historical documentation gap, now resolved by exact replay. |
| Direct `crop_register.tsv` argument ledger | Starts at scan024; no scan008 invocation. The early crop helper printed only the saved path. | No original command recovered; exact output reproduction supplies the accepted geometry. |
| Text members of checkpoint01, checkpoint02, and checkpoint03 | No lost scan008 crop-creation command found; checkpoint03 preserves the then-unresolved exception. | Historical snapshots retained unchanged. |
| Available local execution-history records and narrowly scoped Personal Context lookup | No local command history was available; Personal Context returned unavailable for this conversation. The crop has no filesystem extended attributes. | Textual provenance search exhausted within the available records. No claim that the original command itself was recovered. |
| `support/recovered_008_slanted.tsv`: unrotated normalized cross-correlation | Best score 0.7876389112; rejected. | **Superseded by exact replay. All earlier candidate boxes remain rejected.** |
| `support/recovered_008_slanted_rotated.tsv`: ROI-limited angle/scale normalized cross-correlation | Best NCC 0.8726215329807248 at 43 degrees; all 20 retained rows say `geometry not reached`. Exact JPEG/pixel verification was never reached. | **Superseded by exact replay. All earlier candidate boxes remain rejected.** |
| SIFT descriptors, ratio matching, RANSAC similarity/affine registration | Concrete method not tried by the two earlier correlation helpers; yielded consistent location, angle, and scale. | Supplied geometry for the successful exact replay. |

The raw failed-search TSVs are preserved unchanged as historical numerical reports. Their current superseded status is recorded here rather than rewriting their candidate data:

- `support/recovered_008_slanted.tsv` SHA-256 `dc68fa01839378de5b78ce5599890a8cc416199a298ed9e2fac851d3e49e60c8`.
- `support/recovered_008_slanted_rotated.tsv` SHA-256 `1456f764eb657ffc8dea7d468a3f699b2ba4bee77d35597121feb5d1ec5ffc04`.

## Reproduction

The two recovery scripts save TSV/Markdown metadata only; they never save or display images. The feature script requires OpenCV, NumPy, and Pillow; the replay script requires NumPy and Pillow. OpenCV was installed into isolated scratch dependencies, which are not part of the deliverable.

```sh
python output/scripts/recover_crop_registration.py source/SP59_CW_71_scans/J71-01_71_scan008.jpg crops/008_slanted.jpg --prefix output/metadata/crop008_feature_registration
python output/scripts/verify_crop_registration.py source/SP59_CW_71_scans/J71-01_71_scan008.jpg crops/008_slanted.jpg --registration-prefix output/metadata/crop008_feature_registration --prefix output/metadata/crop008_exact_replay --angles -34
```

The former row in `crop_unrecovered.tsv` asserted that coordinates and rotation were unrecovered and warned against both rejected correlation reports. That row is now retired; `crop_confirmations.tsv` records root's explicit acceptance of the unique byte-identical replay. Historical unknown-status statements in the initial completeness review are superseded by its dated supplemental update.
