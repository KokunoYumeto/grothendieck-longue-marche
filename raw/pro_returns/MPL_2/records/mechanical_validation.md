# Mechanical validation

`scripts/validate_bundle.py` checks delivery structure without opening any scan image, source archive, or context material. It does not establish the accuracy, completeness, or fidelity of a transcription.

Run from any directory:

```bash
python /workspace/scratch/43cfb5ca9c07/MPL_2/scripts/validate_bundle.py --partial
python /workspace/scratch/43cfb5ca9c07/MPL_2/scripts/validate_bundle.py
```

Use `--json` for a structured report, or `--root PATH` to inspect a relocated bundle. The script writes no files. Exit status 0 means no mechanical errors; 1 means one or more errors. Warnings do not change the exit status.

The complete mode checks the required 41 page filenames and order (scans 002–045 except 006, 027, and 031), page markers, the opening cote marker, unescaped brace balance, excluded preamble/image/external-input commands, CSV schema and element identifiers, allowed inventory kinds, all `transcribed` values, exact page content in the combined fragment (allowing whitespace between files), required deliverable presence, and page-completion log entries. Partial mode permits unfinished missing deliverables but still checks every present page and inventory row.

Once a `transcription frozen YYYY-MM-DD HH:MM:SS UTC` line exists, the script additionally checks audit coverage/order, audit/context timestamp order, and each page's and the combined fragment's current SHA-256 against the recorded values. The canonical hash-record format is:

```text
sha256 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef pages/MPL_2_2_scan002.tex
```

Replace the example digest with the actual digest; one such line is required for every page and `MPL_2_transcription.tex`. Conventional `sha256sum` lines and `sha256 relative/path HEX` are also recognized. A final line containing `hashes unchanged` suppresses the reminder to record the closing verification.

Limitations: brace handling is lexical rather than a TeX engine; verbatim environments and deliberately altered TeX category codes are outside its scope. It does not compile LaTeX, interpret mathematics, compare marks against images, infer omitted elements, verify whether inventory elements match the manuscript, judge doubt marks, evaluate research notes, or validate statements about the archive. It does not open or read source images or the context ZIP. The primary reader alone must perform all manuscript readings and audits.

## Structural compilation during the second visual audit

At the administrative check with 41 page files and 853 inventory rows, partial validation passed with no errors or warnings. Environment nesting was balanced throughout. The macro vocabulary consisted of the requested editorial macros, standard LaTeX/AMS commands, TikZ/TikZ-CD commands, and the TikZ-local loop variable `\a`; no additional editorial macro was identified. This was a mutable snapshot, before the transcription freeze.

`scripts/compile_structure.py` provides a reproducible temporary compilation harness. XeTeX/XeLaTeX and the necessary AMS/TikZ packages are installed. The environment's default TeX filename database and dumped formats were absent; the harness enables direct package lookup and builds its format in a temporary directory. It never edits page files and never opens images or the context archive. Its wrapper definitions are deliberately neutral, so this is a syntax check rather than a preview of the final editorial styling.

```bash
python MPL_2/scripts/compile_structure.py
python MPL_2/scripts/compile_structure.py --scans 12 25 --mixed-wrapper-boxes
```

The initial pass, followed by checks with the required TikZ decoration and ellipse libraries loaded, compiled 39 of 41 pages with neutral wrappers. Two passages depended on the eventual editorial-macro definitions: scan 012, lines 36–37 in that snapshot, contained `\uuline{$...$}` inside a display; scan 025, line 28, contained an `\inserted{...}` argument mixing text and dollar-delimited math inside a display. Both pages compiled unchanged with mode-aware wrappers that place these mixed arguments in text boxes. The optional `--mixed-wrapper-boxes` flag reproduces that check. These findings concern TeX encoding only and do not imply a manuscript reading or a mathematical correction. No unconditional syntax blocker was established by these checks.

All temporary compilation files remain outside the deliverable directory. Any later source edits require a fresh check. This harness neither preserves editorial styling nor verifies diagram appearance or drawn geometry.

### Later mutable snapshot: all pages compile with neutral wrappers

Following the primary reader's encoding changes to scans 012 and 025, a fresh check compiled all 41 page files with neutral wrappers, without `--mixed-wrapper-boxes`. No page changed while its individual compilation was running. Partial mechanical validation still passed for 41 files and 853 inventory rows. These checks preceded the final freeze and do not supersede the required visual audit.

A mechanical comparison of notation strings identified the following targets for the primary reader's visual comparison; none is an asserted reading error:

