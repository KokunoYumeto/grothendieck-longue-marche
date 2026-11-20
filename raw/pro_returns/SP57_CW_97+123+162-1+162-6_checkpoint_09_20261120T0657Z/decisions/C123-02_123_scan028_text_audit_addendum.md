# C123-02_123_scan028 — spec/preview text-only addendum

## Files and scope

Audited the generated decision spec, preview and notes against all three previously read reader returns and the initial text audit:

- out/decisions/C123-02_123_scan028_spec.json
- out/decisions/C123-02_123_scan028_preview.tex
- out/decisions/C123-02_123_scan028_notes.md

This addendum records the version checked after root repaired the D05 excerpt and supplied ROOT-01/ROOT-02 bounding boxes. Root also regenerated the files to distinguish the H advice quote from the omitted refusal, record the et pour endpoint choice, localize the upper-subdivision and pale-cancellation doubts, and add the conditional ex.ct abbreviation.

No images were opened or created. No reader, spec, preview or notes file was modified. The finalizer script was read to understand inheritance and metadata assembly; it was not executed.

## Outcome

The preview contains the full chosen prose and all graphic components selected by root. The principal reader disagreements are explicitly represented in the decision rows, including the extra comma-space decision. The C/H change flags are consistent with the chosen readings and the separation of H's synopsis from its selected quotations.

Checks actually performed:

- The sole edit.old exactly matched R1's complete reading.tex.
- edit.new exactly matched the complete preview.
- The spec notes field exactly matched the notes file.
- The merged in-memory difference set contained 63 rows.
- The preview and every final excerpt had zero final brace depth and no negative brace prefix after the D05 repair.
- All begin/end environments matched.
- No empty unsure, deleted, inserted, handwritten, margin, figure or mbox wrapper was found.
- Every difference had nonempty final content and an existing evidence-crop file.
- Every difference had bbox and bbox_source after the ROOT-01/ROOT-02 repair.

These are text and structural checks, not compilation or rendered-layout verification.

## Remaining actionable metadata/excerpt issues

### 1. Upper subdivision trace is locally doubtful but absent from remaining_doubts

The regenerated preview now puts the light upper slant in a nonempty unsure drawing. D53.final and the full-footnote final excerpt inherit the repaired drawing. However, remaining_doubts still contains only the numeral count and closing-parenthesis alternatives for this area.

Add a distinct row for the upper trace's uncertain origin/function, or extend the subdivision row explicitly. The inventory groups the upper trace with the definite heavy lower overrun and labels their hand simply as unnamed handwriting; qualify the upper member if the retained doubt includes ink-versus-surface origin. The lower heavy stroke need not acquire the upper trace's doubt.

### 2. D19.final retains the pre-merge plain second star

D19.final still begins with the ordinary parenthesized functor pair, with a plain second superscript star. The preview and the dedicated R2-D21 row instead contain the adopted broken lower-right ray and detached lower-left point.

The wording of the live second qui clause is correct, and the graphic is not missing from the preview. To make this final excerpt faithfully reflect the chosen text, either use the actual pair-and-clause slice or restrict D19.final to the live underlined qui clause. There is no reason to alter D19's C/H flags for this repair.

### 3. Three inventory positions conflict with the adopted reader loci

These are conflicts between reported whole-image coordinates, not new ink observations:

| Inventory element | Spec position at audit | Existing reader position for the adopted feature | Problem |
|---|---|---|---|
| Pale upright above opening second u | [1295,214,1306,235] | R2 [1342,224,1351,244] | Disjoint horizontal intervals, although the spec says it adopts R2's feature. |
| Detached point at star after image inverse | [1133,732,1152,760] | R2 [1170,727,1177,737]; R3 [1171,728,1178,735] | Spec box is left of the mutually agreeing reader point boxes. |
| Interrupted second star in functor pair | [399,786,424,825] | R2 point [385,800,394,813], separate ray [391,797,401,815] | Spec box excludes the detached point it claims to inventory. |

Reconcile these with the already observed locus metadata. No new crop is requested. The footnote direct-image point box also overlaps only part of R2's smaller reported point box; it can be aligned during the same metadata correction if root has not intentionally revised that location.

### 4. Optional inventory precision

The Exactness insertion inventory row still uses unmarked “est exact à gauche i.e.” as its identifying words, whereas the final choice is ex with point/a uncertainty and point first. This is an identifying label rather than a missing transcription, but updating it to the actual localized form prevents an isolated inventory extract from looking more certain than the text.

The cancelled body-reference medium has a small remaining reader qualification: R1/R3 inventory it as pen, while R2's inventory says printed/pen reference under cancellation. D08 currently records the numerical disagreement only. If root's observed decision settles its medium, one short qualification in D08.readers can record that; it does not create an additional C/H correction from a missing wrapper.

## Graphic coverage confirmed in saved preview

Every selected graphic has actual TeX/TikZ content, not only report prose:

| Area | Actual saved components |
|---|---|
| Opening | One separate doubtful pale upright at the second u; doubtful final point after the handwritten reference. |
| Adjunction reference | Genuine baseline que node, raised reference and its curved leader. |
| Body footnote marker | Definite raised star, parentheses and two separately drawn doubtful lower prongs. |
| Exactness insertion | Genuine baseline commute node, point/a-localized text, main curved leader and separate doubtful high point. |
| Image-inverse statement | Baseline c'est phrase with raised On peut addition and leader; literal superscript star with detached point. |
| Functor pair | Literal second star with separate lower ray and detached lower-left point. |
| Sigma insertion | Baseline cancelled qui / blank-cell x / cancelled peut, definite raised Sigma, principal leader and separate doubtful faint arc. |
| ROOT-03 | A genuine application baseline node and exactly two light diagonal draw paths, both enclosed in the nonempty local ink/surface doubt. |
| et pour | Genuine tout baseline node, raised words and the selected returning right hook. |
| Object phrase | Source opening/closing quotation strokes and underlined ordinary E with prime. |
| Parenthetical E | Definite ordinary E and separate prime node, plus the doubtful lower horizontal and upturned-right material. |
| inverse cancellation | Horizontal strike with rising right terminal and separate initial upright. |
| l'expliciter | Genuine se baseline node, raised typed insertion, definite first e plus its separate doubtful diagonal, and insertion leader. |
| After pour | Exactly three separate low points. |
| Example cancellations | Two additional blank-cell x impressions, supplementing the earlier x between qui and peut. |
| Footnote separator | One long wavy drawn rule. |
| Footnote marker | Literal star with detached lower-left point. |
| Footnote reference | Actual vérifier que baseline node, raised reference and three draw paths: separated pale left return, pale middle path, joined dark right upturn. |
| Footnote functors | Both selected literal star drawings and their detached lower-right points. |
| U insertion | Genuine limites baseline node, raised underlined U-, pale lower leader segment and joined darker rise; second inline underlined U retained. |
| Final D'ailleurs | Doubtful word and comma, plus separate doubtful lower-right tail. |
| Final subdivision | All selected count/closure alternatives, separately doubtful upper slant and definite heavier lower overrun. |
| Page cancellation | Anchored upper path, two individual points, short intervening segment, continuing lower dark path and locally doubtful pale lower continuation. |

The regenerated footnote leader has three draw paths but two connected components: the middle and dark right paths share an endpoint. This matches the R2 topology root selected. It is not the three mutually separated stretches of R3. The current evidence wording distinguishes an interrupted leader from one continuously visible stroke and is compatible with the actual paths.

## Reader-disagreement coverage

The spec records the chosen first page-number candidate, the resolved old section digit, retained old opening digit doubt, narrowed marginal/body references, localized exactness uncertainty, the extra opening marks, body star prongs, high exactness point, individual star fragments, et pour endpoint, heavy-E alternatives, shaped inverse cancellation, expliciter trace, three low points, On peut certainty, footnote comma spacing, ce certainty, two-tone U leader, final comma doubt, final count/closure alternatives, two final traces, and combined page-cancellation geometry.

R3's empty-strut leader implementation and late marginal-reference attachment were not carried into the preview. The full text uses real baseline word nodes and places the margin reference beside inductives. The old R1 D31 truncated final excerpt has been replaced by a complete E/prime picture.

The original audit's R3-only report omissions of the object quotation strokes and footnote opening marker do not propagate: base D27 and the complete D41, plus R2-D43, cover those features. The second underlined U remains covered in D49. All C questions remain covered through the R1-based c_doubts list.

## C/H flags and excerpt interpretation

- D10 correctly changes c_changed to true for the narrower exactness form with point first.
- D07 remains a C change for narrowing/localizing its alternatives and placing the margin correctly.
- D32 now has drawing-or-diagram kind, c_changed=true and an explicit synopsis caveat; it no longer presents H's summary use of inverse as a literal live reading of the cancelled locus.
- D31 correctly gives no H reading for the parenthetical heavy E; the E in H's object phrase is not assigned to that locus.
- D33 now distinguishes H's quoted reader advice from the omitted formal refusal.
- D53 has c_changed=true for the expanded closure alternatives and added graphics.
- ROOT-01, ROOT-02 and ROOT-03 correctly mark omissions/changes against both witnesses.
- All marked-in-H values remain “no”; H has no explicit ill/uncertain marker at these loci.
- Broad prose-omission rows retain c_changed=false while separately identified local changes have their own true flags. This is a coherent locus convention; the mere presence of a separately counted graphic within a broad final excerpt does not require duplicating its C change in the broad row.

Most final values are literal preview slices. The nonliteral values that remain are explainable: D05 has self-contained deletion wrappers added for excerpt integrity; D13 states the local state in words; D20 juxtaposes the two underline spans; D24/D35 differ only in whitespace; ROOT-01 omits the outer handwriting wrapper. D19's unupdated star is the one remaining substantive excerpt mismatch identified above.

The notes accurately distinguish the three readers' reported mathematical checks: R1 gives a targeted Hom calculation, R2 rechecks typing/preservation direction, and R3 checks typing/variance only. The notes' additional root proof claims refer to root's separate mathematics record; this text audit did not re-prove them.

## Handoff

The actionable items above were sent to root before this addendum was saved. No finalization operation was performed. The remaining repairs concern metadata and one apparatus excerpt; no missing selected graphic or body/footnote passage was found in the preview.

### Closed after root's reported repairs

Root subsequently reported that D19 was restricted to the live qui clause, the upper final trace was added to remaining_doubts, and the conflicting inventory positions were corrected from existing reader evidence. Root finalized the page with 63 loci, 95 inventory entries and 20 remaining doubts, with its structural checks passing. These closure facts are reported by root; no further verification or next-page inspection was performed by this auditor.
