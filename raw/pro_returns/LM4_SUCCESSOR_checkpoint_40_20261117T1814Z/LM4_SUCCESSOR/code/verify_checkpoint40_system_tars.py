"""Independent native checkpoint40 verifier with every PDF at its original TAR path.

No packaging or logical-reader imports. The archived digest manifest is
the authority for every original PNG, every PDF including the main PDF, and data path.
The data expectation is the complete manifest partition, not a legacy path policy.
"""
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import csv
import hashlib
import io
import json
import subprocess
import struct
import tarfile
import tempfile
import zipfile
import zlib

BASELINE_MANIFEST = 'records/checkpoint_39_contents_sha256.tsv'
BASELINE_MANIFEST_SHA = 'fe8628388479d0857740d3d236c544db06117ad6f7d7a9befcda4581af4d8c8e'
BASELINE_MANIFEST_BYTES = 1538629
BASELINE_LOGICAL_COUNT = 12758
OMISSIONS_CSV = 'records/checkpoint40_approved_derivative_omissions.csv'
OMISSIONS_CSV_SHA = '947c60823e46447a8eb3d3306d0ab07b9e63e1afd03cb160d71b76f772c4f615'
OMISSIONS_CSV_BYTES = 26723
OMISSION_FIELDS = ['path', 'bytes', 'sha256', 'reason', 'superseded_by', 'regeneration_recipe']
SUPERSEDED_LAYOUT = 'records/pdf_qa/checkpoint39_before_path_wrap/LM4_SUCCESSOR_paper.pdf'

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_40.zip'
assert archive.stat().st_size <= 536870912, 'Archive exceeds the delivery cap'
prefix = 'LM4_SUCCESSOR/'
main_pdf = prefix + 'LM4_SUCCESSOR_paper.pdf'
manifest_name = prefix + 'records/checkpoint_40_contents_sha256.tsv'
report = {'archive': archive.name, 'containers': {}}
with zipfile.ZipFile(archive) as z:
    rows = list(csv.DictReader(io.StringIO(z.read(manifest_name).decode()), delimiter='\t'))
    packaging = json.loads(z.read(prefix + 'records/checkpoint_40_packaging.json'))
    direct = [i.filename for i in z.infolist() if not i.is_dir()]
    assert len(direct) == len(set(direct))
    assert main_pdf not in direct, 'Current main PDF must be stored in the document TAR'
    assert z.getinfo(prefix+'verification_images.tar').compress_type==zipfile.ZIP_LZMA
    assert z.getinfo(prefix+'historical_documents.tar').compress_type==zipfile.ZIP_LZMA
    data_info = z.getinfo(prefix+'historical_data.tar')
    assert data_info.compress_type == zipfile.ZIP_LZMA
    with archive.open('rb') as raw:
        raw.seek(data_info.header_offset)
        header = raw.read(30)
        assert header[:4] == b'PK\x03\x04'
        name_size, extra_size = struct.unpack('<HH', header[26:30])
        raw.seek(name_size + extra_size, 1)
        properties = raw.read(9)
    assert len(properties) == 9 and properties[4] == 93
    assert properties[:2] == bytes([9, 4])
    assert struct.unpack('<H', properties[2:4])[0] == 5
    data_dictionary_bytes = struct.unpack('<I', properties[5:9])[0]
    assert data_dictionary_bytes == 268435456 == packaging['data_lzma_dictionary_bytes']
    image_info = z.getinfo(prefix+'verification_images.tar')
    with archive.open('rb') as raw:
        raw.seek(image_info.header_offset)
        header = raw.read(30)
        assert header[:4] == b'PK\x03\x04'
        name_size, extra_size = struct.unpack('<HH', header[26:30])
        raw.seek(name_size + extra_size, 1)
        image_properties = raw.read(9)
    assert len(image_properties) == 9 and image_properties[4] == 93
    assert image_properties[:4] == bytes([9,4,5,0])
    image_dictionary_bytes = struct.unpack('<I',image_properties[5:9])[0]
    assert image_dictionary_bytes == 671088640 == packaging['image_lzma_dictionary_bytes']
    document_info = z.getinfo(prefix+'historical_documents.tar')
    with archive.open('rb') as raw:
        raw.seek(document_info.header_offset)
        header = raw.read(30)
        assert len(header) == 30 and header[:4] == bytes((80,75,3,4))
        name_size, extra_size = struct.unpack('<HH',header[26:30])
        raw.seek(name_size + extra_size,1)
        document_properties = raw.read(9)
    assert len(document_properties) == 9 and document_properties[4] == 93
    assert document_properties[:4] == bytes([9,4,5,0])
    document_dictionary_bytes = struct.unpack('<I',document_properties[5:9])[0]
    assert document_dictionary_bytes == 268435456 == packaging['document_lzma_dictionary_bytes']
    specifications = [
        ('images', 'verification_images.tar', 'image',
         [r for r in rows if r['path'].lower().endswith('.png')]),
        ('documents', 'historical_documents.tar', 'document',
         [r for r in rows if r['path'].lower().endswith('.pdf')]),
    ]
    # Independently partition the actual immutable digest manifest. The
    # old pre37 policy is deliberately not imported or duplicated here.
    manifest_paths = {prefix + row['path'] for row in rows}
    assert len(manifest_paths) == len(rows), 'Duplicate logical manifest path'
    container_names = {prefix + name for name in (
        'verification_images.tar', 'historical_documents.tar', 'historical_data.tar')}
    assert container_names <= set(direct)
    direct_logical = set(direct) - container_names - {manifest_name}
    assert direct_logical <= manifest_paths
    supplements = packaging['revision_supplement_paths']
    assert isinstance(supplements, list) and all(isinstance(p, str) for p in supplements)
    assert len(supplements) == len(set(supplements)), 'Duplicate revision supplement'
    base_direct = {'RESTORE_CHECKPOINT.txt', 'records/checkpoint_40_packaging.json',
                   'records/checkpoint40_spool_preflight.json'}
    forbidden = base_direct | {'records/checkpoint_40_contents_sha256.tsv',
                              'verification_images.tar', 'historical_documents.tar',
                              'historical_data.tar'}
    for supplement in supplements:
        path = PurePosixPath(supplement)
        assert supplement and not path.is_absolute() and '..' not in path.parts
        assert str(path) == supplement and not any(c in supplement for c in '\x00\n\r\t\\')
        assert supplement not in forbidden and path.suffix.lower() not in {'.png', '.pdf', '.tar'}
        assert prefix + supplement in manifest_paths, 'Unmanifested revision supplement'
    assert direct_logical == {prefix + p for p in base_direct | set(supplements)}, \
        'Actual direct logical entries differ from the explicit revision declaration'
    baseline_raw = z.read(prefix + BASELINE_MANIFEST)
    assert len(baseline_raw) == BASELINE_MANIFEST_BYTES
    assert hashlib.sha256(baseline_raw).hexdigest() == BASELINE_MANIFEST_SHA
    baseline_reader = csv.DictReader(io.StringIO(baseline_raw.decode()), delimiter='\t')
    assert baseline_reader.fieldnames == ['sha256', 'bytes', 'path']
    baseline = {}
    for row in baseline_reader:
        rel = row['path']; path = PurePosixPath(rel)
        assert rel and not path.is_absolute() and '..' not in path.parts and str(path) == rel
        assert all(ord(c) >= 32 for c in rel) and '\\' not in rel
        assert rel not in baseline and rel != BASELINE_MANIFEST
        baseline[rel] = {'bytes': int(row['bytes']), 'sha256': row['sha256']}
    baseline[BASELINE_MANIFEST] = {'bytes': len(baseline_raw), 'sha256': BASELINE_MANIFEST_SHA}
    assert len(baseline) == BASELINE_LOGICAL_COUNT
    current_meta = {r['path']: {'bytes': int(r['bytes']), 'sha256': r['sha256']} for r in rows}
    current_manifest_raw = z.read(manifest_name)
    current_meta['records/checkpoint_40_contents_sha256.tsv'] = {
        'bytes': len(current_manifest_raw), 'sha256': hashlib.sha256(current_manifest_raw).hexdigest()}
    omission_raw = z.read(prefix + OMISSIONS_CSV)
    assert len(omission_raw) == OMISSIONS_CSV_BYTES
    assert hashlib.sha256(omission_raw).hexdigest() == OMISSIONS_CSV_SHA
    omission_reader = csv.DictReader(io.StringIO(omission_raw.decode()))
    assert omission_reader.fieldnames == OMISSION_FIELDS
    omission_rows = list(omission_reader)
    omitted = {r['path'] for r in omission_rows}
    expected_qa = {p for p in baseline if p.startswith('records/pdf_qa/checkpoint39_final/')
                   and p.lower().endswith('.png')}
    assert len(expected_qa) == 58 and len(omission_rows) == len(omitted) == 59
    assert omitted == expected_qa | {SUPERSEDED_LAYOUT}
    for row in omission_rows:
        rel = row['path']
        assert baseline[rel] == {'bytes': int(row['bytes']), 'sha256': row['sha256']}
        assert rel not in current_meta
        assert row['reason'].strip() and row['regeneration_recipe'].strip()
        assert row['superseded_by'] == 'LM4_SUCCESSOR_paper.pdf' and row['superseded_by'] in current_meta
    assert packaging['omissions'] == 59 and packaging['historical_omissions'] == 0
    assert packaging['approved_omissions'] == omission_rows
    for field, rel, raw in [('original_frozen39_manifest', BASELINE_MANIFEST, baseline_raw),
                            ('approved_omissions_csv', OMISSIONS_CSV, omission_raw)]:
        assert packaging[field] == {'path': rel, 'bytes': len(raw),
                                    'sha256': hashlib.sha256(raw).hexdigest(),
                                    'crc32': zlib.crc32(raw) & 0xffffffff}
    generated40 = {'records/checkpoint_40_contents_sha256.tsv',
                   'records/checkpoint_40_packaging.json', 'records/checkpoint40_spool_preflight.json'}
    assert set(current_meta) == (set(baseline) - omitted) | set(supplements) | generated40
    for rel in set(baseline) - omitted:
        assert current_meta[rel] == baseline[rel], ('Surviving frozen39 identity changed', rel)
    report['approved_omission_scope'] = {
        'original_frozen39_logical_count': BASELINE_LOGICAL_COUNT,
        'approved_current_derivative_omissions': 59, 'newQA_PNG_omissions': 58,
        'superseded_failed_layout_PDF_omissions': 1,
        'exact_frozen39_minus_approved_plus_declared_additions': 'PASS',
        'every_surviving_frozen39_identity': 'PASS',
        'approved_omission_csv_sha256': OMISSIONS_CSV_SHA}
    image_paths = {prefix + row['path'] for row in specifications[0][3]}
    document_paths = {prefix + row['path'] for row in specifications[1][3]}
    assert main_pdf in document_paths, 'Original main-PDF path missing from document partition'
    assert not direct_logical.intersection(image_paths | document_paths)
    assert not image_paths.intersection(document_paths)
    data_paths = manifest_paths - direct_logical - image_paths - document_paths
    data_rows = [row for row in rows if prefix + row['path'] in data_paths]
    assert all(PurePosixPath(row['path']).suffix.lower() not in
               {'.png', '.pdf', '.tar'} for row in data_rows)
    assert len(manifest_paths) == (len(direct_logical) + len(image_paths)
                                   + len(document_paths) + len(data_paths))
    assert manifest_paths == direct_logical | image_paths | document_paths | data_paths
    specifications.append(('data', 'historical_data.tar', 'data', data_rows))
    report['manifest_partition'] = {
        'logical_manifest_rows': len(rows), 'direct_logical_rows': len(direct_logical),
        'revision_supplement_paths': supplements, 'exact_declared_direct_partition': 'PASS',
        'image_rows': len(image_paths), 'document_rows': len(document_paths),
        'data_rows': len(data_paths), 'pairwise_disjoint_and_complete': 'PASS',
        'data_selection': 'Exact complement of actual direct, image and document rows in the immutable manifest.',
        'document_selection': 'ALL PDF manifest rows, including the current main PDF at its original logical path.',
    }
    for kind, basename, field, selected in specifications:
        expected = {prefix + r['path']: r for r in selected}
        assert len(expected) == len(selected)
        assert not set(expected).intersection(direct)
        bundle = z.read(prefix + basename)
        assert hashlib.sha256(bundle).hexdigest() == packaging[field + '_bundle_sha256']
        assert len(bundle) == packaging[field + '_bundle_bytes']
        assert len(expected) == packaging[field + '_paths']
        with tempfile.TemporaryDirectory(prefix='lm4-checkpoint40-native-' + kind + '-') as directory:
            temp = Path(directory)
            tar_path = temp / basename
            tar_path.write_bytes(bundle)
            seen = {}
            with tarfile.open(tar_path, 'r:') as tf:
                for member in tf.getmembers():
                    path = PurePosixPath(member.name)
                    assert not path.is_absolute() and '..' not in path.parts
                    assert path.parts[0] == 'LM4_SUCCESSOR'
                    assert member.name in expected and member.name not in seen
                    assert member.isfile() or member.islnk()
                    if member.islnk():
                        assert seen.get(member.linkname) == 'regular'
                    seen[member.name] = 'regular' if member.isfile() else 'hardlink'
            assert set(seen) == set(expected)
            subprocess.run(['tar', '-xf', str(tar_path)], cwd=temp, check=True)
            total_bytes = 0
            for name, row in expected.items():
                path = temp / name
                assert path.is_file() and not path.is_symlink()
                data = path.read_bytes()
                assert len(data) == int(row['bytes']), name
                assert hashlib.sha256(data).hexdigest() == row['sha256'], name
                total_bytes += len(data)
        report['containers'][kind] = {
            'bundle': basename,
            'bundle_sha256': hashlib.sha256(bundle).hexdigest(),
            'paths': len(expected),
            'regular_payloads': list(seen.values()).count('regular'),
            'hardlink_paths': list(seen.values()).count('hardlink'),
            'logical_bytes': total_bytes,
            'system_tar_restore': 'PASS',
            'every_manifest_path_size_and_hash': 'PASS',
        }

report.update(
    archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
    current_main_pdf_original_path_in_document_tar='PASS',
    current_main_pdf_absent_from_direct_zip='PASS',
    archive_bytes=archive.stat().st_size,
    archive_within_536870912_byte_cap='PASS',
    all_three_system_tar_restores='PASS',
    all_three_container_zip_lzma_methods='PASS',
    data_lzma_dictionary_bytes=data_dictionary_bytes,
    image_lzma_dictionary_bytes=image_dictionary_bytes,
    document_lzma_dictionary_bytes=document_dictionary_bytes,
    completed_at=datetime.now(timezone.utc).isoformat(),
    independence='No import of packager, selection predicate, standard-TAR builder or logical reader; exact immutable-manifest partition and native system tar extraction of actual archived bytes.',
)
print(json.dumps(report, indent=2))
