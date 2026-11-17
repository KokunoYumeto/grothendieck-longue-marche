"""Publish readiness only from observed completed producers and explicit writer pauses."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
m=read('records/checkpoint33_metrics.json')
estimate=read('records/checkpoint33_size_estimate.json')
visual=read('records/checkpoint33_visual_review.json')
observed=read('records/checkpoint33_pre_capture_observed.json')
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==estimate['current_main_pdf_sha256']==visual['pdf_sha256']
assert m['statements']==354 and m['pages']==626
assert estimate['estimated_total_with_allowance']<536870912
assert not (root/'records/checkpoint33_size_estimate_run.err').read_bytes()
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_33.zip').exists()
assert not (root/'records/checkpoint33_capture_ready.json').exists()
assert observed['root_observed_actual_exit_codes'] is True
producers=observed['observed_producer_completions']
assert producers and all(p['exit_code']==0 for p in producers)
by_role={p['role']:p for p in producers}
assert len(by_role)==len(producers),'Producer roles must be unique.'
required={
 'final_build':('session_id',14597),
 'final_metrics':('tool_chunk','1d5a60'),
 'final_render':('session_id',38640),
 'corrected_pdf_audit':('tool_chunk','22a4de'),
 'final_visual_record':('tool_chunk','ac574f'),
 'final_size_estimate':('session_id',47557),
}
for role,(key,identifier) in required.items():
    assert role in by_role and by_role[role].get(key)==identifier,(role,key,identifier)
    assert by_role[role]['exit_code']==0
estimator_observed=by_role['final_size_estimate']
assert len(observed['agents'])==3
assert {a['agent'] for a in observed['agents']}=={'/root/involutions','/root/torus_real','/root/topology_census'}
assert all(a['paused'] and a['evidence'] and not a['owned_live_producers'] for a in observed['agents'])
assert not observed['live_producers']
pause=dict(recorded_at=datetime.now(timezone.utc).isoformat(),all_writers_paused=True,
    scope='All three research writers explicitly paused after saving their completed work; all root-owned build, render and size producers have actual observed completion. No assertion about unrelated system processes.',
    agents=observed['agents'],live_producers=[],
    release_rule='Release all three immediately after actual sole capture exit0, before verification or saving.',
    historical_unconfirmed=['old estimator29436 lost execution context','old DEg3:543 lost execution context'])
p=root/'records/checkpoint33_writer_pause.json';assert not p.exists();p.write_text(json.dumps(pause,indent=2)+'\n')
helpers=['code/package_checkpoint.py','code/checkpoint_data_tar.py','code/preserve_checkpoint33_versions_inductive.py',
 'code/verify_checkpoint33_inductive_retention.py','records/checkpoint33_retention_parent_anchor.json',
 'code/estimate_checkpoint33_size.py','code/verify_checkpoint33_system_tars.py','code/check_checkpoint33_preconditions.py',
 'code/capture_checkpoint33.py','code/render_checkpoint33_pdf.py','code/audit_checkpoint33_corrected_pdf.py',
 'code/finalize_checkpoint33_visual_record.py','code/publish_checkpoint33_readiness.py']
reviews=['work_DE/review_checkpoint33_helpers_full_source.md','work_DE/checkpoint33_capture_helpers_source_manifest.json',
 'work_A/review_checkpoint33_capture_helpers.md','work_A/review_checkpoint33_capture_helpers.json']
binding=dict(status='PASS_REVIEWED_CURRENT_SOURCES',helpers={x:sha(x) for x in helpers},
    independent_reviews={x:sha(x) for x in reviews},
    actual_executed_estimator=dict(source_sha256=sha('code/estimate_checkpoint33_size.py'),session_id=estimator_observed['session_id'],
        exit_code=estimator_observed['exit_code'],output_sha256=sha('records/checkpoint33_size_estimate_run.out'),record_sha256=sha('records/checkpoint33_size_estimate.json')),
    scope='Completed source, document, and actual compression evidence only. No future capture verification is preclaimed.')
p=root/'records/checkpoint33_current_operational_bindings.json';assert not p.exists();p.write_text(json.dumps(binding,indent=2)+'\n')
ready=dict(ready=True,recorded_at=datetime.now(timezone.utc).isoformat(),pdf_sha256=m['pdf_sha256'],
    main_A='Open',main_B='Open',actual_CM_parity='Open',
    observed_producer_completions=observed['observed_producer_completions'],
    prior_stopped_producer=dict(session_id=88588,actual_exit_code=130,
        reason='Stopped before corrected-PDF estimation; first output preserved in abstract-firstpass directory. No ZIP opened.'),
    estimate_bytes_with_allowance=estimate['estimated_total_with_allowance'],formal_statements=354,formal_pages=626,
    unpromoted_late_research='Complete separately reviewed relative-central congruence, original r-frame cohomology, and whole family/filling cohomology research; exact scopes and residual gates retained.',
    no_new_zip_yet=True,next_scheduled_review='2026-11-17 12:49:30 UTC')
target=root/'records/checkpoint33_capture_ready.json';tmp=root/'records/checkpoint33_capture_ready.pending'
assert not tmp.exists();tmp.write_text(json.dumps(ready,indent=2)+'\n');os.replace(tmp,target)
print('Readiness atomically published from actual completed producer evidence and explicit writer pauses.',flush=True)
