"""Root decisions after personal viewing of all seven second-reading crops."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='145_scan038';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
subs=[(r'\unsure{g_0}',r'\unsure{g_0|\rho}'),(r"\unsure{On remarque d'abord|commutant}",r"\unsure{On remarque d'abord|On pourrait}"),(r'\unsure{exprimons}',r'\unsure{exprimons|exprimer}')]
for a,b in subs:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
tp.write_text(t)
bxs={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
for i,b,e in [(2,'B01','The crossed glyph has an upper loop, lower stem/loop and low rightward oval, favoring g_0, but the cancellation can also obscure a rho. No separate e establishes the independent de proposal. The live formula retains rho g-infinity without supplied parentheses.'),(12,'B05','The initial closed capital loop and short following stroke establish the opening On more clearly than commutant. The long low middle and tall final stroke remain under the zigzag strike. On remarque d’abord and the independent On pourrait both remain possible; no final donc is independently separable.'),(13,'B06','The canceled first word has ex/pr-like strokes, compressed m and an obscured low ending. It can read exprimons or exprimer. The following que, tilded u and commute are separately legible under the same strike.')]:
 row=r['changes'][i]
 for a,z in subs:row['final']=row['final'].replace(a,z)
 row.update(evidence=e,crop=f'crops/{pg}_second_{b}.png',box=bxs[b],confidence='low')
for d in r['doubts']:
 for a,b in subs:d['reading']=d['reading'].replace(a,b)
 if d['place']=='L1 canceled symbol':d.update(alternatives=r'g_0; \rho',reason='B01: a low right oval favors the subscript in g_0, but the crossed loop/stem can also be rho. No independent second prose letter is clear.')
 if d['place']=='L10 first canceled line':d.update(alternatives="On remarque d'abord; On pourrait",reason='B05: the initial On is supported, excluding a wholly different initial commutant; the zigzag cancellation still hides the middle and ending of the sentence.')
 if d['place']=='L11 canceled initial word':d.update(alternatives='exprimons; exprimer',reason='B06: the low ending is merged with the strike and does not settle -ons against -er.')
for x in r['inventory']:
 for a,b in subs:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
 if x['element']=='E11':x['first_words_or_objects']="On remarque d'abord | On pourrait (uncertain)"
 if x['element']=='E12':x['first_words_or_objects']='exprimons | exprimer (uncertain) que tilde-u commute'
r['notes'].append('The independent audit changes only the explicit alternatives in three canceled passages (B01, B05, B06). The apparent exclamation beside the slanted note is the separate s. beginning the next main-text line and completing il f. et s.; no punctuation is added to the margin. The three factors in (18) were read together: tall looped l, distinct rho actions, p exponents, the star above the middle p and the missing opening parenthesis after the final int are preserved. Reading this relation is not a proof check.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('low','Whole opening formula checked: g0 equals rho g-infinity without parentheses. The separate crossed glyph has upper loop, stem and low oval; retain g0 but add rho as possible. Two prose letters de are not separately established.'),
'B02':('medium','Narrow upright p, sigma, g0, membership, starred hatted Z, ornate S with subscript 3 and two-stroke plus, and hatted lowercase pi with curled right leg agree. Alphabet of ornate S remains unresolved; hat/bracing syntax is equivalent.'),
'B03':('medium','The overworked reference has a curved upper part, descending diagonal and heavy lower horizontal foot of 2. A separate R stem/leg is not the dominant live form. Keep (2), with no added following colon.'),
'B04':('medium','Read entire display and b) clause. The three looped tall l signs differ from the lower tilded u; first two permutation arguments have no parentheses, last sigma(0) does. Middle star sits above p. Final int lacks the opening parenthesis supplied by the blind reading. Visible f. et continues as s. at the next main-line start: that small curved s and its point align with que, not the slanted margin, so no exclamation is added. Y has its own joined arms and descender, without a distinct crossing stroke; retain live y. Raised (donc attaches by a curved leader, not a second comma.'),
'B05':('low','The closed initial capital loop and next short stroke favor On, so narrow out the alternative beginning commutant. The zigzag strike obscures the long middle and tall terminal; retain On remarque d’abord and add On pourrait. A separate donc is not established.'),
'B06':('low','The initial ex/pr/m-like forms are visible beneath a continuous strike, but the ending admits -ons or -er. Retain doubtful exprimons with exprimer alternative. The rest of the canceled clause and live paragraph agree, including double hats and unexpanded mod autom without added stops.'),
'B07':('high','Two-lobed 3 and slanting crossed 7 are distinct; only the pagination wrapper differs. Authorship of the light footer number is not assigned.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b]
 for a,z in subs:final=final.replace(a,z)
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
