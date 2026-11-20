# C123-02_123_scan040 — text-only cross-reader audit

## Scope and status

This audit compares the saved text of R1, R2, and R3. It does **not** adjudicate the source ink. No image, crop, image viewer, OCR, web source, other page, or external edition was opened. No reader file was modified.

Inputs read: `out/briefs/reader_v12.md`; this page's `C.tex`, `H.tex`, `C_questions.md`, and `meta.json`; all three readers' `reading.tex` and `report.json`. `out/PREAMBLE.tex` was additionally read solely to establish what the state macros actually do. In that preamble, `\inserted` adds angle brackets without raising its content, `\deleted` applies `\sout`, and `\handwritten` is an identity wrapper. These macro definitions matter to the placement/coverage findings below.

R3 revised its files during this audit. The final comparison uses its refreshed reading (file modification time `2026-11-20 06:07:08 +0100`) and refreshed report (`06:08:04 +0100`). An earlier R3 report/file mismatch and malformed witness quotations were corrected in that revision; they are not listed as outstanding defects. R1 and R2 were unchanged during the comparison.

The saved returns contain 45/43/49 difference rows, 58/77/67 inventory rows, and 10/11/9 remaining-doubt rows respectively. These are reader-report row counts, **not** independently reconciled correction totals.

## Main findings

The three readings have the same continuous French wording and mathematical expressions apart from the explicit state/uncertainty alternatives described below. A text-only extraction that removes drawing commands and wrapper syntax gives identical word/token multisets for R1 and R3. R2 adds exactly fourteen literal cancellation-space `x` marks and one extra occurrence of `pas` because its local alternative prints both live and deleted `pas`. This check supplements, rather than replaces, the manual comparison of the complete texts.

The decisive current encoding/apparatus issues are:

1. **R1 has an invalid TikZ coordinate** at reading line 36: `--q.south east;` must have coordinate parentheses if that path is retained. Brace/environment balance does not catch this.
2. **R2's claimed contact between the u-map enclosure and the two arms around `est un` is not encoded.** Both arms start `.2em` to the right of the map's right side, as explained below.
3. **All three flatten the reported raised `parmi` and the reported separately raised `en`.** Their `\inserted` wrappers do not raise these words. R1 also flattens the reported raised `s'étend pas`; R2/R3 supply an explicit raised node for that replacement.
4. **R1/R3 omit fourteen explicit cancellation-space x impressions that R2 records**: four within `comme nous le verrons au`, one between `se` and `donne`, and nine within the long cancelled exactness clause.
5. **R3's `est un` contour change is incorrectly marked `c_changed:false`** in D046. Its C quotation excludes the very curve being changed.
6. **R3 D037 treats H's synopsis alphabet as a direct source-glyph error.** R1/R2 explicitly avoid doing that. H's `\mathcal{U}` occurs in the editorial synopsis, not a literal transcription of the source occurrence.

R2 is the only return that places the upper continuation before the opening typescript and the footer continuation after the final typescript. That is a real placement advantage in the code, independent of whether its individual stroke choices are correct. It does not settle the other disagreements.

## A. Substantive cross-reader disagreements

Line references below refer to the audited saved `reading.tex` files. Descriptions of source evidence are attributed to the reader reports; none is a new image observation by this auditor.

