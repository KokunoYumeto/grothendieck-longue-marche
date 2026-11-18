# Durable ZIP upload support

Prepared for the MPL_118 task on 2026-11-18. These files do not read scans,
transcription, context, notes, or inventory, and no upload was performed during
preparation.

- `library_file_transfer.py`: current Library skill helper.
- `library_hosted_apps.py`: its current optional reporting companion.
- `apply_create_result.py`: local adapter for a single direct-create result. It
  accepts the complete tool response as JSON on stdin, requires one distinct
  Library identity, invokes the skill helper with the complete xattrs array,
  and optionally writes a minimal identity record. It performs no network
  actions of its own.

Fetched from:
- skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library/scripts/library_file_transfer.py
- skill://plugin_connector_1p_1b8ff8edfc1481918b252c8277e23125/library/scripts/library_hosted_apps.py

For one already-created local ZIP below about 50 MiB, use the Library direct
create tool with its absolute path and `library_artifact_type: other`. In the
same functions.exec invocation, send the complete response to
`apply_create_result.py LOCAL_PATH --record RECORD_PATH` on stdin using a
quoted heredoc. Inspect its exit code. Retain the original response privately
if metadata persistence fails. Never upload again merely because local metadata
writeback failed.

Checkpoints are independent new files with unique names. This machinery does
not schedule, build, or upload them. The primary agent retains control of the
hourly schedule and all archival/content work.

