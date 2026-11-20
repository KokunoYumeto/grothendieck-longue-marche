# Final requirements and reporting review

Reviewed **2026-11-20 20:23–20:27 UTC**, against the controlling `upload/PROMPT(20261120-181622).md`, especially Method 7–8 and the deliverables/checks sections, and the current output inventory. This is a metadata review. No image reading, ink decision, transcription edit, or frozen-file edit was performed.

## Required artifacts present

All eight original-named page fragments and all named apparatus reports are present: combined transcription, changes, collation, doubts, inventory, notes, progress log, sheet feedback, hand log and `CHECK_EVENTS.tsv`. Each scan has the required neutral boxes, frozen first reading, blind second reading and initial snapshot. The later root audits are complete through scan009 as of its recorded 20:24:42 UTC completion; scan009 metadata synchronization is still in progress when this note is written.

The doubts report already has a notation table, abbreviation section and legibility/witness-comparison assessment. No explicit mathematical-check ID cited in the notes lacked a corresponding `CHECK_EVENTS.tsv` event at the review snapshot. Visual reading is not presented as a mathematical check. No additional named report is missing from the prompt's required list.

## Concrete remaining finalization steps

1. **Reassemble and regenerate after the final scan009 metadata synchronization.** The combined transcription and rendered global reports predate later root audits. The existing structure report states `concatenation_matches:false`; global changes included audit sections only for002,003,005 at the review snapshot. `edition_tools.py assemble` refreshes the combined fragment. `render_reports.py` refreshes changes, collation, inventory and report counts. `render_annotations.py` refreshes doubts and sheet feedback. These renderers do not overwrite the manually synchronized notes or hand log.
2. **Repeat the final static macro/structure and metadata integrity checks on those settled files.** Earlier review JSON files are intermediate snapshots, not final-pass certificates. The parent has commissioned the final macro/excerpt review separately. No TeX compilation is authorized or needed.
3. **Perform the prompt's Method 8 freeze in `progress.log`.** Record `transcription frozen <UTC>` with SHA-256 for every page and the combined transcription only after all decisions are applied. At the end, recheck those hashes and record that they are unchanged in the log. A separate JSON hash manifest does not replace either required log entry.
4. **Resolve the README's prospective completion claim by completing the actual check.** The README says final frozen hashes and their end-of-run recheck are already recorded in `progress.log`; they were absent at this review snapshot. After the actual freeze and recheck, the statement will be accurate. The hand-log introduction, “No habits confirmed yet,” is an initial-state sentence above completed observations; label it as historical or remove the stale qualification.
5. **Build exactly `SP115_CW_156-7.zip` and verify checkpoint filename coverage.** Only that final ZIP is to be offered as the final download. Its contents must retain every non-ZIP filename from both immutable checkpoints, including work documents. Both checkpoint name sets currently remain in `out/`, except `ARCHIVE_MANIFEST.json`, which `make_archive.py` generates during packaging. Nested ZIPs and supplied source inputs are excluded. Run the separate archive coverage check against both checkpoint ZIPs after packaging; archive-manifest content changes are permitted.

The next 45-minute checkpoint cadence would be approximately **20:32:37 UTC** if work is still ongoing. A final archive should not be delayed solely to reach that time; a page/section completion alone does not require a new checkpoint.

## Uncertainty-only counting policy

`render_reports.py` counts `against_C` and `against_H` directly as booleans. Its `count()` has no primary-reading normalization or kind-based exclusion; H collation is gated only by `against_H`. Therefore changing `kind` to `other` alone does not remove a row from substantive witness totals.

A wholly new uncertainty-only disposition belongs in `doubts` and the blind-audit records, without a new substantive `changes` row. If an existing non-substantive disposition remains in `changes`, use actual JSON booleans `against_C:false`, `against_H:false`, with `kind:"other"` and `consequential:false`. Such a row remains in the explicitly labelled Recorded places count and the overall confidence distribution, but not either witness-difference count or H collation. String values such as `"false"` would be truthy and must not be used.

Widening alternatives while retaining the same primary reading does not erase an already established difference from a witness. In the current scan009 records,009-73 and009-75 retain their prior C disagreement (`against_C:true`, `against_H:false`, `kind:"misread word"`) when Cor. Main acquires the alternative Corollaire.009-61 retains its prior H disagreement (`against_C:false`, `against_H:true`, `kind:"misread symbol or index"`) when the primary parallel sign acquires alternative11. Placement009-76 and underline-scope009-84 remain separate substantive disagreements. The blind-audit K count records changed places under its own convention and must not be substituted for either witness-difference total.

No counting-policy or transcription file was edited in this review.

## Subsequent status

At **20:27:25 UTC**, the refreshed structure check passed on all eight fragments and the combined transcription, including exact concatenation. The final static macro review found no concrete defect. Root then recorded the nine transcription hashes in `review/FINAL_TRANSCRIPTION_SHA256.json` and the freeze in `progress.log` at **20:27:43 UTC**. These completed steps supersede the corresponding pending items above; final report rendering, end-of-run hash recheck and ZIP coverage remain the parent's finalization steps.

At **20:28 UTC**, root reported that all apparatus had been regenerated and the final integrity check passed: 240 adjudicated differences, 73 unique changed places, 234 inventory entries, 434 H-collation rows, 25 check events, nine unchanged final transcription hashes and zero problems. This supersedes the earlier pending rendering/integrity items. The separate final archive coverage check follows packaging. The completed scan008/009 excerpt results and final macro review are recorded in the companion review reports.
