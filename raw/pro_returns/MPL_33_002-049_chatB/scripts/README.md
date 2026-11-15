# Structural validation

Run from any directory:

```sh
python /workspace/scratch/5cd8a8eb2f86/MPL_33_002-049_work/scripts/validate_structure.py --partial
python /workspace/scratch/5cd8a8eb2f86/MPL_33_002-049_work/scripts/validate_structure.py
```

The optional positional argument changes the deliverable root. `--partial`
permits unfinished scans and missing final files, but still reports malformed
existing files. Exit status is 1 for errors and 0 otherwise; warnings require
human review.

Checks cover page filenames, scan markers and order, the combined fragment,
balanced braces with escaped braces and comments handled, forbidden preamble
or image commands, editorial macro arguments, CSV structure and coverage, and
the presence of final deliverables. Unknown LaTeX commands are warnings because
standard LaTeX and TikZ commands cannot be exhaustively recognized by a small
static list. No content is changed.

For frozen hashes, write a conventional SHA-256 manifest with one line per file:

```text
<64 hexadecimal digits>  pages/MPL_33_002-049_33_scan002.tex
```

Paths in the manifest are relative to the deliverable root. Automatic manifest
locations are `records/frozen_hashes.sha256`, `frozen_hashes.sha256`, and
`SHA256SUMS`. Use `--manifest PATH` for another location. Every recorded hash is
compared with the current bytes; absent hash targets and changed bytes are
errors. The validator does not manufacture a manifest or assume that the
presence of some hash records proves every page was frozen.

This script never opens images, archives, or contextual source documents and
does not use OCR. Structural checks cannot establish transcription accuracy,
visual completeness, placement of insertions, or the correctness of readings.
Those checks belong to the single transcriber.

## LaTeX syntax smoke test

`smoke_latex.py` builds a temporary XeLaTeX wrapper around the 48 page files and
writes its wrapper, transcript, and input-hash metadata to
`records/latex_smoke/`. It repairs the current environment's missing format and
filename index by using an isolated generated format and explicit paths to the
installed TeX and font trees. No downloads or manuscript edits are performed.

```sh
python /workspace/scratch/5cd8a8eb2f86/MPL_33_002-049_work/scripts/smoke_latex.py
```

Editorial macros are transparent and leave the following braced group intact;
they do not consume TikZ bodies before ampersand catcodes are established.
The result checks syntax, not diplomatic styling or visual fidelity. A
successful run must have exit status zero, no input files changed during the
test, and all 48 pages listed in the compiler transcript. Reproducible `.fmt`,
`.xdv`, and `.aux` files are temporary compilation products, not deliverables.

## Hourly checkpoint and final packaging

`package_deliverables.py` packages every written file under the work directory,
including page fragments, the combined fragment, notes, doubts, inventories,
logs, scripts, testing wrappers, and compiler diagnostics. It excludes supplied
scans/context/uploads, nested ZIPs, caches, and reproducible TeX binary or
auxiliary products. Its internal text manifest records every included file's
size and SHA-256 hash plus excluded paths. It never edits the work files or
uploads an archive.

```sh
python scripts/package_deliverables.py --status
python scripts/package_deliverables.py --checkpoint 1 --dry-run
python scripts/package_deliverables.py --checkpoint 1
python scripts/package_deliverables.py --final
```

The default output directory is the parent of the work directory. Override it
with `--output-dir PATH`. The first line of `progress.log` is the schedule
origin; checkpoint number N is due N hours after that timestamp. Checkpoints
cannot be created early. Both checkpoint and final archives refuse to
overwrite an existing file. Changes to included files during packaging cause
the attempt to fail, so retry at a quiet boundary. Every completed archive is
checked for ZIP CRC errors. `--status` and `--dry-run` create nothing.

For this run, the origin is **2026-11-15 12:11:35 UTC** and checkpoint 01 is due
at **2026-11-15 13:11:35 UTC**. Hourly checkpoints require a separate successful
durable save after packaging; a local packaging success does not imply upload.
