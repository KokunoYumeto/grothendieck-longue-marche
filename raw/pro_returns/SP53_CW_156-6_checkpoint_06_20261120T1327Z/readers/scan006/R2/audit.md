# Independent reading audit — scan 006, R2

## Scope and inputs

Read the assigned packet only: brief.md, inputs.json, C.tex, H.tex, C_context.md, S.json and notation.md. Read the exact referenced preamble at /workspace/scratch/42e661864e98/out/PREAMBLE.tex. S.json is empty. The current notation table has no adjudicated glyphs.

No other reader, other manuscript page, published transcription, external research, OCR, text-recognition library or PDF extraction was consulted. A general reminder from the parent about distinguishing retouching from cancellation supplied no additional reading. All writes are confined to this R2 output directory.

The first recorded UTC timestamp, before image review, is 2026-11-20T08:58:41Z. Initial packet reading preceded that timestamp.

## Emitted image sequence

Every image below was actually emitted through image((await tools.view_image({path:...})).image_url). No whole image, half or crop was emitted a second time.

1. 08:58:44 UTC — whole page, J156-6-01_156-6_scan006.jpg: layout, header, all text blocks, displays, corrections and margins.
2. 08:58:53 UTC — half a, J156-6-01_156-6_scan006_a.jpg: read line by line.
3. 09:00:03 UTC — half b, J156-6-01_156-6_scan006_b.jpg: read line by line.
4. 09:02:51 UTC — crops 01, 02 and 03, each once, in that order.
5. 09:03:34 UTC — crops 04, 05 and 06, each once, in that order.
6. 09:04:45 UTC — crops 07, 08 and 09, each once, in that order.
7. 09:06:09 UTC — crops 10, 11 and 12, each once, in that order.

**Actual crops: 12. Total emitted images: 15.** The crop timestamps are the clock output at the beginning of each three-image call; all three emissions completed within the same sub-second call.

## What remained open after the halves

The remaining regions were: (1) the last token of the top cancelled fragment; (2) the cancelled predication under est appelé; (3) the doubled F at the end of the opening definition; (4) the accent in fidèlement; (5) the slanted inserted sentence above Utilisant; (6) the contracted replacement of d'autre part; (7) the first P's alphabet; (8) the paired domain F forms and cancelled arrow starts in (1.9); (9) the dense letter in multomb; (10) the mark after l'être; (11) the cancelled sentence start and inserted On; and (12) the adjacent de/barred-abbreviation/pour region.

The following doubts or disagreements were already settled by the half views and were **not** cropped again: cancellation of toute; cancelled On before C'est; insertion attachment before the comma after M; the y in déployement; the single upper barb in the Fig arrow; trouve; the stacked inverse-image layout and lack of H's terminal commas; la seconde. Their tight coordinates are supplied in report.json. Recurring P copies were not separately enlarged after the first-glyph decision.

## Crops and transforms

All boxes are Pillow [left, upper, right, lower] coordinates in the named original half, not in the enlarged output. Original halves are 1683 × 1260 (a) and 1683 × 1261 (b). Every crop used Pillow crop, ImageOps.autocontrast(cutoff=0.5), UnsharpMask(radius=1, percent=120, threshold=3), and final LANCZOS enlargement. Crop 05 alone was first rotated −3° with BICUBIC resampling, expand=True and white fill to straighten its slanted baseline. No crop was made from an already enlarged image. No re-cropping, re-viewing or whole-half enlargement was performed.

