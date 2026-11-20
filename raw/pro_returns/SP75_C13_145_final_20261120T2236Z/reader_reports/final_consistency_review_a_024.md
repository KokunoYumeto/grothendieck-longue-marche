# Scan024: read-only post-audit consistency review

Reader A reviewed the accepted page, reviewed report and adjudication after the audit reported complete at 22:09:31 UTC on 20 November 2026. No image, witness, first-reading file or other scan was read for this review. No primary or audit file was changed. The existing `\mathbb\Gamma` serialization is treated as the accepted double-stroke Gamma; its planned serialization replacement is outside this review.

## Result

**No required metadata synchronization was found.** The three accepted revisions, B02, B04 and B11, are consistently represented in the current page and report. All 66 checked current quotation fields—25 change finals, nine indexed decisions, five unlisted C-mark decisions, 16 doubts and 11 adjudicated finals—occur in the page after whitespace-only normalization. All three accepted page-edit replacements are present. All shared audit-row fields agree with the adjudication, and all eight `report_replace` collections match the current report exactly.

| Accepted locus | Current representations checked | Finding |
|---|---|---|
| B02: older ornate S beneath the first intersection’s replacement Gamma | Page `\underset`, `changes[s024-05]`, `inventory[E04]`, `unlisted_decisions[U024-01]`, relevant doubts, audit final | The older symbol is beneath the replacement, with its doubt retained; it is not a separate product factor. |
| B04: live NB level with the lower diagram row; tentative older Gamma beneath lower ornate S | Page diagram, `changes[s024-08]` and `[s024-24]`, `decisions[M0862]`, `inventory[E07]` and `[E23]`, `doubts[14]`, `notation[1]`, `notes[11]` | Placement and older-letter uncertainty agree throughout. The new old-Gamma locus is separately inventoried and counted. |
| B11: short topolog-t/full-word alternative | Page `\unsure{topolog\textsuperscript{t}|topologiquement}`, `changes[s024-25]`, `doubts[15]`, `abbreviations[4]`, `notes[11]` | The shorter form remains preferred and the full word remains an explicit alternative. The abbreviation expansion is conditional. |

## Counts and historical scope

Current collections contain 25 unique change IDs, 23 unique inventory IDs, 16 doubts, nine indexed decisions, five unlisted C-mark decisions, five abbreviation entries and all 35 consecutive source-difference coverage rows. Every coverage reference resolves to an existing change. The new inventory ID E23 appears beside its diagram context; its nonterminal list position is intentional and does not duplicate an ID.

The inventory has seven deletion loci, matching seven `\deleted{` occurrences in the current page, and two insertion loci, matching two `\inserted{` occurrences. **Keep `c_markup_audit.deleted_spans = 6`:** that field counts C’s six source deletions, not the current page’s seven. Its six detail records, two insertion detail records, nine indexed marks and five unlisted C doubts remain internally consistent. The audit-added old Gamma is already covered by s024-24/E23 and is not a newly discovered C mark.

`crop_count = 12`, the 12-entry crop manifest and the root’s twelve-crop account describe the first pass. The blind audit separately records 12 boxes, 11 differing boxes and three changed boxes. B12 is the unchanged footer. These totals are consistent and should not be collapsed into one crop count. The 30 line units are explicitly a first-pass reading count; this text-only review does not independently recount physical lines or propose altering that historical count.

## Structure and mathematical scope

Static checks found balanced TeX groups, 36 inline dollar delimiters, five display pairs, one matched `aligned` environment and one matched `tikzcd` environment. No TeX compilation was performed. The accepted lower-row NB is inside the diagram’s lower row; no additional top-row NB remains in the live margin.

The mathematical notes remain qualified: `notes[8]` conditions the finite-subgroup calculation on the preferred but uncertain Gamma-subscript reading and the stated embedding; `notes[9]` leaves the marginal equality unresolved; `notes[10]` compares both conjugator conventions without determining inverse cancellation state. No note resolves the new older Gamma or topolog-t doubt.

## Reviewed source hashes

| File, relative to edition | SHA-256 |
|---|---|
| `pages/145_scan024.tex` | `6c3df672a4036dd92bb200d68332b7b21720bc0693bb20739dde34bbb4fa4ae8` |
| `reader_reports/145_scan024_reviewed.json` | `ff32ae779b73e2a380758fe704ba46ebf0e5748ffd7965ac8d0d0185c8cff09e` |
| `second/145_scan024_adjudication.json` | `8d03c4868590ab97f2c329cf33efc775f7e2d4c0b1e78e45a5c6c82553f8487c` |

These hashes identify the reviewed state before the planned Gamma serialization work. No alteration is proposed to immutable first/second readings, historical `second_boxes`, C/H quotations or adjudication snapshots.
