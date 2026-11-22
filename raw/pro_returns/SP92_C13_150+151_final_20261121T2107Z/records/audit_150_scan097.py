from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan097';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[(r'i_0,..,i_n',r'i_0,\mathord{\cdot}\mathord{-},i_n'),(r'i_0..i_n',r'i_0\mathord{\cdot}\mathord{-}i_n'),(r'J_0\ldots J_n',r'J_0\mathord{\cdot}\mathord{-}\mathord{\cdot}J_n'),(r'\prec..\prec',r'\prec\mathord{\cdot}\mathord{-}\prec'),(r'(\overset h\sim)',r'\overset h{(\sim)}'),(r'$\overset{?}{\text{alors}}$ on a',r'$\overset{?}{\text{alors}}$ \unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}'),('marche-\\\\\nront','marche-\\\\\nraient')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert a in s,a;s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id'] in ['C01','C02','C03','C15','C16','C20','C22']:x['evidence']='The continuation has one small point followed by a longer horizontal rule, not two typographic dots or three dots. All surrounding indices and punctuation remain as transcribed.'
 if x['id'] in ['C17','C27','C29','C30']:
  x['against_C']=True;x['evidence']='The h stands above the short parentheses enclosing the wave. The parentheses do not enclose h at their own height. The hooked map and its right arrowhead remain as transcribed.'
 if x['id'] in ['C09','C10']:x['evidence']+=' Blind audit: the small parentheses enclose the wave below h; the first crowded label remains uncertain.'
for ident,place,C,H,final,box,why,kind,ek in [
 ('C33','Generalization paragraph, V_J multi-index continuation',r'J_0\ldots J_n',r'J_0\ldots J_n',r'J_0\mathord{\cdot}\mathord{-}\mathord{\cdot}J_n','B09','The middle mark is a horizontal rule, with one smaller point on either side. Preserve the three marks by their shapes.','misread symbol or index','1 symbols/indices'),
 ('C34','NB continuation after marche-','marcheront','marcheront','marche-\\\\\nraient','B12','The continuation begins with a reduced r/a run, an independently dotted i, then the e/n connection and terminal crossed t. The line-end hyphen before the break is clear. Read marche-/raient.','misread word','2 words')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind=kind,error_kind=ek,against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for x in r['doubts']:
 if 'reading' in x:
  for a,z in reps:x['reading']=x['reading'].replace(a,z)
r['doubts'].append(dict(place='After raised question-mark alors',reading=r'\unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}',alternatives=['on a','point-rule-point'],confidence='medium',reason='A low dark point, longer horizontal run and final point can encode compressed on a or the literal three marks. Their letter boundaries are not secure.',crop=f'crops/{pg}_blind_B05.png',box=b['B05']['coordinates']))
for key in ['notes','deletion_insertion_review']:
 if isinstance(r.get(key),str):r[key]=r[key].replace('marche-/ront','marche-/raient').replace('marche-\\\\\nront','marche-\\\\\nraient')
r['notes']+='\n### Blind reading corrections\n\nThe multi-index continuations are point-rule in99,100, the earlier V_i sequence and the flag, and point-rule-point in the later V_J sequence. The homotopy h is placed above parentheses around the wave. The NB verb reads marche-/raient, with a visible i dot in the second line. The literal flag endpoint I_n is retained, as is the unstarred X_J at the end of104. The tiny first superscript in104 and the crowded raised first map label remain uncertain.\n'
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=json.loads((W/'records/v_encoding_repairs.json').read_text()).get(pg,{}).get(box,b[box]['first'])
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The full99 formula shows a point then longer rule in each of the three indices. Only the first index has commas around the continuation. The hook endpoint remains a curled short return without two independent arrowhead arms; keep the existing headless/headed doubt. All terms and Z agree.',True)
put('B03','Viewed the whole crop and an enlarged right-side derivative. The main line begins lowercase si; the crossed word ends fermé without a separate final e. Qui contient has its dotted i and tall final t. The canceled old phrase is too obscured to replace by a confident ou. The raised phrase has de, crossed sorte and que, followed by two V terms and labeled connectors, not en tout cas or a simple X-subset-Z formula. Keep the first X-star and crowded first-label doubts. The h is above parentheses around the wave, as in the larger labels below.',True)
put('B04','The complete canceled formula has a dot above the second X in the initial difference and above the definition X. Both difference marks are simple horizontal minus strokes. Both union indices have strict i<i0 and the final summand is starred. The n indices are the same low n as elsewhere, not m.')
put('B05','The raised hook directly above alors is a clear question mark. The following three low marks do not separately certify on a; leave on a/point-rule-point uncertain.',True)
put('B06','The whole100 map has a definite right arrowhead and left hook. Both indices are point-rule. The h stands above parentheses around the wave. The extra alors on a at the top is the preceding phrase, already transcribed and now locally doubtful in B05.',True)
put('B07','The separate question mark, à vérifier underline, and detached exclamation mark are clear. A newline rather than a quad is only an encoding difference.')
put('B08','The parenthesized on suppose X métrisable is complete, with an accent stroke and three separate final dots. Ldots is a faithful encoding of those three prose dots.')
put('B09','The whole sentence and commas agree. The V_i multi-index has point-rule; the V_J multi-index has point-rule-point, with the middle mark visibly longer than either end point. Restore those shapes literally.',True)
put('B10','The final flag letter has separate top and bottom bars on an upright: capital I_n, matching the nearby I of de I, not the hooked J0. Keep the literal slip. The flag continuation is a point and rule. The quotation marks, bande and On définit agree.',True)
put('B11','The full101 formula agrees, including the union index, headed limit, its d-in-Drap(J) index and final V_d. Provoisinage has no hyphen. Differences in text wrappers and display number placement are immaterial.')
put('B12','The second line of the verb contains an independent i dot between the low ra and ent run: raient, not ront. Preserve the preceding marche- and line break. The complete NB sentence and parentheses agree.',True)
put('B13','The whole102 equality has V_J^Z, intersection and Z exactly as transcribed. Tag placement and command spaces are representation only.')
put('B14','The complete103 map has both hook and arrowhead. The label h is above parentheses around the wave. The caption has a separate stop after hom before its closing parenthesis.',True)
put('B15','The entire104 diagram and final condition were inspected. Its first tiny raised mark still permits h/star; the lower definition contains a clear star. Both map labels put h above parentheses around the wave. The two vertical strokes between the V terms are vertical, the two underlines under si are distinct, and the final X_J is literally unstarred.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('097: all14 differing boxes viewed; nine changed boxes.')