| Comparison target | Recorded LaTeX locations in that snapshot |
|---|---|
| Alphabet of Z and Q | `\mathbb Z` on scans 021–025 and 028; `\mathbf Z` on 024 and 043; `\mathbf Q` on 041. |
| Limit signs | `\underline{\lim}` on scan 033 line 13 and 038 line 9; arrow-under-limit constructions on 033 lines 12 and 26, 034 line 4, and 036 line 7; `\varinjlim` on 038 lines 12 and 23. |
| Prime versus exclamation exponent | The alternative `\widetilde u'|\widetilde u^!` is explicitly marked on scan 021 line 37. Direct apostrophes encode primes; no `\prime` macro was present. |
| Exclamation position | `A!|A^!` and `CK!|CK^!` are explicitly marked alternatives on scan 030 lines 8 and 15. The source strings distinguish `i_!` from `i_*`, and `f_!` from `f_*`. |

The Greek-command inventory used `\varepsilon` without `\epsilon`, and `\varphi` without `\phi`; this statement concerns command names only and does not determine whether Latin-letter or other readings match the ink. Prose quotation strings used paired backticks/apostrophes; mathematical double primes were retained as apostrophes. The mechanical comparison made no normalization, source correction, or mathematical inference.

## Independent frozen-transcription metadata audit

Audit time: 2026-11-16 21:23:02 UTC. Read-only checks were made against the current bundle while the primary reader was completing the research-note assembly. No manuscript images were inspected; no page file, combined fragment, inventory, doubts file, or progress log was edited, and no assembly command was run.

| Check | Observed result |
|---|---|
| Required page set | Exactly 41 page files: scans 002–045, excluding 006, 027, and 031; no extra `.tex` page file. |
| Combined fragment | Exactly the direct byte concatenation of the 41 ordered page files, with no inserted or changed bytes: 71,569 bytes in both forms. |
| Inventory schema | Exact required column order: `cote,scan,sheet_kind,element,kind,position,first_words_or_objects,transcribed`. |
| Inventory completion | 856 data rows; all 856 have `transcribed=yes`. All page references, cote values, element kinds, identifiers, and required fields pass the existing validator. |
| Sheet classification | Each scan has one consistent allowed sheet kind: 22 `text`, 5 `cover`, 14 `reused_typed`, 0 `cancelled_draft` pages. These are metadata counts, not an independent visual confirmation of classification. |
| Frozen digests | All 42 required SHA-256 records—41 pages plus the combined fragment—match the current file bytes. |
| Completion and audit records | Exactly 41 page-done entries and 41 visual-audit entries in the required scan order. The last audit precedes the freeze. |
| Freeze/context order | `transcription frozen 2026-11-16 20:56:22 UTC` is log line 129, followed by `context opened 2026-11-16 20:56:22 UTC` at line 130; all frozen digest records precede the freeze. Equal second-resolution timestamps do not reverse that recorded order. |
| Initial progress timestamp | First line is `2026-11-16 19:40:49 UTC`. |
| Notation table position | The package notation table is the first substantive section of the doubts file, preceding the doubt register; it has 30 entries. |
| Doubt register | 280 grouped doubt entries, with the required columns; every confidence value is exactly `high`, `medium`, or `low`. |
| Abbreviations | A separate doubts-file section has 37 entries and labels expansions as editorial hypotheses; no glossary/preamble was inserted into the transcription. Preservation of individual manuscript abbreviations remains a visual/content responsibility, not something this metadata audit certifies. |
| Legibility statement | Present after the abbreviation section, with explicit limitations and a distinction between foliation and page-count statements. |
| Existing validator | `--partial --json` passes with no errors. Its sole warning is the absent final `hashes unchanged` statement, expected to be added only after the primary reader's closing verification. |

Page classifications recorded in the inventory:

- `cover`: 002, 009, 020, 032, 040.
- `reused_typed`: 011, 013, 015, 023, 024, 025, 026, 033, 034, 035, 036, 037, 038, 039.
- `text`: 003, 004, 005, 007, 008, 010, 012, 014, 016, 017, 018, 019, 021, 022, 028, 029, 030, 041, 042, 043, 044, 045.

Inventory element counts: 316 text blocks, 163 displays, 15 diagrams, 15 drawings, 74 margin notes, 97 insertions, and 176 deletions (total 856). These counts describe inventory rows rather than every nested macro occurrence; one row can document a compound element. The research notes and final ZIP were outside this audit's completeness claim. All required deliverable filenames were present at the time of inspection, but ongoing notes assembly was not treated as finished merely because its filename existed.

## Closing verification — 2026-11-16 21:27:18 UTC

The primary reader repeated the exact byte-concatenation and all 42 SHA-256 comparisons after research assembly; every frozen digest matched. All 41 page files and 856 complete inventory entries are present. The final research file has 90 distinct note headings (80 substantive plus 10 self-flagged) and 9 title/pagination rows, with all 99 IDs covered by actual context-search records. No assembly placeholder or disallowed control character remains in the notes or doubts. The closing `hashes unchanged` statement is now recorded in progress.log.
