# Checkpoint09 typesetting, visual review, and reconciliation

Prepared on 15 November 2026 for the scheduled 19:00 UTC checkpoint.

## Main paper and register

The integrated paper has 392 pages and 241 numbered statements: 193 Proved, 30 Open, 8 Refuted, and 10 Known. All 80 requested lead/task items are mapped. The register reconciliation covers all 65 included TeX files without duplicate identifiers, unregistered statements, missing statements, or status disagreements. All 130 bibliography entries have source-verification annotations.

The eight statements newly integrated since checkpoint08 are A.52--A.54 and D.65--D.69. Each has a complete root proof audit and at least one independent proof audit. Relevant existing scope statements A.45, D.5, D.29, and D.41 were updated consistently; the universal cover frontier and the absent explicit least nilpotent obstruction remain Open.

The included source freeze began at 18:39:25 UTC. All four LuaLaTeX passes completed successfully. Before and after visual QA the overfull-box count is zero, including zero boxes exceeding 2pt; no layout correction was required in this build. The final log has zero undefined references/citations, zero warnings, and zero missing-character messages. BibTeX retains seven previously disclosed metadata warnings: an empty publisher for DE_Kato2004; an empty year for A_LorenzRoquette; an empty journal for fghLuoWatanabe; an empty journal for PBC_MilneCM2007; simultaneous volume and number fields plus an empty publisher for fghOlssonTangential; and an empty year for PBC_SchnepsSurvey. None leaves a citation unresolved.

The executed diagnostics and exact statement-page ranges are recorded in code/qa_checkpoint09.out and qa/checkpoint09/rendered_pages.json. Rendering was followed by actual image inspection, not treated as its substitute.

## Exact visual-review coverage

All 45 rendered final pages were actually viewed:

1, 25, 50, 75, 95, 96, 100, 114, 115, 116, 118, 119, 120, 121, 122, 125, 150, 175, 200, 224, 225, 240, 241, 250, 273, 274, 275, 300, 325, 329, 330, 331, 332, 334, 335, 336, 338, 339, 340, 342, 343, 345, 350, 375, 392.

This includes samples of every newly integrated proof, every modified existing scope statement, and pages spread across the whole paper. Root reviewed 15 pages, FGH 11, DE 13, and PBC 6. The exact assignments and observations are retained in notes/root_checkpoint09_visual_review.md, notes/fgh_checkpoint09_visual_review.md, notes/de_checkpoint09_visual_review.md, and notes/pbc_checkpoint09_visual_review.md. All passed: paragraphs, headings, tables, displays, equation labels, citations, and bibliography are readable and contained in their margins, without clipping or collisions.

## Diagnostic consolidation and computation records

The previously reviewed three-page notes/de_compile/de_compile_D65.pdf is now superseded by the integrated D.65 proof on pages329--331. From checkpoint09 it joins the six diagnostic PDF exclusions explicitly listed in code/package_return.py. All seven wrappers, logs, outputs, proof audits, and visual-review records remain included. The checkpoint08 copy remains unchanged, and all earlier checkpoints are preserved for the final checkpoint_history. No proof or failed attempt has been removed.

The D.67--D.68 stand-alone syntax check used draft mode and generated no real PDF. Its zero-byte engine placeholder is retained with the .empty suffix, as documented in notes/de_diagnostic_pdf_status.md. Those proofs are visually reviewed in the integrated paper.

C.31 remains Open. Its completed original word collection, stopped exact and modular elimination attempts, independent validation records, and continuing native calculation are retained as supporting work. No processed-row vanishing or unfinished native trace is registered as a certificate. A valid closed gzip prefix is required for the snapshot; any raw unfinished compressed prefix and trailing record bytes are separately identified and retained.

To keep the enlarged archive practical without omitting evidence, code/package_return.py now compresses raw files of at least ten million bytes at deflate level6 and stores already compressed gzip files of that size without recompression. Smaller files retain deflate level9. This changes compression only: each captured file's actual bytes and SHA256 are retained in the manifest, and the complete archive must pass its CRC check before saving. The script still refuses to overwrite any prior checkpoint.

The final integrity check confirms that the delivered root PDF and build copy have identical SHA256 fc53cc2305d2d834b010b4b885fed6332aa5f345a8cd2249f56653b708e6978e. The frozen source manifest has66 files (the65 included TeX files plus the bibliography), all unchanged. An initial lowercase-only annotation check incorrectly rejected four existing capitalized Verified annotations; the retained validator explicitly accepts either case, and all130entries pass. No bibliography contents were changed for that check.

The C.31 native search is paused at a valid gzip-member boundary with its live basis preserved. The retained prefix has3,653,273 valid JSON records and3,653,272 contiguous proof nodes; its108,803,164 compressed bytes have SHA256 d6f6603fc702b8276587092e29539f6af9b2e75690168fe3b63bcb96f8a7deda. The exact source modulus, original presentation hash, parsed-record counts, and resume marker are in code/pbc_checkpoint09_trace_manifest.json. All interrupted raw compressed streams and trailing partial records are separately retained and labeled incomplete; valid rewrapped prefixes are also retained. Files ending .gz.incomplete_stream are stored without recompression under the same large-compressed-file policy, preserving their exact bytes. The search has not produced a completed certificate.
