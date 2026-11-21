from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan073'
ev={
'B01':'The M roof, separate raised upright/dot, lower genus alpha and hatted nu alpha are all present. The wording agrees; different math wrappers and script ordering are equivalent.',
'B02':'The first accent has retraced lower/side strokes unlike the clean two-arm roof on the next M. Preserve the canceled-wedge/tilde uncertainty rather than replacing it with an unqualified hat. Infinity, G indices, equality and set-minus agree.',
'B03':'The canceled word exposes the d ascender and terminal x-like crossing, but the strong horizontal cancellation merges the internal e/u bodies. Retain deux as the candidate under whole-word doubt. The neighboring hatted M, bang, hatted nu and live il y en a au moins agree.',
'B04':'The literal dimension inequality has a greater-than angle and separate lower equality bar, followed by1. The alpha and prose agree; ge/geq and math wrappers are equivalent.',
'B05':'The empty-set form has a small high closed loop on a long oblique stem extending well below it. Retain phi, the established drawn form, rather than replace it by the conventional empty-set glyph. The infinity and hatted nu indices, crossed inequality and closing punctuation agree.',
'B06':'The inserted M lies just below the f descender; short slanting traces could form a roof but are not securely independent of that descender. Keep the hatted/bare-M alternatives and the separate insertion guide. Avec has four low joined groups and stays live and readable.',
'B07':'The small formula reads3g−1)+nu=2 with an unclear possible opening curve; do not supply an unqualified missing parenthesis. The initial letter of DPS has an upright and single right bowl, unlike S. The final N≥3 and period agree. The formula is retained as written under the existing whole alternative.',
'B08':'The leading coefficient before g is overworked at the insertion guide, with both2/3 contours plausible. The possible opening parenthesis is also overlapped. Preserve both uncertainties, the closing parenthesis, nu and ≥2; the expected dimension formula does not settle the ink.',
'B10':'The i in chaine has a single small dot and clear paper above it, without a two-arm circumflex. Retain the local unaccented spelling. The two-line wording otherwise agrees.',
'B11':'After eux the low stroke is the reduced initial a of aussi, followed by the u/s/s/i run; no independently separated hyphen lies between the words. Keep eux aussi and the surrounding full wording.',
'B13':'The loop, three filled vertices overall, genus labels, I labels and two braces agree. The live lower segment starts after a small white gap to the left dot. The canceled patch contains many zigzag returns and two long diagonals, not just three lines; g prime remains a doubtful buried suggestion. The first canceled inequality’s I-prime area meets the upper inserted g-double-prime descender and strike, so qualify that prime. The first canceled bound2 remains doubtful. The final live2 was inspected at the image edge: its curved head, descending stroke and lower return remain identifiable, so retain it. The literal g prime+g double prime=0 is not regularized.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
d['B03'].update(changed=True,final=first['B03'].replace(r'\deleted{deux}',r'\deleted{\unsure{deux}}'))
a=r"\deleted{2g'+\operatorname{card}I'\geq\unsure{2}}";b=r"\deleted{2g'+\operatorname{card}I^{\unsure{\prime}}\geq\unsure{2}}"
assert a in first['B13'];d['B13'].update(changed=True,final=first['B13'].replace(a,b))
p=w/'pages'/f'{page}.tex';t=p.read_text()
for k in ['B03','B13']:
 assert first[k] in t,k;t=t.replace(first[k],d[k]['final'])
p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
r['doubts'].extend([
 {'place':'Canceled deux, third main baseline, blind B03','reading':r'\deleted{\unsure{deux}}','alternatives':'deux; obscured internal letters','confidence':'medium','reason':ev['B03']},
 {'place':'First canceled inequality in90b, I prime, blind B13','reading':r'I^{\unsure{\prime}}','alternatives':'prime; overlapping insertion/cancellation stroke','confidence':'low','reason':'The expected prime lies where the inserted g-double-prime descender and cancellation meet. It cannot be isolated confidently, although the I body is readable.'}
])
r['inventory'][2]['first_words_or_objects']=r'\unsure{deux}'
for x in r['inventory']:
 if a in x.get('first_words_or_objects',''):x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
r['notes'].append('Blind audit: the main reader viewed all eleven differing boxes. The crossed deux and the prime on I in the first canceled inequality acquired certainty-only qualifications. The final live2 was checked at the sheet edge and retained. The literal dimension irregularities, DPS, long-stem phi, unaccented chaine, eux aussi, graph gap and g-prime+g-double-prime=0 remain. The audit did not add a new proof or alter any earlier check-event classification.')
r['root_review_notes']=r.get('root_review_notes','')+' All eleven differing blind boxes checked; two certainty changes under cancellations. Final edge2 personally inspected on an additional crop.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['73']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_second_root_B13_end.png'],'extra_boxes':{'B13_end':[1520,2195,1692,2335]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
