# Frozen first-excerpt coverage review

## Result

The eight frozen first-reading TSVs contain **290 box rows: 288 nonempty readings and 2 empty readings**. The empty entries are **scan002 B008** and **scan006 B047**. No TODO/TBD-style work placeholder or descriptive substitute for a reading was identified. Two nonempty entries, scan006 B035 and B037, contain the same explicit source-illegibility marker.

This is a read-only metadata review. It does not adjudicate handwriting, corrections, symbols, or whether an isolated mark is writing. No images or second-reading TSVs were consulted for this review. No frozen TSV, initial page, current page, or decision file was changed.

## Coverage by page

| Scan | Frozen first rows | Nonempty readings | Empty boxes | Source-illegibility marker |
|---|---:|---:|---|---|
| 002 | 29 | 28 | B008 | None |
| 003 | 24 | 24 | None | None |
| 004 | 30 | 30 | None | None |
| 005 | 49 | 49 | None | None |
| 006 | 51 | 50 | B047 | B035 and B037 |
| 007 | 36 | 36 | None | None |
| 008 | 40 | 40 | None | None |
| 009 | 31 | 31 | None | None |
| **Total** | **290** | **288** | **2** | **2 entries, one repeated span** |

## Findings requiring disclosure

### scan006 B047 — missing excerpt, corresponding page text present

- Frozen first field: empty.
- Neutral box: complete central text block or formula, including corrections, decorations and punctuation; coordinates **[466, 2264, 1664, 2352]**.
- Matching content is present in **H156-01_156-7_scan006_initial.tex**, in the final aligned display. The exact opening anchor is `\text{\uline{At}}_{M}\,3&\qquad\text{Si }\Phi,\Psi\in\widetilde{\mathscr F}`. That statement includes the quantified compatibility hypothesis, cancelled `\{X,Y\}` alternative, parenthetical existence condition, conclusion, and union condition.
- The corresponding smaller excerpts B010, B048, B049 and B050 are nonempty: they cover the axiom label, a cancelled span, the existence condition, and the union condition respectively.
- **Classification:** incomplete frozen excerpt extraction/coverage. The blank must not be described as omission of the axiom from the frozen initial page. The reason the extraction is empty was not inferred.

Suggested audit wording: “The frozen first-reading TSV contains an empty B047 excerpt, although the complete At_M 3 statement was already present in the frozen initial page. The excerpt was preserved unchanged; this coverage defect is disclosed separately from page transcription differences.”

### scan002 B008 — blank excerpt for an isolated marginal mark

- Frozen first field: empty.
- Neutral box: “small isolated marginal mark; determine whether it is writing”; coordinates **[35, 452, 100, 505]**.
- No explicit corresponding isolated-mark encoding is identifiable in **H156-01_156-7_scan002_initial.tex**. The initial page contains the marginal reference inscriptions, but those are separately represented by B003 and B004.
- **Classification:** blank first excerpt with no explicit page counterpart identified from text metadata. The empty field is neither an encoded illegibility judgment nor evidence, by itself, that manuscript text was omitted. Determining the nature of the mark belongs to the ink adjudication, outside this review.

Suggested audit wording: “The frozen first-reading field for scan002 B008 is empty. Its neutral box describes an isolated marginal mark. The frozen initial page has no identifiable separate encoding for that mark; the present metadata review makes no decision on whether it is writing.”

## Nonempty illegibility placeholders

| Scan / box | Frozen first content | Matching frozen initial content | Treatment |
|---|---|---|---|
| 006 B037 | `\deleted{\illegible{2}}` | Exact same marker in the marginal note beginning “équivaut à”, after `\inserted{Si $G,H$,}` | Explicit source-illegibility encoding, not an absent first excerpt |
| 006 B035 | Complete marginal note containing `\deleted{\illegible{2}}` | Same complete note and marker in the initial page | Larger overlapping excerpt of the same uncertain cancelled span |

The standard `\unsure{...}` alternatives are populated readings, not missing-work placeholders. Mathematical empty groups such as `={}` and source ellipses are likewise not classified as missing readings.

## Integrity and scope

Inputs were the eight `out/second/H156-01_156-7_scanNNN_first.tsv` files, their neutral box lists where needed, the frozen initial page copies, and `out/second/INITIAL_FROZEN_SHA256.json`. The freeze manifest is dated **2026-11-20 19:24:24 UTC**.

All **8 first TSV hashes** match that frozen manifest. All **8 initial page-copy hashes** match the manifest's recorded original page hashes. Thus the two empty fields and the explicit illegibility marker are properties of the frozen first artifacts, not changes made during this review.

The freeze manifest's general assertion that the first TSVs were “complete” should be qualified in the audit: all 290 box rows were present, but two reading fields were empty. This review is limited to blank/placeholder coverage; it is not a full word-for-word alignment of every nonempty excerpt against the initial pages, and it makes no new transcription decisions.
