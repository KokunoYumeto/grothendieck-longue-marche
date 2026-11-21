from pathlib import Path
import json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan052'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E={
'B02':'The short old word is heavily crossed; low en-like fragments and an r/ch-like rise remain compatible with enrichi, but do not settle it. The visible candidate is retained as doubtful rather than discarded for an unreadable-word count. The raised à repères and Gamma agree.',
'B03':'The subset is a separate curved inclusion sign, and the loop on vector A has its sigma label. The old D-infinity is crossed so that single/double stem remains uncertain. The downward-arrow label has a closed oval with a short upper-right extension: o versus sigma is not fully separable and is now explicit. The cursive l, both sigma indices, plus, gamma and double-stem N agree.',
'B04':'After Gr. the p descender leads directly to the n arch and tall d, with no separate intervening o loop. The literal abbreviation pndrep is retained. Both readings identify the underline and surrounding parentheses.',
'B05':'The three handwritten capital forms, lowered star, top subscript, raised plus/minus and ordinary arrow agree. S and D are the recurring capital forms represented by the established S/calT/D convention; changing all three to calligraphic font does not establish another source symbol. No dot separates Gr from pondrep here.',
'B06':'The word begins with a compact i stroke, then low m arches, a p descender, small o/r group, tall t, and the n/t/e ending. It is one importante, not groupoïde followed by et. The terminal e is retained.',
'B07':'The left word has the d/e/s/c/r sequence, a p descender, tall t and dotted i; the second has a tall t followed by the r/a/d/u/c/t sequence. A separate hyphen joins description-traduction. The proposed segmentation as les/des critères et des choix does not fit these ascenders and descenders.',
'B08':'The overlapping S and looped T, separate D, raised plus/minus and lowered top are all visible. The differing alphabet wrappers are resolved by the same local S/calT/D convention used in B05 and B13.',
'B09':'The inserted abbreviation has gr followed by a distinct point, then poïde and a separate short terminal dash. There is no written ou sequence to expand it to groupoïde. The lower la and catégorie are both traversed by the cancellation.',
'B10':'A separate accent stroke is present above the opening ré group. Before à is a tall open parenthesis. The last word has the long q descender and an es ending with a terminal downward s turn, so uniques remains plural. Isom. retains its visible point.',
'B11':'The article is singular le, and the underlined phrase and final correspondant agree. A compact dark point is visible at the right boundary after the t; although the boundary limits its exterior edge, its presence is established.',
'B12':'A separate horizontal dash precedes plus précisément; both transcriptions represent that same single mark. Triple-hyphen TeX syntax supplies the dash glyph, not three source strokes. The insertion and remaining wording agree.',
'B13':'Canonique, lowered star, top, raised plus/minus and the target with Gr., pond. and rep. points agree. The same S/calT/D font convention is retained consistently, without changing any source symbol.',
'B14':'The small mark before valeurs has an upper dot/stroke and a compact lower mark; it can be the author’s reduced à or colon, so both remain explicit. The parenthetical has et non seulement, le foncteur, dans and two closing parentheses. There is no extra dot in Grbipond; line-break differences alone are not a reading change.',
'B15':'The circled 1 and complete underlined heading agree. The following context has a separate accented capital A, low un, then the o/b/j/e/t pattern including a tall b and final t. It reads À un objet, not rien de plus.',
'B17':'The lower-left annotation has the upper bar and lower curve of 5, then the sloping entry and upright of 1. The mspage wrapper records the folio 51, not a new marginal prose note.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,a,z in [('B03',r'\arrow[d,"o"\']',r'\arrow[d,"\unsure{o|\sigma}"\']'),('B14','foncteur à valeurs',r'foncteur \unsure{à|:} valeurs')]:
 # The apostrophe is literal in tikz-cd label placement.
 a=a.replace("\\'", "'");z=z.replace("\\'", "'")
 assert a in s and a in C[b]['first'],(b,a)
 s=s.replace(a,z);D[b].update(choice='reading',reading=C[b]['first'].replace(a,z))
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
r['doubts'] += [dict(place='Initial diagram, downward-arrow label',reading=r'\unsure{o|\sigma}',alternatives='o; sigma',confidence='medium',reason=E['B03']),dict(place='Inserted parenthesis, before valeurs',reading=r'\unsure{à|:}',alternatives='à; colon',confidence='medium',reason=E['B14'])]
r['notes'].append(dict(id=p+'-N-audit',text='Blind crop comparison confirms importante, description-traduction, the literal missing o in Gr.pndrep, abbreviated gr.poïde-, plural uniques and the continuation À un objet. The downward-arrow label o/sigma and the reduced à/colon before valeurs remain explicit uncertainties. These two uncertainty-only changes add no witness-error rows.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
