# Final technical validation

**Result: STATIC PASS — no concrete technical blocker found.**

Validation completed at **2026-11-17 22:27:37 UTC**. A subsequent comparison
confirmed that none of the checked input hashes changed after the validation.
This final report supersedes the initial and interim technical reports.

## Scope

The inputs were the 42 saved page `.tex` files, the combined
`MPL_138_046-089_transcription.tex`, and `MPL_138_046-089_inventory.csv`.
The exact scan set is **046 through 089, excluding 079 and 088**.

Only saved TeX/CSV sources were read. No scan images, context, or archive was
opened. No manuscript file was edited. The checks do not assert the accuracy
of readings, mathematical meaning, or the intended geometry of handwriting.

The machine-readable record is `final_validation.json`. It includes SHA-256
hashes for all 44 inputs, individual findings, command inventories, every
computed TikZ-cd endpoint, named-coordinate checks, concatenation evidence,
and the inventory checks. Its `blockers` list is empty.

## Results

| Check | Result |
| --- | --- |
| Page count and exact scan set | 42 pages; exact expected set and order. |
| Page marker consistency | Each page has its own expected `\scanpage` marker. |
| Braces, environments, group commands | No unmatched or unclosed brace, environment, `\begingroup`, or `\endgroup` found. |
| Math delimiters and modes | No remaining nested-dollar hazard, unmatched explicit math delimiter, or recognized math-only token in text found. |
| `\left` / `\right` tokens | Balanced in the final source files. |
| Command inventory | All 134 distinct control words are allowed editorial macros, recognized standard/package commands, or locally declared TikZ loop variables. |
| TikZ-cd diagrams | 21 diagrams; all 110 arrow target cells exist. |
| Construction-path coordinates | All 13 named-cell references in scan064 resolve. |
| Ordinary TikZ pictures | 17 explicit `tikzpicture` blocks; no unresolved literal named-coordinate reference found. |
| TikZ matrix separators | All 21 matrices use `ampersand replacement=\&` consistently; no conversion leaked into ordinary arrays. |
| Combined transcription | Exact ordered page bytes with one additional LF separator between adjacent pages. |
| Inventory | 612 rows, 612 unique element IDs, exact scan set, cote `138`, and `transcribed=yes` on every row. |

The combined file was checked independently by the same static mode,
structural, command, and coordinate routines. It has no findings. Counts in
this report refer to the document once, not to the duplicate checks of both
page fragments and their combined representation.

## Command review

The command lexer consumes complete TeX control sequences. In particular,
`\\f` is a row break followed by the letter `f`, not an undefined `\f`
command. The final inventory therefore avoids false positives caused by
matching the second backslash of a row-break command.

The editorial macro set checked was:

| Macro | Occurrences in the combined transcription |
| --- | ---: |
| `\cotefile` | 1 |
| `\scanpage` | 42 |
| `\unsure` | 268 |
| `\deleted` | 126 |
| `\inserted` | 54 |
| `\margin` | 15 |
| `\diagram` | 36 |
| `\figure` | 17 |
| `\uline` | 84 |
| `\uuline` | 3 |

The other control words are recognized TeX/LaTeX, AMS math/font, TikZ,
TikZ-cd, or PGF commands, together with the locally declared `\foreach`
variables `\l`, `\p`, `\r`, `\x`, and `\y`. Their declarations and uses were
checked within the loop scopes. No unknown control word or control symbol
was found. The combined transcription contains 2,822 control-word tokens.

The prescribed editorial macros still require suitable definitions when the
fragments are compiled. In particular, annotations must preserve their
caller's text/math mode and accept any saved paragraph/display arguments.
That is an external preamble contract, not an unresolved error in the saved
fragments. Five ordinary underlining calls remain in recognized math mode;
none contains the previously problematic nested dollar pair.

## TikZ endpoint details

Every relative arrow direction was converted to an absolute matrix row and
column and checked against the actual saved cells. All 110 endpoints exist.
The matrix names and construction-cell references in scan064 also resolve.

Three arrows intentionally have a technically defined empty target, because
their destination cells explicitly contain `{}`:

| File and line | Source cell | Direction | Explicit empty target |
| --- | --- | --- | --- |
| `MPL_138_046-089_138_scan049.tex:36` | Row 4, column 1 | `dd` | Row 6, column 1 |
| `MPL_138_046-089_138_scan049.tex:36` | Row 4, column 2 | `dd` | Row 6, column 2 |
| `MPL_138_046-089_138_scan053.tex:27` | Row 7, column 2 | `uurrr` | Row 5, column 5 |

“Intentionally” here refers only to the explicit node-creating `{}` in the
encoding. It does not assert a handwritten intention. These are not missing
matrix nodes and therefore are not technical blockers. The primary visual
audit owns any decision about their geometry.

The previously reported scan078 missing-cell directions are fixed in the
final snapshot. Its current arrow endpoints all resolve.

## Combined-file identity

Let `page_bytes` be the 42 unmodified page byte strings in increasing scan
order. The comparison that passes is:

```python
combined_bytes == b"\n".join(page_bytes)
```

The page files total **62,357 bytes**. The combined file has **62,398 bytes**:
the difference is exactly **41 LF bytes**, one between each adjacent pair of
pages. There are no other additions, deletions, reordered pages, or changed
page bytes. The direct concatenation without these separator bytes differs
only by those separators; this distinction is recorded explicitly in the
JSON instead of being silently normalized.

The combined file's `\scanpage` sequence exactly matches the expected 42-scan
order. The final JSON records both the expected and actual combined hashes.

## Inventory identity and status

The CSV has the expected eight columns:

```text
cote,scan,sheet_kind,element,kind,position,first_words_or_objects,transcribed
```

All 612 rows parse without missing/extra CSV fields. All 612 element IDs are
unique, and every element ID's three-digit scan prefix matches its row's scan.
Every row has cote `138` and the exact status `yes`. The set of represented
scans is precisely 046–089 excluding 079/088, with no missing or extra scan.
These are metadata integrity checks; they do not independently certify visual
transcription coverage.

## Reproduction and limits

From the project directory, run:

```sh
python technical_qa/final_validate.py
```

This reads the named page, combined-TeX, and inventory inputs and regenerates
`technical_qa/final_validation.json`. It imports the companion
`static_latex_check.py`. Both scripts are read-only with respect to manuscript
inputs. Earlier snapshots remain available for the audit trail.

**No successful compilation is claimed.** This is static validation, not TeX
macro expansion, PDF rendering, or a manuscript visual audit. TeX executables
are present, but the environment's package lookup did not find essential
format/class/package files including `latex.fmt`, `article.cls`, `amsmath.sty`,
`tikz.sty`, and `tikz-cd.sty`.
