"""Bind root's actual completed tool observations; run only after explicit pauses."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--size-session-id',type=int,required=True)
parser.add_argument('--size-launch-chunk',required=True)
parser.add_argument('--size-exit-chunk',required=True)
parser.add_argument('--pause',nargs=3,required=True)
args=parser.parse_args()

def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def operation(role,chunk,paths,session=None,launch=None,exit_code=0,scope=None):
    row={'role':role,'exit_code':exit_code,'tool_chunk':chunk,'evidence':[bind(x) for x in paths]}
    if session is not None:row['session_id']=session
    if launch is not None:row['initial_tool_chunk']=launch
    if scope is not None:row['failure_scope']=scope
    return row

finals=[
 operation('final_build','20b7cb',[
  'records/checkpoint37_build_driver.out','records/checkpoint37_build_driver.err',
  'LM4_SUCCESSOR_paper.pdf','LM4_SUCCESSOR_paper.log',
  'records/build_passes/20261117T154426785434Z/build_stabilize_0.log',
  'records/checkpoint37_A121_correction_install.json',
  'sections/a_elliptic_pentagon_cubic.tex'],70791,'16c03f'),
 operation('final_metrics','1e4569',[
  'records/checkpoint37_metrics.json','records/checkpoint37_metrics_run.out','records/checkpoint37_metrics_run.err'],48509,'348092'),
 operation('final_render','cca131',[
  'records/pdf_qa/checkpoint37_final/render_manifest.json',
  'records/checkpoint37_render_run.out','records/checkpoint37_render_run.err'],90930,'bdf68d'),
 operation('final_pdf_audit','e95c13',[
  'records/checkpoint37_final_pdf_audit.json',
  'records/checkpoint37_final_pdf_audit_run.out','records/checkpoint37_final_pdf_audit_run.err']),
 operation('final_visual_record','249b91',[
  'records/checkpoint37_visual_review.json','records/checkpoint37_typesetting.txt',
  'records/checkpoint37_visual_finalize_run.out','records/checkpoint37_visual_finalize_run.err',
  'records/checkpoint37_root_visual_observations.json',
  'work_A/checkpoint37_final_page_review.json','work_DE/checkpoint37_final_page_review.json',
  'work_CE/checkpoint37_final_page_review.json']),
 operation('final_size_estimate',args.size_exit_chunk,[
  'records/checkpoint37_size_estimate.json','records/checkpoint37_size_estimate_run.out',
  'records/checkpoint37_size_estimate_run.err'],args.size_session_id,args.size_launch_chunk)]
finals[0]['stdout']=bind('records/checkpoint37_build_driver.out')
finals[0]['stderr']=bind('records/checkpoint37_build_driver.err')
failed=[
 operation('initial_build_missing_format','610bf3',[
  'records/checkpoint37_first_build_failure_observed.json',
  'records/checkpoint37_failed_initial_tex_environment/checkpoint37_build_driver.out',
  'records/checkpoint37_failed_initial_tex_environment/checkpoint37_build_driver.err'],exit_code=1,
  scope='Unconfigured TeX invocation could not find lualatex.fmt; mathematics/layout were not reached. The configured recovery environment was used thereafter.'),
 operation('second_build_proof_heading','e4d48f',[
  'records/checkpoint37_second_build_failure_observed.json',
  'records/checkpoint37_failed_second_tex_build/records/checkpoint37_build_driver.out',
  'records/checkpoint37_failed_second_tex_build/records/checkpoint37_build_driver.err'],79648,'55ad01',exit_code=1,
  scope='Improper prevdepth at the A.127 proof-internal paragraph heading; exact sources were preserved and heading-only repairs independently reviewed.'),
 operation('third_build_overfull_display','1978dc',[
  'records/checkpoint37_third_build_failure_observed.json',
  'records/checkpoint37_failed_third_overfull_build/records/checkpoint37_build_driver.out',
  'records/checkpoint37_failed_third_overfull_build/records/checkpoint37_build_driver.err',
  'records/checkpoint37_failed_third_overfull_build/overfull-page-246.png'],89194,'0195c1',exit_code=1,
  scope='TeX passes completed but the wrapper rejected one26.55002pt A.130 display on physicalpage246. The full rejected edition was retained and the three-row repair reviewed.'),
 operation('third_failure_preserver_wrong_text_locator','331a0d',[
  'code/preserve_checkpoint37_third_build_failure.py',
  'records/checkpoint37_third_build_failure_observed.json',
  'code/complete_checkpoint37_third_failure_preservation.py'],exit_code=1,
  scope='All selected copies were retained before an assertion on T(V) failed because extraction had T(V ). A separate retained completion helper located/rendered the actual page246 and exited0.'),
 operation('first_size_estimate_killed','c11211',[
  'records/checkpoint37_failed_size_estimate_observed.json',
  'records/checkpoint37_failed_size_estimate_137/actual_tool_exit_output.txt',
  'records/checkpoint37_failed_size_estimate_137/records/checkpoint37_size_estimate_run.out',
  'records/checkpoint37_failed_size_estimate_137/records/checkpoint37_size_estimate_run.err',
  'records/checkpoint37_failed_size_estimate_137/code/estimate_checkpoint37_size.py'],12069,'4324a9',exit_code=137,
  scope='Actual shell Killed/exit137 at last-reported image input504365056of624814080 bytes. No completed size report or ZIP. All failed bytes retained before a separately reviewed lower-memory revision; no unseen OOM limit is asserted.')]
failed.append(operation('second_size_estimate_delivery_cap','96b054',[
 'records/checkpoint37_failed_size_cap_observed.json',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate.json',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate_run.out',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate_run.err',
 'records/checkpoint37_failed_size_cap/code/estimate_checkpoint37_size.py'],
 41501,'7e6a0c',exit_code=1,
 scope='All three encoders and separate decoders actually exited0 and fully verified their streams. The outer process actually exited1 solely at its final size-cap assertion:550978789bytes with the unchanged5MB allowance exceeded536870912. Complete source, report and logs retained. Exact later identity reuse does not convert this failed outer run into a successful run.'))
agents=[]
for rel in args.pause:
    d=json.loads((ROOT/rel).read_text())
    assert d['paused'] is True and d['owned_live_producers']==[]
    stamp=datetime.fromisoformat(d['paused_at'])
    assert stamp.tzinfo is not None and stamp.utcoffset().total_seconds()==0
    agents.append({'agent':d['agent'],'paused':True,'paused_at':d['paused_at'],
                   'owned_live_producers':[],'evidence':[bind(rel)]})
assert {a['agent'] for a in agents}=={'/root/involutions','/root/torus_real','/root/topology_census'}
estimate=json.loads((ROOT/'records/checkpoint37_size_estimate.json').read_text())
assert estimate['estimated_total_with_allowance']<536870912
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_37.zip').exists()
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
 'root_observed_actual_exit_codes':True,
 'observed_producer_completions':finals,'prior_failed_attempts':failed,
 'agents':agents,'live_producers':[],
 'operational_source_review':bind('records/checkpoint37_operational_source_review.json'),
 'publisher_review':bind('work_A/review_checkpoint37_readiness_streaming_addendum.json'),
 'additional_source_and_history_evidence':[
   bind('records/checkpoint37_late_transporter_root_review.json'),
   bind('records/checkpoint37_root_A127_Bu_alert_retraction.json'),
   bind('records/checkpoint37_before_A121_correction_observed.json')],
 'scope':'Actual root tool exits of all six final producers and all named root failures, with current byte bindings and explicit named-writer pauses. Successful prior builds superseded for the A121 correction are preserved separately. The still-waiting capture orchestrator is not a mathematical/encoding producer; no archive success is preclaimed.'}
with (ROOT/'records/checkpoint37_pre_capture_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps({'result':'ACTUAL_COMPLETIONS_AND_PAUSES_BOUND','final_roles':len(finals),'failed_attempts':len(failed),'agents':len(agents)}))
