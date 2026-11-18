# MPL_64_116-157 — delivery guide

This package contains the diplomatic transcription of the 39 supplied scans of Montpellier archive cote 64, PDF scan positions 116–157, excluding the omitted blank positions 122, 130, and 142. The source images and supplied context archive are not duplicated here.

## Required deliverables

| File or directory | Contents |
|---|---|
| `MPL_64_116-157_transcription.tex` | Combined LaTeX fragment in supplied scan order; no preamble or document wrapper. |
| `pages/` | The 39 separate page fragments, with the same text as the combined fragment. |
| `MPL_64_116-157_doubts.md` | Shared notation table, assessed reading doubts, abbreviation list, legibility assessment, and a concordance of every `\unsure` occurrence. |
| `MPL_64_116-157_inventory.csv` | 655 element records, with the required eight columns and every `transcribed` value equal to `yes`. |
| `MPL_64_116-157_notes.md` | 71 short research notes, the three requested question assessments, separate inventories of self-flagged steps and title sheets/page counts, and APA references. |
| `CHECK_EVENTS.tsv` | Five-column ledger of actual checks, computations, refutations, textual uses, and carried background; verification scope is stated in each outcome. |
| `progress.log` | Start time, page completion and audit times, freeze hashes, context-opening boundary, checkpoint record, and final hash verification. |

## Transcription boundary

The principal transcriber read the whole image and both supplied halves of every retained page, in one stream, and completed a second image audit before freezing the transcription at **2026-11-17 23:29:03 UTC**. No OCR was used. The context archive was opened afterward, at **23:29:08 UTC**, solely for research.

`SHA256SUMS.txt` records the 40 frozen hashes: one for each page and one for the combined fragment. The final validation checks those same hashes. Corrections, mathematical objections, interpretations suggested by Hua's project, and alternative readings prompted by context appear only in the research notes; they do not alter the frozen text.

The inventory and validation records document the work but do not guarantee error-free handwriting recognition. The doubts file identifies the compressed marginal writing, overwritten deletions, faint signs, and disputed letterforms that deserve the closest future image audit.

## Research evidence

The main report keeps each numbered note to one to four sentences. Longer proofs and reproducible calculations are supplied separately:

- `research/analytic_checks.md` and its certificate cover principal parts, linear kernels, orientation, action conventions, explicit free-group generators, fundamental groups, and fixed points.
- `research/arithmetic_evidence.md` and its certificate cover quadratic normality, the dyadic obstruction, the ordinary-node hypothesis, integral normalization, cover charts, completions, and the fourth-division coordinate checks.
- `research/connections_hua.md` contains the detailed Legendre exact differential, Schwarzian, characteristic-three p-curvature, braid-group matrices, and finite octahedral calculation, together with credited comparisons to Hua's modernized reading.
- Independent review files state what was checked, their limitations, and any corrections requested. Context-search files preserve the comparisons and locators; earlier-run claims retain their supplied status.
- `research/check_ledger_coverage.md` and its JSON companion document event coverage and normalization provenance. `scripts/merge_check_events.py` rebuilds the master ledger from the source event files.

The certificate outputs record actual execution in this run. These are exact symbolic or finite computations, not claims that every theorem in the report has been formally verified. The external primary references and retrieval limitations are listed in the main report and `research/REFERENCES.md`.

## Structural and compilation checks

`STRUCTURAL_VALIDATION.txt` records the final structural check. The validator checks all expected pages, their concatenation, inventory fields, required deliverables, ledger columns, and frozen hashes. It does not inspect images or establish the scholarly conclusions.

The complete fragment also compiled successfully with pdfLaTeX before the freeze. The compilation logs are retained under `qa/`; the compiled PDF is not delivered because the requested object is a diplomatic LaTeX fragment, and the temporary renderer uses editorial styling and reflow.

`scripts/COMPILE_HARNESS.md` explains the wrapper, local TeX setup, and its limitations. In particular, its deletion brackets, margin placement, underline fallbacks, and page reflow are validation conventions, not a facsimile of the manuscript. The fragment itself remains independent of that wrapper.

To repeat the structural check from an unpacked package, run:

```bash
python3 scripts/validate_package.py
```

To repeat the exact algebraic certificates, run the three certificate scripts in `research/` with Python and SymPy available. The recorded environment used SymPy 1.14.0.
