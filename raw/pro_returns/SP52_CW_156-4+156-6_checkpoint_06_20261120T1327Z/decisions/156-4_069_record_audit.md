# Administrative record audit — 156-4 scan 069

Run: `/root/audit_069_records`. This is a text-only comparison of the three readers' final `reading.tex` and `report.json` with `page_packets/156-4_069/C.tex`, `H.tex`, and `C_context.md`. It is not a fourth reading. No manuscript image was opened, no OCR or outside research was used, no ink decision was made, and no mathematical statement was checked. Reader files and consolidated decisions/pages were not changed.

All three returns are complete; root supplied the final R2 completion signal before this audit was finalized. The audited final report counts are:

| Reader | Finished UTC, 2026-11-20 | Difference rows | C/context dispositions | Remaining doubts | Inventory | Crops |
|---|---|---:|---:|---:|---:|---:|
| R1 | 10:52:16 | 41 | 27 | 17 | 24 | 11 |
| R2 | 10:54:57.940828 | 48 | 27 | 16 | 24 | 20 |
| R3 | 10:52:55.067525 | 39 | 25 | 16 | 23 | 11 |

## Essential changes to an R1-based record

1. **Add the detached stroke reported by R2.** R2-D06, inventory I08, and Figure F01 identify a short detached low dash below the early middle of `stonienne`, citing `readers/156-4_069/R2/crops/02_ultra.jpg`. This group is absent from R1/R3's text and from R1's inventory. Root reports having independently viewed and accepted it. Add only that stroke to R1's existing opening figure and inventory; R1-D04 already covers the ultra insertion arm bundled into R2-D06. Assign no punctuation or linguistic function merely from the report. At R1's existing inventory granularity this makes **25 elements**.
2. **Account for H's extra placeholder after construction.** H literally reads `\ill{} la construction \ill{} $\Sigma$ en \ill{} que \ill{}`. R1-D17 covers the first placeholder and wording through `la construction`; R1-D18 begins with the material after Sigma. Neither row presently accounts for the distinct `\ill{}` between construction and Sigma. R2-D23 and R3-D19 cover it. Enlarge R1-D17 through `$\Sigma$` with matching witness scope, or record the removal separately. This is a missing witness-comparison entry, not a new manuscript group.
3. **Keep alphabet rows limited to their stated occurrences.** R1-D32 is explicitly the four M alphabets in the final display. Its full-formula snippets also contain the operator, x/X and relation changes already assigned to D31, D33 and D34. It must not acquire another C change merely because root adopts a final-prime doubt or changes one of those other decisions. R1-D38 similarly covers only the two bottom-note M alphabets; `les` and `connexes` belong to D39/D40. Narrow the snippets, or preserve explicit scope fields and keep every shared final snippet synchronized. A separate final-prime decision must distinguish that last occurrence from the argument's M-prime.

No wholly phantom R1 difference row was found: every row has a textual/state/certainty difference or a reported drawing omission at its stated scope. All nonempty R1 C/H snippets are exact substrings of the packet witnesses. A detached-stroke row would add one to its initial 41 rows if all existing rows survive adjudication; absorbing the construction placeholder into D17 need not add another. Final counts must follow the actual adopted rows and flags.

## Complete set of reading and certainty disagreements

These are the readers' written returns, not this auditor's ink judgments. “Uncertain” means the fragment actually contains an uncertainty macro; alternative order is preserved below.

| Locus | R1 | R2 | R3 |
|---|---|---|---|
| Detached stroke below stonienne | absent | drawn | absent |
| Verb before le compactifié | on trouvera / on trouve / on retrouve | on trouve / on trouvera / on retrouve | on trouvera / on trouve |
| Stone | definite | uncertain | definite |
| ne vois | definite | definite | uncertain |
| Extra opening mark in marginal equality | brace / parenthesis | brace / parenthesis | parenthesis / brace |
| Terminal mark in marginal equality | closing brace / point / comma / parenthesis | closing brace / point / comma / parenthesis | point / comma / parenthesis |
| Donc | uncertain | uncertain | definite |
| Supports verb | s'identifient / s'identifieraient | definite s'identifient | s'identifient / s'identifieraient |
| fera | uncertain | definite | definite |
| R in raised compatibility clause | definite calligraphic R | calligraphic R / plain R | definite calligraphic R |
| Lower added quantity word | toute / toutes | definite toute | toute / toutes |
| Phi modifier | bar / prime / unmodified | prime / bar / unmodified | bar / prime / unmodified |
| Last M in final display | definite one prime | one prime / two primes | definite one prime |
| Bottom saturées accent | saturées / saturees | definite saturées | saturées / saturees |

At otherwise matching open readings, R1 assigns the compact abbreviation low confidence while R2/R3 assign medium. R3 assigns the Phi doubt medium confidence, versus low for R1/R2. These confidence labels do not add another physical group.

All readers reproduce the same four insertion leaders/carets and bottom rule. Figure grouping differs: R1/R2 combine the opening leaders into one figure; R3 separates them. Their bottom-rule descriptions range from initial c, to the initial co/connexes area, to near connexes. These are local placement variants of an already inventoried rule. The drawing code also uses different anchors and rotations; it must not be treated as three independent reports of additional strokes.

## C doubts and current-scan context coverage

