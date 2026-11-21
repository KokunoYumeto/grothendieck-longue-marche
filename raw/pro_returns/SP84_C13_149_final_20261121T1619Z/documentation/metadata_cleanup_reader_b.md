# Metadata cleanup — reader_b

Completed: 2026-11-21 15:15:31 UTC

## Scope and verification

Reviewed scans013–020 against their current pages and frozen final adjudications. Only notes, hand, notation, inventory and diff_coverage were edited. The report schema and assembly/audit script behavior were inspected first; no assembly, approval, adjudication or audit-completion script was run. No new readings or mathematical checks were made.

Applied 60 field edits. All 72 protected page/audit files retained their SHA-256 values, and every report field outside the five authorized fields is unchanged. No substantive page/adjudication contradiction was found.

## Exact edits

### 1. Scan 013: notes[4]

Before:

```text
The small centralizer sentence is a live interlinear insertion. The two larger lines beginning Si g and Gamma centralise are struck out. The reading order keeps those states separate. The small words overlap large cancelled subscripts, especially le; this is marked rather than supplied confidently.
```

After:

```text
The small centralizer sentence is a live interlinear insertion. The cores of the two larger lines beginning Si g and Gamma centralise are struck out; the cancellation status of their final relation/word and Gamma_Q tail remains explicitly uncertain after the independent audit. The reading order keeps those states separate. The small words overlap large cancelled subscripts, especially le; this is marked rather than supplied confidently.
```

Evidence: Current page; final adjudications b17–b19 distinguish the live insertion, cancelled old-line cores, and uncertain final tail. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 2. Scan 013: notes[6]

Before:

```text
The extra doubt on display label 14, the doubt on le, and the added doubt on the struck inclusion sign are certainty-only changes: they have no substantive changes rows of their own. C’s nested doubt on the cancelled E′⊂E is also retained.
```

After:

```text
The doubt on display label 14, the doubt on le, and the final tail’s relation/word and cancellation-scope doubts are certainty-only changes: they have no substantive changes rows of their own. C’s nested doubt on the cancelled E′⊂E is also retained.
```

Evidence: Current page; final adjudication b19 expands the former inclusion-only doubt to subset/de/et and uncertain cancellation scope. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 3. Scan 013: hand[3].consistency

Before:

```text
The two small centralizer lines are distinct from the ruled-out Si g and Gamma centralise baselines.
```

After:

```text
The two small centralizer lines are distinct from the cancelled cores of the Si g and Gamma centralise baselines. The final old-line tail has separately uncertain cancellation scope.
```

Evidence: Final adjudications b16–b19 and current page. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 4. Scan 013: diff_coverage[6].reason

Before:

```text
The raised sign is present though its ell reading stays doubtful.
```

After:

```text
The raised sign is present and remains doubtful between ell and t after the independent audit.
```

Evidence: Final adjudication b06 adopts the explicit ell|t alternatives. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 5. Scan 013: diff_coverage[23].reason

Before:

```text
The small insertion ends with plain Gamma and a stop; the larger struck Gamma_Q is on the following baseline.
```

After:

```text
The small insertion ends with plain Gamma and a point/comma doubt. The final indexed Gamma_Q belongs to the larger old baseline, whose tail has uncertain cancellation scope.
```

Evidence: Final adjudications b17 and b19; current page. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 6. Scan 013: diff_coverage[24].reason

Before:

```text
The large struck tail retains the inclusion-like sign under doubt and the indexed Gamma_Q.
```

After:

```text
The final old-line tail retains the relation/word alternatives subset/de/et and the indexed Gamma_Q, with cancellation versus live status also explicitly uncertain.
```

Evidence: Final adjudication b19; current page. Sources: pages/149_scan013.tex, second/149_scan013_adjudications.tsv.

### 7. Scan 014: notes[0]

Before:

```text
Run SP84_C13_149; reader GPT-6 Astra Pro, effort not exposed. The full image was inspected once for layout and each supplied half once. Every word and inline formula was read against the ink. Sixteen retained enlarged crops were personally inspected. No OCR, external research, TeX compilation, or mathematical check was performed.
```

After:

