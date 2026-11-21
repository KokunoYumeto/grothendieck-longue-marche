#!/usr/bin/env python3
"""Read completed checkpoint31 archive bytes and audits; write helper evidence only."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, zipfile

ROOT = Path('/workspace/scratch/94548b74fbe0')
RAW = ROOT / 'SP40_CW_81_checkpoint_31.zip'
EXPECTED_SOURCE_BYTES = 928569758
EXPECTED_SOURCE_SHA256 = 'cf185bacdf5e9e14982058a532585cdc80bbd3b1b6a68797f4669887dd20cb7d'
LIMIT = 536870912
PREFIX = '_checkpoint_transport/'

def file_sha256(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

def fingerprint(path):
    s = path.stat()
    return (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=['v1', 'v2'], required=True)
    args = parser.parse_args()
    variant = args.variant
    archive_path = ROOT / ('persistent' if variant == 'v1' else 'persistent_v2') / RAW.name
    audit_path = ROOT / 'out/checks' / ('checkpoint_31_transport_audit.json' if variant == 'v1' else 'checkpoint_31_transport_v2_audit.json')
    evidence_path = ROOT / 'out/checks' / ('checkpoint_31_helper_transport_' + variant + '_verification.json')
    assert not evidence_path.exists(), 'Helper evidence already exists; do not overwrite'
    assert archive_path.exists() and audit_path.exists()
    assert not archive_path.with_name(archive_path.name + '.part').exists()
    raw_before = fingerprint(RAW)
    archive_before = fingerprint(archive_path)
    source_size = RAW.stat().st_size
    source_hash = file_sha256(RAW)
    output_size = archive_path.stat().st_size
    output_hash = file_sha256(archive_path)
    assert source_size == EXPECTED_SOURCE_BYTES
    assert source_hash == EXPECTED_SOURCE_SHA256
    actual_source = {'basename': RAW.name, 'bytes': source_size, 'sha256': source_hash}
    external_audit_bytes = audit_path.read_bytes()
    external_audit = json.loads(external_audit_bytes)
    with zipfile.ZipFile(RAW) as raw, zipfile.ZipFile(archive_path) as transported:
        source_entries = raw.infolist()
        output_entries = transported.infolist()
        source_names = [info.filename for info in source_entries]
        output_names = [info.filename for info in output_entries]
        assert len(source_entries) == 3528
        assert len(set(source_names)) == len(source_names)
        assert len(set(output_names)) == len(output_names)
        embedded_audit_bytes = transported.read(PREFIX + 'byte_audit.json')
        assert embedded_audit_bytes == external_audit_bytes
        manifest_bytes = transported.read(PREFIX + 'manifest.json')
        manifest = json.loads(manifest_bytes)
        assert manifest['format'] == 'checkpoint-lossless-png-transport'
        assert manifest['format_version'] == int(variant[1:])
        assert manifest['source_archive'] == actual_source
        assert external_audit['source_archive'] == actual_source
        entries = manifest['entries']
        assert [entry['path'] for entry in entries] == source_names
        assert len(entries) == manifest['original_entry_count'] == external_audit['original_entries']
        total_source_bytes = sum(info.file_size for info in source_entries)
        assert sum(entry['original_bytes'] for entry in entries) == total_source_bytes
        assert external_audit['original_file_bytes'] == total_source_bytes
        for info, entry in zip(source_entries, entries):
            assert entry['original_bytes'] == info.file_size
            assert entry['is_directory'] == info.is_dir()
            assert entry['original_zip_compressed_bytes'] == info.compress_size
            assert entry['zip_metadata'] == {
                'date_time': list(info.date_time), 'compression_method': info.compress_type,
                'external_attr': info.external_attr, 'create_system': info.create_system,
                'internal_attr': info.internal_attr, 'flag_bits': info.flag_bits,
            }
            stored = transported.getinfo(entry['storage']['path'])
            assert entry['storage']['bytes'] == stored.file_size
        adopted = [entry for entry in entries if entry['storage']['kind'] != 'original']
        pngs = [info for info in source_entries if not info.is_dir() and info.filename.lower().endswith('.png')]
        assert len(pngs) == manifest['original_png_count'] == external_audit['original_png_entries']
        assert len(adopted) == manifest['encoded_png_count'] == external_audit['encoded_png_entries']
        assert external_audit['adopted_pixel_byte_comparisons_passed'] == len(adopted)
        assert external_audit['adopted_original_png_file_byte_comparisons_passed'] == len(adopted)
        assert manifest['all_adopted_png_file_byte_comparisons_passed'] is True
        for entry in adopted:
            check = entry['png_transport_check']
            assert check['adopted'] is True
            assert check['direct_png_byte_comparison'] is True
            assert check['decoded_pixel_byte_comparison'] is True
            assert check['reconstructed_png_byte_comparison'] is True
        assert external_audit['final_transport_original_entry_byte_comparisons_passed'] == len(source_entries)
        assert external_audit['final_transport_non_png_original_byte_comparisons_passed'] == len(source_entries) - len(pngs)
        assert external_audit['final_transport_original_file_bytes_compared'] == total_source_bytes
        assert external_audit['mismatched_original_files'] == 0
        assert external_audit['original_archive_hash_after_packaging_matches_before'] is True
        assert external_audit['source_files_modified'] is False
        assert external_audit['all_original_paths_and_hashes'] == PREFIX + 'manifest.json'
        assert external_audit['check_event_record'] == PREFIX + 'CHECK_EVENTS.tsv'
        event_bytes = transported.read(PREFIX + 'CHECK_EVENTS.tsv')
        assert len(event_bytes) > 0
        embedded_script_hashes = {}
        pack_name = 'checkpoint_transport_pack.py' if variant == 'v1' else 'checkpoint_transport_pack_v2.py'
        restore_name = 'checkpoint_transport_restore.py' if variant == 'v1' else 'checkpoint_transport_restore_v2.py'
        for name in (pack_name, restore_name):
            embedded = transported.read(PREFIX + name)
            assert embedded == (ROOT / 'out/scripts' / name).read_bytes()
            embedded_script_hashes[name] = hashlib.sha256(embedded).hexdigest()
        assert transported.read('RESTORE_CHECKPOINT.py') == transported.read(PREFIX + restore_name)
    assert fingerprint(RAW) == raw_before
    assert fingerprint(archive_path) == archive_before
    assert audit_path.read_bytes() == external_audit_bytes
    evidence = {
        'utc': datetime.now(timezone.utc).isoformat(),
        'variant': variant,
        'scope': 'Actual archive hashes and sizes, embedded/external audit byte agreement, and source/manifest metadata agreement; no image viewing or new restoration decoding',
        'raw_source': {'path': str(RAW), 'bytes': source_size, 'sha256': source_hash},
        'transport_archive': {'path': str(archive_path), 'bytes': output_size, 'sha256': output_hash},
        'v2_launch_gate_bytes': LIMIT,
        'actual_output_strictly_exceeds_gate': output_size > LIMIT,
        'actual_output_strictly_below_gate': output_size < LIMIT,
        'headroom_bytes': LIMIT - output_size,
        'external_audit_path': str(audit_path),
        'external_audit_sha256': hashlib.sha256(external_audit_bytes).hexdigest(),
        'embedded_audit_sha256': hashlib.sha256(embedded_audit_bytes).hexdigest(),
        'embedded_audit_bytes_equal_external': True,
        'manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest(),
        'manifest_source_identification_matches_actual': True,
        'audit_source_identification_matches_actual': True,
        'source_and_manifest_entry_order_membership_and_zip_metadata_equal': True,
        'manifest_storage_sizes_match_actual_zip_entry_sizes': True,
        'actual_source_entry_count': len(source_entries),
        'actual_transport_entry_count': len(output_entries),
        'original_file_bytes_from_source_zip_metadata': total_source_bytes,
        'adopted_entries_with_all_recorded_exact_byte_checks_true': len(adopted),
        'embedded_scripts_equal_local_scripts': embedded_script_hashes,
        'source_and_transport_unchanged_during_helper_check': True,
        'packaging_audit': external_audit,
        'no_upload_performed': True,
        'no_global_events_history_or_build_records_modified': True,
    }
    with evidence_path.open('x', encoding='utf-8') as handle:
        json.dump(evidence, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    print(json.dumps(evidence, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
