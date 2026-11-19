// Procedure for functions.exec, not a shell/Node program.
// Use only AFTER the scheduled checkpoint time or when the final ZIP is ready.
// Change archivePath for each newly created archive. Do not rerun create after
// a successful save merely because the xattr helper failed: retry only the
// helper with the retained exact result and identifier.
const archivePath = "/workspace/scratch/c6b7a14fa47f/SP32_CW_156-3_checkpoint_01.zip";
const helperPath = "/workspace/scratch/c6b7a14fa47f/SP32_CW_156-3_work/scripts/library_transfer_20261119/library_file_transfer.py";
const recordsPath = "/workspace/scratch/c6b7a14fa47f/SP32_CW_156-3_work/records";

const result = await tools.mcp__codex_apps__library_create_library_file({
  file: archivePath,
  library_artifact_type: "other",
});
// Retain the unmodified response immediately, even if its schema is unexpected.
store("sp32_last_library_create", { original_local_path: archivePath, result });
if (result.isError) {
  throw new Error("Library create returned an error; inspect the retained response.");
}
const roots = [];
if (result.structuredContent != null) roots.push(result.structuredContent);
if (!roots.length) {
  for (const block of result.content ?? []) {
    if (block.type !== "text") continue;
    try { roots.push(JSON.parse(block.text)); } catch (_) {}
  }
}
const objects = [];
function collect(value) {
  if (value == null || typeof value !== "object") return;
  if (Array.isArray(value)) { for (const child of value) collect(child); return; }
  objects.push(value);
  for (const child of Object.values(value)) collect(child);
}
for (const root of roots) collect(root);
const candidates = objects.filter(value =>
  typeof value.library_file_id === "string" && value.library_file_id.length > 0);
const ids = [...new Set(candidates.map(value => value.library_file_id))];
if (ids.length !== 1) {
  throw new Error("Expected exactly one returned Library file id; do not repeat create. Inspect sp32_last_library_create.");
}
const libraryFileId = ids[0];
const attributeArrays = objects.filter(value => Object.hasOwn(value, "xattrs")).map(value => value.xattrs);
if (attributeArrays.some(value => value != null && !Array.isArray(value))) {
  throw new Error("Unexpected xattrs shape; do not repeat create. Inspect the retained response.");
}
const uniqueAttributeArrays = [...new Map(attributeArrays.filter(value => value != null).map(value => [JSON.stringify(value), value])).values()];
if (uniqueAttributeArrays.length > 1) {
  throw new Error("Ambiguous returned xattrs; do not repeat create. Inspect the retained response.");
}
const xattrs = uniqueAttributeArrays[0] ?? [];
const shellQuote = value => "'" + String(value).replaceAll("'", "'\"'\"'") + "'";
const command = "python3 " + shellQuote(helperPath) + " apply-xattrs " + shellQuote(archivePath) + " " + shellQuote(libraryFileId) +
  " <<'SP32_RETURNED_XATTRS_JSON'\n" + JSON.stringify(xattrs) + "\nSP32_RETURNED_XATTRS_JSON";
const applied = await tools.exec_command({ cmd: command, max_output_tokens: 1000, yield_time_ms: 10000 });

// Preserve identity/version metadata with the original local path. Do not copy
// transient download URLs or other unrelated response fields into the record.
const metadataKeys = ["library_file_id", "file_id", "id", "version", "version_id", "current_version", "filename", "name", "path", "library_path"];
const metadata = candidates.map(value => Object.fromEntries(metadataKeys.filter(key => Object.hasOwn(value, key)).map(key => [key, value[key]])));
const record = {
  original_local_path: archivePath,
  library_file_id: libraryFileId,
  returned_metadata: metadata,
  returned_xattrs: xattrs,
  xattrs_applied: applied.exit_code === 0,
  helper_result: applied,
};
store("sp32_last_library_identity", record);
const basename = archivePath.split("/").at(-1);
const recordPath = recordsPath + "/" + basename + ".library.json";
const recordText = JSON.stringify(record, null, 2) + "\n";
const written = await tools.apply_patch("*** Begin Patch\n*** Add File: " + recordPath + "\n" + recordText.split("\n").map(line => "+" + line).join("\n") + "\n*** End Patch");
text({ saved: true, original_local_path: archivePath, library_file_id: libraryFileId, xattrs_applied: applied.exit_code === 0, metadata_record: recordPath });
if (applied.exit_code !== 0) {
  text({ metadata_helper_failed: true, helper_result: applied });
  throw new Error("Archive was saved, but local identity metadata was not confirmed. Retry only apply-xattrs, not create.");
}