```text
Run SP84_C13_149; reader GPT-6 Astra Pro, effort not exposed. The full image was inspected once for layout and each supplied half once. Every word and inline formula was read against the ink. Sixteen retained enlarged crops were personally inspected. No OCR, external research, TeX compilation, or mathematical check was performed during this first visual reading. The later targeted main-reader proof check S014.check1 is recorded separately below.
```

Evidence: Existing notes[11] records S014.check1; this edit distinguishes the first reader’s activity from that later check without changing either claim. Sources: pages/149_scan014.tex, second/149_scan014_adjudications.tsv.

### 8. Scan 014: notes[9]

Before:

```text
All ten packet marks remain unresolved in the proposed text. The audit set covers their entire inline formula units, every insertion and marginal note, every different word, and all nine numeral locations including the Qbar-zero index. Numeric or already-settled boxes c09/c11/c16/c18 were not retained as first-pass images; they remain audit rectangles. Crop c05 is rotated 30 degrees clockwise, with its unrotated original-image coordinates recorded.
```

After:

```text
All ten original packet marks remain unresolved in the finalized text; the independent audit also retains the added réduite/réduit doubt. The audit set covers their entire inline formula units, every insertion and marginal note, every different word, and all nine numeral locations including the Qbar-zero index. Numeric or already-settled boxes c09/c11/c16/c18 were not retained as first-pass images; they remain audit rectangles. Crop c05 is rotated 30 degrees clockwise, with its unrotated original-image coordinates recorded.
```

Evidence: Current page and final adjudication b16; all original marked alternatives remain present. Sources: pages/149_scan014.tex, second/149_scan014_adjudications.tsv.

### 9. Scan 014: hand[4].misread

Before:

```text
No doubled alphabet is inferred solely from the looped first Gamma stem; its full formula remains available for independent review.
```

After:

```text
No doubled alphabet is inferred solely from the looped first Gamma stem; its complete formula was included in the independent audit.
```

Evidence: Final adjudication b02 records inspection of the complete equality; audit is completed. Sources: pages/149_scan014.tex, second/149_scan014_adjudications.tsv.

### 10. Scan 014: inventory[6].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page has margin{13}; final adjudication b20 explicitly retains marginal foliation rather than the author-page wrapper. Sources: pages/149_scan014.tex, second/149_scan014_adjudications.tsv.

### 11. Scan 015: notes[4]

Before:

```text
S015.3 (L15–L20): The Scholie revises sans torsion to à centre and discusses recovering the groupoid, or the associated topos wording as actually written, from the exterior group attached to E_{bar K/K}. It changes a cancelled phrase to défini à isom, while unique près remains ordinary main-line text. The page ends with Les hom.
```

After:

```text
S015.3 (L15–L20): The Scholie revises cancelled sans and the doubtful torsion/tors run to à centre and discusses recovering the groupoid, or the associated topos wording as actually written, from the exterior group attached to E_{bar K/K}. The replacement reads unsure defini/definie à isom without a supplied acute accent; unique près remains ordinary main-line text. The page ends with literal Les hom, without an abbreviation stop.
```

Evidence: Current page; final adjudications b14, b15 and b18 resolve sans and retain the replacement’s letters and accent uncertainty. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 12. Scan 015: notes[5]

Before:

```text
No mathematical check was performed by this reader. The parent is documenting its separate checks at final adjudication. Nothing in the present transcription is emended on mathematical grounds; checks is intentionally empty.
```

After:

```text
No mathematical check was performed by the first reader. The main reader’s separate checks S015.check1 and S015.check2 are documented below. Nothing in the transcription is emended on mathematical grounds.
```

Evidence: Existing notes[16] and notes[17] document the completed main-reader checks; removes the outdated prospective statement and empty-checks claim. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 13. Scan 015: notes[7]

Before:

```text
The tall l and low e-like continuation before centre are live. Additional crowded ink remains. The son hypothesis and even its overwritten/deleted state are not fully established, hence the whole local alternative rather than a claim that son has been read through the strike.
```

After:

```text
The tall l and low continuation before centre permit le or les. Additional crowded ink remains. The son hypothesis and its overwritten/deleted state are not fully established, hence the whole local alternative unsure deleted-son-plus-le / le / les rather than a claim that son has been read through the strike.
```