| No. | Original source and box | Rotation and final size | Output file | Purpose and observed result |
|---|---|---|---|---|
| 01 | half a; [260, 60, 745, 160] | 0°; 3000 × 619 px | 01_struck_opening_fragment.png | Opening cancelled fragment: final a versus de, and whole deleted text. Final token a, without an accent; not de. |
| 02 | half a; [1370, 60, 1668, 225] | 0°; 3000 × 1661 px | 02_inserted_predication.png | Inserted est appelé and underlying cancelled word after Multomb(F). Inserted est appelé is clear. Cancelled de|la remains open, with de first. |
| 03 | half a; [847, 334, 1097, 436] | 0°; 2800 × 1142 px | 03_doubled_F.png | Doubled vertical and top strokes of F after M-multiombre. Distinct doubled stems/bars support literal mathbb F. |
| 04 | half a; [571, 493, 845, 581] | 0°; 3000 × 964 px | 04_fidelement_accent.png | Accent direction and spelling of inserted fidèlement. Short grave accent supports fidèlement. |
| 05 | half a; [368, 644, 1610, 796] | -3°; 3300 × 576 px | 05_inserted_jusqua_sentence.png | Jusqu'à présent versus Jusqu'ici puisque and sentence punctuation/insertion connector. Jusqu'à présent; the lower sweep/right curl is an insertion connector, not textual parentheses. |
| 06 | half a; [882, 714, 1177, 815] | 0°; 3000 × 1027 px | 06_maintenant_contraction.png | Contracted insertion above deleted d'autre part. Compressed maintent|maintnt|maintenant retained. |
| 07 | half a; [570, 1135, 817, 1257] | 0°; 2800 × 1383 px | 07_P_alphabet.png | Calligraphic, script, or fraktur P at first occurrence. Capital P clear; exact calligraphic/script alphabet remains open. |
| 08 | half b; [545, 373, 777, 565] | 0°; 3000 × 2483 px | 08_eq19_F_and_cancelled_hooks.png | Paired domain F glyphs and cancelled left ends of the arrows in (1.9). Old rounded hooks are cancelled. Domain F font remains uncertain at first occurrence. |
| 09 | half b; [1295, 438, 1527, 522] | 0°; 3000 × 1086 px | 09_multomb_overwrite.png | Dense ink inside multomb: possible textual overwrite omitted by both drafts. Read multomb. The dense t is retouched; no separate cancelled text is recoverable. |
| 10 | half b; [1060, 747, 1191, 831] | 0°; 2600 × 1667 px | 10_terminal_cross.png | Small cross or asterisk after l'être. Literal four-armed cross; no corresponding note on the page. |
| 11 | half b; [1213, 714, 1588, 817] | 0°; 3200 × 879 px | 11_cancelled_sentence_start.png | Deleted words before appelle and the inserted On above them. Cancelled on ne rien; inserted capital On above. |
| 12 | half b; [263, 1102, 689, 1188] | 0°; 3200 × 646 px | 12_de_barred_m.png | Word de and barred abbreviation versus equality, including possible cancellation. Live de, barred m and pour. No independent cancelled de même. |

## Line-by-line comparison against both drafts

### Upper half

- **Header and top cancellation:** manuscript number 5 is inked at top centre. The separate cancelled fragment reads une figure a. H's final de is not supported; C's a is retained. No archive pencil number was identified.
- **Pour ... Multomb(F) ...:** Pour, figure F, the comma and Multomb(F) were checked. Toute is cancelled, contrary to H's live word. Est appelé is an insertion. The cancelled underlying token remains de|la; H's dans cannot be recovered.
- **Grande multiombre line:** both words have separate single underlines. The following de F, comma and ou la agree with the drafts.
- **M-multiombre line:** the hyphen is retained; the final F is visibly doubled. The full stop follows it. The next cancelled word is On, then the live C'est en continues into fait on the next line.
- **Fait une figure ensembliste dans ...:** the main text is continuous across M and the following et dont. There is an inserted indexing phrase anchored after M and before its comma.
- **Indexing insertion:** indexée, fidèlement, par tilde F, the parentheses and le déployement de F were checked. The grave accent is resolved by crop 04. The y in déployement is visible in the half; H's déploiement modernises it.
- **Et dont ... F:** et dont la connaissance implique celle de F and its full stop agree with both drafts.
- **Inserted scope sentence:** crop 05 supports Jusqu'à présent il n'était pas question de L. The sweeping enclosure is an insertion connector. H's Jusqu'ici, puisque and textual parentheses do not survive comparison.
- **Utilisant ... l'application:** Utilisant and l'application are live. D'autre part is cancelled. The word above remains the uncertain contraction maintent|maintnt|maintenant; no automatic expansion was made.
- **Inclusion display:** L hooked-right-arrow M, with its comma, agrees with both drafts.
- **Et les applications images inverses / correspondantes:** all words and absence of extra punctuation checked. The first inverse-image row begins at the bottom of the upper half.

