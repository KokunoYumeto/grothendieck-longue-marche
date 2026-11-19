# Finalization checklist — SP32_CW_156-3

This checklist concerns file structure and sequencing. It does not certify any
reading or mathematical statement. Prepared by the infrastructure agent without
opening scans, witness text, transcription pages, apparatus, or context.

## Before freezing

1. Finish the primary reader's second visual audit of scans 026–041. There should
   be one nonempty `records/auditNNN.json` per scan and the required real UTC audit
   entries in `progress.log`.
2. Incorporate any audit corrections before freezing. Assemble the combined
   fragment from the final versions of all sixteen page files, in scan order.
3. Run `scripts/validate_package.py`. The notes may still be absent at this stage;
   assess the resulting missing-notes error as the expected unfinished phase.
   Resolve actual page-marker, schema, brace, environment, and combined-fragment
   discrepancies before freezing. The script makes no reading judgments.
4. Write one SHA-256 manifest containing all sixteen relative `pages/...tex`
   paths and `SP32_CW_156-3_transcription.tex`, preferably
   `records/frozen.sha256` in ordinary `sha256sum` format. Record every hash and
   the real `transcription frozen <UTC time>` line in `progress.log`.
5. Only after that freeze record, append `context opened <UTC time>` and open
   the supplied context and the permitted sweep prose.

## After freezing

1. Treat the seventeen frozen files as immutable. A reading suggested by context
   belongs in the research notes. Do not regenerate the combined fragment or
   alter a page merely to reconcile later research.
2. Complete `SP32_CW_156-3_notes.md` and `CHECK_EVENTS.tsv`. The latter needs actual
   check events; an existing header is not a completed event table. Event types
   must describe what was actually done. Only the reader can assess coverage.
3. Complete the two standing questions and comparison with witness C's notes,
   including reasons for items retained, corrected or dropped.
4. Recompute all seventeen frozen hashes, compare them to the freeze manifest,
   and append the result and real UTC time to `progress.log`. Do not replace
   a discrepant manifest with new hashes to make the check pass.
5. Run the final structural gate from the work directory:

   ```bash
   python scripts/validate_package.py --final --hash-manifest records/frozen.sha256
   ```

   The final gate requires all expected deliverables, all sixteen audit-record
   files, at least one event row, complete freeze-manifest coverage, and matching
   hashes. Inspect warnings separately; these are conservative lexical checks.

## Packaging and saving

1. Finish all desired authored files and logs before packaging. The packager
   snapshots current files; later edits do not enter an existing ZIP.
2. Preserve all earlier checkpoint ZIPs. At the next scheduled checkpoint time
   (21:52:06 UTC on 2026-11-19), use the next unused checkpoint number, with its
   ZIP outside the work directory. Do not create an early checkpoint.
3. The packager automatically includes research notes, `CHECK_EVENTS.tsv`, audit
   records, a frozen manifest, other authored records, evidence crops, scripts,
   and `progress.log`. It excludes original scans, attachment/source folders,
   nested checkpoint ZIPs, and temporary compiler/cache files.
4. Build the final ZIP outside the work directory:

   ```bash
   python scripts/package_archive.py \
     /workspace/scratch/c6b7a14fa47f/SP32_CW_156-3_work \
     /workspace/scratch/c6b7a14fa47f/SP32_CW_156-3.zip
   ```

   The packager refuses an existing output and verifies CRCs and entry count.
   Do not rerun against the same output path expecting it to update an archive.
5. Review the reported archive size. For one archive below approximately 50 MiB,
   use the prepared single-exec direct-save procedure in
   `scripts/save_archive_to_library.exec.js`, changing its `archivePath` constant
   to the actual archive. Inspect the returned upload and xattr-helper outcomes.
   If create succeeded but metadata application failed, retry only the metadata
   helper with the same returned identity; do not create a duplicate upload.
6. The upload identity record is necessarily written after its ZIP is built. A
   checkpoint's record will enter a later checkpoint/final ZIP. A final ZIP's own
   post-upload identity record cannot be inside those already-uploaded bytes;
   this does not change the transcription hashes or the archive's contents.
7. Offer the final `SP32_CW_156-3.zip` as the only download, as requested. Do not
   expose individual internal files or checkpoint links in the final response.

## Concrete limits of the structural tools

- The validator cannot establish that an audit record reflects a full visual
  audit, that notes cover every manuscript item, or that a check-event type is
  warranted. Those remain the primary reader's responsibilities.
- Lexical TeX checks do not replace a real compiler. A warning is a prompt to
  inspect the indicated structure, not evidence that the reading is wrong.
- Do not write new files while packaging. ZIP integrity confirms stored bytes,
  not that simultaneously changing files formed one intended final state.
