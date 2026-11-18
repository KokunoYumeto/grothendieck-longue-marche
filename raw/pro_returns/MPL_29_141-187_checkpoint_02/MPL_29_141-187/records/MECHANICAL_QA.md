# Mechanical QA report

Recorded: 2026-11-18 06:35:47 UTC

## Scope and result

The audited combined LaTeX fragment was compiled successfully with XeLaTeX into a private 47-page QA PDF. The PDF headers run from scan 141 through scan 187 in exact order. All 47 rendered pages were visually inspected as contact sheets, with enlarged checks of the first page, the revised inline diagram on scan 152, the revised scan 185, and earlier detailed checks of scans 176, 180, and 184. This work did not consult the source scans or the context archive, decide any manuscript reading, or perform a mathematical proof check.

The compiled combined fragment had SHA-256:

`356585ed61271981cba23de0be1e79d24649cb387a0e659c3882aa11d4a64d0c`

This is the hash of the file actually tested, not a transcription-freeze event. The primary reader owns the separate freeze and context-opening procedure.

## Structural checks

The mechanical validator passed for the current pre-freeze stage:

| Check | Observed result |
| --- | --- |
| Expected page files | 47 of 47, scans 141–187 |
| Combined fragment | Matches the individual page files in numeric order; only separator newlines are ignored |
| Inventory | 787 rows; all 47 scans covered; every row marked `yes` |
| Completion log entries | 47 scans |
| Second-audit log entries | 47 scans |
| Frozen/context markers at this validation | 0 / 0 |
| Brace and environment checks | No unmatched braces or environments found |
| Diagram/drawing wrapper coverage | Every `tikzcd` is inside `diagram`; every `tikzpicture` is inside `diagram` or `figure` |
| Global custom macros beyond the requested set | None found |

The control words `x` and `y` used as local TikZ `foreach` variables are not additional global transcription macros. No preamble, input, include, or macro-definition commands occur in the page fragments.

The validator's only stage-appropriate warnings were the absence of the freeze marker and of the research-notes file, since this check took place before that phase. The primary reader's audit entries were checked as log records; this mechanical pass did not itself audit the source images.

## Compilation and rendering

The final compilation returned exit status 0. The final log contains no TeX errors and no missing-character warnings. A geometry check of text blocks and vector paths found no content extending beyond any physical PDF page boundary. The final combined PDF was rendered through Poppler for visual inspection.

Five small paragraph overflows remain beyond the nominal text block, all inside the physical page and without clipped text:

| Scan | Maximum overflow beyond text block |
| --- | --- |
| 148 | 10.06 pt |
| 153 | 3.95 pt |
| 161 | 9.38 pt |
| 167 | 7.82 pt |
| 169 | 3.26 pt |

The thin black bars at those paragraph ends are the QA wrapper's explicit overfull-line diagnostics. They are not characters in the transcription. The wrapper uses a basic native underline fallback because `ulem` is not installed; that fallback cannot wrap a single underlined phrase across lines.

Scan 176's wide lower drawing initially clipped at the right page edge. The wrapper now scales an oversized drawing proportionally to the available line width; the corrected rendering is fully on the page. Scan 184's nested diagrams render within the page. Its dense crossing strokes and label regions were not rearranged or interpreted. Scan 180's explicitly baseline-positioned circled word now remains inline. Scan 152's curved arrow compiles inside the surrounding mathematical display and the required `diagram` wrapper.

## Wrapper-only adaptations

All QA-only definitions are in `scripts/latex_qa.py`; they do not alter page-file content. The wrapper supports long paragraph/display arguments in deletion, insertion, and margin macros; uses visible colored revision boundaries for QA; retokenizes captured TikZ separators; handles arrays, nested diagrams, and explicit surrounding math mode; preserves inline TikZ baseline placement; and proportionally fits oversized drawings. These are rendering conventions for verification, not additions to the diplomatic fragment.

The primary reader separately applied the source-level typesetting repairs that this pass identified: protection of the comma in the scan 141 arrow label; math-mode delimiters for the trailing formula and the cancelled `xi` on scan 185; and text-mode rendering of the accented word inside the scan 171 math array. The final combined compilation includes those repairs.

## Reproducibility and limits

The runtime had XeTeX installed but no initialized format. A private XeLaTeX format was built from the installed `xelatex.ini` and LaTeX sources, without package installation or network access. The final compiler log is retained alongside this report as `qa_compiler.log`. The QA PDF and rendered PNGs remain scratch verification products and are not part of the requested PDF-free deliverable set.

A successful compilation, a complete inventory schema, and a clean page-boundary check do not establish transcription accuracy, semantic completeness, faithful placement against the manuscript, or mathematical correctness. No check event should be classified as a proof check on the basis of this report.
