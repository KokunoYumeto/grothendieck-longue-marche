# Checkpoint, freeze, and final archive commands

`package.py` performs mechanical integrity checks and archive capture. It never
reads scans or witness files, decides readings, compiles TeX, schedules work,
or uploads files. The primary reader controls checkpoint timing and durable
saving. The run began at **2026-11-20 14:04:05 UTC**; the first 45-minute
checkpoint is due at **14:49:05 UTC**. A page or section boundary is not a
checkpoint trigger.

## Read-only verification

```bash
python output/scripts/package.py validate
python output/scripts/package.py validate --complete --audits
```

The checks include the documentation schemas, expected page names, inventory
completion flags, coarse brace balance, and exact agreement between the combined
fragment and the page fragments. `--complete --audits` also requires every scan's
completion and audit events in `progress.log` and a saved audit narrative.
These checks do not certify the transcription's fidelity to the ink.

## A due checkpoint

Invoke only when the required 45-minute interval has elapsed:

```bash
python output/scripts/package.py checkpoint --number 1
```

This rebuilds the currently written deliverables, validates them, and creates
`delivery/SP59_CW_71_checkpoint_01.zip`. Use the next number for the next due
checkpoint. An existing archive is never overwritten. The archive captures the
full current output tree, including scripts, documentation, and page records.
It excludes source attachments, scans, crops, images, PDF files, old archives,
JSON records, bytecode, caches, and hidden metadata.

The command reports the exact resulting path, byte size, file count, SHA-256,
and capture time. The primary reader must then save that archive durably and
verify the save result. Local ZIP creation alone is not durable saving.

## Freeze after all second readings

After all 25 pages have been read a second time and their records are final:

```bash
python output/scripts/package.py validate --complete --audits
python output/scripts/package.py freeze
```

`freeze` requires all completion and audit records. It writes
`TRANSCRIPTION_SHA256.tsv` for the 25 page files and the combined transcription,
then appends `transcription frozen <UTC>` and every SHA-256 to `progress.log`.
It never replaces an existing frozen hash list. Repeating it while all bytes
remain unchanged merely reports that the transcription was already frozen.

To verify later:

```bash
python output/scripts/package.py verify
```

Successful verification appends `transcription hashes unchanged <UTC>` to
`progress.log`. A mismatch stops the operation and reports the changed file.

## Final ZIP

```bash
python output/scripts/package.py final
```

This requires all pages and audit records, verifies the frozen transcription,
records that the hashes are unchanged, and creates `delivery/SP59_CW_71.zip`.
It does not rebuild or change the frozen transcription. The primary reader then
saves and delivers this ZIP as the sole final download.

Both checkpoint and final commands accept `--destination /absolute/directory`
for an archive directory outside `output/`. Earlier checkpoints are never nested
inside later checkpoints or the final archive.

## Manifest and archive integrity

Each archive includes `MANIFEST.tsv`, containing relative names, byte sizes,
and SHA-256 values for every other included file. The manifest excludes its own
row to avoid a circular hash. The script writes ZIP entries from the same
captured bytes used to calculate the manifest, then checks the ZIP CRCs and every
manifest digest before reporting success. `ARCHIVE_HISTORY.tsv` names earlier
captures without embedding those archives or claiming they were durably saved.

An already-created archive can be checked without extraction:

```bash
python output/scripts/package.py verify-archive delivery/SP59_CW_71.zip
```

`python output/scripts/package.py manifest` writes only the current manifest
and its explanatory note. It does not create a ZIP, freeze the transcription,
or mark a page complete.
