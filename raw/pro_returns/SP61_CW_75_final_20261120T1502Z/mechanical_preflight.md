# Mechanical preflight

Snapshot: 2026-11-20 14:49:50 UTC. This preflight was performed during the primary reader’s second visual reading. It is a structural check, not a reading audit or a mathematical review. No image or witness was opened by this auxiliary checker.

## Results

- All ten expected page fragments exist, each with its correct single scan marker.
- Braces, escaped characters, comments, inline dollar parity, display delimiters and environments balance. No disallowed fragment command was found. No TeX compilation was performed.
- The combined transcription matches the ordered page fragments and has exactly one leading `\cotefile{75}`.
- Required inventory and collation column names and order are correct; check-event headers are correct. All tabular rows have complete column counts.
- The 203 inventory rows cover scans 16–25, use permitted sheet/element kinds, and all have `transcribed=yes`. Inventory element IDs are unique.
- All 235 decision IDs are unique and contiguous within their scans. Every row has `against_C=yes` or `against_H=yes`; no comparison flagged as different has a final field literally identical to that witness field. This verifies the recorded flags, not the semantic equivalence of different LaTeX spellings.
- The 224 H collation rows are exactly the ordered projection of canonical decision rows flagged `against_H=yes`. Page/folder mappings, kind values, confidence values and flags are valid. No duplicate scan/place collation key was found.
- Counts in the changes report agree with the canonical table, including confidence totals and separate confidence counts by witness.
- There are 77 doubt rows, 83 unique crop keys and 23 uniquely identified check events. No required field in the decision, collation, inventory or check-event tables is empty.
- Changes, notes and hand-log reports each have sections for all ten scans. Other required reports present at this snapshot: doubts, audit and progress log.

## Counts at this snapshot

| Scan | Decision loci | Against C | Against H | High | Medium | Low | Inventory elements |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 29 | 5 | 27 | 21 | 3 | 5 | 21 |
| 17 | 21 | 3 | 18 | 11 | 4 | 6 | 16 |
| 18 | 31 | 4 | 31 | 17 | 8 | 6 | 19 |
| 19 | 37 | 4 | 37 | 23 | 12 | 2 | 22 |
| 20 | 29 | 5 | 28 | 20 | 3 | 6 | 31 |
| 21 | 32 | 4 | 31 | 20 | 6 | 6 | 28 |
| 22 | 14 | 5 | 12 | 9 | 3 | 2 | 17 |
| 23 | 16 | 2 | 16 | 12 | 2 | 2 | 11 |
| 24 | 8 | 3 | 6 | 6 | 1 | 1 | 8 |
| 25 | 18 | 2 | 18 | 11 | 3 | 4 | 30 |
| Total | 235 | 37 | 224 | 150 | 45 | 40 | 203 |

## Pending finalization items

1. `SP61_CW_75_sheet_feedback.md` was not yet present.
2. Exclude or remove `scripts/__pycache__/reading_support.cpython-312.pyc` before packaging. Setting `PYTHONDONTWRITEBYTECODE=1` on subsequent script runs prevents regeneration.
3. `transcription_hashes.sha256` was not yet present; frozen hashes were therefore not checked. This is expected before completion of the second reading.
4. The audit report had a scan 016 section at this snapshot; subsequent audit sections and timestamps were still being added by the primary reader.

## Validator limitation and correction

The first invocation reported false math-nesting errors where a minipage or `\text` suspends an outer math context. The validator was corrected to check delimiter balances independently; it makes no claim to reproduce TeX’s mode engine. `\linewidth`, `\tikz`, `\rm` and `\leftrightarrows` were added to its finite standard/package command catalogue. Eight isolated syntax fixtures passed after the change. The subsequent invocation returned only the missing feedback file and compiled cache artifact as errors, plus the expected absent-hashes warning.

No page, canonical table, or reading report was modified by this preflight.
