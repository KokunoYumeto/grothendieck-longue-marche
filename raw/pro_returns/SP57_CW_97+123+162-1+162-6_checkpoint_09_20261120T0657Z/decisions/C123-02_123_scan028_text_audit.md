# C123-02_123_scan028 — text-only audit

## Scope and status

Read all three complete reading.tex files and all fields of all three report.json files, packet C.tex, H.tex, C_questions.md, and reader_v11.md. No image was opened or created, no research was performed, and no reader file was changed. This is an audit of the submitted text and apparatus, not a fourth ink reading.

References below use R1/R2/R3 for the corresponding reader directory. Dnn is the exact difference identifier, except R2 identifiers have the prefix R2-. Line numbers refer to the saved reading.tex at audit time.

The complete prose has no additional lexical disagreement beyond the registered uncertain cells, the opening final point, and the footnote comma-space boundary. A supplementary comparison removed drawings, insertions, state wrappers and whitespace and compared first-candidate body/footnote strings: the only residual character differences were R3's final opening point and R2's preferred final subdivision iii rather than ii. This comparison is only a text coverage check; it neither resolves alternatives nor tests layout.

## Highest-priority additional findings

1. **Footnote comma-space:** R3 intentionally reads “,pour un foncteur”, against C/R1/R2 “, pour un foncteur”. This is not a serialization accident: R3 D45 explicitly reports no full blank typewriter cell, with crop 17_footnote_reference.jpg and bbox [978,1880,1080,1919]. R3 reading line 82 preserves it. Root has subsequently confirmed the no-space choice on its existing wide-footnote crop.
2. **Extra trace on expliciter:** R2 D36 alone records and draws a short upper-left diagonal on the first e of l'expliciter. The e remains definite. Reading lines 76–82; crop 20_expliciter_insertion.png; reported bbox [1180,1455,1593,1541], with the inventory's smaller mark box [1235,1467,1260,1497]. R1/R3 have neither a drawing nor a report entry for that trace.
3. **Shape of inverse cancellation:** R2 D33 alone draws both the horizontal strike with a rising right terminal and a separate upright at the first i (reading 68–72; crop 19_inverse_cancellation.png; bbox [1400,1267,1580,1344]). R1 D32 and R3 D29 themselves describe a rising right terminal, but their reading.tex has only the generic deleted wrapper. Their described terminal has no separate drawing.
4. **Left-margin placement:** R1/R2 attach the margin macro beside inductives (R1 17–19, R2 22–24). R3 retains it after the complete body at line 67, as C did, although R3 D37/inventory locate the note at approximately y580. A generic margin call there does not itself preserve the reported source-height relation. Root should use the R1/R2 attachment.
5. **Footnote reference leader topology:** R1 draws a single uninterrupted path. R2 draws three paths, with a gap between paths 1 and 2 but a joined endpoint between paths 2 and 3. R3 draws three mutually separated stretches, with a short middle stretch. “Three draw calls” and “three disconnected stretches” are different claims; retain the root's chosen geometry explicitly.
6. **R3 baseline-anchor implementation:** G02/G03/G04/G06/G07/G09/G13 put only an empty strut in the baseline node and append the intended baseline word after the nonzero-width picture. Thus the leader's local origin is not actually attached to que, commute, c'est, qui peut, tout, se or limites in the way the report describes. R1/R2 use genuine baseline word nodes. R3 G12 is an exception: vérifier que really is in its baseline node. Root has indicated it will use R1's nodes.

## Complete reader/reader disagreement register

Differences of harmless scale, identifier names, equivalent math wrappers and drawing syntax are excluded. “Absent” below means absent from that reader's saved text and report; it does not assert that the source lacks the mark.

