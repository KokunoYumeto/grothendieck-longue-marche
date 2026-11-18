# MPL 118 — Delivery and validation report

## What is included

This package contains the diplomatic transcription of **all 38 supplied nonblank scans**, the individual page fragments, an element inventory, the notation and doubts register, the post-freeze research notes, the progress log and the actual check-event ledger. The scans covered are 002–012, 014–037 and 039–041; scans 013 and 038 were omitted as blank in the supplied attachment.

| Deliverable | Contents |
|---|---|
| `MPL_118_transcription.tex` | All 38 scans in order as one fragment, without a document preamble; subject to the frozen assembly limitation below |
| `pages/` | One frozen TeX fragment for each scan |
| `MPL_118_doubts.md` | Package notation table, all 369 local uncertainty occurrences, confidence judgments, four additional geometrical qualifications, abbreviation list and legibility assessment |
| `MPL_118_inventory.csv` | 810 element rows, all marked transcribed=yes; one cover, six reused typed sheets and 31 mathematical text sheets |
| `MPL_118_notes.md` | 126 primary research notes and 270 required context mappings, with source locations and status boundaries |
| `CHECK_EVENTS.tsv` | Actual proof/application checks separated from textual comparisons, background use and final technical computations |
| `progress.log` | Start time, all first-pass completions, all personal second audits, freeze hashes, context opening, hourly checkpoints and final hash verification |
| `records/` | Working scripts, audit records, frozen hash manifest, technical reports, structured research mappings, detailed targeted-check arguments and editorial reviews |

The attached scans, original context sources and earlier checkpoint ZIPs are not copied into this final ZIP. References to `context/...` in the notes identify the separately supplied context attachment. Historical working scripts are retained as records; they should not be rerun indiscriminately against the frozen transcription.

## Reading and freeze protocol

The primary reader personally read the full scan and its supplied halves, wrote each page in the required order, and then personally performed the second image-to-text audit of every page. No OCR was used, and no manuscript transcription or image audit was delegated. The final recurring-notation comparison and all transcription refinements took place before the freeze.

The transcription was frozen at **2026-11-18 02:41:21 UTC**. The context was opened at **02:41:34 UTC**, after which the page files and combined transcription were not changed. Research subagents worked only on the frozen text, source comparisons and selected mathematical applications. The final verification at **03:45:19 UTC** checked all **39 SHA-256 values**—38 page files and the combined fragment—and found them unchanged; the corresponding line is in `progress.log` and the details are in `records/final_validation.json`.

The combined fragment's SHA-256 is:

```
63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149
```

One procedural deviation is disclosed rather than hidden: before the complete prompt had been read, an initial ZIP-directory listing exposed the context archive's filenames and sizes. No context document content was read at that time. This metadata-only deviation was logged at the beginning of `progress.log`.

Hourly checkpoints were saved at approximately 01:19, 02:19 and 03:19 UTC, measured from the 00:19:26 UTC start. No additional milestone checkpoint was made.

## Important technical limitations

**The frozen combined file has two consecutive initial `\cotefile{118}` commands.** The first page already contained the marker, and the assembly prepended another. This mechanical defect was discovered after context access and has been deliberately preserved because the user prohibited every subsequent transcription change. The individual page files are unaffected; no silently corrected alternative transcription is included. See `records/technical_qa/FROZEN_ASSEMBLY_LIMITATION.md`.

The technical checks found no reported delimiter, environment or arrow-bound errors in the final page-fragment versions. They examined **89 TikZ-CD matrices and 434 arrows**. These checks are not a visual rendering audit and do not establish that every diagram will lay out correctly with a particular macro definition or page size.

The attempted TeX compilation could not complete because the available runtime lacked the necessary format and package/font environment. **No successful compiled or rendered validation is claimed.** The attempted wrapper and runtime evidence are retained under `records/technical_qa/`. The combined fragment intentionally has no preamble, in accordance with the requested deliverable format.

