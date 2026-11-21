from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]; page='147_scan062'; c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B02':'The ornate crossed X has a transverse bar and central loop, with a separate peaked hat and dotted exclamation; M likewise has its hat and dotted exclamation. The loop does not securely decide calligraphic versus fraktur. Retain that alphabet doubt and the first formatting.',
'B03':'The four s subscripts0,1,infinity,lambda and final three t indices2,3,4 are distinct. The first t index is heavily reinforced and has a left spur/loop joining a thick upright; it can be1 or4. Add that uncertainty without deriving1 from the sequence. The detached final comma remains.',
'B05':'The second ornate X and M both carry hats and dotted exclamations. The shaft points right and the word échangeant is visible. The source-traced X alphabet doubt is not removed by the blind reader’s conventional calligraphic encoding.',
'B07':'The lower cancelled word has an initial small curved s/c group, a tall h-like stroke, a separate accent-like mark and final s return, favoring the first tentative schémas. The strike hides the internal bodies; relations/solutions is not separately established. Keep the existing doubt and the raised multiplicités replacement.',
'B08':'The focused crop extends above the original audit boundary and shows a complete peaked hat over the ornate X, independent of the neighboring line. The source thus settles hat presence, while the alphabet remains uncertain. Both M occurrences and0,4 indices agree.',
'B09':'The extended right-edge crop shows numéri- and the q descender followed by a compressed low tail at the sheet edge. Numérique is the favored word, but its last letters are not separately secure; add a single-word doubt. The76 reference and preceding words agree.',
'B10':'The small final digit of78 has a looped crossing below its upper dark turn, unlike the first7. Retain78. The arrow labelled1 crosses the divider, the left brace remains, and the segment starts visibly to the right of the left filled point in the2,2 graph; preserve that gap in the first drawing.',
'B11':'Trois has the crossed t, low r/oi and final s. The following p descends below the baseline, while its small ts group is written distinctly above its shoulder. Restore the raised ts placement as p-textsuperscript-ts, retaining the abbreviation.',
'B12':'The M hat and dotted exclamation,0,4 index, and words permutés transitivement entre eux all agree. Only exponent ordering differs.',
'B14':'The first M is bare above, with a dotted exclamation and an to its right. The U has its own an. Both low chi exclamations,2-2g-nu=-1, and paired vertical equality strokes above0 and3 are visible. Alignment/math wrappers only differ.',
'B15':'Hat-M with dotted exclamation/an and0,4, double-stroked P with1/an, and result2 agree. No reading change follows from the different alignment and exponent ordering.',
'B16':'Dense hatching above M begins with a hat-like angle and ends near a small lower dot. It does not securely exclude the first tentative cancelled exclamation, so retain the whole decoration doubt. The following overwritten glyph remains U/double-P; both removed sets show barred j first, then unbarred j. The expanded U has a small an superscript. Retain the first formula and its uncertainties.',
'B17':'The first set again has minus-bar-j then minus-j. After the later -1 the source has a smooth closing parenthesis and no comma before S4, rather than the blind closing brace/comma. The focused extreme-edge crop shows upper and lower tips of a separate large closing-parenthesis curve after S4, clipped by the paper edge. Keep that final parenthesis and the manuscript’s unmatched earlier delimiter.',
'B18':'The denominator favors24: a left2-like body and a right upright/crossbar survive. Its central loop and overwork do not isolate every stroke of an underlying6 or a separate cancellation. The blind deleted6/inserted24 is plausible but not certified; retain the first24/6 doubt and do not resolve it from the arithmetic.',
'B19':'The NB underline, On peut écrire directement, U with an and0,3, division colon, bracketed S4 and independent -1/24 agree. Only exponent ordering differs.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls=[('B03','t_1,t_2',r't_{\unsure{1|4}},t_2'),('B09','purement numérique',r'purement \unsure{numérique}'),('B11','aux trois pts',r'aux trois p\textsuperscript{ts}')]
for b,a,z in repls:d[b].update(changed=True,final=c[b]['first'].replace(a,z))
d['B09']['crop']=f'{page}_second_root_B09_ending.png'
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex'; t=p.read_text()
for _,a,z in repls:assert a in t;t=t.replace(a,z,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
row=next(x for x in r['changes'] if x['id']=='062-02');row['final']=row['final'].replace('t_1,t_2',r't_{\unsure{1|4}},t_2');row['evidence']+=' The comma decision remains high-confidence; the first index is separately qualified after the blind audit.'
r['changes'].append({'id':'062-20','place':'Prose below(78), raised ending of points abbreviation','C':'pts','H':'pts','final':r'p\textsuperscript{ts}','evidence':ev['B11'],'crop':f'{page}_second_B11.png','box':[665,1495,1138,1620],'confidence':'high','against_C':True,'against_H':True,'kind':'insertion or placement','marked_in_H':False,'error_sheet_kind':'insertions put in the wrong place','consequential':False})
r['doubts'] += [{'place':'First t subscript in four-section parenthesis','reading':r't_{\unsure{1|4}}','alternatives':'1;4','confidence':'low','reason':ev['B03']},{'place':'Line before(78), last word at right edge','reading':r'\unsure{numérique}','alternatives':'numérique; ending not fully separable at edge','confidence':'low','reason':ev['B09']}]
r['unresolved'] += ['First t subscript1/4, heavily retraced.','Numérique: compressed final letters at right edge.']
r['notes'][-1]='First-stage '+r['notes'][-1]+' The blind audit adds one substantive placement row for the raised ts in p-ts; two added doubts do not add C/H change rows.'
r['notes'].append('Blind audit: all fifteen differing boxes and three boundary-completion crops were personally viewed. The source confirms the X hat clipped by the initial crop and the two visible tips of the final parenthesis at the far right. The denominator remains unresolved; the blind suggestion of a cancelled6 followed by24 is not established well enough to encode a definite revision history.')
r['root_review_notes']=r.get('root_review_notes','')+' All fifteen differing boxes and three focused boundary crops personally viewed; raised ts restored and two certainty doubts added.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['62']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_{x}.png' for x in ('B08_hat','B09_ending','B17_edge')],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
