# Delivery guide — cote 64, scans 040–077

This package separates the diplomatic transcription, its reading apparatus, and the research written after the transcription was frozen.

## File map

| File or directory | Purpose |
|---|---|
| `MPL_64_040-077_transcription.tex` | Combined transcription in source-scan order; the exact concatenation of the individual page files. |
| `pages/MPL_64_040-077_64_scanNNN.tex` | One LaTeX fragment for each source scan, including reused typed material and non-text sheets where present. |
| `MPL_64_040-077_inventory.csv` | Element-level inventory of text, displays, diagrams, drawings, margins, insertions, and deletions. |
| `MPL_64_040-077_doubts.md` | Notation conventions, reading doubts and alternatives, abbreviations, and legibility observations. |
| `MPL_64_040-077_notes.md` | Post-freeze research notes: contextual comparisons, mathematical checks, proposed continuations, and limits of the conclusions. |
| `CHECK_EVENTS.tsv` | Statement-specific record of actual checks, with UTC date, checker, check type, and outcome. A carried background claim is distinguished from a new proof or computation. |
| `progress.log` | Page-completion and audit history, the recorded freeze, and the time context was opened. |
| `observations_before_context.md` | Observations saved before opening the contextual material. |
| `MECHANICAL_REVIEW.md` | Structural and packaging reviews, including the unresolved local LaTeX-compilation limitation. |
| `research_support/` | Supplemental research reports, proof details, finite computation scripts and outputs, and reviewers' separate check records. |
| `scripts/` | Workflow, structural validation, research-note generation, and packaging helpers. These are supporting tools, not additional manuscript evidence. |

The principal support reports are `boundary_levels.md`, `octahedral_checks.md`, `s20_scope.md`, and `root_proof_supplement.md`. The level-four and octahedral certificate scripts have recorded outputs; `root_checks.json` records the root reviewer's computations. These finite certificates establish their stated finite calculations, not broader global moduli or congruence theorems.

## Reading the page references

A filename ending `64_scan064.tex` and a marker such as `\scanpage{64}` refer to the **source scan number**, not the manuscript's own page number. Visible manuscript numbering is recorded separately by `\mspage{...}`; archival foliation, where recorded, is labelled in a comment. These sequences can differ, and the scan identifier is the stable locator used by the inventory, doubts, and research notes.

Annotation commands preserve cancellations, insertions, margins, uncertainty, illegible passages, diagrams, and drawings. A mathematically surprising reading can be retained with high reading confidence: that confidence concerns the visible text, not the correctness of its mathematics. Interpretive corrections and later arguments belong in the research notes.

## Frozen transcription and later research

The recorded transcription freeze is **2026-11-17 23:04:47 UTC**. Context was opened afterward, at **23:04:53 UTC**. Research findings and comparisons were kept separate from the frozen page fragments, combined transcription, and reading apparatus; they were not used to repair the manuscript retrospectively.

Contextual transcriptions, earlier research notes, and result-register entries are treated as claims or leads with their supplied status. The research notes identify which claims were checked in this run and which were only carried as background. Michel Hua's modernization and findings are credited where used; neither it nor another interpretation substitutes for the frozen reading.

## LaTeX verification and limitation

Structural checks passed for page markers, ordered page concatenation, grouping, environments, explicit mathematics delimiters, and the encoded diagram structure. The final mechanical review also records inventory and reading-apparatus checks.

**A successful local LaTeX compilation and rendered-page quality review are not claimed.** The attempted compilation was blocked by missing TeX formats and required packages, including the LaTeX class/package resources needed by the fragment. TeX executables alone were present. The files are fragments requiring a suitable wrapper, definitions for the annotation commands, and ordinary mathematical and diagram packages such as `amsmath`, `amssymb`, `mathrsfs`, `graphicx`, and `tikz-cd`.

The structural review does not substitute for compilation or visual comparison of a rendered edition. Exact review timing and the superseded intermediate findings are preserved in `MECHANICAL_REVIEW.md`.