| Locus | R1 | R2 | R3 | Audit consequence |
|---|---|---|---|---|
| Top page number | First candidates 2/7, then definite 2 | Same | First candidates 7/2, then definite 2 | Same candidate set, different preference; already known. |
| Old first digit of section number | Definite cancelled 2, D04 | Cancelled 2/3, D05 | Definite cancelled 2, D05 | Substantive uncertainty difference; opening-reference old digit remains 2/3 in all three. |
| Final point after opening reference | Absent | Absent | Doubtful point, D04; line 14 | Additional punctuation/trace; already known. |
| Pale high trace at opening second u | Absent | Separate doubtful trace, D03; lines 10–14 | Absent | Additional graphic; already known. |
| Cancelled marginal reference terminal | 2.11 or 4.11 only, D07 | Adds 4.1, D08 | Adds 4.1, D37 | R1 eliminates the single-final-1 candidate. |
| Marginal-reference uncertainty scope | Whole reference inside unsure | Whole reference inside unsure | I and parentheses outside unsure; only number uncertain | R3's c_changed=false does not register this localization; see apparatus issues. |
| Marginal-reference attachment | Beside inductives | Beside inductives | After entire body | Placement mismatch discussed above. |
| Cancelled body-reference terminal | (2.11) or (I 2.11), D08 | Also (2.1), D09 | Also (2.1), D08 | R1 eliminates the single-final-1 candidate. |
| Body footnote marker after inductives | Definite star plus two doubtful lower prongs, D09 | Plain raised star in parentheses | Plain raised star in parentheses | Two additional strokes only in R1. |
| Inserted exact | Whole exact doubtful, D10 | ex with a/point doubt, then ct definite, D11 | Same localized a/point doubt, D09 | Candidate point/possible ex.ct and doubt-scope difference. |
| Detached point above exactness leader | One doubtful point, D12 | Absent | Absent | Additional point only in R1. |
| Star after image inverse | Plain star | Literal star strokes and definite detached lower-right point, D20 | Definite star plus separately doubtful point, D18/G05 | Presence differs from R1; R2/R3 differ in local uncertainty treatment/function. |
| Second star of functor pair | Plain star | Detached lower-left point and interrupted lower-right ray, D21 | Plain star | Two explicit graphic components only in R2. |
| et pour leader right endpoint | Explicit returning/upturned hook | Explicit returning hook | Ends in a rising segment without the short returning hook | Candidate endpoint-shape difference, subordinate to root's observed geometry; no wording disagreement. |
| Heavy E after topos | Definite E/prime; uncertain lower bar and rising right material; extra E impression or pen work | Definite E/prime; uncertain filled lower rectangle; underline or displaced E | Definite E/prime; uncertain broad curved lower retouch and right upturn; repeated E, pen or low rule | All reject unqualified double striking; retained shapes and named alternatives differ. |
| Cancellation of inverse | Generic deletion; report mentions right upturn | Explicit horizontal/right upturn plus separate initial upright, D33 | Generic deletion; report mentions right upturn | New substantive graphic discrepancy and report-to-text gap. |
| First e of l'expliciter | Plain e | Definite e plus doubtful upper-left diagonal, D36 | Plain e | New extra trace; keep distinct from insertion leader. |
| Three points below pour | Three doubtful-function points, D35 | Absent | Three doubtful-function points, D32/G10 | Three components absent from R2. |
| Footnote opening star | Plain star | Literal star with detached lower-left point, D43 | Plain star | Additional component only in R2. |
| Cancelled On peut | Fully legible | Fully legible | Only eu locally doubtful, D41 | Already known. |
| Leader under (1.5 et 1.8) | One uninterrupted path, D45 | Three paths; first gap then joined middle/right, D45 | Three disconnected stretches, D44/G12 | Topology differs, not just path count. |
| Comma before pour | Comma-space | Comma-space | Comma immediately followed by pour, D45 | Newly confirmed text disagreement; root selected no space. |
| Footnote direct-image star | Plain star | Detached lower-right point, D47 | Plain star | Additional component only in R2. |
| Footnote inverse-image star | Plain star | Detached lower-right point, D48 | Plain star | Additional component only in R2. |
| Corrected ce foncteur | Cancelled d plus definite pen c | Same | Cancelled d plus pen c/d doubt, D46 | Already known. |
| First U insertion leader | Single uniform path | Joined pale lower segment and darker upper segment, D50 | Single uniform path | Tone/segment distinction only in R2; all keep U's underline separate. |
| Comma after final cancelled D'ailleurs | Doubtful comma, D51 | Undoubted comma | Undoubted comma, explicitly defended in D49 | Already known. All three separately draw the lower-right faint tail. |
| Final subdivision | ii/iii/i, all with closing parenthesis | iii/ii/i plus all three alternatives without final close, D54 | ii/iii/i, all with closing parenthesis | Candidate ordering and closing-parenthesis visibility differ. |
| Extra traces at final subdivision | Absent | Absent | Separate light upper trace plus heavy lower overrun, D52–D53/G15 | Two graphic components only in R3. |
| Page-wide cancellation | Upper path, two detached points, short segment, continuing lower path | Long path plus connected pale low continuation; continuation's ink/surface status open | Single continuous path | Known component/topology disagreement. R3 puts this in a standalone pre-body figure rather than an overlay attached to the prose. |

