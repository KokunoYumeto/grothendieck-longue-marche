# Mechanical validation of MPL_133

## Exact-source compilation

At **2026-11-16 23:00:41 UTC**, the exact combined transcription compiled successfully with **exit status 0**. All **50** expected scan markers were reached, in order. No temporary substitutions were applied to the tested transcription. Its SHA-256 before and after compilation was:

```text
a6e7bb4ce96b13852d809760aa02d8d23d4062e9a686851fc2fab20ee4cf0502
```

The test used pdfTeX 1.40.26 (TeX Live 2025/dev/Debian), a locally generated LaTeX2e format, and the installed `amsmath`, `amssymb`, and `tikz-cd` sources. No packages were installed and no network data was fetched. Explicit `TEXMF` and `TEXINPUTS` paths resolved the existing TeX source tree; a format was generated locally with `pdftex -ini -progname=pdflatex '*pdflatex.ini'` and a local job name.

The temporary integration preamble used DVI mode because the environment lacked the aggregate `pdftex.map`. The compiler produced a 52-page test DVI: this is a wrapper pagination result, not a change to the manuscript's 50 scan pages. Neither the test DVI nor a test PDF is part of the deliverable.

## Scope of the test

The preamble loaded the actual mathematical and diagram packages and executed every formula, TikZ path, and `tikz-cd` construction. `\diagram` and `\figure` were noncapturing identity markers (`\let\diagram\relax`, `\let\figure\relax`). The editorial macros `\deleted`, `\inserted`, `\margin`, `\unsure`, `\uline`, and `\uuline` were permissive long identity macros, so their contents were parsed but editorial styling was suppressed; `ulem` was unavailable. `\scanpage` emitted a log marker and page break. The fragment was included directly using `\input`, without alteration or preprocessing.

This is a syntax and integration check, **not** a proof of visual fidelity, reading accuracy, completeness, or the appearance of a fully styled diplomatic edition. The mechanical reviewer did not inspect manuscript images or contextual research materials.

## Diagnostics

- Missing-character warnings: **0**.
- LaTeX or PGF warnings in the final run: **0**.
- Overfull-box layout notices: **8**, in the deliberately simple wrapper. Six concern the printed-page rules; two concern long textual/formula lines. They did not interrupt compilation.
- The scan 019 end-picture rectangle using `\tikzcdmatrixname` and the scan 037 headless-hook options executed successfully.

Earlier test runs identified math-mode guards for array diagrams; ambiguous leading brackets after `aligned` or a row break; accented text used directly in mathematical font commands; the missing upper-right matrix column in scan 042; and ampersand tokenization inside editorial macros. The primary transcriber applied the repairs before this final exact-source test. The scan 042 geometric decision was made by the primary transcriber against the image, not by this mechanical review.

A separate font probe established that, with the standard AMS fonts, `\mathbb{\Omega}` selects AMS-B slot 10, whose installed font metric names the glyph `notlessorslnteql`; it does not render an outlined Omega. This substitution produces no missing-character warning because the unrelated glyph exists. After reviewing the ink, the primary transcriber replaced the three scan 027 occurrences with literal double-contour TikZ constructions. Those constructions compiled in the final exact-source run.

## Package consistency before freezing

The read-only partial validator passed with **50 page fragments**, **809 inventory elements**, **50 distinct inventory scans**, **50 completion timestamps**, and **50 audit timestamps**. It reported no errors or warnings. Its checks include exact byte concatenation of the individual pages, basic TeX grouping/environment consistency, required inventory categories, and completion records. Transcription freezing and the final post-research hash comparison are separate stages recorded in `progress.log`.

No manuscript page, page record, or contextual source was modified by the mechanical reviewer during compilation. Earlier authorized administrative changes normalized inventory categories only and preserved each record's transcription, doubts, observations, and element text.
