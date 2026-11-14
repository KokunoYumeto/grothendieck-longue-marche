# Transcription compilation and layout diagnostics

The complete combined transcription passed XeLaTeX processing and PDF generation with exit status 0. The QA rendering contains 40 output pages for the 38 scan fragments. SHA-256 comparisons before and after the compilation matched for all 38 page files and the combined fragment. No source page, inventory, doubts file, or progress log was modified by this infrastructure work.

The QA PDF remains outside the deliverable tree, at `/workspace/scratch/a2a751f7911a/tex-qa/transcription/qa-check.pdf`. It is a diagnostic rendering only. No scan image or contextual text was opened during the compilation work.

## Resolved issues

- The primary reader grouped the initial absolute-value expression in a TikZ-CD cell on cote 120 scan 007, local line 7. This protected its leading vertical bar from TikZ's cell-options syntax. The infrastructure worker did not change that source.
- The QA wrapper now loads TikZ's `shapes.geometric` library for ellipse nodes.
- The system's generated default font maps are absent. Direct XeLaTeX PDF output aborted while embedding a Latin Modern symbol font. The launcher now produces XDV first, then invokes `xdvipdfmx` with the installed `lm.map` explicitly. The full PDF backend pass then succeeded.

## Remaining QA layout warning

The final stable source snapshot compiled successfully with one overfull horizontal-box warning:

| Cote | Scan | Source local lines | Excess width | Combined-line anchor |
|---|---:|---|---:|---|
| 152 | 010 | 11–20 | 0.76105 pt | 468–477 |

The final log contains no underfull-box or missing-character warnings. The remaining warning is recorded for the primary reader's visual review. It establishes that a box exceeds the wrapper's text width; visible clipping was not inspected by the infrastructure worker.

The missing-ulem fallback remains explicitly active: it uses native unbreakable underline boxes and does not reproduce ulem's word wrapping. State colours and headings are also QA conventions, as documented in the README.

### Earlier source snapshot

The first successful full compilation additionally reported excess widths of 16.17 pt on 152/001, 284.57 pt on 152/003, 64.44 pt on 152/012, 16.17 pt on 120/001, and 117.61 pt on 120/014. The primary reader subsequently changed those five page files and rebuilt the combined fragment. The infrastructure worker did not inspect or change their prose. A fresh compilation of that later snapshot succeeded, with all 39 hashes stable throughout the run; the five larger warnings no longer appeared.

The earlier warnings and compiler logs are retained with `-prior` suffixes. `logs/prior-snapshot-recheck.json` records a comparison made across those two source snapshots and therefore contains differences. The final `transcription-source-immutability.json` records the later compilation's own before/after comparison, which passed.

The successful backend still warns that the default `pdftex.map` and `kanjix.map` files are unavailable. Its explicit Latin Modern map load completed successfully, and the final backend log records all 40 output pages and a successful write.

## Durable evidence

- `logs/transcription-tex-pass.log`: complete final TeX/XDV output.
- `logs/transcription-tex-detail.log`: detailed final TeX log.
- `logs/transcription-pdf-backend.log`: successful explicit-fontmap backend output.
- `logs/transcription-launcher.log`: final end-to-end launcher result.
- `logs/transcription-source-immutability.json`: all 39 before/after SHA-256 values and their equality result.
- `overfull-report.json`: structured source-page mapping of the one remaining overfull warning.
- `overfull-report-prior.json` and logs with `-prior` suffixes: diagnostics from the earlier source snapshot.

Compilation verifies the fragment's TeX and diagram syntax under this wrapper. The primary reader separately performs the manuscript reading, completeness, notation, and visual correspondence audits.
