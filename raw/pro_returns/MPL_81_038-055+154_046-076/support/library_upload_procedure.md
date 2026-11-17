# ZIP saving procedure

No upload has been performed by the support agent.

For each single new checkpoint ZIP or the final ZIP below about 50 MiB, use the
Library skill's direct-create fast path. Each checkpoint is a distinct create;
never replace an earlier checkpoint. The source archives must remain excluded.

The current tool declaration is:

```typescript
tools.mcp__codex_apps__library_create_library_file({
  file: "/absolute/path/to/archive.zip",
  library_artifact_type: "other"
})
```

Exactly one of `file` or `files` is allowed. No destination directory needs to
be specified for the default destination. Keep each checkpoint and final upload
sequential; do not run Library write calls in parallel.

After success, apply the **complete returned** xattrs array (or `[]`) to the
original ZIP with its exact returned `library_file_id`, using:

```bash
python3 /workspace/scratch/89f8415d3ab0/support/library_helpers/library_file_transfer.py \
  apply-xattrs /absolute/path/to/archive.zip EXACT_RETURNED_LIBRARY_FILE_ID <<'LIBRARY_XATTRS_JSON'
[]
LIBRARY_XATTRS_JSON
```

The empty array above is a placeholder; replace it with the returned array when
one is present. Both the create call and this helper must execute in the same
`functions.exec` invocation, without returning to the model between them.
Retain the complete result privately, and print only success metadata needed by
the parent. Do not print signed URLs or credentials.

One defensive code-mode template follows. It inspects the actual returned
payload rather than assuming whether the app wraps its file object in `data`,
`result`, or `files`. It refuses to choose between different returned identities.

```javascript
const zipPath = "/workspace/scratch/89f8415d3ab0/MPL_81_038-055+154_046-076.zip";
const result = await tools.mcp__codex_apps__library_create_library_file({
  file: zipPath,
  library_artifact_type: "other"
});
store("latest_library_zip_create", result);
if (result.isError) {
  text({saved:false, message:"Library create reported an error; inspect retained result."});
  exit();
}
let payload = result.structuredContent;
if (!payload) {
  const texts = (result.content || []).filter(x => x.type === "text");
  for (const block of texts) {
    try { payload = JSON.parse(block.text); break; } catch (_) {}
  }
}
if (!payload) throw new Error("Create result has no parseable structured payload.");
const candidates = [];
function visit(value) {
  if (!value || typeof value !== "object") return;
  if (typeof value.library_file_id === "string") candidates.push(value);
  for (const child of Object.values(value)) visit(child);
}
visit(payload);
const identities = [...new Set(candidates.map(x => x.library_file_id))];
if (identities.length !== 1) {
  throw new Error("Cannot identify exactly one returned Library file; retained create result requires inspection.");
}
const identity = identities[0];
const candidate = candidates.find(x => x.library_file_id === identity && Array.isArray(x.xattrs))
  || candidates.find(x => x.library_file_id === identity);
const attrs = candidate.xattrs || [];
if (!Array.isArray(attrs)) throw new Error("Returned xattrs is not an array.");
const quote = value => "'" + String(value).split("'").join("'\"'\"'") + "'";
const helper = "/workspace/scratch/89f8415d3ab0/support/library_helpers/library_file_transfer.py";
const command = "python3 " + quote(helper) + " apply-xattrs " + quote(zipPath) + " " + quote(identity)
  + " <<'LIBRARY_XATTRS_JSON'\n" + JSON.stringify(attrs) + "\nLIBRARY_XATTRS_JSON\n";
const applied = await tools.exec_command({cmd:command,max_output_tokens:1000});
text({saved:true,library_file_id:identity,local_path:zipPath,
      identity_persisted:applied.exit_code === 0,helper_result:applied.output});
```

If the actual result places xattrs outside the file object, preserve that exact
returned array rather than reconstructing it. The code template should be
adjusted to the observed result shape when necessary. If identity persistence
fails, report that separately from a successful upload; do not upload a duplicate
file just to repeat the metadata operation.

For an archive around 50 MiB or larger, the current `library_prepare_uploads`
and `library_finalize_uploads` tools are available, so read the Library skill's
`references/prepared-uploads.md` and use its bundled prepared-upload helper.
The checkpoint source excludes scans, so the direct path will normally suffice.

The final response should offer only the requested final ZIP. Use its exact
returned native Library ID in a native Library link when appropriate:
`https://chatgpt.com/library?file_id=EXACT_RETURNED_ID&account_id=personal`.
