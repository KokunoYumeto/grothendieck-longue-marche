# SP33_CW_156-5

Complete second pass and research notes for Montpellier cote 156-5, **scans 002–025, manuscript pages 1–24**. The transcription has one page file per supplied scan and one combined LaTeX fragment. It preserves deletions, insertions, margins, diagrams, drawings, abbreviations, unresolved readings, and mathematically surprising wording.

## Start here

| File | Contents |
|---|---|
| `SP33_CW_156-5_transcription.tex` | Frozen consolidated transcription, one fragment with one cote marker and all 24 pages in order. |
| `pages/` | The24 frozen page files, with the original witnessC filenames. |
| `SP33_CW_156-5_changes.md` | Per-page C/H decisions, all C doubt decisions, S-row outcomes, crop evidence, confidence counts, and consequential corrections. |
| `SP33_CW_156-5_collation.tsv` | The558 substantive H-difference loci, using the requested columns and kinds; macro syntax alone is excluded. |
| `SP33_CW_156-5_doubts.md` | Notation table, remaining doubts, abbreviations, and legibility assessment, including the exhaustive385-occurrence uncertainty appendix. |
| `SP33_CW_156-5_inventory.csv` | All543 inventoried elements; every row is marked transcribed. |
| `SP33_CW_156-5_notes.md` | Eighty-one numbered research notes covering every scan, context comparisons and register ids, both standing questions, and item-by-item review of witnessC’s notes. |
| `SP33_CW_156-5_mathematical_checks.md` | Fourteen written proof/check sections, including counterexamples and the exact finite component classification. |
| `CHECK_EVENTS.tsv` | Actual proof, computation, recheck, refutation and separately attributed background events. |
| `SP33_CW_156-5_audit.md` | The second visual-pass record and scope of witnessS. |
| `progress.log` | Actual UTC milestones, page completion/audit times, freeze hashes, checkpoints, context opening, and final verification. |
| `records/`, `crops/`, `scripts/` | Complete decision/crop provenance, uncertainty exports, context-search log, finite computation data and reproducible scripts, and structural validation/packaging tools. |

## Method and freeze

The root reader alone inspected every whole page, both supplied halves, and the enlarged decision regions, then made a second visual pass over all 24 pages. No OCR, PDF text extraction, or image-recognition library was used. Ancillary workers handled only tooling, packaging, and computation from abstract definitions; they did not read the manuscript or witnesses for transcription or interpretation.

WitnessC comprises the supplied GPT-6 Astra Codex returns J156-5-01 throughJ156-5-03; witnessH is the supplied Commutator-project transcription at commit`aef7db2`; witnessS is the supplied sweep correction table. Their agreement does not count as independent evidence of a reading. S’s full156-5 reading, opened only after freeze, explicitly says it viewed no scan images; the research notes qualify its provenance accordingly.

All24 page files and the combined fragment were hashed and frozen at **2026-11-19 21:25:11 UTC**, before the context-opened entry. Context and research work have not changed any of those25 files. The combined SHA-256 is:

`8bdd894d1f3c291524040102a6365da0398baa9f39152fee0db420d13b65d37f`

The authoritative manifest is `records/frozen_hashes.json`. The changes table counts **179 C-difference loci and 558 H-difference loci**, not word-error rates; differences include resolution or addition of uncertainty and editorial state. The final text contains382 `\unsure` marks and 3 `\illegible` marks, all indexed in the doubt materials.

The research notes distinguish literal ink from explicitly qualified mathematical statements. They include the failure of connectedness/C4, the two different interpretations of the product construction, strong versus ordinary irreducibility, finite Boolean generation, the refinement proof, and the maximal-full-support subdivision criterion. Earlier register statuses and unverified context transcriptions remain attributed background; no external literature theorem or unavailable continuation is newly certified.

## Reuse and verification

The LaTeX is intentionally a fragment, as requested. Use the supplied witnessC `PREAMBLE.tex` from the original attachment to typeset it; that original source file is not duplicated in this return. Structural verification checks macro names, delimiters, page order, inventories, collation schema, crop references, uncertainty coverage, and frozen hashes. A full TeX compilation was not possible in this environment because the installed engine lacks the required formats/classes/packages; no compiled-PDF verification is claimed or required by the requested deliverable.

The page generators document first-pass creation. **Do not rerun them over the audited files.** Later audit scripts and the frozen files supersede their initial output. The metadata generator’s freeze guard verifies and preserves frozen TeX, but its older report templates can overwrite later research/editorial additions; do not regenerate reports indiscriminately. The research-note and check-event scripts do not write transcription files.

The final archive contains all current deliverables and work documentation. Original scans, witnesses, context packets, the input archive, and earlier checkpoint archives are deliberately omitted. `records/checkpoints.json` and the progress log identify the separately saved checkpoints without embedding them.
