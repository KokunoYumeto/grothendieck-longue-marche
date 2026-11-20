# scan015 — textual metadata audit

## Scope and result

Read-only review of the three readers’ `report.json`, `audit.md`, and `reading.tex`; `packets/scan015/{C.tex,H.tex,C_context.md,S.json}`; `scan015_main_views.json`; and `scan015_main_crop_notes.md`. Crop JSON sidecars and path existence were checked as metadata. **No image was opened, no OCR/external source was used, and no LaTeX engine or compilation was run.** Reader files and decisions were not edited. This audits the recorded evidence, not the underlying ink independently.

The union is **38 discrepancy loci**: R1 has 36, R2 has 37, R3 has 38. All **11 C doubt loci** are represented by every reader. S is empty. The view manifest lists **27 distinct resolved paths**, comprising **12 main crops and 15 reused reader crops**; each exists. All reader discrepancy and C-doubt entries supply source coordinates, and every non-null linked crop exists. No additional image view is needed for this metadata audit.

### Items requiring attention in the main ledger

1. **Annotation parentheses: R3-015-D05 is the sole additional R3 locus.** H’s formula supplies `(rel. d’ordre dans F)`; C and all readings omit those parentheses. R3 explicitly reports their absence. Main crop 02 / note 17 contains the entire reported box `[675,342,1017,397]`, but note 17 does not explicitly state the parentheses finding. Give this locus its own disposition or an explicit cross-reference. Keep it distinct from brace geometry and family-F typography; credit H’s correct prose note locating the gloss below the row. At the initial snapshot this was a missing explicit main textual disposition, not missing crop evidence. The main reader subsequently confirmed from the already completed view 17 that there are no parentheses, and will add a same-view text supplement plus a separate editorial-markup disposition without an additional H-error count; that disposition credits H’s correct explanatory note. No image was reopened for this clarification.
2. **Canceled-label placement: R2-015-D30 / R3-015-D31 is absent from R1’s difference list.** R1’s audit nevertheless recognizes the crossed (1.32) beside the display; it declines to count H’s placement as more than macro placement. R2/R3 treat attachment to the prose line as a substantive placement error. Main note 25 explicitly settles the display alignment, so preserve that decision and record the apparatus-policy disagreement.
3. **Overlap must survive the final representation.** R2’s first-map code `\deleted{X}\inserted{F}` is sequential although its prose says superimposed. The deleted-X-plus-F alternatives in R2/R3’s second map are also sequential. R1’s `\mathord{\rlap{$\deleted{X}$}F}` encodes overlap. Main note 09 requires overlap at the first map, and note 13 requires overlap inside the relevant alternative at the second map. R2’s additional canceled-F alternative must not disappear when adopting R1/R3’s overlap syntax.
4. **The main notes imply seven residual uncertainty loci**, not any single reader’s count: first family-F alphabet; first/canceled-M alphabet; `avec`; fourth order index; first P alphabet; second-map physical state; final accent. The canceled-M C doubt is resolved only as **M rather than F**; its M alphabet remains uncertain. Repeated F/M/P occurrences still need their individual decisions even though alphabet alternatives are printed only at the first occurrence.
5. **Scoring/type flags are not unanimous.** Brace placement is `against_H=true` in R1/R3 but false in R2, although all credit H’s correct below-row gloss note. Main note 17 states the narrower residual geometry discrepancy. R2 also marks the enclosure, brace, and canceled-label placement as mathematical; R1/R3 do not. Do not copy a reader’s mathematical-row total without harmonizing that classification.
6. **Star-label retracing belongs in the inventory/notes.** Main notes 07 and 12 retain (*) and (**) without inventing predecessor text. Reader inventories include those labels, but their retracing/surcharge details occur chiefly in audits and notes. Carry that state into the final inventory if it claims to record the interventions.

## Complete discrepancy crosswalk

`Dnn` means the reader’s `Rk-015-Dnn`; the union follows R3’s order. Main numbers refer to the 27 numbered sections of `scan015_main_crop_notes.md`. A dash means no separate discrepancy row, not omission from the reader’s transcription.

