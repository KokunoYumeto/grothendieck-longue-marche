# Final ZIP packaging

Only the primary reader should invoke this builder, after the transcription has
been audited and frozen, the context has been opened, the research notes are
complete, and the final unchanged-hash check has been recorded.

```bash
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/make_final_zip.py
```

The default output is:

```text
/workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149.zip
```

`--root` may select a different unpacked work directory and `--output` may select
a different output directory. The archive must retain the requested basename
`MPL_12_099-149.zip` and must be outside the work directory. Existing final ZIPs
are never overwritten.

The builder runs `validate_structure.py` in final mode and refuses errors. It
then packages all eligible work files, including the five requested root
deliverables, all 36 page files, records and scripts. It excludes inputs, scans,
images, crops, context containers, the known context source filenames, existing
archives, dependency caches and attached-prompt copies. Keep all supplied source
materials outside the work directory; filename filters are an additional guard,
not a classification system for arbitrarily renamed sources.

The builder copies the exact page and combined-transcription bytes only after
comparing their SHA-256 digests with the pre-freeze values in `progress.log`.
It verifies the ZIP CRCs and member list and refuses changes to source file
metadata during packaging. A generated `records/final_structure_check.json`
inside the ZIP records structural validation and the 37 frozen hashes verified
for the archived bytes. The builder does not write this record back into the
work tree, alter the progress log, edit the transcription, freeze anything, open
context, or upload the result.

After successful creation, save the returned path using the current Library
helper procedure in `CHECKPOINTS.md`. The sole user-facing download is the final
ZIP. A separate checkpoint is not needed at final packaging unless an hourly
checkpoint is independently due.

## Final validation requirements

- All 36 page files, required inventory rows and nonempty doubts/notes files.
- Exact concatenation of page bytes in scan order into the combined fragment.
- Exactly one initial `cotefile` marker; matching page markers; balanced braces
  and doubt arguments; no obvious editorial placeholders or image-inclusion
  commands.
- Page-completion records in scan order, a subsequent audit record for every
  page, then pre-freeze SHA-256 records for every page and the combined fragment.
- Exactly one freeze record, then exactly one context-open record, then a final
  unchanged-hash record. Milestone UTC timestamps must not run backwards.
- Every current page and the combined fragment must retain its frozen digest.

## Limits requiring the primary reader's review

These checks cannot establish whether every visible element was transcribed,
whether the inventory subdivides the page appropriately, whether sheet kinds or
handwritten page numbers were identified correctly, whether diagrams match the
ink, or whether uncertain readings are appropriately marked. They do not prove
that the visual audits or context-opening dates actually occurred; they verify
the recorded order. They do not check the scholarship, citations, context-result
IDs, abbreviation explanations, or completeness of the requested research-note
questions. A passing structural report is never a claim of semantic accuracy.

This script was prepared and syntax-checked administratively, without examining
manuscript pages, doubts, inventory contents, research notes or context sources.
It was not executed against the task bundle during its preparation.
