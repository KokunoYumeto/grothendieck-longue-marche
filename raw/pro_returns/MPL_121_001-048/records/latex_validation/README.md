# Technical LaTeX validation

## Result

Validated at 2026-11-14 17:13:02 UTC: **43 of 43 current page files compiled successfully**. Every compiled scratch snapshot matched the current source file. The per-page SHA-256 values in `compile_results.json` agree with the independently generated `integrity_results.json` values.

The integrity check found exactly the retained scans (1–48 excluding 3, 25, 29, 38, 40), one matching scan marker in each page, the expected combined scan-marker order, balanced unescaped braces, and braced arguments for each occurrence of the permitted editorial macros. No fragment-level preamble, input, or image-inclusion command was found. The check reported no issues.

The combined transcription SHA-256 at validation was `27f80a98251c590926e0855ce159fd55970124bdbb70420b2904efbb7c7047b0`.

## Files

- `harness.tex`: temporary validation preamble and editorial macro definitions; this is separate from the transcription fragment.
- `run_validation.py`: reproducible compiler runner. It copies inputs to a scratch directory, builds a private pdfLaTeX format from installed sources when needed, and never writes to page files.
- `validate_integrity.py`: structural and hash checks, without manuscript interpretation.
- `compile_results.json`: concise results and hashes for the complete 43-page run.
- `integrity_results.json`: retained scan list, structural results, macro counts, page hashes, and combined-transcription hash.
- `SHA256SUMS`: hashes of the validated page files, combined transcription, and technical validation records.

Scratch compiler logs, source copies, generated formats, and any rendering intermediates are omitted from these records.

## Required software and packages

The complete run used pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian). The commands are `pdftex`, `pdflatex`, and `kpsewhich`, plus Python 3. Installed LaTeX base sources must provide `pdflatex.ini` and the article class. The harness loads `fontenc`, `inputenc`, `amsmath`, `amssymb`, `mathtools`, `tikz-cd`, and `geometry`; TikZ libraries are `arrows.meta`, `shapes.geometric`, `calc`, `patterns`, and `decorations.pathmorphing`.

This environment does not provide `ulem.sty`. Editorial macros, including underline and deletion markers, use transparent wrappers in this syntax harness. The `diagram` wrapper rescans its argument to support tikz-cd ampersands inside enclosing macros and supplies math mode for bare arrays.

## Scope and limitations

The result establishes successful compilation for the recorded input bytes under the supplied harness. It does not establish handwriting accuracy, mathematical correctness, complete inventory coverage, or visual fidelity. The temporary macro definitions do not test underline or deletion appearance. No source scan, context archive, or manuscript reading was delegated to this validation task. Root made all source edits.

The structural checker ignores TeX comments and escaped brace/control-symbol tokens. Compiler checks supplement that scan; neither is a substitute for the root's visual audit.

## Reproduce

From any working directory, provide a scratch output directory outside the package:

```bash
python3 /path/to/MPL_121_001-048/records/latex_validation/run_validation.py --work-dir /path/to/scratch/latex_check
python3 /path/to/MPL_121_001-048/records/latex_validation/validate_integrity.py --output /path/to/scratch/integrity_results.json
```

Both scripts locate the package relative to their own installed location; `--package-root` can override it. The compiler runner always refreshes scratch source copies and writes its new report under the selected scratch directory. It was additionally checked from its packaged location on scan 002; that reproducibility check passed.
