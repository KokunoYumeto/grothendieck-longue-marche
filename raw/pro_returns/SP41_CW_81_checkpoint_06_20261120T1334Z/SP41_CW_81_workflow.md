# SP41_CW_81 workflow

## Run structure

Three fresh independent page readers per scan, each with fork_turns=none and only page inputs. Main reader compares returns and inspects crops. Model: GPT-6 Astra Pro (parent identity); inherited reasoning setting not exposed by the runtime.

## Initial brief

See briefs/reader_brief_v01.md (first used scan 027).

## Brief revisions

Before scan 028: page packets were tightened to remove the folder-wide C notes footer. The first scan 027 packet had included short notes about scan 030 and headings on 032–033; no other-page images or page transcriptions were included. All three scan 027 readers were explicitly instructed to exclude that footer from evidence. Their three independent ink readings remain retained. Subsequent packets contain only the assigned page’s C doubt/notation rows; the main reader holds folder-level notes.

## Crop counts and decisions

The page-by-page records below give created crops and actual main-reader image views.


### Brief v02, prepared during scan 027 adjudication; first use scan 028

- R1 and R2 supplied complete doubt decisions but used different locus IDs; v02 adds source C_doubt_index identifiers to make cross-reader coverage explicit.
- R1/R2 inventories used free labels (text block, margin, underlining, unruled manuscript sheet). v02 specifies the requested CSV enums; the main reader maps the first page’s raw labels to those exact categories without changing represented content.
- The verb ending in the slanted note and the state of très produced R1/R2 disagreements. v02 reinforces stroke-based endings and separating a t crossbar or retracing from cancellation.
- One reader reported extending a crop to recover clipped line beginnings. v02 asks for bounds checks and tight coherent strips before the one crop operation. The first page’s actual crop history is retained.
- The three drawing marks are physically distinguishable on the crops. v02 asks that relative alignment with the accompanying chain be preserved in the TikZ rendering.
- The first packet’s overbroad C notes footer was removed; each later packet carries only the assigned page’s notes.

The complete original and revised briefs are retained in briefs/.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 027 | 9 | 9 | 13 | 2 | 33 | 15 (13 existing + 2 new) |

Scan 027: all three returns compared; main adjudications include retained alternatives for the parenthetical bien pas/non pas, cancelled fragments, Pi/pi, and faint endings; left over-arrow resolved from crop 11. C’s 47 doubt macros are all represented in logged findings. The final text has 21 uncertainty macros. No OCR or mathematical proof check was performed.


### Scan 028 and brief v03, first use scan 029

R1/R3 represented the older Soit as a wholly deleted word; R2 retained the shared Soi and marked only the overwritten t. The main crop supports that local treatment. Brief v03 clarifies shared live letters in overwritten words. It also requests usable coordinate bounds for clear witness differences, allowing the main reader to crop them without asking the independent readers to repeat settled work.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 028 | 16 | 15 | 17 | 10 | 58 | 29 (19 existing + 10 new) |

The main reader viewed all sixteen R1 crops, R3 crops 06, 07 and 15, and ten new crops for clear witness differences without a reader crop. One earlier image-output call was truncated before its images reached the reader; those three images were emitted and actually viewed subsequently. No repeated crop was made. All 24 C doubts have a recorded decision; 13 uncertainties remain in the final text. The three complete readings agree on the overall text and graph. Differences concern accents, arrow preference, local overwrite scope and confidence at compact marks. Structural LaTeX checks passed; no compilation or mathematical proof check was performed.


### Scan 029 and brief v04, first use scan 030

All three complete readings and their finding lists were compared. Main crop inspection resolved bien, the first cancelled A and the live subdivision star, retained local uncertainty in the article and the final abbreviation, and included R3’s possible older Gamma beneath the NB script X. H explicitly maps underlined Gamma to bold Gamma, so mapped occurrences are excluded from collation; its final plain NB Gamma omits an actual underline.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 029 | 19 | 17 | 15 | 3 | 54 | 29 (26 existing + 3 new) |

The main reader viewed all 17 R2 crops, R1 crops 01, 03, 14, 15, 19, R3 crops 02, 04, 08, 11, and three new crops for arbre and the two NB endpoint clauses. An earlier image output was truncated before delivery and was not counted; the images were subsequently delivered and actually viewed. Reader edge-clipping notes are retained in their raw returns; no additional crop of a decided locus was made. All 28 C doubts are covered, with 16 uncertainties in the final text.

