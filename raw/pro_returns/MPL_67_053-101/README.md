# MPL_67_053–101

## Deliverables

This package contains the complete diplomatic LaTeX fragment for the **47 supplied scans** of cote67 (53–101, excluding the supplied omissions83 and90), the47 individual page files, the notation/doubts/abbreviations file, the938-element inventory, the contextual research notes, the check-event ledger, and the chronological progress log.

| File or directory | Purpose |
|---|---|
| `MPL_67_053-101_transcription.tex` | Authoritative combined diplomatic fragment; no preamble and no embedded scan images |
| `pages/` | Authoritative individual frozen page fragments in scan order |
| `MPL_67_053-101_doubts.md` | Notation table first, then a location-indexed doubt list, abbreviation expansions confined to that list, and legibility limits |
| `MPL_67_053-101_inventory.csv` | Every inventoried element, classified by kind and sheet type; every row is marked yes |
| `MPL_67_053-101_notes.md` |100 short research notes,33 self-flagged/withdrawn-step items,12 heading/date/count entries, a36-row Hua coverage map, and primary-source references |
| `CHECK_EVENTS.tsv` | Consolidated record of what was actually checked, computed, used as background, or refuted; outcomes delimit the scope |
| `progress.log` | Start time, page completion and image audit times, notation review, freeze hashes, context opening, checkpoint and final validation records |
| `research/` | Detailed proofs, exact-computation scripts/certificates, actual per-note context searches, specialist fragments, and targeted cross-reviews |
| `records/` | First-pass working records, second image audits, notation comparison, freeze hash set, and assembly/validation records |
| `scripts/` | Work-record, doubt-index, research-assembly and package-validation scripts |
| `support/compile_check.tex` | Optional technical LaTeX wrapper defining the diplomatic macros for a syntax check; it is not a facsimile layout |
| `validation/` | Successful LaTeX compile logs and final structural/hash validation |

## Reading and uncertainty

All supplied whole images and both supplied halves were examined directly by one assistant, in scan order, without OCR. Every page received a second visual audit before the transcription was frozen. The final comparison of recurring signs and abbreviations is documented in `records/notation_audit.md` and the table at the beginning of the doubts file.

The fragment retains **450 explicit `\unsure` occurrences** and **one `\illegible{1}`** inside a cancellation. An uncertainty marker is a proposed reading with a stated limitation, not an omitted passage. Particularly difficult areas include overwritten cancellations, diagonal margins, tiny indices, and the manually transcribed computer-printout banners; the colored freehand drawings on96 are TikZ approximations and are marked accordingly. The doubts file describes these limits more fully.

Archive pencil foliation appears only in comments. The author's live numbering1–15 across scans54–82 is distinct from the47 supplied scan pages; there is no author-written total extent in this packet. Reused printed sheets92 and96 remain fully represented, including their printed matter and handwritten marks.

## Freeze and research separation

The transcription was frozen at **2026-11-18 01:15:15UTC** and the context was opened at **01:15:25UTC**. The48 SHA-256 entries in `records/frozen_sha256.json` cover every page and the combined fragment; final validation checks them byte for byte. The research notes record contextual reading alternatives without applying them to the diplomatic text.

The root assistant alone performed transcription and image auditing. Only post-freeze research was delegated: the octahedral section, the real-elliptic section, and bridges to the supplied context. Selected algebraic and analytic arguments then received a second in-run review; these reviews do not constitute external refereeing or a guarantee of correctness.

The context's prior research notes and result statuses remain attributed claims. The research notes explicitly credit Hua's modernised reading, distinguish elementary arguments checked here from background theorems, retain open comparisons, and identify unavailable source returns. No claim of mathematical novelty is made. The advertised prior Lean proof was not rerun; the included certificates are the actual small Python computations executed in this run.

## Source and working-record conventions

The original prompt, scan images, supplied source ZIPs, and extracted context files are deliberately not duplicated in this archive. Context citations are relative to the supplied context ZIP; the optional prefix `context/` denotes its extracted root. Hua's printed page *p* maps to scan *p+1* throughout these notes.

`records/pageNNN.py` and `records/readings.jsonl` preserve **first-pass history**, including readings later corrected during the pre-freeze image audit. They are not substitutes for the authoritative files in `pages/` and must not be rerun to overwrite the frozen text. `records/checkpoint_state.json` records the state at the first hourly checkpoint, not the final state. The final state is recorded in `validation/final_validation.json`.

The optional compile wrapper uses standard LaTeX, AMS packages, TikZ/tikz-cd and soul, plus definitions of the requested diplomatic macros. Its output is a technical reading layout rather than an attempt to preserve the original manuscript's page geometry. The saved compile logs show a successful full-fragment syntax check; no PDF is part of the requested deliverable.

The first hourly checkpoint was saved during the image-audit phase; earlier checkpoints are not nested in this final archive. The final archive includes the current deliverables, work records, proofs, scripts and logs.
