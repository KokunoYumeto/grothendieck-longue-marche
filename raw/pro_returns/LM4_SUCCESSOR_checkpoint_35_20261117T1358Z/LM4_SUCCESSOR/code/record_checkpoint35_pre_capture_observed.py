"""Record root's actual completed tool observations and three explicit pauses."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--pauses',nargs=3,required=True);args=parser.parse_args()
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def producer(role,chunk,paths,session=None,initial=None):
    row=dict(role=role,exit_code=0,tool_chunk=chunk,evidence=[bound(p) for p in paths])
    if session is not None:row['session_id']=session
    if initial is not None:row['initial_tool_chunk']=initial
    return row

build_paths=['records/checkpoint35_corrected_build_driver.out','records/checkpoint35_corrected_build_driver.err',
 'LM4_SUCCESSOR_paper.pdf','LM4_SUCCESSOR_paper.log','records/checkpoint35_final_pdf_audit.json']
build=producer('final_build','b110b3',build_paths,32067,'618308')
build.update(stdout=bound(build_paths[0]),stderr=bound(build_paths[1]))
assert build['stdout']['bytes']>0 and build['stderr']['bytes']==0
producers=[build,
 producer('final_metrics','22da27',['records/checkpoint35_metrics.json']),
 producer('final_render','25b4df',['records/pdf_qa/checkpoint35_final/render_manifest.json','records/checkpoint35_render_run.out','records/checkpoint35_render_run.err'],75267,'73259c'),
 producer('final_pdf_audit','4e4eef',['records/checkpoint35_final_pdf_audit.json']),
 producer('final_visual_record','ed341d',['records/checkpoint35_visual_review.json','records/checkpoint35_root_visual_observations.json','records/checkpoint35_typesetting.txt']),
 producer('final_size_estimate','faadbe',['records/checkpoint35_size_estimate.json','records/checkpoint35_size_estimate_run.out','records/checkpoint35_size_estimate_run.err'],38880,'4e6606')]
assert bound('records/checkpoint35_size_estimate.json')['sha256']=='0175187ff12f31c3361eaa82fe2562f5361ddf62c5a6d94e51784e4fb9333bb3'
assert bound('records/checkpoint35_size_estimate_run.out')['sha256']=='a9a40fec67f296c0e132322cd266ca980fc06f6551aa62157fa24b3738715b37'
assert bound('records/checkpoint35_size_estimate_run.err')['bytes']==0
assert bound('LM4_SUCCESSOR_paper.pdf')['sha256']=='fc8b22184ee554e6586974df2e31a9b049622bdd700f58992cb0f4e74154b12f'
agents=[];now=datetime.now(timezone.utc)
for rel in args.pauses:
    item=json.loads((root/rel).read_text())
    assert item['paused'] is True and item['owned_live_producers']==[]
    stamp=datetime.fromisoformat(item['paused_at'])
    assert stamp.tzinfo is not None and stamp.utcoffset().total_seconds()==0 and stamp<=now
    agents.append(dict(agent=item['agent'],paused=True,paused_at=item['paused_at'],owned_live_producers=[],evidence=[bound(rel)]))
assert {a['agent'] for a in agents}=={'/root/involutions','/root/torus_real','/root/topology_census'}
failed=dict(role='first_build',exit_code=1,session_id=76561,initial_tool_chunk='7abbe4',tool_chunk='a661f2',
 failure_scope='Actual first build failed its overflow assertion on8.56215pt and11.13672pt. Complete edition, sources, manifests and logs preserved; only the two independently reviewed local line-break corrections followed.',
 evidence=[bound(p) for p in ['records/checkpoint35_build_driver.out','records/checkpoint35_build_driver.err',
   'records/checkpoint35_layout_correction.json','records/pdf_qa/checkpoint35_first_layout/LM4_SUCCESSOR_paper.pdf',
   'records/pdf_qa/checkpoint35_first_layout/LM4_SUCCESSOR_paper.log']])
record=dict(recorded_at=now.isoformat(),root_observed_actual_exit_codes=True,
 observed_producer_completions=producers,prior_failed_attempts=[failed],agents=agents,live_producers=[],
 operational_source_review=bound('records/checkpoint35_operational_source_review.json'),
 publisher_review=bound('work_A/review_checkpoint35_capture_readiness_helpers.json'),
 other_observed_operations=[dict(role='proof_integration',exit_code=0,tool_chunk='a38f7e'),
   dict(role='layout_manifest_binding',exit_code=0,tool_chunk='81e379'),
   dict(role='operational_source_binding',exit_code=0,tool_chunk='6da48a'),
   dict(role='parent_anchor',exit_code=0,session_id=91802,tool_chunk='4c8c16')],
 observation_scope='The exact tool chunks/sessions above were actually observed by root. File existence or empty stderr is not used to infer an exit code. The three pause receipts are each explicit writer attestations. All task-owned build/render/size processes have completed; no statement about unrelated system processes is made.',
 archive_scope='No checkpoint35 ZIP exists yet. The sole scheduled capture, independent closed-child verifications and save remain future operations. Release all writers immediately after actual sole capture exit0, before any verification or saving.')
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_35.zip').exists()
with (root/'records/checkpoint35_pre_capture_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print('Recorded six real successful final producer roles, one preserved real failed build, and three explicit writer pauses.')