Brief v04 asks readers to save their complete text before composing the detailed JSON, so comparison can start earlier. It clarifies exact declared H rendering mappings, and limits insertion macros to actual insertion evidence while preserving possible older layers under overwritten letters. No OCR, compilation or proof check was performed.


### Scan 030 and brief v05, first use scan 032

All three complete readings and finding lists were compared. The main reader resolved the two written groups before images as les des with R2, retained R3’s open final subscript as c|a, and preserved six unresolved loci. The full H editorial note attributes the nonempty relation to the interlinear addition, so its narrower add-macro boundary was excluded as a separate state difference; the extra words and expanded abbreviation remain collated.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 030 | 12 | 12 | 12 | 3 | 39 | 17 (14 existing + 3 new) |

The main reader viewed all 12 R2 crops, R3 crops 09 and 12, and three new crops covering the clear H wording and punctuation differences. One earlier image-output call delivered only a truncation message; the four images were subsequently emitted and actually viewed, and the failed delivery is not counted. The new two-line wording crop contains all letter bodies and word endings but clips the bottom tip of the long q descender; the complete half readings and visible body settle the words, so the decided locus was not recropped. This edge limitation is recorded in its finding. All 13 C doubts have decisions: eight resolved, five retained. The new E-subscript uncertainty brings the final total to six. No OCR, compilation or proof check was performed.

Brief v05 extends the explicit-H-convention instruction to editorial notes that identify insertion or deletion state, avoiding a duplicate finding based only on macro boundaries. It also asks that original bounds include full long descenders and accents before the one crop is made.

### Scan 032 and brief v06, first use scan 033

All three complete texts, finding lists and inventories were compared. The final reading resolves indiciellement, final epsilon-prime in (3), cancelled la, and the older omega under the intersection. It retains the written omega superscript in (4), in agreement with C and H's explicit note, while recording H's displayed epsilon and S row SA01-K81-04's proposed epsilon. The final verb reads indique, and the large insertion attaches after sont. The tiny second accent gives acute first with a grave alternative; the two marks after ens are retained as colon|à. Every one of C's twelve doubts has a decision: four resolved and eight retained. Ten uncertainty loci remain overall.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 032 | 13 | 13 | 12 | 1 | 39 | 21 (20 existing + 1 new) |

The main reader viewed all twelve R3 crops, R1 crops 04, 06, 08, 10 and 11, R2 crops 11, 12 and 13, and one new crop for the second family letter in (2′). An earlier image-output call was truncated before delivering R3 crops 10–12; they were subsequently delivered and actually viewed. The failed output is not counted. The R2/R3 final-verb crops clip the lower q-descender tip; their decisive letter bodies and dots remain visible, and the readers reported the full descender in half b. No decided locus was recropped. No OCR, compilation or mathematical proof check was performed.

Brief v06 clarifies two record fields after all three readers treated H's confident editorial notes as doubt marks: marked_in_H is reserved for actual doubt/illegibility marks, with editorial notes recorded separately. It also requires the exact high/medium/low confidence values and explains that against_C includes uncertainty-markup changes without calling resolved primary readings errors. The root applies those definitions to this page's final apparatus. No additional instruction was needed for the remaining ink disagreements; their alternatives and crop decisions are recorded.

During the scan 033 reading stage, the clarified H doubt-field definition was checked against earlier final records. Scan 029 entries 028 and 043 were metadata-corrected from yes to no: editorial expansion/layout notes are not doubt marks at those exact loci. Entry 009 now quotes H’s explicit note proposing a crossed calligraphic A, instead of calling the older layer simply absent; the final plain A glyph decision remains unchanged. No page text was altered.


### Scan 033 and brief v07, first use scan 034

All three complete texts, findings, notes and inventories were compared. Main decisions resolve live Si, omega, both parenthetical primes, the low dot, cas, lowercase on, cond, the prose dot and definis. Older layers remain represented; five marks in (7) retain identity and state uncertainty. The final short indices keep 2|1, the final tag keeps 17|12, and the shared two-stroke prose ending keeps colon|à at its first occurrence. All 26 C doubts have a decision: nine resolved and seventeen retained; twenty uncertainty loci remain overall. The first parenthetical prime is already acknowledged by H's explicit correction note, and that note is quoted in the apparatus.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 033 | 15 | 13 | 17 | 7 | 52 | 27 (20 existing + 7 new) |

