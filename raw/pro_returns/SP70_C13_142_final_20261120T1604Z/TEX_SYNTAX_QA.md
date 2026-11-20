# TeX lexical syntax and packaging QA

Checked: 2026-11-20 16:03:19 UTC.

## Scope

Mechanical lexical inspection of all 24 current page fragments, with the supplied `PREAMBLE.tex` as the custom-macro reference. The check distinguishes control words from escaped control symbols and ignores comments. Recognized facilities include standard LaTeX/AMS commands, the preamble's ulem and TikZ packages, and locally declared `\foreach` variables. No manuscript images were viewed, no OCR was used, no reading or mathematical interpretation was made, and no TeX compilation was performed.

## Lexical result: PASS

- Inspected 3,682 control-word occurrences, comprising 103 distinct names.
- Found no unsupported control words or remaining concatenated command names.
- The previously identified scan-044 tokens `\simeqG` and `\setminusV` are absent following the reader's separator fixes.
- `\p`, `\x`, and `\y` are declared local `\foreach` variables; their uses occur within their loop lines.
- No page TeX was modified by this QA.

This is a lexical syntax check. It does not replace the separately recorded image readings, structural validator, or final hash verification.

## Checkpoint path continuity: PASS

The candidate member selection was evaluated using the exact filter in `scripts/package.py`, without creating an archive. Every path stored in checkpoint 01 (48 files) and checkpoint 02 (80 files) is present in the current candidate. This compares retained paths; the files contain the later revisions.

The candidate contains no image files, previous ZIPs, or source-attachment directories. The package selector excludes `__pycache__` and `.pyc` files. This report is itself included by that selector.

Final freeze, the 25 recorded TeX hashes, final-mode validation, and the final archive's integrity check are separate closing gates; they were not asserted or performed by this pre-freeze lexical check.
