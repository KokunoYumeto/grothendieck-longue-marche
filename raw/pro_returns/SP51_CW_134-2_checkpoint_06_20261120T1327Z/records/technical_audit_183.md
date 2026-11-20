# Scan183 technical audit

## Scope and result

This is a text-only consistency audit of the completed scan183 records. It does not supply another manuscript reading or reconsider the main reader's ink decisions. The three complete `report.json` files and `reading.tex` files, the final page, `decision.json`, `main_viewed_crops.txt`, `main_display_failures.json`, `audit_183_disposition.md`, and the supplied scan183 C/H/question packet were read. The saved A/C crop manifests, the three main-crop JSON sidecars, and relevant scan183 brief rules were also checked as metadata. No image was opened, displayed, interpreted or recropped; no OCR, PDF extraction, internet research, TeX engine, compilation or rendering was used.

The final reading and its seventeen uncertainty wrappers agree with the recorded substantive decisions. The audit found two H classification labels that require a metadata disposition. No final transcription change follows from either finding.

## Findings requiring disposition

The difference numbers below are one-based positions in `decision.json`'s `differences` array; the objects themselves do not have IDs.

| Finding | Difference | Current field | Concrete inconsistency |
|---|---|---|---|
| F1 | D04, L4 modules ending | `kind: other` | H reads `modules`; the final preferred reading is `module` in `module\|modules`. This changes the preferred word, rather than only adding doubt to H's same preferred reading. The scan183 brief reserves `other` for uncertainty-only changes and requires H classifications. A and B classify this same H change as `misread word`. C's original `other` classification was consistent with C's own unchanged preferred `modules`, but the consolidated preferred reading has changed. |
| F2 | D22, L14 donnant/donnait | `kind: misread word` | H already reads `\uncertain{donnant}` and the final reads resolved `donnant`. Against H, this is solely a resolution of uncertainty; the brief assigns such changes `other`. The word change from `donnait` belongs to the C comparison, not the H kind. The final `differs_C: true`, `differs_H: true` and `marked_in_H: yes` flags remain consistent. |

These labels exchange one `other` and one `misread word` membership. Correcting both would leave the numeric H category totals unchanged. A's D23 and B's B183-D20 also use `misread word` for their resolution of H's doubtful `donnant`; those original reader classifications are source-report inconsistencies, not grounds to alter their readings. No shared record was edited during this audit.

## Final reading and uncertainty correspondence

The final page has seventeen `\unsure` occurrences, matching the seventeen consolidated unresolved entries. Their argument contents and preferred-order lists are:

| Site | Final uncertainty | Correspondence |
|---|---|---|
| L4 coefficient ending | `constant\|constants` | Decision and unresolved list agree. |
| L4 module ending | `module\|modules` | A/B preference selected; C-reader preference explicitly rejected. |
| L5 argument separator | `;\|,` | Preferred semicolon; the comma alternative retains the documented detached upper point, whose role is open. The comments and unresolved entry explain that distinction. |
| L5 article | `le\|la` | A/C order selected against B. |
| L6 live word | `foncteur\|foncteurs` | All reports and final agree on retained number doubt. |
| L6 cancelled abbreviation | `ab\|ab.` | Retained inside deletion. |
| L6 cancelled word | `foncteur\|foncteurs` | Retained inside deletion. |
| L6a replacement | `cohomologique\|cohomologiques` | Retained inside insertion. |
| L7 article | `le\|la` | A/C uncertainty selected against B's resolved `la`. |
| L7 overwritten fragment | `struc` | One-reading doubt retained inside deletion. |
| L10 ending | `formee\|forme\|formée\|form-` | C's preferred `formee` plus A's `forme`; `formés` is explicitly rejected in the consolidated evidence. |
| L13 old fragment | `m\|sou\|de` | Exact final order agrees with the unresolved list; reader alternatives are quoted correctly. |
| L22 first parenthetical word | `sans\|sa\|san` | A/B doubt retained against C's resolution. |
| L22 noun | `structures\|structure` | A/C doubt retained against B's resolution. |
| L22 adjective | `supplémentaires\|supplémentaire` | A/C doubt retained against B's resolution. |
| L23 word | `sur` | Inner wrapper qualifies only the word. The following `$X$` is outside it. |
| L23 insertion state | `\inserted{\unsure{sur} $X$}` | Outer wrapper records state doubt, as explicitly stated in the page comments, D34, unresolved list and notes. It is not a new doubt about the shape of X. |

