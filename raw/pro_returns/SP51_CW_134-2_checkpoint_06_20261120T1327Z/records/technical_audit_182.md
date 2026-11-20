# Text-only technical audit — scan 182

## Scope

Audited the three `records/scan182/{A,B,C}/report.json` files and their complete `reading.tex` files; `records/scan182/decision.json`; `records/scan182/main_viewed_crops.txt`; `pages/H134-06_134-2_scan182.tex`; and the supplied scan182 C/H/question/metadata packet. Compared crop references with the three scan182 crop manifests and the four main-crop JSON sidecars. Consulted the decision, assembly, validation, and note-index helper code for metadata conventions.

No image was opened, displayed, recropped, or interpreted. No other page text, OCR, internet source, TeX engine, compilation, or rendering was used. This audit does not adjudicate ink or alter the transcription.

## Finding

**Low severity — inherited reader-level wording has no explicit scope in the final separator review.** In `decision.json`, `doubt_review[9].evidence` retains reader C's sentence “No crop was needed.” It immediately follows this with “Main inspected crops/scan182/main/03_separator.jpg.” The main crop is present in the saved metadata, the main-view list, the corresponding difference row, and the workflow account. Thus there is no missing crop or incorrect crop count; the record mixes C's half-view-only account with the later main adjudication without identifying the former as reader-level history.

Suggested record-only clarification: replace the unscoped sentence with “Reader C settled this in the top-half view; main subsequently inspected the saved separator crop.” No reading, confidence, classification, or count needs to change. No source record was modified by this audit.

No blocking or substantive decision-to-transcription inconsistency was found.

## Decision and disagreement coverage

The final decision records 21 difference rows: 11 counted changes against C and 18 against H. Every substantive A/B/C reading disagreement is represented in the final decision and implemented in the final page:

| Locus | Reader disagreement | Final disposition checked against text |
| --- | --- | --- |
| L3, aborder | A doubtful; B/C resolved | A's single-reading uncertainty retained |
| L20 connector | A gives dashv/arrow/line; B/C line/arrow | All three alternatives retained in A's preferred order |
| L21 exponent | A also permits `ij`; B/C permit dot/plus | `i·j`, `i+j`, and `ij` retained |
| L23 accent | B acute/circumflex; A/C acute | B's acute-first uncertainty retained |
| L24 older question mark | A/C doubtful; B resolved | A/C's uncertainty retained |
| Point below first constant | A/B reproduce; C rejects as grain | Reproduced with origin unassigned |
| Point inside first H | C reproduces separately; A/B do not | Reproduced with origin/function unassigned |
| H doubt flag at final overwrite | B true; A/C false | Final `marked_in_H: no`, with an explicit rationale |

The other two detached strokes are common to all readers and remain represented. Differences in drawing syntax, uncertainty-wrapper placement around the cancelled label's secure parenthesis, and confidence levels do not expose a further unrecorded reading disagreement. The final separator, first-H overwrite, accent, and final-overwrite classifications have coherent explanations even where reader classifications differ.

All 14 supplied C question rows have final dispositions. The three earlier-note topics also have dispositions; the later-page quotation is explicitly left outside this page's evidence. The added `ij` alternative is expressly recorded as an expansion of an existing uncertainty, with unchanged preferred C reading, rather than silently omitted from the account.

## Unresolved readings and inventory

The eight final `\unsure` sites correspond to the eight `unresolved` entries: aborder; cancelled a/alpha; intrigu-/intrigué; old equals/plus; connector; target exponent; réconstituer/rêconstituer; and the older question mark. Their preferred readings and alternatives agree with the final page. The four nontext marks remain physically represented without converting origin/function uncertainty into unsupported textual alternatives.

All 15 final inventory rows use permitted kinds and carry `transcribed: yes`: six text, one insertion, five drawing, and three deletion entries. The five drawings comprise the separator and four detached marks. The formula is classified as running text. The archive number is assigned to its separate pencil hand and retained in a comment; the author page number is 37. No hand is asserted for the four detached marks.

## H collation metadata

Final `kind` and `marked_in_H` values use the helper/validator conventions. The cancelled label is classified as readable ink left wholly illegible in H and is marked in H. Aborder's H uncertainty is retained, so that row correctly has `differs_H: false` while recording `marked_in_H: yes`. H's descriptive notes about the separator and final overwrite are not turned into explicit reading doubts. The underlying first-H sign and older question mark are treated as omissions from H's main transcription, rather than live/deleted-state reversals.

## Crop provenance

All crop-bearing `bbox` fields checked in the three reports and final decision match the corresponding saved crop manifest or main JSON sidecar. Feature rectangles and preserved `reader_report_bbox` values are separate from the actual selected crop rectangles. No mismatched or absent crop metadata was found.

| Owner | Reported crops | Manifest entries | Saved image paths | Recorded unique crop views |
| --- | ---: | ---: | ---: | ---: |
| A | 16 | 16 | 16 | 16 |
| B | 15 | 15 | 15 | 15 |
| C | 17 | 17 | 17 | 17 |
| Main | 4 new | 4 sidecars | 4 new | 19 total |

The 19 main-view entries are unique existing paths: 15 reused reader crops and four new main crops. Every crop cited by a final difference row is in that view list. File existence and JSON metadata were checked without opening image contents; this audit does not independently certify an actual display event or pixel geometry.

## Notes and check-event scope

The notes preserve the page's open question and qualifications, keep historical/English editorial assertions outside the verified page evidence, and explicitly distinguish visual reading decisions from mathematical verification. Each reader's `check_events` array is empty. The final four events comprise one general notes background record and three indexed source-statement background records; none claims a proof, computation, or local mathematical check. The three statement IDs and scopes match the final `note_statements` entries.

## Result

Only the minor separator provenance wording above merits clarification. No transcription change, additional image inspection, or new ink decision is recommended by this audit.
