# Feedback on the recurring-error sheet

## Counting basis

These counts use the final `CHANGE_LEDGER.tsv`, with one primary kind assigned to each recorded place. They include differences against either witness and exclude differences of macro syntax alone and changes of certainty alone. A place differing from both witnesses is counted once in “Places” and in each applicable witness column. Several separate occurrences of a recurring sign have separate rows; a spatially continuous passage or diagram feature can be one row. The witness columns indicate which text differs at that place; they are not independent recategorizations of every witness's error. In particular, a row classified as recovery of H's illegible text can also contain a different, previously uncertain reading in C.

The ten categories are the supplied error-sheet categories, mapped to the permitted collation kinds. The short ledger label “deletion state” has been unified with its full label. Counts describe the recorded collation, not an estimate of all errors left in either draft.

| Error-sheet kind | Places | Rows differing from C | Rows differing from H |
|---|---|---|---|
| 1. Symbols and indices | 124 | 49 | 108 |
| 2. Words | 76 | 8 | 72 |
| 3. Omissions | 54 | 16 | 51 |
| 4. Drawings and diagrams | 46 | 19 | 43 |
| 5. Readable ink left as illegible | 51 | 4 | 51 |
| 6. Insertions put in the wrong place | 27 | 8 | 27 |
| 7. Struck text | 25 | 16 | 22 |
| 8. Abbreviations expanded / spelling modernised | 41 | 12 | 38 |
| 9. Text not on the page | 22 | 6 | 18 |
| 10. Other | 18 | 3 | 16 |
| TOTAL | 484 | 141 | 446 |

Confidence across these 484 places: 317 high, 107 medium, 60 low. Confidence concerns the recorded ink decision; unresolved readings remain marked in the transcription.

The 187 supplied doubt marks have 100 first-reading decisions, 10 alternative-reading decisions, 11 other readings/removals and 66 undecided entries. These figures are not added to the error-category totals. There are also 41 separately recorded certainty-only resolutions outside `MARKS.tsv`. The doubts table contains 124 located entries; one entry can cover more than one adjacent uncertainty wrapper.

## What recurred in this batch

