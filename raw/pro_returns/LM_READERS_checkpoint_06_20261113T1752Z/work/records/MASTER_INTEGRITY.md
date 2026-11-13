# Master and reader source integrity

Audit stage: `build`. **PASS**.

This audit reconstructs every package from its immutable source, checks every recorded mechanical and layout stage, reverses editorial annotation and link instrumentation, and compares the complete common body in every form. Compilation, visual layout and PDF annotation geometry are reported separately.

## Source coverage

The unit manifest contains 245 translation units in 116 packages. Exact French-unit and English-unit reassembly: **PASS**.

| Language | Packages | Scans | Doubtful marks | Illegible marks | Authorial variants | All variants |
|---|---:|---:|---:|---:|---:|---:|
| FR | 116 | 1588 | 17117 | 1261 | 10888 | 10888 |
| EN | 116 | 1588 | 17117 | 1261 | 10888 | 10889 |

The paired French/English authorial variant ID sequence agrees: **PASS**.

## Shared master bodies

| Language | One body shared by all forms | Recomputed source pipeline matches | SHA-256 |
|---|---|---|---|
| FR | True | True | `39835a78e6b3f2520a9cefe370a0f459dbc2582a675a63dd10b7864a014bcf31` |
| EN | True | True | `fc94ffcdd7b39ae74d41340b41a6bcc984dd5e33af5cc9cc83afd99986b6a2be` |

Original ZIP bytes are checked against their manifest hashes. Text processing uses Python newline normalization (CRLF to LF); this changes no printed content. The source-reading fields in the change logs are checked against annotations of the raw checked package texts, before typesetting modifications. A layout wrapper is therefore not mistaken for a new manuscript reading. Each source-local layout replacement is replayed within its recorded scan.

## Mark counts and their meaning

Original source marks, literal master occurrences, executed source IDs, TeX expansions and PDF link runs are different counts. The common master contains both variant branches and the apparatus/carryover alternatives. Its literal mark count is consequently larger than the original-source count. The form selector identifies the exact literal IDs that should execute in each reader. LuaLaTeX may expand an identified mark several times while measuring mathematics; those expansions reuse the same source ID. A marked passage may occupy several PDF link rectangles. No equality between these distinct quantities is assumed.

| Reader | Expected executed source IDs | Ledger source IDs | Missing expected IDs | Unexpected IDs | Unlinked IDs |
|---|---:|---:|---:|---:|---:|
| LM_FR_diplomatique.tex | 19966 | 19966 | 0 | 0 | 0 |
| LM_FR_corrige_apparat.tex | 21374 | 21374 | 0 | 0 | 0 |
| LM_FR_texte_de_lecture.tex | 25045 | 25045 | 0 | 0 | 0 |
| LM_EN_corrected_apparatus.tex | 21374 | 21374 | 0 | 0 | 0 |
| LM_EN_reading.tex | 25045 | 25045 | 0 | 0 | 0 |
| LM_FR_master_annotated.tex | 21374 | 21374 | 0 | 0 | 0 |
| LM_EN_master_annotated.tex | 21374 | 21374 | 0 | 0 | 0 |

## Portability and privacy

| Reader | Actual body hash agrees | No external source/assets | No local paths or email addresses | Safe grouping for unbraced scripts |
|---|---|---|---|---|
| LM_FR_diplomatique.tex | True | True | True | True |
| LM_FR_corrige_apparat.tex | True | True | True | True |
| LM_FR_texte_de_lecture.tex | True | True | True | True |
| LM_EN_corrected_apparatus.tex | True | True | True | True |
| LM_EN_reading.tex | True | True | True | True |
| LM_FR_master_annotated.tex | True | True | True | True |
| LM_EN_master_annotated.tex | True | True | True | True |

The files may load standard TeX Live packages and fonts. Their Lua code is embedded; relative audit-output filenames do not constitute external input dependencies. The instrumentation wrapper uses literal TeX grouping, so original constructions such as an unbraced `_{\unsure}`-style script do not acquire a forbidden `\begingroup` token at the math-field boundary.

## Exceptions

No failed source-integrity checks.