### Lower half

- **Inverse-image display:** P(M) maps right to P(L); Fig(M) has a single upper-barbed arrow to Fig(L). The two rows are stacked. H's commas after them are absent. The P identity is clear, but its font family remains uncertain.
- **On trouve ...:** on trouve, en composant avec 1.6 a)b) is read as written. The final e and separate comma resolve C's trouvera alternative. The prior statement (1.6) was not consulted.
- **(1.9)a:** the label is to the left of a two-row brace; a), the domain F-family, the cancelled hook with live right arrow, P(L), and F maps to omb(F) are all included. Domain F's alphabet remains marked at its first occurrence.
- **(1.9)b:** b), the repeated domain, its cancelled hook, the live arrow to Fig(L), and F maps to multomb(F) are included. The final comma is retained. Crop 09 shows dense retouching of t, without a recoverable earlier letter or an independent strike-through; no deletion was fabricated.
- **Dont la première ...:** dont la première n'a aucune raison is continuous into d'être injective on the next line; its comma is retained.
- **La seconde ...:** the feminine article and final e support la seconde par contre, against H's le second.
- **A une tendance ...:** a une tendance à l'être is followed by a literal cross. Crop 10 resolves its shape, without assigning it an unseen note or replacing it by a period.
- **Cancelled new sentence and insertion:** crop 11 supports cancelled on ne rien, with a separately inserted capital On. H's On va omits the clear third word.
- **Appelle ...:** appelle omb(F) la petite ombre de F, with a single underline across petite ombre and a following comma, agrees apart from the preceding correction state.
- **Ou simplement ...:** ou simplement son ombre quand une, then confusion semble exclue, et, were checked word by word and left unchanged.
- **De barred m ...:** the crop resolves live de, a barred m and the separate word pour before multomb, followed by comma and la (petite). H's cancelled expanded de même is not recoverable; pour is omitted in H.
- **Final line:** multiombre de la is singly underlined, followed by figure F and a full stop. The parentheses around petite and its own single underline are retained.

Ordinary macro equivalents were not counted as differences: operatorname versus mathrm, uline versus H's emph for the same underline, and state-macro names. A hook recorded in H's explanatory note was not treated as missing merely because H did not encode it inline.

## Mathematical reading and checks

The page defines the grande/M-multiombre, describes its faithful indexing by tilde F, and then restricts along L into M to form the two small-shadow applications (1.9). The arrows' domains and targets parse consistently with the inverse-image construction. This was an internal direction/type check, not a verification of earlier definitions or a proof of injectivity.

The literal doubled F, one-barbed Fig arrow, and cancelled hooks are preserved. The later text gives only the qualified claim “dont la première n'a aucune raison d'être injective, la seconde par contre a une tendance à l'être”. The naming qualification “quand une confusion semble exclue” and retrospective check “Jusqu'à présent il n'était pas question de L.” are recorded. No independent proof of the recovery or injectivity assertions was attempted.

## Completion and limits

reading.tex is a complete diplomatic page using the supplied preamble's macros and standard LaTeX only. report.json records 23 substantive differences, all 12 distinct C doubts, an empty S-row list, 26 inventory entries, six actual check events and notation proposals. Nine C doubts are resolved and three retained. One additional recurring uncertainty concerns the domain F's alphabet. The duplicate doubt rows in C_context do not create extra loci.

The remaining uncertainties are explicitly marked in the page: the cancelled de|la, the contracted maintenant, the P alphabet, and the domain F alphabet. Heavy cancellation and the difference between handwriting and typeset alphabet names limit confidence. No formula or symbol was replaced by illegible, no gap was left, and no unobserved diagram, margin note or footnote was supplied.



Output verification: report.json parses as UTF-8 JSON; required fields and all referenced crop paths are present. The 15 view-log entries are unique, all 12 crops are 2400–3600 pixels wide, all 12 C loci are accounted for, and reading.tex has balanced grouping braces, three display pairs and four uncertainty marks. No TeX compilation or further image view was performed.