The main reader viewed all thirteen R2 crops, R1 crops 04, 10, 12, 13 and 15, R3 crops 11 and 13, and seven new crops for clear witness differences and S's complete local formula sequence. A failed image-output call did not deliver R1 crops 12 and 13; subsequent successful delivery supplied the counted views. No crop was remade. The main period crop clips unrelated portions of the preceding slashed oval, while the target point is complete. R3's proposed C omission of that point was rejected: exact text inspection confirms that C already contains it.

The manuscript's three lower formula bodies were confirmed against S SA01-K81-01, with its quoted prepositions qualified by the ink's colon/à uncertainty. The supplied concrete interval counterexample was computed using an exact seven-cell representation, whose inverse maps and operation preservation are documented. The true inclusions and intersection {2} refute the written equivalence for this concrete pair; the manuscript transcription remains unchanged by that calculation. These events are recorded as computation/certificate and refutation, separately from source-account notes. No OCR, external research or compilation was performed.

Brief v07 clarifies that uncertainty-only differences with H's same first reading do not count as H text changes, after several readers marked them as changes. It also requires exact witness-string checking before asserting an omission, prompted by R3's mistaken final-period finding. The raw return is preserved and the rejected candidate is recorded in the final decision.

### Scan 034 — brief v07 retained for the next page

All three complete texts and detailed returns were compared, including every finding, inventory, note and remaining doubt. The root resolves the first cancelled E1, written index 22, three-bar relation, bottom cancelled Sigma1-plus, final separator and final index 2. Other older layers remain uncertain. The final text preserves the first E2 factor's written index 1 and the marginal Sigma1-minus. It retains R3's additional roof-shaped accent uncertainty. All 23 C doubts are covered: six resolved and seventeen retained, with twenty uncertainty loci overall.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 034 | 17 | 15 | 16 | 3 | 51 | 22 (19 existing + 3 new) |

The root viewed all seventeen R1 crops, R2 03 and R3 03, and three new crops for the first E2 expression, the second family glyph and the diagram's label. An earlier image-output attempt for R1 04–06 returned only a truncation message; their later successful delivery supplies the counted views. No crop was remade. The E2 crop clips an unrelated preceding formula tail at the left; the target expression is complete. R3 records its own crop-edge limitation near the cancelled bottom starter, which the root viewed completely in R1's crop.

The three local margin crops show two separate et groups. R2 assigned only one to the main sentence and omitted the marginal connective; the root retains both with R1/R3/C and records that disagreement. Other differences concern the degree of confidence in tiny suffixes, cancellation boundaries and the accent. These arise from the local ink rather than an omitted convention, so no further brief version is introduced. Brief v07 continues for scan 035.

S SA01-K81-04's scan034 written forms are confirmed, while its proposed replacement indices are kept out of the diplomatic text. H explicitly identifies the diagram number in its note; the exact note-to-tag association is recorded and adds no collation row. H's extra comma after the second marginal inclusion is separately recorded. No OCR, external research, compilation or mathematical proof check was performed on this page.

During scan035's independent reading stage, the inventories already completed were ordered by their recorded vertical coordinates. Scans 028, 029, 030 and 033 required row permutations. The audit retains the exact original-to-final and inverse index maps and checks that every row field is unchanged; all page-text hashes stayed unchanged. An initial parser stopped at a position containing only a y-range. The prior row order was restored from the existing checkpoint, verified by exact row-multiset equality, and the revised script checked every coordinate and permutation before writing. This is a metadata-order operation, with no new reading or crop. The same coordinate-order check now runs before each page's apparatus is completed.

### Scan 035 — brief v07 retained for the next page

All three complete texts, detailed findings, inventories, notes and metadata were compared. The main reader inspected 23 local crops: all fifteen R1 crops, R2 03 and 11, R3 14, and five new crops for alors, heading emphasis, the two separate margin strokes and the unpunctuated intersection ending. The corresponding image views and their targets are recorded in decisions/scan035_main_observations.md. Failed output that supplied no image is not counted as a view. No locus was cropped twice by the same reader.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 035 | 15 | 15 | 15 | 5 | 50 | 23 (18 existing + 5 new) |

The root resolves the opening replacement separator, live Pi3, colon, semicolon, panachées, omega, older display numerals 7 and 8, et and injective. The compressed annotation keeps uncertainty in both its older and live index. The extra horizontal after its X, seen by R2, is retained with uncertainty over identity and state. Readers differed on the first reading of Soient/Soit, hypothèse/hypothese and the target subscript; the root records every candidate and follows the visible stroke evidence. Eleven C doubts are resolved and nine retained. Fourteen uncertainty macros remain, grouped into thirteen findings because the older and live annotation suffix occupy one locus.