All three retain the same three standalone cancellation x impressions: one between qui and peut, one after ou, and one after de. R3 includes these x nodes inside the phrase's deletion wrapper; R1/R2 put them between separately wrapped words. This is not an additional underlying-text disagreement: each report identifies all three as cancellation marks in otherwise blank cells.

All three preserve the faint arc below Sigma, the distinct lower-right tail at final D'ailleurs, both U underlines, all four emphatic body underlines, the footnote separator, the locally live comma after the first cancelled qui, the truncated exac, the cancelled assurant/de/inverse/qui peut/ou de bimodule, and the explicit formal-justification refusal. No additional missing prose passage was found among readers.

## Report-to-text and apparatus discrepancies

### Definite or directly checkable

- **R1/R3 inverse endpoint:** R1 D32 and R3 D29 describe a heavy strike rising at its right end; R1 reading line 68 and R3 line 55 give only the deletion wrapper. R2 supplies the explicit shape. This is the clearest additional described-but-not-drawn mark.
- **R3 leader anchors:** The empty-strut issue affects G02, G03, G04, G06, G07, G09 and G13. Their source words are present, so this is not a lexical omission. It is a failure to encode the claimed geometric relation.
- **R3 page-wide stroke:** G01 reproduces a curve in source-like coordinates, but it is a standalone figure before the text, without overlay/remember-picture anchors. The deletion wrappers preserve cancellation state; the saved drawing does not itself cross the typescript. Root's R1-based approach avoids this.
- **R3 margin attachment:** D37 says c_changed=false despite retaining C's late call and describing the correct high source position. Its inventory's coordinates do not relocate the actual macro.
- **R3 localized marginal doubt:** D37 and c_doubts explicitly narrow the doubt to numerical content, but c_changed remains false. Under reader_v11's rule that substantive uncertainty changes are apparatus loci, flag this localization if root retains it; do not confuse it with the separate terminal-1/11 question.
- **R2 page-wide continuation:** The pale lower path is drawn, but the local doubt is an empty “unsure{}” node placed at its endpoint (reading 134), rather than a doubt enclosing the uncertain trace. The report and comment retain ink-versus-surface uncertainty. Ensure root's saved text gives that doubt actual content.
- **R3 final upper trace:** D52 and remaining_doubts leave its identity/origin uncertain, but the upper stroke in reading 94 is not locally wrapped in doubt. Only the subdivision text is doubtful in G15. The heavy lower overrun is separately drawn and can remain definite if root so decides.
- **R1 D31 report excerpt:** Its reading field stops at the inner reinforcement drawing and omits the subsequent prime node and final outer-picture close. The complete reading.tex lines 59–67 does contain them. This is a truncated report excerpt, not a missing prime in the transcription.
- **R2 D14 broad reading field:** It repeats C's whole-word “unsure{exact}”, whereas the actual reading and dedicated D11 choose localized ex[a/point]ct. The dedicated row is the precise decision. Analogously, broad prose-omission rows sometimes repeat cancellation phrases without the separately reported blank-cell x drawings; do not use those broad excerpts to overwrite the complete transcription.

### Candidate omissions in reader apparatus, while text remains present

- **R3 actual object quotation strokes:** No specific difference row identifies omission from H of the source opening strokes before objet and closing strokes after Sigma. They are in reading 50, in notation, and the opening strokes are inventoried. Broad D24 includes the whole passage, so this is absorbed coverage rather than a missing transcription. R1 D27 and R2 D29 make the specific source-quotation difference explicit.
- **R3 opening footnote marker:** The marker “(*)” is in reading 74 and the inventory but lacks its own H-omission difference. D40 starts at pour, after the marker and opening revisions. R1 D41 includes it in the complete-footnote omission; R2 D43 explicitly covers the marker graphic.
- **R3 second U omission:** The second underlined U is in the text and inventory and within broad D40. R1 D49 and R2 D51 give it a separate H-omission row. Treat this as broad rather than absent coverage.
- **R2/R3 des ensembles déduits question:** Both retain the exact words, and their structure-prose difference rows include them. Unlike R1, neither supplies a dedicated c_doubts response to C_questions' explicit “not a slip” note.
- **R2/R3 prior-C page-number question:** Both fully handle it in D01, remaining_doubts and notes, although not as a separate c_doubts row. R1 includes such a row.
- **R2 possible ex.ct abbreviation:** R2 puts the candidate in the transcription, differences and remaining_doubts but its abbreviations list has only resp. and i.e. R3 adds an explicitly conditional ex.ct expansion. If the point candidate survives in root, record the possible abbreviation as conditional, not as an established expansion.

