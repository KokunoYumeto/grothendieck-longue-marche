from pathlib import Path
from datetime import datetime, timezone
import ast, difflib, hashlib, json
root=Path('/workspace/scratch/a50d05093ca1/LM4_SUCCESSOR')
changes=[]
def publish(name,text):
    path=root/'code'/name
    assert not path.exists(), path
    ast.parse(text, filename=str(path))
    path.write_text(text)
    old=root/'code'/name.replace('35','34')
    diff=''.join(difflib.unified_diff(old.read_text().splitlines(True),text.splitlines(True),fromfile=str(old.relative_to(root)),tofile=str(path.relative_to(root))))
    changes.append((path,old,diff))

s=(root/'code/check_checkpoint34_preconditions.py').read_text()
s=s.replace('checkpoint34','checkpoint35').replace('checkpoint_34','checkpoint_35')
s=s.replace("range(106,112)","range(112,120)").replace("range(165,167)","range(167,169)")
s=s.replace('362','372').replace("'Proved':318","'Proved':328")
s=s.replace("anchor['parent_number']==33 and anchor['child_number']==34","anchor['parent_number']==34 and anchor['child_number']==35")
s=s.replace('checkpoint_33.zip','checkpoint_34.zip').replace('508499680','529409669').replace('5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96','28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb')
s=s.replace('10053','10387').replace('142600','152653').replace("anchor['inherited_archives']==32","anchor['inherited_archives']==33")
s=s.replace("('documents',8388608)","('documents',67108864)")
s=s.replace('thirty_fourth_hour','thirty_fifth_hour').replace('closed33 anchor','closed34 anchor')
s=s.replace("    for item in ready['observed_producer_completions']:\n        assert item['exit_code']==0\n", "    producers=ready['observed_producer_completions']\n    assert len(producers)==6 and {r['role'] for r in producers}=={\n        'final_build','final_metrics','final_render','final_pdf_audit',\n        'final_visual_record','final_size_estimate'}\n    for item in producers:\n        assert item['exit_code']==0 and item['tool_chunk'] and item['evidence']\n    bindings=read('records/checkpoint35_current_operational_bindings.json')\n    assert bindings['status']=='PASS_REVIEWED_CURRENT_SOURCES'\n    for rel,digest in bindings['helpers'].items():\n        assert sha(rel)==digest,rel\n    for rel,digest in bindings['independent_reviews'].items():\n        assert sha(rel)==digest,rel\n")
publish('check_checkpoint35_preconditions.py',s)

s=(root/'code/capture_checkpoint34.py').read_text()
s=s.replace('checkpoint34','checkpoint35').replace('checkpoint_34','checkpoint_35').replace('Scheduled34','Scheduled35').replace('immutable34','immutable35').replace('Immutable34','Immutable35')
s=s.replace('datetime(2026,11,17,12,49,30','datetime(2026,11,17,13,49,30').replace('next_due=datetime(2026,11,17,13,49,30','next_due=datetime(2026,11,17,14,49,30')
s=s.replace('Thirty-fourth','Thirty-fifth').replace('thirty-fourth','thirty-fifth').replace('thirty_fourth','thirty_fifth').replace('progress_review_34h','progress_review_35h')
s=s.replace('362','372').replace('318 Proved','328 Proved').replace('All eight new','All ten new')
s=s.replace("'reason':'Actual first central congruence hexagon and modular conjugacy, quotient factor transporter, cyclic and coherent frame obstructions, and entire deletion/filling cohomology spaces proved; both main problems and actual CM parity remain open.'", "'reason':'Actual central quotient and residual structures, full modular central tower, normalized residual reduction, entire cyclic and involution obstruction spaces, and a strictly larger mixed contact image proved; both main problems and actual CM parity remain open.'")
a=s.index('Open. The same marked hexagon')
b=s.index('\n\nThis is the single34 capture',a)
s=s[:a]+'''Open. The actual central quotient has its complete product and odd
cohomology description. The next modular central refinement, entire central
tower, and nontrivial relatively perfect residual retain genuine quotient
automorphisms and full peripheral lifts at their proved scopes. The
normalized residual reduction retains its five-factor transported pentagon;
no unproved ordinary pentagon is assigned to its new word. Entire cyclic
and involution cohomology retains the original coherent obstruction without
deciding it. The actual single-contact compact family is explicit, and a
prescribed mixed contact word lies outside it; the whole contact-image
equality remains open.'''+s[b:]
s=s.replace('single34 capture','single35 capture').replace('pinned33','pinned34').replace('closed33 certificate','closed34 certificate')
s=s.replace('10053 parent logical entries','10387 parent logical entries').replace('142600 prior','152653 prior').replace('152653 resulting','163040 resulting')
s=s.replace("retained['archives']==33 and retained['archive_entries']==152653","retained['archives']==34 and retained['archive_entries']==163040")
s=s.replace("'code/package_checkpoint.py'),'34'","'code/package_checkpoint.py'),'35'")
s=s.replace('Next review: 2026-11-17 13:49:30 UTC.','Next review: 2026-11-17 14:49:30 UTC.')
publish('capture_checkpoint35.py',s)

