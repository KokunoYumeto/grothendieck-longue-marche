# Scan027: read-only post-audit consistency review

Reader A reviewed only the current accepted page, reviewed report and adjudication. No images, witnesses, sealed readings, other scans or mathematical certificates were opened or executed. Only this review was written. All proposals below concern report metadata; accepted page text and immutable audit records must remain untouched.

## Result

**The accepted page and core current readings agree.** All 72 checked quotations—29 change finals, eight indexed decisions, seven unlisted decisions, 18 doubts and ten adjudicated finals—occur in the page after whitespace-only normalization. All eleven accepted page-edit replacements are present. Shared audit-row fields agree with the adjudication, and all ten `report_replace` collections match the current report, including the stale metadata identified below.

The new underbrace relation is qualified; barred j is dotless; the high2/cancellation-scope alternatives are explicit; Pi-conjugués is capital; the separate comma before s’obtiennent is absent; qui/et, the dark middle index1, les/leurs and cancelled ou/un/tau are qualified; both abbreviated endings are raised. The core changes, decisions, doubts and corresponding main-baseline inventory entries preserve these choices.

## Exact current-field synchronization proposals

Paths below are relative to `reader_reports/145_scan027_reviewed.json`; array indices are zero-based. Preserve IDs, coordinates, source quotations, confidence values, witness flags and all other fields unless specifically listed. Do not apply these synchronizations to the adjudication’s historical `report_replace` snapshot.

### A. Inventory quotations

**1. `inventory[2].first_words_or_objects`, E03**

Old:

```tex
Underbrace and $=\unsure{\mathfrak S_3|\mathcal S_3}$
```

Proposed:

```tex
Underbrace and $\unsure{=|\simeq}\unsure{\mathfrak S_3|\mathcal S_3}$
```

The existing bare equals contradicts the accepted B02 qualification. The underbrace’s alphabet doubt remains unchanged.

**2. `inventory[32].first_words_or_objects`, E33**

Old `\unsure{les}` → proposed `\unsure{les|leurs}`.

**3. `inventory[32].position`, E33**

Old `Start of baseline 16: retraced final s in one word` → proposed `Start of baseline 16: one retraced les/leurs word`.

E32 already quotes the accepted full clause correctly; E33 is the smaller overlapping entry that was not synchronized.

### B. C-markup audit: update reading fields, preserve source fields

The C audit appropriately retains six source deletions and six source insertions. Its `source_span` strings are witness quotations and must remain unchanged. Four accompanying `reading` fields still present superseded final readings:

**4. `c_markup_audit.items[1].reading`, deleted ordinal2 / E14 / B05**

Old:

```tex
\deleted{\unsure{\dot\rho}}
```

Proposed:

```tex
\unsure{\deleted{\unsure{\dot\rho^2}}|\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}}
```

**5. `c_markup_audit.items[3].reading`, deleted ordinal4 / E26 / B07**

Old `\deleted{\unsure{qui}}` → proposed `\deleted{\unsure{qui|et}}`.

**6. `c_markup_audit.items[5].reading`, deleted ordinal6 / E34 / B09**

Old `\deleted{\unsure{$\tau$}}` → proposed `\deleted{\unsure{ou|un|$\tau$}}`.

**7. `c_markup_audit.newly_recorded_cancellations[1].reading`, E38 / B10**

Old `pt\deleted{\unsure{s}}` → proposed `p\textsuperscript{t\deleted{\unsure{s}}}`.

These reproduce already accepted readings; they do not add cancellations or alter their scope.

### C. Summaries must preserve the dark-index and scope doubts

**8. `notation[4].observation`**

Old:

> The stabilizer list literally writes sigma indices 1,2,3, whereas the later list and the live lift choices use 0,1,infinity.

Proposed:

> The stabilizer list literally writes sigma indices 1,2,3. The later savoir list has 0, an uncertain index read preferentially as 1, and infinity; the live lift choices use 0,1,infinity.

**9. `notes[2]`: exact sentence replacement**

Old:

> Later on this same sheet he writes 0,1,infinity in the list of elements carrying P to Pbar and in the lift choices.

Proposed:

> Later on this same sheet, the list of elements carrying P to Pbar has 0, a doubtful middle index preferred as 1, and infinity; the live lift choices have 0,1,infinity.

Preserve the rest of the note, including the literal 1,2,3 stabilizer indices and the refusal to normalize the index shift.

**10. `notes[1]`: exact phrase replacement**

Old `for the listed tau-containing involutions.` → proposed `for the listed tau-containing expressions.`

