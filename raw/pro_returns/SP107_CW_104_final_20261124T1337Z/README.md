# SP107_CW_104 — diplomatic edition

Final edition: all nine pages have completed both reading stages.

## Scope and sources

Alexander Grothendieck, Université de Montpellier archive, cote 104, scans 009–017: nine handwritten pages. The supplied catalogue description is “[Champs (stacks) 1][92]: copies de notes manuscrites (s.d.).” This catalogue label is not presented as a title written on these leaves. The manuscript is undated.

Witness C is the supplied Codex diplomatic transcription: H104-01 for 009 and H104-02 for 010–017. Witness H is the supplied Commutator transcription, commit `aef7db2`, whose page number equals the scan number minus one. The source-file manifest records the supplied paths and SHA-256 digests. The scans and witnesses themselves are deliberately absent from this package; the saved decisive crops are included.

Archival citation: Grothendieck, A. (n.d.). *[Champs (stacks) 1]* [Handwritten notes, cote 104, scans 009–017]. Fonds Grothendieck, Université de Montpellier. Catalogue title and dating follow the supplied materials.

Witness reference: Commutator-IO. (n.d.). *Grothendieck project* [LaTeX transcription, commit aef7db2]. https://github.com/Commutator-IO/grothendieck-project. This run used only the supplied files, without fetching the repository or researching external literature.

## Transcription and apparatus

- `SP107_CW_104_transcription.tex`: the complete ordered LaTeX fragment, beginning with `\cotefile{104}`.
- `pages/`: one finalized fragment per scan, using the supplied preamble’s conventions. No preamble, compiled PDF or new macro definitions are included. Use these fragments with the existing supplied `PREAMBLE.tex`.
- `SP107_CW_104_changes.md`: witness comparisons, confidence counts, decisions on C’s doubt marks, and every differing independent reading with the principal adjudication.
- `SP107_CW_104_collation.tsv`: H discrepancies in the requested column schema.
- `SP107_CW_104_inventory.csv`: page elements, including revision layers and numberings.
- `SP107_CW_104_doubts.md`: maintained notation, remaining doubts, literal abbreviations with tentative expansions, and a legibility assessment.
- `SP107_CW_104_notes.md` and `CHECK_EVENTS.tsv`: brief mathematical notes and the exact scope of any checks actually performed.
- `SP107_CW_104_hand_log.md` and `SP107_CW_104_sheet_feedback.md`: local handwriting patterns and counts by the supplied error-sheet classes.

Current comparison totals are **398 documented features**, **98 against C** and **387 against H**. A feature may differ from both witnesses. Counts concern specified words, symbols, revision states or separate marks, not whole sentences or crops. Pure macro conversions, confidence-only changes and H’s explicit editorial notes are excluded. The body of the changes log supplies the evidence behind every counted feature.

## Reading and independent audit

Three first readers worked on different pages, one page at a time, in the supplied scan order. Each inspected the whole page and both full-resolution halves, read all agreed text as well as disagreements, and then inspected the required crops. The principal reader inspected every open or witness-disagreeing place. Every page was registered in `progress.log` when moved into `pages/`.

Only after all nine first readings were complete were **290 boxes** frozen for an image-only independent reading. Fresh readers received only their assigned images and neutral coordinate lists with opaque IDs. They did not receive either witness, the consolidated page, the frozen first readings, notes or previous crop names. Assignments and method records document this separation.

For each page, `second/` contains the coordinate-only `_boxes.tsv`, immutable `_first.tsv`, independent `_second.tsv`, token comparison, token operations, input/submission hashes, crop manifest and reader method record. The original-to-opaque ID map is retained for provenance but was not part of a blind packet. Token comparison retains words, symbols, punctuation and macros; it ignores whitespace only. Formatting or crop-scope differences are therefore visible alongside substantive differences and are adjudicated from the image rather than silently discarded.

At this stage **9 pages** have a completed principal audit, covering **215 differing boxes**, of which **22 changed the first-pass page reading**. The latter includes changes to uncertainty notation where the page itself changed; such changes need not count as substantive corrections against a witness. Every differing box receives a saved crop decision. `records/` preserves the detailed page evidence, earlier proposals, review decisions and accounting history. First-pass progress counts remain a historical record if later audit or editorial-accounting decisions change final totals.

## Fidelity and verification

The edition preserves source spelling, abbreviations, accents or their absence, missing letters, incomplete punctuation, unexpected indices and arithmetic slips. A doubtful reading remains marked where the crop does not settle it. No OCR, text-recognition software, external mathematical research or TeX compilation was used.

Static checks cover TeX braces, math delimiters, environments and fragment structure. They are not a compilation result. The mathematical notes distinguish source claims, local type checks, arithmetic and conditional proof checks; reading a claim is never described as proving it. Final transcription hashes and their end-of-run verification are recorded in `progress.log` when the edition is complete.

`scripts/` contains the assembly, crop generation, comparison, adjudication-recording, static verification and packaging helpers. `records/checkpoints.json` identifies the separately saved 45-minute checkpoints; no checkpoint ZIP is nested inside this package.
