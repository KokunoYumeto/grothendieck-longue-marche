# Assembly and final structural validation

**Final status:** the principal reader reviewed and ran `scripts/assemble_and_validate.py` after all 44 visual audits and reviewed corrections. The successful assembly is recorded in `records/assembly_validation.json`; read-only verification is in `records/assembly_verification.json`. The combined SHA-256 is `3f85b51570feeb779ae2fd3d9e338ea8f90078fbce6e6e406722a402d6bc8c79`. The principal reader froze the transcription at 2026-11-15 11:49:57 UTC; the write example below describes the completed assembly step and must not be used to change the frozen sources.

The script expects exactly scans 043–087 with scan 060 excluded. It validates the page filenames and scan headers, the single initial cote header, all 44 completion records, all 44 audit records and their UTC timestamps, the ordering of the completion/audit phases, inventory schema and statuses, unique element IDs, per-scan inventory-record presence, permitted control words, and the required diagram/drawing environments. Its checks use the actual source files. It performs no image or context reading.

## Validate without writing

```sh
python MPL_134-8_043-087/scripts/assemble_and_validate.py
```

The default is read-only validation. An optional `--report PATH` writes a separate JSON manifest containing the ordered source hashes and the expected combined hash. It never writes to the progress log.

## Assemble after all audits and reviewed corrections

```sh
python MPL_134-8_043-087/scripts/assemble_and_validate.py --write --report MPL_134-8_043-087/records/assembly_validation.json
```

The combined fragment is the byte-for-byte concatenation of the 44 page files in numerical scan order. The existing `\cotefile{134-8}` at the start of scan 043 supplies the combined fragment's first header. The script adds no separators, duplicate header, preamble, newline normalization, or other content. A page lacking its final newline fails validation rather than receiving a silent edit.

The program checks that its inputs remain unchanged during validation, writes the combined fragment atomically only after all gates pass, and verifies the written bytes. Its manifest is deterministic for the same inputs and mode; it adds no current-time field. The `--write` mode refuses to operate after a `transcription frozen` or `context opened` marker appears in the progress log.

## Verify an existing assembled fragment

```sh
python MPL_134-8_043-087/scripts/assemble_and_validate.py --verify-existing --report MPL_134-8_043-087/records/assembly_verification.json
```

This requires the existing combined fragment to equal the exact ordered page bytes and does not write any transcription. The separate LaTeX compiler check remains available through `scripts/check_latex.py --fragment ...`.

This script does not freeze the transcription, append hashes or timestamps to `progress.log`, open the context archive, assign confidence to doubts, or edit a notation table. Those steps remain with the principal reader.
