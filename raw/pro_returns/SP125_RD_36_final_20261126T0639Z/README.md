# SP125_RD_36 — consolidated diplomatic transcription

## Scope and reading method

The deliverable covers every supplied scan, **065–085 inclusive (21 pages), cote 36**. Each page was read against the supplied witnesses, with the ink as the authority. The three page readers worked on separate pages; the main reader reviewed their disputed and uncertain places. A different reader then read each page's selected difficult regions from images alone, without the witnesses, consolidated page or first box readings. Those independent readings were written before comparison and remain unchanged.

The independent stage contains **874 ordered box entries (873 distinct page/rectangle scopes)**. Script comparison identified **627 token-different boxes**; the main reader adjudicated each from a crop. **242 scopes changed the first consolidated reading**, including changes of certainty, cancellation/insertion assignment and diagram placement. Token differences include encoding differences as well as substantive disagreements; 627 is not a count of transcription errors.

All **189 source MARKS** have a decision in source order. All **710 supplied C/H difference rows** have a recorded disposition. Witness H is available for 13 of these 21 pages; the H collation contains no entries for the other pages.

No OCR, recognition library, PDF text layer, external research or TeX compilation was used. The transcription preserves visible peculiarities, omissions, abbreviations and unresolved readings. Mathematical expectations did not silently replace the ink.

## Contents of the final archive

| File or directory | Contents |
| --- | --- |
| `pages/` | One finished LaTeX fragment per supplied scan. |
| `SP125_RD_36_transcription.tex` | The 21 fragments in order, without a preamble. Use the supplied macro definitions and the stated standard LaTeX/TikZ packages if processing it separately. |
| `SP125_RD_36_changes.md` | Per-page differences from C/H, confidence, literal readings, ink evidence, crop coordinates, unresolved places and the complete independent adjudications. The opening tables give final counts. |
| `SP125_RD_36_collation.tsv` | Differences from witness H, using the required 11 columns and scan/page offset. |
| `decisions.tsv` | One row for every original MARKS item, in its original order. |
| `SP125_RD_36_doubts.md` | Notation table, current doubts, abbreviation expansions and a legibility assessment. Expansions belong to this apparatus, not the transcription. |
| `SP125_RD_36_inventory.csv` | Text, formulas, diagrams, drawings, margins, insertions and cancellations, with sheet and hand classifications. |
| `SP125_RD_36_notes.md` | Page summaries, limited mathematical observations and codicological/page-order notes. |
| `CHECK_EVENTS.tsv` | Actual mathematical check events, distinct from ordinary transcriptional reading, with stated provenance and linked note identifiers. |
| `SP125_RD_36_sheet_feedback.md` | Error-sheet category counts and local observations for subsequent work. |
| `SP125_RD_36_hand_log.md` | Observed handwriting habits with local scope and exceptions. Earlier attached habits were hypotheses, not imported evidence. |
| `second/` | Box lists, frozen first and blind second readings, token comparisons and main-reader adjudications for all pages. |
| `crops/CROPS.tsv` | Complete crop reconstruction index: filename, scan, original-pixel rectangle, rotation and decided place. |
| `progress.log`, `TRANSCRIPTION_SHA256.tsv` | Completion chronology, audit counts, checkpoint history and the final 22-file transcription hash manifest. |
| `records/`, `review/`, `scripts/` | Structured reading records, reversible application histories, documentary reviews, validation reports and the scripts used. Historical QA snapshots retain their original dates and pending states; the final validation reports supersede those status snapshots. |

## Separate crop archive

`SP125_RD_36_crops.zip` contains **1,864 grayscale JPEGs at quality 85**, including every changed/uncertain crop and the additional saved reading and adjudication crops. Its size is **137,171,277 bytes**, below 200 MB. Images use paths `crops/<filename>.jpg`, matching the index and citations. The final archive contains only the crop index, so the images are supplied once.

Neither archive includes the attached scans, unchanged source texts, prepared page halves or earlier checkpoint ZIPs.

## Reading the apparatus

An explicit `\unsure{...}` remains part of the diplomatic text. Its first alternative is the preferred ink reading, not a silent correction to the mathematics. Cancellation, insertion and marginal attachment may themselves be uncertain; the competing layer assignments are retained where necessary. Confidence in a selected reading is separate from an unresolved alternative: a medium-confidence recovery does not automatically introduce a new doubt mark. Two formula gaps use `\unsure{?}` as an explicitly editorial unknown-sign or unclassified-continuation marker. It does not assert a manuscript question mark, a particular relation, an ellipsis or a word count; the local notation entries explain both cases.

The weakest passages are the densely crossed, overwritten or crowded manuscript regions, especially the late drafts and marginal additions. The page-specific doubts and crop evidence identify these places rather than asserting that agreement between two AI readers settles them.

One frozen redundancy is retained: scan 067 boxes **B049 and B066** have the same rectangle and the same first, second and final readings after documented framing repairs made before the blind reading was written. This accounts for 874 entries versus 873 unique scopes; it is neither a missing region nor a conflicting decision.

The final structural checks verify coverage, file integrity, source quotation/record consistency, crop metadata and the frozen transcription hashes. They do not constitute a proof of every mathematical claim or a certification that all ambiguous handwriting has been resolved.
