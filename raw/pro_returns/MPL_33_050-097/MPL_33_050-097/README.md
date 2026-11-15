# MPL_33_050-097

## Contents

This package contains the complete scan-order diplomatic transcription of Montpellier cote 33, scans 050–097, together with its uncertainty register, element inventory, research notes and work records.

| File or directory | Contents |
|---|---|
| `MPL_33_050-097_transcription.tex` | One LaTeX fragment, without preamble, containing all 48 pages in the requested order |
| `pages/` | The 48 individual page fragments |
| `MPL_33_050-097_doubts.md` | Package notation table, 384 indexed uncertainty occurrences, abbreviation expansions and legibility assessment |
| `MPL_33_050-097_inventory.csv` | 763 inventoried elements; every row marked `yes` |
| `MPL_33_050-097_notes.md` | 72 numbered research notes, manuscript admissions, title/pagination register, context comparisons and APA references |
| `progress.log` | Start time, per-page completion/audit times, freeze hashes, context-opening time and final verification |
| `records/` | Reading/audit records, context-search results, calculations, validation reports and frozen hash manifest |
| `scripts/` | Work scripts and the separate diagnostic LaTeX wrapper |

The supplied ZIP attachments, source scans and context files are not duplicated in this archive. No OCR or sub-agent was used. Every whole scan and both supplied halves were inspected, and every page underwent the requested second visual audit before the transcription was frozen.

## Reading the transcription

The fragment uses the requested editorial macros and standard LaTeX/TikZ notation. Deletions, insertions, marginal notes, uncertainty and source punctuation remain part of the text; a mathematically preferable expression is not substituted for a visible anomaly. An `\illegible{n}` occurrence denotes an estimated number of physically obscured **words**, never an omitted mathematical symbol; there are19 such occurrences, included within the 384-entry uncertainty index.

The top-level notation table in the doubts file governs the package. The first-pass `records/research_leads.md` and `records/doubt_details.md` preserve contemporaneous observations, including provisional readings that the later audit sometimes superseded; use the frozen page text, final doubts file and `records/audit_details.md` for the final reading. In particular, the provisional “ennui de signe” lead for scan 058 was revised to the uncertain degree reading documented in the final text and note N08.

The main manuscript's heading numerals 21,22,23,23 bis,24 and corrected 25 are section labels, not page totals. The fragment preserves visible numeric labels with `\mspage`; the research notes distinguish those heading labels from typed pagination and the separate lower-pencil foliation. Scan order is retained even when an argumentative continuation or reused-source pagination points to a different reading order.

## Research-note limits

Each note has its own context search in `records/context_queries.md`; only the two files actually included in the context ZIP were searched. Files merely named by the supplied results register were not available and are not represented as read. Register statuses remain the supplied runs' claims, with reviewed IDs distinguished explicitly.

Note locators use per-page TeX line numbers, labelled `L`, plus approximate positions on the image; they do not pretend that TeX line wrapping reproduces handwritten baselines. Mathematical repairs, counterexamples and reconstruction proposals are confined to the notes and identified as such. The bibliography distinguishes inspected passages from bibliographic-only or unavailable comparison sources.

## Validation and immutability

The 48 page files and combined fragment were frozen at **2026-11-15 11:14:17 UTC**, before opening the context at **11:14:30 UTC**. Their 49 SHA-256 hashes are in both the progress log and `records/transcription_sha256.txt`; the final unchanged-hash verification is recorded at the end of the work.

The combined fragment compiled successfully with XeLaTeX into a 48-page diagnostic rendering. All 23 TikZ commutative diagrams were inspected in that rendering, alongside the source audit; the separate wrapper in `scripts/validation_wrapper.tex` is a diagnostic layout, not a finished edition or an additional requested PDF. It uses colors to make editorial states visible, so its color choices are not assertions about the manuscript's ink.

To run the read-only structural checks without appending a log entry:

```bash
python scripts/verify_package.py
```

To compare against the frozen hashes and append an unchanged-hash verification:

```bash
python scripts/verify_package.py --verify
```

The historical page-recording, inventory-revision and audit scripts document the workflow; they are not a batch rebuild command and should not be rerun against the frozen text. The `--freeze` mode is intentionally guarded against a second freeze. To reproduce the context searches, place the original context contents in a sibling `context/` directory; the supplied context sources are intentionally absent from this deliverable.

