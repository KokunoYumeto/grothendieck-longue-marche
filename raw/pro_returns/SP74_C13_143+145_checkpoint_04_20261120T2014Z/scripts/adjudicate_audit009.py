from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[1];key='143_scan009';reader='C'
r=json.loads((R/'reviews'/f'{key}_accepted.json').read_text())
a=json.loads((R/'reviews'/f'{key}_audit{reader}.json').read_text());f=a['findings'][0]
z=copy.deepcopy(next(x for x in r['changes'] if x['place']=='Cancelled final line, group'))
z['final']=z['final'].replace(f['before'],f['after']);z['ink']+=' The terminal point lies on the long cancellation stroke among similar lower-edge projections; its existence is now explicitly uncertain, without changing the preferred character.'
p={'key':key,'reader':reader,'findings':[{'index':1,'decision':'accept','reason':'Main re-inspected the existing cancelled_block26 crop. A rounded projection after the final primed glyph may be a period, but it cannot be securely separated from the cancellation and its neighboring projections. Retain the point under doubt.'}],
 'change_operations':[{'operation':'replace','place':z['place'],'row':z}],
 'remaining_doubts_add':[a['remaining_doubts'][-1]],
 'certainty_resolutions_add':[{'place':'Final point of canceled compatibility sentence','C':'.','final':r'\unsure{.}','ink':f['reason']}],
 'notes_add':a['notes'][:3], 'hand_log_add':[a['hand_log'][1]],'check_events_add':[],
 'main_summary':'Main inspected the reused cancellation crop and accepted the single certainty-only punctuation change. All material readings, inventory elements, and original MARKS decisions remain as accepted; every second-reader finding is decided.'}
for e in a['check_events']:
 z=copy.deepcopy(e);z.update(date='2026-11-20',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; second reader C');p['check_events_add'].append(z)
(R/'reviews'/f'{key}_main_audit_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