| Category | Located observations for the next run |
|---|---|
| Symbols and indices | The Lefschetz letter is ζ, rather than C's ξ, at sixteen occurrences on 16_scan053; lower-case projectors p and capital primitive spaces P are distinct. The category letter defined on 120_scan008 is calligraphic E, including its later use on 120_scan011; it supports the still-qualified isolated occurrence on 120_scan007. The written slips in 120_scan005 (a/x), 120_scan010 (Y/Z), 120_scan011 (I/A), 120_scan021 (a/x), 120_scan022 (arity) and 136_scan329 (B/A and pq/p+q) are retained. |
| Words | Endings and small connectives require separate attention: singular “Énoncé analogue” on 120_scan025; “disjointes” on 120_scan015; “c'est le cas” on 120_scan017; “faut s.” on 120_scan019; “antifiltre” on 120_scan020. The mathematics was used to identify a reason to inspect, not to supply a grammatical correction. |
| Omissions | Most vulnerable are small text under cancellation, slanted annotations on 120_scan006–007 and 120_scan015, hooks and labels inside the cancelled corollary on 120_scan012, and small strokes belonging to the diagrams on 136_scan328. Underlines, bars inside circled Roman numerals and the independent divider on 136_scan329 are source elements too. |
| Drawings and diagrams | Headless shafts and hooks occur beside explicit arrowheads: 16_scan053; 120_scan003–004, 006, 011–014, 016–017, 021–022; 136_scan328–329. The hook's direction and the presence of a head must be decided separately. On 136_scan328 the diagonal and long curved cohomology arrows must be attached to their spatial source and target, not to the nearest convenient array cell. |
| Readable ink left as illegible | H leaves numerous short or cancelled passages blank where strokes support a reading; examples include the slanted note on 120_scan006, the cancelled corollary on 120_scan012, the compact heading on 120_scan015 and “loc.” on 120_scan025. Recovery is sometimes only partial or still qualified. Heavily entangled ink on 120_scan006–007 and a cancelled word on 120_scan009 remains illegible; it has not been filled from context. |
| Insertion or placement | The small additions on 120_scan003, 005–007 and 009 require both a reading and an attachment decision. On 120_scan020 both “Esploc” labels keep loc on the baseline, with only M_* subscripted. In 120_scan024 the lambda annotation is placed under g_beta(x), even though the calculation points to f_alpha(x). |
| Struck text | The enclosing cancellation on 120_scan007 and the layers of replacement on 120_scan009 must be retained together with the smaller strikes inside them. The whole corollary on 120_scan012 is cancelled, including its diagram. On 136_scan328 a printed staff rule does not cancel “Comm”, and only the first term of the nearby arithmetic fragment is crossed. |
| Abbreviations and spelling | tt/tte must be distinguished from an actual ∀ on 120_scan005, 008, 013, 020–021 and 024. Barred m and = are prose abbreviations for même in this run. ess. with raised t on 120_scan025 is not “est-il”; hom, élts and grde on 136_scan329 are not expanded. cpct and cpcte on 120_scan020 are separate written forms. |
| Text not on the page | Do not fill the live gaps left by cancellation (120_scan009), add a coefficient/comma to H2(BT') or a final parenthesis to the unfinished upper target (136_scan328), or turn a single component expression into two copies (120_scan025). The first-pass layout of the integral row on 136_scan328 had an extra Z node; the single written Z now carries the map labelled 2. |
| Other | Quotation marks, punctuation and emphasis remain substantive when the written marks differ. Examples: double raised quotation strokes on 120_scan003 and 006–007; circled 3/4/5 on 120_scan005 and 1/2 on 136_scan329; the semicolon/question-mark doubt after (M1)_0 on 120_scan019; and the two question marks on 120_scan025. |

## Recurring subtypes that the sheet does not name explicitly

No additional broad error class was needed. The following narrower, repeatable failure modes deserve explicit reminders within the existing classes.

1. **Duplicating a source expression when linearizing a diagram or display.** H repeats the component expression on 120_scan025 and repeats the live BG'-cohomology object when starting its next array on 136_scan328. C's earlier array on 136_scan328 also introduces a second integer node beside the integral identification. Compare the number of written objects with the number of typeset objects before choosing a grid.
2. **Adding a visible brace from a typesetting convenience.** The family display on 120_scan011 and the M7 display on 120_scan013 acquire braces in H that are not drawn. A `cases` environment is a reading decision if it introduces a brace.
3. **Giving related category names uniform decorations.** On 120_scan015 the first and last Esp names have upper and lower arrows, whereas the parenthetical occurrence has only the lower arrow. On 120_scan020 loc is on the baseline in both instances. Compare each occurrence instead of propagating the expected category typography.
4. **Turning a relation glyph into both a label and a new edge.** The middle black Z identification and the lower blue integral comparison on 136_scan328 have no additional shaft beyond their written relation strokes. In the lower blue occurrence the curled left end still leaves simeq versus a decorated left arrow open. The extra edge must not be supplied whichever candidate is adopted.

Two further local hazards are worth carrying forward even though they do not establish a new recurring class: printed music staves under the ink on 136_scan328, and reuse of the label M5 for different hypotheses between 120_scan007 and 120_scan010. The hand log and notation table keep these scoped to the places that support them.

## Scope of the audit

The primary reader read the 25 scans in the supplied order and then reread all 25 in the same order. The same reader made every transcription and image-based decision. Auxiliary work was limited to mechanical file, schema, macro and archive checks; no page content was delegated. There was no OCR, external research or TeX compilation. The final audit corrected several previously accepted places as well as qualifying the overwritten M4/M7 endpoint on 120_scan024 and the lower blue relation on 136_scan328. The surviving doubts are part of the result, not a claim that their first alternatives are certain.
