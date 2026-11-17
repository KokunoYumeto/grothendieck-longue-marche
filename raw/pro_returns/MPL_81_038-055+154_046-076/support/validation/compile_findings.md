# Current mechanical compilation status

The final pre-freeze combined run completed successfully at **2026-11-17 14:02:35 UTC**, after the transcription owner's second visual audit and notation concordance. It processed all **31 scans** and generated **40 PDF pages** at `manuscript_validation.pdf`.

- Source syntax errors: **none**.
- Overfull boxes: **none** in the A4 landscape validation layout.
- Missing-character warnings: **none**.
- Underfull warnings: four, in scan 057 (lines 10–123, twice; lines 128–130) and scan 062 (lines 9–36).
- Source SHA-256 hashes remained unchanged during compilation and matched again after rendering and extraction.
- No source page was edited by the support agent.

Current successful evidence: `compile_07_final_prefreeze.stdout`, `compile_07_final_prefreeze.log`, and `compile_07_final_prefreeze.json` (also copied to `compile_report.json`). The JSON includes the compiled page-file hashes.

Every PDF page is rendered at 150 dpi under `prefreeze_renders/`. Its `scan_pdf_mapping.csv` maps every scan to its PDF page range; `render_manifest.json` lists all 40 full-page PNGs. Three contact sheets cover PDF pages 1–14, 15–28, and 29–40. The support agent has not interpreted or judged their content.

The current uncertainty extraction has exact 31-file coverage, 507 `unsure` occurrences, zero `illegible` occurrences, and no malformed arguments. The complete snapshot is in `uncertainties_prefreeze.json`, also written to the current `uncertainties_full.json`. `uncertainties_review.txt` groups exact readings and alternatives by scan with page ordinal, source line, and nearest position; no confidence is assigned.

## Earlier diagnostic history



# Mechanical compilation findings

No page source was modified by the support agent. No scan or context file was opened.

## Source syntax errors reported to the transcription owner

| Source scan | Exact source line | Token sequence | Diagnostic |
| --- | ---: | --- | --- |
| 058 | 41 (reported at enclosing close on 42) | `\deleted{\unsure{\chi}}` | Math-only `\chi` encountered in text mode; `Missing $ inserted.` |
| 061 | 23 | `\deleted{\unsure{\ell}}` | Math-only `\ell` encountered in text mode; `Missing $ inserted.` |

The owner must supply the intended explicit math delimiters. These are token-context errors; this support work makes no judgment about the manuscript readings.

## Coverage and retained evidence

The combined run processed scans 046–057 and stopped in 058. Individual runs then tested scans 059–076: all passed except 061. Thus 29 scans passed their initial compilation path; the two source errors above require correction and another combined run.

- Initial combined diagnostics: `compile_01.stdout`, `compile_01.log`, `compile_01.json`.
- Extended-context combined diagnostics: `compile_02.stdout`, `compile_02.log`, `compile_02.json`.
- Remaining scans: `individual/scanNNN_validation.stdout`, `.log`, and `.json`.
- Machine-readable per-page summary: `individual/summary.json`.

The failed combined run caused the XeTeX PDF driver to abort after the TeX error. The partial `manuscript_validation.pdf` from that run is not a valid complete deliverable.

## Nonfatal layout diagnostics

- Scan 053: underfull listing paragraphs at source lines 50–56.
- Scan 057: overfull boxes of 0.18268 pt and 48.92114 pt within the paragraph spanning source lines 10–123; underfull listing paragraphs also reported.
- Scan 062: one 63.89702 pt overfull box and one underfull box.
- Scan 073: one underfull box.

No missing-character warnings occurred in the individual runs for scans 059–076. Layout warnings describe the external validation wrapper's current layout; they do not establish transcription errors.