| Union / R3 | R1 | R2 | Locus | Main note |
|---|---|---|---|---|
| D01 | D01 | D01 | Opening family F | 01 |
| D02 | D02 | D02 | Opening de | 16 |
| D03 | D03 | D03 | Open enclosure | 17 |
| D04 | D04 | D04 | Brace/gloss lateral placement | 17; H flag differs |
| D05 | — | — | Annotation parentheses supplied by H | 17 covers; main confirms absence and will supplement |
| D06 | D05 | D05 | Family F in annotation | 17 |
| D07 | D06 | D06 | definit accent | 02 |
| D08 | D07 | D07 | Canceled M after definit | 02 |
| D09 | D08 | D08 | First inclusion M | 03 |
| D10 | D09 | D09 | First inclusion family F | 03 |
| D11 | D10 | D10 | avec after (1.20) | 04; main retains doubt |
| D12 | D11 | D11 | M centered below first ≤ | 18 |
| D13 | D12 | D12 | M centered below first ≪ | 18 |
| D14 | D13 | D13 | Family F centered below second ≤ | 05 |
| D15 | D14 | D14 | Family F/barred f below second ≪ | 05; main retains doubt |
| D16 | D15 | D15 | M in L ⊂ M | 19 |
| D17 | D16 | D16 | Literal reference (1.25) | 06 |
| D18 | D17 | D17 | First-map domain family F | 20 |
| D19 | D18 | D18 | First power-set P | 08 |
| D20 | D19 | D19 | M in first P(M) | 08 |
| D21 | D20 | D20 | First-map overwritten X/F | 09 |
| D22 | D21 | D21 | Dep operator | 10 |
| D23 | D22 | D22 | Inserted alors | 11 |
| D24 | D23 | D23 | definie accent | 11 |
| D25 | D24 | D24 | M in (1.31) | 21 |
| D26 | D25 | D25 | Second-map domain family F | 22 |
| D27 | D26 | D26 | M in second-map Fig(M) | 23 |
| D28 | D27 | D27 | Second-map input/correction state | 13; main retains three states |
| D29 | D28 | D28 | M subscript in mapped Fig | 24 |
| D30 | D29 | D29 | Colon after (1.4) | 14 |
| D31 | — | D30 | Canceled (1.32) placement | 25 |
| D32 | D30 | D31 | M subscript in Fig definition | 25 |
| D33 | D31 | D32 | Second power-set P | 25 |
| D34 | D32 | D33 | M in terminal P(M) | 25 |
| D35 | D33 | D34 | M in tilde-X definition | 25 |
| D36 | D34 | D35 | Concluding family F | 26 |
| D37 | D35 | D36 | Concluding M | 27 |
| D38 | D36 | D37 | Final s’interprète/s’interprête | 15; main retains doubt |

The crosswalk exhausts all 36 + 37 + 38 reader rows. The initial main notes covered every union locus except that the specific parentheses statement remained implicit in note 17; the main reader has since confirmed that finding and plans the explicit supplement and editorial-markup disposition. Main notes 07 and 12 address the two star-label inventory questions, which do not need fabricated discrepancy rows.

## All C doubts

The positions below follow C’s eleven `unsure` instances. “Retained/revised” means uncertainty survives but its alternatives have been updated from the ink descriptions. Status is the disposition supported by the **main notes**, not a new visual judgment.

| C locus | Union | Main note | Main disposition |
|---|---|---|---|
| Opening family F | D01 | 01 | Retained/revised: mathcal F or mathfrak F; C’s mathscr alternative is replaced. |
| definit/définit | D07 | 02 | Resolved: unaccented definit. |
| Canceled M/family F | D08 | 02 | M identity resolved; canceled mathcal M versus ordinary M remains a separate alphabet doubt. |
| Fourth index, family F/barred f | D15 | 05 | Retained; R2’s certain F is not adopted. |
| Final digit of (1.26)/(1.25) | D17 | 06 | Resolved: literal (1.25), without cross-page repair. |
| First P alphabet | D19 | 08 | Retained/revised: mathcal, mathscr, or mathfrak P; plain roman P removed. |
| First canceled X | D21 | 09 | Resolved: X below superimposed live F. |
| Dep/Def | D22 | 10 | Resolved: Dep, without acute or final l. |
| définie/definie | D24 | 11 | Resolved: unaccented definie. |
| Second canceled X | D28 | 13 | Retained/expanded as state alternatives: live F, canceled F, or X overwritten by F. |
| s’interprète/s’interprête | D38 | 15 | Retained; R1’s certain grave is not adopted. |