| Locus | R1 | R2 | R3, refreshed | Consequence for reconciliation |
|---|---|---|---|---|
| Upper marginal continuation | `les opérations…etc.` follows the `De plus` insertion, after the opening sentence (15–22). | Whole upper continuation precedes `sent…` (5–17). | Whole upper continuation follows the ending/De-plus layout, after the opening sentence (14–24). | R1/R3 retain C's semantic insertion-point ordering; R2 explicitly preserves the physical upper-note position. |
| Bottom marginal continuation | Placed inside the `Par suite` insertion before section 3.1.3 (55–60). | Placed below an anchored final `Lorsque…g` block (114–120). | Placed inside `Par suite` before section 3.1.3 (68–77). | R1/R3 preserve the link but relocate the footer; R2 preserves its lower-page relation and separator. |
| Page number 23 and arch | Adds a separate arch over/around `23` in the mspage drawing (2–5); D01 says a distinct rising curved stroke. | Plain `\mspage{\handwritten{23}}`. | Same plain number. | A separate source-stroke disagreement. R1's arch is actually encoded; this is not merely a report claim. |
| Initial `les` in top note | Baseline `les opérations`. | `les` is a separate raised, slightly left-shifted node above `opérations` (8); D07 and inventory 3. | Baseline `les opérations`. | Placement disagreement. No reader has an independent additional hook/slant in this local node; that would require root's own evidence. |
| First upper-note call sign | One shaft returning into one lower loop. | Shaft, open lower ellipse, and separate filled upper component (7); D08 explicitly calls it a filled small upper loop plus open lower loop. | One shaft returning into one lower loop. | R2 contains additional literal ink absent from R1/R3 and C. Its other member of this call pair remains a simpler lower-loop form. |
| Thin trace after `inductives)` | Separate unsure close-shaped curve between typed close and stop (9). | Separate unsure close-shaped curve in its own node, before the typed stop (19–24). | One definite continuous thin path from the ending area into the lower boundary of the raised `De plus` addition (6–13), without an unsure wrapper. | Disagreement in connectivity and uncertainty. R3 resolves the function/connection as a boundary; R1/R2 leave it open. R3's latest code now matches its connected-boundary report. |
| Heavy paragraph brackets | Both opposing bracket paths are tied to the `Quant au` picture (33–37); the left member sits left of Quant. | Heavy closing member surrounds the preceding ending/stop; opening member surrounds `Quant au` in a different picture (23, 37). | Heavy closing member around the prior ending/stop, opening member around `Quant au` (12, 34). | R1 assigns a different textual attachment to one bracket. This is more than a stylistic path variation. |
| `De plus` placement and lower boundary | Separate inline picture after the opening sentence; lower path has a right-hand dip (11–14). | Raised above `Quant au`; lower path ends along the underside with no explicit downward/right-end dip (32–38). | Raised above/right of the `inductives).` node; one connected path includes the close-shaped left part, long underside, and right dip (6–13). | Three different spatial constructions. The R2 boundary has less right-end contour detail than R1/R3. |
| Raised `:E→E′` map | Node is anchored above `d.north west`, where `d` includes `u_*` and comma (37–41). | Node anchored above/right of `direct.north east`; comma is a separate baseline node, and the leader starts by the comma (40–45). | Node anchored above/right of `direct.north east`, but `direct` already contains the comma (37–41). | Same map and live comma, different addition placement. R2 most explicitly distinguishes the comma's baseline location from the map. R1 puts the map farther left than the other two. |
| Trace after second `épimorphisme` | Conventional alternatives `\unsure{;|,}` (51). | Unsure literal shaft/tail, complete ellipse, and detached upper angle, using three paths (61–65). | Unsure literal shaft/tail, additional bowed loop-forming stroke, and detached upper hook, using three paths (56–60). | R1 loses the separately drawn rising shaft/upper angle described by R2/R3. R2's full ellipse and taller shaft differ from R3's partial bowed stroke and shorter proportions; root must choose the literal contour. |
| Following opening parenthesis | Plain `(` outside handwritten wrapper. | Explicitly handwritten `(`; inventory 35 calls it a large opening-parenthesis insertion. | Plain `(` outside handwritten wrapper. | R2 makes an explicit medium claim. A wrapper-only difference must not by itself become a witness error count, but this is a real report-level assignment to review. |
| Extra x before `comme` | Definite `\texttt{x}` on the ordinary baseline, followed by a separately unsure upper-right oblique tick (51–54). | Definite lowered x (`yshift=-.4ex`), plus horizontal pen cancellation and an ascending tick (67–72). | Definite baseline roman x, horizontal pen line and short tick (61–66). | Vertical placement of the x differs. R1 marks the tick's function uncertain; R2/R3 draw it without local doubt. Typography of x alone is not counted as an independent reading difference. |
| Interword cancellation-space x impressions | None explicitly drawn within the three runs below. | Four between the five words `comme/nous/le/verrons/au`; one between `se/donne`; nine between the ten words `y/compris/et/de/déterminer/s'il/admet/un/foncteur/exact` (68–72, 83, 96). | None explicitly drawn within those three runs. | Exactly fourteen additional cancellation marks in R2. Generic `\deleted{…}` creates a strike, not literal x impressions in the spaces. All three do draw the separate initial x before comme and final x after g. |
| Horizontal pen cancellation over the beginning of the `comme` clause | No separate long pen line; only generic deletion strike and the small unsure tick. | Separate horizontal line from the lowered x through `comme` and `nous`, plus tick. | Separate horizontal line from initial x to `([xshift=.25\linewidth]comme.west)`, plus tick. | R2/R3 preserve an additional pen line. Their right endpoints also differ: R2 is word-anchored, R3 depends on page linewidth. R1 D23 acknowledges pen cancellation but does not draw that separate line. |
| Cancelled `transforme` | Certain `\deleted{transforme pas}` (55); D24 high confidence. | `\deleted{\unsure{transforme}}` (76). | `\deleted{\unsure{transforme} pas}` (70). | Substantive certainty difference even though the preferred word agrees. |
| Lower `pas` after cancelled transforme | Definitely deleted as part of `transforme pas`. | `\unsure{pas|\deleted{pas}}`: live/deleted alternatives. | Definitely deleted. | Separate deletion-boundary disagreement. R2's extra lexical `pas` is only the written alternative, not additional source prose. |
| Raised replacement `s'étend pas` | Inline `\inserted{s'étend pas}` after the cancelled baseline phrase. | Explicit raised node over `old`. | Explicit raised node over `trans`. | R1's report and inventory say raised, but its macro-only encoding is not raised in this preamble. |
| Section replacement and leader before `un` | Cancelled `se donne` is outside the picture; node contains actual `un`; raised replacement anchored above/right relative to un (62–66). | Separate cancelled `se`/`donne` and live `un` nodes, both inside one picture; leader explicitly begins by un (82–87). | One combined node contains `\deleted{se donne} un`; leader starts 4 mm left of that combined node's right edge (80–84). | All include the intended baseline word, but the geometry differs. R2 directly anchors the leader to un; R3 approximates un's left location using an offset from the whole phrase. |
| First formula enclosure, `f=u^*,` | Straight left side. | Straight left side. | Bowed left side with a Bézier segment (98); D044 describes it. | A literal contour disagreement. All retain the comma inside the first enclosure and its two lower outward feet. |
| Second formula enclosure and `est un` | Separate map and `est un` pictures; curved upper and lower arms around est un. | Both text nodes in one picture; two arms start at a common point near est un; report claims contact with map enclosure. | Separate map and `est un` pictures; curved upper and lower arms around est un. | R2 intends a connected topology, but does not actually join the arm starts to the map border. R1/R3 do not encode such a contact at all. See section B. |

