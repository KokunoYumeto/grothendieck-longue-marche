# Source coverage audit — 156-4 scan072

## Status and authority

Text-only administrative audit of `page_packets/156-4_072/C.tex`, `H.tex`, and `C_context.md`. No image was viewed, no OCR or compilation was run, and no mathematical or ink decision was made. The initial source-only stage preceded adjudication. Root subsequently confirmed all three complete v08 returns and supplied the exact final page and final decisions. The record-assembly stage below applies that authority without adopting an independent ink reading or modifying page text; root review remains pending.

Balanced-brace source extraction verified **30 literal C `\unsure` occurrences**, **23 C-context table rows**, and **15 literal H `\ill{}` placeholders**. Two of H’s placeholders occur inside an editorial `\note`; they are included in 15. Repeated discussions of one physical position remain separate source-coverage entries, not extra physical differences.

## C literal uncertainty coverage

Each quotation below is copied byte-for-byte from C. C-number order is literal source order.

- **C01** (C line 3): `\unsure{=}` — Opening, second pair of horizontal strokes after quand; the preceding literal `=` is outside the macro.
- **C02** (C line 3): `\unsure{en forme|en jeu}` — Opening, phrase after définition.
- **C03** (C line 5): `\unsure{\deleted{\mathcal F}\mathcal C|\mathscr C|\mathbb C}` — Definition, one capital position before the tuple equals; deletion is an alternative inside this one occurrence.
- **C04** (C line 5): `\unsure{\preceq|\leqslant}` — Definition tuple, second order sign only.
- **C05** (C line 5): `\unsure{satisfait|satisfont}` — Definition, verb after qui.
- **C06** (C line 7): `\unsure{quelc.}` — Condition a, abbreviation following sup.
- **C07** (C line 7): `\unsure{correspond|correspondant}` — Condition a, end of the s’en-correspond phrase; prefix `s'en` is outside the macro.
- **C08** (C line 7): `\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}` — Condition a, mapping in the raised par insertion.
- **C09** (C line 7): `\unsure{\mathrel{\mapstochar\relbar}|\mapsto}` — Condition a, mapping following M′.
- **C10** (C line 10): `\unsure{(condition stricte)|(condition stricts)}` — Slanted question, entire first parenthetical condition.
- **C11** (C line 10): `\unsure{et}` — Slanted question, a token within an external `\deleted{...}`.
- **C12** (C line 10): `\unsure{de|des}` — Slanted question, after ou bien.
- **C13** (C line 10): `\unsure{(condition large)|(condition lge)}` — Slanted question, entire second parenthetical condition.
- **C14** (C line 12): `\unsure{\}|?}` — Condition b, brace/question-like mark after M; the escaped closing brace is part of the macro content.
- **C15** (C line 12): `\unsure{à savoir|savoir}` — Condition b, opening of the deleted clause; colon and si X∈ are outside this occurrence.
- **C16** (C line 15): `\unsure{reporter|rajouter}` — Marginal c, instruction preceding circled c.
- **C17** (C line 15): `\unsure{fixé|fixée}` — Marginal c, adjective after subd.
- **C18** (C line 15): `\unsure{F}` — Marginal c, candidate F within external deletion immediately before sous-fig.
- **C19** (C line 15): `\unsure{-|\longrightarrow}` — Marginal c, relation between the two sous-fig. phrases.
- **C20** (C line 15): `\unsure{s}` — Marginal c, candidate s within external deletion before commute.
- **C21** (C line 15): `\unsure{i.e.}` — Marginal c, terminal abbreviation.
- **C22** (C line 20): `\unsure{de|dans|ds}` — First C6 diagram, qualifier before the family capital.
- **C23** (C line 26): `\unsure{avec|ou}` — C6 part a, final word after H∈family.
- **C24** (C line 32): `\unsure{strates|str.tes|arêtes}` — Right note b, first occurrence of strates/str.tes/arêtes.
- **C25** (C line 32): `\unsure{S}` — Right note b, separately encoded deleted S immediately before the second strates-like occurrence.
- **C26** (C line 32): `\unsure{strates|str.tes|arêtes}` — Right note b, second occurrence of strates/str.tes/arêtes; retain separately from C24.
- **C27** (C line 32): `\unsure{tel|\deleted{tel}}` — Right note b, first three letters of telles and their deletion state; literal `les` follows outside the macro.
- **C28** (C line 32): `\unsure{G|G_m|G_n}` — Right note b, G or a subscripted form after X′≪.
- **C29** (C line 32): `\unsure{servira}` — Right note b, verb before plus bas.
- **C30** (C line 34): `\unsure{sous-fig}` — Bottom paragraph, final sous-fig within external deletion.

