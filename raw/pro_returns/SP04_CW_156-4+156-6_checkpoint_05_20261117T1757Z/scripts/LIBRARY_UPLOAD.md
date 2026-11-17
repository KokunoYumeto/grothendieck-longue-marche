# Prepared Library transfer procedure

These are administrative instructions for the root agent. No checkpoint has
been created or uploaded by the tooling-preparation agent.

Current official skill/helper source:

`skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library`

The current complete official helper files were fetched unchanged into this
fresh private directory (no older downloaded helper copies were found):

```
/workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/SKILL.md
/workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/scripts/library_upload.py
/workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/scripts/library_hosted_apps.py
/workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/scripts/library_file_transfer.py
```

Reuse these copies for this task. The upload helper owns preparation, byte
transfer, finalization, ordered result inspection data, and local metadata
writeback. Do not call prepare/finalize separately or implement file transfers.

## Hourly checkpoint creation

The task started at `2026-11-17 12:53:17 UTC`. The first checkpoint is due at
`2026-11-17 13:53:17 UTC`; `manage.py checkpoint` enforces the one-hour interval.
It returns the actual ZIP path. Always use that returned path and retain each
checkpoint under its existing sequential name. A checkpoint ZIP contains all
output records and crops but excludes attached source files and prior ZIPs.

## Prepared upload: one ZIP around/over 50 MiB, or a multiple-file task

The prepared tools are available. All paths below must refer to an existing
regular local file. Substitute only the actual returned checkpoint path.
Pass this whole JSON and EOF together; do not start the helper interactively.

```bash
python3 /workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/scripts/library_upload.py <<'JSON'
{
  "uploads": [
    {
      "local_path": "/workspace/scratch/ef49975b2dd8/SP04_CW_156-4+156-6_checkpoint_01.zip",
      "purpose": "create_library_file",
      "library_artifact_type": "other"
    }
  ]
}
JSON
```

The official helper offers the conversation-scoped path for direct transfer
when available and privately handles a signed transfer otherwise. Its result
contains an ordered `results` array. Inspect the individual item's `status`,
`library_file_id`, `file_id`, `file_name`, `path` when present,
`current_version_number` when present, and `local_metadata_applied`.
Retain the complete result privately. The expected success is the actual
item's `status: succeeded`, not merely a successful subprocess exit.

For a prepared upload, give the skill's brief saving update before invocation.
The user asked for only the final ZIP as a download: do not add checkpoint
download links to chat. Record the checkpoint's successful persistent save in
the live progress log after inspecting the result. That later log line will
be included in the next checkpoint.

This task writes successive checkpoint files and a final file. The prepared
helper is a suitable route for each due checkpoint, including a small ZIP,
while preserving their order.

## Direct route for exactly one local ZIP under about 50 MiB

The direct create schema currently exposed is:

```typescript
tools.mcp__codex_apps__library_create_library_file({
  file: absoluteLocalPath,
  library_artifact_type: "other"
})
```

`file` and `files` are exclusive. The latter accepts 1–20 absolute paths, but
prepared tools are available and should be used for multiple files. A resolved
destination can be supplied with `directory_id`; do not invent one.

After direct-create success, use the returned per-item metadata and invoke
the official `library_file_transfer.py apply-xattrs` with the original path,
the actual returned `library_file_id`, and the complete returned `xattrs` array
or `[]` on stdin. The create tool and metadata helper must run in one
`functions.exec` call, without returning to the model between them. Prefer
`structuredContent` to a parsed text content block. Inspect each actual
result's status before applying metadata; do not manufacture missing fields.

```bash
python3 /workspace/scratch/ef49975b2dd8/out/scripts/library_helpers_r_wds6xe/scripts/library_file_transfer.py \
  apply-xattrs '/absolute/original/checkpoint.zip' 'actual-returned-library-id' <<'JSON'
[]
JSON
```

The array above is only a shape example; replace it with the complete actual
returned xattrs array. The prepared helper already performs this operation,
so never repeat it after a prepared-helper upload.

## Crop utility

`out/scripts/crop.py` applies only explicit geometry supplied by the root
reader, then appends a recipe to `out/crop_recipes.jsonl`. It does not claim a
reading, mark an image viewed, inspect text, or make transcription decisions.

```bash
python out/scripts/crop.py /absolute/source.jpg /absolute/out/crops/name.png \
  --box 100 200 800 500 --rotation 0 --scale 2 --label 'root-authored label'
```

The box is `(left, top, right, bottom)` in original pixels, with right/bottom
excluded. No automatic EXIF orientation change is made. Rotation is
counterclockwise after the crop, with expanded bounds; scale is applied last.
The log records source/output hashes and dimensions, exact geometry, time,
format, resampling, and root-supplied label. Existing targets require explicit
`--overwrite`. Original images are never modified. PNG is preferable for
lossless enlarged crops.
