"""Root's explicit one-shot decisions after viewing all five mismatches."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1]; pg='147_scan007'; rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repl=[(r'\unsure{\text{avec}}',r'\unsure{\text{avec}|\text{et}}'),(r'\inserted{(pour les iso)}',r'\inserted{(pour les isos)}')]
for a,b in repl:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
tp.write_text(t)
for d in r['doubts']:
 if 'canceled word' in d['place']:
  d.update(reading=r'\deleted{\unsure{\text{avec}|\text{et}}}',alternatives=['avec','et'],reason='B04: thick horizontal ink covers the letter bodies. A low initial curve and short upright can also fit et, as the blind reader proposed. Neither complete reading is secure; preserve the canceled-word doubt.')
for c in r['changes']:
 for a,b in repl:c['final']=c['final'].replace(a,b)
 if c['place']=='L9 struck word after sur S':c['evidence']+=' Blind B04 adds et as a possible reading of the short upright and lower curve; the cancellation still prevents resolution.'
bxs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
r['changes'].append(dict(place='Final inserted parenthesis: plural ending of isos',C=r'\inserted{(pour les iso)}',H=r'\add{(pour les iso)}',final=r'\inserted{(pour les isos)}',evidence='After the i/s/o sequence there is a separate small right-curving s before the larger closing parenthesis. Compare the baseline (pour les iso) immediately above, which lacks this extra curve. The inserted article begins with a taller l, followed by low e/s, not un. Root checked the rotated B08 and the existing upright final crop; the connector still enters before the baseline comma.',crop=f'crops/{pg}_second_B08.png',box=bxs['B08'],confidence='medium',against_C=True,against_H=True,kind='omission',marked_in_H='no',consequential=False))
r['notes'].append('Independent audit: the small canceled word in (5)b now retains avec/et alternatives. Partout has the tall internal/final t strokes rather than the extra humps required by purement. The quotient retains the visible older X beneath the reinforced Y; the lower-right arm of X survives. The final inserted parenthesis has a separate terminal s in isos, unlike the baseline iso above. The shortened schém.s forms and phi/empty-set ambiguity remain. No independent mathematical check was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B04':('low','Comme is on a separate raised baseline above ci-dessus. Sur S has a connector rather than a comma. Partout has p descender, low a/r and tall t strokes, not the extra m/e sequence of purement. Both abbreviation point and separate comma follow sous-schém. The canceled word permits avec/et, now both recorded. The full three-part formula, tilde-A, I, sigma subscript and empty-set sign were checked; phi/varnothing remains uncertain.'),
'B05':('medium','The old X retains a lower-right arm beneath the dark overwork. The reinforced replacement has upper arms meeting a long descending stem, Y. Keep deleted X then inserted Y. Hat, equals, quotient slash, sigma and comma agree.'),
'B06':('high','The relation has a wavy upper stroke over a straight lower bar, simeq. Tilde-A, slash and sigma agree; only brace syntax differs.'),
'B07':('medium','A separate point-like trace occurs between the low m and detached s. It can be an abbreviation stop or a very reduced a, so the existing sous-schém.s/sous-schémas doubt remains. Fermés is raised and its connector enters before finis.'),
'B08':('medium','The main le has a tall initial loop, not a low c. Mapsto has a bar at its tail and arrowhead at the right; I is inserted into the tuple. The diagonal NB reads est compatible aux images inverses, and its apparent (6) belongs to the upright display. Schém.s keeps its point/reduced-a doubt. The final insertion has les and a distinct last s in isos before the closing parenthesis; its connector ends before the baseline comma. The separate faux tel quel ! and page 6 are preserved.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b]
 for a,z in repl:final=final.replace(a,z)
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
