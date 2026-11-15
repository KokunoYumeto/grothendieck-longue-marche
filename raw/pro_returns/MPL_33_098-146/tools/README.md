# Structural validation

`validate.py` is a read-only checker for the deliverable's structure. It does
not inspect images, use OCR, interpret mathematical notation, or certify
paleographic accuracy or completeness. Every image and every inventory item
still requires the transcriber's visual examination.

Run from any directory:

```sh
python /workspace/scratch/ef44ae13eff0/MPL_33_098-146_work/tools/validate.py --partial
python /workspace/scratch/ef44ae13eff0/MPL_33_098-146_work/tools/validate.py
```

An optional directory argument selects another copy of the complete working
directory. Partial mode checks a contiguous completed prefix starting at scan
098, its inventory, and its completion records; final mode requires all 49
pages, the combined fragment, companion files, and audit/freeze/context records.

Checks include filenames and scan markers, brace and environment balancing,
fragment-only commands, inventory headers and classifications, `yes` values,
ordered completion records, required audit records, and exact concatenation of
page files (allowing whitespace only between files). Unrecognized commands are
warnings for human review, since the list of standard LaTeX/TikZ commands is
deliberately finite. This tool does not define any transcription macros.

For hash verification, create `records/frozen_sha256.json` at the freeze stage
with relative filenames as keys and hexadecimal SHA-256 strings as values:

```json
{
  "pages/MPL_33_098-146_33_scan098.tex": "<64 hexadecimal characters>",
  "MPL_33_098-146_transcription.tex": "<64 hexadecimal characters>"
}
```

Include all 49 page files and the combined transcription, not just the two
illustrative entries above. A wrapper object with this mapping in a `files`
field is also accepted. Record each relative path and its hash together on a
line in `progress.log`; keep that manifest unchanged after freezing. The checker
verifies both the file bytes and their hash entries in the log. If no manifest
exists, final-mode hash verification produces a warning rather than claiming
integrity.

Exit status is 0 when no structural errors were found, 1 when errors were
found, and the usual argparse status for invalid invocation. Warnings still
need human review. Neither exit status nor inventory `yes` values establish
that all manuscript content has been transcribed correctly.

## Mechanical LaTeX compilation

`compile_validate.py` reads a fresh snapshot of all 49 page fragments and
compiles their ordered concatenation with XeLaTeX. It never edits a page or the
combined deliverable and does not read images or context sources.

```sh
python /workspace/scratch/ef44ae13eff0/MPL_33_098-146_work/tools/compile_validate.py
```

Add `--isolate` to compile each page separately after a failed combined compile;
this can reveal independent failures without changing any source. The script
writes a concise machine-readable record to
`records/latex_compile_validation.json`, including the snapshot page hashes.
The harness, joined copy, logs, format file, and compiled temporary PDF remain
outside the deliverables in
`/workspace/scratch/ef44ae13eff0/MPL_33_098-146_compile_tmp`.

The temporary harness supplies standard AMS mathematics, TikZ/tikz-cd, font,
and graphics packages. Editorial content wrappers are streaming pass-through
commands: their braced contents are left un-tokenized until TeX reads them.
This avoids creating artificial active-ampersand errors in TikZ matrices.
Uncertainty alternatives are both retained. Underlining, deletion styling,
and other editorial decoration are deliberately not rendered by this syntax
check. Its PDF is temporary validation output, not a deliverable or a visual
audit. A successful compile does not certify the manuscript readings.
