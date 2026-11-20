from pathlib import Path
from datetime import datetime, timezone
import json
p=Path('/workspace/scratch/8db4dde48936/sp53_recovery/out/readers/scan015/R2')
r=json.loads((p/'report.json').read_text())
plan=json.loads((p/'crop_plan.json').read_text())
parts=[r'''# Scan 015 — independent reader R2 audit

## Scope and method

Read only the assigned scan015 packet, supplied notation table, exact output PREAMBLE, H convention file, and the permitted crop utility source. C and H were treated as unverified witnesses. No other page image, other reader’s output, consolidated decision, OCR, text recognition, PDF extraction, web source, or published transcription was consulted. No other reader was spawned or consulted.

The whole image was emitted once for layout. The two supplied halves were emitted once each, in order, and read line by line against both C and H. The supplied halves overlap; there was no additional full-half view or whole-half enlargement. Thirteen original enhanced crops were then emitted once each. No image was re-viewed and no crop was replaced or recompressed. All writes are in the assigned R2 directory.

The start timestamp is the first explicit clock reading, taken just after the initial packet/convention reads; it is not an invented earlier start time. All view timestamps come from clock samples at the corresponding emitted images.

## Image-view sequence

| Order | Role | Image | UTC |
|---:|---|---|---|
''']
for i,v in enumerate(r['view_log'],1):
 parts.append(f"| {i} | {v['role']} | {Path(v['image']).name} | {v['viewed_utc']} |\n")
parts.append(r'''
Actual view count: **16** = 1 whole + 2 supplied halves + **13 actual crops**.

## Open loci after the two halves

The crop pass was limited to these local questions:

1. Opening family-F alphabet: letter identity clear, ornamental typeface unresolved.
2. Adjacent `definit` and canceled symbol: initial acute and canceled M/F identity.
3. First live M in its inclusion: M alphabet and comparison with the neighboring family F.
4. Tiny `avec` after (1.20): H’s explicit local doubt.
5. The final induced-order label: family-F cap versus an overbar on small f; the adjacent label supplies a local comparison.
6. Last digit in (1.25)/(1.26).
7. First power-set P alphabet, with its M argument as nearby context.
8. Crossed/overwritten source in (*).
9. Operator letters and accent in Dep/Def/Dépl.
10. Possible acute in `definie`, near the insertion connector.
11. Physical state of the source in (**): plain F, canceled F, or X overwritten by F.
12. The two tiny punctuation marks after (1.4).
13. Accent in the final `s’interprète`/`s’interprête`.

Other matters were settled from the halves, including the missing `de` in H’s opening, inserted `alors`, the right-open enclosure, brace offset, four centered order labels, repeated letters’ locally visible shapes, canceled (1.32) position, the sets’ separators/inclusions, tildes, arrow directions, and the final equivalence. Their original-source boxes appear in the report even where no crop was made.

## Crop transforms and decisions

All crops were generated from the stated original half, without rotation (0°), by Pillow crop → autocontrast → UnsharpMask(radius=1.2, percent=120, threshold=3) → LANCZOS resizing to 2800 pixels across, then JPEG quality 95. Original evidence was not overwritten. Per-crop JSON sidecars preserve the same transform and coordinates. Boxes are `(left, top, right, bottom)` in the original source image; half_b coordinates are relative to that supplied half, not to the whole.

| Crop | Source | Original box | Scale | Output pixels | Purpose / result |
|---|---|---|---:|---|---|
''')
results={
'01':'Family F clear; mathcal/fraktur alphabet uncertainty retained.',
'02':'No acute in definit. Canceled symbol has two peaks and trough: M; its alphabet remains a separate initial doubt.',
'03':'Confirms cursive M construction and local family F, without choosing a unique M font.',
'04':'Avec remains plausible but compressed; H’s doubt retained and a doubt added against C.',
'05':'Final detached horizontal is the family F’s cap. The label is not barred f. Both labels sit centered under their signs.',
'06':'Literal final digit is 5: top bar and open short lower return, no closed 6 loop.',
'07':'Ornamental P; exact alphabet retained as mathcal/script/fraktur alternatives. M argument locally read.',
'08':'Two crossing diagonals of X remain under a heavy F. X identity resolved; H’s physical-state note credited.',
'09':'Dep: long looped descending p, no final l, no acute.',
'10':'No independent acute over initial e; large upper-left curve belongs to inserted alors’s connector.',
'11':'One oblique stroke and complete F do not prove X. Live-F, canceled-F, and overwritten-X states retained.',
'12':'Two separate points confirm colon.',
'13':'Word readable; accent remains unresolved near tall strokes and a preceding-line descender.'}
for q in plan:
 x0,y0,x1,y1=q['box']; w=x1-x0; h=y1-y0
 parts.append(f"| {q['name']} | {Path(q['source']).name} | `{q['box']}` | {2800/w:.4f}× | 2800 × {round(h*2800/w)} | {results[q['name'][:2]]} |\n")
