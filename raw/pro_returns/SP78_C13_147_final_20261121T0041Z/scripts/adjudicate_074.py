from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan074'
ev={
'B01':'The ink number36 and du cas are retained. The difference is only the math wrapper around a).',
'B02':'The upper b-like glyph has overlapping ascending strokes, so its cancellation state remains uncertain. The lower a-prime is clear. The loop, two filled vertices, white gap at the left end of the lower edge, and repeatedly hatched upper arc are visible. The right-hand conditions are unbraced. No independent canceled I2 before the doubtful quelconque is established; the lower canceled line remains a whole uncertain candidate.',
'B03':'Both live formulas and the inserted on a card I2≥2 are legible. The crossing obscures the canceled word and lower line; retain their existing whole uncertainties rather than the blind reader’s more definite alternative phrases. The empty-set signs have long-stem loop forms, retained as phi.',
'B04':'The compressed initial capitals support NB. The first capital of OPS is a closed round loop, unlike a separate S or upright D. Pourvu que g≥2 is lower left; the partition clause follows to the right. The dot after quelc. is visible, but no independent semicolon after2 or terminal period after I appears.',
'B05':'The si dot, low on-like bodies and two descending p strokes support the existing si on suppose candidate. The horizontal strike merges their upper bodies, so the whole phrase remains doubtful. The separate g-prime is clear.',
'B06':'The oval returns to the left of two filled vertices; the joining edge meets both. Immediately above the left dot the loop has a short left/downward stub, retained in the first drawing. The I-prime/I-double-prime and g-prime−1/g-double-prime labels agree.',
'B07':'Donc si g≥1 and de sorte que le cas a) existe agree in the ink. Only math wrappers differ; the closing parenthesis has no following comma.',
'B08':'The canceled low word remains an uncertain avec candidate before the clear g-prime not-equal trial. In the live noun the compressed low beginning, short ascender, taller crossed t and i dot support notations, but do not separate all its internal letters securely. Qualify the word rather than assert entiers or conditions. No separate de follows.',
'B10':'The abbreviated éch. ends with a detached dot. A separate loop and long returning descender, crossed horizontally, follow it before the clean g-prime/g-double-prime pair; retain that doubtful canceled g. The inserted b-prime)=a-prime) and its guide are present. The abbreviation is not expanded to échanger.',
'B11':'The main wording, crossed Si g, genus-zero condition and raised donc card I≥6 agree. The guide places the latter at the end of that clause. The differences are only wrappers around the case labels.',
'B12':'The canceled upper abbreviation has a rounded first body but remains overlapped, so keep OPS uncertain. The lower cancellation includes a separate first a-like body before il y a. The live Or on a is above that canceled baseline beside the earlier crossed phrase: mark it as an insertion. Its O/r and low on/a bodies are distinct.',
'B13':'The canceled first word has a descending p-like loop and stays an uncertain pour candidate. At the first comparison, a short lower slanted stroke is visible, but the long cancellation coincides with the angle and prevents deciding ≥ versus >; qualify that relation. The later ≥3 is distinct. The spanning qui a donc candidate and punctuation remain uncertain. The sketch’s two large crossing paths cover labels and prose, but the lower two-point edge itself remains uncrossed and starts after a white gap.',
'B14':'The two large cancellation paths, crossed case label and upper I labels are distinct from the lower two-point edge. Its left end has a white gap. The small overworked lower glyph remains a doubtful g candidate. Do not cancel every stroke of the sketch or replace its crossing paths by a single deletion wrapper.',
'B15':'Ten explicit vertex marks are visible; the one above the literal b-minus1 label is open. There is no separate ell in that index and no upper weight above a_(k−1). The a_k label lacks enclosing parentheses. The local edge gaps, left continuation dots/stroke, right continuation dots and lower wave, and the two braces are retained. The right caption’s sign and final overwritten I-double-prime remain doubtful.',
'B16':'The left caption has five physical rows and no detached comma after segments. Its final plus has an independent crossing upright and its I-prime is clear. Preserve the row layout and wording.',
'B17':'The right caption has no added commas. The sign before ell is mostly horizontal with a dark center, without an independently clear upright like the left caption’s plus; keep minus/plus uncertainty. The final I-double-prime is overworked, so its existing doubt remains.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls={
'B08':('les notations',r'les \unsure{notations}'),
'B12':('Or on a',r'\inserted{Or on a}'),
'B13':(r"\operatorname{card}I'\geq\operatorname{card}I''",r"\operatorname{card}I'\unsure{\geq|>}\operatorname{card}I''")}
p=w/'pages'/f'{page}.tex';t=p.read_text()
for k,(a,b) in repls.items():
 assert a in first[k],k
 d[k].update(changed=True,final=first[k].replace(a,b))
 assert first[k] in t,k
 t=t.replace(first[k],d[k]['final'])
p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
r['changes'][23].update(final=r'\unsure{notations}',confidence='medium',evidence=ev['B08'])
r['changes'][30].update(final=r'\inserted{Or on a}',against_C=True,evidence=ev['B12'])
a,b=repls['B13']
for x in r['changes']:
 x['final']=x['final'].replace(a,b)
r['changes'][32]['evidence']+=' The first comparison now carries ≥/> uncertainty because the cancellation overlaps its central and lower strokes; this does not change the established canceled state.'
r['doubts'].extend([
 {'place':'Live noun after les, blind B08','reading':r'\unsure{notations}','alternatives':'notations preferred; compressed internal strokes','confidence':'medium','reason':ev['B08']},
 {'place':'First relation in canceled cardinality trial, blind B13','reading':r'\unsure{\geq|>}','alternatives':'greater-or-equal; greater-than','confidence':'low','reason':ev['B13']}
])
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
r['inventory'].append({'scan':74,'sheet_kind':'text','hand':'his hand','element':'33','kind':'insertion','position':'Above canceled a il y a, beside crossed et OPS','first_words_or_objects':r'\inserted{Or on a}','transcribed':'yes'})
r['notes'].append('Blind audit: all sixteen differing boxes were inspected by the main reader. Or on a is now explicitly marked as a raised insertion above the canceled restart. The compressed notations candidate and the first canceled cardinality comparison acquired certainty qualifications. The open vertex, literal b_(-1), missing upper weight, unparenthesized a_k, edge gaps, loop stub and uncertain right-caption minus/plus remain as drawn. No new mathematical check was claimed.')
r['root_review_notes']=r.get('root_review_notes','')+' All sixteen differing blind boxes inspected; one placement correction and two certainty qualifications. Extra crops inspected the compressed noun and canceled first relation.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['74']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_second_root_B08_word.png',f'{page}_second_root_B13_relation.png'],'extra_boxes':{'B08_word':[1350,880,1605,977],'B13_relation':[420,1570,970,1690]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