Resolved `donc`, `triangulé`, `donnant`, and `dessus` occur without uncertainty wrappers, as required by the final decisions. The L21 code contains a partial-n overlay, `\uline{on abé}`, an unwrapped `l` followed by its partial-letter overlay, and `\uline{ien}`. This matches the deliberate first-n start and partial-l resumption recorded in the disposition. The old whole-word underline approximation is not present in the final page.

Static text checks found balanced braces, twenty paired dollar delimiters, and nine matching `tikzpicture` begin/end pairs. The final has one scan marker, one author-page marker, five insertion wrappers, three deletion wrappers, and two `\uline` spans. These are structural checks only; no typeset geometry was assessed.

## Every reader disagreement

The fifteen `reader_comparisons` entries accurately describe the returns, including the corrected B old-fragment order. Their final dispositions are reflected in the final page or the associated difference evidence.

| Place | Reader difference | Recorded final disposition |
|---|---|---|
| L4 module | A/B `module\|modules`; C `modules\|module` | A/B preferred order. |
| L5 separator | A comma plus detached point; B plain comma; C semicolon/comma uncertainty | C's punctuation preference, with both physical components and the alternative role explicitly retained. |
| L5 article | A/C `le\|la`; B `la\|le` | A/C order. |
| L7 article | A/C uncertain `le\|la`; B resolved `la` | A/C doubt and order. |
| L10 ending | A `forme\|formée\|formés\|form-`; B `form-\|formée\|formés`; C `formee\|formée\|form-` | `formee\|forme\|formée\|form-`; rejection of `formés` has a stated disposition. |
| L12 ending | A retained `triangulé\|triangulée`; B/C resolved `triangulé` | Resolved `triangulé`. |
| L13 old fragment | A `m\|sou\|de`; B `sou\|m\|de`; C `m\|de\|sou` | `m\|sou\|de`; B's actual order is now quoted correctly. |
| L14 verb | A/B resolved `donnant`; C `donnant\|donnait` | Resolved `donnant`. |
| L17/L23 isolated spots | A omits all three; B retains ils/permettent spots; C retains all three | All three are present and individually inventoried, with origin unassigned. |
| L21 underline | A continuous macro with segment comment; B split at whole-letter boundaries; C split with partial-l overlay | Split physical rule with partial-n and partial-l overlays. The additional partial-n refinement is explicitly traced to the existing disposition. |
| L22 sans | A `sans\|sa`; B `sans\|sa\|san`; C resolved `sans` | B's complete uncertainty list. |
| L22 structures | A/C uncertain; B resolved plural | A/C doubt retained. |
| L22 supplémentaires | A/C uncertain; B resolved plural | A/C doubt retained. |
| L23 sur X | A/C qualify phrase and state; B qualifies sur but leaves X and insertion clear | Word doubt and state doubt separated; X clear. |
| L6 grouping/H scope | A separates old phrase and replacement; B/C group the site | One final contiguous row, with all sub-doubts and H's limited uncertainty scope retained. |

The differing L17 stroke encodings also have a final disposition: A/B describe and draw a bent stroke, C's original code is straighter, and final D23 expressly records the bent, lobed shape and the final code includes the bends. This representational difference is handled in D23 even though it is not a separate `reader_comparisons` row. The small coordinate differences between readers remain labelled approximate; the final uses its selected coordinates consistently.

## All seventeen supplied C questions

Each reader has seventeen question-review entries. The first seventeen entries of the consolidated `doubt_review` cover the same seventeen supplied questions in order. The remaining twelve entries cover two earlier C note topics and ten H editorial-note topics.

| Question | Supplied topic | Final recorded disposition |
|---|---|---|
| Q1 | donc | Resolved. |
| Q2 | modules/module | Retained, preferred order changed to module first. |
| Q3 | constant/constants | Retained. |
| Q4 | cancelled ab/ab. | Retained. |
| Q5 | cancelled foncteur | Retained, plural alternative stated. |
| Q6 | overwritten struc | Retained as one-reading doubt. |
| Q7 | form-/formée/formés | Retained with `formee`, `forme`, `formée`, `form-`; `formés` expressly rejected. |
| Q8 | triangulé/triangulée | Resolved as triangulé. |
| Q9 | old de/sou/m | Retained as `m\|sou\|de`. |
| Q10 | sans/sa | Retained with san also included. |
| Q11 | structures/structure | Retained. |
| Q12 | dessus/disons | Resolved as dessus. |
| Q13 | raised sur X | Sur remains uncertain, X clear, insertion state separately uncertain. |
| Q14 | L1–L8 category number, coeff., equality, formula, formelles punctuation | Plural category phrase, abbreviation, unbracketed equality and final stop preserved; coefficient/module endings and H separator remain qualified. No editorial bracket or `?)` imported. |
| Q15 | two long additions, aux and only one X | Both complete additions and their separate destinations retained; aux preserved; no additional X supplied in the additions. |
| Q16 | L, R Hom, en effet, editorial footnote | Derived-letter forms and unruled Hom recorded; en effet is the complete short addition; no editorial footnote imported. |
| Q17 | final parenthesis, n-champs, loc. constants, sur X | Complete construction retained with the stated local doubts; no constructible-sheaf wording or final punctuation supplied. |

