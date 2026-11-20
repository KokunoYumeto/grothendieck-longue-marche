# Read-only consistency review — scans 021 and 022

## Scope and method

Reader B reviewed the accepted pages, current reviewed reports, adjudication JSON, first/second comparison records, generated apparatus and raw-difference coverage for scans 021 and 022. This is a documentation and serialization review: no image was reopened, no crop was made, no new ink decision was attempted, and no TeX compilation, OCR or external research was used. Only this review file was written.

Paths below are relative to `edition/`, except the explicitly identified packet difference files. Historical first/second readings, audit outcomes and accepted page text are not proposed for alteration. The two factual issues concern substantive-locus counting and hand-attribution wording.

## Factual findings

### F1 — Scan 022's newly qualified Gamma separator is counted as a substantive change although the preferred reading is unchanged

**Files/locus:** `reader_reports/145_scan022_reviewed.json`, change `s022-26`; the corresponding collation and count/feedback outputs; `scripts/build_edition.py`, lines 25–29 and 54–64 in the reviewed snapshot.

The change row records:

```tex
C:     \Gamma_{0,3}
H:     \Gamma_{0,3}
Final: \Gamma_{0\unsure{,|.}3}
```

Its explanation only reopens whether the existing small separator is a comma or point, retaining comma first. It supplies no changed preferred reading, new inscription, cancellation state or placement. Both `c_changed` and `h_changed` are nevertheless `true`, and the row contributes to the declared substantive-locus totals and feedback categories 1 and 10.

This conflicts with the existing counting rule that certainty-only changes belong in the doubt apparatus unless a reading or diplomatic state also changes. Root agreed during this review that both witness-change flags should be false and that the full crop/ink record must remain documented.

**Suggested correction:** Preserve `s022-26` as an explicitly noncounted observation, with its accepted reading, crop, coordinates and ink rationale intact. Set both witness-change flags false. Either give the builder a supported noncounted marker or publish such observations from a separate collection.

Changing only those two flags is insufficient with the current builder: `len(r['changes'])` still contributes the row to total loci, the confidence counter still includes it, and its `error_category` values still increment the feedback counts. All substantive totals must consistently exclude the noncounted observation while its documentation remains available.

If this is the only count adjustment, scan022's substantive totals become **25 loci, 7 against C and 24 against H**, from the current 26 / 8 / 25. Its low-confidence substantive count and feedback categories 1 and 10 each decrease by one. This does **not** change the audit count of three changed boxes: B06's accepted final qualification differs from its first reading, even though it does not establish a substantive departure from the witnesses' preferred comma.

The accepted page, the existing doubt entry “Gamma identity, lower separator”, the final B06 adjudication and the comparison record are already consistent. They need no reading revision.

### F2 — Scan 022's hand observation still attributes every inscription despite indeterminate pagination attribution

**Files/locus:** `reader_reports/145_scan022_reviewed.json`, `hand[0]`; `SP75_C13_145_hand_log.md`; inventory I01 and I23 in the same report and generated inventory.

The hand observation ends:

> All inscriptions are assigned to his hand absent contrary evidence.

The current inventory separately labels the header `9` (I01) and footer `21` (I23) as **“pagination hand, attribution indeterminate”**. Those are inscriptions, so the blanket sentence conflicts with the already-settled attribution scope.

**Suggested correction:** Retain the observation that darker marginal ink does not itself establish a second hand. Scope the following attribution to the mathematical notes and margins, and state that isolated pagination remains unattributed. For example:

> The mathematical notes and marginal additions are treated as the author’s working hand; attribution of the isolated pagination is indeterminate. The darker marginal ink does not by itself establish another hand.

No inventory hand label, source numeral or source text needs alteration. The scan021 notes and hand observations contain no equivalent blanket attribution problem.

## Focused synchronization checks that passed

### Scan 021

- **Critique abbreviation `n.`:** The accepted page (line38), s021-27, inventory I19, abbreviation entry7, final B08 audit/comparison and the added note/hand observations all retain `La n.`. The proposed expansion “notation” occurs in the abbreviation apparatus and in explanations of the old reading, rather than replacing the inscription. Historical C and first-reading quotations appropriately retain their former expanded wording.
- **Pi/pi after `sur`:** Page line22, s021-13, the separate doubt “group sign after sur”, inventory I09, notation observation0 and B04 consistently retain `\unsure{\pi|\Pi}` after `sur`. They distinguish it from the clear capital Pi after `et de`. The separate small point after `sur` is preserved as `\unsure{.}` in the page, s021-37, its doubt entry, inventory I09 and B04.
- **Three-stroke relation in (15):** Page line46, s021-36, inventory I22 and B12 agree on `\equiv` between the two products in the infinity row. The first two rows retain ordinary equality. The added note expressly distinguishes this glyph transcription from the earlier mathematical equality checks; those computations are neither silently changed nor claimed anew.
- **Cancelled point-name alternatives:** The page, s021-19, U021-02, the matching doubt entry, inventory I09/I12 and final B05 all retain the old point-name as `a_i / infinity / a`, with the live following `i` kept separate. The old narrower `a_i` appears in historical C/first-reading fields and `C_mark`, where it belongs. It is not an unsynchronized current reading.
- **Coverage:** The 51 raw rows have current, sequential coverage. The main additions discovered where the witnesses agree are not incorrectly required to have their own C/H-difference row. The references to existing change IDs remain valid.

