# Scan025: read-only post-audit consistency review

Reader A reviewed the accepted page, reviewed report and adjudication after the audit reported complete at 22:13:45 UTC on 20 November 2026. This extends the separate scan024 review. No images, witnesses, sealed first/second readings or other scan materials were opened. No primary or audit file was changed.

## Result

**The accepted readings, current decision states, doubts and inventory agree.** Two coverage explanations should extend their final-paragraph references to the new s025-32 record. A minor prose typo survives in the immutable B03 ink account and its report mirror. Neither issue affects the page transcription.

| Accepted audit locus | Current records checked | Result |
|---|---|---|
| B01: retraced exponent alpha/beta | Page, `doubts[14]`, `notes[0]`, audit B01 | The exponent is `\unsure{\alpha_i|\beta_i}`; the clearer later parenthetical alpha remains unchanged and is explicitly not used to settle the earlier glyph. No new change row is needed for this additional doubt alone. |
| B05: reopened M0864 and crossed phrase | `decisions[M0864]`, `changes[s025-12]`, `unlisted_decisions[U025-08]`, `doubts[7]` and `[24]`, `inventory[I20]`, coverage rows23–24, `notes[2]` | M0864 is undecided at low confidence; groupe/formé/formée and par le couple/par les couples/par le groupe are consistently retained. |
| B05: separate mark above des | Page drawing, `changes[s025-31]`, `inventory[I46]`, `hand[5]`, `notes[2]` | The mark is reproduced geometrically above des, without an assigned letter or function. I46 is unique and is placed beside its definition context. |
| B07: colon after aura | Page, `changes[s025-30]`, `doubts[26]`, `inventory[I27]`, `notes[13]` | `\unsure{:}` is retained consistently. Both witness-change flags are true for the omitted inscription. |
| B08: reopened M0865 and cancelled dot/colon | `decisions[M0865]`, `changes[s025-16]` and `[s025-18]`, `unlisted_decisions[U025-10]`, `doubts[9]` and `[25]`, `inventory[I28]`, `[I29]`, `[I32]`, coverage row30, `notation[4]`, `notes[3]` | M0865 is undecided at medium confidence. The weak opening is qualified, the preferred expression still has its unmatched outer opening, and the old separator retains dot/colon alternatives. |
| B10: square brackets around the marginal index list | Page, `changes[s025-23]`, `unlisted_decisions[U025-14]`, `notation[5]`, `notes[4]` | The current reading is `\Pi^{[0,1,\infty]}`. U025-14 records the resolved first alternative at high confidence; the former delimiter doubt is absent from the current doubt register. |
| B11: absent exclamation on map domain only | Page, `changes[s025-26]` and `[s025-32]`, `notation[6]`, `notes[5]` | The domain immediately before the arrow has no exclamation. The earlier S-extension and the Aut ext target retain theirs. The upper-wave qualification remains. Both witness-change flags in s025-32 are true. |

The new drawing s025-31 also has both witness-change flags true. Existing false C-change flags on s025-12, s025-16 and s025-18 do not claim certainty: their current changes broaden uncertainty while retaining C-supported readings. The corresponding H departures remain recorded. No additional flag correction is proposed.

## Exact metadata proposals

These are proposed report-only synchronizations. Do not apply them to sealed audit records or to the adjudication’s historical `report_replace` snapshot as part of this review.

### 1. Coverage row34

Path: `reader_reports/145_scan025_reviewed.json` → `diff_coverage[33].explanation` (`row = 34`). Keep its existing status and `change_id = s025-22`.

**Old**

> Margin/main-text ordering creates the long alignment shift. The entire margin is transcribed; s025-22 to24 cover its differences, s025-25 to29 the final paragraph.

**Proposed**

> Margin/main-text ordering creates the long alignment shift. The entire margin is transcribed; s025-22 to24 cover its differences, s025-25 to29 and s025-32 the final paragraph.

### 2. Coverage row38

Path: `reader_reports/145_scan025_reviewed.json` → `diff_coverage[37].explanation` (`row = 38`). Keep its existing status and `change_id = s025-24`.

