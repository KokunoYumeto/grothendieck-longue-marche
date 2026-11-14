"""Independent physical/logical readback of the 226-statement research ZIP."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import csv
import hashlib
import io
import json
import zipfile

BASE = Path(__file__).resolve().parent
TREE = BASE / 'LM7_FERMAT_TOWER'
ARCHIVE = BASE / 'LM7_FERMAT_TOWER.zip'
PREFIX = TREE.name + '/'
PDF_SHA = '66def8ecc7e237f7969b07911264e933c496191cff6aa7b39c19463808e7774a'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    digest = sha(ARCHIVE.read_bytes())
    assert ARCHIVE.stat().st_size <= 536870912
    assert ARCHIVE.with_suffix('.zip.sha256').read_text().split()[0] == digest
    with zipfile.ZipFile(ARCHIVE) as z:
        assert z.testzip() is None
        physical = z.namelist()
        assert len(physical) == len(set(physical))
        manifest_bytes = z.read(PREFIX + 'LM7_FERMAT_TOWER_manifest.json')
        assert manifest_bytes == (TREE / 'LM7_FERMAT_TOWER_manifest.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        assert manifest['numbered_statements'] == 226
        assert manifest['coverage_rows'] == 33
        assert manifest['pdf_pages'] == 728
        assert manifest['pdf_sha256'] == PDF_SHA
        records = {r['path']: r for r in manifest['files']}
        assert len(records) == len(manifest['files']) == manifest['logical_file_count']
        assert len(physical) == manifest['ordinary_member_count_including_manifest']
        expected_physical = {PREFIX + r['storage_path'] for r in records.values()}
        expected_physical.add(PREFIX + 'LM7_FERMAT_TOWER_manifest.json')
        assert set(physical) == expected_physical

        logical_bytes = 0
        aliases = []
        for name, item in records.items():
            p, q = PurePosixPath(name), PurePosixPath(item['storage_path'])
            assert not p.is_absolute() and '..' not in p.parts
            assert not q.is_absolute() and '..' not in q.parts
            data = z.read(PREFIX + item['storage_path'])
            assert len(data) == item['bytes'] and sha(data) == item['sha256'], name
            assert data == (TREE / name).read_bytes(), name
            logical_bytes += len(data)
            if p != q:
                assert p.suffix.lower() in {'.png', '.jpg', '.jpeg'} and 'qa' in p.parts
                assert q.suffix.lower() in {'.png', '.jpg', '.jpeg'} and 'qa' in q.parts
                assert not name.startswith(('qa/contact_', 'qa/detail226_'))
                assert records[str(q)]['storage_path'] == str(q)
                assert PREFIX + name not in physical
                aliases.append(item)
            else:
                assert PREFIX + name in physical

        def read(name):
            return z.read(PREFIX + records[name]['storage_path'])

        plan = json.loads(read('ledger/archive_image_aliases.json'))
        assert plan['format_version'] == 1 and plan['current_statement_count'] == 226
        assert plan['aliases'] == aliases
        assert len(aliases) == manifest['image_alias_count']
        frozen_counts, amendment_counts = {}, {}
        for count, expected in [(224, 676), (226, 667)]:
            ledger = json.loads(read(f'ledger/checkpoint{count}_integration.json'))
            mappings = ledger['frozen_to_archive_mapping']
            assert len(mappings) == expected
            for item in mappings:
                assert sha(read(item['archive'])) == item['sha256'], item
            amendments = ledger['active_ledger_amendments']
            assert len(amendments) == 4
            for item in amendments:
                assert sha(read(item['file'])) == item['after_sha256'], item
                assert sha(read(item['author_freeze'])) == item['before_sha256'], item
            frozen_counts[str(count)] = len(mappings)
            amendment_counts[str(count)] = len(amendments)

        pdf_sha = sha(read('LM7_FERMAT_TOWER_paper.pdf'))
        assert pdf_sha == PDF_SHA
        qa = json.loads(read('qa/pdf_qa.json'))
        visual_bytes = read('qa/visual226_root.json')
        visual = json.loads(visual_bytes)
        assert qa['sha256'] == visual['pdf_sha256'] == pdf_sha
        assert qa['pages'] == visual['pdf_pages'] == 728
        assert visual['all_pages_inspected_in_contact_sheets']
        assert visual['observed_layout_defects'] == []
        assert len(visual['contact_sheets']) == 46
        assert len(visual['detail_images']) == 27
        for item in visual['contact_sheets'] + visual['detail_images']:
            assert sha(read(item['path'])) == item['sha256'], item
            assert records[item['path']]['storage_path'] == item['path']
        results = list(csv.DictReader(io.StringIO(read('LM7_FERMAT_TOWER_results.csv').decode())))
        assert len(results) == 226
        assert {r['id'] for r in results} == set(qa['statement_pages'])
        counts = Counter(r['status'] for r in results)
        assert counts == {'Proved': 202, 'Refuted': 9, 'Known': 12, 'Open': 3}, counts
        assert len(json.loads(read('LM7_FERMAT_TOWER_coverage.json'))) == 33
        assert read('LM7_FERMAT_TOWER_report.md').startswith(b'INCOMPLETE\n')
        methods = Counter(info.compress_type for info in z.infolist())
        assert methods[zipfile.ZIP_LZMA] > 0
        result = {
            'status': 'PASS', 'zip_sha256': digest,
            'zip_size': ARCHIVE.stat().st_size,
            'physical_members': len(physical),
            'logical_files_including_manifest': len(records) + 1,
            'logical_file_bytes_checked': logical_bytes,
            'physical_crc_errors': 0,
            'all_manifest_files_byte_equal_to_current_tree': True,
            'image_aliases': len(aliases),
            'all_aliases_exact_historical_QA_raster_bytes': True,
            'all_mathematical_records_are_ordinary_members': True,
            'compression_method_member_counts': dict(methods),
            'exact_frozen_mappings': frozen_counts,
            'active_amendments_and_exact_originals_checked': amendment_counts,
            'missing_files': 0, 'unexplained_changes': 0,
            'pdf_pages': 728, 'pdf_sha256': pdf_sha,
            'numbered_statements': 226, 'statement_status_counts': dict(counts),
            'original_task_rows': 33,
            'visual_record_sha256': sha(visual_bytes),
            'contact_images_rehashed': 46, 'detail_images_rehashed': 27,
            'checked_utc': datetime.now(timezone.utc).isoformat(),
        }
    (BASE / '.lm7_archive226_readback.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
