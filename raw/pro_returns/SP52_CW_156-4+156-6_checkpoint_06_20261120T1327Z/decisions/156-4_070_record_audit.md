# 156-4/070 — text-only record audit

Compared the completed R1/R2/R3 fragments and reports with C, H and C_context. No images were viewed, no crops created, and no ink or mathematical decisions were made.

## Record repairs and counting controls

1. **Lower H placeholders require occurrence-specific alignment.** R1-D28/D29 and R3-D28/D30 map the first `\struck{\ill{}}` before `Je` to cancelled `on a`, and the second after `donner` to cancelled `C5`. R2-D30/D32/D33 instead calls `on a` omitted, maps the first placeholder to `C5`, and treats the second as text absent from the page. These dispositions are mutually exclusive. Root has independently reported the R1/R3 alignment credible. If adopted, do not carry R2's additional omission/phantom-placeholder claims into H's tally. Preserve C5's physical placement separately from its decipherment; R1-D30 correctly uses `change_h:false` for the placement-only issue already deciphered in D29.

2. **Account for `que`.** R2-D20 and R3-D19 quote `vu` versus `car`, but C/final have `vu que le` and H has `car le`. Use the complete corresponding scope, as R1-D19 does.

3. **Replace nonliteral quotations/references.** R2-D16.h should quote H's `$F'$, $F''$`. R2-D22.c, R1's upper-right-sign C-doubt, and R3-C13.c join text separated by wrappers in C; quote the exact original label or the exact deleted subfragment. R2-D22.reading/CD26.reading and R1's diagram doubt fields use explanatory prose rather than the actual final drawing: supply an exact final fragment/reference. R2-D08 and R1-D40 concatenate separate TikZ labels; identify that extraction or point to their exact grouped figure. R1's two cancelled-clause doubt readings separately close a `\deleted` wrapper that spans both groups in the fragment; use exact local unsure groups or the complete cancelled clause.

4. **Scope repeated context dispositions locally.** R1's “C_context explicit bowed signs across page” is globally `resolved`, although its upper-right diagram sign remains uncertain. Qualify that occurrence explicitly. All C unsure loci otherwise have dispositions; no missing remaining-doubt locus was found. R1's two d-un(e) unsure groups share one doubt entry, so its 16 macros versus 15 entries is grouping, not an omitted doubt. R2 has 17 matching groups/entries; R3 has 14.

5. **Keep graphic rows from recounting their labels.** R2-D09/D21/D31/D41 and R3-D29/D35 quote whole figures containing text already compared locally. Count only the stated arm/layout/points/bars in those rows. R2-D21/D22 must distinguish layout from upper-right sign state. All nine H unreadable placeholders receive dispositions in every report; their lower-paragraph alignment, not their coverage, is disputed.

6. **Normalize flags before aggregation.** All boolean fields have actual JSON boolean types; inventory enums are valid. `marked_in_h` differs on the raised-sign state (R1 yes; R2/R3 no), diagram (R2 no; R1/R3 yes), and C5 bars (R2 no; R1/R3 yes). H explicitly describes the diagram and bars editorially; retain that fact separately from its literal transcription. Root should also settle inconsistent `math_consequential` classifications at the prose prime count, diagram, NB X/x, and C7 suffix/whole-note row; this audit does not adjudicate them. No independent difference based only on equivalent macro syntax was found.

## Written disagreements requiring root disposition

| Locus | Disagreement in completed returns |
|---|---|
| Raised condition's separate arm | Only R2 draws/inventories a distinct curved arm (G1/D09). R1/R3 have no corresponding drawing or disposition. Decide its status before treating their inventories as complete. |
| Word following figures | R1: unsure `toujours`; R2: unsure `en général` / `en position`; R3: certain `toujours`. |
| Opening certainty | R1/R3 resolve `aura`; R2 retains it. R1 retains `(i.e.` / `liée.`; R2/R3 resolve `(i.e.`. |
| Worked adjective | R1's joint alternatives allow no separately deleted older middle; R2/R3 always retain a deleted ati/atib layer. |
| Cancelled clause | R1: unsure `quand et que`, then seul/sub/seulement. R2: quand et/on dit/c.à.d., then seulement/sub. R3: quand et/on dit, then seul/sub. |
| Diagram lower-right position | R1/R3 use `uur` to the single upper-level F; R2 uses `ur` to an empty middle-row position. This is a concrete fragment difference, beyond the agreed upper-level placement of F. |
| Diagram worked sign | R1 draws the strokes; R2 uses a doubtful glyph plus a drawn stroke; R3 gives glyph/older-glyph alternatives. Carry the chosen representation into the doubt and inventory records. |
| Definition noun ending | R1 changes this occurrence to singular `subdivision`; R2/R3 retain `subdivisions`. Keep it separate from the agreed singular earlier in paragraph two. |
| Definition d-un(e) | R1/R3 allow an older d' before a surviving d'; R2 allows the single initial d' itself to be cancelled. These are different state alternatives. |
| Points after on a | R1 encodes unsure `..`/colon; R2/R3 draw the two detached points without assigning punctuation function. |
| Lower note | R1 retains Reporter/reporter/Rejeter/rejeter and resolves ces; R2 resolves Reporter but retains ces/mes; R3 retains only initial case of Reporter/reporter and resolves ces. |
| NB older F | R1 resolves the deleted F; R2/R3 retain uncertainty. |

The cancelled C5 also occupies three different fragment positions: R1 between `donner` and `aucune`, R2 before `Je`, R3 in a margin macro before the paragraph. A local layout chosen by root must be reflected in the final placement record and inventory.