The lower margin stroke is preserved separately from the upper one. R3's assessment that H's general emphasis note covered these marks is recorded in its raw return; the final comparison records that H names a single stroke while two separate complete strokes are visible. H's preamble expressly maps its emphasis macro to the author's own emphasis. That mapping is used when recording the heading's different emphasis scope. H's current label (17) agrees with the ink, and no earlier numeral is independently decipherable there; R2's proposed text difference from H's general rewriting note is rejected. These are applications of brief v07's existing exact-note and uncertainty rules, so v07 continues for scan036. No new convention is introduced.

The two main emphasis crops clip neighboring right-hand words, and the intersection-ending crop clips the preceding equals sign at the left; every target mark and its relevant endpoint is complete. No OCR, external research, compilation or mathematical proof check was performed.

### Scan 036 — brief v07 retained for the next page

All three complete texts and all detailed returns, findings, inventories, notes and metadata were compared. Every raw finding has an explicit source-ID correspondence in the final decision record: R1 34/34, R2 32/32 and R3 33/33. The root resolves hypothèse, envisagées, the live right Sigma in (****) and d’où, while retaining the other seventeen C doubts. The complete text and doubts record each contain twenty-four uncertainty loci.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 036 | 11 | 11 | 14 | 3 | 39 | 18 (15 existing + 3 new) |

The root viewed R1 crop 09; all eleven R2 crops; R3 crops 02, 06 and 09; and three new crops for A ce propos notons, the complete shared brace and pas l’un. The new targets are complete. Their borders clip adjacent context only. R3’s cropped contextual top line was not used as the complete evidence for A ce propos notons; a separate main crop contains that distinct target. R1’s crop 09 supplies the complete right-hand comma, including the endpoint that is beyond R3’s right bound. The original lower edge physically cuts the concluding sentence. No root whole-image or half-image view occurred.

The final reading keeps the two crossed a) relations with ne first and equality as an alternative. The root retains the b) arrow doubt with R2, the cancelled étant doubt with R3, the additional low 2’s state with R1/R2, and the possible older E’s state uncertainty with R3. The first raised reference is a short hooked horizontal; the root puts dash first with a retained, recording the readers’ a-first choices. The final colon/à uncertainty follows R3. H’s explicit notes and emphasis mapping were considered; the record distinguishes its acknowledged rewriting from the omitted older text.

S SA01-K81-05’s reported crossed form is confirmed with final-state uncertainty. Its proposed equalities are not substituted. The row’s no-scan provenance and the narrative’s missed crop are explicitly recorded. No mathematical repair or proof check is claimed. The reader differences concern local stroke confidence and state; the existing brief already addresses those matters and exact punctuation checking, including the comma reported only by R1. Therefore v07 continues for scan037. Boolean raw reader doubt flags are mapped exactly by true→yes and false→no for the final TSV.

No OCR, external research or compilation was performed.


### Scan 037 — brief v07 retained for the next page

All three complete texts and detailed returns, including every inventory, note, notation entry and workflow field, were compared. The final record maps all raw findings: R1 35/35, R2 40/40 and R3 42/42. Seven C doubts are resolved and fourteen retained. The complete text contains twenty-two uncertainty macros, matched by twenty-two unresolved entries.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 037 | 12 | 15 | 15 | 8 | 50 | 23 (15 existing + 8 new) |

The root viewed R1 07 and 12; R2 11 and 15; R3 01–07 and 11–14; and eight new crops. The new crops cover inverses/par, de =, ou inclusion inverse/on, the two panachées occurrences, i.e, les ensembles and the later high signs, the first lower list and the complete marginal rule. Root opened no whole page or half. The first attempted delivery of R3 01 yielded only an output-truncation message; its subsequent successful delivery is counted once. No crop was remade. The root used R1’s broad revision crop to include the complete targeted word bodies and line-end revision; adjacent contextual descender clipping is recorded in the reader returns. The bottom line lies close to the physical edge of the source image.

The root resolves the opening D’s cancellation with R3, keeps shared ans live, places the bare second cancelled Sigma term first with R2, retains the possible older upright with R1/R3, and puts 1 before 2 at the overwritten target index with R2. The compact high signs are compared at five actual occurrences. Their cap and downstem forms receive top first with plus retained at the first occurrence; the existing recurring-glyph convention governs the four subsequent occurrences. Clear crossed plus marks remain plus. No algebraic identification is inferred from these shapes.

