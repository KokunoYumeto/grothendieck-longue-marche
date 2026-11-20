# Textual records audit — scan181

Date: 2026-11-20. Scope: completed scan181 only. Auditor: `/root/audit_records_181`.

## Finding

The three completed returns are substantively covered by the final decision. No missing reader disagreement, missing supplied C question, missing inventory element, unsupported change to a root reading, or mathematical-check scope inflation was found. The final page agrees with the final textual decisions and the recorded treatment of the four detached points.

Two small final-decision metadata inconsistencies require correction. A crop citation can also be clarified, and one grammatical description can be corrected. These fixes do not alter any ink decision, preferred reading, doubt, difference count, inventory attribution, or final TeX. No final file was changed in this audit.

## Concrete corrections

All JSON array indexes below are zero-based. All four findings are in `result/records/scan181/decision.json`.

### A181-01 — stale `bbox_role` on three saved-crop references

Locations:

- `$.differences[0].bbox_role` — `181C-D01`.
- `$.differences[6].bbox_role` — `181C-D07`.
- `$.differences[17].bbox_role` — `181C-D18`.

Each currently says: `Approximate feature rectangle observed in the half image, not a saved crop.` These rows now have a saved `crop` and a `bbox` for that saved crop. D01 and D18 use the two reinstated main crops whose exact rectangles are recorded in the recovery note. D07 uses A's saved `L11_ou_n_loc.png`, and its final `bbox` equals the A report/manifest rectangle. Each row separately preserves the earlier approximate feature rectangle under `reader_report_bbox`.

Smallest fix: remove these three optional `bbox_role` fields. Alternatively, change their value to `Saved crop rectangle; the earlier reader feature rectangle is preserved in reader_report_bbox.` Preserve `crop`, `bbox`, and `reader_report_bbox` unchanged. The original reader C report should remain unchanged: its corresponding rows genuinely had no saved crop at that stage.

### A181-02 — D07 place label contradicts its retained uncertainty

Location: `$.differences[6].place` — `181C-D07`.

The current label is `L11, loc without abbreviation stop`. The final reading is `\unsure{loc.|loc}`, its first candidate includes a stop, and the evidence explicitly leaves the stop/no-stop choice unresolved. The label is inherited from reader C's resolved undotted reading, which the root decision did not adopt.

Smallest fix: change only the label to `L11, uncertain abbreviation stop after loc`. Preserve the final reading, evidence, confidence, flags, and crop.

### A181-03 — unqualified “crop 03” is ambiguous in the final note review

Location: `$.doubt_review[11].evidence`, the earlier conditional-verbs note.

The clause `incarnerait is separately supported by crop 03` comes from reader C's note review. At the consolidated level, C's `03_fin_insertion.png` and main's `03_types_quote_close.jpg` are different crops; only the latter is a root inspection-ledger entry, and it concerns a different locus. The final verb difference D05 already cites root-inspected `crops/scan181/A/L10_incarnerait.png`.

Smallest clarity fix: replace that clause with `incarnerait is separately supported by crops/scan181/A/L10_incarnerait.png`. This uses the existing final evidence reference and ledger entry. The original bare reference is not evidence of an incorrect reading or a newly required inspection; the issue is consolidated-reference clarity.

### A181-04 — “both nouns” mislabels the article in `des types`

Location: `$.differences[17].evidence` — `181C-D18`.

The sentence currently says `Both nouns are plural in the written des types, unlike H’s du type.` The two words are an article and a noun.

Smallest copyedit: replace `Both nouns are plural` with `The article and noun are plural`. This corrects the grammatical description without changing any claim about the written forms or the consequential difference from H.

## Three-return coverage

Every field of the A, B, and C reports and all three complete `reading.tex` files was read. Each report has `complete=true`; all three have exactly 23 main-baseline entries plus four addition entries, with no missing or duplicated line identifiers. Each has all 11 supplied C question reviews. Both earlier-note topics are represented in each return and in the final review, although A records them in its notes rather than a separately named earlier-note array.

