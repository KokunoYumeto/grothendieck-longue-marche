"""Finalize current workflow metadata after all visual audits, without changing TeX."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
paths=sorted((R/'records').glob('149_scan*.json'))
records=[json.loads(p.read_text()) for p in paths]
assert len(records)==23 and all(r.get('audited') and r.get('main_reviewed') for r in records)
page_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
for path,r in zip(paths,records):
    r['open_questions']=[f"{d['place']}: {d['reading']} — {d.get('reason','')}" for d in r.get('doubts',[])]
    r['record_status']='final root-approved reading, with explicit unresolved doubts'
    path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
assert page_hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
statepath=R/'records/next_steps.json';state=json.loads(statepath.read_text())
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
state.update(second_phase_complete=True,second_phase_pending=[],blind_audits_complete=[r['scan'] for r in records],stage='All visual reading and adjudication complete; final validation, freeze and packaging',updated_utc=now)
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
review={'completed_utc':now,'page_files':len(page_hashes),'all_first_readings_reviewed':True,'all_blind_audits_complete':True,'open_questions_rebuilt_from_current_doubts':True,'page_bytes_unchanged_by_this_script':True,'ocr_used':False,'external_research_used':False,'tex_compilation_performed':False}
(R/'records/final_bookkeeping_review.json').write_text(json.dumps(review,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write(f'final bookkeeping reconciled {now}: 23 current records; open questions rebuilt from current doubts; no page TeX changed\n')
print(json.dumps(review))
