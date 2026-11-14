# TeX QA infrastructure

This directory contains an auxiliary wrapper and compiler launcher. It contains no manuscript readings. Infrastructure preparation did not inspect scans, context material, or the transcription.

## Verified environment

- pdfLaTeX, LuaLaTeX, XeLaTeX, latexmk, and kpsewhich executables are present.
- The system `ls-R` files link into an absent `/var/lib/texmf`, so default package lookup fails.
- The launcher sets a process-local `TEXMF` search path without database-only (`!!`) prefixes. It does not change the system configuration.
- Prebuilt formats were absent. The launcher builds a scoped XeLaTeX format from the installed `xelatex.ini` when necessary.
- Available packages include fontspec, amsmath, amssymb, mathtools, mathrsfs, cancel, TikZ, tikz-cd, xcolor, and geometry.
- `ulem.sty`, `french.ldf`, and `stmaryrd.sty` were absent. An attempted official CTAN fetch of ulem returned HTTP 503; no downloaded package was installed.
- French accents and guillemets, script and Gothic letters, math, TikZ, and tikz-cd compiled in the synthetic smoke document.

## Run after the visual audit

```bash
python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/compile_qa.py \
  /workspace/scratch/a2a751f7911a/work/MPL_152+120_transcription.tex \
  --output-dir /workspace/scratch/a2a751f7911a/tex-qa/transcription
```

The launcher never writes to the input fragment. It passes paths as subprocess arguments, disables shell escape, runs XeLaTeX with `-halt-on-error` and `-file-line-error`, and records the complete compiler output. Its default output directory is outside `work`, under `tex-qa/build`.

The launcher produces XDV and then invokes `xdvipdfmx` with the installed Latin Modern font map explicitly. This handles the missing generated system font maps without changing system files. The full transcription's final successful compile and remaining layout warnings are recorded in `compile-summary.md` and the associated logs. TikZ's `shapes.geometric` library is included for ellipse nodes.

## QA-only rendering conventions

The wrapper loads ulem when it is available. Otherwise its `\uline` and `\uuline` fallback uses native underline boxes, with an explicit package warning. This preserves the underlining operation for a syntax check but does not provide ulem's text wrapping.

Deletion, insertion, marginal, and uncertain text receive distinct colours through unconstrained groups, so their arguments can contain prose, inline math, displays, paragraphs, or drawings. Deletion colour does not recreate manuscript strike-through. The wrapper's colours and headings belong exclusively to QA; they do not enter the transcription fragment.

The diagram and figure macros rescan their bodies so tikz-cd can establish its ampersand catcodes despite the enclosing macro argument. The synthetic test also verifies an array wrapped in `\diagram` and a drawing wrapped in `\figure`.

## Verification records

`synthetic-smoke.tex` exercises every authorized state macro, text mixed with math, a display inside a deletion, a commutative diagram, an array, and a TikZ drawing. Its final compilation exited successfully and produced one PDF page. The bootstrap and successful compilation logs are retained under `logs/`.

This infrastructure check makes no claim about manuscript completeness, decipherment, or visual correspondence. The main reader performs those checks separately.

## Nonsemantic preflight and freeze support

`preflight.py` has four subcommands. Its default root is the `work` directory containing `qa_infrastructure`; another fixture can be selected with `--root`. It outputs filenames, line numbers, counts, and structural diagnostics, with no manuscript prose.

```bash
python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/preflight.py check \
  --report /workspace/scratch/a2a751f7911a/work/qa_infrastructure/structural-check.json

python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/preflight.py build

python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/preflight.py check --require-combined

python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/preflight.py manifest

python /workspace/scratch/a2a751f7911a/work/qa_infrastructure/preflight.py verify
```

The read-only `check` command validates the exact 38 expected page filenames, cote/scan markers, required page order, literal brace and environment balance, and the inventory header, page coverage, identifiers, order, allowed values, and `yes` status. It counts each authorized state macro, including separate `unsure` and `illegible` totals and the numeric word estimates in `illegible`. TeX comments and escaped braces are excluded from the structural checks. These are lexical checks; they do not replace compilation or the visual inventory audit.

`build` first requires a successful page/inventory preflight, then preserves every source byte and joins the 38 files in the specified order with one LF between successive files. It writes only the combined fragment. It accepts an identical existing output; replacing a different earlier combined output requires `--replace`, which is for work before the transcription is frozen.

`manifest` requires the combined file and a successful preflight. It writes exactly 39 records to `qa_infrastructure/transcription.sha256`: the 38 page files in order, then the combined file. `--manifest` selects another manifest path. A different existing manifest is never silently replaced. The utility does not append timestamps or hashes to `progress.log`; the main reader makes the required freeze log entries.

`verify` checks the manifest's exact entry set/order and each SHA-256. It reads only the 39 expected target paths, ignores no mismatches, and writes nothing except an explicitly requested optional diagnostic report. A failed check or verification exits with status 1; success exits with status 0. Auxiliary report/manifest outputs are guarded against replacing page files or required deliverables.

The infrastructure smoke test (`preflight_smoke.py`) uses an isolated synthetic 38-page fixture. It exercised successful checks, exact assembly and hashing, unchanged source bytes, detection of a later byte change, unmatched braces/environments, duplicate inventory IDs, missing page coverage, non-yes rows, and missing/unexpected filenames. No active manuscript file was opened while preparing this utility.