Evidence: Final adjudication b07 and current page explicitly retain le|les and correction-state uncertainty. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 14. Scan 015: notes[9]

Before:

```text
The cancelled sans, torsion/tors., and que l’on/question remain doubtful because not every internal letter is plain. In the torsion/tors. run, the dark terminal point may belong to an abbreviated ending; no fuller unmarked reading is asserted. Two small dots lower and to the right of that cancellation have no secure textual attachment and are not promoted to punctuation.
```

After:

```text
The cancelled sans is resolved by the independent audit. The cancelled torsion/tors run remains doubtful, with a separate colon/point alternative inside the cancellation. The longer cancelled phrase retains que l’on/question/équivalence alternatives. Two small dots farther lower-right of the torsion run have no secure textual attachment and are not promoted to punctuation.
```

Evidence: Final adjudications b14, b15 and b18; current page. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 15. Scan 015: hand[3].consistency

Before:

```text
Observed in sans, torsion/tors. and the phrase replaced by défini à isom. None is generalized to other words.
```

After:

```text
The torsion/tors run and the longer phrase replaced by doubtful defini/definie à isom remain partly obscured. The independent audit resolves cancelled sans from its surviving letter sequence; that result is not generalized to other words.
```

Evidence: Final adjudications b14, b15 and b18 distinguish resolved sans from unresolved cancellations and replacement. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 16. Scan 015: hand[3].misread

Before:

```text
H leaves the latter two as illegible. C’s proposed readings are retained only as explicit doubts because complete letter sequences do not survive plainly.
```

After:

```text
H leaves the latter two cancelled passages as illegible. The torsion/tors and que l’on/question/équivalence readings remain explicit alternatives because complete letter sequences do not survive plainly; the raised replacement also retains defini/definie without a supplied acute accent.
```

Evidence: Final adjudications b15 and b18. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 17. Scan 015: inventory[19].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page margin{14}; final adjudication b20 retains the separate foliation as a margin item. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 18. Scan 015: diff_coverage[3].reason

Before:

```text
The crowded ink around live le is not a securely readable literal question mark; the possible correction state is represented explicitly.
```

After:

```text
The crowded ink before centre is not a securely readable literal question mark; the independent audit retains le/les and possible overwritten-son correction-state uncertainty.
```

Evidence: Final adjudication b07. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 19. Scan 015: diff_coverage[4].reason

Before:

```text
Rather than choosing a bare son or bare le with certainty, the possible overwritten son and the live le are represented in a local state alternative.
```

After:

```text
The local alternatives retain possible overwritten son followed by le, or live le/les, without asserting the correction state or terminal s as certain.
```

Evidence: Final adjudication b07; current page. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 20. Scan 015: diff_coverage[9].reason

Before:

```text
H’s illegible cancelled run permits the uncertain torsion/tors. reading, but the ending remains unresolved.
```

After:

```text
H’s illegible cancelled run permits torsion or abbreviated tors, with colon/point punctuation separately uncertain inside the cancellation.
```

Evidence: Final adjudication b15; current page. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 21. Scan 015: diff_coverage[12].reason

Before:

```text
The cancelled phrase retains partial readable ink but neither que l’on nor question can be resolved fully.
```

After:

```text
The cancelled phrase retains partial readable ink but que l’on/question/équivalence remain unresolved alternatives; the raised replacement is separately doubtful defini/definie à isom without a supplied acute accent.
```

Evidence: Final adjudication b18; current page. Sources: pages/149_scan015.tex, second/149_scan015_adjudications.tsv.

### 22. Scan 016: notes[5]

Before:

```text
The left glyph in the final identification is now printed E-first with Gamma as an alternative. Its middle and lower strokes support E, while their lighter weight leaves an overtracing question. The resulting written identification is retained without replacing it by an expected mathematical letter or inventing a correction history.
```

After:

```text
Both capitals in the final identification remain uncertain: E-first with Gamma as an alternative on the left, and Gamma-first with E as an alternative on the indexed right. Lighter middle/lower traces beside the heavy roofs and stems leave overtracing unresolved. The written identification is retained without choosing expected mathematical letters or inventing a correction history.
```

Evidence: Final adjudication b17 and current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 23. Scan 016: notes[7]

Before:

```text
Agreed ink was checked as well, including donc (H doubts it), the initial prime/bar placements, the written singular du morphisme structural, the abbreviations hom and isom without supplied stops, and every extension index. The inline numeral 1 was settled from the half and receives audit coordinates without an extra crop.
```

After:

```text
Agreed ink was checked as well, including donc (H doubts it), the initial prime/bar placements, singular du morphisme, the abbreviations hom and isom without supplied stops, and every extension index. The vowel in structural/structurel remains uncertain after the independent audit. The inline numeral 1 was settled from the half and received audit coordinates without an extra crop.
```

Evidence: Final adjudication b10 qualifies the adjective while retaining singular morphisme; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 24. Scan 016: hand[2].habit

Before:

```text
The word ou can be reduced to a tiny rounded first mark and one low horizontal run.
```

After:

```text
A short connective can be reduced to a tiny curved first mark and one low horizontal run.
```

Evidence: Final adjudications b06 and b11 retain ou/en/on instead of a certain ou. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 25. Scan 016: hand[2].consistency

Before:

```text
Both occurrences before alternative groupoid maps agree; c04 and c09.
```

After:

```text
Both groups before alternative groupoid maps have this reduced shape; c04 and c09. Their ou/en/on alternatives remain explicit.
```

Evidence: Final adjudications b06 and b11; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 26. Scan 016: hand[4].consistency

Before:

```text
The overwritten word in c06 and the final capital in c14 have separable light/heavy strokes but uncertain layer order.
```

After:

```text
The overwritten word in c06 and both capitals of the final identification in c14 have separable light/heavy strokes but uncertain layer order.
```

Evidence: Final adjudications b08 and b17. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 27. Scan 016: hand[4].misread

Before:

```text
The final capital cannot safely be normalized to Gamma or assigned a confident E-to-Gamma correction sequence.
```

After:

```text
The final capitals cannot safely be normalized to a single certain alphabet or assigned a confident E-to-Gamma correction sequence.
```

Evidence: Final adjudication b17 retains separate E/Gamma alternatives on both sides. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 28. Scan 016: notation[4].written

Before:

```text
\unsure{E|\Gamma}=\Gamma_{\bar K/K}
```

After:

```text
\unsure{E|\Gamma}=\unsure{\Gamma|E}_{\bar K/K}
```

Evidence: Current page and final adjudication b17. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 29. Scan 016: notation[4].rendering

Before:

```text
\unsure{E|\Gamma}=\Gamma_{\bar K/K}
```

After:

```text
\unsure{E|\Gamma}=\unsure{\Gamma|E}_{\bar K/K}
```

Evidence: Current page and final adjudication b17. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 30. Scan 016: notation[4].meaning

Before:

```text
Written identification in the extension sentence; left glyph remains uncertain.
```

After:

```text
Written identification in the extension sentence; both the left glyph and the indexed right glyph remain uncertain.
```

Evidence: Final adjudication b17. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 31. Scan 016: notation[4].evidence

Before:

```text
c14: middle/lower rightward strokes favor E, but heavy roof/stem and lighter lateral strokes leave overtracing unresolved.
```

After:

```text
c14 and audit b17: middle/lower rightward traces beside heavy roofs and stems leave E/Gamma uncertainty on both sides; no correction sequence or deliberate doubled alphabet is established.
```

Evidence: Final adjudication b17. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 32. Scan 016: diff_coverage[5].reason

Before:

```text
The connective is ou, with no t stem.
```

After:

```text
The connective remains uncertain between ou, en and on; no t stem supports H’s et.
```

Evidence: Final adjudication b06; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 33. Scan 016: diff_coverage[8].reason

Before:

```text
The initial word of the line is sera, without the final t needed for est.
```

After:

```text
The initial short group remains uncertain between sera and dc.; its compressed middle and detached terminal point do not securely decide the reading.
```

Evidence: Final adjudication b09. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 34. Scan 016: diff_coverage[9].reason

Before:

```text
The source has singular du morphisme structural; du is in c07 and the two nouns/adjective forms are in c08.
```

After:

```text
The source retains singular du morphisme; the adjective’s final vowel remains uncertain between structural and structurel.
```

Evidence: Final adjudication b10; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 35. Scan 016: diff_coverage[10].reason

