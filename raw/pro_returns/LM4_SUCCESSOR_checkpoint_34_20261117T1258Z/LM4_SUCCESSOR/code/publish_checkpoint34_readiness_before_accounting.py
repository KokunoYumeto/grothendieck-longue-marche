"""Publish checkpoint34 readiness only from actual completed observations.

Source-only until root runs it. The observation JSON must contain six unique
required producer roles, the actual failed first build, three explicit writer
pauses, and nonempty hash-bound evidence lists. No earlier slot's producer,
stopped-session claim, or empty all-zero test is accepted.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import re


def main():
    root = Path(__file__).resolve().parents[1]
    expected_pdf = '566fc1211d2e328880a7fcce96b0da0ce4856d9809b554ff40155c3cf035f423'
    cap = 536870912

    def read(rel):
        return json.loads((root / rel).read_text())

    def sha(rel):
        return hashlib.sha256((root / rel).read_bytes()).hexdigest()

    def evidence(item):
        assert isinstance(item, dict), 'Evidence must be a bound file record.'
        rel = item['path']
        path = Path(rel)
        assert isinstance(rel, str) and rel and not path.is_absolute()
        assert '..' not in path.parts
        assert re.fullmatch(r'[0-9a-f]{64}', item['sha256'])
        assert isinstance(item['bytes'], int) and item['bytes'] >= 0
        assert (root / rel).is_file(), rel
        assert (root / rel).stat().st_size == item['bytes'], rel
        assert sha(rel) == item['sha256'], rel
        return rel

    def evidence_list(items):
        assert isinstance(items, list) and items, 'Evidence may not be empty.'
        paths = [evidence(item) for item in items]
        assert len(paths) == len(set(paths)), 'Duplicate evidence path.'
        return set(paths)

    def observed_chunk(row):
        chunk = row.get('tool_chunk')
        assert isinstance(chunk, str) and re.fullmatch(r'[0-9a-f]+', chunk), row['role']

    observation_path = 'records/checkpoint34_pre_capture_observed.json'
    observed = read(observation_path)
    assert observed['root_observed_actual_exit_codes'] is True
    producers = observed['observed_producer_completions']
    assert isinstance(producers, list) and producers
    by_role = {row['role']: row for row in producers}
    assert len(by_role) == len(producers), 'Producer roles must be unique.'
    required = {
        'final_build': ({'session_id': 98925, 'tool_chunk': 'c06201'}, {
            'records/checkpoint34_corrected_build_driver.out',
            'records/checkpoint34_corrected_build_driver.err'}),
        'final_metrics': ({'tool_chunk': '940ea7'}, {'records/checkpoint34_metrics.json'}),
        'final_render': ({'session_id': 93609, 'tool_chunk': '0bf9df'}, {
            'records/pdf_qa/checkpoint34_final/render_manifest.json'}),
        'final_pdf_audit': ({'tool_chunk': '6fdbad'}, {'records/checkpoint34_final_pdf_audit.json'}),
        'final_visual_record': ({'tool_chunk': '26a572'}, {'records/checkpoint34_visual_review.json'}),
        'final_size_estimate': ({'session_id': 55851}, {
            'records/checkpoint34_size_estimate.json',
            'records/checkpoint34_size_estimate_run.out',
            'records/checkpoint34_size_estimate_run.err'}),
    }
    assert set(by_role) == set(required), 'Require exactly the six final roles.'
    for role, (identifiers, required_files) in required.items():
        row = by_role[role]
        assert row['exit_code'] == 0, role
        observed_chunk(row)
        for key, value in identifiers.items():
            assert row.get(key) == value, (role, key, value)
        assert required_files <= evidence_list(row['evidence']), role

    failed = observed['prior_failed_build']
    assert failed['session_id'] == 46912 and failed['exit_code'] == 1
    assert {
        'records/pdf_qa/checkpoint34_first_layout/records/checkpoint34_build_driver.out',
        'records/pdf_qa/checkpoint34_first_layout/records/checkpoint34_build_driver.err',
    } <= evidence_list(failed['evidence'])

    agents = observed['agents']
    expected_agents = {'/root/involutions', '/root/torus_real', '/root/topology_census'}
    assert isinstance(agents, list) and len(agents) == 3
    assert {a['agent'] for a in agents} == expected_agents
    now = datetime.now(timezone.utc)
    for agent in agents:
        assert agent['paused'] is True and agent['owned_live_producers'] == []
        stamp = datetime.fromisoformat(agent['paused_at'])
        assert stamp.tzinfo is not None and stamp.utcoffset().total_seconds() == 0
        assert stamp <= now
        evidence_list(agent['evidence'])
    assert observed['live_producers'] == [], 'Task-owned producers must have completed.'

    metrics = read('records/checkpoint34_metrics.json')
    estimate = read('records/checkpoint34_size_estimate.json')
    visual = read('records/checkpoint34_visual_review.json')
    render = read('records/pdf_qa/checkpoint34_final/render_manifest.json')
    audit = read('records/checkpoint34_final_pdf_audit.json')
    assert sha('LM4_SUCCESSOR_paper.pdf') == expected_pdf
    assert metrics['pdf_sha256'] == estimate['current_main_pdf_sha256'] == expected_pdf
    assert visual['pdf_sha256'] == render['pdf_sha256'] == audit['final_pdf_sha256'] == expected_pdf
    assert metrics['statements'] == 362 and metrics['pages'] == render['page_count'] == 646
    assert metrics['task_rows'] == 49 and metrics['bibliography_entries'] == 116
    assert metrics['statuses'] == {'Known': 6, 'Proved': 318, 'Refuted': 19, 'Open': 19}
    assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
    assert visual['visual_review'] == 'PASS' and audit['result'] == 'PASS_FINAL_LOGS'
    assert audit['first34_overfull_count'] == 1 and audit['final_overfull_count'] == 0
    assert set(render['required_new_mathematical_pages']) <= set(visual['individually_inspected_pages'])
    assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == cap
    assert estimate['baseline_archive'] == 'LM4_SUCCESSOR_checkpoint_33.zip'
    assert estimate['baseline_bytes'] == 508499680
    assert estimate['baseline_sha256'] == '5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96'
    assert not estimate['creates_zip'] and not estimate['writes_authored_input_files']
    for kind, size in [('images', 67108864), ('documents', 8388608), ('data', 67108864)]:
        assert estimate['prospective_bundles'][kind]['dictionary_bytes'] == size
        assert estimate['prospective_bundles'][kind]['zip_method'] == 'ZIP_LZMA'
    assert not (root / 'records/checkpoint34_corrected_build_driver.err').read_bytes()
    assert not (root / 'records/checkpoint34_size_estimate_run.err').read_bytes()
    assert not (root.parent / 'LM4_SUCCESSOR_checkpoint_34.zip').exists()

    five_review = read('work_CE/review_checkpoint34_five_helpers.json')
    assert five_review['result'] == 'PASS_COMPLETE_SOURCE_ONLY_REVIEW'
    for rel, digest in five_review['inputs'].items():
        assert sha(rel) == digest, rel
    capture_review = read('work_CE/review_checkpoint34_capture_helpers.json')
    assert capture_review['result'] == 'PASS' and capture_review['entire_sources_and_diff_read']
    for item in capture_review['sources']:
        evidence(item)
    final_review = read('work_CE/review_checkpoint34_final_audit_visual_sources.json')
    assert final_review['result'] == 'PASS' and final_review['entire_sources_read']
    for item in final_review['sources']:
        evidence(item)
    publisher_review_path = evidence(observed['publisher_review'])
    publisher_review = read(publisher_review_path)
    assert publisher_review['result'].startswith('PASS')
    assert publisher_review['source']['path'] == 'code/publish_checkpoint34_readiness.py'
    evidence(publisher_review['source'])

    helpers = [
        'code/package_checkpoint.py', 'code/checkpoint_data_tar.py',
        'code/preserve_checkpoint34_versions_inductive.py',
        'code/verify_checkpoint34_inductive_retention.py',
        'code/build_checkpoint34_parent_anchor.py',
        'records/checkpoint34_retention_parent_anchor.json',
        'code/estimate_checkpoint34_size.py', 'code/verify_checkpoint34_system_tars.py',
        'code/check_checkpoint34_preconditions.py', 'code/capture_checkpoint34.py',
        'code/render_checkpoint34_pdf.py', 'code/audit_checkpoint34_final_pdf.py',
        'code/finalize_checkpoint34_visual_record.py', 'code/publish_checkpoint34_readiness.py',
    ]
    reviews = [
        'work_CE/review_checkpoint34_five_helpers.txt',
        'work_CE/review_checkpoint34_five_helpers.json',
        'work_CE/review_checkpoint34_capture_helpers.txt',
        'work_CE/review_checkpoint34_capture_helpers.json',
        'work_CE/review_checkpoint34_final_audit_visual_sources.txt',
        'work_CE/review_checkpoint34_final_audit_visual_sources.json',
        publisher_review_path,
    ]
    binding = dict(status='PASS_REVIEWED_CURRENT_SOURCES',
        helpers={rel: sha(rel) for rel in helpers},
        independent_reviews={rel: sha(rel) for rel in reviews},
        observed_record=dict(path=observation_path, sha256=sha(observation_path)),
        actual_executed_estimator=dict(
            source_sha256=sha('code/estimate_checkpoint34_size.py'),
            session_id=55851, tool_chunk=by_role['final_size_estimate']['tool_chunk'], exit_code=0,
            output_sha256=sha('records/checkpoint34_size_estimate_run.out'),
            record_sha256=sha('records/checkpoint34_size_estimate.json')),
        scope='Source reviews and actual completed pre-capture evidence only; no future archive verification is preclaimed.')
    pause = dict(recorded_at=now.isoformat(), all_writers_paused=True,
        scope='The three named research writers and all task-owned producers only; no assertion about unrelated system processes.',
        agents=agents, live_producers=[],
        source_observation_sha256=sha(observation_path),
        release_rule='Release immediately after actual sole capture exit0, before verification or saving.')
    ready = dict(ready=True, recorded_at=now.isoformat(), pdf_sha256=expected_pdf,
        main_A='Open', main_B='Open', actual_CM_parity='Open',
        observed_producer_completions=producers, prior_failed_build=failed,
        prior_failure_scope='The first build actually exited1 on the retained provenance overflow; it is not described as a stopped producer.',
        estimate_bytes_with_allowance=estimate['estimated_total_with_allowance'],
        formal_statements=362, formal_pages=646, bibliography_entries=116,
        no_new_zip_yet=True, next_scheduled_review='2026-11-17 13:49:30 UTC',
        source_observation_sha256=sha(observation_path),
        unpromoted_late_research='Separately reviewed central-refinement, cyclic-centralizer and compact contact-family results retain their exact scopes; the actual main decisions and CM value remain open.')

    outputs = ['records/checkpoint34_writer_pause.json',
               'records/checkpoint34_current_operational_bindings.json',
               'records/checkpoint34_capture_ready.json',
               'records/checkpoint34_capture_ready.pending']
    assert all(not (root / rel).exists() for rel in outputs), 'Preserve any earlier partial publication.'
    for rel, data in [(outputs[0], pause), (outputs[1], binding)]:
        with (root / rel).open('x') as stream:
            json.dump(data, stream, indent=2)
            stream.write('\n')
    with (root / outputs[3]).open('x') as stream:
        json.dump(ready, stream, indent=2)
        stream.write('\n')
    os.replace(root / outputs[3], root / outputs[2])
    print('Checkpoint34 readiness atomically published from six actual completed roles and three explicit writer pauses.', flush=True)


if __name__ == '__main__':
    main()