### Contour variations that preserve the same broad topology

These remain differences in the supplied code, but should not automatically become separate reading-error counts:

- The upper note's stepped lower enclosure is inherited as a short diagonal rising step in R1/R3, but is a vertical step at the south anchor in R2. All show a left-and-lower boundary with top and right open, with the same broad coverage.
- The left margin instruction is the same two rows in all three. R1/R2 rotate the entire layout by 12 degrees. R3 rotates the first row by 8 degrees and the second by 12 degrees, with an independently slanted boundary. Row staggering and open-left enclosure agree; exact slopes/lengths differ.
- The leaders for `peuvent`, `par suite`, `exclusivement`, `toutes`, and `une` use different offsets and Bézier controls. All include the appropriate baseline word in a node and preserve the left descent/under-running line/right rise. R1 often centers the raised words; R2/R3 use left anchors. No additional lexical or endpoint-target disagreement was found at these five loci.
- The f/c and the two é/t overlaps have small offset differences. All three preserve both contours and explicitly leave chronological order doubtful; none promotes them to same-letter double striking.
- The footer call pair uses C-like continuous closed cubic loops in R1/R3 and separately drawn ellipses plus shafts in R2. Their upper-loop/descending-shaft topology agrees. Separator-jog geometry and position differ, chiefly because R2 puts the separator at the physical footer while R1/R3 put it in the earlier insertion block.
- R2/R3's short pen tick over the first cancellation x is rendered as definite, whereas R1 puts its drawing under `\unsure`. This uncertainty difference is substantive; the small typographic difference among texttt/plain/roman x is not.

