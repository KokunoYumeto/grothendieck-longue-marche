# Mechanical support tools

These scripts inspect written text and local work files only. They perform no OCR, read no scan images or context archive, make no manuscript readings, upload nothing, and never add `done`, `audited`, or `frozen` lines to the progress log.

## Validation

```sh
python scripts/validate.py --mode checkpoint
python scripts/validate.py --mode final --warn-unknown-macros
python scripts/validate.py --mode final --json
```

The default root is the parent of this scripts directory. `--root /absolute/path` selects a different work directory. Output goes only to stdout; redirect it to a record file when desired. Exit status is 1 for mechanical errors and 0 otherwise.

Checkpoint validation permits unwritten later pages and absent final deliverables, while flagging gaps before an already written page. Final validation requires scans 035–081 and the requested deliverables. Both modes check page names and markers, braces with escaped characters and comments handled, paired environments, CSV columns and field values, one or more inventory rows for each written page, and correctly formatted `done` log lines. Combined transcription bytes must equal the page bytes joined directly, with one newline, or with two newlines. A standard preamble or image inclusion in a fragment is flagged. Unknown macro classification is advisory because standard LaTeX and TikZ have extensive vocabularies.

Freeze checks accept SHA-256 lines in these forms (substitute actual digest):

```text
<64-hex-digit digest>  pages/MPL_72_035-081_72_scan035.tex
SHA-256 MPL_72_035-081_transcription.tex <64-hex-digit digest>
```

Write all required digests before `context opened ...`; the validator then compares them with current bytes. The exact required log forms are:

```text
2026-11-14 23:30:22 UTC
72 scan 035 done YYYY-MM-DD HH:MM:SS UTC
scan 035 audited YYYY-MM-DD HH:MM:SS UTC
transcription frozen YYYY-MM-DD HH:MM:SS UTC
context opened YYYY-MM-DD HH:MM:SS UTC
```

The first line above is an illustrative start timestamp. Record each real timestamp from the current UTC clock. The final post-context log statement should include `hashes unchanged`, `hashes match`, or `hashes verified`; the actual per-file comparison is also performed by the validator.

These checks cannot establish that each word, sign, insertion, deletion, drawing, or other manuscript element was transcribed, that doubt macros are placed correctly, or that the research notes are adequate. They do not replace visual audit.

The separate `MECHANICAL_REVIEW.md` records the static review of scans 035–069, proposed TikZ-CD syntax adjustments, and the observed compilation limitation: engine binaries are present, but the required format and package files are absent. No successful TeX compilation is claimed.

Additional read-only static checks are available with:

```sh
python scripts/static_tex_review.py
python scripts/static_tex_review.py --max-scan 69
```

This prints JSON diagnostics for explicit math delimiters, paired `\left`/`\right` commands, nested TikZ-CD environments, literal matrix cell separators inside macros, simple relative arrow targets, referenced empty cells, and leading subscripts/superscripts inside marking macros. It skips over escaped control symbols, macro groups, and nested environments when separating matrix cells. It performs no TeX expansion or rendering. Consumer-wide styles and macro definitions may address an advisory; inspect the actual code before changing anything. The command never edits task files.

To refresh the macro-to-inventory coverage report:

```sh
python scripts/inventory_coverage.py
```

This writes only `scripts/macro_inventory_coverage.md` and `scripts/macro_inventory_coverage.csv`. The Markdown table compares five marked-macro counts with inventory-kind counts for every saved scan. The CSV gives each call's exact source line, raw argument prefix, enclosing marked call, and corresponding inventory count. Nested calls are retained. Source hashes identify the inspected versions without making a freeze claim. Count differences are reconciliation cues; matching counts alone cannot establish element completeness.

`inventory_deletion_proposals.md` and its companion CSV map the observed deletion-count differences to specific existing record elements. They distinguish combined descriptions from separately marked children. The generator `inventory_deletion_proposals.py` writes supporting proposals only, checks the original record descriptions before using its snapshot IDs, and stops after those descriptions change. The primary transcriber reviews and applies all proposed inventory changes.

## Exact freeze verification

After the primary transcriber has recorded the freeze, run:

```sh
python scripts/freeze_verify.py --json
python scripts/freeze_verify.py --require-context --json
```

The second form is for the final check after opening context. `FREEZE_VERIFY.md` gives the full formats and scope. This helper requires exactly 47 unique audit records and 48 unique transcription hash entries, checks recorded ordering and timestamps, compares current bytes, and verifies direct concatenation. It writes no task record. Record the 48 manifest entries once; later verification uses those original entries and a separate summary statement rather than a duplicate manifest.

## Packaging

```sh
python scripts/package.py --checkpoint 1 --list-only
python scripts/package.py --checkpoint 1
python scripts/package.py --final
```

The archive is created next to the work directory unless `--output-dir` is specified. Exact names are `MPL_72_035-081_checkpoint_01.zip`, etc., and `MPL_72_035-081.zip`. Existing ZIPs are never overwritten. No ZIP is made by `--list-only`.

Final packaging refuses mechanical validation errors. Checkpoints retain work even when errors remain, reporting those errors in stdout. The first checkpoint is refused before one hour has elapsed from the progress log's initial timestamp. The operator is responsible for spacing later checkpoints hourly and for saving each ZIP through the authorized persistent storage route; this script neither schedules nor uploads checkpoints.

Packaging includes all regular work files, including records, notes, logs, and scripts. It excludes symlinks, other archives, scan/image files, Python cache files, LaTeX temporary files, and directories named `context`, `inputs`, `sources`, `attachments`, `scans`, `upload`, `uploads`, `tmp`, `temp`, `qa`, `preview`, `previews`, `rendered`, `renders`, and common cache directories. Keep supplied sources in those excluded directories or outside the work directory. Inspect `--list-only` to verify an unusual new artifact is included or excluded correctly. A CRC check and SHA-256 are reported after packaging; no completion claim or progress-log edit is made.
