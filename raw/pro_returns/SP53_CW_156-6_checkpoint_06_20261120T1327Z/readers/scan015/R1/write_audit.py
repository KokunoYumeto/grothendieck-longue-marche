from pathlib import Path
import json
from datetime import datetime,timezone
O=Path('/workspace/scratch/8db4dde48936/sp53_recovery/out/readers/scan015/R1')
r=json.loads((O/'report.json').read_text())
# Remove Python raw-string escapes used only to delimit French apostrophes.
def clean(v):
 if isinstance(v,str): return v.replace("\\'", "'")
 if isinstance(v,list): return [clean(x) for x in v]
 if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
 return v
r=clean(r)
plan=json.loads((O/'crop_plan.json').read_text())
results={
1:'Family F is certain; exact mathcal/fraktur typography remains open.',
2:'definit: no separate acute above e; the tall stroke is f.',
3:'Canceled M is resolved against F; its two peaks and rounded trough remain beneath the strikes. Typography is still mathcal/ordinary M.',
4:'Live M repeats the two peaks, rising entry and rounded trough, supporting the same alphabet treatment.',
5:'Retain family F/barred-f doubt: the detached cap and small crossed lower stem remain compatible with both.',
6:'Literal (1.25); no closed lower bowl of a 6. No mathematical correction to the reference.',
7:'Current (*) is readable; long/retraced strokes do not reveal a separate predecessor. No cancellation is invented.',
8:'Ornamental P, not plain roman; mathcal/script/fraktur typeface still underdetermined.',
9:'X is readable below the live F: both oblique arms remain. H’s explicit note is credited.',
10:'Dep, with a descending-loop p; no acute and no final l.',
11:'Inserted alors, followed by unaccented definie. The large upper curve is the insertion indicator, not an acute.',
12:'Current (**) is readable; no independent previous symbol is separable despite retracing.',
13:'A long extra oblique is clear, but not a complete second X. Explicit canceled-X/live-F state alternatives retained.',
14:'s’interprète preferred at medium confidence: one faint oblique accent, without a second joined circumflex leg. Adjacent-line ink is separated.'}
lines=['# scan015 — independent R1 audit','',
'## Scope and permitted material','',
'I read only the assigned scan015 packet (brief v007, notation table, inputs, C, H, C context, and S), the supplied C PREAMBLE and H convention file, and the permitted crop script’s usage/source. S is an empty array. I did not inspect another reader, another page, an external transcription, OCR output, PDF text, or web material. I did not spawn readers. Every image claimed below was emitted with `tools.view_image`; source images were not opened again after the required pass. Writes are confined to `out/readers/scan015/R1`.','',
'## Image sequence','',
'1. Whole page, once, for layout: handwritten page number 14; opening text; enclosure and offset brace/gloss; ordinary display formulas; several correction/overwriting loci; one inserted word; final paragraph and equivalence. No independent margin note, date, archive pencil number, or geometric illustration was seen.',
'2. Supplied half_a, once, line by line against C and H.',
'3. Supplied half_b, once, line by line against C and H. The supplied halves themselves overlap; I did not request an additional half view.',
'4. Fourteen unique tight crops, each emitted once in numerical order. There were no re-crops or repeat crop views.','',
'| Image role / filename | Emitted UTC |','|---|---|']
for v in r['view_log']:
 lines.append(f"| {v['role']}: {Path(v['image']).name} | {v['viewed_utc']} |")
lines += ['', '## Open loci after the half-page passes','',
'The halves settled the main prose and all nine displays, the omitted opening de in H, the two distinct single underlines, the enclosure’s open right edge and left-corner gaps, the offset gloss/brace, ordinary versus family F identity, every repeated M/P occurrence’s local shape, centered order labels, the hook and mapsto geometry, the two-point colon after (1.4), the struck old (1.32), and terminal punctuation. All half-settled differences receive tight original-source coordinates in report.json. Exact typographic alphabets remained underdetermined at their first occurrences.',
'',
'The remaining crop list was fixed before any crop was viewed: first family F; definit accent; the canceled letter after definit; first live M typography; the fourth order label; the digit of (1.25); the irregular (*) label; first P alphabet; first overwritten X; Dep/Def/Dépl; the insertion alors/donc together with the adjacent defining-verb accent; irregular (**); the second possible overwritten X; and the final s’interprète/s’interprête accent. The two adjacent accent/insertion questions share one adequate local crop. The first live M and canceled M crops address separate written occurrences.','','## Crop transforms and decisions','',
'All crops were made by the supplied script: crop at the listed source coordinates; rotation **0°**; autocontrast; unsharp mask (radius 1.2, percent 120, threshold 3); enlargement to **2800 px across** by LANCZOS; JPEG quality **95**. Existing evidence was never overwritten. `a` and `b` below are the supplied full-resolution half_a and half_b images, respectively; each is 1681 × 1260 pixels. The b coordinates are local to half_b (whose top corresponds to whole-page y=1100).','',
'| Crop | Source and box (left, top, right, bottom) | Output px / linear scale | Why needed and decisive result |','|---|---|---|---|']
for p in plan:
 n=int(p['name'][:2]);x0,y0,x1,y1=p['box'];w=x1-x0;h=y1-y0;out_h=round(h*2800/w);scale=2800/w;src='a' if p['source'].endswith('_a.jpg') else 'b'
 lines.append(f"| {p['name']}.jpg | {src}: {p['box']} | 2800 × {out_h}; {scale:.3f}× | {p['reason']} {results[n]} |")
