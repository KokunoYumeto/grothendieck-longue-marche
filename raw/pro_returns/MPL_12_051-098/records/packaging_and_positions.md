# Packaging and inventory-position preparation

No checkpoint or final ZIP was created while preparing these helpers. No transcription, doubts, existing inventory, or progress-log file was changed.

## Checkpoint command

Run `python records/package_bundle.py checkpoint` from the work directory, or `python MPL_12_051-098_work/records/package_bundle.py checkpoint` from its parent. The first scheduled time is **2026-11-17 19:41:17 UTC**, with one scheduled slot per subsequent hour. Early calls or a second call in an already saved slot are refused. A missed slot is not backfilled with several immediate checkpoints.

The helper creates a uniquely numbered `MPL_12_051-098_checkpoint_NN.zip` beside the work directory. It captures all selected work products, scripts, records and logs in one archive. Source/context directories, all image/PDF files, nested archives, bytecode, compiled temporary files and symbolic links are excluded. Additional copied-source paths can be excluded with repeated `--exclude` glob arguments. `--dry-run` reports the selection without creating an archive or changing logs.

The archive includes an exact UTC creation line in its copy of `progress.log`, a schedule-state record and a per-file checksum manifest. After ZIP integrity succeeds, the same creation line and records are committed to the live work tree. Existing archives are never overwritten. The helper detects files that change while snapshot bytes are being collected.

The command prints the ZIP path, hash, size and next scheduled time. **Library persistence is a separate required step** using the authorized create tool and current transfer helper. The local creation record does not claim that upload succeeded.

## Final packaging

Use the same helper with `final`. It requires the frozen-transcription marker and successful complete structural validation, then creates `MPL_12_051-098.zip` with the same source exclusions. It refuses an existing final filename. Freeze-hash verification must still be performed against the saved freeze manifest before calling this command; structural validation alone does not verify a manifest unless one is supplied to that validator separately.

## Physical positions in the candidate inventory

Source order, TeX line numbers and character offsets do **not** establish physical locations on the scanned sheets. The original 640-row inventory remains untouched.

`rebuild_inventory.py` now preserves original physical-region metadata only when the scan and normalized element kind agree and the original and candidate prefixes have a unique match in both directions. Matching is literal: whitespace is normalized and one leading state/visual wrapper may be ignored. No mathematical equivalence, reading correction, positional interpolation or visual inference is used.

The separate `MPL_12_051-098_inventory_candidate_positions.csv` retains **27** safely matched original physical positions. The remaining **543** rows explicitly say `physical position unassigned` and retain their exact TeX source spans. `inventory_position_report.json` records every match and every unassigned row. These unassigned rows require review by the sole visual reader before this candidate can serve as a complete physical page inventory. The original physical metadata should not be discarded merely because the generated candidate has more systematic source ordering.
