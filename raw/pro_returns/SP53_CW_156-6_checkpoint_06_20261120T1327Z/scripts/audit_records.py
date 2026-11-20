"""Audit completeness of the saved reading records, without reinterpreting the ink."""
from pathlib import Path
from collections import Counter
import json,sys
O=Path(__file__).resolve().parents[1]
errors=[];rows=[]
event_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted, with refined statement ID'}
def normalize_crop(path):return str(path).split('/out/',1)[-1]
coverage_path=O/'S_coverage.json'
coverage=json.loads(coverage_path.read_text()).get('expected_reviews',[]) if coverage_path.exists() else []
for p in sorted((O/'decisions').glob('scan[0-9][0-9][0-9].json')):
    d=json.loads(p.read_text())
    if not d.get('committed'):continue
    n=d['scan'];page=O/'pages'/d['filename']
    expected_s={x['id'] for x in coverage if x['scan']==n}
    if {x['id'] for x in d.get('s_rows',[])}!=expected_s:errors.append(f'scan{n:03}: main S-row coverage mismatch')
    if page.read_text()!=(O/f'decisions/scan{n:03}_final.tex').read_text():errors.append(f'scan{n:03}: final/page mismatch')
    if not d.get('adjudicated_all'):errors.append(f'scan{n:03}: not adjudicated')
    view_path=O/f'decisions/scan{n:03}_main_views.json'
    main_views=json.loads(view_path.read_text()) if view_path.exists() else []
    if isinstance(main_views,dict):main_views=main_views.get('viewed_crops',[])
    main_seen={normalize_crop(x) for x in main_views}
    for x in d.get('differences',[])+d.get('adjudications',[])+d.get('s_rows',[]):
        if x.get('crop') and normalize_crop(x['crop']) not in main_seen:errors.append(f'scan{n:03}: cited main crop not in successful-view record: {x.get("id",x.get("place"))}')
    for e in d.get('check_events',[]):
        if e.get('type') not in event_types:errors.append(f'scan{n:03}: invalid check-event type {e.get("type")}')
    for x in d['inventory']:
        if x.get('transcribed')!='yes':errors.append(f'scan{n:03}: untranscribed inventory {x.get("element")}')
    for i in range(1,4):
        folder=O/f'readers/scan{n:03}/R{i}'
        r=json.loads((folder/'report.json').read_text())
        if {x['id'] for x in r.get('s_rows',[])}!=expected_s:errors.append(f'scan{n:03} R{i}: S-row coverage mismatch')
        legacy_complete=(n==6 and d.get('brief')=='v001' and r.get('finished_utc') and r.get('inventory') and r.get('notes'))
        if r.get('status')!='complete' and not legacy_complete:errors.append(f'scan{n:03} R{i}: incomplete return')
        roles=Counter(x.get('role') for x in r.get('view_log',[]))
        crops=list(folder.rglob('*.jpg'))+list(folder.rglob('*.png'))
        for role in ('whole','half_a','half_b'):
            if roles[role]!=1:errors.append(f'scan{n:03} R{i}: {role} successfully viewed {roles[role]} times')
        if roles['crop']!=len(crops):errors.append(f'scan{n:03} R{i}: crop files/view records differ')
        rows.append({'scan':n,'reader':f'R{i}','completion_basis':'v001 had no status field; completed return and finished timestamp' if legacy_complete else r.get('status'),'view_roles':dict(roles),'actual_crop_files':len(crops),'C_doubts_reviewed':len(r.get('c_doubts',[]))})
    for x in d['differences']:
        if x.get('confidence') not in ('high','medium','low'):errors.append(f'scan{n:03}: confidence {x.get("id")}')
        if x.get('marked_in_H') not in ('yes','no'):errors.append(f'scan{n:03}: H mark {x.get("id")}')
        if not all(k in x.get('readers',{}) for k in ('R1','R2','R3')):errors.append(f'scan{n:03}: reader variants {x.get("id")}')
        if x.get('crop') and not (O/x['crop']).exists():errors.append(f'scan{n:03}: missing evidence crop {x.get("id")}')
result={'committed_page_count':len(rows)//3,'errors':errors,'reader_records':rows}
if '--save' in sys.argv:(O/'RECORD_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
