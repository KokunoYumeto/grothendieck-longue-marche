"""Main decisions from the already inspected final-display, margin and Psi crops."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1];key='143_scan015'
a=json.loads((R/'reviews'/f'{key}_auditB.json').read_text());r=json.loads((R/'reviews'/f'{key}_accepted.json').read_text())
p=dict(key=key,reader='B',findings=[
 dict(index=2,decision='accept',reason='Main inspected main_final_display: shallow left-upturned rule, no middle cusp; two annotation lines. This complete replacement also incorporates finding 1.'),
 dict(index=1,decision='accept',incorporated_by=2,reason='Main independently followed the wave continuously into the preceding xi foot. The first right-hand X has no detached tilde. Its correction is already incorporated by the enclosing finding 2 replacement; the same string elsewhere on the page is unaffected.')
],change_operations=[],remaining_doubts_remove=['tiny second Psi index'],remaining_doubts_add=[],inventory_remove=[],inventory_add=[],notes_add=a['notes'],hand_log_add=a['hand_log'][:4],check_events_add=[])
old=next(x for x in r['changes'] if x['place']=='final torsor factor');new=dict(old);f=a['findings'][0]
new.update(final=f['after'],ink=f['reason'],confidence='medium',against_C=True,against_H=True,consequential=True)
p['change_operations'].append(dict(operation='replace',place=old['place'],row=new))
f=a['findings'][1]
row={k:f[k] for k in ('place','C','H','against_C','against_H','kind','confidence','crop','box','marked_in_H','consequential')};row.update(final=f['after'],ink=f['reason'])
p['change_operations'].append(dict(operation='append',row=row))
d=dict(next(x for x in a['remaining_doubts'] if x['place']=='tiny second Psi index'));p['remaining_doubts_add'].append(d)
old=next(x for x in r['changes'] if x['place']=='second splitting-map label index');new=dict(old);new['ink']=d['reason'];new['confidence']='low'
p['change_operations'].append(dict(operation='replace',place=old['place'],row=new))
for eid,kind,description in [('E14','diagram','leftward isomorphism from unaccented X-prime(j) wedge_(pi_1) lifted X-prime to lifted X-prime[j]'),('E15','drawing','shallow rule with left upturn and no central cusp, with torseur à / dr sous pi_1 on two lines')]:
 old=next(x for x in r['inventory'] if x['element']==eid);new=dict(old);new.update(kind=kind,first_words_or_objects=description);p['inventory_remove'].append(eid);p['inventory_add'].append(new)
for e in a['check_events']:
 e=dict(e);e.update(date='2026-11-20',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; second reader B');p['check_events_add'].append(e)
p['main_summary']='Both final-display corrections accepted after main visual inspection. The apparent factor accent belongs to preceding xi; the annotation has a shallow rule. Tiny second Psi index stays doubtful j with more accurate evidence. Marginal separator flip withdrawn after note-relative orientation comparison. Fourteen original MARKS and five retained doubt groups unchanged.'
(R/'reviews'/f'{key}_main_audit_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