The heading’s terminal-point doubt is resolved while R2’s roof-shaped accent becomes a separate retained uncertainty. R3’s Pi/R, strictement/Strictement and bottom Pi-index uncertainties are retained. R1’s two punctuation points after non and its two-segment marginal trace are retained. The full marginal crop confirms the gap and long extent. The definition twice writes panachées; H’s notes acknowledge the interlinear group and marginal mark, so their acknowledged state is not counted as an additional H difference. H’s added or is unmarked even though its following lit has an uncertainty macro; the final flag is local to the added word.

The differences concern local glyph/state confidence and graphical extent. The existing brief already directs readers to inspect these and to use exact witness strings, so no new brief version is introduced. Brief v07 continues for scan038. No S correction row names scan037. The sweep’s reported proof check is not recast as a check performed in this run. No OCR, outside research or compilation was performed.


### Scan 038 — brief v08 introduced for scan 039

All three complete texts and all detailed findings, inventory entries, notes and metadata were read. The final record maps R1 37/37, R2 35/35 and R3 38/38 findings. Seven C doubts are resolved and eleven retained. Seventeen uncertainty macros and one unreadable cancelled word correspond to eighteen unresolved entries.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 038 | 13 | 11 | 11 | 4 | 39 | 18 (14 existing + 4 new) |

Root inspected R1 04, 08, 13; R2 04; R3 01–04 and 06–11; and new crops for cette, opening panachées, the terminal point at the right edge of (24), and parenthetical panachée. Root viewed no whole image or half. The complete reader texts were saved before detailed returns. One combined text output was truncated; the missing R1 metadata tail and R2 inventory 1–10 were subsequently read in bounded outputs. R3’s whole detailed return was also read in bounded parts.

Two reader boxes did not reach the physical right edge at the possible terminal point. Root’s additional crop includes that edge and retains an uncertain point because a dark nub merges with the border. R1/R3’s word findings omitted C’s existing terminal period from their quotation; the final punctuation finding gives the exact C and H point. These recurring boundary and quotation problems lead to brief v08, first used on scan039: check full source-edge bounds and quote punctuation directly from the witness, keeping word and punctuation decisions separately identifiable.

Local disagreements remain explicit: colon/à after ens.; top/plus; ou/où; the cancelled diagram label’s 2/1; the short interlinear écrit/écrite/noté and indiciellement/individuellement; mut/mul; n/nu; the heading’s dot/acute accent; and the final singular/plural ending. The small t in pt is raised. The preliminary observation describing the adjacent une/un word as a leader is corrected in the final observation record. Both commas in the involution addition were already visible in the inspected crop and occur in all three complete texts. H’s notes acknowledging points, cancellation and the whole involution insertion are incorporated. No S row names scan038. No OCR, external research, compilation or independent mathematical proof check was performed.


### Cross-record traceability audit during scan039 reading

The completed scan027–035 records were checked against every raw reader finding. Eleven source-reference fields were extended to identify component findings already covered by the recorded crop decisions. Original and resulting metadata values, the exact inverse restoration rule, and unchanged hashes for every page and the combined text are in `validation/early_reader_traceability.json`. The known scan033 R3 final-period candidate remains explicitly rejected because C already contains the period. All raw findings are now mechanically accounted for. No transcription, ink decision, count of changes or crop was changed. The record validator now checks this coverage, consistency of C-doubt statuses, local crop references for changed loci and the unique fresh-reader registrations.


### Scan 040 and brief v10, first use scan 041

All three complete texts and every detailed return field were read. Each reader supplied 29 findings, all mapped into 30 final loci. The root resolves both lower comparisons as less-than-or-equal from their separate lower strokes, the bracket-final comma, the point after on and the semicolon after incomparables. The old article retains identity and cancellation uncertainty; the old word keeps notons first and noter as an alternative, explicitly recording R1’s reversed choice. The final falling stroke retains its uncertainty and receives no completed operand. Three C doubts are resolved and eleven retained; fifteen uncertainty loci remain.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 040 | 13 | 17 | 14 | 3 | 47 | 18 (15 existing + 3 new) |

The root viewed all thirteen R1 crops, R2 crops 05 and 06, and three new local crops for the complete statement required by S, the capital Si and the final reference. An earlier output containing no delivered images is excluded from these counts. All three noun crops clipped the q descender. The separately required S statement crop contains the whole descent. No settled locus was cropped again.