publisher=r'''"""Publish checkpoint35 readiness from complete actual evidence, without execution guesses.

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
    parent_sha = '28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb'
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

    observation_path = 'records/checkpoint35_pre_capture_observed.json'
    observed = read(observation_path)
    assert observed['root_observed_actual_exit_codes'] is True
    producers = observed['observed_producer_completions']
    assert isinstance(producers, list) and producers
    by_role = {row['role']: row for row in producers}
    assert len(by_role) == len(producers), 'Producer roles must be unique.'
    required = {
        'final_build': set(),
        'final_metrics': {'records/checkpoint35_metrics.json'},
        'final_render': {'records/pdf_qa/checkpoint35_final/render_manifest.json'},
        'final_pdf_audit': {'records/checkpoint35_final_pdf_audit.json'},
        'final_visual_record': {'records/checkpoint35_visual_review.json'},
        'final_size_estimate': {'records/checkpoint35_size_estimate.json',
            'records/checkpoint35_size_estimate_run.out',
            'records/checkpoint35_size_estimate_run.err'},
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
    assert not (root / 'records/checkpoint35_size_estimate_run.err').read_bytes()

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

    metrics = read('records/checkpoint35_metrics.json')
    estimate = read('records/checkpoint35_size_estimate.json')
    visual = read('records/checkpoint35_visual_review.json')
    render = read('records/pdf_qa/checkpoint35_final/render_manifest.json')
    audit = read('records/checkpoint35_final_pdf_audit.json')
    expected_pdf = metrics['pdf_sha256']
    assert re.fullmatch(r'[0-9a-f]{64}', expected_pdf)
    assert sha('LM4_SUCCESSOR_paper.pdf') == expected_pdf
    assert (root / 'LM4_SUCCESSOR_paper.pdf').stat().st_size == metrics['pdf_bytes']
    assert estimate['current_main_pdf_sha256'] == expected_pdf
    assert visual['pdf_sha256'] == render['pdf_sha256'] == audit['final_pdf_sha256'] == expected_pdf
    assert metrics['statements'] == 372 and metrics['pages'] == render['page_count'] > 0
    assert metrics['task_rows'] == 49 and metrics['bibliography_entries'] == 116
    assert metrics['statuses'] == {'Known': 6, 'Proved': 328, 'Refuted': 19, 'Open': 19}
    assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
    assert visual['visual_review'] == 'PASS' and audit['result'] == 'PASS_FINAL_LOGS'
    assert audit['final_overfull_count'] == 0
    assert render['dpi'] == 144
    assert set(render['required_new_mathematical_pages']) <= set(visual['individually_inspected_pages'])
    assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == cap
    assert estimate['baseline_archive'] == 'LM4_SUCCESSOR_checkpoint_34.zip'
    assert estimate['baseline_bytes'] == 529409669 and estimate['baseline_sha256'] == parent_sha
    assert not estimate['creates_zip'] and not estimate['writes_authored_input_files']
    assert estimate['header_manifest_retention_late_text_allowance_bytes'] == 5000000
    assert estimate['previous_direct_main_pdf_headers_removed'] == 0
    for kind in ('images', 'documents', 'data'):
        assert estimate['prospective_bundles'][kind]['dictionary_bytes'] == 67108864
        assert estimate['prospective_bundles'][kind]['zip_method'] == 'ZIP_LZMA'
    migrated = estimate['previous_direct_main_pdf_migrated']
    removed = estimate['previous_direct_main_pdf_compressed_payload_removed']
    assert removed == (0 if migrated is None else migrated['compressed_payload_bytes'])
    assert not (root.parent / 'LM4_SUCCESSOR_checkpoint_35.zip').exists()

    formal_review_path = 'records/checkpoint35_root_formal_reviews.json'
    formal = read(formal_review_path)
    assert formal['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
    assert [r['statement'] for r in formal['copies']] == ['A.'+str(n) for n in range(112,120)]+['B.167','B.168']
    assert read('records/checkpoint35_formal_source_copies.json')['copies'] == formal['copies']
    for row in formal['copies']:
        assert (root / row['source']).read_bytes() == (root / row['target']).read_bytes()
        assert sha(row['target']) == row['sha256']
    for rel, digest in formal['independent_reviews'].items():
        assert sha(rel) == digest, rel
    assert sha(formal['bibliography']['path']) == formal['bibliography']['sha256']

    helper_paths = {
        'code/package_checkpoint.py', 'code/checkpoint_data_tar.py',
        'code/preserve_checkpoint35_versions_inductive.py',
        'code/verify_checkpoint35_inductive_retention.py',
        'code/build_checkpoint35_parent_anchor.py',
        'code/estimate_checkpoint35_size.py', 'code/verify_checkpoint35_system_tars.py',
        'code/check_checkpoint35_preconditions.py', 'code/capture_checkpoint35.py',
        'code/render_checkpoint35_pdf.py', 'code/audit_checkpoint35_final_pdf.py',
        'code/finalize_checkpoint35_visual_record.py', 'code/publish_checkpoint35_readiness.py',
    }
    source_review_path = evidence(observed['operational_source_review'])
    source_review = read(source_review_path)
    assert source_review['result'] == 'PASS_COMPLETE_SOURCE_REVIEW'
    assert helper_paths <= evidence_list(source_review['sources'])
    independent_paths = evidence_list(source_review['independent_reviews'])
    publisher_review_path = evidence(observed['publisher_review'])
    publisher_review = read(publisher_review_path)
    assert publisher_review['result'].startswith('PASS')
    assert publisher_review['source']['path'] == 'code/publish_checkpoint35_readiness.py'
    evidence(publisher_review['source'])
    independent_paths.add(publisher_review_path)
    independent_paths.add(source_review_path)

    anchor_path = 'records/checkpoint35_retention_parent_anchor.json'
    anchor = read(anchor_path)
    assert anchor['parent_number'] == 34 and anchor['child_number'] == 35
    assert anchor['archive_bytes'] == 529409669 and anchor['archive_sha256'] == parent_sha
    assert anchor['logical_entries'] == 10387 and anchor['inherited_rows'] == 152653
    assert anchor['inherited_archives'] == 33
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
        formal_statements=372, formal_pages=metrics['pages'], bibliography_entries=116,
        no_new_zip_yet=True, next_scheduled_review='2026-11-17 14:49:30 UTC',
        source_observation_sha256=sha(observation_path),
        unpromoted_late_research='Actual residual and contact comparisons retain their exact scopes; both main decisions, the coherent class, and actual CM parity remain open.')
    outputs = ['records/checkpoint35_writer_pause.json',
               'records/checkpoint35_current_operational_bindings.json',
               'records/checkpoint35_capture_ready.json',
               'records/checkpoint35_capture_ready.pending']
    assert all(not (root / rel).exists() for rel in outputs), 'Preserve any earlier partial publication.'
    for rel, data in [(outputs[0], pause), (outputs[1], binding)]:
        with (root / rel).open('x') as stream:
            json.dump(data, stream, indent=2)
            stream.write('\n')
    with (root / outputs[3]).open('x') as stream:
        json.dump(ready, stream, indent=2)
        stream.write('\n')
    os.replace(root / outputs[3], root / outputs[2])
    print('Checkpoint35 readiness atomically published from six actual completed roles and three explicit writer pauses.', flush=True)


if __name__ == '__main__':
    main()
'''
publish('publish_checkpoint35_readiness.py',publisher)
manifest={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Source-only adaptation; no new helper imported or executed and no archive created. All checkpoint34 predecessors remain unchanged.','sources':[]}
for path,old,diff in changes:
    data=path.read_bytes(); olddata=old.read_bytes()
    manifest['sources'].append({'path':str(path.relative_to(root)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'predecessor':str(old.relative_to(root)),'predecessor_sha256':hashlib.sha256(olddata).hexdigest(),'predecessor_bytes':len(olddata)})
(root/'records/checkpoint35_capture_readiness_source_adaptation.diff').write_text(''.join(x[2] for x in changes))
(root/'records/checkpoint35_capture_readiness_source_adaptation.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
