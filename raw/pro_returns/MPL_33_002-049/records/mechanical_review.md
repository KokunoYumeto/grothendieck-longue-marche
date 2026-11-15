# Mechanical review of saved transcription

Generated: 2026-11-15 13:14:54 UTC.

Scope: saved LaTeX and inventory only. No scan images or context files were opened. These checks cannot establish visual completeness, intended notation, or correctness of a reading.

## Structural results

- Page files: 48. Inventory rows: 711. Inventory scans: 48.
- Validator result: PASS in partial mode (no final freeze assertion).
- Invalid inventory kinds or element identifiers: 0.
- Element-number gaps: 0. Blank required inventory cells: 0.
- Text rows by scan are retained in inventory_mechanical_summary.tsv. Absence of an image element cannot be detected from saved text alone.
- Source files changed while this report ran: none.

## Macro counts versus inventory rows

These are count differences for visual/inventory review. Nested deletions may be covered by one inventory entry; one figure wrapper may contain several drawings. No difference is automatically an omission.

| Scan | Source macro | Occurrences | Inventory kind | Rows |
|---|---|---:|---|---:|
| 021 | `\figure` | 1 | drawing | 5 |

## Recurring notation tokens

Counts are literal source strings. Prime pairs are included in the double-quote/prime category; its opening/closing totals are therefore not a quotation-balance test. notation_occurrences.tsv records each source location and context.

### Gamma notation

- `\Gamma`: 34.
- `\Gamma_2`: 4.
- `\Gamma_X`: 1.
- `\Gamma_Y`: 4.
- `\Gamma_{Y'}`: 1.

### f notation

- `f^*`: 8.
- `f^{-1}`: 1.
- `f_!`: 3.
- `f_*`: 36.
- `f_1`: 2.
- `f_A`: 1.
- `f_i`: 2.
- `f_n`: 2.
- `f_x`: 1.

### bang subscript

- `_!`: 41.

### bang superscript

No matching source token.

### double quote/prime

- `''`: 52.
- ``` `` ```: 13.

### R exponent

- `R^*`: 3.
- `R^0`: 1.
- `R^8`: 2.
- `R^i`: 11.
- `R^n`: 1.
- `R^q`: 14.
- `R^{-i}`: 2.
- `R^{2(d+d')}`: 1.
- `R^{2d'}`: 1.
- `R^{2d-i}`: 1.
- `R^{2d}`: 4.
- `R^{2r+2d}`: 2.
- `R^{2r}`: 2.
- `R^{\ell+1}`: 1.
- `R^{i-1}`: 1.

## Delimiter and macro scope

extract_uncertainties.py supplies uncertainty_occurrences.tsv and latex_mechanical_findings.tsv. The checks respect escaped braces and comments, include nested uncertainty macros, and flag unmatched math delimiters or near-misses of the editorial macro names. They do not prove general TeX compilability.

The source uses the TikZ loop control word `\x`, locally bound by `\foreach`. control_word_counts.tsv is tokenized to distinguish a control word from an alphabetic character after a doubled backslash line break. No source change was made.
