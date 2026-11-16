# Mechanical package support

`package_tools.py` was prepared as support code only. Its author did not open the manuscript images, page transcriptions, or context contents, and did not execute the script. It does not perform OCR or assess the fidelity of any reading. Only the principal transcription stream may mark a page complete or visually audited.

Run commands from any directory, using this absolute path:

```bash
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py combine
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py check
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py freeze
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py verify-frozen --record
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py checkpoint
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/package_tools.py final
```

The root defaults to the parent of `scripts/`. To resume from an extracted checkpoint in a different location, the script remains relocatable, or supply `--root /absolute/package/directory` **before** the subcommand.

## Behavior

- `combine` joins existing page files in scan order and adds `\\cotefile{84}` at the start only if needed. It refuses to overwrite the combined file after a freeze has been logged. Page files are never edited.
- `check` requires all 48 scans, 97–145 except the omitted blank scan 123. It checks filenames, one corresponding `\\scanpage` marker in every page, basic brace balance with escaped braces/comments respected, the inventory header and row values, and correspondence of the combined fragment to the pages. It checks for preamble, included-file, and image macros. It does not compile LaTeX or determine whether manuscript content was omitted.
- `check --partial --without-combined` applies mechanical checks to a work in progress without requiring every scan or the combined fragment.
- `freeze` requires a complete successful mechanical check, every `84 scan NNN done ...` line and every `scan NNN audited ...` line. It refuses to freeze after `context opened` or after an earlier freeze. It writes `freeze.sha256`, repeats all 49 hashes in `progress.log`, and appends `transcription frozen <UTC time>`. It never changes the page files or the combined transcription. The operator remains responsible for actually performing all audits before recording them.
- `verify-frozen` verifies the 48 page hashes and the combined fragment hash; `--record` adds `frozen transcription hashes unchanged <UTC time>` on success.
- `checkpoint` refuses before one hour has passed since the initial timestamp or the latest checkpoint assembly timestamp. It creates the next uniquely numbered archive beside the package directory and never overwrites an earlier archive. It includes all written deliverables and work documentation under the package directory, including support scripts. It excludes source-image extensions, ZIP files, and directories named `upload`, `uploads`, `scans`, `context`, `sources`, `__pycache__`, or `.git`. No source materials should be stored within the deliverable directory under other names. It does not upload the ZIP.
- `final` requires a successful complete mechanical check, nonempty doubts and notes files, and matching frozen hashes. It records the final hash check and package assembly, then creates `MPL_84_097-145.zip` beside the package directory. It refuses to overwrite an existing ZIP. It does not certify that research notes are substantively complete and does not upload the ZIP.

## Current Library metadata helper

The unmodified current skill resources were fetched into `scripts/.library_helpers/`:

- `library_file_transfer.py` from `skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library/scripts/library_file_transfer.py`
- `library_hosted_apps.py` from `skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library/scripts/library_hosted_apps.py`

No Library content searches, downloads, or mutations were performed by the support-code author. After a successful authorized `create_library_file` call, the principal agent should invoke the metadata helper in that same code-mode invocation, with the exact original local path and exact returned Library ID. Supply the entire returned xattrs array, or `[]`, on standard input:

```bash
python3 /workspace/scratch/67d808a057eb/MPL_84_097-145/scripts/.library_helpers/library_file_transfer.py apply-xattrs /absolute/path/to/archive.zip EXACT_RETURNED_LIBRARY_FILE_ID <<'JSON'
[]
JSON
```

The displayed `[]` and identifier are placeholders; use the actual create result. Inspect the helper result before claiming metadata persistence. Do not use the helper to access sources outside the conversation's allowed scope.