H explicitly identifies the written tot abbreviation despite expanding its main text. R1’s proposed expansion difference is declined; R2/R3’s mapping is adopted. Brief v10 makes this abbreviation-note mapping explicit and asks readers to trace long descenders across the next line before selecting the crop bounds. These refinements respond to actual page040 disagreements and crop limitations.

S SA01-K81-02’s quoted principal-set assertion is confirmed from the ink. A new exact certificate constructs six oriented cuts of the four-vertex tripod, computes the graph components after each cut, records the cut/subset map and its inverse, checks all written finite conditions and exhibits incomparable members of an upper and a lower principal set. The script and certificate preserve all pair comparisons and twelve intervals. This is a concrete refutation event; the larger 18,247-tree sweep and a general replacement theorem are not claimed as verified. The transcription remains governed by ink. No OCR, outside research or compilation was used.


### Scan 041 — brief v10 retained for the next page

All three complete texts and detailed returns were read. Each reader made one coherent title crop containing the long q and p descenders. The root viewed R1’s crop once; no additional crop was required. All three C doubts remain retained. The high downward-right stroke favors èquiv. first with R1/R3, while R2’s unaccented preference and R1’s additional èqui. alternative remain recorded. The first-word i and final extra e remain uncertain. H has no text, so this page adds no H collation row. The title-only sheet is assigned cover in the final inventory, with the raw text classifications preserved.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 041 | 1 | 1 | 1 | 0 | 3 | 1 |

The full-descender instruction worked on this coherent title crop. The remaining disagreement concerns a faint local stroke, and the existing brief already requires retaining that uncertainty. Brief v10 therefore continues for scan042. No OCR, external research, compilation or proof check was performed.


### Page-context extraction repair at the start of scan 042

The J81-06 doubt table uses a first field such as “42, opening”, whereas the earlier extractor required the scan number to be followed immediately by a column boundary. The main reader found this before deciding scan042. The extractor now accepts either the column boundary or a comma after the exact scan identifier. The repaired current-page context supplies 35 page042 rows to each of its three independent readers; C, H and the 25 C doubt IDs remain unchanged. Later unread packets were repaired deterministically with the same selector. No other-page reading or main decision was sent to a reader.

The check in validation/earlier_context_selector_check.json confirms that all relevant first-column rows for the fourteen completed pages were already in their packets; none was missing. The input-only repair and counts are preserved in validation/context_selection_repair.json and scripts/repair_context_selection.py. No completed page text was changed.


### Scan 042 — brief v10 retained

All three complete texts and every detailed return field were personally read. The final record maps all 49 R1, 48 R2 and 47 R3 findings into 53 loci. Seven C doubts are resolved and eighteen retained. The text contains 29 explicit uncertainty arguments, independently counted by a mechanical documentation helper that opened no images, witnesses or reader returns. That helper performed only an exact token/structural audit and did not serve as an additional reader. The source-to-final text edits have an exact forward and inverse reconstruction record.

| Scan | R1 crops | R2 crops | R3 crops | Main new crops | Total created | Main reader crops inspected |
| --- | --- | --- | --- | --- | --- | --- |
| 042 | 18 | 13 | 20 | 3 | 54 | 32 (29 existing + 3 new) |

Root viewed all R1 crops; R2 01, 02, 06, 10, 12, 13; R3 09, 14, 17, 18, 20; and new local crops for the isolated point after une, both NB abbreviation endings, and the gap before the second example. No whole page or half was opened by root. The R3 example crop did not contain that last target, and no decision about the gap is credited to it. The narrower R1 compound-word crop omitted the faint distant point; the R2 punctuation crop includes it. A failed image output and a truncated detailed-return output are excluded from actual-view/read counts; the missing material was subsequently delivered and read in bounded outputs.

The root preserves the first example colon and the later à, the live comma after the old membership expression, both union primes, the first live S-prime in the final paragraph, the two diagonal low marks, and the possible older capital. The intersection's parallel rules and curves retain their explicit emphasis/attachment uncertainty. The right i.e/i.e. abbreviation remains open despite the raw readers' resolution, and the marginal heading's independent underline is counted as an H difference. All other differing confidence judgments remain documented with the actual three readings. The existing brief covers these local uncertainties and crop-boundary checks, so v10 continues. No S correction row names this page. No OCR, external research, compilation or mathematical proof check was performed.
