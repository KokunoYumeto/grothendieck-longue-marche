from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan096';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[('et $X$ metrisable',r'\unsure{et|tt} $X$ metrisable'),(r'\deleted{\unsure{et}}',r'\deleted{$V_{\unsure{ij|j}}$}'),(r'\deleted{\unsure{d|donc}} comme',r'\deleted{\unsure{d|donc|On}} \unsure{comme|aura}'),(r'\deleted{\unsure{les}}',r'\deleted{$V_i$}'),(r'\unsure{borne|bornera}','bornera')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C02':x.update(final=r'\unsure{et|tt} $X$',confidence='medium',evidence='Two linked upright strokes form a very compressed et or tt; their exact identities remain uncertain. There is no comma-plus-si group.')
 if x['id']=='C12':x.update(final=r'\deleted{\unsure{d|donc|On}}',evidence='The tall old loop and basal return are crossed; they allow d/donc or a compressed On. The following low live group is now separately left comme/aura uncertain.')
for ident,place,C,H,final,box,why,kind in [
 ('C34','Canceled term after enfin',r'\deleted{\unsure{et}}',r'\struck{\ill{}}',r'\deleted{$V_{\unsure{ij|j}}$}','B08','The large left hooked descending curve and returning right arm have the same V skeleton as the nearby formulas. A lower j-like hooked stroke survives, with a possible preceding i under the crossed mass. This is a canceled V term, not the short et.','misread symbol or index'),
 ('C35','Canceled term before i<j',r'\deleted{\unsure{les}}',r'\struck{\ill{}}',r'\deleted{$V_i$}','B11','The large open left hook, low bowl and raised right arm are a V. A small detached lower-right i survives the diagonal crossing strokes; there is no sequence of l/e/s letters.','misread symbol or index'),
 ('C36','Verb after mais on se','borne','bornera','bornera','B13','After the b/o/r/n/e run there are two further short groups, the angled r shoulder and final rounded a, separated from the preceding e. The full written verb is bornera.','misread word')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high' if ident=='C35' else 'medium',kind=kind,error_kind='1 symbols/indices' if ident!='C36' else '2 words',against_C=True,against_H=ident!='C36',consequential=False,marked_in_H=ident!='C36',phase='blind audit'))
r['doubts']=[x for x in r['doubts'] if x['place'] not in ['Canceled word before i<j','Verb after mais on se']]
for x in r['doubts']:
 if x['place']=='Canceled word after enfin':x.update(place='Canceled V term after enfin',reading=r'V_{\unsure{ij|j}}',alternatives=['ij','j'],reason='The large curved V is clear; its lower j hook survives but the possible i is inside the cancellation.')
 if x['place']=='Canceled old start before comme':x.update(reading=r'\unsure{d|donc|On}',alternatives=['d','donc','On'],reason='The compact old loop and basal return remain crossed; no complete internal word boundaries are secure.')
for place,reading,alts,box,why in [
 ('Before X metrisable',r'\unsure{et|tt}',['et','tt'],'B02','Two linked uprights and a common bottom return permit compressed et or tt.'),
 ('Live word after the canceled old start',r'\unsure{comme|aura}',['comme','aura'],'B09','The low linked run lacks independently separable internal letters; its final return can belong to e or a.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
for key in ['notes','deletion_insertion_review']:
 if isinstance(r.get(key),str):
  r[key]=r[key].replace('second canceled et','canceled V term with uncertain ij/j index').replace('canceled les','canceled V_i')
r['notes']+='\n### Blind reading corrections\n\nThe crossed group after enfin is a V with an unresolved ij/j index; the later crossed group before i<j is V_i. Both replace the earlier short-word readings. The verb after mais on se is bornera, with separately visible ra. The clipped right-edge words are not completed. The literal closing brace after phi remains a brace, although the opening delimiter is a parenthesis. The slanted marginal phrase remains et des protopos homotopes, with exponent Z and plus bas.\n'
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=json.loads((W/'records/v_encoding_repairs.json').read_text()).get(pg,{}).get(box,b[box]['first'])
  for a,z in reps:f=f.replace(a,z)
  if box=='B02':f=f.replace('et $X$',r'\unsure{et|tt} $X$')
  notes[box].update(changed=True,final=f)
put('B01','The final b/l group physically meets the black paper edge. No surviving e/s follows it, so neither complete incomparable nor incomparables is supplied. Keep the clipped incomparab with uncertain l.')
put('B02','The linked two-upright form can be et or tt; retain that local ambiguity. The X and unaccented metrisable are clear, followed by a comma.',True)
put('B03','The opening on is already in the page immediately before this excerpt. The crossed long word still supports trouve only provisionally; the separate live low aura is clear. No text is duplicated.')
put('B04','The whole V_ij=phi formula agrees. Beneath the short strike an e loop and a separate final t upright are visible; retain resolved et, not ou.')
put('B06','The whole equality chain and the parenthetical opening agree. The left pour i=j fragment is already transcribed before on aura; it is an overlapping boundary, not an omission.')
put('B08','The large hooked left arm, low bottom and rising right arm match the V in nearby formulas. A low j hook is visible under the crossings, with a possible preceding i. Replace the short-word et hypothesis by canceled V with ij/j uncertainty. The following si is live and already outside the cancellation.',True)
put('B09','The old tall loop is repeatedly crossed; d/donc/On remain possible. The separate live low run can be comme or aura, and its internal letters are too compressed to settle. No whole old word is confidently restored.',True)
put('B10','The visible word reaches the black edge immediately after r. No final e survives; retain literal clipped d\'introduir, without supplying a doubtful off-page letter.')
put('B11','The canceled large body has the same rounded V construction as the formulas, with an independently placed lower-right i. Two diagonal strokes cross it. Read canceled V_i, not les.',True)
put('B12','The entire98 definition agrees: one long subscript rule on the left, two separated short rules between the intersection signs, final comma. Plain V encoding is retained, with proper command separation.')
put('B13','After borne there are two further exposed low groups: an angled r shoulder and rounded a. These resolve bornera, matching the blind reading.',True)
put('B14','The entire set-of-indices phrase and lower phi are visible. The closing mark has an upper hook, central bend and lower horizontal foot: a right brace, not a smooth parenthesis. Keep the mismatched delimiters literally. En fait ils sont rangés agrees.')
put('B15','The abbreviation str. and complete increasing chain agree. There are two separated continuation rules and four strict comparison signs as transcribed; display versus inline encoding adds no difference.')
put('B16','The long possible opening curve remains entangled with the descending p from the slanted note. Do not remove its uncertainty. The words pour éviter des redondances, right parenthesis and following stop are clear.')
put('B17','Les protopos and the raised star are clear. Text superscript versus math superscript is only encoding.')
put('B18','The dotted i and small e are followed by two reduced r shoulders and the e/s ending: pierres. There is no independent extra u before a v to support pieuvres, nor the shorter c group of pièces. Both paired high quotation ticks and de construction are present.')
put('B19','The whole live line reads pour en construire des tas d\'autres with a final comma. Sont les belongs to the preceding baseline already transcribed, not an added phrase here.')
put('B20','The lower rule under lim has a short thick upward/lower return at its right endpoint, retaining the directed-limit reading at the previously stated medium confidence. The parenthetical finies si I fini is complete. The following comma is already in the page outside this box excerpt.')
put('B22','Viewed the exact note and a36-degree rotation. The first short word has e plus crossed t; then des and protopos. The next line has h, reduced omo, crossed t and the p/o/s ending of homotopes. The exponent has two bars joined by a straight diagonal: Z. The last line reads plus bas, with a tall b and low a/s, not gros. The i0 comma, one continuation rule and in remain literal.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('096: all19 differing boxes viewed; five changed boxes.')
