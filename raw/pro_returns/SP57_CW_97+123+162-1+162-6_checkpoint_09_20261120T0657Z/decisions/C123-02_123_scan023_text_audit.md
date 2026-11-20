# C123-02_123_scan023 — text-only coverage audit

## Scope and result

Read all three complete `reading.tex` files and complete `report.json` files in `out/readers/C123-02_123_scan023/{R1,R2,R3}/`, plus the packet’s `C.tex`, corrected `H.tex`, and `C_questions.md`. The reports contain 35, 34, and 36 difference entries respectively. No images, crops, OCR, web material, other-page files, excluded cover, or root decision files were consulted. This is an audit of what the saved texts and reports actually encode, not an independent determination of the ink.

All C questions have coverage. The three readings share the same complete body text and mathematical expressions, apart from localized readings, uncertainty scope, correction representation, and drawings identified below. Their reports do **not** establish identical graphic coverage.

### Material coverage failures or divergences

1. **Extra cancellation x after deleted “this”: omitted by every reading.** R1-D08 explicitly says “an extra x continues past the word.” All three saved texts have only `\deleted{this} for`; none has an additional x or corresponding independent graphic. R1’s inventory also lists only cancelled “this.” This matches the parent’s supplied coverage concern; this audit supplies no additional ink judgment.
2. **Detached high signature point: R1 only in the saved drawings.** R1-D34, its inventory, and its saved `\fill (7.93,-.32) circle[radius=.012cm];` agree. R2-D31 independently mentions a “separate high speck to the right,” but R2 does not draw or separately inventory it. R3 does not record it. R2’s final `\fill (0,0) circle (.10pt);` belongs to the much lower interrupted trace and cannot discharge the signature-point omission.
3. **D-subscript lower-right tail: R3 describes it without separately drawing it.** R2-D12 and its inventory explicitly include the low projection; R2’s D cell has `\draw[line width=.25pt] (.16,-.13) -- (.23,-.42);`. R3-D14 describes a “short oblique lower-right tail,” but R3’s D cell contains only the two r/n glyph nodes, with no independent tail stroke. R1-D12 mentions lower offset ink and draws an r/n overlay, but does not separately describe or draw the same oblique tail. Whether a glyph contour alone suffices is an ink/layout decision; the three saved constructions are not equivalent descriptions.
4. **Lower interrupted trace: three distinct constructions.** R1 draws **five line segments**; R2 draws **a top point plus six line segments**; R3 draws **four line segments**. R1’s explicit five-segment report matches its file; R2/R3 describe the count generically. All preserve a trace, but agreement on its existence must not be reported as agreement on its topology.
5. **Answer’s w-like cell: different graphic commitments.** R1 draws w with a separate rounded outline and also offers u; R3 overlays w and u; R2 uses only `\unsure{w|u}`. R2’s report/inventory describes a doubtful letter rather than promising an extra drawn contour, so this is primarily a cross-reader coverage difference, not an internal false drawing claim.
6. **Candidate sets are not equally explicit in the saved TeX.** R1 explicitly serializes a same-letter subscript alternative as `|\mathbb{r}` at both A and D. R2/R3 mention same-letter restriking in their reports but save only an uncertain n/r overlay. R3 allows e/e as well as e/o in the dimension report but draws one uncertain e/o overlay; R1/R2 explicitly encode both candidate shapes. These are differences in how much of the reported alternatives reaches the text. In particular, `\mathbb{r}` is an alphabet/glyph construction, not automatically an exact representation of two displaced r impressions.

## Exhaustive union of reported substantive differences

References below identify each reader’s difference entries. Grouped rows retain every separately reported occurrence. “All” describes agreement in the saved reading/report, not verification from the image.

