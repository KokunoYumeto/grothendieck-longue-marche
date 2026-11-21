from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan075'
ev={
'B03':'The abbreviation after premiers has a low e curl, tall l and a short oblique accent stroke at its upper left, followed by a detached comma. It differs from the following et, whose t has a more extended transverse stroke. Retain él without expansion. The raised défini and transposition, baseline mod and crossed interversion agree.',
'B04':'The d/e loop, long f and two dotted i strokes support définissent, but the densely retraced final group does not separate all the s/e/n bodies. Qualify that live word. The following canceled une remains a tentative whole word; the last e is not secure enough to resolve un/une.',
'B05':'The M infinity formula, low une group, literal equality mark and composante connexe agree. The complete suffit de is raised and its guide enters before montrer. The dots and ascenders in the following ordres totaux déduits clause support the first reading.',
'B06':'Transposition des deux is on the raised interline; the labels and preceding overworked epsilon/membership-shaped mark occupy the next level, with élts consécutifs continuing below. Keep that attachment and word order. The short des has its terminal s return. The abbreviation has l/t and a short s, without a distinct m or full éléments. The overworked symbol remains unresolved; both literal equality strokes remain.',
'B07':'At the line end the descending q is followed by an elision mark and a low on group; retain qu’on, not just que. Or on le voit en notant and the preceding connexe. agree.',
'B08':'The tiny initial a is followed by deux. The final noun begins with a looped g descender and accented e/n/e sequence, not an s/p cluster. Retain générisation, even though the blind reading proposed spécialisation.',
'B09':'The lower d loop and short e-like ending lie under a thick strike. Retain the existing whole-word uncertainty on de. The replacement dans is written above and has its full low a/n/s continuation.',
'B10':'The first drawing has six explicit vertex marks, multiple small white gaps, two short continuation strokes and a curled final endpoint with a dark upper body. Those contours are retained instead of a straight continuously joined chain. Its paired c labels and indices agree; isolated C/c stays uncertain.',
'B11':'The ending after the dotted i has one low e/n run leading to a final t, with no additional n/e/n sequence. Retain the written singular provient de without grammatical regularization.',
'B12':'The third written label has a short horizontal minus before1, not the distinct plus of the lower drawing. Preserve the literal repeated c_(i−1). The fourth operator is darkened and remains minus/plus doubtful. Four main points, the extra small lower dot, local gaps and irregular continuation marks are visible.',
'B13':'The lower drawing’s second label has the independent upright of plus1; the third is c_i and the fourth has plus2. Four main points, local gaps and unequal short continuation strokes are retained, not a continuous dotted schematic.',
'B14':'The second c index has a very small mostly horizontal wedge with an overworked center; keep minus/plus doubt. The clear plus in the earlier paired label or lower drawing cannot supply its upright. The canceled seg candidate, raised arête with accent, joint, comma and OK. agree.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
d['B04'].update(changed=True,final=first['B04'].replace('définissent',r'\unsure{définissent}'))
p=w/'pages'/f'{page}.tex';t=p.read_text();assert first['B04'] in t;t=t.replace(first['B04'],d['B04']['final']);p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
r['doubts'].append({'place':'Live verb before canceled une, blind B04','reading':r'\unsure{définissent}','alternatives':'définissent preferred; compressed ending','confidence':'medium','reason':ev['B04']})
r['unresolved'].append('The live définissent candidate has a densely retraced ending and remains qualified after the blind audit.')
r['notes'].append('Blind audit: the main reader viewed all twelve differing boxes, and a focused crop of él. The live définissent was qualified because its ending is densely retraced. The raised insertion order, epsilon/membership uncertainty, qu’on, générisation, singular provient, graph gaps and endpoint curl, literal repeated c_(i−1), and local minus/plus doubts were retained. This was an ink audit, without a new proof of the geometric claims.')
r['root_review_notes']=r.get('root_review_notes','')+' All twelve differing blind boxes inspected. One certainty-only change qualifies définissent; the short accented él was also inspected on a focused crop.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['75']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_second_root_B03_abbrev.png'],'extra_boxes':{'B03_abbrev':[1460,240,1580,330]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