The accepted cancellation-scope alternative can leave a rho followed by tau. The note should not classify every alternative expression as an involution. This wording follows the retained ink states and leaves the separate conditional calculation in `notes[9]` intact.

### D. Cached current totals

| Field | Stored | Recomputed from current records |
|---|---:|---:|
| `validation.c_departures` | 9 | 12 |
| `validation.h_departures` | 26 | 25 |
| `validation.remaining_doubts` | 17 | 18 |

These are three further exact-value proposals. The current change rows themselves already have the correct flags; no row should be added or removed to make the totals agree. The historical `validation.checks` description includes first-pass witness and second-selection checks; changing cached counts must not be represented as a fresh rerun of those historical checks against sealed selections.

### Optional descriptive-label alignment

These labels still use a preferred word alone, although their associated readings are correct. Aligning them would make the reopened alternatives explicit wherever the loci are named:

| Field | Old | Proposed |
|---|---|---|
| `changes[18].place`, s027-19 | After E: cancelled qui before the live qui | After E: cancelled qui/et before the live qui |
| `changes[23].place`, s027-24 | Before produits: one retraced les, no separate extra cancelled token | Before produits: one retraced les/leurs word, no separate extra cancelled token |
| `doubts[9].place` | Cancelled qui after E | Cancelled qui/et after E |
| `doubts[12].place` | Les before produits: final-letter surface state | Word before produits: les/leurs and retraced ending |

These optional label edits do not change the interpretations, confidence or counted departures.

## Certainty-only counting review

**No additional certainty-only change row or witness flag requiring removal was found. No new row is proposed.** The underbrace equals/simeq qualification and dark1 qualifier are uncounted doubts. The dotless-j and raised-letter choices are serialization/placement changes, not separately counted lexical discoveries. The broadened qui/et and les/leurs readings retain false C-change flags in their existing substantive H-departure rows.

The changes that explain the C total moving from9 to12 are substantive: s027-07 records the additional high2-like inscription and scope alternative; s027-16 removes C’s separate comma; s027-25 changes the preferred cancelled recovery from tau to ou/un while retaining tau as an alternative. The comma reversal also explains H’s total moving from26 to25. Resolving capital Pi does not create another row: s027-14 already records an actual case departure from both witnesses’ lower-case pi.

Keep `validation.unlisted_C_doubts = 6`. U027-01 through U027-06 audit C doubts; U027-07 explicitly resolves a case doubt introduced in the first consolidated reading. Seven total unlisted-decision records therefore do not mean seven C-source doubts.

Keep eight physical deletion loci and six insertion loci. The page now contains nine serialized `\deleted{` occurrences because the rho-prefix locus has two mutually exclusive cancellation alternatives. Counting both branches as two physical cancellations would inflate the total. The inventory correctly has eight deletion entries, six insertion entries and 41 unique elements overall.

The 35 line units, fourteen first-pass crops and first reader’s `blind_second_reading_performed = false` remain historical provenance. The separate audit records eleven boxes, ten differing boxes and six changed boxes: B02, B05, B06, B07, B09 and B10. All 37 source-difference rows are present once, with valid change references. No coverage row is newly required for a certainty-only qualification.

## Mathematical and structural scope

Apart from the neutral wording proposed for `notes[1]`, the mathematical notes preserve their limits. `notes[9]` checks rho tau only and expressly refuses to determine the prefix, high2, dot or cancellation scope. The finite-action notes retain the author’s 1,2,3 list and do not restore the doubtful later index. The splitting-transport proof is conditional on the geometric sections and is not a completeness theorem; the broad correspondence is explicitly carried without a completeness proof. No certificate was rerun for this review.

Static checks found balanced TeX groups, 66 inline dollar delimiters and one matched display pair. The two underbrace structures are grouped correctly. The handwritten opening parenthesis followed by a closing brace remains intentionally mismatched. No TeX compilation occurred.

## Reviewed source hashes

| File, relative to edition | SHA-256 |
|---|---|
| `pages/145_scan027.tex` | `6005f8f6ab5c5b4495c0b8d256f4783535b4dba504d64a5be87998a61206a8a6` |
| `reader_reports/145_scan027_reviewed.json` | `81265893d8a1694508b3a5eb939266128a9883c85ad96ebb6909dfd24f4de2bf` |
| `second/145_scan027_adjudication.json` | `8f778d391e72405d990565cc01e471aac413de0a4ef451bad144fdd8e3a254c5` |

No mutation of these files, source quotations, immutable audit snapshots, first/second readings or mathematical certificate outputs was performed.
