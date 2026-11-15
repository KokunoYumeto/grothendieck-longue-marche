# Proposed inventory kind conversion

**Status: prepared for principal-reader review; the live inventory was not overwritten.**

The input contains 1,223 rows, 33 distinct kind values, and 44 scans. The proposed CSV contains 1,240 rows using exactly the seven permitted kind labels. 124 source rows have labels outside the required vocabulary; 17 of those source rows produce two adjacent output rows.

The conversion reads the live inventory and existing metadata labels only. No scan image, transcription page, or context source is read.

## Complete mapping

| Original kind | Input rows | Output kind or ordered pair | Scans | Reason |
|---|---:|---|---|---|
| `annotation` | 1 | `text` | 084 | The recorded annotation is the word OK. |
| `boxed_formula` | 1 | `display` | 079 | The box qualifies a formula; its content is retained as a display. |
| `bracketed_text` | 1 | `text` | 081 | The existing label identifies bracketed text. |
| `bracketed_text_formula` | 1 | `text` + `display` | 086 | The existing composite identifies text and a formula; both kinds receive a row. |
| `claim_formula` | 1 | `text` + `display` | 081 | The recorded incipit begins with prose (Je dis qu’alors) followed by a formula; both kinds receive a row. |
| `clipped_text` | 2 | `text` | 085 | Clipping is retained in the original label and incipit; the content kind is text. |
| `deletion` | 222 | `deletion` | 043, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 061, 062, 063, 064, 065, 066, 067, 069, 070, 071, 073, 074, 075, 076, 077, 079, 081, 082, 084, 085, 086 | Already one of the permitted labels; retained unchanged. |
| `deletion_insertion` | 3 | `deletion` + `insertion` | 077, 081 | The existing composite names both revision states; it is split in that order. |
| `diagram` | 182 | `diagram` | 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 056, 057, 058, 059, 061, 062, 063, 065, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076, 079, 081, 084, 086 | Already one of the permitted labels; retained unchanged. |
| `display` | 330 | `display` | 043, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 061, 062, 063, 065, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076 | Already one of the permitted labels; retained unchanged. |
| `drawing` | 43 | `drawing` | 046, 049, 050, 051, 052, 054, 055, 056, 057, 058, 061, 062, 063, 065, 067, 068, 069, 072, 073, 074, 075, 076, 078, 079, 084, 086, 087 | Already one of the permitted labels; retained unchanged. |
| `faded_typed_text` | 4 | `text` | 082, 083, 085, 087 | Fading and typescript are retained in provenance; the content kind is text. |
| `formula` | 24 | `display` | 077, 079, 081, 084 | The existing label identifies a formula. |
| `insertion` | 51 | `insertion` | 045, 046, 047, 048, 049, 051, 053, 054, 055, 056, 058, 061, 064, 065, 066, 068, 069, 074, 075, 077, 081 | Already one of the permitted labels; retained unchanged. |
| `margin note` | 36 | `margin note` | 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 058, 061, 069, 071, 074 | Already one of the permitted labels; retained unchanged. |
| `marginal_formula` | 4 | `margin note` | 079, 081, 086 | The whole recorded element is a margin note containing mathematics. |
| `marginal_note` | 3 | `margin note` | 077, 079, 081 | This is the existing margin-note label with its required spelling. |
| `overtyping` | 15 | `text` | 080, 082, 083, 085, 087 | The proposed broad category is text; cancellation/insertion states are not assigned from metadata alone. See the explicit ambiguity below. |
| `page_number` | 16 | `text` | 077, 078, 079, 080, 081, 082, 083, 084, 085, 086, 087 | The original page-number text is retained verbatim. |
| `question` | 2 | `display` | 077 | Both recorded incipits are mathematical expressions with an epi/mono property; their question role remains in provenance. |
| `question_formula` | 1 | `display` | 079 | The recorded incipit is a formula with a question mark; no separate prose component is recorded. |
| `stray_typed_marks` | 5 | `text` | 080, 082, 083, 085, 087 | The existing metadata identifies typescript marks; their descriptions remain unchanged. |
| `symbol` | 1 | `display` | 086 | The existing label identifies a standalone mathematical symbol. |
| `symbols` | 1 | `display` | 084 | The existing label identifies standalone mathematical symbols. |
| `text` | 235 | `text` | 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079 | Already one of the permitted labels; retained unchanged. |
| `text_formula` | 11 | `text` + `display` | 077, 081, 084 | The existing composite identifies text and a formula; both kinds receive a row. |
| `text_insertion` | 1 | `text` + `insertion` | 081 | The existing composite identifies text and an insertion; both kinds receive a row. |
| `title` | 1 | `text` | 078 | The original title text is retained verbatim. |
| `typed_section` | 5 | `text` | 080, 082, 083, 085, 087 | Section structure and typescript remain in provenance; the content kind is text. |
| `typed_text` | 15 | `text` | 080, 082, 083, 085, 087 | The content kind is text; the typescript qualifier remains in provenance. |
| `underbrace` | 1 | `display` | 084 | The recorded element is a mathematical underbrace and its formula label. |
| `underline` | 3 | `text` | 080, 083, 087 | The recorded underlined words remain text; the underline qualifier remains in provenance. |
| `unfinished_formula` | 1 | `display` | 086 | The unfinished state remains in provenance and in the unchanged incipit. |

