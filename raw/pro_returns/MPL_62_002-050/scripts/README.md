# Mechanical package utilities

These scripts perform no OCR and make no scholarly reading decisions. The validator can check the package's internal consistency; only the primary transcriber can certify coverage against the images.

## Main utility

Run from any working directory (the default root is this script's parent directory):

```sh
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py validate --stage draft
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py assemble --partial
```

`draft` validates each existing page, its inventory rows and its `done` log entry. It does not require all 46 pages or the final audit.

Once all pages are present, assemble without `--partial`. The assembly preserves page bytes and joins files in scan order with a separating newline; it never edits a page file.

```sh
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py assemble
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py hashes
```

`hashes` prints 47 log-ready records of the form `sha256 relative/path digest`. It does not append anything or declare the transcription frozen. The primary transcriber controls the audit, freeze timestamp, context opening and final unchanged-hash record.

`validate --stage complete` requires every page, every audit entry, and all named final deliverables, including research notes. `validate --stage frozen` additionally checks the freeze record and all 47 recorded hashes. The former can therefore report a missing research-note file when run at the transcription-only stage. Warnings about commands absent from the mechanical whitelist require review; they do not automatically mean that a standard LaTeX command is forbidden.

The validator checks filename/scan-marker agreement, the inventory schema and enumerated values, per-page coverage, editorial-macro arguments, braces and environments, prohibited preamble/image/alternate editorial commands, explicit uses of `illegible` in mathematical blocks, done/audit entries, and assembly equality. It cannot assess lexical or mathematical accuracy, detect every missing manuscript element, or certify that a macro's visual rendering matches the manuscript.

## ZIP creation

```sh
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py zip --mode checkpoint --output /workspace/scratch/a578466e229b/MPL_62_002-050_checkpoint_01.zip
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/package_tools.py zip --mode final --output /workspace/scratch/a578466e229b/MPL_62_002-050.zip
```

The tool never overwrites a ZIP. Checkpoint filenames must use the next unused number, and creation is refused until at least one hour has passed since the first progress-log timestamp or the latest checkpoint ZIP's modification time. A checkpoint packages all current work, even if incomplete. The final ZIP requires successful frozen-stage validation. No command uploads anything.

ZIPs include deliverables, records, logs and scripts. They exclude source-scan/context/upload directories, image crops/renders, caches, build auxiliaries, nested ZIPs and symbolic links. Keep source attachments outside the work root as already arranged.

## Current Library helpers

Fresh copies obtained from the current Library skill are in `.library_helpers/`:

- `SKILL.md`
- `library_file_transfer.py`
- `library_hosted_apps.py`

For each successful direct Library create, apply all returned xattrs and the exact returned identity in the same code-mode invocation as the create:

```sh
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/.library_helpers/library_file_transfer.py apply-xattrs ABSOLUTE_ZIP_PATH EXACT_RETURNED_LIBRARY_FILE_ID <<'JSON'
[]
JSON
```

Replace `[]` with the complete returned xattrs array. No Library write was performed during infrastructure preparation.

## Compilation syntax harness

`compile_fragments.py` compiles snapshot copies of page fragments without modifying their sources. Use `--combined` for one compilation of every currently saved page, or `--scans 25 32 36` to select individual scans. Supply an absolute `--build` directory outside the work root so temporary PDFs, copied fragments, and caches are not included in the deliverable. The harness uses identity editorial groupings and does not certify visual fidelity or manuscript accuracy. The initial successful run and the local runtime invocation are documented in `records/qa/mechanical_checks_38_pages.md`.

## Consolidation of primary-reader doubt records

`consolidate_doubts.py` mechanically regenerates the main doubts Markdown from `records/doubts.jsonl` and `records/notation.md`; it also extracts unclassified abbreviation candidates into `records/qa/`. It assigns no abbreviation expansions and includes an explicitly provisional legibility section. Run it after the primary reader's final record updates and before manually finalizing those sections, because regeneration overwrites the generated doubts file. Source records and page files are not modified.
