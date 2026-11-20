"""Root image adjudications on scan021; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan021';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repls={'correspondante,':r'\unsure{correspondante|correspondants},',r'\unsure{le|les}':r'\unsure{le|les|la}'}
for a,b in repls.items():assert t.count(a)==1;t=t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects')]:
 for q in r[group]:
  for a,b in repls.items():q[field]=q[field].replace(a,b)
for d in r['doubts']:
 if d['place']=='Final paragraph, article before groupoïde':d.update(reading=r'\unsure{le|les|la}',alternatives=['les','la'],reason='B06: the tall looped l is clear. The following retraced low oval and horizontal exit favor e but also admit an a-shaped closed body; the downward terminal turn may hide s. Retain le first, with les and la alternatives, without a revision chronology.')
r['doubts'].append(dict(place='Opening word, final e/s',reading=r'\unsure{correspondante|correspondants}',alternatives=['correspondants'],confidence='medium',reason='B01: correspondan and the tall crossed t are readable. Its short low rightward ending can be an open e or a reduced terminal s. The singular feminine ending remains first, but grammar does not settle the last stroke.'))
if isinstance(r['notes'],str):r['notes']=[r['notes']]
r['notes'].append('Independent audit: the opening final e/s is now explicitly uncertain. The canceled qui/que and overworked G subscript remain unresolved. The abbreviation after deuxième has m and a tall b on the same baseline, without separate re or an independent abbreviation point. Est un is heavily retraced but has no distinct cancellation line or raised replacement baseline, so it stays live. The final article admits la as well as le/les because its low body is retraced; the live spelling remains standart. The full formulas (23) and (24), including the single-wave equivalence sign and bracketed G, were inspected. Script M has a curved left entry/foot on this sheet and scan019, contrasting with the upright first stems inspected in scan022 B03. No independent check of the asserted equivalence or moduli interpretation was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('medium','The opening correspondan and crossed t are clear, but the short low rightward ending admits an open e or reduced s; retain correspondante with correspondants alternative. The canceled word still has a clear q descender but its u and terminal strokes merge with the strike, so qui/que remains. De sorte qu’on aura and un iso can. are visibly present, with no extra près.'),
'B03':('low','The full expression has label (23), script M with a curved left foot, one wave over a straight bar, product indexed by alpha, and g-alpha/hatted-I-alpha subscripts. The first G subscript is heavily looped and retraced; the blind reader’s definite G does not resolve its extra strokes. Retain the existing G doubt and no invented revision sequence.'),
'B04':('medium','The whole action and system formula agree, including Gamma=Aut G and the indexed hatted-I/g pair. The abbreviation has low m and a b whose bottom shares its baseline; the tall b ascender is not a raised suffix and no separate re follows. Est un has reinforced letter strokes but no independent crossing line or raised replacement, so retain it live. The final Gamma and punctuation agree.'),
'B05':('high','Both M forms have a curved left entry and foot, like the script forms in scan019 and unlike the upright first stem in scan022 B03. The complete (24) expression retains the M_G/Gamma pair, equality, M with bracketed G subscript and final comma; braces and display wrappers alone otherwise differ.'),
'B06':('medium','The article has a tall l and a retraced low oval/exit; e is preferred, but a and a hidden terminal s remain possible. Extend the existing le/les doubt to include la. Standart has a tall internal d and a separate final crossed t, not the shorter stables reading. The numeral 2, category abbreviation, parentheses and bracketed type G are intact.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box]
 for a,b in repls.items():final=final.replace(a,b)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