The inventory and macro counts are not expected to be identical for every kind: one physical note can contain several markup commands, and braces or strokes can occur inside a diagram. `STRUCTURAL_REVIEW.md` records these mechanical differences as review aids, not as an assertion that visible content is missing. The element inventory was revised before freezing, and its 810 rows all have transcribed=yes.

## Legibility and confidence

There are **369 `\unsure` occurrences**, including nested doubts in cancelled text and diagrams: **271 low-confidence** and **98 medium-confidence** readings. There are no `\illegible` placeholders; the difficult ink has been attempted and locally marked rather than silently omitted. This does not imply that every unmarked reading is error-free.

The weakest areas are the cramped and overwritten class diagrams, oblique margins, small indices and arrowheads, and the extensive cancelled proof material. The doubts file gives the exact TeX-fragment line as well as an approximate visual zone, and distinguishes reading confidence from mathematical correctness. It preserves unusual words, abbreviations, variable choices and apparent errors instead of normalizing them from the research context.

## Research findings and their scope

The main notes contain **396 individual notes or mappings**: 3 historical answers, 14 targeted-check notes, 33 further manuscript claims and links, 48 authorial uncertainty/withdrawal entries, 20 comparisons with Hua, 8 title/pagination entries, and all 270 required context comparisons. Every mapping retains the supplied status as a source claim and distinguishes a whole-statement match from a related ingredient. The distribution is **18 partial forms, 50 analogues and 202 absent statements**; all 255 dossier IDs and all 15 NEW_RESULTS entries are covered.

The principal historical conclusions are these:

- **Strong W(7):** absent from 118 in its later reverse-excision form. The explicit strong W7bis/W7 formulations were located at XII manuscript pp. 75–78 in the supplied later material, with a self-stated verification gap. No archive-wide chronological priority is claimed. See H01.
- **Total asphericity and filteredness:** the implication is absent from 118, and the product/diagonal meaning used on these sheets must be separated from the later ordinary-final-image meaning. The later question and withdrawal were located at II pp. 36–36ter. See H02.
- **Relative Theorem A:** the common-base principle is used on 026 and 040, but this alone does not securely date that formulation to calendar year 1983; cote 117's pages were not supplied or read. See H03.

The targeted mathematical work resolves or qualifies several local steps. Strict base change of the integral is an isomorphism (C01); the comparison theorem on 021 already has its cartesian hypothesis and does not need Hua's added cocartesian hypothesis (C02); and the lax filtration triangle can be repaired using a Grothendieck-construction replacement (C03). The 1-equivalence pushout expectation has a positive answer (C07), while a supplied later weak-sieve counterexample applies to the separate attaching-map question (C12), with its existing sphere calculation explicitly carried as background.

Hua's groupoid finding is credited and its manuscript application checked (C04), including the author's published correction of the cited literature implication. The notes distinguish that result from Hua's misquotation of condition (ii) as (iv), and give the separate arbitrary-localizer qualification to the literal sum claim (C11). The finite-fence obstruction already present in the supplied companion answers the strict infinite-product question (C06). The telescope's final implication checks out conditionally, but the manuscript's full saturation proof still depends on ingredients not established on these sheets (C09); the formal transfer of strong saturation to W_A is separately checked (C10).

The complete proofs and precise restrictions of these checks are in the research records. Reported Lean certificates, omitted return files and broader prior claims were not represented as executed or independently validated. The original source statuses and open problems are not upgraded merely because the manuscript contains related terminology.

## Final verification record

`records/final_validation.json` records the frozen-hash, scan-order, inventory, uncertainty, mapping-ID/status and literal-quotation checks. The independent editorial review checked all 270 mappings, including **262 literal manuscript evidence excerpts**, and the primary notes were reviewed for their distinctions and quotation accuracy. The event ledger records the model and the fact that its reasoning-effort setting was not exposed, rather than inventing an effort level.

All remaining uncertainty, incomplete manuscript proofs, contextual scope limits and the frozen assembly defect are deliberately visible in the deliverable. None has been repaired by changing the transcription after the context was opened.