## B. Report-to-file coverage and placement audit

### B1. Definite current gaps

**R2 D35 and inventory 69: claimed contact at the u-map.** The `est` node is anchored at `([xshift=.5em]u.base east)`. Both arm starts are `([xshift=-.3em]est.west)`. Since west/base-west and east/base-east share their horizontal coordinates, these starts lie approximately `.2em` to the right of the u-node's right side. The enclosure itself follows `u.north east` to `u.south east`. No connecting segment reaches either arm start. Putting the drawings in one picture has not made the reported contact. If root's ink decision requires contact, use an actual shared border anchor, such as the appropriate point on `u.east`, for both starts.

**All readers: raised `parmi`.** R1 D17, R2 D17, and R3 D017 say the typed replacement is above cancelled `dans`; their inventories also distinguish the raised replacement. Every reading instead has `\deleted{dans}\inserted{parmi}` inline. Because `\inserted` only adds angle brackets, the saved text records replacement state without reproducing the claimed vertical placement.

**All readers: separately raised `en`.** The reports repeatedly say handwritten `en` sits above the gap after typed `est` in the raised phrase `est présenced'`. Every reading places `\inserted{\handwritten{en}}` inside the same text node as `est` and `présenced'`. The entire replacement is raised, but en is not separately raised within it. A second small node is needed if that reported two-level placement is to be preserved literally.

**R1 D24/inventory 31: raised `s'étend pas`.** R1 uses only adjacent `\deleted{transforme pas}\inserted{s'étend pas}`. Its report says the replacement is raised. R2/R3 actually encode that relation with a separate node.

**Separate pen cancellation around `comme`.** R1 D23 says pen and x cancellation are real, but the long pen run is absent as an independently positioned stroke. R1's small tick is encoded. R2/R3 separately draw the horizontal pen run and tick, in addition to the generic deletion strike.

**Pen cancellation of `l'`.** R2 inventory 62 explicitly assigns both x overtyping and pen; R3 D043/inventory 59 also mention x/pen cancellation. All saved readings contain only generic `\deleted{l'}` plus the curved insertion leader. No distinct oblique pen-cancellation path is drawn over that cell. The reports alone do not establish the exact number or endpoints of those pen strokes, so this is a coverage issue requiring root's source decision, not a shape reconstruction by this auditor.

### B2. Claims requiring qualification

- R2 D10 says the thin closing-shaped stroke joins or nearly touches the `De plus` boundary. Its saved code puts the thin stroke and the De-plus boundary in separate pictures and does not preserve a literal join. Because the report itself leaves contact uncertain, do not manufacture a definite join merely to satisfy that sentence. The report/reading should consistently describe whichever broad relation root preserves.
- R3 D029 mentions a nearby detached point in the vertical neighbourhood of the following line's `produit`, while rejecting it as decisive evidence for a comma after `groupe`. No independent point is drawn. The report does **not** say whether that is an extra mark or the ordinary dot associated with the word below. Text alone cannot establish an omitted independent point; keep this as an unresolved coverage question rather than asserting a missing stroke.
- R1/R3 label upper/footer notes as marginal in their inventories and give source-position boxes, but their saved reading order relocates both notes to insertion points. The call marks are present; the physical location is not. This is explicit in R1's comment and apparent from both code sequences.
- R2's statement that all reported curves have corresponding content is correct for existence of the arm drawings, but too broad if interpreted as confirming their claimed connectivity or all raised-word geometry. The structural checks did not establish those properties.

### B3. Coverage that is present

All three actually encode the top deleted illegible word, the retouched `nt` and doubtful `r`, both call-sign pairs, upper-note enclosure, slanted margin instruction and enclosure, direct-map/par-suite/exclusivement/toutes/une leaders, f/c and both é/t overlaps, cancelled e, cancelled comme clause, cancelled se donne, cancelled long exactness clause, cancelled qui, cancelled l', both formula enclosures, doubled opening quotation pair, cancelled final g, and separate following x. No empty unsure wrapper or empty difference-reading field was found. This statement concerns textual encoding, not visual fidelity.

## C. Syntax and structural checks

### C1. Definite syntax defect

R1 reading line 36 ends the second Quant-au bracket with:

```tex
--q.south east;
```

