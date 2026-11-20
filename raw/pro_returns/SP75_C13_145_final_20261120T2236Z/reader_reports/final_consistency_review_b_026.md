# Read-only consistency review — scan 026

Reader B reviewed the accepted page, current reviewed report, adjudication, comparison TSVs, generated apparatus and coverage metadata following the audit recorded at 22:17:06 UTC. No image was opened, no new ink decision was made, and no OCR, external research or TeX compilation was used. Only this review file was written. Paths below are relative to `edition/`.

## Outcome

The substantive current readings are synchronized. The expanded alternatives requested for review are present in the accepted page and their applicable current decision, doubt, change and inventory fields. No change to the accepted page or the substantive counts is proposed. Two small descriptive/abbreviation entries should be clarified to avoid suggesting that older, narrower readings remain current.

### Minor synchronization recommendations

**1. The cancelled u is still called simply “tilde-u” in two locators.**

In `reader_reports/145_scan026_reviewed.json`:

- `changes[id=s026-19].place` remains “last cancelled line, second surviving cluster before tilde-u”.
- `diff_coverage[row=18].explanation` begins “The ink has two separated short clusters before tilde-u” and mentions only the older i.e./si candidates.

The accepted last cancelled line now has a hat-first hat/tilde alternative, and its first cluster has i.e./ici alternatives. The page, s026-18, s026-33, corresponding doubts, inventory I14, notes3/13 and the final B06 audit agree on those qualifications.

**Suggested wording:** Use “before the hat/tilde-qualified cancelled u” in the locators. In coverage row18, retain the explanation that H suggested i.e. and C suggested si, while making clear that the current first cluster is i.e./ici and the separate second cluster remains doubtful si. The linked change IDs can stay as they are: they identify the two raw-difference clusters, while the separate accent correction is documented in s026-33.

**2. The abbreviation entry records only the possible i.e. branch of the expanded first cluster.**

`abbreviations[2].form` remains `\unsure{i.e.}`, with a possible *id est* expansion and the location “first cluster of the cancelled last line”. The accepted written cluster is `\unsure{i.e.|ici}`.

This can legitimately be an entry for the possible abbreviation alone, but that narrower scope is not explicit in its location label. Either reproduce the full written alternative and explain that only the i.e. branch would expand to *id est*, or label the entry expressly as the possible i.e. branch of the i.e./ici cluster. No expansion should be inserted into the transcription. The current page and doubt record already preserve both readings.

## Focused checks that passed

- **Opening alpha mark:** The page, s026-32, the dedicated doubt, inventory I01, notation0/6 and B01 all retain raised-i / lower-i / prime alternatives, with raised i first. The known `\alpha\prime` serialization is reserved for reader C's documented typography stage; it is not treated here as a new ink decision or a reason to change counts.
- **Initial cancelled word and second old product:** The accepted de/des/dans alternatives appear in the page, s026-01, doubt and inventory I03. The second trial's inverse-present / no-inverse alternatives agree across the page, s026-04/05, U026-02, doubt, inventory I05 and B02. Coverage row7 describes the historical C candidate's uncertain inverse; that wording does not contradict the fuller current alternative.
- **Extra upper marks on both group names:** Both occurrences retain the live-wave / cancelled-wave / infinity-shaped options in the page, s026-08/12, doubts, notation1 and B03. Their short inventory labels describe the visible upper trace without asserting an exhaustive lexical interpretation. The marginal group names remain separately single-hatted.
- **Old phrase after live par:** The page, s026-13, U026-04, doubt, inventory I11, notes5 and B04 retain leurs / par la / de la. The preceding par remains live and conjugaison remains outside the cancellation.
- **Opening before barred u:** The weak opening parenthesis is qualified in the page, dedicated doubt, inventory I13, notes1 and B06. M0867 continues to resolve the bar on the live right-hand u, which is a different sign from that parenthesis and from the accent on the cancelled u below.
- **Cancelled hat-u / tilde-u:** Apart from the stale descriptive locators above, the accepted accent alternatives agree in the page, s026-33, dedicated doubt, inventory I14, notation6, hand5, notes3/13 and B06. The full cancellation state is retained.

## Counts and overlapping loci

Current counts are **33 substantive loci: 7 against C and 31 against H**. No row has both witness-change flags false, and no duplicated substantive locus was identified.

The newly qualified opening parenthesis is correctly retained as a doubt without a separate substantive change row. By contrast, s026-32 changes the preferred opening alpha mark from the witnesses' lower index to raised i, and s026-33 changes the preferred cancelled-u accent from tilde to hat while preserving alternatives. Those are preferred glyph/placement changes, not merely new doubt wrappers around an unchanged preferred reading.

The two additional group traces occupy separate physical occurrences. Broadening their shape alternatives does not create additional change rows. The two old cancelled products and H's duplicated live product/order are also distinct issues; their contextual quotations overlap without duplicating the same substantive correction.

## Traceability verification

The **8 prescribed boxes**, **7 token-differing boxes** and **5 explicitly changed audit boxes** agree across the available records. Both reading hashes and the boxes hash match the pre-comparison receipt; the first-reading hash matches the seal, and the report's retained first-box readings match the immutable first TSV.

The comparison and report-audit readings agree; final/adjudication/ink fields and changed flags also agree with the adjudication file. All referenced differing-box crops exist, but none was opened. All **25 raw-difference rows** are covered in order, and both singular and plural change-reference fields resolve to existing IDs.

The **31 H-collation rows** faithfully match their report fields. The single listed decision, M0867, agrees with the global decision table. The accepted page occurs verbatim in the current combined transcription and has 34 unescaped dollar signs. Mathematical check events and their stated limitations remain separate from the new ink qualifications.

No correction was applied by this reviewer. The minor metadata recommendations do not affect source text, witness-departure counts, audit changed-box counts or the pending typography-only repair.
