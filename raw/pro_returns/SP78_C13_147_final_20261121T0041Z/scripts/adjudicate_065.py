from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan065'
c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'The opening M has no surrounding class brackets. All five fractions, the two primes and point indices agree; the second reading differs only in display syntax.',
'B02':'The paired E upright, the two minus signs before S0/S1, both plus signs before a2/a3 and both plus signs on the T(1) line are visible. Flattening the two lines changes no reading.',
'B03':'The source has où, a separate de, a long descending f in façon, the looped g and tall l of générale, then the short on and descending p of pose. Retain où de façon générale on pose, rather than the blind alternatives.',
'B06':'The zeta subscript p, doubled Zs and i with a low p! are visible. The bang has a distinct dot below its short upright. The mathematical reading agrees.',
'B07':'The separate où stands at the far left and is retained. The three low exclamation marks and the distinction Z_p/Z agree. A focused endpoint crop shows the shaft ending in a dark rounded dab with an upward return, without separately readable arrow arms. The probable rightward arrow is therefore marked uncertain rather than certified from the map context.',
'B09':'The prime on S0 is a separate raised stroke; the two a terms and both zeta terms are preceded by minus signs. Retain the first aligned-row encoding.',
'B10':'The prime and subscript1 are distinct, and all four minus signs agree. Only wrappers/alignment differ.',
'B11':'The sign before zeta3 is a short horizontal stroke with a tiny retraced loop but no independent long vertical. Minus remains preferred; the loop still prevents a categorical exclusion of plus. The crossed mark after1/4 has an angular upper return, a descending stem and a lower crossing, making4 a better tentative reading than plus; the crossing prevents certainty, so retain both candidates. The live plus before1/6 is separate. The brace and5/12 are above the parenthesis, and the lower24/12 denominators agree.',
'B12':'The source writes7/12 with a slash. The canceled mark after it has merged upper loops and a descending angular return: zeta remains possible, while4 is also admitted. The next fraction has an overworked upright numerator and two-loop denominator; retain the whole-fraction1/8 doubt. The later1/6 is clear.',
'B13':'The rewritten line has one half(T(1)-1), then minus1/12, plus1/8 zeta2 and plus1/6 zeta3, followed by a separate comma and donc. Their placement agrees with the first reading.',
'B14':'The left number80, two-row brace, bare M in the first row, independent hat in the second, and all displayed fractions/indices agree. No additional class bracket or exponent is supplied.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls={
'B07':(r'\longrightarrow',r'\unsure{\longrightarrow}'),
'B11':(r'\deleted{\unsure{+}}',r'\deleted{\unsure{4|+}}'),
'B12':(r'\deleted{\unsure{\zeta}}',r'\deleted{\unsure{\zeta|4}}')}
for b,(a,z) in repls.items():
 assert a in c[b]['first'];d[b].update(changed=True,final=c[b]['first'].replace(a,z))
d['B07']['crop']=f'{page}_second_root_B07_endpoint.png'
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for a,z in repls.values():assert a in t;t=t.replace(a,z,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
row=next(x for x in r['changes'] if x['id']=='065-13')
row.update(final=d['B11']['final'][d['B11']['final'].find(r'\frac14'):d['B11']['final'].find(r'\right)')],against_C=True,evidence=ev['B11'],crop=f'{page}_second_B11.png')
row=next(x for x in r['changes'] if x['id']=='065-14');row['final']=row['final'].replace(*repls['B11'])
row=next(x for x in r['changes'] if x['id']=='065-15');row.update(final=row['final'].replace(*repls['B12']),evidence=ev['B12'],crop=f'{page}_second_B12.png')
for x in r['doubts']:
 if x['reading']==repls['B11'][0]:x.update(reading=repls['B11'][1],alternatives='Canceled4 preferred; plus remains possible.',reason=ev['B11'])
 if x['reading']==repls['B12'][0]:x.update(reading=repls['B12'][1],alternatives='Canceled zeta or4.',reason=ev['B12'])
r['doubts'].append({'place':'Map between the two K groups, right endpoint','reading':r'\unsure{\longrightarrow}','alternatives':'Probable rightward arrow; head is contracted into a rounded ink dab.','confidence':'low','reason':ev['B07']})
r['unresolved']=[x.replace('remains tentatively plus; its original strokes are obscured.','is now4|+, with4 preferred; its crossed strokes do not settle it.').replace('remains tentatively zeta; its original letter is not plain.','remains zeta|4; its original character is not plain.') for x in r['unresolved']]
r['unresolved'].append('The K-group connection has a blunt rounded endpoint; rightward arrow is retained only under a doubt mark.')
r['notes'][1]='The manuscript defines zeta_p=[Spec Z/pZ]=i_p!(1), with all four Z glyphs double-stroked. Its displayed K-group connection is probably a rightward arrow, but the focused blind-audit crop shows a dark rounded endpoint without separately readable arms; the arrow is now marked uncertain. The precise geometric formalism and Z_p notation are not independently reconstructed.'
r['notes'][8]='After the blind audit there are16 substantive comparison rows:6 against C and11 against H. M1043 remains undecided; the sign comparison is not a proven H error. Five doubtful places are recorded, including the newly qualified connection endpoint. Changing the canceled coefficient mark from tentative plus to4|+ changes its preferred reading; the other new alternatives are certainty changes.'
r['notes'].append('Blind audit: all eleven differing boxes and the focused connection endpoint were personally viewed. The canceled mark after1/4 is now4|+, the later canceled mark zeta|4, and the rightward map symbol is qualified. Minus remains preferred at M1043 but its small loop still leaves plus possible. Conditional arithmetic from the first pass is unchanged and does not settle the sign.')
r['witness_comparison']+=' Blind audit qualifies the rounded arrow endpoint, favors a canceled4 over plus while retaining both, and admits4 beside the tentative canceled zeta. M1043 remains unresolved.'
r['root_review_notes']='All eleven first-pass crops and all eleven differing blind boxes were personally viewed, with a focused endpoint crop. The three changes affect the arrow certainty and the two canceled-character candidates. M1043 and the overwritten fraction remain doubtful; no arithmetic normalization was made.'
for x in r['notation']:
 x['reading']=x['reading'].replace(*repls['B11'])
for x in r['inventory']:
 for a,z in (repls['B11'],repls['B12']):x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['65']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B07_endpoint.png'],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