## All 23 context rows

CX-number order is the 23 table rows under “C doubts for this page”. Each fenced row is an exact complete source line, including the draft’s own explanations. These explanations are witness claims, not this audit’s findings. Coverage pointers only identify where a final record must account for them.

### CX01

```text
| 72, definition, just left of = | looped C with interior F-shaped stem and bar; family F in the parentheses | `\unsure{\deleted{\mathcal F}\mathcal C\|\mathscr C\|\mathbb C}, \mathcal F` | The interior form closely matches the ℱ drawn just to the right. A heavier C runs around it; a single elaborate script or doubled C is also possible. The C in the same triple on 66 has a smooth open interior. |
```

Coverage: C03; additionally the following family capital, which has no literal C unsure.

### CX02

```text
| 72, definition and C6 diagrams | ≤ and curved ≼; rotated ≤ | `\leq, \unsure{\preceq\|\leqslant}, \rotatebox{90}{$\leq$}` | Horizontal curved sign points left. The vertical sign points down, with its detached stroke to the right. |
```

Coverage: C04; additionally all displayed order signs and both rotated vertical-order drawings.

### CX03

```text
| 72, two lines of a and margin c | horizontal mapping strokes with different ends | `\mathrel{\vdash\joinrel\dashv} or \mathrel{\mapstochar\relbar}, alternative \mapsto` | Two caps on the inserted ℱ′ mapping and the marginal G mapping. The M′ mapping has a clear left cap and a dark right endpoint. The long line between sous-fig. has no definite head. |
```

Coverage: C08, C09, C19; additionally the unmarked G-to-G′ mapping in marginal c.

### CX04

