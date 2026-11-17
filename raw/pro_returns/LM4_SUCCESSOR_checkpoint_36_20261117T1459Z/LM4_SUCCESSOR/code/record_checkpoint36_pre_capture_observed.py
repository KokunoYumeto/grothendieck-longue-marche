"""Bind six actual final producer roles and three explicit writer pauses."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--pauses',nargs=3,required=True)
parser.add_argument('--size-chunk',required=True)
parser.add_argument('--size-session',type=int)
parser.add_argument('--size-initial')
parser.add_argument('--source-binding-chunk',required=True)
parser.add_argument('--publisher-review',required=True)
args=parser.parse_args()
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def producer(role,chunk,paths,session=None,initial=None):
    row=dict(role=role,exit_code=0,tool_chunk=chunk,evidence=[bound(p) for p in paths])
    if session is not None:row['session_id']=session
    if initial is not None:row['initial_tool_chunk']=initial
    return row
build_paths=['records/checkpoint36_build_driver.out','records/checkpoint36_build_driver.err',
 'LM4_SUCCESSOR_paper.pdf','LM4_SUCCESSOR_paper.log','records/checkpoint36_final_pdf_audit.json']
build=producer('final_build','cfd675',build_paths,42125,'c663f0')
build.update(stdout=bound(build_paths[0]),stderr=bound(build_paths[1]))
assert build['stdout']['bytes']>0 and build['stderr']['bytes']==0
producers=[build,
 producer('final_metrics','b0cb76',['records/checkpoint36_metrics.json','records/checkpoint36_metrics_run.out','records/checkpoint36_metrics_run.err'],68954,'cf480f'),
 producer('final_render','93719d',['records/pdf_qa/checkpoint36_final/render_manifest.json','records/checkpoint36_render_run.out','records/checkpoint36_render_run.err'],7478,'4e7415'),
 producer('final_pdf_audit','948efe',['records/checkpoint36_final_pdf_audit.json','records/checkpoint36_final_pdf_audit_run.out','records/checkpoint36_final_pdf_audit_run.err']),
 producer('final_visual_record','f4f576',['records/checkpoint36_visual_review.json','records/checkpoint36_root_visual_observations.json','records/checkpoint36_typesetting.txt','records/checkpoint36_visual_finalize_run.out','records/checkpoint36_visual_finalize_run.err']),
 producer('final_size_estimate',args.size_chunk,['records/checkpoint36_size_estimate.json','records/checkpoint36_size_estimate_run.out','records/checkpoint36_size_estimate_run.err'],args.size_session,args.size_initial)]
assert bound('records/checkpoint36_size_estimate_run.err')['bytes']==0
assert bound('LM4_SUCCESSOR_paper.pdf')['sha256']=='2124bdcf0bc9e3fc34f0bb69d2c232ef216f94ab56ed3afae7045cbea275add1'
estimate=json.loads((root/'records/checkpoint36_size_estimate.json').read_text())
assert estimate['estimated_total_with_allowance']<536870912
assert estimate['header_manifest_retention_late_text_allowance_bytes']==5000000
agents=[];now=datetime.now(timezone.utc)
for rel in args.pauses:
    item=json.loads((root/rel).read_text())
    assert item['paused'] is True and item['owned_live_producers']==[]
    stamp=datetime.fromisoformat(item['paused_at'])
    assert stamp.tzinfo is not None and stamp.utcoffset().total_seconds()==0 and stamp<=now
    agents.append(dict(agent=item['agent'],paused=True,paused_at=item['paused_at'],owned_live_producers=[],evidence=[bound(rel)]))
assert {a['agent'] for a in agents}=={'/root/involutions','/root/torus_real','/root/topology_census'}
failed=dict(role='initial_128_size_estimate',exit_code=1,session_id=26477,initial_tool_chunk='15f6e4',tool_chunk='00e3f0',
 failure_scope='All three exact prospective component encodings completed and the full report was saved; actual exit1 occurred only at the unchanged final delivery-cap assertion. Entire report/stdout/stderr preserved. This is not a failed mathematical build.',
 evidence=[bound('records/checkpoint36_first_size_estimate/'+name) for name in ['checkpoint36_size_estimate.json','checkpoint36_size_estimate_run.out','checkpoint36_size_estimate_run.err']]+[bound('records/checkpoint36_first_size_observed.json')])
record=dict(recorded_at=now.isoformat(),root_observed_actual_exit_codes=True,
 observed_producer_completions=producers,prior_failed_attempts=[failed],agents=agents,live_producers=[],
 operational_source_review=bound('records/checkpoint36_operational_source_review.json'),
 publisher_review=bound(args.publisher_review),
 other_observed_operations=[dict(role='proof_integration',exit_code=0,tool_chunk='7d63c7'),
   dict(role='operational_source_binding',exit_code=0,tool_chunk=args.source_binding_chunk),
   dict(role='parent_anchor',exit_code=0,session_id=82229,initial_tool_chunk='9dbec8',tool_chunk='0691ea'),
   dict(role='root_visual_receipt',exit_code=0,tool_chunk='8fd3ab'),
   dict(role='prescribed_D8_control',exit_code=0,tool_chunk='49abf9')],
 observation_scope='The six exact final tool results above were observed by root. File existence or empty stderr is never used to infer an exit. Component measurements performed by CE retain their separate named observer, actual session, tool result and full-output receipts. The final accounting producer binds those actual measurements. All task-owned build/render/compression/accounting processes are complete; three explicit pause receipts attest to writers, not unrelated system processes.',
 archive_scope='No checkpoint36 ZIP exists. Sole scheduled capture, closed-child verification and save remain future operations. Release all three writers immediately after actual capture exit0, before any post-closure operation.')
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_36.zip').exists()
with (root/'records/checkpoint36_pre_capture_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print('Recorded six actually successful final roles, preserved initial size exit1, and three explicit writer pauses.')
