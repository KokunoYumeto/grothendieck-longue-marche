"""Root image adjudications on scan016; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan016';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repls={r'\uline{g}:S\to\mathbb N':r'\uline{g}:S\unsure{\to|-}\mathbb N',r'\deleted{\unsure{+1}}':r'\deleted{\unsure{+1|et}}'}
for a,b in repls.items():assert a in t;t=t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects'),('notation','form')]:
 for q in r[group]:
  for a,b in repls.items():q[field]=q[field].replace(a,b)
for d in r['doubts']:
 if d['place']=='canceled group after first h_1=1':
  d.update(reading=r'\deleted{\unsure{+1|et}}',alternatives=['et'],confidence='low',reason='B04: the strike merges with the initial short cross-like trace and following upright. The latter can be a numeral 1 or the tall t of a reduced et; the low initial body is not separable enough to exclude either reading.')
r['doubts'].append(dict(place='Opening tuple, map from S to N',reading=r'S\unsure{\to|-}\mathbb N',alternatives=['horizontal stroke without certified arrowhead'],confidence='medium',reason='B01: the horizontal shaft is clear, but its tiny right endpoint does not certify an independent arrowhead. The preferred map reading is unchanged; the ambiguity is explicitly retained.'))
r['notes'].append('Independent audit: anabélien has the tall b/l and dotted i sequence, and the genus symbol has a separate underline. The map shaft is clear but its very small right endpoint remains arrow/minus uncertain. The canceled group following the first live h_1=1 remains +1/et uncertain. The stability insertion reads de type (1,0): the tall t and descending y/p are distinct, and the lower pair has two figures separated by a comma. It is not a reference to a numbered condition. Live Mais un is below the leader, and nuls retains its terminal s. The h-index, later h_1 value, canceled ou/comme and insertion punctuation remain doubtful. No independent proof of the proposition was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('medium','The opening word anabélien has an a/n/a beginning, tall b and l, and a dotted i, rather than the initial s/t of stable. A separate short bar crosses below the body of g. The map shaft is clear but the tiny right endpoint does not certify its head: retain the arrow as preferred with a horizontal-stroke alternative. The full tuple, page 7 and inequality 2g+nu>=3 were inspected.'),
'B02':('high','The whole condition has g=1 followed by a separate comma and nu=0, then alors la relation. Both numeral forms and both equals signs agree; grouping and math-wrapper differences do not alter the reading.'),
'B03':('medium','The full sum has g=1, a second equals sign, sum g-alpha, plus and h with a compact hooked index. A 1 is favored, but the rounded tail still admits 0. No independent capital-G crossbar can be isolated in that small junction, so the existing 1/0 doubt remains.'),
'B04':('low','After live h_1=1 the strike absorbs an initial short cross-like trace and the following upright: +1 and reduced et remain possible. In the raised tree parenthesis, low joined est strokes stand between G and un. The raised g-alpha-zero, Dans le premier cas leader, both s0-s1 relations and all numerical terms agree; no text or parentheses are supplied from the diagram-like leaders.'),
'B05':('medium','The stability insertion has de followed by a tall crossed t and descending y/p in type; its lower parenthesis contains two figures with an intervening comma, (1,0), rather than a numbered-case reference. Live un remains after Mais below the leader. The raised tree replacement has no written pas. After de genre the final downturned s is visible in nuls. The h_1 value remains 1/0 uncertain, and the canceled ou and comme cannot be resolved letter by letter. The complete lower argument, pt. insertion, circle phrase and final order 2/trois statement were inspected and retained.'),
'B06':('high','The pale lower-left pagination has an upright 1 and the upper bar, descending stem and lower bowl of 5. The manuscript-page wrapper differs, but the reading 15 agrees; its authorship remains unidentified.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box]
 for a,b in repls.items():final=final.replace(a,b)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