Both earlier C note topics are present: the on-page uncertainty about recovery of homotopy type, and the 183/38 number pairing. All H note topics are represented, including the two article sites, the overwritten L7 layer, raised replacement, addition guides, literal relatif, donnant, absent je, darker final wording, final phrase state, and excluded external editorial material.

## H flags and counts

There are thirty-five final difference rows: twenty-one differ from C and thirty-three differ from H. Only resolved donc and resolved dessus are C-only differences. Among the thirty-three H differences, four are marked in H and twenty-nine are unmarked.

| H-marked final row | Supplied H basis | Scope check |
|---|---|---|
| D06, L5 article | `\uncertain{la}` | Yes; the final changes the preferred article order. |
| D08, L6 correction | `\ill{}` and cancelled `\uncertain{foncteurs}` | Yes at the grouped site. `H_doubt_scope` explicitly excludes the unqualified raised `cohomologiques` ending. |
| D22, L14 verb | `\uncertain{donnant}` | Yes; final resolves H's doubt. F2 concerns only its kind label. |
| D34, L23 final phrase | `\struck{\ill{}}` and the illegibility note | Yes; content and state are changed together at one site. |

H's note about overloading structure does not express a reading doubt about the missing older fragment. D10 therefore correctly records an unmarked omission. Descriptions of raised placement and attachment guides likewise do not create extra H doubt flags. All kind strings are members of the required enumeration; F1 and F2 are the semantic classification exceptions identified above.

The current H-kind tally is thirteen `misread word`, eight `other`, one `misread symbol or index`, one `readable ink left as \ill{}`, nine `omission`, and one deletion-state row. The thirty-five rows do not duplicate the L6 sub-doubts as separate consolidated changes.

## Crop provenance and bounding boxes

All thirty-five final `bbox` fields exactly match the recorded rectangle for their selected `crop`. All thirty-one lines of `main_viewed_crops.txt` are unique, have matching crop metadata, and point to existing saved files. Every final difference crop and every unresolved-entry crop is in that manifest.

The manifest comprises five A crops, two B crops, twenty-one C crops and three new main crops: twenty-eight reused reader crops plus three new crops. Thirty unique crops are cited by the difference rows. The remaining viewed crop, `A/l14_rhom.png`, is explicitly used in the Q16/notation discussion and is not an orphan. Ten final rows preserve a different original reader rectangle under `reader_report_bbox`; those values are not substituted for the selected crop's actual `bbox`.

| Selected crop, relative to `result/crops/scan183/` | Recorded rectangle | Metadata match |
|---|---|---|
| A/l3_donc_categories.png | [620, 218, 1185, 315] | Exact |
| B/l04_constant_ending.png | [228, 320, 712, 414] | Exact |
| C/03_modules.png | [806, 331, 1187, 414] | Exact |
| C/04_H_formula.png | [218, 421, 460, 506] | Exact |
| C/05_la_structure.png | [1035, 431, 1450, 512] | Exact |
| C/06_foncteur.png | [216, 515, 501, 621] | Exact |
| A/l6_cancellation_replacement.png | [537, 499, 1124, 628] | Exact |
| C/08_struc_overwrite.png | [480, 633, 931, 715] | Exact |
| C/09_dash_point.png | [219, 737, 331, 822] | Exact |
| main/01_etc_stop.jpg | [1518, 626, 1672, 728] | Exact |
| main/02_paragraph_boundary.jpg | [205, 731, 797, 925] | Exact |
| A/l10_first_addition.png | [652, 910, 1584, 1017] | Exact |
| C/10_formee.png | [1427, 956, 1630, 1039] | Exact |
| A/l11_second_addition.png | [162, 1017, 699, 1139] | Exact |
| C/11_loc_constante.png | [877, 1064, 1354, 1147] | Exact |
| C/12_triangule.png | [913, 1174, 1301, 1275] | Exact |
| C/13_multiplicative_cancel.png | [551, 1269, 818, 1376] | Exact |
| C/14_tensor_point.png | [1119, 1255, 1215, 1392] | Exact |
| A/l14_rhom.png | [423, 1385, 830, 1491] | Exact |
| C/15_donnant.png | [851, 1399, 1137, 1484] | Exact |
| C/17_si_stroke.png | [202, 1750, 302, 1867] | Exact |
| C/18_ils_marks.png | [714, 1749, 933, 1840] | Exact |
| C/19_par_points.png | [890, 1870, 1002, 1985] | Exact |
| main/03_linearisation_quotes.jpg | [167, 2068, 635, 2177] | Exact |
| C/20_partant.png | [1220, 2081, 1481, 2180] | Exact |
| C/21_non_abelien_underline.png | [277, 2184, 709, 2285] | Exact |
| C/22_sans.png | [416, 2253, 587, 2320] | Exact |
| C/23_structures.png | [573, 2250, 814, 2318] | Exact |
| C/24_supplementaires.png | [811, 2250, 1192, 2324] | Exact |
| C/25_dessus.png | [1182, 2253, 1416, 2327] | Exact |
| B/l23_sur_x.png | [994, 2269, 1230, 2358] | Exact |

