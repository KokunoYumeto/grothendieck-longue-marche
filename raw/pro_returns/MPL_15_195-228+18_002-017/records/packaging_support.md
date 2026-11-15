# Mechanical packaging support

This record concerns packaging and persistence only. It does not document a manuscript reading, an audit, or completion of any transcription page.

## Checkpoint timing

The work-start timestamp supplied by the primary reader is **2026-11-15 12:11:41 UTC**. The first hourly checkpoint is therefore due **2026-11-15 13:11:41 UTC**. Checkpoint ZIPs must be produced only at the requested hourly intervals, with increasing two-digit names, and must never overwrite earlier snapshots. The final ZIP is separate.

## Packaging script

`records/package_deliverables.py` packages all regular files below the deliverable directory, retaining relative paths. It excludes Python bytecode/cache directories, source-input directories, the supplied archives, supplied scan-image filenames, and the known context-source files. It refuses symlinks and outputs inside the source tree, verifies that input files did not change while packaging, checks the ZIP CRCs and member list, and publishes its output atomically without overwriting an existing file.

The script does not schedule itself, create log entries, or upload anything. Append the intended checkpoint event to `progress.log` before packaging if that event must appear in the snapshot; record the confirmed save afterward for inclusion in subsequent snapshots.

From the deliverable directory, when checkpoint 01 is due:

```bash
python records/package_deliverables.py \
  /workspace/scratch/390184a42c26/MPL_15_195-228+18_002-017_checkpoint_01.zip
```

For the final ZIP, after all required checks:

```bash
python records/package_deliverables.py \
  /workspace/scratch/390184a42c26/MPL_15_195-228+18_002-017.zip
```

The JSON result records the path, byte count, file count, SHA-256, and excluded paths. No ZIP was created during preparation of this script.

## Current Library helper bundle

The current skill's helper files were read in full and copied unchanged into this fresh private scratch directory:

`/workspace/scratch/390184a42c26/.mpl_library_helpers_18x03sdj`

| Helper | SHA-256 |
| --- | --- |
| `library_file_transfer.py` | `d0385de4b634c4a6d4c26a83b40ee4ff33461e42473ce8c0387460be2465e314` |
| `library_hosted_apps.py` | `7958642b88cde925aaca036989de1028c0864eb6d82a9cb175ebf9380cb9677b` |
| `library_upload.py` | `5bc473dadefe1f68ee8797baaed19d6662642d0ea4bcba128fa12938faa0d767` |

Source package: `c0/library`.

Source directory: `skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library/scripts/`.

All three helpers were syntax-checked. A new environment must refetch the current helpers following the Library skill; do not assume this scratch path persists or reuse stale helpers from another run.

## Saving one completed small ZIP

For one confirmed local ZIP below approximately 50 MiB, the Library skill's fast path is `mcp__codex_apps__library_create_library_file` with its absolute local path and `library_artifact_type: "other"`. Inspect the success response, retain its exact `library_file_id`, filename, version and xattrs, and, **within the same `functions.exec` invocation**, call the current transfer helper with `apply-xattrs`, that original local path, and the returned exact `library_file_id`. Supply the complete returned xattrs array (or `[]`) as JSON on stdin. Do not return to the model between the create and metadata calls.

```bash
python3 /workspace/scratch/390184a42c26/.mpl_library_helpers_18x03sdj/library_file_transfer.py \
  apply-xattrs /absolute/path/completed.zip RETURNED_LIBRARY_FILE_ID <<'JSON'
[]
JSON
```

The `[]` above is only the no-xattrs case; otherwise use the complete actual returned array. Inspect the helper's exit status before claiming local identity persistence. Do not fabricate an identifier, retry an uncertain create blindly, or save a checkpoint before its due time.

## Prepared-upload route

Both prepared Library tools are available. For multiple completed files or a file approximately 50 MiB or larger, use the current upload helper, which owns preparation, transfer, finalization, result correlation and metadata persistence. Supply one complete JSON request with stdin closed, preserve file order, and inspect every result. Do not call prepare/finalize separately or switch a started helper write to direct writes.

```bash
python3 /workspace/scratch/390184a42c26/.mpl_library_helpers_18x03sdj/library_upload.py <<'JSON'
{"uploads":[{"local_path":"/absolute/path/completed.zip","purpose":"create_library_file","library_artifact_type":"other"}]}
JSON
```

Use actual completed file paths. The upload helper has not been executed, and no Library save was performed during this support task.