| Locus | Report entries | Coverage and exact textual issue |
|---|---|---|
| `beinteresting` and raised stroke | R1/R2/R3 D01 | All retain no supplied word space and draw a stroke over e, replacing C’s freestanding raised bar and H’s space. R3 additionally describes and draws a darker short upper segment; R1/R2 use one uniform stroke. |
| Six Lie-algebra loci | R1/R2 D02–D05, D18, D21; R3 D02–D05, D20, D23 | First g→h/W, defining g, Cartan h, G-on-g, x-in-g, and repeated g→h/W all retain ordinary underlined letters against H’s explicit Fraktur. This covers eight individual g/h glyphs. |
| `analoguous` | All D06 | All read H’s `analoguous` against C’s `analogous`. |
| Cancelled fragment before `map` | All D07 | All save `\deleted{applic\unsure{at}i}`: cancellation retained, doubt narrowed from C’s entire `applicati` to at. H omits the fragment. No reader completes “application.” |
| Cancelled `this` | All D08 | All retain C’s deleted word omitted by H. Extra trailing cancellation x is report-only in R1 and absent from every text; see above. |
| Raised n-, medium, leader, point | R1/R2 D09; R3 D09–D11 | All preserve raised n- separately from r-2, draw the curved leader and low point, and withhold a certain handwritten attribution. R2/R3 prefer typed appearance; R1 leaves the medium open. H’s final note explicitly calls n- handwritten, so the medium conflict is substantive. R3 expressly doubts the low point’s origin/function; R1 inventories its medium as uncertain; R2 groups it with the pen leader. |
| Cancelled and lower retyped phrase | R1/R2 D10; R3 D12 | All stack deleted `the next lower after` above its live retyping. C preserves both strings but linearizes them; H preserves only the resulting phrase. |
| A subscript | R1/R2 D11; R3 D13 | All replace C’s old/new chronology and H’s uncertain n with a doubtful n/r overlap. Same-letter alternative differs in explicit encoding as noted above. |
| D subscript | R1/R2 D12; R3 D14 | Same chronological/candidate issue as A; D has the additional lower-right-tail coverage problem. |
| Raised `all` and leader | R1/R2 D13; R3 D15 | All retain handwritten all and draw its curved, unheaded connection to before other. Both witnesses know the word; H explicitly calls it handwritten. The substantive addition is shape/placement of the leader, not merely a handwriting wrapper. |
| `caracteristic` | R1/R2 D14; R3 D16 | All agree with H against C’s `characteristic`. |
| Cancelled extra homogeneous cell | R1/R2 D15; R3 D17 | R1/R2 save definite deleted a, confidence high. R3 retains deleted `\unsure{a|u}`, confidence medium, agreeing with C’s unresolved candidate set. H omits the cancelled cell. This remains a genuine reader conflict. |
| Quotes around homogeneous | R1/R2 D16; R3 D18 | All retain paired upright quotation strokes against H’s guillemets. The cancelled-letter disagreement is a distinct issue. |
| Dimension crowded vowel | R1/R2 D17; R3 D19 | All preserve lower e and a raised rounded impression without C’s chronology. R1/R2 explicitly allow raised o/e; R3’s report allows the same, but its saved graphic is an uncertain e/o overlay. H has clean `dimension`. |
| First and second Brieskorn cells | R1/R2 D19–D20; R3 D21–D22 | Each saved reading contains two separate e/i composites. All decline C’s inferred strike order; H has only clean `Brieskorn`. Node painting order does not itself establish chronological disagreement between readers. |
| Quotes around rational | R1/R2 D22; R3 D24 | All retain upright paired quotation strokes against H’s guillemets. |
| f/s cell in `if` | R1/R2 D23; R3 D25 | All draw both contours and withhold C’s s-then-f chronology; H has clean `if`. |
| Two middle cells of `then` | R1/R2 D24–D25; R3 D26–D27 | All draw both h/e composites separately, without C’s stated old/new order; H has clean `then`. |
| Underlined O | R1/R2 D26; R3 D28 | All retain ordinary underlined O against H’s explicit script O. R2 implements the O/F-prime assembly graphically, which is equivalent symbol coverage rather than an omission of its reported `\underline{\mathrm{O}}_{\mathrm{F}'}` snippet. |
| Cancelled upper-right O-adjacent sign | R1/R2 D27; R3 D29 | R1 keeps t before star in the alternatives; R2/R3 put star first. All retain both candidates and cancellation. R2 uses a local drawing beside O rather than a mathematical superscript; R1/R3 use superscript syntax. H suppresses the sign. Candidate preference and physical placement must remain distinguishable. |
| Answer w-like cell | R1/R2 D28; R3 D30 | New local doubt absent from C/H. R1 custom composite plus u alternative; R2 w/u alternatives only; R3 w/u composite. No reader supplies a plural s. |
| Extra upright at answer e | R1/R2 D29; R3 D31 | All draw it. R1 leaves e definite and draws the trace without an enclosing doubt macro. R2/R3 enclose e-plus-trace in `\unsure` although their prose identifies e. Confidence: R1/R2 medium, R3 low. Function/medium doubt should not silently become uncertainty about the readable e. |
| Underlying ot/to and pen to | R1/R2 D30; R3 D32 | All retain `\deleted{\unsure{ot|to}}\handwritten{to}`, agreeing with C and restoring layers omitted by H. |
| Signature name uncertainty | R1 D31; R2 D32; R3 D34 | All narrow C’s uncertain Grothendieck to definite G plus uncertain rothendieck. H prints the whole name without explicit uncertainty. |
| Period after A | R1 D32; R2 D31; R3 D33 | All omit H’s supplied period, agreeing with C. R2’s evidence additionally identifies the undrawn high speck. |
| Closing/signature placement | R1/R2 D33; R3 D35 | All give the signature a substantial rightward offset on a lower line. R1 uses a combined figure; R2/R3 use horizontal spacing. The shared positional relation is preserved; these implementations are not exact geometric agreement. |
| Detached signature point | R1 D34; R2 D31 evidence only | Actual independent point in R1 only. R2 reports but does not encode it; R3 has neither entry nor point. |
| Lower interrupted trace | R1 D35; R2 D34; R3 D36 | All draw a separate lower trace with unresolved ink/surface origin, but with different point/segment constructions detailed above. |

## Every C doubt and warning

Question numbers follow the order of the 16 rows in `C_questions.md`. Repeated warnings are identified explicitly rather than counted as unaddressed omissions.

