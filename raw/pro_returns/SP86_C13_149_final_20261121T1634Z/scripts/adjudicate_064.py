"""Root adjudication of nine differing blind crops on scan 064."""
from pathlib import Path
import json,csv
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan064';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text()
opening=r'Que \unsure{deviendraient|donneraient}'
revised=r'\deleted{\uline{\unsure{fausses|bonnes}} sections, de} \inserted{relèvements continus}'
for a,b in [('Que deviendraient',opening),('(5)',r"\unsure{(5)|(4')}"),(r'\deleted{\uline{\unsure{fausses|bonnes}} sections de} \inserted{relèvements continus}',revised)]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t);c={x['id']:x for x in r['changes']}
open_ev='The initial Q loop and crossing return, then u/e, are clear. The following word starts with a looped d and ends in the rounded a, dotted i, compressed en and tall final t. The long middle is flattened into discontinuous low arches; it does not securely separate devien-dr from donne-r. Retain deviendraient/donneraient locally instead of the earlier firm word.'
number='Within the parentheses, the upper stroke of the digit is extremely faint and the lower body bends down. A small separate-looking upper-right trace leaves the supplied 4-prime alternative possible; the faint junctions do not settle its connection to the digit. Reopen the original (5)/(4-prime) choice, with (5) still first.'
rev_ev='Aux has a low a/u run and a separate crossed x before the strike begins. The cancelled underlined adjective retains its uncertain initial upright/loop and low bowls. Sections has its t ascender and i dot, then low o/n/s; a separate dark downward comma occurs beyond that word and before the final de. The strike continues through this punctuation and de. Above it, the replacement has initial r/e, tall l, accented low vowel and v/e/m/e/n/t/s, then c/o/n, tall t, dotted i and n/u/s: relèvements continus. The underline lies beneath the adjective alone.'
c['P01'].update(final=opening,evidence=open_ev,confidence='medium')
c['P13'].update(final=r"\unsure{(5)|(4')}",evidence=number,confidence='low',against_C=False,against_H=False,accounting_note='The original C alternatives and H reading 5 remain available; no resolved numeral correction is counted.')
c['P20'].update(final=revised,evidence=rev_ev,against_C=True)
c['P02'].update(against_H=False,accounting_note='Both C à and H colon remain explicit alternatives at the same coordinate; no settled departure from either is counted.')
for ident in ['P02','P13']:
 x=c[ident];r['changes'].remove(x);r.setdefault('nonmaterial_observations',[]).append(x)
for d in r['decisions']:
 if d['id']=='M1175':d.update(decision='undecided',reading=r"\unsure{(5)|(4')}",evidence=number,crop=f'crops/{page}_B08_second.png',confidence='low')
r['doubts'].extend([dict(place='main line 1, B01 opening verb',reading=r'\unsure{deviendraient|donneraient}',alternatives='deviendraient/donneraient',confidence='medium',reason=open_ev),dict(place='diagram number, M1175 / B08',reading=r"\unsure{(5)|(4')}",alternatives='(5)/(4-prime)',confidence='low',reason=number)])
for d in r['doubts']:
 if d['place']=='Main line 11, P12 crop, cancelled underlined adjective':d['reading']=r'\deleted{\uline{\unsure{fausses|bonnes}} sections, de}';d['reason']=rev_ev
for x in r['inventory']:
 x['first_words_or_objects']=x.get('first_words_or_objects','').replace('Que deviendraient',opening).replace('sections de','sections, de')
for h in r['hand']:
 if h['form']=='Handwritten 5':h.update(form='Handwritten diagram number 5 / 4-prime',observation=number,scope='This numeral remains unresolved after blind rereading.',witness_errors='C alternatives retained; H 5 remains a candidate, so no material numeral correction is counted.')
 if h['form']=='Cancellation and lower underline':h['observation']=rev_ev
r['notes'][0]=r['notes'][0].replace('Que deviendraient les conjectures précédentes',r'Que \unsure{deviendraient|donneraient} les conjectures précédentes')
r['notes'].append('Blind audit reopens the opening verb and the diagram-number alternatives and preserves the comma inside the cancelled sections, de. The coordinate-level diagram reading retains six objects, four downward arrows, two leftward arrows and the dashed diagonal; the numbering uncertainty does not identify a new object or arrow. Both older S candidates remain under the two live overwritten K forms. The earlier mathematical check is unchanged in scope.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (B/'second'/f'{page}_comparison.tsv').open() as f:cmp={z['box']:z for z in csv.DictReader(f,delimiter='\t')}
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
change('B01',opening,'Qualify the compressed opening verb',open_ev)
keep('B02','Retain the two possible small forms and following une','Two dark marks stand between the final applique strokes and une. The lower one remains compressed and the upper can be an accent or upper point, so à/colon remains. At the right of the crop the three low connected bodies of une remain visible; the blind shorter scope does not remove them.')
keep('B04','Retain relative with the unresolved following point','After the r/e and tall looped l, low a, crossed t and dotted i, the pen forms an open low v cup and a flattened e return. The opening in that cup and the low final return support ve. The detached tiny mark after the word remains doubtful in status, with its trace preserved locally.')
keep('B06','Retain the two-object vertical diagram and left label','The observed objects are upper E with U_S and lower E with S, linked by one downward shaft ending in a lower arrowhead. The number 4 stands to the left at the shaft midpoint. The correspondence of the two renderings maps each E, its same subscript and this sole oriented edge to its same coordinate; the extra empty numbering row changes only the printed spacing. The curly E font in the blind return maps to the same two-lobed letter body.')
keep('B07','Retain est','The first e loop runs into a low horizontal s body with an upward return, followed by the tall terminal t and its crossing stroke. The s is highly flattened but its separate rise before t remains visible; the observed short word stays est.')
b8=cmp['B08']['first'].replace('(5)',r"\unsure{(5)|(4')}")
change('B08',b8,'Reopen the number and retain the traced diagram',number+' The upper short stroke can be traced continuously back into the long g descender of chgt; only the lower long stroke independently connects the two pi bodies. The detached cap above middle-left E is its upper lobe, aligned with the same gapped E ductus in display (4). The four downward shafts end in downward heads. Each horizontal left arrow has one joined V head, with a pale parallel retracing on the lower upper wing; no second complete joined V is separated. At the dashed diagonal the upper-left wings meet at one tip, followed by a short nearby dash and further spaced shaft segments; retain one head and the looped phi label. The source and target are lower-right E_K and middle-left E_U_S, respectively. The prose déduit par chgt de base remains visibly above the diagram.')
keep('B09','Retain the two overwritten-index records','At both indices, dark angular K strokes overlie pale curved earlier bodies. The surviving upper and lower curves still leave the earlier S uncertain. The letters occupy the same baseline index position through overwriting; record the covered candidate with deleted followed by the live K, preserving both physical layers. The blind inserted wrappers describe this same replacement, without a separate raised insertion or leader visible.')
change('B10','aux '+revised,'Retain the cancelled comma and the raised replacement',rev_ev)
keep('B12','Retain the cancelled word and inserted triviaux','The low old bowls remain crossed by the thick strike and do not settle every letter of nuls. Above them, triviaux retains its tall crossed t, low r, two separate i dots, v/a/u and terminal x run. The far-right descending mark belongs at the end of the lower cancelled stroke; the upper word has no independently secure comma after it. No added live comma is supplied.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_a')