## Exact forward and inverse operations

For each source row, the forward operation copies all eight fields. It substitutes the required kind label and retains the original element ID for the first output row. Each additional row receives the same original content, position, scan, sheet kind, cote, and transcribed status, with a unique role suffix on its element ID. The original incipit is copied in full into every split row; no fragment of it is inferred or discarded.

The provenance sidecar records the original kind, original element ID, source record index, and ordered output IDs for every input row. The inverse reads the first output for each source record, restores the saved original kind and element ID, and places the recovered row at its original record index. This inverse reconstructed every original row dictionary in its original order; all eight field values matched the input exactly.

Verified: True; unique output element IDs: True; exact ordered reconstruction: True; all source/output transcribed values are yes: True.

## Split-row provenance

| Original element | Original kind | Output elements and kinds |
|---|---|---|
| `077.05` | `deletion_insertion` | `077.05` → `deletion`; `077.05.insertion` → `insertion` |
| `077.10` | `text_formula` | `077.10` → `text`; `077.10.display` → `display` |
| `077.12` | `text_formula` | `077.12` → `text`; `077.12.display` → `display` |
| `077.14` | `text_formula` | `077.14` → `text`; `077.14.display` → `display` |
| `077.16` | `deletion_insertion` | `077.16` → `deletion`; `077.16.insertion` → `insertion` |
| `077.17` | `text_formula` | `077.17` → `text`; `077.17.display` → `display` |
| `077.21` | `text_formula` | `077.21` → `text`; `077.21.display` → `display` |
| `081.03` | `text_formula` | `081.03` → `text`; `081.03.display` → `display` |
| `081.05` | `text_formula` | `081.05` → `text`; `081.05.display` → `display` |
| `081.08` | `text_formula` | `081.08` → `text`; `081.08.display` → `display` |
| `081.09` | `text_formula` | `081.09` → `text`; `081.09.display` → `display` |
| `081.10` | `deletion_insertion` | `081.10` → `deletion`; `081.10.insertion` → `insertion` |
| `081.12` | `text_formula` | `081.12` → `text`; `081.12.display` → `display` |
| `081.14` | `text_insertion` | `081.14` → `text`; `081.14.insertion` → `insertion` |
| `081.16` | `claim_formula` | `081.16` → `text`; `081.16.display` → `display` |
| `084.17` | `text_formula` | `084.17` → `text`; `084.17.display` → `display` |
| `086.15` | `bracketed_text_formula` | `086.15` → `text`; `086.15.display` → `display` |

## Classification requiring principal-reader judgment

**overtyping — 15 source rows.** The existing label and per-scan metadata identify superimposed typescript, but do not assign old/new cancellation or insertion states to every overstruck character. A text classification retains the printed marks without adding those states.

Proposed category: `text`. A cancellation/insertion split remains a principal-reader decision; the proposal preserves the existing detailed label in provenance and assigns no such states from metadata alone.

Affected elements: `080.03`, `080.06`, `080.09`, `082.04`, `082.08`, `082.10`, `083.03`, `083.07`, `083.10`, `085.04`, `085.10`, `085.12`, `087.03`, `087.08`, `087.11`.

No other kind classification remained unresolved on the supplied label and incipit evidence. Qualifiers such as faded, clipped, typed, boxed, and underlined remain in the original-kind field of the sidecar.

## Resulting kind counts

| Required kind | Output rows |
|---|---:|
| `text` | 317 |
| `display` | 375 |
| `diagram` | 182 |
| `drawing` | 43 |
| `margin note` | 43 |
| `insertion` | 55 |
| `deletion` | 225 |

## Files and reproduction

- Input: `/workspace/scratch/df60b930783b/MPL_134-8_043-087/MPL_134-8_043-087_inventory.csv`
- Proposed CSV: `/workspace/scratch/df60b930783b/MPL_134-8_043-087/records/inventory_proposed.csv`
- Full mapping: `records/inventory_kind_mapping.json`
- Complete row provenance and verification: `records/inventory_conversion_provenance.json`
- Explicit ambiguity record: `records/inventory_kind_ambiguities.json`
- Conversion script: `scripts/propose_inventory_kinds.py`

Run the script again after any inventory changes. It refuses to use the live input path as the output path and writes a separate proposal by default.

```sh
python MPL_134-8_043-087/scripts/propose_inventory_kinds.py
```

Generated UTC: 2026-11-15 11:18:53 UTC

Source SHA-256: `7a255f4b5dabb449a068dce5f0c45f6f58b3e72aa2422f653d1bc1b803d2134d`

Proposed CSV SHA-256: `942a4152982e51065cb886e224e6562ed00d8b52e53daa431b207ef64099ad5d`

These hashes describe this preparation run. The script leaves the source CSV and all per-scan JSON records unchanged.
