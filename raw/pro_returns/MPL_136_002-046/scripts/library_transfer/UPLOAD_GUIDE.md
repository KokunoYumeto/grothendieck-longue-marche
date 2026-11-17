# Uploading the checkpoint and final ZIPs

Preparation only: no upload was made while creating this guide. The first hourly checkpoint is due **2026-11-17 14:21:10 UTC**; subsequent checkpoints are hourly. Do not create extra checkpoint uploads between those times. Each checkpoint is an independent new ZIP, never a replacement of a preceding checkpoint. The final ZIP is also a new item.

The three Python helpers in this directory were copied in full, unchanged, from the current `c0/library` cloud skill resources on 2026-11-17. The directory is private (mode 0700). Helpers are reused during this run, including retries; do not fetch an older copy or write a substitute transfer client.

## Available direct-create tool

The tool's current declaration is:

```ts
tools.mcp__codex_apps__library_create_library_file(args: {
  directory_id?: string | null;
  file?: string;
  files?: Array<string>;
  library_artifact_type?:
    "other" | "image" | "image_gen" | "report" | "sheet" | "slides" | null;
}): Promise<CallToolResult>
```

Supply exactly one of `file` and `files`. `file` must be the absolute path of an existing local file. `files` accepts 1–20 such paths, but the prepared helper is the required route when both prepared tools are available and several files are saved together. Both prepared tools are currently available.

For one newly completed ZIP below about 50 MiB, use the direct create route. Checkpoint ZIPs must omit the attached sources, scans, and previous ZIPs. No Library search, listing, reading, or materialization is needed or permitted for this task.

## Direct create and metadata in one code-mode invocation

Set `localPath` to the actual completed ZIP. Run the create call and `apply-xattrs` within the **same `functions.exec` invocation**, without returning to the model between them. The following handles the documented structured result and the usual single-item `results` variant, and passes the entire returned xattrs array unchanged to the bundled helper:

```javascript
const localPath = "/workspace/scratch/3c4fe837ef18/MPL_136_002-046_checkpoint_01.zip";
const helper = "/workspace/scratch/3c4fe837ef18/MPL_136_002-046/scripts/library_transfer/library_file_transfer.py";
const result = await tools.mcp__codex_apps__library_create_library_file({
  file: localPath,
  library_artifact_type: "other"
});
store("latest_library_create_result", result);
if (result.isError) {
  text(result);
  exit();
}
let payload = result.structuredContent;
if (payload == null) {
  for (const block of result.content ?? []) {
    if (block.type !== "text") continue;
    try {
      const parsed = JSON.parse(block.text);
      if (parsed && typeof parsed === "object") { payload = parsed; break; }
    } catch (_) {}
  }
}
const records = Array.isArray(payload?.results) ? payload.results : [payload];
if (records.length !== 1 || !records[0] ||
    records[0].status === "failed" ||
    typeof records[0].library_file_id !== "string") {
  text({error: "Inspect the saved create result; do not create the file again.", result});
  exit();
}
const record = records[0];
const shellQuote = value => "'" + String(value).replace(/'/g, "'\\''") + "'";
const command = ["python3", helper, "apply-xattrs", localPath,
                 record.library_file_id].map(shellQuote).join(" ") +
  " <<'LIBRARY_XATTRS_JSON'\n" +
  JSON.stringify(record.xattrs ?? []) + "\nLIBRARY_XATTRS_JSON";
const applied = await tools.exec_command({cmd: command, max_output_tokens: 1000});
const receipt = {
  local_path: localPath,
  library_file_id: record.library_file_id,
  file_id: record.file_id,
  file_name: record.file_name,
  path: record.path,
  current_version_number: record.current_version_number,
  local_metadata_applied: applied.exit_code === 0
};
store("latest_library_create_receipt", receipt);
text(receipt);
if (applied.exit_code !== 0) text(applied);
```

Inspect the operation and per-item result rather than assuming success. Retain the exact returned identity, name, path, and version beside the original local path in the work record. The returned filename and path are authoritative because name collisions can cause renaming. Do not claim that local metadata was persisted if the helper failed, and do not upload a second time merely to retry metadata application.

The helper's required form is:

```sh
python3 /workspace/scratch/3c4fe837ef18/MPL_136_002-046/scripts/library_transfer/library_file_transfer.py \
  apply-xattrs /absolute/path/to/the-created.zip EXACT_RETURNED_LIBRARY_FILE_ID <<'JSON'
[]
JSON
```

Replace `[]` with the complete actual returned `xattrs` array when present. Both positional arguments after `apply-xattrs` are required. This command applies identity and metadata; it does not perform another upload.

## Prepared upload, only if required by size or batch

If a ZIP is around 50 MiB or larger, or several files must be saved in one operation, invoke the bundled prepared helper once with the entire ordered batch. It handles preparation, transfer, finalization, and xattrs itself. Do not call prepare/finalize separately or transfer returned URLs manually.

```sh
python3 /workspace/scratch/3c4fe837ef18/MPL_136_002-046/scripts/library_transfer/library_upload.py <<'JSON'
{"uploads":[{"local_path":"/absolute/path/to/the-completed.zip","purpose":"create_library_file","library_artifact_type":"other"}]}
JSON
```

The JSON and EOF must be supplied together, as shown. Inspect every item in the ordered `results` array, including `status` and `local_metadata_applied`. Never switch a started prepared upload to a direct write. If an operation times out with an unknown outcome, preserve that uncertainty instead of creating a second write automatically.

For the final user-facing download, use the exact returned Library ID in the supported native Library URL if needed:

```text
https://chatgpt.com/library?file_id=EXACT_RETURNED_LIBRARY_FILE_ID&account_id=personal
```

Do not expose signed transfer URLs or xattr details in the user-facing response. Offer only the requested final ZIP download; checkpoint receipts remain work records.
