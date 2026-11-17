"""Publish checkpoint36 readiness from complete actual evidence, without execution guesses.

Source-only until root runs it. Six unique final roles, current source reviews,
and three explicit writer pauses are mandatory. Final PDF and process identifiers
come from bound current metrics and root's actual observations. Failed attempts,
if any, are preserved separately; no earlier checkpoint's failure is assumed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import re


def main():
    root = Path(__file__).resolve().parents[1]
    cap = 536870912
    parent_sha = '33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'
    now = datetime.now(timezone.utc)

    def read(rel):
        return json.loads((root / rel).read_text())

    def sha(rel):
        return hashlib.sha256((root / rel).read_bytes()).hexdigest()

    def evidence(item):
        assert isinstance(item, dict), 'Evidence must be a bound file record.'
        rel = item['path']
        assert isinstance(rel, str) and rel
        path = Path(rel)
        assert not path.is_absolute() and '..' not in path.parts
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

    def observed_identity(row):
        chunk = row.get('tool_chunk')
        assert isinstance(chunk, str) and re.fullmatch(r'[0-9a-f]+', chunk), row
        if 'session_id' in row:
            assert isinstance(row['session_id'], int) and row['session_id'] > 0
        assert isinstance(row['exit_code'], int)

    observation_path = 'records/checkpoint36_pre_capture_observed.json'
    observed = read(observation_path)
    assert observed['root_observed_actual_exit_codes'] is True
    producers = observed['observed_producer_completions']
    assert isinstance(producers, list) and producers
    by_role = {row['role']: row for row in producers}
    assert len(by_role) == len(producers), 'Producer roles must be unique.'
    required = {
        'final_build': set(),
        'final_metrics': {'records/checkpoint36_metrics.json'},
        'final_render': {'records/pdf_qa/checkpoint36_final/render_manifest.json'},
        'final_pdf_audit': {'records/checkpoint36_final_pdf_audit.json'},
        'final_visual_record': {'records/checkpoint36_visual_review.json'},
        'final_size_estimate': {'records/checkpoint36_size_estimate.json',
            'records/checkpoint36_size_estimate_run.out',
            'records/checkpoint36_size_estimate_run.err'},
    }
    assert set(by_role) == set(required), 'Require exactly the six final roles.'
    for role, required_files in required.items():
        row = by_role[role]
        observed_identity(row)
        assert row['exit_code'] == 0, role
        assert required_files <= evidence_list(row['evidence']), role
    build = by_role['final_build']
    build_stdout = evidence(build['stdout'])
    build_stderr = evidence(build['stderr'])
    assert build_stdout != build_stderr
    assert {build_stdout, build_stderr} <= evidence_list(build['evidence'])
    assert (root / build_stdout).stat().st_size > 0
    assert not (root / build_stderr).read_bytes()
    assert not (root / 'records/checkpoint36_size_estimate_run.err').read_bytes()

    failed_attempts = observed.get('prior_failed_attempts', [])
    assert isinstance(failed_attempts, list)
    for row in failed_attempts:
        observed_identity(row)
        assert row['exit_code'] != 0
        assert isinstance(row['role'], str) and row['role']
        assert isinstance(row['failure_scope'], str) and row['failure_scope']
        evidence_list(row['evidence'])

    agents = observed['agents']
    expected_agents = {'/root/involutions', '/root/torus_real', '/root/topology_census'}
    assert isinstance(agents, list) and len(agents) == 3
    assert {a['agent'] for a in agents} == expected_agents
    for agent in agents:
        assert agent['paused'] is True and agent['owned_live_producers'] == []
        stamp = datetime.fromisoformat(agent['paused_at'])
        assert stamp.tzinfo is not None and stamp.utcoffset().total_seconds() == 0
        assert stamp <= now
        evidence_list(agent['evidence'])
    assert observed['live_producers'] == [], 'Task-owned producers must have completed.'

    metrics = read('records/checkpoint36_metrics.json')
    estimate = read('records/checkpoint36_size_estimate.json')
    visual = read('records/checkpoint36_visual_review.json')
    render = read('records/pdf_qa/checkpoint36_final/render_manifest.json')
    audit = read('records/checkpoint36_final_pdf_audit.json')
    expected_pdf = metrics['pdf_sha256']
    assert re.fullmatch(r'[0-9a-f]{64}', expected_pdf)
    assert sha('LM4_SUCCESSOR_paper.pdf') == expected_pdf
    assert (root / 'LM4_SUCCESSOR_paper.pdf').stat().st_size == metrics['pdf_bytes']
    assert estimate['current_main_pdf_sha256'] == expected_pdf
    assert visual['pdf_sha256'] == render['pdf_sha256'] == audit['final_pdf_sha256'] == expected_pdf
    assert metrics['statements'] == 383 and metrics['pages'] == render['page_count'] > 0
    assert metrics['task_rows'] == 49 and metrics['bibliography_entries'] == 117
    assert metrics['statuses'] == {'Known': 6, 'Proved': 339, 'Refuted': 19, 'Open': 19}
    assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
    assert visual['visual_review'] == 'PASS' and audit['result'] == 'PASS_FINAL_LOGS'
    assert audit['final_overfull_count'] == 0
    assert render['dpi'] == 144
    assert visual['required_math_pages'] == render['required_new_mathematical_pages']
    assert visual['required_editorial_pages'] == render['required_editorial_pages']
    assert visual['required_individual_pages'] == render['required_individual_pages']
    assert set(render['required_individual_pages']) <= set(visual['individually_inspected_pages'])
    assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == cap
    assert estimate['baseline_archive'] == 'LM4_SUCCESSOR_checkpoint_35.zip'
    assert estimate['baseline_bytes'] == 530938760 and estimate['baseline_sha256'] == parent_sha
    assert not estimate['creates_zip'] and not estimate['writes_authored_input_files']
    assert estimate['header_manifest_retention_late_text_allowance_bytes'] == 5000000
    assert estimate['previous_direct_main_pdf_headers_removed'] == 0
    for kind, dictionary in [('images', 268435456), ('documents', 134217728), ('data', 67108864)]:
        assert estimate['prospective_bundles'][kind]['dictionary_bytes'] == dictionary
        assert estimate['prospective_bundles'][kind]['zip_method'] == 'ZIP_LZMA'
    migrated = estimate['previous_direct_main_pdf_migrated']
    removed = estimate['previous_direct_main_pdf_compressed_payload_removed']
    assert removed == (0 if migrated is None else migrated['compressed_payload_bytes'])
    assert not (root.parent / 'LM4_SUCCESSOR_checkpoint_36.zip').exists()

    formal_review_path = 'records/checkpoint36_root_formal_reviews.json'
    formal = read(formal_review_path)
    assert formal['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
    assert [r['statement'] for r in formal['copies']] == ['A.'+str(n) for n in range(120,126)]+['B.'+str(n) for n in range(169,174)]
    assert read('records/checkpoint36_formal_source_copies.json')['copies'] == formal['copies']
    for row in formal['copies']:
        assert (root / row['source']).read_bytes() == (root / row['target']).read_bytes()
        assert sha(row['target']) == row['sha256']
    for rel, digest in formal['independent_reviews'].items():
        assert sha(rel) == digest, rel
    assert sha(formal['bibliography']['path']) == formal['bibliography']['sha256']

    helper_paths = {
        'code/package_checkpoint.py', 'code/checkpoint_data_tar.py', 'code/checkpoint_image_tar.py',
        'code/preserve_checkpoint36_versions_inductive.py',
        'code/verify_checkpoint36_inductive_retention.py',
        'code/build_checkpoint36_parent_anchor.py',
        'code/estimate_checkpoint36_size.py', 'code/verify_checkpoint36_system_tars.py',
        'code/check_checkpoint36_preconditions.py', 'code/capture_checkpoint36.py',
        'code/render_checkpoint36_pdf.py', 'code/audit_checkpoint36_final_pdf.py',
        'code/finalize_checkpoint36_visual_record.py', 'code/publish_checkpoint36_readiness.py',
    }
    source_review_path = evidence(observed['operational_source_review'])
    source_review = read(source_review_path)
    assert source_review['result'] == 'PASS_COMPLETE_SOURCE_REVIEW'
    assert helper_paths <= evidence_list(source_review['sources'])
    independent_paths = evidence_list(source_review['independent_reviews'])
    publisher_review_path = evidence(observed['publisher_review'])
    publisher_review = read(publisher_review_path)
    assert publisher_review['result'].startswith('PASS')
    assert publisher_review['source']['path'] == 'code/publish_checkpoint36_readiness.py'
    evidence(publisher_review['source'])
    independent_paths.add(publisher_review_path)
    independent_paths.add(source_review_path)

    anchor_path = 'records/checkpoint36_retention_parent_anchor.json'
    anchor = read(anchor_path)
    assert anchor['parent_number'] == 35 and anchor['child_number'] == 36
    assert anchor['archive_bytes'] == 530938760 and anchor['archive_sha256'] == parent_sha
    assert anchor['logical_entries'] == 10746 and anchor['inherited_rows'] == 163040
    assert anchor['inherited_archives'] == 34
    for item in anchor['trusted_coverage']['verification_records'].values():
        assert item['actual_exit_code_observed'] == 0
        evidence(item)
    helper_paths.add(anchor_path)
    binding = dict(status='PASS_REVIEWED_CURRENT_SOURCES',
        helpers={rel: sha(rel) for rel in sorted(helper_paths)},
        independent_reviews={rel: sha(rel) for rel in sorted(independent_paths)},
        observed_record=dict(path=observation_path, sha256=sha(observation_path)),
        actual_size_estimate=by_role['final_size_estimate'],
        prior_failed_attempts=failed_attempts,
        scope='Current source reviews and actual completed pre-capture evidence only; no future archive verification is preclaimed.')
    pause = dict(recorded_at=now.isoformat(), all_writers_paused=True,
        scope='The three named research writers and all task-owned producers only; no assertion about unrelated system processes.',
        agents=agents, live_producers=[], source_observation_sha256=sha(observation_path),
        release_rule='Release immediately after actual sole capture exit0, before verification or saving.')
    ready = dict(ready=True, recorded_at=now.isoformat(), pdf_sha256=expected_pdf,
        main_A='Open', main_B='Open', actual_CM_parity='Open',
        observed_producer_completions=producers, prior_failed_attempts=failed_attempts,
        estimate_bytes_with_allowance=estimate['estimated_total_with_allowance'],
        formal_statements=383, formal_pages=metrics['pages'], bibliography_entries=117,
        no_new_zip_yet=True, next_scheduled_review='2026-11-17 15:49:30 UTC',
        source_observation_sha256=sha(observation_path),
        unpromoted_late_research='Actual elliptic and complementary contact comparisons retain their exact scopes; both main decisions, the boundary condition, the coherent class, and actual CM parity remain open.')
    outputs = ['records/checkpoint36_writer_pause.json',
               'records/checkpoint36_current_operational_bindings.json',
               'records/checkpoint36_capture_ready.json',
               'records/checkpoint36_capture_ready.pending']
    assert all(not (root / rel).exists() for rel in outputs), 'Preserve any earlier partial publication.'
    for rel, data in [(outputs[0], pause), (outputs[1], binding)]:
        with (root / rel).open('x') as stream:
            json.dump(data, stream, indent=2)
            stream.write('\n')
    with (root / outputs[3]).open('x') as stream:
        json.dump(ready, stream, indent=2)
        stream.write('\n')
    os.replace(root / outputs[3], root / outputs[2])
    print('Checkpoint36 readiness atomically published from six actual completed roles and three explicit writer pauses.', flush=True)


if __name__ == '__main__':
    main()