TikZ coordinate syntax requires:

```tex
--(q.south east);
```

The same defective source fragment propagates into the relevant R1 report excerpts. This is one defect at one source locus, not multiple independent reading errors.

### C2. Checks performed and their limits

A text-only scan of all three complete readings and all difference `reading` fields found balanced unescaped braces, matched begin/end environments, and even numbers of math-dollar delimiters. The complete readings contain 23, 21, and 22 explicit `tikzpicture` environments respectively. Every required difference field is present and every `reading` field is nonempty. Every inventory position is numerically inside the reported 1684 × 2141 page bounds. These checks do not verify coordinates against pixels, actual stroke visibility, rendering, line wrapping, glyph fonts, or compilation.

No TeX compilation or rendered preview was performed by this auditor. No syntax defect beyond the bare R1 coordinate was identified by the limited textual check.

## D. Witness-locus and apparatus audit

### D1. H's synopsis must remain distinct from direct quotation

H begins with `\note{Feuillet de tapuscrit…}`, an editorial synopsis. Its direct marginal transcriptions and exact quoted insertions are distinct passages. R1 and R2 expressly respect this distinction; most of R3 does too.

**Outstanding exception: R3 D037.** It calls underlined ordinary U versus H's `\mathcal{U}` a `misread symbol or index`, with `h_changed:true`, and says H writes calligraphic U “in its synopsis of this occurrence.” That is exactly the locus distinction required by reader_v12: a synopsis alphabet is not evidence that H directly transcribed this particular source glyph in that alphabet. R1 D33 and R2 D25 correctly place this under missing literal body text and avoid counting a demonstrated source-glyph misreading. R3 D037 should be recategorized/qualified or removed as a separate direct-glyph correction in the reconciled apparatus.

The synopsis also uses final section number 3.1.3 and fluent final wording such as n'est. The readers generally classify the untranscribed underlying 2/e and other cancelled words as omissions, not assertions that H saw them live. That handling is appropriate. H's `\page{39}` and manuscript `23` have different functions; none of the reports needs a false numeral misreading `39→23`.

### D2. Incorrect or incomplete graphic change accounting

**R3 D046:** `c_changed:false` is inconsistent with the actual C path. C has a straight upper branch from an offset near `n.north` to `(n.west)`; R3 uses a Bézier upper arc starting near the upper right. R3's C field quotes only `\node…{est un};`, thereby excluding the very contour being changed. Quote the full C curve and set the change flag according to the root's retained contour. R1 D41 explicitly records this change against C.

**R2 De-plus lower boundary and opening bracket:** R2 has a new lower boundary under De plus and a word-anchored opening bracket around Quant au. The boundary is inventoried and is present in reading.tex. D10's evidence speaks broadly of both opposing paragraph marks, but its `reading` field contains only the ending's closing bracket and thin trace; its C field quotes only `inductives)\handwritten{)}.`. No separate row clearly quotes and accounts for the newly drawn De-plus lower boundary or opening Quant bracket as changes from C's unattached bracket pair. A reconciled graphic locus should include the relevant full before/after layouts rather than relying on the inventory alone. The physical move of the upper continuation is also more explicit in the code/comment than in D08's call-mark-focused prose.

### D3. Literal witness quotations and marked doubts

In the refreshed reports, all nonempty C/H difference quotations are literal substrings of their supplied witness after whitespace normalization. Earlier R3 versions used `E\prime` and `s\prime étend pas` where the actual witnesses have apostrophes, and omitted local unsure wrappers from some reading excerpts; those defects were corrected before this final audit.

Only the top cancelled-word-placement row is marked `marked_in_H:true` in each reader (R1-D04, R2-D04, R3-D003). This agrees with H's explicit `\struck{\ill{}}` at its later `qui…peuvent` locus. The reports correctly distinguish moving that marked illegibility to the `fonctorielles…habituelles` locus from inventing a second cancelled word. General H editorial statements about crossed words are not falsely marked as explicit uncertainty markers.