### Scan 022

- **Word after `expliciter`:** Page line20, s022-12, the matching doubt, final B05, abbreviation entry5, note11, hand observation5 and coverage row30 agree on the qualified abbreviated `direct` + barred `m` + `t`, with `directement` retained as an alternative. `d’emblée` survives only in historical witness/first-reading material or an explanation that it has been rejected.
- **Gamma's small separator:** Page line20, s022-26, the doubt entry, note11 and final B06 agree on comma-first comma/point uncertainty. The problem is the counting policy in F1, not inconsistency in the accepted reading.
- **Two points beneath phi in (11):** Page line27, s022-20, the dedicated doubt, inventory I15, note11, hand observation5 and final B08 consistently preserve a qualified colon-like mark below phi. The ordinary colon to phi's right remains separate. The mathematical notes continue to describe the graph map without pretending that the doubtful low marks determine its meaning.
- **Abbreviation escaping is correct:** A direct code-point check of `abbreviations[5].form` found one backslash before `unsure` and one before `bar`, with no doubled literal backslash substring. An initial concern raised from an extra JSON serialization layer in tool output is withdrawn; no escaping correction is warranted on this evidence.
- **Coverage:** Row30 was updated to the accepted compressed-word reading. Rows39 and42–44 still describe the separate layout and target-punctuation issues in (11); their explanations need not repeat every newly recorded point within the linked complete formula. All 50 raw rows remain covered with valid references.

## Locus-counting review: overlapping quotation is not itself duplication

No second substantive change row was found that simply repeats another row's whole semantic issue. Several rows quote overlapping context but address distinct signs or states:

| Rows | Distinct issues | Assessment |
| --- | --- | --- |
| s021-13, s021-14, s021-37 | Pi case, sigma indices, and the small point after `sur` | Distinct adjacent issues. The longer Pi quotation contains neighboring indices and the point as context; it does not require merging the rows. |
| s021-26, s021-27 | Heading underline versus the readable Critique wording and notation proposal | Distinct state/content corrections. The complete note quotation repeats the underlined heading for context. |
| s021-19, s021-20 | Cancelled point-name/live `i` versus the following loop-image sentence and its local cancellations/index | Distinct adjacent loci, despite using the same broad audit crop. |
| s022-20, s022-26 | Layout, punctuation and the new low phi points in (11), versus the prose Gamma separator | Different physical locations and different issues. Only the separator row is certainty-only. |
| s022-22, s022-23, s022-24 | Live dotted rho, the separate cancelled rho-like sign, and the marginal hook/connector | Distinct adornment, deletion and graphic-mark issues. The full-margin quotation in s022-24 supplies context for its geometric correction. |

The two newly recorded point groups must also be distinguished from F1. The point after `sur` and the two points below phi are absent from the witnesses' quoted transcriptions and are now preserved, albeit tentatively. Adding those source marks is not merely attaching uncertainty to a sign already read identically by both witnesses.

F1 is therefore a **certainty-only row included in substantive counts**, rather than proof of two duplicate substantive rows. The uncertainty record and its audit evidence should remain fully available.

## Traceability and structural verification

| Check | Scan021 | Scan022 |
| --- | ---: | ---: |
| Prescribed boxes / ordered first and second coverage | 13 | 10 |
| Token-differing boxes reproduced independently | 11 | 9 |
| Explicitly changed audit boxes | 4 | 3 |
| Current documented change rows, before F1 correction | 37 | 26 |
| Current C departures, before F1 correction | 11 | 8 |
| Current H departures, before F1 correction | 35 | 25 |
| Raw-difference coverage entries | 51 | 50 |
| Listed decisions checked against global decisions.tsv | 4 | 4 |
| Unescaped dollar signs in final page | 66 | 36 |

Both sealed first TSVs match the first-reading seal. First, second and box-file hashes match their reading receipts. Stored report `second_boxes` retain the original first readings exactly. Reader assignments are independent and match the completed audits.

All 20 token-differing boxes have matching first/second/final/adjudication/ink records between the comparison TSVs and reviewed-report audits. Their final/adjudication/ink fields also match the adjudication files. Their explicit `changed` flags agree. No adjudication is pending; recorded crop paths exist and coordinates match the prescribed boxes. No crop was opened during these checks.

The current 60 H-collation rows match the reviewed-report source fields, including the presently incorrect positive H flag of s022-26. All eight listed decisions match the global decision table. This is faithful propagation, not evidence that the count flag itself is correct.

The final pages have balanced grouping braces and even unescaped-dollar counts in the non-compiling structural check, and both occur verbatim in the combined transcription. No duplicate change, inventory, listed-decision or unlisted-decision IDs were found. All single and list-valued coverage references resolve.

These checks do not re-evaluate the manuscript images or independently prove the mathematical notes. No correction was applied by this reviewer; root will decide and record the metadata synchronization.