Before:

```text
The second connective is again ou.
```

After:

```text
The second connective retains the same ou/en/on uncertainty as the first.
```

Evidence: Final adjudication b11; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 36. Scan 016: diff_coverage[14].reason

Before:

```text
The a body and paired tall f stems support affiné.
```

After:

```text
The initial return and reduced ending leave affiné/différent unresolved; the two tall f strokes do not decide the entire word.
```

Evidence: Final adjudication b16; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 37. Scan 016: diff_coverage[15].reason

Before:

```text
E is now the first graphic reading, with Gamma retained because of possible overtracing.
```

After:

```text
E remains the first reading on the left with Gamma as an alternative; the indexed right glyph separately retains Gamma/E uncertainty because of its lighter middle/lower traces.
```

Evidence: Final adjudication b17; current page. Sources: pages/149_scan016.tex, second/149_scan016_adjudications.tsv.

### 38. Scan 017: notes[4]

Before:

```text
Four interlinear additions are separately retained: un, est, K after ext., and et Gamma=Gamma_{K-bar/K}. Their leaders were traced to their attachment points. In the last addition, sont des belongs to the main baseline. Its capital K subscript forms match the neighbouring pi equality; the source notation is not silently reconciled with the earlier Gamma_{Q-bar/k}. No mathematical consistency claim is made.
```

After:

```text
Four interlinear additions are separately retained: un, est, K after ext., and et Gamma=Gamma_{K-bar/K} with a doubtful raised can/unreadable cluster on the right Gamma. Their leaders were traced to their attachment points. In the last addition, sont des belongs to the main baseline. Its capital K subscript forms match the neighbouring pi equality; the source notation is not silently reconciled with the earlier Gamma_{Q-bar/k}. No mathematical consistency claim is made.
```

Evidence: Current page and final adjudication b11 add the previously omitted raised cluster while preserving the insertion attachment. Sources: pages/149_scan017.tex, second/149_scan017_adjudications.tsv.

### 39. Scan 017: notes[5]

Before:

```text
All three listed C marks were examined: M1006 resolves to est, M1007 to met, and M1008 remains a dash/arrow doubt. Three further C doubts inside cancellations, absent from marks.tsv, were also cropped: ain remains tentative, compatible remains tentative, and S K-bar is resolved from the two visible glyphs and the overbar. No expansion to Spec is supplied in that cancelled fragment.
```

After:

```text
All three listed C marks were examined: M1006 resolves to est, M1007 to met, and M1008 remains a dash/arrow doubt. Three further C doubts inside cancellations, absent from marks.tsv, were also cropped: the first now retains ain/un/une alternatives, the second compatible/correspond alternatives, and S K-bar is resolved from the two visible glyphs and the overbar. No expansion to Spec is supplied in that cancelled fragment.
```

Evidence: Final adjudications b02, b06 and b07; current page. Sources: pages/149_scan017.tex, second/149_scan017_adjudications.tsv.

### 40. Scan 017: notes[6]

Before:

```text
The final map shaft retains a limited terminal-shape doubt. Its complete formula is in the audit boxes. The two unresolved cancelled prose readings are retained in place; compatible does not amount to a confident rejection of every letter of H’s compte tenu.
```

After:

```text
The final map shaft retains a limited terminal-shape doubt. Its complete formula is in the audit boxes. The two unresolved cancelled prose runs retain ain/un/une and compatible/correspond alternatives in place; compatible is not asserted as a certain recovery of the obscured word.
```

Evidence: Final adjudications b02, b06 and b12; current page. Sources: pages/149_scan017.tex, second/149_scan017_adjudications.tsv.

### 41. Scan 017: inventory[11].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page margin{16}; final adjudication b13 distinguishes thin foliation from the author’s 8. Sources: pages/149_scan017.tex, second/149_scan017_adjudications.tsv.

### 42. Scan 018: inventory[5].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page margin{17}; final adjudication b06 explicitly retains the marginal foliation wrapper. Sources: pages/149_scan018.tex, second/149_scan018_adjudications.tsv.

### 43. Scan 019: notes[3]

Before:

```text
S019.2 — A sixth description is written vertically in the left margin. It names the groupoid and the Galoisian topos after tensoring K with Q-bar, with the indicated Gamma action; its parenthesis explicitly says pas néc. connexe. The full note has five rows when rotated clockwise.
```

After:

```text
S019.2 — A sixth description is written vertically in the left margin. It names the abbreviated gr.-oïde/gr.-oïdes and the topos quotient after tensoring K with Q-bar, with the indicated Gamma action; its parenthesis explicitly says pas néc. connexe. The full note has five rows when rotated clockwise.
```

Evidence: Current page; final adjudication b20 adopts quotient, not galoisien, and preserves the abbreviated noun alternatives. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 44. Scan 019: notes[4]

Before:

```text
S019.3 — The relation in the last main paragraph is preserved as pi_K unsure{neq|=} pi_1(K). Its lower hooked ink does not form a clean upper-bar crossing. No mathematical expectation was used to turn that stroke into an unequivocal equality or inequality.
```

After:

```text
S019.3 — The relation in the last main paragraph is preserved as pi_K unsure{neq|=|simeq} pi_1(K). Its additional curved ink does not cleanly cross the upper bar, and the slight wave also permits the similarity-sign alternative. No mathematical expectation was used to choose among these readings.
```

Evidence: Final adjudication b19; current page. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 45. Scan 019: notes[5]

Before:

```text
The literal de le clôture is clear and has not been grammatically repaired. The opening word before extension has uncertain cancellation state; the raised K attaches after extension. The source also has the short forms pts, rev., pro-gr, hom, ss-, alg. and néc.; they are not expanded in the transcription.
```

After:

```text
The literal article sequence de le is retained without grammatical repair; the following clôture/cloture accent remains uncertain. The opening word before extension retains une/d’une/des alternatives and uncertain cancellation state; the raised K attaches after extension. The source also has the short forms pts, rev., pro-gr, hom, ss-, alg. and néc.; they are not expanded in the transcription.
```

Evidence: Final adjudications b02 and b17; current page. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 46. Scan 019: notes[8]

Before:

```text
The only prelisted mark M1010 remains undecided. The C-only doubtful crossed comme was separately cropped and remains tentative because the cancellation masks its middle. Other localized doubts are the opening word state, the old numeral under 3, fixée/fixe, the tiny si, and the pi relation. No formula was completed from mathematical context.
```

After:

```text
The only prelisted mark M1010 remains undecided. The C-only doubtful crossed comme now retains comme/connexe/connexes alternatives. Other localized doubts include the opening word and its cancellation state, ce/en, the compressed au-dessus/dash-disons/dash-dessus phrase, the old numeral under 3, item-4 punctuation and map endpoint, fixée/fixe, the tiny si, clôture/cloture, the three-way pi relation, and the marginal abbreviation, accent and punctuation. No formula was completed from mathematical context.
```

Evidence: Current page and final adjudications b02, b06, b08, b12, b14, b16–b20 and b22. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 47. Scan 019: hand[1].consistency

Before:

```text
Clear in L16 and the par le groupe replacement in L18; the short crowded overtrace on une is a limiting case and is not asserted certain.
```

After:

```text
Clear in L16 and the par le groupe replacement in L18; the short crowded overtrace on the opening une/d’une/des group is a limiting case, with both word reading and cancellation state left uncertain.
```

Evidence: Final adjudication b02; current page. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 48. Scan 019: notation[5].rendering

Before:

```text
\unsure{\neq|=}
```

After:

```text
\unsure{\neq|=|\simeq}
```

Evidence: Final adjudication b19; current page. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 49. Scan 019: notation[5].evidence

Before:

```text
c14: the additional ink attaches at/below the lower bar without a clean crossing of the upper bar.
```

After:

```text
c14 and audit b19: additional curved ink attaches at/below the lower bar without a clean crossing of the upper bar; the slight wave also permits simeq, so all three relation alternatives remain.
```

Evidence: Final adjudication b19. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 50. Scan 019: inventory[2].first_words_or_objects

Before:

```text
\unsure{\deleted{une}|une}
```

After:

```text
\unsure{\deleted{\unsure{une|d'une|des}}|\unsure{une|d'une|des}}
```