This is **six resolved C questions and five retained C questions**, with the resolved M-identity question still generating a separate alphabet uncertainty. Adding that M alphabet and the newly retained `avec` produces the seven residual loci above. `C_context.md` repeats some loci and contains cross-page/mathematical suggestions; these do not create additional C doubt instances or authorize correction of (1.25).

## Inventory crosswalk

Numbers are one-based positions in each report’s inventory array. The 30 harmonized subelements below split combined entries solely to expose coverage: R3 separates frame, gloss, and brace; R2 alone gives the first source’s replacement F its own inventory entry. They are **not** 30 claims of independent source regions.

| Covered subelement | R1 | R2 | R3 |
|---|---:|---:|---:|
| Page number 14 | 1 | 1 | 1 |
| Opening paragraph and two underlines | 2 | 2 | 2 |
| Order display and (1.30) | 3 | 3 | 3 |
| Three-sided enclosure | 3 | 4 | 4 |
| Annotation text | 4 | 4 | 5 |
| Offset brace | 4 | 4 | 6 |
| que je vais partir. | 5 | 5 | 7 |
| Second paragraph introduction | 6 | 6 | 8 |
| Canceled M | 7 | 7 | 9 |
| First inclusion | 8 | 8 | 10 |
| First induced-order line | 9 | 9 | 11 |
| Second induced-order line | 10 | 9 | 12 |
| Second inclusion | 11 | 10 | 13 |
| Reference and application introduction | 12 | 11 | 14 |
| First map and (*) label | 13 | 12 | 15 |
| Canceled X at first source | 14 | 13 | 16 |
| Superimposed replacement F at first source | 14 | 14 | 16 |
| Definition introduction after first map | 16 | 16 | 17 |
| Raised alors and its leader | 15 | 15 | 18 |
| (1.31) definition | 17 | 17 | 19 |
| Connecting et | 18 | 18 | 20 |
| Second map and (**) label | 19 | 19 | 21 |
| Second input state uncertainty | 20 | 20 | 22 |
| par (1.4) and colon | 21 | 21 | 23 |
| Canceled (1.32) label | 22 | 22 | 24 |
| Fig formula | 23 | 23 | 25 |
| Connecting avec | 24 | 24 | 26 |
| Tilde-X definition and terminal point | 25 | 25 | 27 |
| Concluding paragraph | 26 | 26 | 28 |
| Final equivalence and live (1.32) | 27 | 27 | 29 |

All 27 / 27 / 29 original entries are covered. Every inventory entry has `sheet_kind=text`, `hand=his hand`, and `transcribed=yes`; drawings within the text sheet use their own `kind` values. The union contains all nine mathematical display units (R3 uses one figure plus eight display-delimiter pairs), page number 14, two separately underlined phrases, the raised alors, certain canceled M and first X, uncertain second-map intervention, and canceled versus live (1.32). No unmatched prose block or inventory object was found.

## Remaining metadata cautions

- R1/R3 read certain `avec`; R2 and main retain it. R2 resolves the fourth index; R1/R3 and main retain it. R1 resolves the final accent; R2/R3 and main retain it. These are genuine reader disagreements, not internal report/reading mismatches.
- R1 orders the second-map alternatives with overwritten X first; R2/R3 put live F first. Main adds canceled F as a third state. Preserve the chosen ordering consistently across the final reading, decision, and unresolved list.
- The same recurring alphabet convention does not eliminate occurrence-specific evidence: the reports consistently enumerate eight family-F occurrences, thirteen M occurrences including the canceled one, and two P occurrences. The 38-locus crosswalk retains these separately.
- H’s emphasis versus C’s underlining, equivalent label syntax, and ordinary line wrapping are not additional discrepancies. H’s first-X note earns credit for recognizing the correction; do not count the canceled X as omitted by H.
- The three readers’ mathematical check events all explicitly say no mathematical verification was performed. Their assertions of reading/structural completion must not be upgraded into proof validation. Their author-doubt content is empty/negative, consistently with empty S.
- R2 serializes `notes` as a one-item array and its negative author-doubt statement as text; R1/R3 use a notes object and empty author-doubt arrays. This is a schema-normalization concern if consolidating programmatically, not an additional transcription dispute.

No final decision JSON was audited; this report is the textual crosswalk for the main decision being drafted. The main reader confirmed that all 37 R2 loci will receive rows, first-X markup will preserve overlap while crediting H’s note, all three second-input states will remain, and the final inventory will use R3’s entries plus a replacement-F element. No reader file or decision was changed.
