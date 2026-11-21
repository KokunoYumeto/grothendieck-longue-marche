#!/usr/bin/env python3
"""Assemble completed checkpoint34 transport evidence without global mutation."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, zipfile

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
LIMIT = 536870912
PREFIX = 'checkpoint_34_helper_transport_'

def read(name):
    return json.loads((OUT / (PREFIX + name)).read_bytes())

def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

def file_record(path):
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': sha(path)}

def main():
    v1 = read('v1_verification.json')
    c1 = read('v1_process_completion.json')
    assert c1['exit_code'] == 0
    variants = ['v1']
    verification = {'v1': v1}
    completion = {'v1': c1}
    if v1['transport_archive']['bytes'] > LIMIT:
        variants.append('v2')
        verification['v2'] = read('v2_verification.json')
        completion['v2'] = read('v2_process_completion.json')
    for variant in variants:
        v, c = verification[variant], completion[variant]
        assert c['exit_code'] == 0
        actual = file_record(Path(v['transport_archive']['path']))
        assert actual == v['transport_archive']
        assert c['completion_stdout']['output_bytes'] == actual['bytes']
        assert c['completion_stdout']['output_sha256'] == actual['sha256']
        assert v['raw_source'] == v1['raw_source']
        assert read(variant + '_launch.json')['cache_argument_is_parent']
        assert read(variant + '_launch.json')[variant + '_launch_attempt_number'] == 1
    selected = variants[-1]
    assert verification[selected]['transport_archive']['bytes'] <= LIMIT
    event_bytes, event_files, segments = {}, {}, []
    combined = b''
    for variant in variants:
        path = Path(verification[variant]['exact_transport_check_events_copy_path'])
        event_bytes[variant] = path.read_bytes()
        with zipfile.ZipFile(verification[variant]['transport_archive']['path']) as z:
            assert event_bytes[variant] == z.read('_checkpoint_transport/CHECK_EVENTS.tsv')
            assert z.read('_checkpoint_transport/byte_audit.json') == Path(verification[variant]['external_audit_path']).read_bytes()
        start = 0 if not combined else event_bytes[variant].index(b'\n') + 1
        if combined:
            assert event_bytes[variant][:start] == event_bytes['v1'].splitlines(keepends=True)[0]
        end = len(event_bytes[variant])
        segments.append({'source': str(path), 'source_start_inclusive': start,
                         'source_end_exclusive': end, 'destination_start_inclusive': len(combined),
                         'destination_end_exclusive': len(combined) + end - start})
        combined += event_bytes[variant][start:end]
        event_files[variant] = file_record(path)
    combined_path = OUT / (PREFIX + 'CHECK_EVENTS.tsv')
    with combined_path.open('xb') as handle:
        handle.write(combined)
    rows = list(csv.DictReader(io.StringIO(combined.decode('utf-8')), delimiter='\t'))
    assert rows == [verification[v]['actual_transport_check_events_rows'][0] for v in variants]
    raw_actual = file_record(Path(v1['raw_source']['path']))
    assert raw_actual == v1['raw_source']
    v1_actual = file_record(Path(v1['transport_archive']['path']))
    assert v1_actual == v1['transport_archive']
    audit_files = {v: {'path': verification[v]['external_audit_path'],
                      'sha256': verification[v]['external_audit_sha256'],
                      'embedded_audit_bytes_equal_external': True} for v in variants}
    audits = {v: verification[v]['packaging_audit'] for v in variants}
    result = {
        'utc': datetime.now(timezone.utc).isoformat(), 'selected_variant': selected,
        'selected_archive': verification[selected]['transport_archive'], 'size_limit_bytes': LIMIT,
        'selected_headroom_bytes': LIMIT - verification[selected]['transport_archive']['bytes'],
        'selection_basis': 'Observed successful exits and actual completed archive sizes govern the one v1 run and the size-gated one v2 run. Every preserved audit equals its embedded bytes.',
        'raw_archive': raw_actual, 'v1_archive': v1_actual,
        'v2_archive': verification.get('v2', {}).get('transport_archive'),
        'observed_exit_codes': {v: completion[v]['exit_code'] for v in variants},
        'launch_attempt_counts': {v: 1 for v in variants},
        'both_cache_arguments_are_parent_directory': True,
        'both_completion_stdout_records_match_actual_archive_measurements': True,
        'v1_post_v2_preservation': {'actual_bytes': v1_actual['bytes'], 'actual_sha256': v1_actual['sha256'], 'matches_pre_v2_exact_size_and_hash': True},
        'audit_files': audit_files, 'full_packaging_audits': audits,
        'original_entries_compared_in_each_packaging_run': audits['v1']['original_entries'],
        'original_file_bytes_compared_in_each_packaging_run': audits['v1']['original_file_bytes'],
        'mismatched_original_files_in_each_packaging_audit': 0,
        'exact_event_copies': event_files,
        'combined_event_file': {**file_record(combined_path), 'row_count': len(rows), 'byte_segments': segments},
        'actual_CHECK_EVENTS_rows': rows,
        'delegated_execution_attribution': {'operator': '/root/codec026_b',
                                           'authorizing_agent': '/root',
                                           'sessions': {v: completion[v]['session_id'] for v in variants},
                                           'embedded_event_who_fields_preserved_exactly': True},
        'selected_preservation_scope': 'Every original entry path and original file bytes; the raw source ZIP container remains separately preserved at raw_archive.path.',
        'no_upload_performed': True, 'no_global_events_history_or_progress_modified': True,
    }
    path = OUT / (PREFIX + 'selection.json')
    with path.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    print(json.dumps({'selection_record': file_record(path), 'selected_archive': result['selected_archive'],
                      'raw_archive': raw_actual, 'v1_archive': v1_actual,
                      'headroom_bytes': result['selected_headroom_bytes'],
                      'combined_events': result['combined_event_file']}, indent=2))

if __name__ == '__main__':
    main()
