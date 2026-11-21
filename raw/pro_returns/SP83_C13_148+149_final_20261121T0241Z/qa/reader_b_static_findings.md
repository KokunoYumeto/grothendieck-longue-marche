# Reader B: static QA findings

This was a read-only check of the documentation, records and frozen reading files against the governing prompt. It makes **no new manuscript-reading decisions**. The snapshot had **23 pages, 16 completed audits, 261 supplied doubt decisions, 707 material places, 262 C differences and 634 H differences**. The seven unfinished audits were expected.

## Actionable findings

| ID | Priority | Exact record or note | Required follow-up |
|---|---|---|---|
| BQA-001 | High | **148_scan058-01**, **148_scan058-N07** | The final old adjective is `ord.\|sol.`, while H still has `ordinaires`; `diff_h=false` is stale. Set it true if that final reading remains. This adds **one H difference**, without adding a material place. Update N07's old macro-order-only explanation. |
| BQA-002 | Conditional | **148_scan067-15**, **148_scan067-26** | Their current C primary readings are unchanged; only alternatives were added. If the pending audit keeps these readings, set `diff_c=false` for both. H differences remain. Conditional effect: **two fewer C differences**, unchanged place/H totals. |
| BQA-003 | High | **148_scan064-N04** and its **CHECK_EVENTS** outcome | They still say Sigma is “formally empty.” The accepted text and N-audit now say it “ne joue aucun rôle.” Update the source summary and carried-background outcome. |
| BQA-004 | Medium | **148_scan064-N05**; notation entry **Curved insertion leaders** | They still treat the opening before `en tant que` as unsupported. The audit restored separate opening parentheses before `en tant que` and `d'un`. Remove the obsolete witness-error claim. |
| BQA-005 | Medium | **148_scan061-N03**, its check event, notation entry **mathbb Z** | The old target-numerator `Z/Z_a` doubt remains in these summaries. **148_scan061-28** now has unindexed target Z letters and a **d/d_a** multiplier doubt. Synchronize those descriptions. |
| BQA-006 | Medium | **148_scan053-N02** | It asserts gamma weighting and cancellation of `bi`. The accepted diagram instead retains **sigma/gamma**, with cancelled **b/ph** and a **live i**. See **053-29** and **053-62**. |
| BQA-007 | Medium | **148_scan063-N06** | Its old unreadable-unit/single-word segmentation is superseded by the current `fl.`, possible `(`, `des`, and `unités/données` reading in the cancelled run replaced by `structures`. |
| BQA-008 | Low | **148_scan058-N03**, **M0746**, **058-19** | `en plus` is still listed as a current alternative, although the audit retained only doubtful `en près`. Remove it from the current summary or label it historical. |
| BQA-009 | Advisory | **notation_final.md**; **061 notation[8]**; **064 notation[4]** | Carry the new **dotted divisibility** form into final notation consolidation, and record the **overline-Sigma** alternative locally in the 064 margin. The tuple's separate ambiguity must keep its own scope. |

The detailed JSON contains the exact stored excerpts and proposed actions. Findings on 067 are explicitly conditional because its adjudication was still in progress.

## Checks that passed

- All **261 MARKS IDs match exactly in order**, with no duplicates. Required record keys and aggregate table columns are present.
- Current aggregate decisions and collation match their page records. All referenced crops exist, and required main-reader view registrations are present.
- All check-event statement IDs resolve to actual notes. Enumerated collation, error-sheet and inventory categories are valid.
- The retained first readings match the frozen `_first.tsv` files; existing comparisons preserve those first readings.
- No confirmed missing remaining-doubt mapping was found. Apparent substring gaps were explained by separate reading/alternative fields, shared cancellation scope or parameterized drawing labels.
- No completed-audit row was found whose material flag merely counts an exact return to C/H. The broad macro comparison's 048 candidates are **real word-gap changes**, not macro-only rows.

## Files and limits

The audit wrote only `result/qa/` files. It did not modify pages, records, frozen TSVs or aggregates; did not inspect manuscript images; and used no OCR, outside research or TeX compilation. Raw candidate diagnostics are retained for reproducibility, but **only the curated findings above are recommendations**. Parent comparison and adjudication remain authoritative.
