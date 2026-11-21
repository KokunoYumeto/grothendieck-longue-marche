"""Record root's actual checkpoint 34 transport checks and the two completed events."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import zipfile

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
CHECKS = OUT / 'checks'
LABEL = 'checkpoint_34'
RAW_SHA = 'bd31c3339886c88775ad7552ced09c8c1147c260c453753caf1aec2beb99d322'
RAW_SIZE = 945698410
LIMIT = 536870912

def hash_file(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()

def new_file(path, data):
    with path.open('xb') as stream:
        stream.write(data)

def event_table(rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'],
                            delimiter='\t', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()

proof_path = CHECKS / (LABEL + '_root_actual_verification.json')
event_path = CHECKS / (LABEL + '_root_event_copy.json')
assert not proof_path.exists() and not event_path.exists()
selection_path = CHECKS / (LABEL + '_helper_transport_selection.json')
selection = json.loads(selection_path.read_bytes())
assert selection['selected_variant'] == 'v2'
assert selection['observed_exit_codes'] == {'v1': 0, 'v2': 0}
assert selection['launch_attempt_counts'] == {'v1': 1, 'v2': 1}

when = datetime.now(timezone.utc).isoformat()
archives = []
copied_events = []
for variant in ('raw', 'v1', 'v2'):
    reference = selection[variant + '_archive']
    path = Path(reference['path'])
    actual = {'variant': variant, 'path': str(path),
              'bytes': path.stat().st_size, 'sha256': hash_file(path)}
    assert actual['bytes'] == reference['bytes']
    assert actual['sha256'] == reference['sha256']
    if variant == 'raw':
        assert actual['bytes'] == RAW_SIZE and actual['sha256'] == RAW_SHA
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            original_count = len(infos)
            original_bytes = sum(info.file_size for info in infos)
        assert original_count == 4473 and original_bytes == 1575577438
    else:
        audit_path = Path(selection['audit_files'][variant]['path'])
        audit_bytes = audit_path.read_bytes()
        audit = json.loads(audit_bytes)
        event_file = Path(selection['exact_event_copies'][variant]['path'])
        event_bytes = event_file.read_bytes()
        with zipfile.ZipFile(path) as archive:
            assert archive.read('_checkpoint_transport/byte_audit.json') == audit_bytes
            assert archive.read('_checkpoint_transport/CHECK_EVENTS.tsv') == event_bytes
        assert audit['source_archive']['sha256'] == RAW_SHA
        assert audit['source_archive']['bytes'] == RAW_SIZE
        assert audit['mismatched_original_files'] == 0
        assert audit['original_archive_hash_after_packaging_matches_before'] is True
        assert audit['final_transport_original_entry_byte_comparisons_passed'] == original_count
        assert audit['final_transport_original_file_bytes_compared'] == original_bytes
        assert audit['adopted_original_png_file_byte_comparisons_passed'] == 1214
        assert audit['adopted_pixel_byte_comparisons_passed'] == 1214
        rows = list(csv.DictReader(io.StringIO(event_bytes.decode()), delimiter='\t'))
        assert len(rows) == 1
        row = rows[0]
        copied = dict(row)
        copied['who'] += '; execution delegated by /root to /root/codec026_b (single observed process exit 0)'
        copied_events.append({'variant': variant, 'raw_event': row, 'copied_event': copied})
        actual.update({'embedded_external_audit_exact': True,
                       'embedded_external_event_exact': True,
                       'audit_sha256': hashlib.sha256(audit_bytes).hexdigest(),
                       'observed_helper_exit_code': 0})
    archives.append(actual)

assert archives[1]['bytes'] > LIMIT
assert archives[2]['bytes'] < LIMIT
assert selection['selected_archive']['sha256'] == archives[2]['sha256']
global_path = CHECKS / 'global_check_events.json'
before = global_path.read_bytes()
events = json.loads(before)
page_events = []
for record_path in sorted((OUT / 'records').glob('scan*.json')):
    page_events.extend(json.loads(record_path.read_bytes()).get('check_events', []))
table_path = OUT / 'CHECK_EVENTS.tsv'
table_before = table_path.read_bytes()
assert event_table(page_events + events) == table_before
for item in copied_events:
    event = item['copied_event']
    assert not any(old['statement_id'] == event['statement_id'] for old in events)
    events.append(event)
after = json_bytes(events)
table_after = event_table(page_events + events)
assert table_after.startswith(table_before)
frozen = json.loads((OUT / 'freeze_manifest.json').read_bytes())
assert len(frozen['sha256']) == 25
for relative, expected in frozen['sha256'].items():
    assert hash_file(OUT / relative) == expected, relative
event_proof = {'at_utc': when, 'before_sha256': hashlib.sha256(before).hexdigest(),
               'after_sha256': hashlib.sha256(after).hexdigest(), 'events': copied_events,
               'copied_once': True,
               'who_suffix_reason': 'Embedded packer metadata names root as task owner; the exact delegated operator is appended from observed launch/process records. Raw rows remain verbatim.'}
proof = {'at_utc': when, 'archives': archives, 'selected_variant': 'v2',
         'scope': 'Root measured actual archive hashes/sizes and embedded provenance equality. All-entry and pixel comparisons were performed by the helper-owned original runs; no encoding or pixel comparison was repeated here.',
         'public_event_table_map': {
             'before_sha256': hashlib.sha256(table_before).hexdigest(),
             'after_sha256': hashlib.sha256(table_after).hexdigest(),
             'preserved_prefix_bytes': len(table_before),
             'exact_builder_projection': 'Ordered page check_events followed by ordered global events, using the same five fields, csv.DictWriter delimiter and extrasaction as build_records.py.',
             'old_projection_compared_to_actual_bytes': True,
             'appended_rows': 2,
             'inverse': 'Retain the first preserved_prefix_bytes bytes to recover the complete prior public table.',
             'frozen_transcription_files_written': 0}}
new_file(event_path, json_bytes(event_proof))
global_path.write_bytes(after)
table_path.write_bytes(table_after)
for relative, expected in frozen['sha256'].items():
    assert hash_file(OUT / relative) == expected, relative
proof['frozen_transcription_hashes_rechecked_unchanged'] = 25
new_file(proof_path, json_bytes(proof))

history_path = OUT / 'checkpoint_history.json'
history = json.loads(history_path.read_bytes())
entry = history[-1]
assert entry['name'] == 'SP40_CW_81_checkpoint_34.zip'
assert entry['created_utc'] == '2026-11-21T10:33:06.828334+00:00'
assert 'raw_size' not in entry
entry.update({
    'raw_size': RAW_SIZE, 'raw_sha256': RAW_SHA,
    'writers_paused_during_raw_snapshot': True,
    'raw_process_session': 62624, 'raw_observed_exit_code': 0,
    'transport_status': 'complete; all 4473 original entries directly byte-compared, 0 mismatches; 1214 original PNG bytes and pixels recovered exactly',
    'transport_format': 'mixed lossless JXL/WebP v2 with exact original-file reconstruction',
    'transport_path': archives[2]['path'], 'transport_size': archives[2]['bytes'],
    'transport_sha256': archives[2]['sha256'],
    'transport_audit': 'out/checks/checkpoint_34_transport_v2_audit.json',
    'root_actual_verification': 'out/checks/checkpoint_34_root_actual_verification.json',
    'actual_events_copy': 'out/checks/checkpoint_34_root_event_copy.json',
    'v1_preserved_path': 'persistent/SP40_CW_81_checkpoint_34.zip',
    'v1_preserved_size': archives[1]['bytes'], 'v1_preserved_sha256': archives[1]['sha256'],
    'v1_size_gate': 'out/checks/checkpoint_34_helper_transport_selection.json'
})
history_path.write_bytes(json_bytes(history))
print(json.dumps({'verified': True, 'global_events': len(events),
                  'original_entries': original_count, 'selected': archives[2],
                  'frozen_hashes_unchanged': 25}))
