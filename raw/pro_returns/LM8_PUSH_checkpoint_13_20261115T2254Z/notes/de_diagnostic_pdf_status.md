# Superseded diagnostic PDFs

`notes/de_compile/de_compile_D62_D63.pdf` is an isolated compilation diagnostic for the D.62 and D.63 drafts. Both statements are now integrated into the main paper as `sections/D_alexander_all_lim1.tex` and `sections/D_alexander_separated.tex`. The diagnostic PDF is superseded by the integrated paper and is not a user deliverable. It may be excluded from checkpoint08 and later packages while retaining its wrapper source, log, and console output as verification evidence.

The same principle applies to earlier isolated D/E compile PDFs in `notes/de_compile`: the authoritative deliverable is the current integrated paper. Their TeX wrappers and logs record compilation checks rather than alternate versions of the final paper.
# Additional D.64 diagnostic

`notes/de_compile/de_compile_D64.pdf` is an isolated five-page syntax/layout diagnostic for the candidate retained at `notes/de_alexander_one_prime_draft.tex`. Its wrapper and logs are retained. After integration it is superseded by the main paper and its bibliography; exclude the diagnostic PDF from the checkpoint deliverable.


# D.65 candidate diagnostic

`notes/de_compile/de_compile_D65.pdf` is a three-page isolated diagnostic of the still-unregistered candidate `notes/de_alexander_kernel_type_draft.tex`. Root and PBC have passed the proof audit. The latest build includes the countable-product reformulation and has no undefined references, citation warnings, overfull boxes, or remaining warnings. Its wrapper and logs are retained. It is not deleted; root decides whether to include this notes-only diagnostic in checkpoint08. After D.65 integration it is superseded by the main paper.

D65 was integrated after checkpoint08 release as `sections/D_alexander_kernel_type.tex`. Its three-page diagnostic is now superseded by the integrated paper; source, PDF, logs, and exact visual-review ledger remain retained.


## D67–D68 draft-mode syntax and layout check

The wrapper notes/de_compile_D67_D68.tex was compiled with LuaLaTeX --draftmode, including real bibliographic entries and two post-BibTeX passes. Final log notes/de_compile/de_compile_D67_D68.log has zero overfull boxes, undefined references/citations, LaTeX warnings, missing characters, or errors. The engine created a zero-byte file with a PDF suffix despite draft mode; this is not a PDF and contains no pages. It is retained under notes/de_compile/de_compile_D67_D68_pdf_placeholder.empty. No rendered diagnostic PDF was created or delivered; visual review belongs to the integrated paper after the root build. Console and auxiliary files are retained.