No report has an empty difference.reading field. The only empty local doubt found in the complete texts is R2's cancellation-continuation marker discussed above.

## H coverage: synopsis versus selected quotations

H lines 2–14 explicitly provide an editorial synopsis and say only additions of words are being selected. H lines 16–30 then supply four additions plus quoted contexts and a short footnote note. Missing literal source wording is a real coverage difference, but the synopsis must not be treated as a claimed diplomatic reading of every word or cancellation state.

| Source portion or H assertion | Coverage in H | Reader report coverage and audit treatment |
|---|---|---|
| Opening uniqueness continuation | Not transcribed; final (3.2.1) mentioned separately | R1 D02–D03, R2 D02/D04, R3 D02–D03. Preserve the entire continuation, including both functors, resp., quotation and old digit. |
| First exactness exposition | H 4–6 summarizes preservation and conclusion | R1 D05, R2 D06/D14, R3 D06. Omission is full wording, adjunction justification, named functors/directions and explicit condition, not absence of the mathematical topic. |
| (I 2.11) | Mentioned in H's correction list | All three separately cover the missing leader. The cancelled marginal/body references are other loci; H's live-reference mention does not cover them. |
| est exact à gauche i.e. | Direct selected addition | All three preserve added doubt or narrower candidate; all separately reject H's explicit claim that it replaces the still-live commute phrase. This is a genuine state disagreement with H. |
| Underlined est/exact and cancelled exac | Summary gives est exact without source emphasis/revision | R1 D14–D15, R2 D14–D15, R3 D12/D17 cover. |
| On peut donc dire que and following quoted context | Direct addition and quotation | All cover the leader, old C, first qui deletion, second qui omission and underlining. H explicitly says donc is cancelled; no new omission should be invented for that cancellation. |
| Structure-definition prose | H 6–9 summarizes species and image statement | R1 D22/D29/D33, R2 D23/D26/D30/D32, R3 D24. All retain data of arrows, base/derived sets, repeated operations, the internal-exactness parenthesis and (II 4.1). |
| et pour and object phrase | Direct addition and quoted target in H 24–25 | All cover the leader and underlined object E. Source double quotation strokes are not represented by H's editorial guillemets; R1/R2 state that specifically. |
| Heavy E after topos | H omits the entire local parenthesis | R1 D31 correctly leaves H empty. R2 D31 and R3 D28 quote H's E' from the object phrase, conflating two source loci. For the heavy E, H is an omission, not a reading of that local E as plain. |
| Cancelled inverse in son image inverse par | H synopsis says l'image inverse par u* | R1 D32 labels this a deletion-state error, but H is paraphrasing in the synopsis. Prefer omitted local cancellation state/paraphrase. R2 D32 correctly quotes the synopsis as compressed coverage; R3 D29 records omission of the deleted source word. |
| Formal refusal and reader advice | H omits the refusal but directly quotes “nous conseillons au lecteur de se convaincre de sa validité” in 28–29 | R1 D33's empty H field is too broad if read as total absence of this whole span. R2 D34 quotes the surviving H advice; R3 D30 says excerpts remain. Distinguish omitted refusal from retained advice. |
| l'expliciter et de | Direct selected addition | All cover leader; R2 alone adds the e trace. No source word omission. |
| Examples | H lists six surviving nouns only | R1 D36–D37, R2 D37–D38, R3 D30/D33–D35. Restore full prepositions/bases, singular celle, cancelled phrase and its two blank-cell marks. |
| Final body parenthesis through se définis | Absent | R1 D38, R2 D39, R3 D36. All retain the open/cut form. |
| Complete footnote criterion | Absent apart from selected corrections | R1 D41 plus details, R2 D42–D54, R3 D40–D53. Includes both directions, corrected initial, adjoint alternatives, si et seulement si, both U qualifiers and cut-edge open parenthesis. R3's marker-specific apparatus omission noted above. |
| Footnote vérifier | H explicitly says vérifier is cancelled | All resolve vérifier que and note missing que; do not state H omits the fact of vérifier's cancellation. |
| (1.5 et 1.8) | Mentioned in correction list | All preserve the reference and separately report missing leader. |
| First U- | H explicitly prints script U and includes it among ink corrections | All give ordinary underlined typed U, with its separate pen leader. This is a localized alphabet/medium difference; the second U is absent from H's literal coverage. |
| Final cancelled sentence | H quotes c'est une conséquence immédiate de 1.2 and explicitly marks it cancelled | All preserve that agreed cancelled wording. The omissions are preceding doubtful D'ailleurs, trailing subdivision, relevant punctuation/graphic details; do not count the quoted clause as wholly absent. |
| Separator and long cancellation | Separator absent; long cancellation explicitly mentioned | All cover separator. For the long stroke, missing graphic geometry is the difference, not failure to mention cancellation. |