| C question(s) | Coverage in all three readers |
|---|---|
| 1: deleted `applicati` | Covered in differences, c_doubts, inventory, and saved text; narrowed to at with final i definite. |
| 2 and 12: A/D identities and strike order | Both cells separately encoded; chronology remains open. R1’s explicit same-letter alternative differs from R2/R3’s report-only alternative. |
| 3 and 13: extra homogeneous letter and cancellation | Cancellation retained by all; a versus a/u remains unresolved across readers. |
| 4: dimension vowel | Lower e plus upper rounded contour retained; order not asserted. Explicit o/e alternative scope varies. |
| 5: both Brieskorn cells | Both cells covered independently; no old/new order imposed. |
| 6: cancelled sign above F-prime | t and star both retained; R1 preference differs from R2/R3, and R2 preserves placement graphically. |
| 7: old ot/to below handwritten to | Covered and retained unresolved in all. |
| 8: signature | Covered; A and G treated as definite, remaining name tentative. |
| 9: `beinteresting` | No supplied space; over-e trace drawn by all. |
| 10: `how varies` and `rang` | Both source forms retained verbatim by all. No syntax or spelling repair. |
| 11: n- addition before r-2 | Addition remains separately placed; its glyphs are definite and medium disputed. Leader and point are added to C’s coverage. |
| 14: if/is overprint | Both s/f contours retained without certain chronology. |
| 15: tehn/then corrections | Both middle composites retained without certain chronology. |
| 16: singular answer followed by plural are | Agreement retained by all; the newly marked w/e traces are independent of grammatical number. |

The packet’s current-page contextual cautions are also preserved: the text continues an opening question; “There are some reasons to believe,” “I would expect,” “maybe,” and “would imply” remain qualifications. No reading inserts a proof or promotes the expectations to established results. The closing, absence of date/title/authorial pagination/total count, and archive-number-only comment are covered in all reports. The prior-scan summary in C_questions supplies context, not text to import onto this page.

## Inventory and graphic reconciliation

All inventory entries were compared with the saved TeX. The common inventories correspond to actual text or drawing for: the opening continuation; main paragraph; raised e trace; five rightward arrows including the labelled resolution arrow; two membership signs; E subscripts 6, 7, 8; <, ≤, >; f’s subscript star; the cancelled fragment and this; raised n-, leader and point; two stacked repeated-phrase rows; two diagram-index composites; raised all and its curve; homogeneous cancellation; dimension composite; two Brieskorn composites; if composite; two then composites; the cancelled O-adjacent sign; answer’s local treatment; old ot/to and pen to; closing; autograph; and lower trace.

The exceptions/qualifications are the extra x, detached signature point, D tail, answer-w contour choice, and differing lower-trace construction described above. No whole paragraph, formula, closing, or ordinary inventory object is absent from any of the three readings.

The archive `22` is present only as `% archive sheet number: 22` in each reading. Its inventory status “transcribed: yes” means comment coverage, not a typeset authorial page number.

R2-D17’s report snippet ends `\end{tikzpicture}%nsion`. The **actual file** has a newline after the percent sign and then `nsion`, so the saved reading does not lose that suffix. This is a nonliteral report-excerpt serialization issue, not a transcription omission. Similarly, report snippets spanning the whole Brieskorn/then/answer composite do not mean their separately described cells are missing.

## H markers and exclusions

- **marked_in_H is correct in every difference entry:** true only for A and D subscripts (R1/R2 D11–D12; R3 D13–D14). Corrected H has exactly those explicit `\uncertain` markers and no `\ill` marker.
- H’s final editorial note about handwritten n-, handwritten all, overstruck A/D, and the handwritten signature is **not** an uncertainty marker. Its explicit medium claims nevertheless count as witness assertions. Thus the n- medium disagreement is substantive even though marked_in_H is false.
- Do not create additional medium discrepancies merely because H omits C’s `\handwritten` wrapper at arrows, relations, subscripts, or corrected to. A wrapper’s absence alone supplies no contrary medium assertion.
- Exclude ordinary `\mathrm{G}` versus `G` and analogous upright/default math choices, spacing commands, source line wrapping, `resp.\`/`i.e.\` spacing, `\overset` versus `\xrightarrow` for the same labelled arrow, and `\longrightarrow` versus `\to` where the same single rightward relation is represented.
- Exclude the page-identification macro difference (`\scanpage{23}` versus `\page{22}`) as an additional body-text conflict. Scan 23 and the archive-sheet comment 22 play different identification roles.
- Do **not** exclude the explicit Fraktur-versus-underlined alphabets, script-versus-underlined O, guillemets-versus-upright quotations, omitted cancellation layers, or genuine placement/mark differences as “macro-only.”
- TikZ units, node names, parameter values, and reverse traversal of the same unheaded curve do not by themselves establish a new substantive reading. Segment/point count, an independently described tail, and a separate high point are different: those change the claimed mark coverage.
- The corrected H packet ends with the letter and its editorial note. No title or cover content from the following unassigned scan belongs to this audit.

The remaining ink adjudication is for the parent. This audit does not revise any reader file or choose among their contested marks.

