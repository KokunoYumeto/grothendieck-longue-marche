"""Publish genuine completed32 evidence and atomically release the sole capture gate."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
m=read('records/checkpoint32_metrics.json')
estimate=read('records/checkpoint32_size_estimate.json')
visual=read('records/checkpoint32_visual_review.json')
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==estimate['current_main_pdf_sha256']==visual['pdf_sha256']
assert estimate['estimated_total_with_allowance']==502998522<536870912
assert not (root/'records/checkpoint32_size_estimate_run.err').read_bytes()
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_32.zip').exists()
assert not (root/'records/checkpoint32_capture_ready.json').exists()
pause={'recorded_at':datetime.now(timezone.utc).isoformat(),'all_writers_paused':True,
 'scope':'Three owned research/recovery writers paused; all reconstruction/build/render/sizing producers completed. The sole scheduled capture controller11244 is the intended next writer, not an unaccounted research producer. No unrelated system-wide process assertion.',
 'agents':[
 {'agent':'/root/involutions','paused':True,'evidence_time':'2026-11-17T10:50:22.908371+00:00','evidence':'Explicit pause message after individual pages154–160 receipt','owned_live_producers':[]},
 {'agent':'/root/torus_real','paused':True,'evidence_time':'2026-11-17T10:47:30.592981+00:00','evidence':'work_CE/recovery32_pause_status.json','owned_live_producers':[]},
 {'agent':'/root/topology_census','paused':True,'evidence_time':'2026-11-17T10:48:52.711947+00:00','evidence':'Explicit quiescent message after individual pages512–521 receipt','owned_live_producers':[]}],
 'live_producers':[],'sole_capture_control_session':11244,
 'historical_unconfirmed':['old estimator29436 lost execution context','old DEg3:543 lost execution context'],
 'read_only_conversation_audits_after_pause':'CE and DE separately confirmed the integral all-congruence strengthening without tools or filesystem operations.',
 'release_rule':'Release all three immediately after the actual capture exits0, before archive verification or saving.'}
p=root/'records/checkpoint32_writer_pause.json';assert not p.exists();p.write_text(json.dumps(pause,indent=2)+'\n')
helpers=['code/package_checkpoint.py','code/checkpoint_data_tar.py','code/preserve_checkpoint_versions_inductive.py','code/verify_checkpoint_inductive_retention.py','work_DE/checkpoint32_retention_parent_anchor.json','code/estimate_checkpoint32_size.py','code/verify_checkpoint32_system_tars.py','code/check_checkpoint32_preconditions.py','code/capture_checkpoint32.py','code/render_checkpoint32_pdf.py']
reviews=['work_A/review_inductive_retention_reconstruction32.md','work_CE/review_reconstructed_retention_helpers32.txt','work_DE/review_checkpoint32_image_dictionary_recovery.md','work_A/review_checkpoint32_estimator_native_sources.md','work_A/review_estimator_final_prose_diff32.md','work_DE/review_checkpoint32_capture_preconditions32.md','work_DE/review_render_checkpoint32_recovery.md']
p=root/'records/checkpoint32_current_operational_bindings.json';assert not p.exists();p.write_text(json.dumps({'status':'PASS_REVIEWED_CURRENT_SOURCES','helpers':{x:sha(x) for x in helpers},'independent_reviews':{x:sha(x) for x in reviews},'actual_executed_estimator':{'source_sha256':sha('code/estimate_checkpoint32_size.py'),'session_id':42455,'exit_code':0,'output_sha256':sha('records/checkpoint32_size_estimate_run.out'),'record_sha256':sha('records/checkpoint32_size_estimate.json')},'scope':'Source reviews and completed estimation only; future archive verification is not preclaimed.'},indent=2)+'\n')
ready={'ready':True,'recorded_at':datetime.now(timezone.utc).isoformat(),'pdf_sha256':m['pdf_sha256'],
 'main_A':'Open','main_B':'Open','actual_CM_parity':'Open',
 'observed_producer_completions':[
 {'producer':'checkpoint31 restore and three checked system TAR extractions','session_id':92434,'exit_code':0},
 {'producer':'fresh restored31 logical audit','session_id':51534,'exit_code':0},
 {'producer':'actual64MiB parent image stream measurement','session_id':28137,'exit_code':0},
 {'producer':'final combined build with stabilization','session_id':66120,'exit_code':0},
 {'producer':'fresh347-statement metrics','tool_chunk':'d934f3','exit_code':0},
 {'producer':'final combined PDF render','session_id':20122,'exit_code':0},
 {'producer':'final visual/log binding','tool_chunk':'6f3fec','exit_code':0},
 {'producer':'actual prospective three-container estimator','session_id':42455,'exit_code':0}],
 'failed_attempts_preserved':'System missing-format build and three A101 delimiter-stage failures; official runtime initial fallbacks; first A5 attempt missing numeric exit status.',
 'historical_unconfirmed':pause['historical_unconfirmed'],
 'estimate_bytes_with_allowance':estimate['estimated_total_with_allowance'],
 'formal_statements':347,'formal_pages':611,'unpromoted_late_research':'Complete all-signed-congruence hexagon proof plus all recovered outage sources, with scope and supersession records.',
 'no_new_zip_yet':True,'next_scheduled_review':'2026-11-17 11:49:30 UTC'}
target=root/'records/checkpoint32_capture_ready.json'
tmp=root/'records/checkpoint32_capture_ready.pending'
assert not tmp.exists();tmp.write_text(json.dumps(ready,indent=2)+'\n')
os.replace(tmp,target)
print('Readiness atomically published; sole scheduled capture controller may now proceed.',flush=True)