C.tex contains **19 explicit uncertainty occurrences**. R1 and R2 dispositions 1–19 cover these in source order. R3 also covers all 19 in that order. All 26 table rows in C_context are represented, including the standalone possible-pas check; no current-scan check is absent merely because R3 has 25 entries rather than 27. R3 combines the repeated Phi and operator checks with their C.tex dispositions.

For an exact coverage map, the following are **one-based R1 c_doubts array positions**:

| C_context table rows | Corresponding R1 disposition positions, in row order |
|---|---|
| 1–7, notation checks | 20; 21; 22 plus 6/7; 23 plus 16; 24 plus 18; 25; 26 plus 19 |
| 8–13, quelc. through marginal delimiters | 1; 2; 3; 4; 5; 6/7 |
| 14–19, Donc through ultra separator | 8; 9; 12; 13; 14; 15 |
| 20–26, relation through possible pas | 16/23; 17; 18/24; 10; 11; 19/26; 27 |

Propagate adjudication consistently across repeated dispositions: relation 16/23; Phi 18/24; operator 19/26; marginal edge marks 6/7 plus the explicitly core-only formula entry 22; and je/prouver 4/5 plus the no-pas entry 27. Entry 25 covers the comma and primes and therefore must reflect any new doubt at the last M. The fact that entry 22 resolves the core wedge/vee sequence does not resolve its separately doubtful edge marks. The no-pas disposition likewise does not resolve je, prouver, or R3's ne vois doubt.

R1 records multiple evidence references for the quotations and the three R occurrences, rather than pretending its primary crop covers all of them. Its je/prouver entries acknowledge the crop-07 framing limitation and refer to crops 06/08. This is an evidence-scope statement in the report, not a visual finding by this auditor.

The older C_context narrative contains draft variants including `Il va y avoir`, `cpt`, `l'ens.`, and `cosupp`, followed by later revisions. All three final returns instead agree on the cancelled `Il faudra y revenir`, uncertain `cpct/cpt/compact`, unpointed `ens`, and definite `cosup`. Preserve the current explicit dispositions; do not import an earlier draft assertion as another reader's conclusion. The current C notes about présume, the cancelled sentence, no supplied pas, and manuscript number 68 are all represented.

## Overlapping counts and quotation accuracy in the other returns

- **R2-D08 is a whole-note H omission**, with `change_c=false`; D09–D11 separately describe local C revisions at Stone and the two edge marks. Their H omissions are already inside D08. If these rows inform the consolidated counts, make the local rows C-only or explicitly exclude their repeated H claims from the aggregate. The drawing and its text are still one note.
- **R3-D06 repeats D07/D08's C changes**, while also counting the whole-note H omission. Keep D06 H-only when local rows retain the C revisions, and avoid counting the same H omission again in D07/D08. **R3-D36 repeats D37's saturées doubt**: its other changes concern H, so a lexical-only D36 should have no C change once the accent is assigned to D37.
- R2-D03/D04/D05 can represent separate insertion-state, quotation-glyph and hyphen decisions, but their shared span is not three copies of each change. R2-D43/D44 similarly need quotation-only versus comma/ou scopes. R2-D29/D32/D48 are drawing rows: their surrounding words are context, not additional counts of the already reported lexical changes.
- R2-D04's C snippet flattens the insertion macro. D27 closes `\inserted{muni de la relation}` and `\add{et de la relation}` prematurely; the actual inserted phrases continue through the relation and `de compatibilité`. Quote the partial prefixes without artificial closing braces, or quote the complete phrases. R2-D38/D39 normalize H's spaces/macros; D39 also substitutes `\quad` for H's literal spacing command. D41 quotes `\mathcal M'` where H literally has `\mathcal{M}'`. These are quotation repairs, not new manuscript differences.
- R3-D03 supplies a closing parenthesis immediately after stonienne in both source fields; both actual witnesses continue with a comma and the cause clause before closing the parenthesis. Remove that artificial close from the quoted scope. R3-D33 omits C's thin-space commands; this is normalized quotation, not a lexical difference.
- H editorially acknowledges both the long marginal note and the lower trait. Empty H fields in omission/drawing rows must therefore mean “no diplomatic transcription/drawing,” not “no mention anywhere.” R3 marks the whole marginal omission unmarked while R1/R2 mark it acknowledged. Apply one consistent `marked_in_h` policy. In R1-D38/R2-D45, `yes` reflects nearby illegible lexical text, whereas the M alphabet differences themselves are unmarked; an alphabet-only scope should make that distinction clear.

## Inventory and report/fragment consistency

The only separately reported physical group absent from R1 is R2's detached stroke. R2/R3 combine the construction and following cosupport-definition prose into one inventory block where R1 uses two. That grouping explains why R2's additional stroke does not increase its total over R1, and why R3 has one fewer element. No additional textual block, deletion, insertion, display, or marginal note was found missing from R1's inventory union.

All final fragments and remaining-doubt lists agree on their substantive readings and uncertainty scopes: 17 uncertainty macros/17 doubt entries for R1, and 16/16 for each of R2 and R3. Figure-separated words need not occur as contiguous source strings in the LaTeX; that alone is not an omitted-text discrepancy. Every repeated full-span report snippet must nevertheless follow root's eventual final fragment.

R3 uses string `yes`/`no` change flags; R1/R2 use booleans. Normalize explicitly before aggregating—ordinary truthiness would incorrectly treat R3's `no` as true. The readers also differ in some consequence classifications; those fields do not represent performed validations. All three `check_events` arrays are empty. This audit adds no check event.
