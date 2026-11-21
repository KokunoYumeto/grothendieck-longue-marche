"""Root crop decisions for the ten blind differences on scan 068."""
from pathlib import Path
import json,csv
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan068';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text()
kw=r'$\unsure{K_{1\deleted{2}}|K_1,|K_{12}}$';ext=r'\unsure{ext.|\deleted{de}ext.}'
assert t.count('soit des')==2;t=t.replace('soit des',r'\unsure{soit|sont} des',2)
for a,b in [(r'$K_1$\unsure{,}',kw),('car tt corps ext.','car tt corps '+ext)]:assert t.count(a)==1;t=t.replace(a,b)
p.write_text(t);c={x['id']:x for x in r['changes']}
soit='The s has a curled/angled entry and the word ends in a tall triangular t. The intervening o and following low connected run are very compressed; a distinct i dot is not secure and the same run also admits n. Both occurrences have this pattern independently. Retain soit/sont at each coordinate, while the visible s opening continues to support a departure from H tant.'
num='The whole (0,nu_2) sur K expression is visible. K has the upright and two oblique limbs; its lowered 1 is separate. Below/right is a dark body with a curled upper hook, oblique middle and short lower horizontal return, giving a 2-like form. The middle is heavily retraced and can carry a strike. Preserve the alternatives K with 1 and cancelled 2, K_1 followed by comma, and live K_12; the actual ink does not settle that revision state. The existing comma candidate is retained within the full expression.'
ext_ev='The first abbreviation has a final tall crossed t and a separate dark stop. Before the central x, the ink contains a broad low oval, a tall returning loop and a second narrow upright/loop. These can belong to retraced e/x or to older d/e overwritten by ext. The lower and diagonal overlaps do not isolate one state securely. Retain live ext. in both alternatives and show the possible old de in a deletion wrapper only within the uncertainty. The crop does not show a strike crossing the complete live ext. including t.'
for i in ['P02','P04']:c[i].update(final=r'\unsure{soit|sont}',evidence=soit,confidence='medium')
c['P03'].update(final=kw,evidence=num,confidence='low')
c['P09'].update(final=ext,evidence=ext_ev,confidence='low')
for d in r['decisions']:
 if d['id']=='M1187':d.update(reading=kw,evidence=num,crop=f'crops/{page}_B02_second.png',confidence='low')
for d in r['doubts']:
 if 'M1187' in d['place']:d.update(reading=kw,alternatives='K with subscript 1 and cancelled 2; K_1 followed by comma; K_12',reason=num)
r['doubts'].extend([dict(place='line 1, B01 first short verb',reading=r'\unsure{soit|sont}',alternatives='soit/sont',confidence='medium',reason=soit),dict(place='line 4, B04 repeated short verb',reading=r'\unsure{soit|sont}',alternatives='soit/sont',confidence='medium',reason=soit),dict(place='line 10, B11 first ext. and possible old letters',reading=ext,alternatives='live ext.; cancelled de followed by live ext.',confidence='low',reason=ext_ev)])
r['notes'][0]=r['notes'][0].replace('both introduced by soit','both introduced by the locally uncertain soit/sont')
r['notes'][1]=r['notes'][1].replace('car tt corps ext. de type',r'car tt corps \unsure{ext.|\deleted{de}ext.} de type')
r['notes'][3]='N068_04 — Three secure cancellation regions contain de type, the first étale and the tentative E before E_Q. The blind audit additionally leaves a possible cancelled 2 beside the first K_1 and possible old de beneath the first ext.; both retain alternative readings. The current ext. and ça remain live. No separate interlinear insertion, marginal prose, display, diagram or drawing is present.'
r['notes'].append('Blind audit keeps the literal finalt abbreviation: its long low return from l reaches the terminal t without a distinct extra e/m body. It preserves the separate full stop at the first ext. and the blank after the second ext. The possible numeral revision is recorded in the entire K expression; no inferred extension degree is used to decide it.')
for h in r['hand']:
 if h['form']=='soit':h.update(form='soit/sont',observation=soit,witness_errors='Both occurrences retain the visible s opening; H tant remains a material departure, while C soit remains an explicit alternative.')
 if h['form']=='ext. / ext':h['observation']=ext_ev+' The second occurrence has no detached stop; the third retains its separately observed stop.'
r['inventory'].extend([dict(element='A_B02',kind='deletion',position='line 2 beside the first K_1, B02',first_words_or_objects=kw,transcribed='yes',hand='his hand',sheet_kind='text'),dict(element='A_B11',kind='deletion',position='line 10 beneath first ext., B11',first_words_or_objects=ext,transcribed='yes',hand='his hand',sheet_kind='text')])
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
change('B01',r'pour avoir, \unsure{soit|sont}','Retain avoir and qualify the following short verb','After the separate final r of pour there is a small a body before the shallow v, low o, dotted i and final r. That extra initial body supports avoir; the terminal r is open and distinct. The comma is separate. '+soit)
change('B02',r'$(0,\nu_2)$ sur '+kw,'Record the numeral and punctuation alternatives in the full expression',num)
keep('B03','Retain K_1 and its closing parenthesis','K has its tall stem and two angular limbs. A single lowered upright 1 follows, then one separate closing curve. The blind math delimiter includes that same parenthesis inside math mode; the selected encoding leaves it outside with the same order and attachment.')
change('B04',r'\unsure{soit|sont} des','Qualify the repeated compressed verb',soit+' The following d loop and e/s run form the separate des.')
keep('B08','Retain U with 0-nu1 and the closing punctuation','The open U has the lowered zero, angled nu and further lowered upright 1. The space between zero and nu contains no comma. A separate closing parenthesis and dark stop follow. Both returns map to these same symbols; the difference only moves the parenthesis across the math delimiter.')
keep('B09','Retain finalt without expansion','The tall f descender and crossing loop, dotted i, compressed n/a, tall l and terminal triangular t are visible. From the foot of l a continuous low return runs directly to t; it has no separately articulable intervening e or m body. Retain the written short form finalt with the t on the rising baseline and no supplied stop.')
keep('B10','Retain the locally cancelled E and live E_Q','The earlier curved E candidate is crossed by angular strokes between sur and the live two-lobed E. The deletion remains confined to that candidate. The final Q is an oval with a lower inner stroke continuous into its diagonal tail; the Q/mathbb-Q renderings in the blind alternatives map to this same identifier body. Its subscript attachment to E is secure; no distinct second letter is introduced.')
change('B11',ext,'Qualify possible overwritten letters under live ext.',ext_ev)
keep('B12','Retain ext without a stop','After the initial e loop there are two crossing oblique strokes making a low left loop and an upper-right return, then the tall t and its long rightward crossbar. The central crossed body supports x. The blank interval after its terminal contains no detached stop, so ext remains unexpanded and unpunctuated.')
keep('B15','Retain both d’une and d’un','The d loop, apostrophe and low u/n run are visible before the large crossed X. The extra small final return favors e but flattens into the exit and does not securely isolate its full loop. The independent reading agrees with the first candidate; the local d’une/d’un uncertainty remains.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_c')
