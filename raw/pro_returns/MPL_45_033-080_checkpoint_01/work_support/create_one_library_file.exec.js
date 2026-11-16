// Run this entire file in one functions.exec call after editing file and receipt.
// No upload is performed merely by saving this recipe.
const file = "/workspace/scratch/b07ac00ff1ac/REPLACE_WITH_READY_ZIP.zip";
const helperDir = "/workspace/scratch/b07ac00ff1ac/delivery_helpers_2a_fdpar";
const receipt = helperDir + "/receipts/REPLACE_WITH_READY_ZIP.json";
const sh = s => "'" + s.replaceAll("'", "'\\''") + "'";

// Stat only: this does not inspect or extract the archive.
const preflightCode =
  "import pathlib,sys,json; p=pathlib.Path(sys.argv[1]); " +
  "assert p.is_absolute() and p.is_file(), 'missing absolute regular file'; " +
  "n=p.stat().st_size; assert n < 50*1024*1024, 'use maintained prepared helper for files >=50 MiB'; " +
  "print(json.dumps({'size_bytes':n,'path':str(p)}))";
const preflight = await tools.exec_command({
  cmd: "python3 -c " + sh(preflightCode) + " " + sh(file),
  max_output_tokens: 300
});
if (preflight.exit_code !== 0) {
  text(preflight);
  throw new Error("Upload preflight failed; no Library write attempted");
}
const result = await tools.mcp__codex_apps__library_create_library_file({
  file,
  library_artifact_type: "other"
});
store("latest_library_write_response", result);
store("latest_library_write_path", file);
// Immediate writeback: do not insert a model turn or another mutation here.
const writeback = await tools.exec_command({
  cmd: "python3 " + sh(helperDir + "/apply_library_writeback.py") + " " + sh(file) +
       " --receipt " + sh(receipt) + " <<'LIBRARY_WRITEBACK_JSON'\n" +
       JSON.stringify(result) + "\nLIBRARY_WRITEBACK_JSON",
  max_output_tokens: 2000
});
text(writeback);
if (writeback.exit_code !== 0) {
  // Inspect the retained response; do not repeat the create blindly.
  text(result);
  throw new Error("Inspect write result and repair metadata without duplicating the upload");
}

