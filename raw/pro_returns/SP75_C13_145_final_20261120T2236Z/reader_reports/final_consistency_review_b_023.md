# Read-only consistency review — scan 023

Reader B reviewed the completed page, current reviewed report, adjudication, comparison TSVs and coverage metadata. No image was reopened, no new ink decision was made, and no OCR, external research or TeX compilation was used. This review does not alter the accepted page or historical readings. Paths below are relative to `edition/`.

## Confirmed stale fields

### 1. Two observations still call the opening word uncertain

**File:** `reader_reports/145_scan023_reviewed.json`.

- `notes[0]` says: “The opening inverse preference is determined from the local strokes and remains doubtful”.
- `hand[0].witness_effect` says: “The opening word remains inverse-first uncertain”.

The accepted page begins with plain **inverse**. Change s023-01 has final `inverse`, confidence `high`, and the accepted B01 audit explicitly resolves that reading. The later note11 also states that it is resolved, and the former opening-word doubt is no longer in the current doubts list. The two earlier statements therefore contradict the current decision.

**Suggested synchronization:** Replace only the assertions of continuing uncertainty with an explicit statement that the blind audit resolves the word as inverse. Preserve the surrounding Malgoire observations, the explanation of compressed cursive, and the separate comments about H's readings of désignera and the signature phrase. No page, decision, confidence, audit or count change is required.

### 2. Inventory I09 omits the accepted old-index alternative

**File/locus:** `reader_reports/145_scan023_reviewed.json`, inventory I09, “(17), first row, earlier second RHS index”.

Its current quotation is:

```tex
\deleted{\unsure{\infty}}
```

The accepted page, s023-06, U023-03, the matching doubt entry and final B03 instead retain:

```tex
\deleted{\unsure{\infty|0}}
```

**Suggested synchronization:** Update only I09's `first_words_or_objects` to the accepted qualified old index. Preserve its deletion kind, position, coordinates, hand, element ID and transcription status. The live following index1 and all current loop products remain unchanged.

## Other focused checks

The cancelled short word is consistently retained as `relati.` / `relat.` across the page, s023-04, U023-01, doubts, inventory I04 and the abbreviation entry. The newly qualified first cancelled tau1 factor is present in the page, its dedicated doubt, inventory I06 and B03. The other overwritten indices retain their distinct local uncertainties; they are not normalized by a cyclic identity.

The seven local capital-Pi readings agree between the page and notation observation. The detached marginal rho remains unfinished; no equation has been supplied. The vertical sign under the double-hatted Gamma remains qualified as bars/cup. The four terminal points, the inserted generator phrase and the cancelled extérieurs/live à states are retained. The mathematical notes remain explicitly independent of the uncertain old indices.

No additional duplicate substantive locus was identified. The seven Pi corrections refer to separate occurrences. The 31 coverage records use both `change_id` and `change_ids`; every referenced ID exists, and the plural-valued rows account for distinct components of a single raw difference.

## Traceability check

The **13 prescribed boxes**, **12 token-differing boxes** and **3 explicitly changed audit boxes** agree across the available records. Both reading hashes and the boxes hash match the pre-comparison receipt; the first-reading hash matches the seal, and the report's retained first-box readings match the immutable first TSV. The final/adjudication/ink fields agree between comparison, report audit and adjudication records. Referenced crops exist; none was opened.

All **31 raw-difference rows** are covered in order, with valid change references. The accepted page occurs verbatim in the combined transcription and has even inline-math delimiter parity. Current substantive counts are **31 loci, 11 against C and 30 against H**; the three metadata synchronizations above do not alter those counts or the audit's changed-box count.

Root requested inclusion of these three exact field corrections in the separately staged metadata plan. This report records the pre-correction snapshot and is to remain unchanged when that plan is applied.
