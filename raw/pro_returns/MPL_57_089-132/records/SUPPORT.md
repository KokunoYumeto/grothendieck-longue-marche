# Mechanical support tools

`package_tools.py` performs structural checks only. It never opens scan images or the context archive, uses OCR, evaluates readings, or edits page text. Its checks cannot establish visual completeness or correctness.

`refresh_doubts.py` aggregates the reader's `scanNNN.json` records into the doubts file. Run `python records/refresh_doubts.py` after adding or correcting records. It validates the record schema before replacing the generated doubts file and writes its status to `records/doubts_aggregation_report.md`. It groups only exact repeated notation or abbreviation entries and retains all doubt rows verbatim. Manual audit material belongs in `records/doubts_manual.md`; edits inside the generated file's marked manual section are also preserved on refresh, with conflicting copies retained separately. It never opens source images, context, transcription files, or inventory.

When present, the reader-supplied `records/notation_review.md` is inserted before the detailed notation table, and `records/reader_legibility_review.md` begins the legibility section. The latter's heading level is nested under that section; its prose is unchanged. These reader assessments remain distinct from the aggregation script's mechanical counts and do not imply that the script inspected images.

`structural_review.py` runs additional environment, diplomatic-macro, control-character, arrow-option, quotation-token, notation-variant, and inventory-count heuristics, writing `records/mechanical_review_full_pass.md` by default. It reads transcription and metadata only, never images or context, and makes no automatic corrections. Its inventory-count explanations concern code nesting and explicitly grouped inventory rows; they are not findings of visual completeness. The optional per-page `audit` metadata is validated by the record reader and preserved in the records, not copied into the doubt table.

The default root is this package's parent directory. Run it using Python 3:

```bash
python records/package_tools.py validate
python records/package_tools.py combine
python records/package_tools.py validate --complete --report records/mechanical_validation.md
python records/package_tools.py hashes
python records/package_tools.py checkpoint 1
python records/package_tools.py final
```

For an unfinished combined working copy, use `combine --partial`. `combine` refuses to write after the progress log contains a `transcription frozen` marker. `hashes` prints SHA-256 values without changing any files.

`checkpoint N` creates `MPL_57_089-132_checkpoint_NN.zip` one directory above the package. It refuses to overwrite a checkpoint and enforces at least one hour from the first progress timestamp or most recent checkpoint. It does not append to the progress log or upload anything. The calling reader owns the hourly schedule and the preservation step.

`final` requires all expected scans, their inventory rows marked `yes`, a combined transcription matching the page files, and the named doubts, notes, and progress files. It creates `MPL_57_089-132.zip` and refuses to overwrite it. Its gates are mechanical only, not certification that a second visual audit or research work is complete.

ZIPs contain the deliverable tree, including supporting records and scripts. They exclude `scans`, `upload`, `uploads`, `context`, cache directories, symlinks, `.zip`, and compiled Python bytecode. The original supplied archives and source scans are outside the deliverable tree and are not included.

## Current Library helpers

The three scripts in `library_helpers/` were retrieved on 2026-11-17 from the current `c0/library` skill's exact resources:

- `scripts/library_file_transfer.py`
- `scripts/library_upload.py`
- `scripts/library_hosted_apps.py`

They are the provider's unmodified helpers, not task-specific replacements. No Library content was read and no file was uploaded while preparing these helpers. For direct creation of one small ZIP, the Library skill requires its `create_library_file` action followed by `library_file_transfer.py apply-xattrs ABSOLUTE_PATH EXACT_RETURNED_LIBRARY_FILE_ID`, supplying the complete returned xattrs array (or `[]`) on standard input. In code mode those two actions must be in the same invocation. If using prepared uploads, first read the current skill's `references/prepared-uploads.md`; `library_upload.py` has both required sibling modules here.