lines += ['', '**Actual crop count: 14. Actual image emissions: 17 (one whole, two halves, fourteen crops).**','',
'## Line-by-line comparison record','',
'| Page segment | Comparison with both witnesses and outcome |','|---|---|',
'| Header and opening two lines | Page 14 is present. The ornate family F carries the first alphabet doubt. C preserves c’est **de** la; H drops de. résumé, donnée, and the independent underlines on relations and d’ordre were checked locally. |',
'| (1.30) row | Both order signs, comma, telles que, two ordinary F, two ordinary G, ≤ and ≪, and the right double implication agree in content. Both witnesses close the box; the scan shows only three sides reaching the right paper edge. H correctly notices the enclosure. |',
'| Gloss beneath (1.30) | rel. d’ordre dans and its final family F are present; the abbreviation remains rel. The brace above this gloss is offset to the right, with its cusp between the second sign and telles. H’s note is credited for the below-row gloss and brace, while the actual geometry is recorded. The family-letter alphabet disagreement is a separate occurrence row. |',
'| que je vais partir. | Both witnesses match; the final point is visible. |',
'| En termes de celles-ci, on definit and canceled letter | The verb has no independently inked acute. The canceled letter resolves as M, with alphabet uncertainty kept separately. C’s candidate F is not supported by the two-peak structure. H recognizes cancellation. |',
'| M ⊂ F | Both identities and the open subset relation agree. C’s M alphabet and H’s family-F alphabet differ from the first-candidate readings; both occurrences receive rows. |',
'| par (1.20), avec les relations ... induites | Literal reference, comma, avec, les relations and induites checked. H’s genuine uncertainty on avec is resolved. The two M labels sit centered beneath their signs; C uses ordinary M and H lower-right placement. |',
'| par ... puis and L ⊂ M | Both centered family labels and comma/puis are present. The fourth label retains F/barred-f alternatives. L is the calligraphic L in both witnesses; the final M is another individual alphabet row. |',
'| par (1.25). L’application | The crop supports a literal final 5. The period and apostrophe are present. H’s editorial claim about (1.26) elsewhere is not treated as manuscript ink or checked on another page. |',
'| (*) application | Current label (*) is retraced; no readable predecessor is invented. The hook, family source, ornamental P, M argument, overlaid X/F source, mapsto, tilde F, equality, literal Dep and (F) are all read. C’s X uncertainty and Dep/Def doubt resolve; H’s explicit canceled-X note is credited. Each alphabet occurrence has a row. |',
'| est [alors] definie par | The inserted word reads alors, against H’s donc. No separate acute can be isolated over the e of definie; the large curve is the insertion indicator. |',
'| (1.31) | Label, tilde F, equals, opening/closing braces, X ∈ M, single separator and X ≤ F agree. Only the recurring M alphabet differs from C. |',
'| et and (**) application | et is present. Current (**) is readable, with no independent prior symbol assignable. Source family F, hooked arrow, Fig(M), mapsto and Fig_M(F) checked. The extra oblique at the live F source is not enough to settle a whole canceled X, so the state alternatives are shown explicitly. |',
'| par (1.4) : and old label | Both colon points are visible; H omits them. The old (1.32) is visibly canceled at the left of the next formula; H’s struck state is credited, and mere macro placement is not counted as a new disagreement. |',
'| Fig_M(F) set formula | Capital Fig, subscript M, ordinary F, equality, braces, tilde X, single vertical separator, X ∈ tilde F, open subset and final P(M) checked. M, P, M have individual alphabet rows. |',
'| avec and tilde X definition | avec, tilde X, equality, braces, Y ∈ M, separator, Y ≤ X and final point agree. The M alphabet gets its own row. |',
'| Ainsi paragraph, three manuscript lines | Ainsi, family F, est interprété comme un ens. de parties dans M via (*), et ≤, s’interprète simplement par l’inclusion read throughout. ens. keeps its point; the asterisk reference is not doubled. Family F and M get separate rows. C’s final accent doubt resolves to a preferred grave at medium confidence. |',
'| Final (1.32) | F ≤ G, two-way double arrow, tilde F ⊂ tilde G and label (1.32) match in visible content. No terminal point is visible. |','',
'## Completion, checks, and limits','',
'The complete draft reading.tex was persisted immediately after the fourteen crop views, and the main reader was notified before the report was finished. report.json contains 36 substantive difference loci, all 11 unique C doubt loci, an empty S-row array because no S rows were supplied, 27 inventory entries, five unresolved matters, full notes, and the actual view log. The alphabet report is occurrence-specific: eight family-F occurrences, thirteen M occurrences including the canceled one, and two P occurrences. The ordinary F and G operands were inspected and left unchanged where both witnesses match the ink.',
'',
'Only visual/structural verification was performed. The mathematical statements were read as the author’s assertions; no targeted proof check, re-proof, computation, formal certificate, or cross-page validation was performed. check_events records only this background status. No LaTeX compilation or format build was attempted. Structural checks cover JSON/schema fields, crop-file existence, balanced braces/math delimiters/environments, and absence of new macro definitions.',
'',
'The exact handwritten font families remain underdetermined despite clear letter identities. The detached fourth label and the second map’s correction history remain explicit uncertainties. The final s’interprète accent is faint and is resolved only at medium confidence. Enlarging the supplied raster cannot recover lost stroke detail. The decorative frame and brace are reproduced as inline TikZ within the mathematical display; they are not an independent geometrical illustration. No further image inspection was performed after the fixed crop pass.',
'']
(O/'audit.md').write_text('\n'.join(lines))
r['finished_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(O/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('audit.md saved; report apostrophes normalized; finished_utc updated.')
