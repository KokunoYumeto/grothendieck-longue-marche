"""Main reader's explicit decisions after viewing all five audit loci."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
key='143_scan018'
a=json.loads((R/'reviews'/f'{key}_auditC.json').read_text())
r=json.loads((R/'reviews'/f'{key}_accepted.json').read_text())
p=dict(key=key,reader='C',findings=[],change_operations=[],
       remaining_doubts_remove=['defining tuple final output'],
       certainty_resolutions_add=[],notes_remove=[f'{key}-N4'],notes_add=[],
       hand_log_add=[],check_events_add=[],inventory_remove=[],inventory_add=[])
reasons=[
 'Main inspected A_tuple: a compact dark point followed by a short stroke, with no separate comma or third point. Preserve both visible marks literally.',
 'Main independently compared 017 action-map with 018 tuple and both 019 occurrences. The compressed a has the same shoulder and low wave; no distinct relation sign is established. Resolve as the named action datum a at medium confidence.',
 'Main inspected A_isom-diagram: a point and a short low stroke precede the close parenthesis. No third point appears.',
 'Main inspected A_margin: the rule ends beneath F(j), above the final equivalence and its tilde. The revised endpoint fits that relation.',
 'Main inspected A_unique-iso: the thin unheaded curve rises from below-left of isom to the raised pi-prefix. Draw the physical guide without altering the word or bare fibre shaft.'
]
for n,(f,idx,reason) in enumerate(zip(a['findings'],[4,5,12,16,25],reasons),1):
 p['findings'].append(dict(index=n,decision='accept',reason=reason))
 old=r['changes'][idx-1]; new=dict(old)
 new.update(final=f['after'],ink=f['reason']+' '+reason,confidence=f['confidence'],
            against_C=f['against_C'],against_H=f['against_H'],crop=f['crop'],box=f['box'])
 if n in (1,3):new['kind']='other'
 if n==5:
  new['kind']=old['kind'];new['confidence']='medium'
  new['ink']=old['ink']+' Main and second reader also confirm the visible curved guide, now drawn in addition to the raised prefix.'
 p['change_operations'].append(dict(operation='replace',place=old['place'],row=new))
p['certainty_resolutions_add'].append(dict(place='defining tuple final output: second-reading resolution',C=r'\mathcal G,a',final=r'\mathcal G,a',ink=reasons[1]))
note=dict(next(x for x in r['notes'] if x['id']==f'{key}-N4'))
note['text']=note['text'].replace('The tuple’s last entry a versus tilde remains unresolved.','The tuple’s compressed last entry is read as a after comparison with the explicitly named action map on scan017; it is not a correction of a clear relation sign.')
p['notes_add']=[note]+a['notes']
p['hand_log_add']=[a['hand_log'][i] for i in (0,1,4)]
for e in a['check_events']:
 e=dict(e);e.update(date='2026-11-20',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; second reader C');p['check_events_add'].append(e)
for eid,description in [('E03','alpha(input tuple with a two-mark continuation) = output tuple ending in a'),('E08','Isom(z,z prime)={pt}; for all z,z prime; downward arrow; lower Isom equality; cat. discrète followed by a point and a short stroke'),('E12','vertical separating rule ending above the final marginal equivalence')]:
 old=next(x for x in r['inventory'] if x['element']==eid);new=dict(old);new['first_words_or_objects']=description
 p['inventory_remove'].append(eid);p['inventory_add'].append(new)
p['main_summary']='All five audit findings visually adjudicated. Four physical corrections accepted; preferred a resolved at medium confidence by verified handwriting and local notation. Seven original MARKS decisions unchanged. Fourteen remaining doubt groups retained. Existing inventory E20 already includes the newly drawn pi-prefix guide.'
(R/'reviews'/f'{key}_main_audit_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
