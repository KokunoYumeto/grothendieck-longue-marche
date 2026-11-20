"""Explicit root decisions after viewing all eight scan010 mismatches."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan010';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text();repl=[('tt arc,',r'\unsure{tt|tte} arc,'),('compo-',r'\unsure{compo-|comp.-}')]
for a,b in repl:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
tp.write_text(t)
for c in r['changes']:
 for a,b in repl:c['final']=c['final'].replace(a,b)
r['doubts'] += [dict(place='L14 abbreviated word before arc',reading=r'\unsure{tt|tte}',alternatives=['tt','tte'],confidence='medium',reason='B09: two upright t stems share a crossbar. A separate low curved exit after the second can be the end flourish or a very reduced e. Keep tt preferred without forcing agreement with arc.'),dict(place='Final divided or abbreviated word',reading=r'\unsure{compo-|comp.-}',alternatives=['compo-','comp.-'],confidence='medium',reason='B10: after the p descender is a tiny round trace before the hyphen. It can be reduced o or an abbreviation point. Do not expand the fragment or decide it from the next, unsupplied page.')]
for a in r['abbreviations']:
 if a['form']=='tt':a.update(form=r'\unsure{tt|tte}',expansion='tout | toute; the possible terminal e remains a reading uncertainty')
r['notes'].append('Independent audit: the top numeral is an angular open 4. The final curve after tt and the tiny trace before the hyphen in compo- are now explicitly doubtful (tt/tte; compo-/comp.-). Their preferred primary readings are unchanged. The singular boucle and fermée have no independently visible extra s. The raised sc./ie. abbreviation and the canceled initial à remain uncertain. The verbal shorthand keeps two near-parallel strokes without a separate m body. No independent mathematical check was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('high','The numeral has an open angular left branch, horizontal bar and descending right stem, with no closed upper bowl: 4 rather than 9.'),
'B03':('high','After se the word begins with a separate short r/e-like joined pair before the c/o/u and long p descender. These extra low strokes support recoupent, not coupent. The final deux has a looped d and crossed x.'),
'B04':('medium','The insertion connector enters inside the opening parenthesis before quadratiques. Paired quote ticks and comma are visible. The first abbreviation glyph is tall and undotted, while the second c/e shape is compact; keep sc./ie. rather than supply a secure i.e. with an unobserved intermediate point.'),
'B06':('high','Correspondent, biunivoquement with long q descender, aux pts doubles and X sub alpha agree. The separator is a horizontal dash. Line-break and dash encodings do not change the reading.'),
'B07':('medium','Boucle ends with the low e turn and a connected exit stroke; no independent additional s body is visible. Retain singular boucle rather than normalize it from surrounding plural expressions.'),
'B08':('high','Fermée has its accent, a separate final e and then blank paper before the comma. There is no extra s between e and the comma.'),
'B09':('medium','Two upright stems share a crossbar. The low curve after the second stem may be its exit or a reduced e. Retain tt as preferred and add tte as an explicit alternative; the masculine noun does not decide the ink.'),
'B10':('medium','The raised parenthesis joins before the canceled phrase. L’aide is readable but the initial à is absorbed by the strike and stays doubtful. The verbal shorthand has two near-parallel strokes without independent m humps. After final p is a tiny round trace before the hyphen, now compo-/comp.-. All other words, hat and dash agree.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b]
 for a,z in repl:final=final.replace(a,z)
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
