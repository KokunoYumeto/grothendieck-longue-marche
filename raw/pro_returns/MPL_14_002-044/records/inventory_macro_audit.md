# Inventory/state-macro count comparison

Snapshot read started **2026-11-15 00:39:25.282584 UTC** and finished **2026-11-15 00:39:25.283624 UTC**.
This read-only comparison covers the 40 saved page fragments after the primary transcriber reported completion of the second visual audit. The inventory was still being finalized. These are snapshot counts for review; no claim of manuscript completeness is made.

## Method

Every balanced occurrence of `\deleted`, `\inserted`, `\margin`, `\diagram`, and `\figure` was counted, including nested occurrences. TeX comments and escaped control symbols were skipped. Each occurrence contributes to its own category; a diagram inside a margin macro contributes to both categories. “Nested” counts occurrences enclosed by any of these five state macros.

| Macro | Inventory kind |
|---|---|
| `\deleted` | deletion |
| `\inserted` | insertion |
| `\margin` | margin note |
| `\diagram` | diagram |
| `\figure` | drawing |

Inventory rows describing individual drawn paths or annotations inside a diagram may exceed wrapper-macro counts. The comparison specifically flags smaller inventory counts. It preserves the intentional placement of annotation macros inside diagrams.

## Category totals

| Category | Macro occurrences | Nested occurrences | Inventory rows | Sum of page-level deficits |
|---|---:|---:|---:|---:|
| deletion | 155 | 10 | 155 | 0 |
| insertion | 74 | 5 | 74 | 0 |
| margin note | 36 | 0 | 37 | 0 |
| diagram | 20 | 8 | 20 | 0 |
| drawing | 11 | 6 | 12 | 0 |

## Page/category deficits

**No page/category deficits were found in the captured inputs.**

## Drawn paths inside diagrams

The following `\draw` commands occur inside `\diagram` arguments and outside any `\figure` argument. An inventory drawing row can therefore have a direct path representation without adding a figure-macro occurrence.

| Scan | Diagram-internal draw commands | Figure macros | Drawing inventory rows |
|---|---:|---:|---:|
| 031 | 1 | 0 | 1 |

## Snapshot qualifications

- Inventory SHA-256 at snapshot: `195a81de485769c101b2c6d1d97d9dd9ef7632f30d764096d5b3ca0ffc2f7b9c`.
- No page file or inventory row was changed, and no assembly or freeze was performed.
- Re-reading all input bytes at the end found no change during this comparison. Later inventory edits may change the counts.
- All encountered state-macro arguments were balanced.