Evidence: Current page; final adjudication b02. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 51. Scan 019: inventory[19].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page margin{18}; final adjudication b21 distinguishes thin foliation from author number 9. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 52. Scan 019: diff_coverage[2].reason

Before:

```text
The opening word state remains locally doubtful; the raised K is placed after extension from the ink, not before it.
```

After:

```text
The opening word retains une/d’une/des alternatives with cancellation state also doubtful; the raised K is placed after extension from the ink, not before it.
```

Evidence: Final adjudication b02; current page. Sources: pages/149_scan019.tex, second/149_scan019_adjudications.tsv.

### 53. Scan 020: notes[0]

Before:

```text
Scan020 is a handwritten continuation sheet with no visible author’s page number, title or date. Small thin foliation 19 appears at the lower left and is assigned to another or uncertain hand. There are two prose blocks, six interlinear additions, two cancellations and one slanted marginal note; no diagram or drawing is present.
```

After:

```text
Scan020 is a handwritten continuation sheet with no visible author’s page number, title or date. Small thin foliation 19 appears at the lower left and is assigned to another or uncertain hand. There are two prose blocks, six interlinear addition groups (the Gamma equality/inclusion group has two raised pieces around baseline Gamma_K), two cancellations and one slanted marginal note; no diagram or drawing is present.
```

Evidence: Final adjudication b09 and current page split the former whole-expression insertion around the baseline term while retaining the same physical interline. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 54. Scan 020: notes[7]

Before:

```text
The accent in réconstituer, both opening underlines, the source forms hom and isom without stops, all six additions, both cancellations, and the thin foliation are preserved. The six listed C marks are resolved, as is the additional C doubt inside the cancelled formula. The new K-map uncertainty does not alter C’s first reading of its shaft.
```

After:

```text
The accent in réconstituer, both opening underlines, the source forms hom and isom without stops, all six addition groups, including the two raised pieces around baseline Gamma_K, both cancellations, and the thin foliation are preserved. The six listed C marks are resolved, as is the additional C doubt inside the cancelled formula. The new K-map uncertainty does not alter C’s first reading of its shaft.
```

Evidence: Final adjudication b09; current page. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 55. Scan 020: notation[3].meaning

Before:

```text
The added group equality/inclusion preceding sur.
```

After:

```text
Group equality/inclusion formed by two raised additions around baseline Gamma_K, before sur.
```

Evidence: Final adjudication b09; current page. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 56. Scan 020: inventory[2].first_words_or_objects

Before:

```text
un sous-groupe ouvert $\Gamma$ (non précisé d'avance) de
```

After:

```text
un sous-groupe ouvert $\Gamma$ (\unsure{non-précisé|non précisé} d'avance) de
```

Evidence: Current page; final adjudication b03 retains hyphen/space uncertainty. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 57. Scan 020: inventory[4].first_words_or_objects

Before:

```text
on suppose pour simplifier que c'est le $=$ $k\subset\overline{\mathbb Q}$\ldots
```

After:

```text
\unsure{on|en} suppose pour simplifier que c'est relatif \unsure{au} $=$ $k\subset\overline{\mathbb Q}$\ldots
```

Evidence: Current page; final adjudication b05 replaces the former c’est le reading and retains on/en plus au uncertainties. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 58. Scan 020: inventory[8].position

Before:

```text
Above main paragraph line 9, before baseline sur
```

After:

```text
Main paragraph line 9, two raised pieces around baseline Gamma_K: Gamma= above left and subset Gamma_K-prime above right, before baseline sur
```

Evidence: Final adjudication b09; current page. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 59. Scan 020: inventory[8].first_words_or_objects

Before:

```text
\inserted{$\Gamma=$}$\Gamma_K$\inserted{$\subset\Gamma_{K\prime}$}
```

After:

```text
\inserted{$\Gamma=$}$\Gamma_K$\inserted{$\subset\Gamma_{K'}$}
```

Evidence: Current page and final adjudication b09; synchronizes the exact split insertion and apostrophe-prime spelling. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.

### 60. Scan 020: inventory[11].kind

Before:

```text
text
```

After:

```text
margin note
```

Evidence: Current page margin{19}; final adjudication b17 identifies marginal foliation. Sources: pages/149_scan020.tex, second/149_scan020_adjudications.tsv.
