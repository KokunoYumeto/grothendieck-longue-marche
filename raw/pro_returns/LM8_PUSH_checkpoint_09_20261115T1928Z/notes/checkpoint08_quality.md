# Checkpoint08 typesetting, visual review, and reconciliation

Prepared on 15 November 2026 for the 18:00 UTC checkpoint window.

## Main paper

The final paper has364 pages and233 registered statements:185 Proved,30 Open,8 Refuted,10 Known. All80 requested lead/task items are mapped. The register verification reconciles all57 included TeX files with no duplicate identifiers, unregistered statements, missing statements, or status disagreements. All128 bibliography entries retain their source-verification annotations.

The preliminary four-pass build produced two overfull boxes per pass:1.00848pt in the A.50 normalizer paragraph on page109, and28.96704pt in the C.37 dimension table on page195. Thus one distinct box exceeded the2pt limit. The prose was rephrased equivalently and the table's column headings were shortened. Two missing acute-accent glyph diagnostics in A.46's etale subscripts on page96 were also repaired by moving the accent outside the Roman alphabet command. No mathematical claim changed.

After the repairs, every one of the four final LuaLaTeX passes has zero overfull boxes, including zero above2pt. The final log also has zero unresolved references/citations, zero warnings, and zero missing-character messages. BibTeX reports seven pre-existing metadata warnings: an empty publisher for DE_Kato2004; an empty year for A_LorenzRoquette; an empty journal for fghLuoWatanabe; an empty journal for PBC_MilneCM2007; simultaneous volume and number fields plus an empty publisher for fghOlssonTangential; and an empty year for PBC_SchnepsSurvey. These are retained transparently; they do not leave any citation unresolved.

The preliminary logs are retained under qa/checkpoint08/preliminary/. The final diagnostics and exact statement-page map are in qa/checkpoint08/rendered_pages.json. Rendering was followed by actual image inspection, not treated as its substitute.

## Exact visual-review coverage

All46 rendered final main-paper pages were viewed:

1,25,50,75,96,99,100,102,103,105,106,107,109,110,111,113,125,150,175,186,187,189,190,191,192,193,194,195,196,197,199,200,225,250,275,300,307,308,309,310,312,313,314,316,325,364.

This includes every formerly overflowing page, the repaired accent page, a sample across the complete paper, and the new A.48--A.51, C.33--C.39, and D.62--D.64 proofs. The root reviewed13 spread pages and preliminary96,109,195; FGH reviewed12 A pages; PBC reviewed13 C pages; and DE reviewed8 D pages. Exact per-reviewer lists are retained in notes/root_checkpoint08_visual_review.md, notes/fgh_checkpoint08_visual_review.md, notes/pbc_checkpoint08_visual_review.md, and notes/de_checkpoint08_visual_review.md.

All reviews passed: paragraphs, headings, tables, mathematical displays, equation labels, citations, and bibliography are legible and contained within their margins, with no clipping or collisions observed. Page195's table visibly fits after repair. The root paper PDF and its build-directory copy have identical bytes.

## Other PDFs and superseded diagnostics

The notes-only D.65 candidate remains outside the frozen main paper and register. Its three-page PDF notes/de_compile/de_compile_D65.pdf is retained. The log has zero overfull boxes, warnings, undefined references/citations, and missing-character messages. All three rendered pages in qa/checkpoint08/d65_diagnostic/ were individually inspected and passed. The proof has independent root and PBC mathematical audits recorded separately.

Six older diagnostic PDFs are omitted from the current-file package because their complete mathematical contents are superseded by the integrated main PDF: de_compile_check.pdf, de_prosolvable_compile.pdf, de_compile_D60.pdf, de_compile_D61.pdf, de_compile_D62_D63.pdf, and de_compile_D64.pdf, all under notes/de_compile/. Their wrapper sources, logs, outputs, and proof audits remain included. The exact paths and reasons are recorded in code/package_return.py and notes/session.md. Any copies in earlier immutable checkpoints are unchanged and will be retained in the final checkpoint_history. The supplied attachments and reproducible primary-source/runtime caches remain excluded under the previously recorded rule.

The heavy C.31 original-presentation computation continues in the work records. Its completed original word collection is a supporting computation, not a registered vanishing result: an exact original-row relation certificate and independent replay remain required. The archival packaging script captures each file's bytes once, so the manifest hashes and archive entries agree even if an active computation subsequently appends to its own log.