H's remarks concerning Kostant, reuse, and the possible correcting hand are editorial commentary. They are not source prose to insert, nor automatic “text not on the page” errors. All readers refrain from identifying the hand. H's broad blue-ink description should not create additional named-word medium errors solely because its marginal macro lacks the readers' wrappers; the U discrepancy is explicitly localized.

R1's several broad H-empty rows acknowledge in their evidence that H summarizes the subject. They should be described as missing literal passage coverage, not as proof that H lacks every included concept. This applies especially to D05, D22, and the advice portion of D33. The exact H field should use the relevant actual synopsis or quotation wherever it helps disambiguate the claim.

## C_questions.md coverage

| C question / prior note | R1 | R2 | R3 | Result |
|---|---|---|---|---|
| Old digit in final opening reference | c_doubts row 1 | row 1 | row 1 | All retain 2/3; live 3 definite. |
| Old digit in section number | row 2 | row 2 | row 2 | Covered; R1/R3 resolve 2, R2 retains 2/3. |
| Left cancelled marginal reference | row 3 | row 3 | row 3 | Covered; terminal candidates and doubt scopes differ. |
| Cancelled body reference | row 4 | row 4 | row 4 | Covered; R1 narrows terminal candidates. |
| Small exact insertion | row 5 | row 5 | row 5 | Covered; whole-word versus middle-cell doubt. |
| Cancelled vérifier que | row 6 | row 6 | row 6 | All resolve words while retaining cancellation. |
| Final D'ailleurs and subdivision | rows 7–8 | rows 7–8 | rows 7–8 | Covered; uncertainty and trace details differ. |
| ).Comme run-together boundary | row 9 | row 9 | row 9 | All retain no space. |
| est muni | row 10 | row 10 | row 10, grouped | All retain no added e. |
| telles que celle de | row 11 | row 11 | row 10, grouped | All retain singular celle. |
| des ensembles déduits, correctly formed | explicit row 12 | retained in text and D26, no explicit c_doubts row | retained in text and D24, no explicit c_doubts row | Content covered; minor report-response omissions in R2/R3. |
| Final se définis | row 13 | row 12 | row 11 | All preserve visible fragment only. |
| No visible close after droite | row 14 | row 13 | row 12 | All preserve open visible form. |
| Prior note: refusal of formal justification; advice insertion; vérifier que is not a surviving instruction | notes 4–5 | notes 4–5 | notes 5–6 | Fully covered in each; no invented proof obligation. |
| Prior own-page-number 22, revised section, no date/title/total | row 15 plus notes | D01 and notes | D01 and notes | Covered, with shared 22/72 doubt and differing preference. |

## Handoff

At the time of handoff, root reported that its existing crops had resolved the no-space “,pour” boundary and that it would build an R1-based spec using genuine baseline nodes, R2's additional graphics and segmented footnote leader, and R3's final-subdivision traces. This audit does not independently endorse any ink decision. The remaining implementation/apparatus fixes are the inverse-terminal coverage, correct margin attachment, explicit doubt content, accurate leader topology, H-locus distinctions, and the small report-only omissions listed above.