```text
| 72, a bracket | F with a roof and M with a prime | `\overline F\subset M'` | Roof covers the one plain F. M′ appears also squeezed above de. |
```

Coverage: No literal unsure: barred F, plain/prime M forms, the raised M′, and insertion placement.

### CX05

```text
| 72, right of C6 square | X′, two left angles, G with short downward ticks | `X'\ll\unsure{G\|G_m\|G_n}` | At the end of G the dark thickened stroke bends down twice. These strokes might form a small lowered m or n. |
```

Coverage: C28; the ≪ relation remains a separate notation scope.

### CX06

```text
| 72, C6 letter labels | a b c within circles | `\textcircled{a}, \textcircled{b}, \textcircled{c}` | The letters in the definition above are followed by an ordinary closing parenthesis. |
```

Coverage: No literal unsure: three circled labels c/a/b versus ordinary a)/b) in the definition.

### CX07

```text
| 72 | first paragraph | quand = = ; en forme | second = perhaps a repeat mark; en jeu | medium | Two neighbouring pairs of strokes. Last word begins with a large descending loop. |
```

Coverage: C01 and C02; the first literal equals/repetition mark also needs coverage.

### CX08

```text
| 72 | definition, first capital and second order | calligraphic C over a possible ℱ; ≼ | one script C; double-stroked C; sloping ≤ | medium | The vertical has a short crossbar as in the adjacent ℱ. The C in the corresponding triple on 66 is drawn without that stem. The lower line of the second order is curved. |
```

Coverage: C03 and C04; repeated source discussion, not a new physical occurrence.

### CX09

```text
| 72 | a, after sup and after titre | quelc.; s'en correspond | correspondant | medium | First word has a terminal dot. The long word crosses the line break after corre-. |
```

Coverage: C06 and C07.

### CX10

```text
| 72 | a, mappings; marginal c | two capped strokes, or left cap and dash | mapsto | medium | The ends are differently drawn; the small right mark has little or no slope. |
```

Coverage: C08, C09, C19 and the unmarked marginal G mapping; overlaps CX03.

### CX11

```text
| 72 | oblique note, after quelconques | (condition stricte); struck et; (condition large) | (condition stricts); (condition lge) | low | A sharp crossing adjoins the parenthesis; the final word runs into the paragraph on the right. |
```

Coverage: C10, C11 and C13; contraction spelling is broader than selecting one supplied alternative.

### CX12

```text
| 72 | b, after M′ de M; crossed clause | }; à savoir : si X ∈ | ?; savoir : si X ∈ | low | Curved extra sign, and a single long stroke through the superseded clause. |
```

Coverage: C14 and C15; include the rest and extent of the deleted clause.

### CX13

```text
| 72 | marginal c | reporter; subd. fixé; F and s under strokes; i.e. | rajouter; fixée | low | Reporter resembles the instruction on 70. A raised accent is visible over fixé; the tiny endpoint could include e. The diagonal pointer ends beside i.e. |
```

Coverage: C16, C17, C18, C20 and C21; pointer is an additional structural scope.

### CX14

```text
| 72 | C6, qualifier to the right | de | dans; ds | low | The preposition after its initial d is a single low undulation. Dans and its contraction are possible here. |
```

Coverage: C22.

### CX15

```text
| 72 | a, end of line | avec | ou | low | Three low strokes end at the edge; H in this sentence is clear. |
```

Coverage: C23; H and the line-end punctuation remain separately auditable.

### CX16

```text
| 72 | b by the square | strates, strates | str.tes or arêtes | low | The tied medial strokes and abbreviated-looking gap occur twice. The second initial has a separate crossing. |
```

Coverage: C24 and C26; C25 deletion state is adjacent and must not be silently absorbed.

### CX17

```text
| 72 | b next to square, before que and at end | telles; servira | tel crossed in telles | low | The first three letters have a long horizontal touch which may be the t bar. The letters immediately preceding plus bas are almost all low pen strokes. |
```

Coverage: C27 and C29.

### CX18

```text
| 72 | last line, deleted ending | sous-fig | — | medium | Tall last ascender/descender and a single stroke over the word. |
```

Coverage: C30.

### CX19

```text
| 72 | definition, after qui | satisfait | satisfont | medium | The low closed group after f ends in a rising t. Its medial strokes do not establish ai or on. |
```

Coverage: C05.

### CX20

```text
| 72 | slanted note, after ou bien | de | des | medium | A short d and low stroke; compare the slightly longer group before the first sup. |
```

Coverage: C12.

### CX21

```text
| 72 | square, note b, after X′ ≪ | G | G with lowered m or n | low | Two short downward strokes touch the right edge of the G. The prose about G favours the single letter. |
```

Coverage: C28; repeated discussion of the same G position as CX05.

### CX22

```text
| 72 | C6, part a and second diagram | un unique H; lower left G′ | same letter at both places | The declaration has two uprights joined by a tilted stroke, the drawn node a rounded G and a prime. |
```

Coverage: No literal unsure: H in the prose and G′ at the diagram node are two distinct written positions.

### CX23

```text
| 72 | a, after titre | s'en correspond | an ending agreeing with sous-ens. may be intended | The ending is obscured by the line break and the correspondence is repeated immediately in signs. |
```

Coverage: C07; repeated discussion of the same correspondence phrase as CX09.

## H placeholder alignment coverage

Each H-number counts one literal placeholder in source order. Repeated quotations deliberately show the enclosing scope; they do not multiply the placeholder count.

### H01 (H line 2)

```tex
les axiomes \ill{} passent aux sous-contrées.
```

Opening clause. Preserve the quoted H verb passent as part of the comparison with C’s vont passer; the placeholder is not independently a proven single missing word.

### H02 (H line 2)

```tex
la définition en forme [\ill{}]
```

Raised bracketed [pleine] insertion at the definition. This is the same physical item as C’s `\inserted{[\uline{pleine}]}`; record once, with H’s placement explained. Do not invent a second word after en forme or double count a missing pleine.

### H03 (H line 7)

```tex
$\mathcal{M}'$ de $\mathcal{M}$, \ill{} plus bas)
```

Raised replacement above the b deletion; compare C’s `\inserted{qu'on va formuler}`. H’s first editorial note offers a conflicting partial description of this same insertion.

### H04 (H line 7)

```tex
\struck{\ill{} si $X \in F$}
```

Start of the deleted b clause. Scope includes the struck state and H’s final F; neither the placeholder nor C’s shorter clause can settle that endpoint administratively.

### H05 (H line 9)

```tex
\marginal{il faudra \ill{} des \ill{} (\ill{})}
```

First of three placeholders in H’s compressed slanted question. All three align to that single marginal block; no exact word partition is licensed by H.

### H06 (H line 9)

```tex
\marginal{il faudra \ill{} des \ill{} (\ill{})}
```

Second placeholder in the same compressed slanted question. Retain its ordinal and group mapping; do not count the block again as a second whole omission.

### H07 (H line 9)

```tex
\marginal{il faudra \ill{} des \ill{} (\ill{})}
```

Third placeholder in the same compressed slanted question, within parentheses. Preserve the group mapping and wait for root’s literal contraction/parenthesis decisions.

### H08 (H line 10)

```tex
sous-fig. de $F'$, \ill{} aux Sup (pour $\leq$) i.e.}
```

Marginal c, verb before aux Sup. Adjacent deleted starts and mapping signs are outside this placeholder.

### H09 (H line 15)

```tex
(a) Alors il existe un unique $H \in \mathfrak{F}$ \ill{} :
```

C6 part a, final word after H∈family. The H colon is explicit punctuation outside the placeholder.

### H10 (H line 20)

```tex
(« \ill{} complètement \ill{} »)
```

First placeholder inside H’s editorial note quoting a partial lower line. Align to the Ce complément… line; this is an editorial observation, not a manuscript unknown word.

### H11 (H line 20)

```tex
(« \ill{} complètement \ill{} »)
```

Second placeholder inside the same editorial-note quote. Same lower line, same grouped mapping; H’s explicit complètement must also be compared with the final reading.

### H12 (H line 21)

```tex
\marginal{\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{} sur la sous-figure $G$ de $F$}
```

First placeholder in H’s combined marginal block. Its local alignment belongs to the symmetry note; no separate manuscript token can be supplied just because H used a placeholder.

### H13 (H line 21)

```tex
\marginal{\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{} sur la sous-figure $G$ de $F$}
```

Second placeholder in the same combined marginal block, between symétrie and the order signs. Final scope follows root’s separate symmetry-note reading.

### H14 (H line 21)

```tex
\marginal{\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{} sur la sous-figure $G$ de $F$}
```

Third placeholder in the combined marginal block, after the order signs and before sur la sous-figure. This is a structural transition between two marginal notes unless root establishes ink there; do not invent a joining word.

### H15 (H line 23)

```tex
par la subd. $F'$ de $F$, \ill{} que $G'$ est la \struck{sous-fig.}
```

Bottom paragraph conjunction before que; compare C’s explicit ou. The final cancelled word is a separate scope.

## Explicit scopes beyond the placeholder inventories

- **H’s first editorial note:** preserve its literal claim `deux mots, « qui ne » et un mot souligné non lu` as a witness/editorial claim about the b insertion; do not transplant it into manuscript text. The same note’s circled c and downward-arrow description requires a structural record.
- **H’s second editorial note:** besides H10/H11, it describes circled a/b, square disposition, the H/G′ mismatch, double ruling at b, and the long C6 border. These are structure/evidence scopes independent of H’s prose flattening of the diagrams.
- **Definition:** opening Pour/Par; vont passer/passent; literal repetition marks versus même; heading/underlining; raised bracketed pleine and its connector; worked single capital position; family alphabet; plain M/M′ versus calligraphic M; live/cancelled tout; hyphenation and line divisions.
- **Condition a:** correspondence insertion and connector; raised M′ and connector; both distinct mapping strokes; overbar on F versus H’s bare F; bracket/brace/stop scope.
- **Slanted question and b correction:** entire marginal sentence, contractions, punctuation and small deletion; curved extra mark; initial deleted clause and endpoint; raised replacement; no grammatical normalization.
- **Marginal c:** instruction and circled label; fixed/fixée; one worked initial position versus a separately encoded deletion; G mapping; horizontal relation; second cancelled start; commute/Sup/i.e.; long pointer.
- **C6 and lower margin:** qualifier; first diagram layout, two detached points reported by root, and all sign orientations; symmetry note, accent and C6 rule; final word and colon; second diagram H/G′ positions; repeated strates-like forms, worked initial and tel state; final G suffix; added Ce complément line and its ruling; bottom worked capitals, separate underlines, punctuation, final cancellation, and slanted sur la sous-figure note.

These scopes are a checklist of comparisons suggested by the supplied sources and root notes. Their final readings, change flags, confidence and crop support were subsequently supplied by root and applied in the record builder; final approval and consolidation remain reserved to root.

## Record-assembly gate and schema checklist

- **Gate met:** root explicitly confirmed all three complete returns and supplied `SP52_work/pages/J156-4-09_156-4_scan072.tex` plus final choices before report comparison and JSON assembly.
- Preserve all three reader readings and provenance at every disputed locus. Do not infer agreement from missing coverage. A majority is not an ink decision.
- Use the previous record’s schema: page metadata and final-text hash; `differences`; `c_doubts`; `disputes`; `remaining_doubts`; `h_placeholder_alignment`; `inventory`; `notation`; `abbreviations`; `witness_reviews`; `check_events`; reader counts; root-viewed crop allowlist; workflow and administrative validation.
- Every C literal uncertainty C01–C30 and every context row CX01–CX23 needs explicit final coverage. Context-only matters must not disappear because they lack a literal `\unsure`.
- Every H placeholder H01–H15 needs an ordinal mapping, including H10/H11 in editorial prose. H02 is the single raised pleine insertion; H05–H07 are one grouped marginal block; H10/H11 are one editorial quote; H12–H14 span two marginal notes.
- Exact C/H excerpt scopes must be source substrings. Editorial descriptions must be labeled as such; omission claims must be labeled rather than presented as invented quotations.
- `crop`, `bbox`, and `bbox_image` must come from root-authorized evidence metadata; administrative assembly must not claim image inspection.
- Record mathematical checks only if root explicitly made them. This audit made none.
- No page text, shared deliverable, compilation, research, or finalization is performed by this audit.

## Mechanical source verification

Passed: balanced C macro extraction = 30; C-context table rows = 23; H exact placeholders = 15; each H scope quotation is an exact H substring. The escaped brace inside C14 and nested deletion inside C03/C27 were parsed without truncation.

## Completed record assembly and administrative checks

Root’s all-three-final notice and exact final page enabled `SP52_work/scripts/decide_072_records.py`. It writes only `SP52_work/decisions/156-4_072.json`; status remains **draft — awaiting root review**. No image was opened, and no page text, shared deliverable or finalization state was changed.

| Check | Result |
| --- | --- |
| Final metadata | v08, scan 72, manuscript folio 71 |
| Difference scopes | 69; 38 C changes and 63 H changes |
| Literal C uncertainty coverage | All 30, quoted exactly and in source order |
| Context-only coverage | 7 additional rows; all 23 source-context rows mapped |
| H placeholders | All 15, including the two inside editorial prose |
| Three-reader disputes | 29, preserving all three readings and source IDs |
| Remaining doubt loci | 22, covering every one of the final page’s 23 unsure occurrences |
| Complete reader difference-row coverage | R1: 62/62; R2: 43/43; R3: 64/64 |
| Inventory | 45 unique elements, with original-orientation positions |
| Reader crops | R1: 17; R2: 18; R3: 18 |
| Root evidence | 20 distinct existing crops plus 5 new crops |
| Mathematical check events | 0 |

All nonempty difference-row C/H quotations are exact source substrings. All transcribed final excerpts and supplemental excerpts are exact final-page substrings. D65 and its C20 coverage row are explicitly labeled absence dispositions (“No independent s after F′.”), anchored to the exact final line rather than misquoting adjacent live text. Reader source IDs resolve to their preserved complete reports. Every cited evidence crop belongs to root’s explicit viewed-crop allowlist. The final-text hash matches the exact page.

### Scope decisions preserved in the audit

- H’s raised bracketed placeholder maps once to `[pleine]`. R2’s separate “missing word after en forme” interpretation is retained as a rejected alignment dispute, without a second counted omission.
- H’s three placeholders in the compressed supremum question map to one block. Its two placeholders around editorial `complètement` map to the one added lower continuation. The symmetry and lower sur-notes remain separate physical notes.
- Convention 7 joins physical `corre-/spond` as `correspond`. The physical hyphen is reading evidence only; joining it does not count as an H change.
- Convention 4 already permits a deleted old glyph before a live one to encode an overprint. Zero-width placement and math-safe wrappers do not themselves count as C changes. The definition-capital C revision is the added plain calligraphic-C alternative. The c and second-noun revisions concern actual identity/state/case alternatives.
- Convention 6 gives first-candidate priority meaning: D11 satisfont/satisfait, D26 savoir/à savoir and D53 G_n/G_m/G are counted as C preference revisions. Their decisions and C dispositions state this explicitly without grammatical or mathematical claims. The avec/ou priority already matches C and remains unchanged.
- The lower diagram uses root a02 together with existing R1/15; a02’s clipped lower edge is explicitly documented. The overlap at source y2205–2215 and continuation in R1/15 supply the tails, without a second new crop.
- The final body retains a clean later G prime and a plain final F followed by a doubtful literal drawing. The first body capital and lower marginal capital retain their separate worked alternatives.
- The bottom punctuation inventory item precedes the final cancelled sous-fig on that same line. The lower sur-note is explicitly alongside the foot paragraph, separate from the earlier symmetry note.
- Notes quote the author’s opening caution and slanted question; remaining local doubts are described separately.

### Final-page fingerprint

`864106f5af428070e14d2535a9dd9a33748aa68eaf304d7de0ccfa7c04c31966`

## Last root correction batch applied

- D11, D26 and D53 now have `change_c=true`, and C05/C15/C28 are marked revised for their changed preferred candidate. C changes consequently total 38.
- D01 Pour, D30 reporter and D42 de use medium confidence.
- D16’s main final excerpt includes both raised M′ and baseline de M; its scope note excludes the intervening mapping node. D29’s main excerpt includes deletion, raised replacement and plus bas. D54’s main excerpt includes plus bas.
- D65 and C20 state the absence of an independent s after F′ and are explicitly classified as absence dispositions; all other final excerpt substring checks remain in force.
- D69 compares only the C/H comma. H’s following unreadable conjunction remains confined to D59.
- D15/D20 evidence descriptions concern only their family-F scopes; D45 describes a only.
- D33/D51 describe uncertainty of the earlier layer or initial’s state/case, without treating C’s permitted deleted/live encoding as evidence of sequential glyph positions.

The builder was rerun successfully after this batch. The page was unchanged and its hash still matches. Root approval/finalization remains pending.

## Root approval — 2026-11-20 12:57:00 UTC

All three complete independent readings and all consolidated scopes have been reviewed against the root crop record. Approved:69 loci,38 C/63 H changes;23 uncertainty macros covered by22 remaining-doubt loci;29 disputes;45 inventory elements. Root viewed20 existing and5 new crops. The final page hash matches; no mathematical proof check occurred.