A's saved manifest is exactly equal to its thirty-one report crop objects, and C's saved manifest is exactly equal to its twenty-six report crop objects. B's twenty-six crop objects supply its metadata. All eighty-three reader crop paths are unique within their reader, exist, have internally consistent recorded scale/output-size arithmetic, and agree with the bbox of every associated reader difference that names a crop. This checks metadata, not image pixels or the historical fact of display.

`main_display_failures.json` lists one failed three-item output: C/18_ils_marks.png, C/19_par_points.png, and main/03_linearisation_quotes.jpg. Each path appears once in the successful thirty-one-path manifest. The failure record excludes the failed output from successful inspections and states subsequent successful displays of the same saved files without recropping. Its counts agree with `decision.json`: thirty-one successful unique inspections, twenty-eight reused crops, three new crops, one failed output and three failed image items.

## Inventory, hands and baseline accounting

Each reader has exactly L1–L23 and the five addition entries L6a, L10a, L11a, L18a and L23a. No main baseline or addition label is missing. Their crop counts are A=31, B=26 and C=26; their reported total successful source-plus-crop inspections are respectively 34, 29 and 29. These totals include one whole, one top-half and one bottom-half inspection per reader.

The final inventory has nineteen entries: three text entries, five insertions, three deletions and eight drawings. The text entries are the main prose, author page number 38, and archive number 183. The insertion and deletion counts match the page's five `\inserted` and three `\deleted` occurrences. The final L23 phrase remains a preferred insertion with an explicit alternative state, rather than an undocumented fourth deletion.

Eleven inventory entries are assigned to the author's hand, seven detached-mark sites have unassigned hand/origin, and the archive number has its separate archive-pencil designation. The seven detached sites contain eight point/stroke components because the contre site has two points. The eighth drawing inventory entry is the interrupted authorial underline. The final's nine figure wrappers comprise the seven detached sites plus the two partial-letter underline overlays; they do not represent nine separate incidental-mark sites. The H-separator upper point belongs to the preferred punctuation representation and is separately discussed as a role uncertainty, not counted twice as an eighth detached site.

The page number is consistently 38 in the supplied C marker, H note, final marker and final inventory; the archive 183 remains a comment and separate-hand inventory entry. The packet's `their_page: 182` is not substituted for either of those numbers. The single continuous prose-block decision, lack of an independent display or diagram, and unfinished final `pour tout n` agree across the final notes and reading.

## Note and check-event scope

All three reader `check_events` arrays are empty, and their reports explicitly distinguish visual notation reading from mathematical verification. The consolidated record has four events, all typed `carried as background without fault found`: S183-notes plus S183-N1, S183-N2 and S183-N3. None is labelled a proof, computation or independent verification. Their outcomes expressly state that source assertions are being recorded without independent proof.

The three `note_statements` IDs match the three scoped N1–N3 event IDs. N1 covers the initial cohomological data, N2 the derived-category candidate and the author's explicit lack of certainty about recovering homotopy type, and N3 the ensuing confidence in the nonabelian proposal. Those scopes agree with the corresponding notes and final text. The umbrella S183-notes event does not claim an additional mathematical check. External editorial material and other-page quotations are treated as review topics, not imported into the final transcription or presented as independently verified facts.

Only this audit file was written. Shared readings, reports, decisions, pages, scripts and aggregates were left unchanged.
