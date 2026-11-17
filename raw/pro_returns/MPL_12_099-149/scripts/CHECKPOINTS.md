# Hourly checkpoints and file-transfer procedure

`make_checkpoint.py` creates one numbered ZIP only when explicitly invoked. It
does not schedule itself, change the deliverables, or upload anything.

The first checkpoint cannot be created before **2026-11-17 20:43:18 UTC**.
Later calls must be at least one hour after the preceding checkpoint. Do not
invoke this script after individual pages, parts, sections, or other milestones.

At the hourly boundary, the primary reader can run:

```bash
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/make_checkpoint.py
```

The default output directory is
`/workspace/scratch/1e5f3f82ab2e/work/checkpoints`, outside the bundle itself.
Each archive has the name `MPL_12_099-149_checkpoint_NN.zip`; the sequence starts
at 01 and existing names are never overwritten. Atomic exclusive publication
prevents accidentally replacing an earlier checkpoint. The script reports the
absolute path, creation time, next eligible time, file count, size and SHA-256.
It does not mark the checkpoint as uploaded.

The archive contains every eligible file under the work bundle, with paths
relative to its root, including page files, inventory, doubts, notes, logs,
scripts, reports and other records. It excludes input/upload/scan/image/crop/
context/checkpoint directories, raster/vector image files, ZIPs, bytecode,
dependency caches and copies of the attached prompt. Symlinks are refused.
The script checks for files changing during creation and checks ZIP CRCs.
These operations copy bytes without interpreting manuscript contents.
Known context-source filenames and directories containing `context` or `scans`
in their names are also excluded. Keep supplied source materials outside the
work tree; filters cannot identify sources that have been arbitrarily renamed.

## Current-run Library helpers

The current Library skill's three helper resources were copied unchanged into
one private directory outside the deliverable bundle:

```text
/workspace/scratch/1e5f3f82ab2e/.mpl_current_library_helpers_rf6iuok6/library_upload.py
/workspace/scratch/1e5f3f82ab2e/.mpl_current_library_helpers_rf6iuok6/library_file_transfer.py
/workspace/scratch/1e5f3f82ab2e/.mpl_current_library_helpers_rf6iuok6/library_hosted_apps.py
```

They are reusable within this run. A resumed run in a new environment must fetch
current helpers again, following the Library skill; these scratch paths are
not assumed to survive. No helper contains copied manuscript or context data.

Both prepared-upload tools are available. The Library skill requires its
prepared-upload helper for multiple files in an ordered task batch or a file
around 50 MiB or larger. The helper owns preparation, transfer, finalization and
metadata writeback. Invoke it once for the file(s) presently due, supplying JSON
and EOF together, and inspect every result:

```bash
python3 /workspace/scratch/1e5f3f82ab2e/.mpl_current_library_helpers_rf6iuok6/library_upload.py <<'JSON'
{
  "uploads": [
    {
      "local_path": "/absolute/path/to/the/checkpoint.zip",
      "purpose": "create_library_file",
      "library_artifact_type": "other"
    }
  ]
}
JSON
```

This example is a procedure, not an executed upload. Replace its path with the
exact archive path returned by the checkpoint builder. Do not call
`prepare_uploads` or `finalize_uploads` separately when using this helper.
Do not switch an upload already started with the helper to a direct action.
Do not automatically retry an upload whose finalization outcome is uncertain.
Store the returned Library identity with the root's administrative records.

For a single confirmed local file under approximately 50 MiB, the skill also
provides its direct-create fast path:

1. Call `mcp__codex_apps__library_create_library_file` with
   `{"file":"/absolute/path/to/file.zip","library_artifact_type":"other"}`.
2. Inspect the returned result. Prefer `structuredContent`, otherwise parse its
   JSON text content. Retain the exact `library_file_id`, `file_id`, version,
   original local path and complete `xattrs` array.
3. In the **same code-mode invocation**, run
   `library_file_transfer.py apply-xattrs ORIGINAL_PATH LIBRARY_FILE_ID`, passing
   the complete returned xattrs array (or `[]`) as JSON on stdin. Inspect its
   result. Use proper shell quoting for arguments and a quoted heredoc for JSON.

The final deliverable is a separate `MPL_12_099-149.zip`, saved through the same
applicable Library route. Do not delay or create extra hourly checkpoints merely
to make final packaging coincide with an hourly boundary.
