# SP60_CW_71 — Feedback on the error sheet

Generated from the recorded decisions on 2026-11-20 15:01:03 UTC. This is a mechanical account of the primary reader's saved decisions, not an additional reading of the scans or witnesses. Regenerate it after any decision or doubt-status update.

## Read H's omission count as a coverage measure

**Of 41 discrepancy rows against H, 22 represent broad source-block coverage gaps and 9 are local or additional omissions. These must not be presented as 31 attempted readings that H got wrong.** The remaining H rows comprise 7 partial recoveries from illegibility placeholders and 3 other recorded differences.

The source-block group records places where H's editorial descriptions or short source locators do not supply the full source text. Local omissions concern such things as marginal marks, folio rules, trailing marks, or side strokes. A description in an editorial note does not supply a diplomatic transcription of the described source. No H discrepancy rows are counted for scans 39–46, where H has only description or no source text.

This is not an error-rate comparison between the witnesses: their coverage differs, and a recorded place can range from one mark to several omitted lines. The source-block classification below follows the saved place/coverage records; it does not come from a fresh examination of H.

## Counts for all ten error-sheet categories

Each changed decision place has one **primary category**. The same row counts once against each witness it differs from, once in overlap if it differs from both, and once in distinct places. Thus distinct = C + H − overlap. Counts include changes that remain explicitly uncertain; they are recorded differences, not uniformly certain corrections.

| Error-sheet category | Against C | Against H | Overlap | Distinct places |
|---|---|---|---|---|
| 1. Symbols and indices | 6 | 1 | 0 | 7 |
| 2. Words | 5 | 0 | 0 | 5 |
| 3. Omissions | 12 | 31 | 3 | 40 |
| 4. Drawings and diagrams | 1 | 1 | 1 | 1 |
| 5. Readable ink left as illegible | 1 | 7 | 1 | 7 |
| 6. Insertions put in the wrong place | 0 | 0 | 0 | 0 |
| 7. Struck text / deletion state | 1 | 0 | 0 | 1 |
| 8. Abbreviations expanded or spelling modernised | 4 | 1 | 1 | 4 |
| 9. Text that is not on the page | 1 | 0 | 0 | 1 |
| 10. Other | 1 | 0 | 0 | 1 |
| Total | 32 | 41 | 6 | 67 |

The primary category belongs to the place, not separately to each witness's cause of error. If C and H differ for different reasons at one place, both witness columns inherit the stored category; the table does not silently invent separate per-witness diagnoses. For example, `048-C05` is stored under recovered illegibility, while its scan record also discusses a compressed versus expanded form. Its witness-specific causes must be read in the changes log.

Confidence of the 67 changed-place records: high 42, medium 16, low 9.

## Retentions and certainty are separate ledgers

There are 83 decision rows with neither witness-change flag set; they document retained readings or crop decisions and contribute zero to the discrepancy table. The doubt ledger contains 69 resolved certainty entries, 82 remaining entries, and 0 explicitly retained-doubt entries. These ledgers may refer to the same places and must not be added together. A certainty change without a changed reading does not enter the discrepancy counts.

## H coverage and recovery breakdown

| Scan | Broad source-block gaps | Local/additional omissions | Partial illegibility recoveries | Other differences | All H rows |
|---|---|---|---|---|---|
| 38 | 8 | 5 | 0 | 0 | 13 |
| 47 | 7 | 1 | 2 | 3 | 13 |
| 48 | 7 | 3 | 5 | 0 | 15 |
| Total | 22 | 9 | 7 | 3 | 41 |

Broad source-block coverage IDs: `038-H01`, `038-H02`, `038-H03`, `038-H04`, `038-H05`, `038-H06`, `038-H07`, `038-H08`, `047-HB01`, `047-HB02`, `047-HB03`, `047-HB04`, `047-HB05`, `047-HB06`, `047-HB07`, `048-HB01`, `048-HB02`, `048-HB03`, `048-HB04`, `048-HB05`, `048-HB06`, `048-HB07`.

Local/additional omission IDs: `038-H09`, `038-H10`, `038-H11`, `038-H12`, `038-H13`, `047-C01`, `048-C01`, `048-C06`, `048-H04`.

Partial recovery IDs: `047-H02`, `047-H03`, `048-C05`, `048-H01`, `048-H02`, `048-H03`, `048-H05`.

