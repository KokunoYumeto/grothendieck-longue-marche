# Mechanical record consistency review

This review was performed after the ordered second visual audit, on the documentation snapshot containing 492 change rows, 433 H-collation rows, 162 supplied-mark decisions, 573 inventory entries and 13 mathematical check events. Later reader amendments may change those totals; the final generated reports and validation log govern the final counts.

## Scope and division of work

A separate assistant checked tabular structure, field agreement and the supplied H transcription's explicit doubt markup. It did not inspect manuscript images, use OCR, interpret handwritten letters, adjudicate a manuscript reading, edit page TeX, or perform an independent mathematical proof. All ink decisions and both ordered readings belong to the primary reader. This review is supplementary to the final structural validator and hash check.

## Checks completed

- Every H-collation row matched the corresponding change row's scan/place, C reading, H reading, final reading, evidence, crop reference, kind and confidence. All H page numbers were the scan number minus one; every folder was 142.
- The number of collation rows equalled the number of change rows with `against_H=yes`. No change row claimed neither witness differed.
- Change IDs, change scan/place pairs, collation scan/line pairs and inventory element IDs had no duplicates.
- The 162 decision IDs, cotes and scans matched `MARKS.tsv` exactly and in its original order.
- All 24 requested scans were represented in the inventory, and every recorded element had `transcribed=yes`. This checks register coverage; it is not an independent visual completeness assessment.
- Confidence fields used the documented high/medium/low values. Remaining doubt confidence was distinct from confidence in a passage's presence or deletion state.
- The 13 check events had identifiable manuscript locations and outcomes. Their conditional assumptions and limited scope were explicit. The notes distinguished descriptions of manuscript assertions from independent verification; no event claimed an independent re-proof of the overall groupoid argument.

## Corrected H doubt flags

The original H files contain explicit `\uncertain{...}` or `\ill{}` at 34 changed passages whose collation rows had `marked_in_H=no`. Those flags were changed to `yes`; every other field and the entire row order were preserved. The resulting snapshot has 84 yes flags and 349 no flags. A neighboring uncertain phrase was not treated as marking a separately transcribed, unmarked symbol.

The corresponding change IDs are:

| Scan | Change IDs |
| --- | --- |
| 026 | 026-01 |
| 027 | 027-06, 027-22 |
| 028 | 028-02, 028-16, 028-17, 028-22 |
| 029 | 029-02, 029-04, 029-19, 029-21 |
| 041 | 041-07, 041-12, 041-13 |
| 044 | 044-01, 044-15, 044-16, 044-17, 044-24, 044-25 |
| 045 | 045-06, 045-08, 045-11 |
| 047 | 047-01, 047-12 |
| 048 | 048-12 |
| 050 | 050-08, 050-11, 050-13, 050-23, 050-24 |
| 051 | 051-06, 051-07, 051-08 |

## Findings passed to the primary reader

The prose note for scan 041 still described 79/78 as unresolved after the visual audit had selected 79. The scan 030 note still referred to a provisional zeta reading and an outstanding notation comparison. The primary reader was notified to reconcile these with the final audit and notation review.

The reviewer initially reported apparent doubled backslashes in 37 instances of the `readable ink left as \ill{}` kind. Direct character-count verification during final reconciliation corrected that report: the initial report had confused escaped tool-output representation with literal file content. Both checkpoint 02 and the final table contain exactly one U+005C backslash in every such kind value. No repair of those 37 category strings was necessary.

## Final reconciliation

After the primary reader's final notation and documentation amendments, the mechanical comparison was repeated on 502 change rows and 443 H-collation rows. All row correspondence checks passed again, including readings, evidence, crop references, confidence, kind, page offset and folder. The change table records 163 places differing from C. Every one of the 34 corrected H doubt flags survived the collation rebuild; the final collation has 84 yes flags and 359 no flags.

All 492 earlier change IDs remain. Exactly ten new change IDs were added: 027-24, 027-25, 027-26, 028-27, 028-28, 028-29, 028-30, 030-30, 030-31 and 030-32. The H collation grew by ten rows in total. The earlier grouped Roman-label row 030-29 remains under its revised, more specific place description; its former scan/place key therefore changed without deleting the change ID.

The 162 supplied-mark decisions still match the original register exactly in ID, cote, scan and order. The 573 inventory entries still cover all 24 requested scans and all say `transcribed=yes`. The final crop register contains 144 entries, and the regenerated remaining-doubt table contains 126 occurrences. These are mechanical counts, not additional manuscript readings.

The scan 041 note now records the audit's medium-confidence resolution to 79. The scan 030 note now records the completed zeta comparison and distinguishes the separate uncertain cancelled xi-like signs. All 37 `readable ink left as \ill{}` kind strings were verified to contain the required single literal backslash; as explained above, this was a confirmation rather than a repair.

The notes and all 13 check-event records were compared again for statements explicitly presented as checked. Each actual algebraic, endpoint, indexing, quadratic-form, Euler-characteristic or tangent-orientation check described in the notes has a corresponding event and an identifiable scope. Descriptions of manuscript assertions, visual symbol comparisons and explicitly unproved presentations were not reclassified as mathematical proof events. This was a completeness review of the records, not a new proof or refutation.
