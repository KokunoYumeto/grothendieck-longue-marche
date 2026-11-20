"""Explicit root decisions on scan014; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan014';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text();old=r'\uline{Courbes ``stables\'\'}.'.replace("\\'","'");new=r'\uline{Courbes ``stables\'\'}\unsure{,|.}'.replace("\\'","'")
assert t.count(old)==1;t=t.replace(old,new);tp.write_text(t)
for c in r['changes']:
 c['final']=c['final'].replace(old,new).replace("Courbes ``stables''.",r"Courbes ``stables''\unsure{,|.}")
 if c['place']=='Underline scope in the section 3 heading':c['evidence']=c['evidence'].replace('point following stables','punctuation mark following stables')
 if c['place']=='Heading quotation marks and full stops':
  c.update(place='Heading quotation marks and punctuation',against_C=True,confidence='medium',evidence='Stables is enclosed by paired raised ticks. The separate low mark after them is slightly elongated and tapered downward, favoring a comma, but at this source resolution a full stop is not excluded. A definite separate point follows graphes and the section number 3 has its point. The doubtful comma/period remains outside the first underline.')
r['doubts'].append(dict(place='Heading, punctuation after closing quote of stables',reading=r'\unsure{,|.}',alternatives=['comma','full stop'],confidence='medium',reason='B06: the small low mark has a tapered downward extension, favoring comma over period; its short extent does not certify the distinction. It is outside the underline.'))
r['notes']=[n.replace('the point after stables lies outside the first span','the comma/period mark after stables lies outside the first span') for n in r['notes']]
r['notes'].append('Independent audit: the small heading punctuation after stables favors comma but remains comma/period uncertain. The first card is retained with the same operator reading as its repeated occurrence in (16); size alone does not establish a capital. The rounded double-bowl omega is retained in (17), with one vertical definition attachment and no duplicated omega. Live et has a tall second stroke and does not read two low letters ou. All hats, tildes, subscripts, labels and both inequalities were inspected. No independent proof of equivalence or stability criterion was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('medium','The main card operator has the same open initial curve and remaining a/r/d shapes as its repeated occurrence in (16); larger initial size alone does not establish a distinct capital. The marginal X-alpha belongs to the composante phrase. Reduced à has a compact body below its accent, matching scan004. Both full expressions and number 6 agree; margin placement wrappers differ.'),
'B02':('medium','The final term has two rounded bowls and a central join, read omega consistently with the notation here. Hat-nu, nu, plus and all alpha subscripts agree. One omega stands above vertical parallel bars and déf; the attached explanation is below it. The full formula and definition, not merely the uncertain alphabet, were inspected.'),
'B04':('medium','The overworked joining word has a low e body followed by a tall t stem and rightward cross/exit, not two low letters ou. There is no separate independent cancellation. The reduced preposition before l’infini again has the local à shape. Retain et and the complete parenthesis.'),
'B05':('high','The wavy tilde is above the peaked hat on X, in that order. Y-alpha, Y, equality and final point agree; macro sizes alone differ.'),
'B06':('medium','MD begins with multiple uprights and two internal slants, M rather than N. Standart ends in a tall crossed t. The small mark after the closing quote is tapered downward and favors a comma, but retains period as an alternative. The three underline spans, final point and inserted sur k alg. clos attachment agree.'),
'B07':('high','No separate comma follows suivantes; the small terminal turn belongs to the final s. The full Aut condition and both inequalities agree, including g-alpha, hatted nu-alpha, 3, the subtraction of 2 and final 1. The preposition after satisfait follows the same reduced à habit. Display and brace syntax alone otherwise differ.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box].replace(old,new)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
