"""Independently restore all three actual checkpoint32 containers with system tar.

No packaging or logical-reader imports. The archived digest manifest is
the authority for every original PNG, historical/preview PDF, and selected data path.
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

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_32.zip'
prefix = 'LM4_SUCCESSOR/'
manifest_name = prefix + 'records/checkpoint_32_contents_sha256.tsv'
report = {'archive': archive.name, 'containers': {}}
with zipfile.ZipFile(archive) as z:
    rows = list(csv.DictReader(io.StringIO(z.read(manifest_name).decode()), delimiter='\t'))
    packaging = json.loads(z.read(prefix + 'records/checkpoint_32_packaging.json'))
    direct = [i.filename for i in z.infolist() if not i.is_dir()]
    assert len(direct) == len(set(direct))
    assert prefix + 'LM4_SUCCESSOR_paper.pdf' in direct
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
    assert properties[:2] == bytes([9, 4])
    assert struct.unpack('<H', properties[2:4])[0] == 5
    data_dictionary_bytes = struct.unpack('<I', properties[5:9])[0]
    assert data_dictionary_bytes == 67108864 == packaging['data_lzma_dictionary_bytes']
    image_info = z.getinfo(prefix+'verification_images.tar')
    with archive.open('rb') as raw:
        raw.seek(image_info.header_offset)
        header = raw.read(30)
        assert header[:4] == b'PK\x03\x04'
        name_size, extra_size = struct.unpack('<HH', header[26:30])
        raw.seek(name_size + extra_size, 1)
        image_properties = raw.read(9)
    assert image_properties[:4] == bytes([9,4,5,0])
    image_dictionary_bytes = struct.unpack('<I',image_properties[5:9])[0]
    assert image_dictionary_bytes == 67108864 == packaging['image_lzma_dictionary_bytes']
    document_info = z.getinfo(prefix+'historical_documents.tar')
    with archive.open('rb') as raw:
        raw.seek(document_info.header_offset)
        header = raw.read(30)
        name_size, extra_size = struct.unpack('<HH',header[26:30])
        raw.seek(name_size + extra_size,1)
        document_properties = raw.read(9)
    assert document_properties[:4] == bytes([9,4,5,0])
    document_dictionary_bytes = struct.unpack('<I',document_properties[5:9])[0]
    assert document_dictionary_bytes == 8388608 == packaging['document_lzma_dictionary_bytes']
    specifications = [
        ('images', 'verification_images.tar', 'image',
         [r for r in rows if r['path'].lower().endswith('.png')]),
        ('documents', 'historical_documents.tar', 'document',
         [r for r in rows if r['path'].lower().endswith('.pdf') and r['path'] != 'LM4_SUCCESSOR_paper.pdf']),
    ]
    specifications.append(
        ('data', 'historical_data.tar', 'data',
         [r for r in rows
          if PurePosixPath(r['path']).suffix.lower() not in {'.png', '.pdf', '.tar'}
          and (r['path'].startswith('checkpoint_history/')
               or (PurePosixPath(r['path']).suffix.lower() == '.json'
                   and int(r['bytes']) >= 1000000))]))
    for kind, basename, field, selected in specifications:
        expected = {prefix + r['path']: r for r in selected}
        assert len(expected) == len(selected)
        assert not set(expected).intersection(direct)
        bundle = z.read(prefix + basename)
        assert hashlib.sha256(bundle).hexdigest() == packaging[field + '_bundle_sha256']
        assert len(bundle) == packaging[field + '_bundle_bytes']
        assert len(expected) == packaging[field + '_paths']
        with tempfile.TemporaryDirectory(prefix='lm4-checkpoint32-native-' + kind + '-') as directory:
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
            'every_original_path_size_and_hash': 'PASS',
        }

report.update(
    archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
    current_main_pdf_direct='PASS',
    all_three_system_tar_restores='PASS',
    all_three_container_zip_lzma_methods='PASS',
    data_lzma_dictionary_bytes=data_dictionary_bytes,
    image_lzma_dictionary_bytes=image_dictionary_bytes,
    document_lzma_dictionary_bytes=document_dictionary_bytes,
    completed_at=datetime.now(timezone.utc).isoformat(),
    independence='No import of packager, standard-TAR builder or logical reader; native system tar extraction of the actual archived bytes.',
)
print(json.dumps(report, indent=2))