Other H difference IDs: `047-C02`, `047-C03`, `047-H01`.

## Recurring issues already covered by the sheet

These families are supported by the saved `place` and `scan_shows` records. They cut across primary categories and are not extra rows to add to the totals. Wording such as 'favors' or 'uncertain' in an underlying record remains in force.

| Recurring issue | Decision IDs | What the saved records document | Use in the next run |
|---|---|---|---|
| Small tails, stems, raised marks, and overwritten numerals | `042-C1`, `042-C2`, `043-C2`, `045-C02`, `047-H01` | The records distinguish a descending tail, projecting crossbar, raised mark, or retraced stem; several decisions remain explicitly uncertain. | Already covered by symbols and indices; keep the distinction between a visible mark and an expected formula. |
| Cancellation state and the reading underneath are separate decisions | `039-C1`, `039-C2`, `044-C07`, `047-H03`, `048-C02` | The records separately identify overstriking or deletion and the surviving word ending, letter shape, or case. | Already covered by struck text and words/symbols; a resolved deletion state need not resolve the cancelled reading. |
| Flat accent strokes and uncertain accent absence | `040-C1`, `040-C2`, `040-C3`, `047-C02` | The records describe near-horizontal accent marks or the absence of a securely visible circumflex, with alternatives retained. | Already covered by spelling and normalization; preserve shape uncertainty instead of silently choosing the conventional accent. |
| Repeated cramped letter junctions | `044-C02`, `044-C03` | Two occurrences are recorded as having the same extra undotted minim at a cramped junction. | Already covered by words and the hand log; the two locations remain separate change places. |
| Faint, slanted marginal annotations recovered only in part | `047-H02`, `047-H03`, `048-C05`, `048-H01`, `048-H02`, `048-H03`, `048-H05` | The records document rotated crops and distinguish recoverable strokes from unresolved endings or alternative readings. | Already covered by readable ink left illegible; these are partial recoveries, not claims of complete certainty. |
| Long adjoining strokes can resemble punctuation | `043-C4`, `048-C03` | One record retains uncertainty about a long final curved mark; another records no separate punctuation where letter, attachment, and following-word strokes meet. | A useful subtype of symbol/other or text-not-on-page decisions; decide a punctuation mark separately from an adjacent connector. |

## Specific refinements for the next error sheet

The metadata establish no new mutually exclusive error class beyond the ten categories. They do support the following recurring subtypes, which the broad sheet does not name individually. H's partial-quotation coverage is an additional comparison issue, addressed prominently above; it should remain distinct from misreading attempted source text.

| Refinement | Decision IDs | Recorded issue |
|---|---|---|
| Rules surrounding folios and references | `038-H13`, `043-C1`, `044-C01`, `044-C04`, `045-C01`, `047-C01`, `048-C01` | Parallel rules above and below a folio or reference are recorded as omitted marks. This is a recurring completeness issue even where the numeral itself was already present. |
| Detached points retained without an assigned mathematical meaning | `043-C3`, `044-C05`, `044-C08` | The records retain small detached or raised points, including a point at a word's line division, without forcing a conventional mathematical interpretation. The feedback concerns each mark's presence, not its meaning. |
| Connected annotation enclosures, notches, and side strokes | `047-C03`, `047-C04`, `048-C04`, `048-C06` | The records identify a continuous enclosure, insertion notch, lower connecting rule, or long side mark. These refine the existing drawing/placement categories: a connector need not be emphasis or cancellation. |

## Bookkeeping limits and regeneration

The totals count unique decision IDs. Identical normalized scan/place labels are checked below, but differently worded labels can still refer to the same physical place; only the primary reader can settle that. A zero category means no changed place currently carries that primary classification, not that the associated feature was absent from the manuscript.

No duplicate decision IDs or repeated exact normalized scan/place labels occur in the changed-place ledger.

Regenerate only this feedback file with `python3 scripts/generate_feedback.py .` from the package directory. The script reads metadata tables and writes this file; it does not alter page files, decision records, doubt records, or the combined transcription. Its named issue families are summaries of already recorded evidence and are not new manuscript judgments.

Decision-table SHA-256 at generation: `2ae52610b973dfdd9df4cca1ed9f5948728fd8363ac0d34d9ce298f439c519f9`.
