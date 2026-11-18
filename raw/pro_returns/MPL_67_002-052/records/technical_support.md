# Technical support record

An assistant prepared `validate_package.py` without opening source scans, the
context archive, or any transcription page. The primary reader retains sole
responsibility for transcription, notation, inventories, and image audits.

The utility provides four explicit commands. It is not run automatically.

```bash
python records/validate_package.py validate --partial
python records/validate_package.py assemble
python records/validate_package.py freeze
python records/validate_package.py verify-freeze --record
python records/validate_package.py validate --final
```

Run from the package directory; alternatively pass an absolute script path.
`assemble` concatenates the 46 required page files without changing them.
`freeze` requires an existing combined transcription and all 46 audit events
already written by the reader. It computes SHA-256 hashes, writes
`records/transcription.sha256`, and records the hashes and freeze time in
`progress.log`. It refuses to overwrite a freeze or operate after a recorded
context opening. `verify-freeze` checks all 47 frozen files, and `--record`
appends the result only after a successful comparison.

Structural validation checks filenames, scan coverage, scan markers, inventory
schema and coverage, exact `yes` flags, check-event row structure, required
files, and exact concatenation. These checks do not assess reading accuracy,
mathematical validity, or whether every visible element was inventoried.

The Library helper resources were obtained from the current `c0/library`
skill, using its resource interface. The helper and its companion are stored
outside this deliverable directory in a private temporary directory. No file
was uploaded by the support assistant.

## Optional LaTeX syntax compilation

`compile_qa.py` creates an isolated document wrapper and compiles existing page
fragments, or the already assembled combined file with `--combined`. It never
edits or assembles the source transcription. Outputs go to a separate scratch
directory, outside this deliverable tree. To select a page, use `--scan 51`;
repeat `--scan` for more than one page. `--prepare-only` writes the wrapper
without invoking TeX.

```bash
python records/compile_qa.py
python records/compile_qa.py --combined
```

The harness uses transparent editorial wrappers, including underlining,
deletions, insertions and doubt marks. It checks the underlying LaTeX and TikZ
syntax; it does not test a particular diplomatic-edition style or certify
layout. The diagram wrapper enters math mode when needed while leaving its
braced contents in the input stream. This allows an array directly inside the
requested diagram macro and preserves TikZ-CD's ability to tokenize matrix
ampersands. A synthetic test of ordinary `ensuremath` argument capture failed
for TikZ-CD; the input-stream wrapper passed arrays, TikZ-CD and use inside
existing math mode.

In this runtime, TeX binaries and package resources exist, but the default
database-only lookup lacks filename databases and prebuilt formats. The
harness uses process-local resource paths and creates a format in its scratch
output directory. It does not alter the system TeX installation. The `ulem`
package is absent; transparent underline wrappers avoid that dependency for
syntax QA. A synthetic document containing a TikZ-CD arrow, a LaTeX array,
a TikZ drawing, mathematics and verbatim text compiled successfully before
any manuscript input was compiled.

The XeTeX wrapper loads Unicode math fonts and installed Noto CJK text fonts
for the Japanese material. Strict lost-character tracing treats missing glyphs
as compilation errors. `--no-pdf` performs syntax and missing-glyph checks without
invoking the PDF driver. This runtime's `xdvipdfmx` raised an assertion for some
pages after TeX processing, so the per-page batch uses `--no-pdf` and records
that limitation explicitly. A successful syntax report is not a PDF rendering
check.

`run_compile_qa_batch.py` runs isolated per-page checks and writes a structured
report in `records/latex_qa_report.json`. Its `--changed-only` option rechecks
failed sources and sources whose hashes differ from the preceding report.

Compiler reports record return status, diagnostic locations, box warnings,
missing-character diagnostics and font-warning counts. Hash comparisons before
and after compilation report whether the selected source files changed during
the run. These checks are technical only and supply no mathematical check event.