| Reader | Difference rows | Covered by final rows | Textual doubt sites | Other uncertainty entries | Reported crops |
|---|---:|---|---:|---|---:|
| A | 20 | D01–D08, D11–D12, D14–D23 | 4 | 2 point-origin/function entries | 13 |
| B | 21 | D01–D08, D10–D12, D14–D23 | 3 | 3 point-origin/function entries | 14 |
| C | 23 | D01–D23 | 3 | 4 point-origin/function and 2 intended-emphasis entries | 17 |

The final decision's eight `reader_comparisons` rows account for every substantive A/B/C divergence:

| Locus | Final disposition | Record consistency |
|---|---|---|
| L11 `loc` | Retain A's stop/no-stop uncertainty, stop first | Difference D07, unresolved entry, abbreviation entry, notes, and final page agree; only the place label needs A181-02 |
| L12a `inductive` | Retain A's one-candidate uncertainty against B/C's resolution | D08, doubt review, unresolved entry, notes, and final page agree |
| L12 underline | Select C's `t\uline{ous}` physical span | D09, inventory coordinates, notes, and final page agree |
| L16 underline | Select C's `th\uline{éorèmes de finitude}` physical span | D14, related right-endpoint crop, inventory, notes, and final page agree |
| L20 `ordinaire` | Retain uncertainty and A's `ordïnaire` alternative | D19, review, unresolved entry, notes, and final page agree |
| L22 accent | Retain B/C's acute-first accent alternatives against A's resolution | D21, review, unresolved entry, notes, and final page agree |
| Detached points | Preserve C's union of four sites; use graphic treatment at `fonctoriellement` | D10–D13 and four drawing inventory entries agree with the final page; A's inline period is explicitly adjudicated |
| Doubt scope | Five textual doubts; point origin and intended emphasis stay outside that list | Final unresolved array, notes, inventory, and textual doubt count agree |

No return is treated as a vote that overrides the root's recorded adjudication. Unanimous decisions—including the singular endings, barred-m reading, prefix placement, and quotation form—are covered by the corresponding final rows and question review.

## Supplied C questions and earlier notes

The final `doubt_review` has 13 rows: one for every one of the 11 supplied questions, followed by both earlier notes. The overlaps between Q4–Q6 and Q11 are explicitly acknowledged; they do not create additional unresolved-text entries.

| Supplied item | Final disposition |
|---|---|
| Q1, partition alphabet | Retained; calligraphic P first at L7a, same preferred family at independently inspected L9 |
| Q2, `inductive` | Retained one-candidate uncertainty |
| Q3, `ordinaire` | Retained, with `ordïnaire` alternative and singular ending |
| Q4, `élément` / `éléments` | Resolved to singular `élément` |
| Q5, `polyédres` / `polyèdres` | Retained, acute first |
| Q6, barred m / equals | Resolved to barred m; expansion listed separately |
| Q7, wording, conditional, plural types, prefix | Confirmed with retained alphabet doubt |
| Q8, baseline wording and additions, `loc`, underline | Explicitly qualified by the final stop doubt and physical underline span |
| Q9, `clos`, plural théorèmes, singular adjectives, `ou`, underline | Confirmed with final physical span |
| Q10, `des types d'homotopie fin` | Confirmed with plural types and singular fin |
| Q11, constituent/quoted phrase/sign overlap | Singular élément and barred m resolved; accent doubt retained; quotation and separator scope preserved |
| Earlier conditional-verbs note | Confirmed as source wording, without a proof claim; citation clarification in A181-03 |
| Earlier page-number note | Confirmed as author page 36, separate from archive pencil 181 |

## Difference counts, H flags, and kinds

The final 23 distinct recorded places give the following arithmetic:

| Set | Places | High | Medium | Low |
|---|---:|---:|---:|---:|
| All final difference rows | 23 | 13 | 10 | 0 |
| Differ from C | 11 | 5 | 6 | 0 |
| Differ from H | 22 | 13 | 9 | 0 |

Ten places differ from both witnesses, one from C alone (D03), and twelve from H alone. Thus the witness totals do not imply 33 distinct places. Every final row differs from at least one witness; all IDs D01–D23 are unique.

D19's `differs_C=false` is intentional under the stated count convention: the preferred singular reading and its doubt remain; adding A's supported alternative is handled by the separate retained-doubt review. It is not a silently omitted preferred-reading change. D07 and D08 correctly count their certainty differences from H, which has no corresponding doubt mark.

