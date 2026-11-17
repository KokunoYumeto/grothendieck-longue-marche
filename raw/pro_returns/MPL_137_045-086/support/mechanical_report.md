# Mechanical structural report

## Scope and limits

This report records structural checks of the 42 LaTeX page fragments for scans
045–086, their combined transcription, the inventory CSV, and audit markers in
`progress.log`. The initial editorial check was recorded on 2026-11-17 at
21:33:38 UTC. After the root transcriber's final notation edits and the freeze at
21:38:33 UTC, the page/concatenation/inventory, brace/environment/diagram, and
43-hash checks were rerun successfully on the frozen snapshot. The macro counts
below have likewise been refreshed from the frozen text.

The checker did not open scan images, the scan archive, or the context archive.
It did not assess manuscript readings, mathematical meaning, completeness against
the images, source order within a visual block, or the correctness of diagram
objects and arrows. No page text was changed by the checker.

## Results

| Check | Result for the checked snapshot |
|---|---|
| Expected page fragments | All 42, scans 045–086 |
| Scan markers | One correct marker per page |
| Combined transcription | Byte-for-byte concatenation in scan order |
| Fragment opening | Required cote and first scan markers present |
| Braces | Balanced on every page; the earlier scan070 issue is resolved |
| Environments | 64, all balanced |
| `tikzcd` environments | 41 |
| Arrow commands | 179 |
| Math delimiter checks | No unmatched `\[…\]` or `\(...\)`; even unescaped-dollar counts |
| Arrow option checks | No detected unclosed options or escaped apostrophe suffixes |
| Known extra macro dependencies | No findings |
| Forbidden image commands and placeholder patterns | No findings |
| Inventory | 794 rows covering all 42 scans; every `transcribed` value is `yes` |
| Inventory identifiers | No duplicate `(cote, scan, element)` keys |
| Inventory scan order | Monotone, with no backward scan transition |
| Sheet classifications | Consistent within each scan |
| Audit log markers | 42 entries for 42 distinct scans |
| Freeze verification | 43 matching SHA-256 hashes: 42 pages plus combined transcription |

The control-word scan found the permitted editorial macros and familiar standard
LaTeX/AMS/TikZ commands. This is a lexical check, not proof that every command is
valid in its particular mathematical or diagram context.

## Editorial macros and doubt notation

The frozen snapshot contains one `\cotefile`, 42 `\scanpage`, 821 `\unsure`,
219 `\deleted`, 102 `\inserted`, 38 `\margin`, 60 `\uline`, 3 `\uuline`,
41 `\diagram`, 8 `\figure`, and 2 `\illegible` occurrences. No `\mspage`
occurrence was detected; the checker makes no judgment about whether a handwritten
page number is present in an image.

All detected editorial commands have braced arguments. Both `\illegible`
arguments are positive integer word counts, and neither occurrence is detected
inside math or TikZ contexts.

No raw ASCII double quote or typographic double-quotation character was detected
outside TikZ syntax. The lexical count found three unmatched closing `''` pairs:
scan045 line 30, scan054 line 3, and scan067 line 15. The root transcriber reported
that these are intentional source notation: the first two occur in formula
references, and the third preserves closing quotation strokes. The checker did
not verify that explanation against the images and did not alter the marks.

The detailed earlier editorial-token output is in
`pre_freeze_editorial_checks.json`; that historical snapshot predates the final
notation doubts and therefore contains the earlier `\unsure` count of 576.

## Inventory granularity

Counts of `\diagram`, `\figure`, `\margin`, and `\inserted` match the inventory
counts for their corresponding element kinds. The remaining count differences
are confined to deletion markup:

| Scan | `\deleted` occurrences | Deletion inventory rows |
|---|---:|---:|
| 046 | 14 | 8 |
| 050 | 6 | 5 |
| 052 | 11 | 5 |
| 053 | 17 | 5 |
| 059 | 17 | 5 |

A cancelled block or diagram can require several `\deleted` commands to render
one visual cancellation. Counts alone therefore do not establish an omission.
Whether the grouped inventory entries cover the visual elements is a question
for the root image audit; it was not adjudicated mechanically.

## Compilation limitation

The executables `pdflatex`, `lualatex`, `xelatex`, and `latex` are present, but
`kpsewhich` could not locate `article.cls`, `latex.ltx`, `pdflatex.fmt`,
`amsmath.sty`, `tikz-cd.sty`, or `ulem.sty`. No packages were installed and no
network retrieval was attempted. Consequently no full TeX compilation or rendered
layout check was performed.

`compile_wrapper.tex` is an uncompiled, temporary syntax-check wrapper. It is not
a proposed edition layout. It makes the editorial macros transparent and sets
the ampersand catcode before reading a `\diagram` argument. Its behavior remains
untested in a working TeX installation.

Static checks cannot establish that TikZ arrow destinations exist, that the full
PGF option grammar is satisfied, or that diagram geometry reproduces the source.

After freezing, the wrapper's `\unsure` definition was adjusted to expand to a
braced group. This supports use immediately after a math script marker, as in
the cancelled notation on scan086, without editing any frozen fragment. The
wrapper remains uncompiled; this is a support-layer adjustment only.

## Frozen-hash verification

After the root transcriber recorded the freeze at **2026-11-17 21:38:33 UTC**,
`validate.py --hashes support/frozen_hashes.json` verified **43 matching hashes**:
the 42 page fragments and their combined transcription. The structural check
passed with 794 inventory rows. This verification did not inspect images or
validate manuscript readings.

## Reproducible checks and final packaging

Run these from the parent workspace:

```bash
python -B MPL_137_045-086/support/validate.py
python -B MPL_137_045-086/support/static_tex_checks.py
```

After the transcription is frozen, pass its hash manifest or conventional
SHA-256 log entries:

```bash
python -B MPL_137_045-086/support/validate.py \
  --hashes MPL_137_045-086/progress.log
```

`pack_final.py` is available for final packaging after notes and freeze records
exist. It validates the required files, audit-before-freeze ordering,
freeze-before-context ordering, and unchanged hashes before creating the final
ZIP. It never creates checkpoints. Packaging has not been performed by this
checker.