Other direct H disagreements consistently identified by all readers are: `fonctionnelles` versus `fonctorielles`; the location of the cancelled illegible word; omitted nt/r correction state and doubt; literal quotation strokes/commute underline; `puis` versus `après` in the quoted margin instruction; `en présence d'` incorrectly attached to the Par-suite marginal note; footer `ou un` versus `en un`; and the omitted deleted le/de before module libre. These are genuine quoted-passage loci, unlike the U synopsis issue. This auditor does not choose the ink reading at any of them.

### D4. Noncontiguous or simplified excerpts that are not current defects

- The three margin-instruction `reading` fields concatenate the two rows into prose; their complete readings contain the two actual nodes.
- R2 D20/D30 give the deleted lexical phrases without the separately reported cancellation-space x marks. D21/D31 and the saved reading supply those marks; the simplified lexical excerpts are not omissions from the complete return.
- R2 D43 quotes the final prose without its separately reported final x. D37 and the complete reading supply it.
- R3 D001 linearizes opening text across its node boundary. R3 D011 concatenates the correct ending and Quant-au layouts across intervening top-note/margin content. These are currently correct component excerpts, not a renewed unsaved-layout discrepancy.
- Broad body-omission rows sometimes have `c_changed:false` although their long reading excerpt contains graphic edits separately listed elsewhere. Their stated locus is the literal body omission from H. Do not blindly count every changed character in a broad excerpt as another C error.

## E. Inventory and doubt coverage

All three reconsider every C doubt/question locus listed in C_questions.md, including the opening fragment, no supplied articles before épimorphisme, source spacing `présenced'`, f/c/e/t-é overprints, doubled opening quotes, final cancelled g, and the own/section numbers. The different remaining-doubt totals are explained chiefly by R1's extra doubtful pen tick, R2's doubtful transforme and lower-pas state, and R3's resolved connected-boundary interpretation. No C uncertainty was silently replaced solely by an agreed preferred word in the report.

R1's inventory is less granular about the three separate handwritten low-star additions on body u occurrences; R2/R3 list those individually. The stars themselves are present in all saved readings. R1/R3 mention the inverted archive number only in a code comment and notes, without a separate inventory row; R2 explicitly inventories it as an archive annotation whose medium is undetermined. These are inventory granularity differences, not missing manuscript numerals from the chosen text.

The reports distinguish local direction/notation checks from unproved mathematical assertions. Their prose does not claim a theorem about exactness or adjoint existence was proved merely by transcription. This auditor performed no mathematical proof and does not validate the readers' source-view workflow claims.

## F. Reconciliation checklist for root

Root should adjudicate the page-number arch; raised les and all associated traces; first call's filled/open components; the closing-shaped thin trace and its possible connection; the heavy brackets' attachment; De-plus right dip; exact direct-map placement; epimorphism punctuation's literal contours and opening-parenthesis medium; cancellation-space x counts and the small tick's uncertainty; transforme/pas state; and formula-enclosure/est-un connectivity. The shared raised-parmi/en gaps and separately claimed pen cancellations need actual geometric encoding if retained.

A single base reader cannot settle these points. R2 supplies physical top/footer order and explicit cancellation-space marks; R1 contributes the page-number arch and additional local uncertainty; R3 supplies the bowed first-formula enclosure and a different asserted top-boundary connection. These are descriptions of the saved returns, not votes about source truth.

The audit does not authorize new crops or repeat image views. Root can resolve each open issue from its existing authorized source observations and preserve uncertainty where those observations remain insufficient.

## G. Follow-up audit of root's specification and preview

At root's further request, this auditor read `out/decisions/C123-02_123_scan040_spec.json` and `out/decisions/C123-02_123_scan040_preview.tex`, still as text only. This section checks whether root's stated decisions are encoded; it does not independently certify the root's source observations.

Audited preview SHA-256: `b1a89644a787fbce938442f2e9c9ce249b4767456d3d8ab40da4aa9c3772bb93`.

### G1. Repairs confirmed in the actual consolidated code

The preview now contains the manuscript-number arch; raised les; a separately unsure pale slant by les; R2's filled/open upper call components; physical upper and footer note placement; separate unsure close-shaped trace; heavy ending and Quant-au brackets attached to their respective text; a right dip in the De-plus lower boundary; literal epimorphism punctuation and separately handwritten opening parenthesis; all fourteen interword cancellation x marks, in addition to the two standalone end-cell marks; raised parmi; separately raised en within the already raised section replacement; the raised s'étend pas; two oblique pen paths over cancelled l'; bowed left sides on the two formula enclosures; and both est-un arms starting literally at `(u.east)`.

