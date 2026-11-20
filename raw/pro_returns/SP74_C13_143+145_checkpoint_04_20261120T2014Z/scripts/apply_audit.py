#!/usr/bin/env python3
"""Apply an explicitly adjudicated audit plan. No reading choices are inferred.

Usage: apply_audit.py reviews/KEY_main_audit_plan.json
Each plan lists every finding with index, decision, reason and optional after.
Material rows, doubts and MARKS edits must be supplied explicitly in the plan.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,sys
R=Path(__file__).resolve().parents[1]
plan_path=Path(sys.argv[1]);plan_path=plan_path if plan_path.is_absolute() else R/plan_path
p=json.loads(plan_path.read_text());key=p['key'];reader=p['reader']
audit_path=R/'reviews'/f'{key}_audit{reader}.json';a=json.loads(audit_path.read_text())
accepted_path=R/'reviews'/f'{key}_accepted.json';r=json.loads(accepted_path.read_text());assert r['reader']!=reader
assert key==a['key'] and a['reader']==reader
assert not r.get('audited_at'), 'Page already audited'
findings=a.get('findings',[]);actions=p.get('findings',[])
assert sorted(x['index'] for x in actions)==list(range(1,len(findings)+1)), 'Every finding requires a decision'
page_path=R/'pages'/f'{key}.tex';text=page_path.read_text();outcomes=[]
for x in actions:
 f=findings[x['index']-1];decision=x['decision'];assert decision in ['accept','reject','modify']
 if decision!='reject':
  before=f['before'];after=x.get('after',f['after'])
  if 'incorporated_by' in x:
   prior=[z for z in outcomes if z['index']==x['incorporated_by'] and z['decision']!='reject']
   assert len(prior)==1 and after in prior[0]['final'] and after in text, 'Overlapping change must already be incorporated in an accepted enclosing replacement'
  else:
   count=text.count(before)
   assert count==x.get('expected_occurrences',1),(x['index'],count,before)
   text=text.replace(before,after,x.get('expected_occurrences',1))
 outcomes.append(dict(index=x['index'],place=f['place'],decision=decision,reason=x['reason'],final=x.get('after',f['after']) if decision!='reject' else f['before']))
# Each operation names an existing physical locus or supplies a new complete row.
for x in p.get('change_operations',[]):
 op=x['operation'];assert op in ['replace','drop','append']
 if op=='append':r['changes'].append(x['row']);continue
 matches=[i for i,z in enumerate(r['changes']) if z['place']==x['place']];assert len(matches)==1,(x['place'],matches)
 i=matches[0]
 if op=='replace':r['changes'][i]=x['row']
 else:r['changes'].pop(i)
for x in p.get('decision_updates',[]):
 matches=[i for i,z in enumerate(r['decisions']) if z['id']==x['id']];assert len(matches)==1,x['id']
 r['decisions'][matches[0]]=x
for field in ['remaining_doubts','certainty_resolutions','inventory','notes','hand_log','check_events']:
 for x in p.get(field+'_remove',[]):
  lookup={'notes':'id','inventory':'element','hand_log':'habit','check_events':'statement_id'}.get(field,'place')
  matches=[i for i,z in enumerate(r.get(field,[])) if z.get(lookup)==x];assert len(matches)==1,(field,x,matches)
  r[field].pop(matches[0])
 r.setdefault(field,[]).extend(p.get(field+'_add',[]))
for x in p.get('auxiliary_list_updates',[]):
 field=x['field'];assert field in ['physical_indices']
 matches=[z for z in r[field] if z['place']==x['place']];assert len(matches)==1
 z=matches[0]
 for k,v in x.get('before',{}).items():assert z[k]==v,(field,x['place'],k)
 z.update(x['after'])
for x in p.get('auxiliary_list_retirements',[]):
 field=x['field'];assert field in ['excluded_certainty_only_changes']
 matches=[i for i,z in enumerate(r[field]) if z['place']==x['place']];assert len(matches)==1
 old=r[field].pop(matches[0])
 r.setdefault('superseded_'+field,[]).append({'prior_record':old,'superseded_by':x['reason']})
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r.setdefault('audit_adjudications',[]).append(dict(reader=reader,time=now,plan=str(plan_path.relative_to(R)),outcomes=outcomes,main_summary=p['main_summary']))
a['main_adjudication']=dict(time=now,outcomes=outcomes,summary=p['main_summary'],plan=str(plan_path.relative_to(R)))
# Static plan assertions precede the actual mutation.
assert text.count('\\scanpage')==1
page_path.write_text(text);accepted_path.write_text(json.dumps(r,ensure_ascii=False,indent=2));audit_path.write_text(json.dumps(a,ensure_ascii=False,indent=2))
print(json.dumps(dict(key=key,reader=reader,findings=len(findings),accepted=sum(x['decision']!='reject' for x in actions))))
