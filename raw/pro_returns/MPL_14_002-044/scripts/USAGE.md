# Mechanical packaging utility

`package_transcription.py` performs structural checks and packaging. It does not
access images, perform OCR, or certify textual accuracy or visual completeness.
Only the transcriber can certify those matters.

The default working root is this script's parent directory. It expects the 40
scan numbers 002–044, omitting 018, 023, and 043. Individual page files have the
form `pages/MPL_14_002-044_14_scanNNN.tex`. Each file carries exactly one matching
`\scanpage{N}`. The first file may carry `\cotefile{14}`; the combined fragment
receives that marker when the first file does not already contain it.

Run commands from this `scripts` directory, or supply the absolute script path:

```sh
python3 package_transcription.py assemble --partial
python3 package_transcription.py validate --partial
python3 package_transcription.py assemble
python3 package_transcription.py validate
python3 package_transcription.py freeze
python3 package_transcription.py verify --log
python3 package_transcription.py validate --require-notes
python3 package_transcription.py zip /absolute/output/MPL_14_002-044.zip
```

`assemble` leaves each page file intact. It joins their exact UTF-8 text with two
newlines and supplies a missing final newline. It refuses to run after a freeze
manifest exists. `--partial` accepts only a sequential completed prefix.

`validate` checks all required file names, the ordered scan and cote markers,
balanced braces and LaTeX environments, the absence of preamble and image/input
commands, exact CSV columns, supported element and sheet kinds, nonempty element
metadata, and `transcribed=yes` for every inventory row. It verifies that every
completed page has inventory rows and that the combined text equals assembly
from the current page files. This is structural lint, not a TeX compiler. TeX
verbatim constructs or unconventional command definitions require separate
review; the requested fragment ordinarily does not need those constructs.

`freeze` requires all 40 pages and an existing `scan NNN audited ...` line for
every page in `progress.log`. It refuses to freeze after a `context opened ...`
line. It writes 41 SHA-256 entries to `records/frozen_hashes.txt`, appends each
hash to `progress.log`, and then appends `transcription frozen <UTC time>`.
`verify --log` verifies all 41 entries and records that they remain unchanged.

Hourly checkpoints are explicitly requested by the primary agent at the proper
time. The utility does not schedule, create, or upload them automatically:

```sh
python3 package_transcription.py zip /absolute/output/MPL_14_002-044_checkpoint_01.zip --checkpoint
```

Checkpoint packaging includes all eligible authored files already present, even
before the combined transcription or audit is complete. Final packaging requires
full validation, research notes, and unchanged frozen hashes. Existing ZIPs are
never overwritten. The archive includes authored files, including records and
scripts of any text extension. It excludes input/source directories, raster
images, PDFs, previous ZIPs, symlinks, hidden files, and caches. Keep supplied
context outside the deliverables root or under the explicitly excluded `context`
directory. The PDF and raster exclusions protect the supplied sources; the
requested deliverables are text files. ZIP integrity and its SHA-256 are checked
after creation.

Library transfers and checkpoint timing remain the primary agent's responsibility.
