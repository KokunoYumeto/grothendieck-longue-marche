# Montpellier 156-1 and 156-2

## Contents and reading order

The diplomatic transcription covers all 46 supplied scans in the prescribed order: cote 156-1, scans 001–027, followed by cote 156-2, scans 001–019. The same primary transcriber read every whole-page image and both supplied overlapping halves, then performed a second visual audit of every page and a cross-page notation audit. No OCR or delegated image reading was used.

| File or directory | Purpose |
|---|---|
| MPL_156-1+156-2_transcription.tex | Complete ordered LaTeX fragment, with no preamble or document class |
| pages/ | The 46 individual page fragments |
| MPL_156-1+156-2_doubts.md | Notation table, manuscript-position doubts, exhaustive uncertainty index, abbreviations, and legibility assessment |
| MPL_156-1+156-2_inventory.csv | 955 element-level rows, all marked yes |
| MPL_156-1+156-2_notes.md | 125 research entries, author-qualification audit, titles and foliation, context comparisons, and APA references |
| progress.log | Completion, audit, freeze, checkpoint, recovery, and final verification record |
| transcription.sha256 | SHA-256 checksums of all 46 page files and the combined fragment |
| records/ | Page observations, audit records, mathematical verification memos, context searches, and validation evidence |
| scripts/ | Scripts retained to document assembly and verification |

There are two institutional covers and 44 manuscript sheets. The handwritten page numbers are recorded independently of scan numbering; the research notes contain the complete two-strand foliation ledger. The archive includes neither the supplied scan images nor the supplied context files.

## Status of the transcription

The transcription was frozen at **2026-11-14 20:03:21 UTC**, after every second visual audit and the final notation audit, before the context contents were read. All 47 frozen hashes were verified unchanged after recovery of the execution environment and again during final assembly. Research notes have not altered manuscript readings.

The uncertainty index contains **472 occurrences of the unsure macro and one occurrence of illegible**, the latter estimating two words. Of the unsure occurrences, **88** are the faint EXTRA STRONG paper legends, two on each manuscript sheet. The least secure substantive material is small rotated marginalia, layered corrections, and heavily cancelled drafts; the doubts file identifies the locations and alternatives. These counts measure explicit uncertainty marking, not an estimated error rate.

Drawings are reproduced in TikZ and diagrams in tikz-cd or arrays, with visible labels and cancellation states; the drawings approximate handwritten geometry. The combined fragment passed the recorded pdfTeX draft-mode syntax check. The diagnostic preamble supplies the required macros and loads amsmath, amssymb, graphicx, xcolor, tikz-cd, and the TikZ calc/arrows.meta libraries; it is not an edition design. The original environment's full PDF attempt failed at embedding an unavailable TS1 font, so no rendered publication-layout verification is claimed.

## Research findings

The definitions and their limits are collected as D01–D16. These pages define a zero-dimensional form, develop changing one-dimensional model axioms called networks, and study geometric cutting and gluing of ficelles and mailles. They do not complete a general definition of a form as a pro-object of finite posets or categories; no workshop or atelier is defined.

- **A11–A13:** arbitrary-subset restriction fails because retained segments may require an ambient glued support outside the subset.
- **A17–A18:** the global orientation theorem is explicitly unverified.
- **A21–A25:** the manuscript retracts the local-to-global filtering argument; the two F6 formulations differ at singular endpoints, with a positive repair when the other endpoints are regular.
- **B22–B28:** disconnected ends expose two literal counterexamples; a tripod witnesses the endpoint-enlargement retraction even for connected contractible enlarged ends.
- **B52–B53:** the reduced existence and arc-uniqueness claims have elementary proofs for connected nontrivial finite polyhedra.
- **B34–B51:** the global Stone spectrum of the rive algebra, a relative spectrum over the node, and the étalé space of ring elements retain different information.
- **P03–P05:** compatible literal cut chains do not automatically have common refinements.
- **P06–P12:** finite-space homotopy models, literal inverse limits, stratified exit categories, and the Esquisse's geometric assembly have different hypotheses and conclusions.

The notes distinguish manuscript assertions, retractions, unproved claims, doubtful readings, and our own counterexamples or proposed constructions. The 26-entry standing audit labels deliberate limitations separately from expressions of doubt. All nine open entries in the supplied research register retain their supplied status.

## Provenance and reproducibility

The source page fragments and their frozen combined join are authoritative for this transcription. Per-page JSON records and observations document work stages; preliminary questions there are superseded by the final doubts and research notes where a later decision is recorded.

The execution environment reset during the post-freeze research phase. The saved checkpoint preserved the complete transcription, all audits, the final doubts and inventory, and the freeze manifest; all hashes matched after restoration. The unsaved research prose was reconstructed from retained analyses and checked against the frozen text and supplied context. The recovery event and approximate original context-opening time are identified transparently in the log.

The primary transcriber alone read the images. Three research reviewers assisted only after the freeze, using the frozen text, context register, and literature; their checks are retained in records. The supplied register contains summaries of earlier returns, not the underlying files, and its statuses are not treated as independently established theorems.

To verify the frozen text, run from the extracted archive root:

    python3 scripts/freeze_transcription.py

To rebuild notes and their exact searches, supply the original context separately:

    python3 scripts/assemble_notes.py --final --context /path/to/extracted/context

To assemble the deliverable ZIP:

    python3 scripts/build_package.py final

The builder checks the frozen combined join and does not rewrite it. Page-recording, page-auditing, and doubts-finalization scripts document the transcription phase; the final frozen reading should be preserved.
