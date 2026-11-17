# Final validation record

Completed **2026-11-17 20:10:09 UTC**.

## Coverage and consistency

| Check | Result |
|---|---|
| Retained scans | All 47: 002–019, 021, 023–050. |
| Page files | 47 separate UTF-8 LaTeX fragments, in numerical scan order. |
| Combined transcription | Exactly the ordered page fragments with the documented blank-line separators; no preamble or embedded scan images. |
| Inventory | 749 rows, all `transcribed=yes`; 44 text pages, 2 `reused_typed` pages (009 and 011), 1 cover (021). |
| Doubts | 411 registered occurrences: 398 `unsure` and 13 `illegible` annotations; the latter concern unreadable text, not replacements for mathematical symbols. |
| Notation table | 57 entries; Markdown table delimiters checked after a formatting-only repair. |
| Research register | N001–N101 in order, each with witness, kind, context relation, RS relation, and search terms; own ideas state confidence and a reason. |
| Context searches | All 101 items searched in all four supplied comparison texts: 404 file-query sets, preserved with source locators. |
| Research length | 17,462 whitespace-delimited words, including tables, metadata, and bibliography. |
| Bibliography | 17 defined and used external source codes, with primary-source URLs and exact locators. |
| Standing sections | Author-marked unverified steps; titles, contents, page counts, and pagination evidence. |
| Completion and audit log | 47 page-done entries and 47 second-reading audit entries, retaining the original UTC timestamps. |
| Freeze order | Frozen at 19:23:39 UTC; context opened at 19:23:47 UTC on 17 November 2026. |
| Final freeze verification | All 48 SHA-256 values unchanged: 47 page files and the combined transcription. |

## Structural checks and their limits

`python3 work/scripts/validate_package.py --root work` passed the page/scan-marker, required-file, inventory-schema, allowed-value, brace-balance, ordered-concatenation, and frozen-hash checks. A separate check found balanced LaTeX environments, even unescaped dollar delimiters, and 109 matching display-delimiter pairs. The checks did not modify the transcription.

These checks cannot establish whether a difficult handwritten word has been read correctly. The root reader's whole-page/half-page inspection, second reading, and notation reconciliation are documented separately in `progress.log`, `audit_notes.md`, and the doubts file. No OCR was used on the manuscript scans, and no research assistant read or transcribed those images.

A full typesetting run was **not available**: the installed TeX executables lacked the required format and package resources. The output is the requested LaTeX fragment, without a preamble or annotation-macro definitions. The structural checks are not presented as successful compilation.

The package includes the deliverables, research records, log, manifest, and supporting scripts. Its packaging rule excludes the supplied scan images, source PDFs, source/context ZIPs, context documents, caches, and earlier checkpoint archives. Intermediate research records are identified as such; the main notes contain the reconciled final interpretations.
