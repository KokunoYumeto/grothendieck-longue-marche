"""Root image adjudication of scan009; one-shot history."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan009';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text();old='(ou arêtes orientées)';new=r'(\unsure{--|ou} arêtes orientées)';assert t.count(old)==1;t=t.replace(old,new);tp.write_text(t)
bxs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
r['changes'].append(dict(place='Parenthesis after arcs: short mark before arêtes',C='(ou arêtes orientées)',H="(ou arêtes \\uncertain{munies d'une} orientation)",final=new,evidence='After the curved opening parenthesis there is a very low, nearly horizontal short trace. A separate closed o and u humps are not secure. A short dash is preferred, while compressed ou remains possible. The blind reader also proposed a dash or equals; two independently stacked bars are not visible, so equals is not adopted. The clearly written orientées remains unchanged.',crop=f'crops/{pg}_second_B08.png',box=bxs['B08'],confidence='low',against_C=True,against_H=True,kind='other',marked_in_H='no',consequential=False))
r['doubts'].append(dict(place='Parenthesis after arcs, before arêtes',reading=r'\unsure{--|ou}',alternatives=['short dash','ou'],confidence='low',reason='B08: the low short trace after the opening parenthesis favors a dash; compressed ou remains possible. No clear o loop/u humps or two vertically stacked equals bars can be separated.'))
r['notes'].append('Independent audit: all four origin-map occurrences retain o after comparison with the separate angular sigma on this sheet and scan008. The parenthesis after arcs begins with a low short mark, now recorded as dash/ou uncertainty; no grammatical synonym is imposed on it. The complete two graph systems, the inclusion arrows and (9) agree. This does not independently verify the graph construction.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B02':('medium','The opening sigma has an angular hanging bowl and straight top bar. The later map name is a small closed round o with a short exit, followed by a distinctly stemmed p. Retain o; brace syntax alone otherwise differs.'),
'B03':('high','Both maps have a curved hook at the left and a right arrowhead. Tilde-A is heavily retraced but has a triangular A body; no separate underlying cancellation is recoverable. The comma separates the two maps; math grouping alone differs.'),
'B05':('medium','The whole parenthesized pair is present. The map label has a small closed round loop with upper-right exit, unlike the angular sigma-sub-tilde-A to its right. Keep origin-map o. Arrow direction, comma and parentheses agree.'),
'B06':('medium','The upper row is parenthesized; A is below its left object, reached by a downward arrow labeled deg 2 without a stop. The horizontal o has the same closed loop and exit as B05. A comma follows the upper closing parenthesis. The full layout is preserved.'),
'B08':('low','The low mark after the opening parenthesis has no secure separate o loop or u humps; a short dash is preferred with ou retained as an alternative. Two stacked bars for equals are not visible. Orientées is one word; arcs alone is underlined. The later round map name remains o, and ens has no separate point.'),
'B09':('high','Paired raised short ticks open and close origine d’un arc; a separate full stop follows. The straight-quote encoding is normalized to the required diplomatic paired ticks.'),
'B10':('high','The whole display (9) has serifed I, a single unlabelled right arrow with no tail bar or hook, and S. Only display wrappers differ.'),
'B11':('high','The light lower-left numeral has two loops crossed at the waist: 8. Margin/page wrapper is the only difference.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b].replace('(ou arêtes orientées)',new)
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