parts.append(r'''
The canceled symbol and `definit` are adjacent questions served by a single phrase crop. The family-label crop includes the adjacent label for letter construction. The P crop includes its immediate M argument. These crops are reused as evidence in the relevant rows; no second crop was made for a question already covered.

## Line-by-line comparison

- **Header:** manuscript page number `14` present. No archive pencil number or date observed. C’s `mspage` and H’s page-number note cover the same item.
- **Opening two lines:** `En résumé, en termes de F, c’est de / la donnée de deux relations d’ordre`. H drops `de`; both underlined phrases are separately present. Family F has the established cap/cross-arm/return form, with first-occurrence alphabet doubt retained.
- **(1.30):** both order signs, comma, `telles que`, ordinary F/G operands, implication direction, and label are read as both witnesses otherwise give them. The gloss is `rel. d’ordre dans F`, without expansion. H’s note correctly observes the below-signs brace. The brace/gloss are offset right relative to C’s centered representation. Top, left, and lower enclosure strokes are present; no right upright is visible, and gaps separate the left upright from both horizontal rules. The supplied closed boxes change that geometry; TikZ records the visible enclosure and brace.
- **Continuation:** `que je vais partir.` agrees with both witnesses, including final point.
- **Second paragraph opening:** `En termes de celles-ci, on definit` has no separate acute over e. The canceled following letter is M, not single-stem family F. Its typographic alphabet remains uncertain at this first M occurrence.
- **First inclusion:** M subset family F; the subset is open and has no bar. Both letters were locally inspected. C’s ordinary-M choice differs from the first candidate used here; H’s family-F alphabet differs.
- **Two prose lines after (1.20):** the reference, comma, `les relations`, `induites par`, `puis`, and punctuation agree. The small `avec` remains doubtful. The two M labels and two family-F labels are centered beneath their signs. H’s lower-right subscripts change that placement. The last F’s detached cap is not a separate overbar.
- **Second inclusion:** calligraphic L subset M. L and the open subset agree; M is reported individually against C’s alphabet.
- **Application introduction:** literal `par (1.25). L’application`. The final digit is 5. H’s note about the definition on another page was not independently checked and was not used to correct this page.
- **(*):** family domain F, hooked application arrow, ornamental power-set P(M), and the element-map’s vertical bar/right arrow were inspected. Both diagonals of an older X remain beneath the source F. H’s explicit canceled-X note is credited, rather than counted as an omission. The operator is `Dep(F)` with no acute/final l. The rough star label is legible; no former label was invented beneath it.
- **Definition introduction:** inserted word is `alors`, not H’s `donc`; `est` and `par` agree. `definie` has no independent acute. The insertion is placed between `est` and `definie`.
- **(1.31):** tilde F equals the set of X in M with X ≤ F. Braces, single vertical separator, ordinary operands, tilde, order direction, and label agree. M alphabet is separately reported.
- **`et` and (**):** family F maps by a hooked arrow to Fig(M); the element map goes right to Fig_M(F). Every M and family F occurrence is separately reported. The source has a complete F and one rising diagonal. C’s definite older-X structure is not secured; H’s unqualified live F is also too definite. The transcription explicitly retains the physical-state alternatives.
- **`par (1.4) :`:** two points confirm the colon omitted by H.
- **Canceled (1.32) and Fig definition:** the crossed label is aligned with the display below the `par (1.4)` line, not in that prose line as in H. `Fig_M(F) = {tilde X | X in tilde F} subset P(M)` agrees in letters, separators, tilde positions and inclusion direction apart from the individually reported alphabets.
- **`avec` and tilde-X definition:** `tilde X = {Y in M | Y ≤ X}.` agrees in all remaining tokens and terminal full stop. The M occurrence is individually reported.
- **Closing paragraph:** `Ainsi, F est interprété comme un ens. de parties dans M via (*), et ≤ s’interprète simplement par l’inclusion`. The family F and M alphabets are separately reported. `ens.` remains abbreviated. The final verb’s grave/circumflex ambiguity remains marked as in C; H has no local doubt mark. No strike was invented from the retraced initial s.
- **Final (1.32):** F ≤ G iff tilde F subset tilde G, with the printed label exactly (1.32). Ordinary F/G, tilde waves, the two-direction double implication, and the open subset were inspected; no further discrepancy was found.

## Completeness and mathematical scope

The report contains 37 substantive-locus rows, including one row per each of the 8 family-F occurrences, 13 M occurrences, and 2 power-set P occurrences; the alphabet rows also state local placement differences where relevant. There are 11 individually accounted-for C doubt loci. S.json is the empty array, so `s_rows` is correctly empty. The inventory contains 27 top-to-bottom elements and records every prose block, display, visible correction/insertion, enclosure/brace and page number. No independent marginal note or arrow-graph diagram is on this page.

The reading follows the author’s construction sufficiently to identify the two orders, the inclusions, the deployment set, the Fig family, and the asserted inclusion equivalence. It does **not** claim a proof check. The five `check_events` are explicitly “carried as background without fault found,” each with “read as the author’s assertion; no mathematical verification performed.” No proof, computation, or cross-page verification was performed. There is no authorial doubt/check phrase on this page.

## Structural validation and limits

JSON parses; all mandatory fields are present; required confidence/mark values, evidence-file existence, source boxes, inventory coverage, and view-log count were checked. LaTeX braces, dollar/display delimiters and environment pairing were checked structurally, and the control words were compared with the supplied PREAMBLE and permitted standard LaTeX/AMS/TikZ commands. No new macro is defined. **No LaTeX compilation or format build was attempted.**

The enlarged crops cannot create new source resolution. Typeface distinctions remain uncertain. The last verb’s accent remains unresolved where adjacent/preceding-line strokes intrude; no second crop or view was made. The second map’s single diagonal does not establish a correction history. The enclosure is described as open on the visible scan; no invisible right edge is supplied. The complete reading was persisted immediately after the crop pass and the main reader was notified before apparatus completion.
''')
(p/'audit.md').write_text(''.join(parts))
r['finished_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(p/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Audit written; report finished timestamp updated.')
