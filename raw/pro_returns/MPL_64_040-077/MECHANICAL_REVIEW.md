# Mechanical review of the first-pass transcription

Review time: 2026-11-17 22:45:34 UTC

Scope: syntax and file consistency only. This review did not inspect any scan, crop, source archive, or context contents and did not assess manuscript readings or mathematics. A temporary copy of the first-pass files was inspected while the primary transcriber began the visual audit. Later visual-audit changes are outside this snapshot.

## Checks completed

- All 38 expected page filenames exist, for scans 040–077 of cote 64.
- Each page contains its own expected scan marker; the combined markers occur in order.
- The combined transcription is byte-for-byte the concatenation of the 38 page files as decoded in UTF-8, without extra separators.
- Grouping braces balance in every page. All 30 begin/end environment pairs match and nest consistently.
- Token-aware checks found no unmatched display or inline math delimiters. Per-page dollar counts are even; left/right delimiter counts agree.
- The 9 tikzcd diagrams have structurally consistent matrix rows and relative arrow targets in the encoded text.
- The inventory has 616 rows, covers every expected scan, uses only the requested column names and valid kind/sheet_kind values, has no duplicate (cote, scan, element) keys, and has transcribed=yes in every row.
- The progress snapshot has one done record for each of the 38 scans. No audit or freeze events were created by this review.
- The doubts file contains the required notation, doubts, abbreviations, and legibility headings. Its Markdown tables have consistent column counts. Its 191 doubt rows all use high, medium, or low confidence.
- The macros found are the authorized annotation macros or recognizable standard LaTeX/package commands. The fragment needs ordinary support for amsmath, amssymb, mathrsfs, graphicx, and tikz-cd, as well as definitions of the requested annotation macros.
- All Python scripts present when inspected parsed without Python syntax errors.

The final-package validator reported only the missing research-notes file; that file is not expected until after the transcription is frozen and the context is opened.

## TikZ matrix portability

All nine tikzcd environments are passed inside the argument of the requested diagram macro. Under a conventional one-argument definition of that macro, literal ampersand column separators have already been tokenized before TikZ can assign its normal matrix ampersand catcode. The portable encoding is to set `ampersand replacement=\&` on each tikzcd environment and use `\&` for that environment's column separators.

The prepared `scripts/tikzcd_portability.py` prints a unified diff by default and changes files only with `--apply`. It preserves ampersands in nested array/aligned/gathered environments, leaves all non-diagram content alone, regenerates the combined file from the pages only when applied, and refuses changes after a recorded transcription freeze. This review prepared that script but did not execute it.

## Annotation-count differences for the primary auditor

These are mechanical counts, not findings of omitted manuscript content. An inventory element can group several nested annotation macros, and the primary auditor must decide whether the inventory describes each actual element sufficiently.

| Scan | Annotation | Macro occurrences | Inventory rows |
|---|---|---:|---:|
| 050 | deletion | 7 | 6 |
| 050 | insertion | 4 | 3 |
| 051 | deletion | 12 | 10 |
| 053 | deletion | 15 | 14 |
| 055 | insertion | 5 | 6 |
| 056 | deletion | 8 | 7 |
| 068 | deletion | 7 | 6 |
| 076 | deletion | 6 | 7 |

## Compilation limitation

A temporary XeLaTeX wrapper was prepared with pass-through annotation definitions so that custom annotation styling would not obscure syntax checks. The compilation attempt failed before document parsing because `xelatex.fmt` is absent. Targeted checks also found no pdflatex/lualatex format, latex.ltx, article.cls, amsmath.sty, amssymb.sty, mathrsfs.sty, graphicx.sty, or tikz-cd.sty. TeX executable binaries are installed, but the formats and packages required for a LaTeX compilation are not available. Therefore this report does not claim a successful compilation or rendered-page inspection.

No transcription page, inventory entry, doubt reading, progress event, audit record, or frozen hash was altered by the mechanical reviewer.


## Follow-up mechanical review during the visual audit

Review time: 2026-11-17 22:51:57 UTC

Only current TeX, inventory, doubts, and scripts were inspected. No scans, crops, images, OCR output, source archives, or context contents were accessed. No page text or audit/freeze records were edited.