The latter point resolves the prior report/code connectivity defect: `(u.east)` lies on the enclosure's right vertical border between its northeast and southeast anchors. The preview has two `\draw (u.east)` starts. No gap remains between that border and the two arms.

The new pale material near added à is drawn in two separate segments under a nonempty local unsure wrapper, with definite à in a different node. Its uncertainty does not swallow the known letter. The pale les trace similarly has actual drawing content inside the unsure wrapper.

The thin closing-shaped trace is left separate and unsure in the preview, and root D10 now expressly declines to assert the R3 connection. The code and the root's stated decision agree. Root's new ROOT-01/02/03 rows also now explicitly account for the De-plus lower boundary, opening Quant bracket, and physical upper-note placement that were incompletely described by the original R2 difference rows.

Root keeps the definite short pen tick at the leading cancellation x while declining to assign its function. That is not a missing mark: the path is present. The extra remaining-doubt row should continue to describe uncertainty of function, not a claim that the physical stroke is absent or unreadable.

### G2. Structural results for the consolidated version

- The specification's single full-text `old` replacement occurs exactly once in the R2 base. Applying the replacement reproduces the preview byte-for-byte.
- The merged apparatus has 48 unique difference IDs, 81 inventory rows, and 14 remaining-doubt rows.
- The preview contains 27 explicit matched TikZ picture environments. Braces and environments balance, and math-dollar parity is even.
- All 48 merged final excerpts are nonempty and pass the same limited brace/environment/dollar-parity scan.
- No empty unsure wrapper or bare `--name.anchor` token remains in the preview. The original R1 bare-coordinate defect is confined to the intentionally retained, unused reader return.
- The previous report-only raised words, pen strikes, and claimed est-un contact have actual code counterparts in the root preview. No further definite report-to-drawing omission was identified in this text-only follow-up.

These are structural checks, not TeX compilation, visual layout verification, or fresh source-image validation.

### G3. Witness-field provenance cleanup — resolved

The first audited root specification replaced several exact H fields with English explanations. The explanations were useful in `evidence` or `readers`, but were not quotations of the supplied witness. Reader_v12 requires the actual C/H string when comparing a witness. Root corrected this in the specification regenerated at **2026-11-20 05:18:19 UTC**. The targeted text-only recheck found **no remaining nonliteral nonempty C/H field** after whitespace normalization. The preview hash is unchanged, so the geometry and structural findings in G1–G2 still apply.

The affected existing override H fields were **R2-D01, D02, D13, D18, D19, D20, D21, D25, D27, D28, D29, D30, D31, D32, D33, D36, D37, and D43**. Examples included “Editorial synopsis only; no literal transcription of this source locus” and an English paraphrase of H's direct-image synopsis. These now use empty H fields for unquoted loci or exact French synopsis snippets for the main body passages; the explanations have moved into evidence.

The corresponding new-row repairs are recorded here for traceability:

| Row / field | Initial content type | Repair applied |
|---|---|---|
| ROOT-02 H | “H quotes Quant au but draws no bracket.” | Exact supplied H Quant-au quotation. |
| ROOT-03 C | “Top continuation is embedded after the later De plus insertion.” | Exact C opening-plus-note context excerpt. |
| ROOT-03 H | “H explicitly describes the continuation as at the top of the sheet.” | Exact supplied `\note{en tête du feuillet, encadré, relié par un trait à l'insertion suivante}` passage. |
| ROOT-05 H | “No literal source transcription here.” | Empty H field. |

This was a provenance/serialization issue, not a new source-reading disagreement. Root's treatment of the synopsis U as an omission rather than a demonstrated alphabet error is correct. The audit's original cross-reader findings remain relevant as a record of why the consolidated choices were necessary; they are not all outstanding defects in the root preview.

**Final text-only disposition:** no remaining concrete syntax, missing-path, claimed-connectivity, empty-field, or literal-witness-quotation defect was identified in the consolidated preview/specification within this audit's scope. Reader originals intentionally retain their documented defects. Source fidelity, crop observations, and visual rendering remain outside this text-only audit.
