# Structural and TeX validation — first-pass snapshot

Snapshot: 2026-11-18 08:29:11 UTC. This report concerns immutable temporary copies taken before the root reader completed the second visual audit.

## Scope and limits

The support agent read page-file text and inventory records only. No scan images, OCR, context contents, source-reading decisions, page-file edits, inventory edits, combined transcription, or freezing were involved. Syntax checks cannot certify accuracy or completeness relative to handwriting.

## TeX compilation

- All 43 page fragments have balanced grouping braces under the conservative lexical checker.
- A temporary local XeLaTeX format was generated because engine binaries and packages were installed but format files were absent.
- With a macro-aware temporary wrapper, 42 of 43 first-pass page fragments compile successfully.
- Scan 162 fails because two inner pairs of dollar delimiters occur inside already open inline formulas: at line 8, `\uuline{$\operatorname{Aut}_S$}`; at line 16, `\uuline{$\operatorname{Imm}_S^{\mathrm{sp}}$}`. Removing only the inner dollar pairs in a separate temporary probe makes that page compile. The original page file was not modified.
- The wrapper gives editorial macros identity definitions, and handles tikz-cd ampersands inside macro arguments. It is a syntax test, not a presentation style or a facsimile.

## Inventory granularity

Every page has inventory rows. There are no diagram or drawing macro-count deficits. Several inventory rows combine multiple separately encoded editorial elements; therefore their row counts are smaller than the macro counts. This is a granularity flag, not proof that the source content is missing from the transcription. The detailed JSON report gives each occurrence and the existing rows for reconciliation.

| Scan | Element type | Macros | Inventory rows |
|---|---|---:|---:|
| 139 | deleted | 10 | 4 |
| 147 | deleted | 9 | 7 |
| 149 | deleted | 9 | 5 |
| 151 | deleted | 7 | 6 |
| 153 | deleted | 5 | 4 |
| 154 | deleted | 2 | 1 |
| 155 | deleted | 5 | 4 |
| 158 | margin | 5 | 4 |
| 158 | inserted | 4 | 2 |
| 160 | inserted | 5 | 4 |
| 160 | deleted | 11 | 6 |
| 166 | inserted | 2 | 1 |
| 166 | deleted | 6 | 3 |
| 167 | deleted | 5 | 3 |
| 169 | inserted | 4 | 3 |
| 169 | deleted | 6 | 4 |
| 170 | deleted | 8 | 5 |
| 173 | deleted | 6 | 4 |
| 174 | deleted | 3 | 2 |
| 176 | inserted | 2 | 1 |
| 176 | deleted | 7 | 4 |
| 177 | inserted | 3 | 2 |
| 178 | deleted | 4 | 3 |
| 179 | deleted | 4 | 3 |

The deficits total 39 deletion rows, 7 insertion rows, and 1 margin-note row if each macro is assigned its own element row. Nested deletion macros and composite rows account for at least some of this difference. In addition, scan 147 has 8 explicit display environments but 7 display rows: row `147.23` combines the two displayed calculations starting at lines 44 and 47, and row `147.24` combines the two corresponding deleted formulas. Split these if applying the prompt’s one-row-per-element requirement literally.

The initial source hashes and compiled snapshot are in the temporary build directory recorded by `tex_validation_location.json`. Root changed scans 135 and 144 after this snapshot was taken; these changes were not part of this initial compile.

## Repeating the check after the audit

Use `documentation/run_tex_validation.py --label final --format /workspace/scratch/641dc45262b6/tex_validation_20261118T082911Z/xelatex.fmt`. It snapshots current page files without modifying them, writes build files outside the deliverable folder, records hashes and any changes during compilation, and writes a named report under `documentation/`.