**Old**

> The margin has no final stop. The displaced main paragraph includes the crossed groupe, local upper mark, final product uncertainties and omitted footer24, covered by s025-25 to29.

**Proposed**

> The margin has no final stop. The displaced main paragraph includes the crossed groupe, local upper mark, absent map-domain exclamation, final product uncertainties and omitted footer24, covered by s025-25 to29 and s025-32.

### 3. B03 prose erratum; preserve immutable records

The exact phrase `DonC is written as donc on the following line; no punctuation is supplied from spacing macros.` occurs in:

- `second/145_scan025_adjudication.json` → `differences[2].ink` (`box = B03`);
- `reader_reports/145_scan025_reviewed.json` → `audit.differences[2].ink` (its exact mirror).

For an errata note or a separately authorized prose correction, use: `The following line reads donc; no punctuation is supplied from spacing macros.` This corrects only the accidental mixed-case explanatory word. The manuscript reading is already lowercase donc throughout the page, s025-09 and coverage row17. **No immutable record was edited.**

## Counts, quotation scope and structure

The report has 32 unique change records, four indexed decisions, 14 unlisted-decision records, 27 doubts, 46 unique inventory IDs, six abbreviation entries and all 38 consecutive source-coverage rows. Every coverage `change_id` resolves. The root-review account of **thirteen unlisted C doubts** remains correct: U025-01 through U025-13 are the C-doubt audit; the new U025-14 explicitly identifies a doubt introduced by the first consolidated reading, not an indexed C mark. Do not relabel that historical count as fourteen C doubts.

All eleven blind boxes have adjudications; six boxes changed: B01, B05, B07, B08, B10 and B11. All seven accepted page replacements are present. All shared audit-row fields match the adjudication, and all nine `report_replace` collections match the current report at the reviewed state.

Of 87 nonempty current quotation fields, 83 are direct page substrings after whitespace-only normalization. The remaining four pass at their documented component scope: s025-17, U025-11 and its doubt record isolate the inserted-and-cancelled upper expression inside the page’s longer insertion wrapper; audit B08 combines the complete (24) display with the physically included later inserted S-group, separated by prose in the page’s linear serialization. Their underlying text and states agree. Inventory I30 uses the same isolated inserted component. M0863 has an intentionally empty reading because the supplied à was rejected.

The inventory contains 15 deletion records, six insertion records and three drawings. These are not interchangeable with macro counts: the page has 19 deletion macros because the four upper-wave alternatives each include a possible deletion; five insertion wrappers encompass six separately inventoried physical insertion loci. The first-pass note about fifteen C cancellation ranges and five C insertion ranges therefore remains historical source coverage. The 38 line units and eleven first-pass crops are likewise retained as provenance, not recounted from images.

Static checks found balanced TeX groups, 56 inline dollar delimiters, seven paired displays and three matched `tikzpicture` environments. The dollar check allows the text-box math span in the (23) TikZ node. The authorial round-parenthesis imbalance remains intentionally untouched. No TeX compilation or mathematical certificate execution occurred.

The mathematical discussion is conditional on the conjugator convention and, where needed, the stated group/centralizer assumptions. Its generic alpha/beta parameters do not resolve the opening glyph; the notes explicitly retain that doubt. The cocycle check does not supply the weak parenthesis, and the kernel discussion does not supply the absent domain exclamation.

## Reviewed source hashes

| File, relative to edition | SHA-256 |
|---|---|
| `pages/145_scan025.tex` | `c67f85179618c5f98d2419945dffc66c588d8e2c383219cccf85756ed066ceef` |
| `reader_reports/145_scan025_reviewed.json` | `e129da15f8f496e1b6ba371eb70f955795fb70c35c5010ba126dac08c0b754ff` |
| `second/145_scan025_adjudication.json` | `5e4f109e84197add51edbeae280b2f289c1ca2b72762fa2a07ee7966cca0d32c` |

Only this review file was written for scan025. All accepted pages, report data, audit records and sealed readings remain unchanged by this review.
