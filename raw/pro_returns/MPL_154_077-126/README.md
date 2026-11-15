# Montpellier 154 — scans 077–126

This package contains the diplomatic LaTeX transcription of all 49 supplied
scans: 77–98 and 100–126. Scan 99 was omitted as blank in the supplied selection.
The research notes are separate from the transcription.

## Deliverables

| File or directory | Contents |
|---|---|
| `MPL_154_077-126_transcription.tex` | All 49 pages in numerical order, as one fragment without a preamble. |
| `pages/` | One fragment for each supplied scan; the combined fragment is their exact byte concatenation. |
| `MPL_154_077-126_doubts.md` | Recurring-notation table, localized reading doubts, abbreviations, and legibility assessment. |
| `MPL_154_077-126_inventory.csv` | 626 inventoried elements, all marked transcribed. |
| `MPL_154_077-126_notes.md` | 75 individually anchored research items, the two standing-question sections, contextual comparisons, and primary references. |
| `progress.log` | Page completion and audit times, checkpoint records, frozen hashes, context-opening time, and final verification. |
| `records/` | Work records, historical construction scripts, contextual search records, compilation diagnostics, and validation tools. |

## Frozen text and use of the records

The transcription was frozen at **2026-11-15 01:39:54 UTC**; the contextual
files were opened at **01:39:55 UTC**. The SHA-256 manifest is
`records/frozen_hashes.json`. All 49 page fragments and the combined fragment
retain those hashes. Contextual questions and mathematical deductions belong
only in the notes.

The page-construction and drawing scripts in `records/` are historical records,
some predating the subsequent visual audit. **Do not rerun those writers over
the final fragments.** The authoritative text is in `pages/` and the combined
fragment; the audit changes are separately recorded in
`records/audit_changes.jsonl`.

The original attachments, source images, supplied contextual texts, generated
diagnostic PDFs, and regenerable TeX caches are not included. The contextual
search records identify the supplied files and locations without duplicating
their contents.

## Checking or typesetting

From the extracted package directory, the read-only structural check is:

```bash
python records/validate_package.py --require-frozen
```

The transcription requires definitions for the editorial macros specified in
the task, together with standard LaTeX, TikZ and tikz-cd support. A separate
diagnostic harness is provided:

```bash
python records/run_compile_qa.py
```

The harness defines display conventions for the editorial macros and writes
its own output under `records/qa-build/`. Its coloring and page layout are
diagnostic conventions, not an additional manuscript edition. The environment
requirements and fallback font configuration are documented in
`records/qa_compile_README.md`; the actual checks and their limits are recorded
in `records/final_review.md`.

The notes cite scan numbers and line numbers in the frozen page fragments.
They do not renumber the manuscript's visible marginal numbers or attribute
those pencil numbers to the author without evidence. A successful compilation
or hash check is not a certificate that every difficult reading is correct;
the doubts file preserves the unresolved readings.