### Script changes

`scripts/package_delivery.py` now additionally checks:

- exact byte equality between the combined transcription and the ordered page concatenation;
- unexpected `.tex` files in `pages/`;
- token-aware grouping braces, begin/end environments, explicit math delimiters, even unescaped dollar counts, and unescaped TeX parameter characters;
- inventory element kinds, sheet kinds, duplicate/empty element identifiers, and CSV field counts.

It also provides `--check-transcription`, a read-only validation mode that does not require the research-notes file and does not write log entries. That command passed against the files current at this review. All current Python scripts parsed successfully.

The checks remain structural and do not establish successful compilation or accuracy against handwriting. The earlier missing-TeX-formats/packages limitation remains unresolved. The prepared tikzcd portability script had not yet been applied when inspected.

### Patterns referred to the primary visual auditor

The following were present when this pass began. Their existence is a request for an ink-based decision, not evidence that they are omissions; manuscript-written ellipses must of course be retained.

| Scan | Approximate TeX line | Pattern |
|---|---:|---|
| 050 | 8 | `\unsure{a\in\{0,1,i,\ldots\}}` inside a deletion |
| 053 | 20 | `\unsure{$\Delta\ldots$}` |
| 074 | 11 | `\unsure{\ldots}` |

The abbreviations and legibility sections of the doubts file still contained their explicit end-stage completion placeholders at this inspection. No `[ ... ]`, TODO, TBD, or FIXME placeholder was found in page text. No TeX file-I/O, command-definition, shell-escape, or package-loading command was found in page fragments. Non-ASCII page characters were French text letters, section/degree signs, and apostrophes; no raw Unicode mathematical operators needed conversion.

The latest inventory read in this pass had 621 rows. The remaining annotation-count differences at that time were scan 040 insertion 3 macros / 4 rows; 053 deletion 15 / 14; 055 insertion 5 / 6; 056 deletion 8 / 7; 068 deletion 7 / 6; and 076 deletion 6 / 7. As before, grouped/nested annotations can account for count differences, so only the primary visual audit can decide whether any row needs correction.

One helper limitation was noted for the primary transcriber: `audit_record.py` currently assigns `sheet_kind=text` to every newly appended inventory element. If new elements are added while auditing a cover or reused typed sheet, their sheet kind should match that sheet rather than defaulting to text. This helper was not changed in this review.


## Final mechanical validation after reconciliation

Review time: 2026-11-17 23:05:32 UTC

This check was requested as the final pre-freeze review. By the time the progress log was inspected, its freeze event was already present. This report records the actual review timing; the reviewer did not freeze, unfreeze, or alter any transcription file, doubt entry, inventory row, or log event.

- The current combined transcription is the exact ordered byte concatenation of all 38 page files. Structural checks pass, including page markers, grouping braces, environments, and explicit math delimiters.
- All 38 page audits are recorded exactly once, with no missing scan.
- The doubts document has three contiguous Markdown tables with respectively 3, 6, and 3 columns. Every row has the correct width; escaped pipes inside code spans do not create extra columns. The tables contain 30 notation entries, 217 doubt entries, and 64 abbreviation entries. Every doubt confidence is high, medium, or low.
- No unresolved completion placeholder remains in the doubts document or inventory. The occurrences of the word “placeholder” are explanatory statements that unread text has not been replaced by placeholder dots, not unfinished fields.
- The inventory contains 624 rows, all marked yes. Its schema, scan coverage, element kinds, sheet kinds, and unique element identifiers pass.
- The primary transcriber confirms that the two remaining insertion-count differences are intentional: scan 040 has 3 insertion macros and 4 inventory insertion elements; scan 055 has 5 macros and 6 elements. In each case a long insertion is encoded as one macro while its separate page elements receive separate inventory rows. These differences are not treated as unresolved count errors.
- All 9 tikzcd environments now use the portable ampersand encoding. A read-only transformation check found zero remaining column replacements and no further edits to propose.

The earlier concerns about completion placeholders, unreconciled annotation counts, and unapplied TikZ portability are superseded by this final check. Successful LaTeX compilation is still not claimed because the required formats and packages are unavailable. No scan images or context contents were consulted.
