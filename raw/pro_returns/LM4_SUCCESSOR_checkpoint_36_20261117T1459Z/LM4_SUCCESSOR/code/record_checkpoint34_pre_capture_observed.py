"""Persist root's actual tool observations and the three explicit writer pauses."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
root=Path(__file__).resolve().parents[1]
def evidence(rel):
    path=root/rel
    return dict(path=rel,bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())
def producer(role,chunk,paths,session=None):
    result=dict(role=role,tool_chunk=chunk,exit_code=0,evidence=[evidence(rel) for rel in paths])
    if session is not None: result['session_id']=session
    return result
producers=[
 producer('final_build','c06201',['records/checkpoint34_corrected_build_driver.out','records/checkpoint34_corrected_build_driver.err','LM4_SUCCESSOR_paper.pdf'],98925),
 producer('final_metrics','940ea7',['records/checkpoint34_metrics.json']),
 producer('final_render','0bf9df',['records/pdf_qa/checkpoint34_final/render_manifest.json','records/checkpoint34_render_run.out','records/checkpoint34_render_run.err'],93609),
 producer('final_pdf_audit','6fdbad',['records/checkpoint34_final_pdf_audit.json','code/audit_checkpoint34_final_pdf.py']),
 producer('final_visual_record','26a572',['records/checkpoint34_visual_review.json','records/checkpoint34_root_visual_observations.json','code/finalize_checkpoint34_visual_record.py']),
 producer('final_size_estimate','0fbb5e',['records/checkpoint34_size_estimate.json','records/checkpoint34_size_accounting_correction.json','records/checkpoint34_size_accounting_run.out','records/checkpoint34_size_accounting_run.err','code/reconcile_checkpoint34_size_accounting.py'],37167)]
agent_inputs=[
 ('/root/involutions','work_A/status_checkpoint34.json','work_A/checkpoint34_owned_manifest.json'),
 ('/root/torus_real','work_CE/checkpoint34_status.json','work_CE/checkpoint34_final_manifest.json'),
 ('/root/topology_census','work_DE/checkpoint34_final_status.json','work_DE/checkpoint34_final_manifest.json')]
agents=[]
for name,status,manifest in agent_inputs:
    data=json.loads((root/status).read_text())
    assert data.get('paused',data.get('no_owned_live_producers')) is True
    assert data['owned_live_producers']==[]
    agents.append(dict(agent=name,paused=True,paused_at=data['paused_at'],owned_live_producers=[],
                       evidence=[evidence(status),evidence(manifest)],
                       acknowledgment='Explicit parent-directed pause message received after the final status command completed.'))
failed_build=dict(session_id=46912,exit_code=1,tool_chunk='b1f7ed',evidence=[evidence(rel) for rel in
 ['records/pdf_qa/checkpoint34_first_layout/records/checkpoint34_build_driver.out',
  'records/pdf_qa/checkpoint34_first_layout/records/checkpoint34_build_driver.err',
  'records/checkpoint34_layout_correction.json']])
failed_size=dict(session_id=55851,exit_code=1,tool_chunk='15fae9',
    scope='All real compression streams and the report completed; the final conservative cap assertion failed.',
    evidence=[evidence(rel) for rel in
 ['records/checkpoint34_size_before_reconciliation/checkpoint34_size_estimate.json',
  'records/checkpoint34_size_before_reconciliation/checkpoint34_size_estimate_run.out',
  'records/checkpoint34_size_before_reconciliation/checkpoint34_size_estimate_run.err',
  'records/checkpoint34_size_before_reconciliation/estimate_checkpoint34_size.py',
  'records/checkpoint34_size_accounting_correction.json']])
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),root_observed_actual_exit_codes=True,
    observed_producer_completions=producers,prior_failed_build=failed_build,
    prior_failed_size_measurement=failed_size,agents=agents,live_producers=[],
    publisher_review=evidence('work_A/review_checkpoint34_readiness_accounting_final.json'),
    root_complete_source_reviews=['code/publish_checkpoint34_readiness.py','work_CE/checkpoint34_readiness_accounting.diff',
        'work_A/review_checkpoint34_readiness_accounting_final.md','work_A/review_checkpoint34_readiness_accounting_final.json',
        'work_CE/review_checkpoint34_size_reconciliation.txt','work_CE/review_checkpoint34_size_reconciliation.json'],
    late_research_binding=evidence('records/checkpoint34_late_research_reviews.json'),
    historical_unconfirmed=['pre-recovery estimator29436','pre-recovery DE g3:543'],
    scope='Actual completed tool outputs and explicit writer acknowledgments. The failed measurement and the successful reconciliation remain distinct. No assertion about unrelated system processes; no future archive result is preclaimed.')
target=root/'records/checkpoint34_pre_capture_observed.json'
assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
backup=root/'records/checkpoint34_before_readiness'
backup.mkdir(exist_ok=False)
path=root/'records/checkpoint34_computation_audit_state.md'
shutil.copyfile(path,backup/path.name)
path.write_text(path.read_text()+'''\n## Actual final producer and writer observations\n\nAll six final roles have actual root-observed exit0, including the separate\naccounting session37167/chunk0fbb5e. The original measurement55851/15fae9\nremains exit1. A paused at12:43:17.296725, CE at12:44:30.864765, and DE\nat12:42:03.819782 UTC. Their exact final status and manifest bytes, every\nproducer evidence file and the current final publisher review are bound\nin checkpoint34_pre_capture_observed.json. No task-owned producer remains.\nThe forthcoming readiness publication is not a capture. The scheduled\ncontroller will remain the only project writer during immutable capture;\nall three writers are to be released immediately after actual capture exit0.\n''')
print('Recorded six actual completed roles, both actual prior failures, and all three explicit writer pauses.')
