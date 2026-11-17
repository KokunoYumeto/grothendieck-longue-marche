# Structural validation

`validate_package.py` is a read-only validator for the five requested deliverables and the individual page files. It does not open any images or archives, perform OCR, interpret manuscript content, or change any file. Structural success does not establish transcription accuracy or completeness against the scans.

Run from the package directory:

```sh
python scripts/validate_package.py
python scripts/validate_package.py --check-log
python scripts/validate_package.py --final
```

The package directory can also be supplied as the first argument. Add `--json` for a machine-readable report on standard output. The script itself writes nothing; a caller may redirect the report into a file when desired.

## What it checks

- Exactly the 44 expected scan files: 002–046, excluding 019; each existing page's scan marker and the initial cote marker.
- UTF-8 decoding, basic TeX brace and environment balance, and absence of a document preamble.
- The combined transcription equals the **literal byte concatenation**, with no added separator, of the page files in scan order. End individual page files with their desired trailing newline(s).
- The inventory's exact column order, accepted sheet and element kinds, `transcribed=yes`, and coverage of existing pages (all 44 with `--final`). Duplicate element identifiers on a page are flagged for review.
- Presence of the doubts, notes, and progress files.
- With `--check-log` or `--final`: the initial timestamp, page completion and audit records, freeze and context-open order, and frozen SHA-256 values against current file bytes.

Provisional mode treats missing deliverables and unfinished coverage as warnings, while malformed existing material remains an error. `--final` makes missing required material an error and automatically enables log checks. Exit status is 0 when there are no errors, or 1 otherwise. Warnings still require human consideration.

The command report distinguishes the required editorial macros, recognized standard/commonly used mathematical or TikZ commands, and unclassified commands. Its recognition list is deliberately non-exhaustive; an unclassified command is a review warning, not an automatic claim that the command is forbidden. No substitution is performed.

## Progress and hash records

Expected progress labels follow the prompt, for example:

```text
136 scan 002 done 2026-11-17 14:00:00 UTC
scan 002 audited 2026-11-17 15:00:00 UTC
SHA-256 pages/MPL_136_002-046_136_scan002.tex <64-character hexadecimal digest>
transcription frozen 2026-11-17 15:05:00 UTC
context opened 2026-11-17 15:06:00 UTC
```

ISO UTC timestamps ending in `Z` or an explicit timezone offset are also recognized. A hash record must contain the exact basename and one 64-digit hexadecimal digest on the same line. Either `sha256sum` order or filename-first order works. For each required page and the combined transcription, the last hash record before the first `context opened` line is taken as the frozen reference. Later verification records cannot replace it. If context has not yet been opened, the available log is searched to its end.

The validator does not certify that timestamps describe the real work or that each inventory row exhausts the ink. Those remain the transcriber's responsibilities.
