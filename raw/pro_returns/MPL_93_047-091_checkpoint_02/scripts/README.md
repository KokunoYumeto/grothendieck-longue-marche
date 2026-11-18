# Structural validation and packaging

`validate_package.py` uses only the Python standard library. It checks filenames,
page and cote markers, page order, exact concatenation of page files, required
deliverable names, inventory columns and element identifiers, and `transcribed`
values. It rejects document preambles and embedded-image commands in the
transcription fragments. The task's `typed` sheet classification is accepted.

Run from the deliverable folder, or supply its absolute path as the first
argument:

```bash
python3 scripts/validate_package.py
```

For a partial checkpoint, completed pages must form the initial sequential
subset of the 42 requested scans. The research-notes file may still be absent;
the other bookkeeping files, including a header-only `CHECK_EVENTS.tsv`, must
already exist. The combined transcription must equal the byte concatenation of
all saved page files even in partial mode.

```bash
python3 scripts/validate_package.py --partial
python3 scripts/validate_package.py --partial --output ../MPL_93_047-091_checkpoint_01.zip
```

After all work is finished:

```bash
python3 scripts/validate_package.py --output ../MPL_93_047-091.zip
```

The ZIP contains relative file paths without an enclosing folder. Packaging
includes deliverables, documentation, logs, and scripts. It excludes supplied
input/context directories, image files, hidden directories, caches, all ZIPs,
and earlier checkpoint files. It refuses to overwrite any existing output ZIP
and checks the completed archive's CRCs. Saving the ZIP to persistent storage
remains a separate step for the primary agent. No checkpoint schedule is imposed
by this utility; the primary agent follows the user's once-per-hour rule.

This is a structural validator, not a visual or mathematical reviewer. It does
not compare with scans, decide whether a reading is correct, establish that an
inventory is complete, distinguish archive foliation from manuscript numbering,
or certify a research claim. Those remain the primary agent's tasks. The script
does not modify transcription, inventory, doubts, notes, or progress files.

## Optional mechanical LaTeX parsing

`compile_fragments.py` creates temporary wrappers and runs LuaLaTeX (or XeLaTeX)
against each saved page fragment. It leaves all transcription files untouched.
Supply a scratch path **outside** the deliverable folder:

```bash
python3 scripts/compile_fragments.py --through 75 --scratch ../tex_qa
```

The wrapper loads standard mathematical and TikZ packages and defines only the
task's custom macros. Underlining and textual state macros use identity
definitions because this is a syntax check, not a faithful rendering check.
The diagram macro supplies display math for array bodies and rescans its body so
that TikZ can tokenize matrix ampersands correctly. Neither accommodation
requires changes to the transcription fragments.
The current environment has no `ulem` package. Generated wrappers, PDFs, logs,
and a sanitized syntax report stay in scratch. Reported errors include file and
line locations but omit the compiler's source-prose context lines. A successful
parse says nothing about the correctness of a reading or a mathematical claim.

The current installation also lacks prebuilt engine format files. A XeLaTeX
format can be generated entirely in a separate scratch folder by running
`xetex -ini -etex -jobname=xelatex -progname=xelatex xelatex.ini` there. Pass the
resulting format explicitly with `--engine xelatex --format /absolute/scratch/xelatex.fmt`.
This requires no change to the transcription or system TeX configuration.
XeLaTeX runs with `-no-pdf`, producing XDV syntax output and avoiding unrelated
PDF-driver/font errors.