All 23 `marked_in_H` values are `no`. This agrees with the supplied H text: its `\add`, `\emph`, and editorial `\note` wrappers do not express reading doubt. The 22 H collation rows therefore contain no marked-H doubt. The kind distribution is valid under the helper schema:

| Kind | All rows | H differences |
|---|---:|---:|
| `other` | 7 | 7 |
| `insertion or placement` | 2 | 2 |
| `misread symbol or index` | 1 | 0 |
| `misread word` | 8 | 8 |
| `drawing or diagram` | 4 | 4 |
| `abbreviation expanded or spelling modernised` | 1 | 1 |

The four graphic points are consistently classified as drawings in the final record, regardless of A/B's earlier `omission` classification or A's inline-point representation. No change to the kinds or counts is proposed.

## Inventory, page, and notes

The 11 final inventory entries comprise the author page number, one prose block, four additions, four detached-point drawings, and the separate archive number. The two underline spans are nested in the prose inventory entry and described in the notes; they have not disappeared merely because they are not separate top-level rows.

Author prose/additions/page number are attributed to `his hand`. The archive number is attributed to `archive pencil hand, distinct from main writing`. All four detached points have `uncertain attribution; no authorial origin asserted`. Every entry has `transcribed=yes`. The final page contains the corresponding four additions, four inline nontext figures, two underline spans, author page 36, and archive-sheet comment 181. The parenthesis inventory's `\unsure{inductive}` is a single-backslash macro in the parsed metadata and is consistent with the page.

The final five unresolved-text entries correspond to the five `\unsure` sites: partition alphabet, `loc` stop, `inductive`, `ordinaire/ordïnaire`, and `polyédres/polyèdres`. The physically recorded point locations and underline endpoints are kept separate from unassigned origin or intended emphasis. The notes preserve those qualifications instead of turning them into doubtful words or assigning authorship.

All three reader `check_events` arrays are empty. The final four events consist of one general notes entry and three paragraph-scoped content entries, all typed `carried as background without fault found`, with explicit statements that no independent proof or computation occurred. The three `note_statements` IDs match those scoped events. Nothing in the final records claims that visual reading verified the mathematical assertions. The notes retain the conditional language and distinguish H's editorial continuation-location claim from the visible unfinished sentence.

## Recovery and reference consistency

The environment recovery note and all three separate reader recovery notes were read before treating the view counts as current-session activity. They explicitly describe restoration of completed returns and original inspection counts, with no replacement readers or new image views. This audit added no image inspection.

Text-only checks found:

- The report, manifest, and saved-filename counts agree at A13/B14/C17, with no duplicate manifest paths or mismatched report/manifest rectangle, rotation, scale, size, or recorded inspection-count values.
- Main has three saved crop filenames. Its inspection ledger contains 20 unique paths: 17 reader crops (A2/B3/C12) and three main crops. Every final primary crop, related crop, and fully qualified doubt-review crop reference is represented in that ledger.
- A's restored text sizes match its recovery note: report 44,760 bytes; reading 1,735 bytes. B's report and reading SHA-256 values match the two hashes in its recovery note.
- C's `metadata.their_page=180` is consistent with the assembly helper's scan-minus-one witness-page convention; author page 36 and archive sheet 181 are separate fields.
- The final structural wrappers are described by the supplied preamble. No TeX engine, probe, compilation, or rendering was used to assess them.

## Scope boundary

Inputs were the designated scan181 decision, complete A/B/C reports and readings, scan181 C/H/question packet text, final page, preamble, recovery text, scan181 text manifests/inspection ledger, and relevant helper-schema source. No other page content, image, PDF text, OCR, internet source, or external source was examined. Filename existence and metadata comparisons did not open image files. The audit checks internal textual consistency; it neither verifies physical ink facts anew nor overturns the root's completed visual adjudication.

## Main-reader disposition

All four proposed metadata/citation clarifications were accepted. Saved crop rectangles, image decisions, final page text, counts and doubts are unchanged. Applied by scripts/apply_audit_181.py; no images were reopened.
