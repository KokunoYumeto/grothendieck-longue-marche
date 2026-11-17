"""Record checkpoint31 only after immutable, native-TAR and saved-identity checks."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import struct
import zipfile


def main():
    root = Path(__file__).resolve().parents[1]
    read = lambda name: json.loads((root / 'records' / name).read_text())
    v = read('checkpoint31_archive_verification.json')
    t = read('checkpoint31_system_tars_verification.json')
    results = read('checkpoint31_upload_result.json')['results']
    assert len(results) == 1
    r = results[0]
    assert r['status'] == 'succeeded' and r['local_metadata_applied']
    found = []

    def walk(value):
        if isinstance(value, dict):
            if value.get('library_file_id') == r['library_file_id'] and value.get('name') == r['file_name']:
                found.append(value)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(read('checkpoint31_library_metadata.json'))
    assert len(found) == 1
    item = found[0]
    assert r['file_name'] == v['archive'] == t['archive'] == 'LM4_SUCCESSOR_checkpoint_31.zip'
    assert item['size_bytes'] == v['bytes'] <= 536870912
    assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
    assert v['prior_entries_retained'] == 123532
    assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
    assert t['all_three_system_tar_restores'] == t['current_main_pdf_direct'] == 'PASS'
    assert t['all_three_container_zip_lzma_methods'] == 'PASS'
    assert t['data_lzma_dictionary_bytes'] == 67108864
    assert t['archive_sha256'] == v['sha256']
    for kind in ('images', 'documents', 'data'):
        assert t['containers'][kind]['system_tar_restore'] == 'PASS'
        assert t['containers'][kind]['every_original_path_size_and_hash'] == 'PASS'
    retention = read('checkpoint_version_retention_summary.json')
    assert retention['archives'] == 30 and retention['archive_entries'] == 123532
    assert retention['omissions'] == 0
    m = read('checkpoint31_metrics.json')
    assert m['statements'] == 333 and m['task_rows'] == 49 and m['bibliography_entries'] == 114
    assert m['statuses'] == {'Known': 6, 'Proved': 289, 'Refuted': 19, 'Open': 19}
    release = read('checkpoint31_writer_release.json')
    p = read('checkpoint_31_packaging.json')
    for kind, field, hardlinks in (
            ('images', 'image', 'standard_tar_hardlinks'),
            ('documents', 'document', 'standard_tar_document_hardlinks'),
            ('data', 'data', 'standard_tar_data_hardlinks')):
        assert p[field + '_paths'] == t['containers'][kind]['paths']
        assert p[hardlinks] == t['containers'][kind]['hardlink_paths']
        assert p[field + '_bundle_sha256'] == t['containers'][kind]['bundle_sha256']
        assert p[field + '_zip_method'] == 'ZIP_LZMA'
    assert p['data_lzma_dictionary_bytes'] == 67108864

    archive = root.parent / v['archive']
    assert archive.stat().st_size == v['bytes']
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == v['sha256']
    prefix = 'LM4_SUCCESSOR/'
    with zipfile.ZipFile(archive) as z:
        assert json.loads(z.read(prefix + 'records/checkpoint_31_packaging.json')) == p
        assert json.loads(z.read(prefix + 'records/checkpoint31_metrics.json')) == m
        assert json.loads(z.read(prefix + 'records/checkpoint_version_retention_summary.json')) == retention
        pdf = z.read(prefix + 'LM4_SUCCESSOR_paper.pdf')
        assert len(pdf) == m['pdf_bytes'] and hashlib.sha256(pdf).hexdigest() == m['pdf_sha256']
        # Agents resume immediately after capture. Describe the captured records,
        # not later mutable inventory or research files in the active workspace.
        inventory_text = z.read(prefix + 'records/computation_inventory.csv').decode()
        inventory_count = len(list(csv.DictReader(inventory_text.splitlines())))
        review = z.read(prefix + 'records/progress_review_31h.md').decode()
        qa = json.loads(z.read(prefix + 'records/checkpoint31_visual_review.json'))
        late = json.loads(z.read(prefix + 'records/checkpoint31_root_late_reviews.json'))
        for basename in ('verification_images.tar', 'historical_documents.tar', 'historical_data.tar'):
            assert z.getinfo(prefix + basename).compress_type == zipfile.ZIP_LZMA
        data_info = z.getinfo(prefix + 'historical_data.tar')
    with archive.open('rb') as raw:
        raw.seek(data_info.header_offset)
        header = raw.read(30)
        assert header[:4] == b'PK\x03\x04'
        name_size, extra_size = struct.unpack('<HH', header[26:30])
        raw.seek(name_size + extra_size, 1)
        properties = raw.read(9)
    assert properties[:2] == bytes([9, 4]) and struct.unpack('<H', properties[2:4])[0] == 5
    assert struct.unpack('<I', properties[5:9])[0] == 67108864

    review_time = re.search(r'^Actual review record: (.+)\.$', review, re.M).group(1)
    driver = (root / 'records/checkpoint31_capture_driver.log').read_text()
    capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
    record = f'''## Checkpoint31: saved and verified

Review:{review_time}, CONTINUE.
Immutable capture completed:{capture_time}.
Writer release recorded:{release['released_at']}.
Creation:{item['created_at']}.
Archive:{r['file_name']}.
Bytes:{v['bytes']}; logical entries:{v['entries']};
physical ZIP entries:{v['physical_zip_entries']}; manifest rows:{v['manifest_rows']}.
SHA-256:{v['sha256']}.
Library ID:{r['library_file_id']}.
File ID:{r['file_id']}. Version:0.
Independent metadata matches name, size, identity and version; local identity applied.

CRC, every logical manifest entry and every retained version:PASS.
All123532 logical entries of the30 previous immutable archives are retained
byte-exactly with zero omissions. History contains
{retention['total_historical_copies']} distinct copies totaling
{retention['total_historical_bytes']} bytes. The computation inventory has
{inventory_count} programs at capture. The standard image TAR retains
{p['image_paths']} original PNG paths with{p['standard_tar_hardlinks']} hardlinks;
the standard document TAR retains{p['document_paths']} historical/preview
PDF paths with{p['standard_tar_document_hardlinks']} hardlinks; the standard
data TAR retains{p['data_paths']} selected original paths with
{p['standard_tar_data_hardlinks']} hardlinks. All three use lossless
ZIP_LZMA. The actual data-stream property is64MiB, independently read from
its ZIP local header and checked against the packaging and native verification.
The current main PDF remains a direct ZIP entry.
Independent native tar extraction of all three actual archived containers
verified every original path, size and byte hash without importing the
packager or its logical reader. Restore from the ZIP extraction parent:
tar -xf LM4_SUCCESSOR/verification_images.tar
tar -xf LM4_SUCCESSOR/historical_documents.tar
tar -xf LM4_SUCCESSOR/historical_data.tar
All30 earlier archives remain unchanged. Exactly one new ZIP was created.

The formal PDF has {m['pages']} pages and333 statements:289 Proved,
19 Refuted,19 Open and6 Known; all114 references are printed and49 task rows retained.
PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
The final combined build has no overfull boxes, actual warnings, undefined
references or errors. Both final engine stdout and full log were scanned
case-insensitively. The final accepted underfull notice count is
{len(qa['final_log_and_stdout_audits'][0]['underfull_notices'])};
the complete accepted scope is: {qa['underfull_scope']}.
All {len(qa['required_math_pages'])} new mathematical pages were individually
inspected within {len(qa['individually_inspected_pages'])} individual views.
The {qa['contact_sheets_inspected']} separately inspected contact sheets cover
{len(qa['rendered_pages'])} final rendered pages.

All ten frozen formal sources A92--A94 and B148--B154 have complete root
and independent source reviews. The separate late record binds
{len(late['proof_sources'])} complete proof records at their exact current
scopes without promoting additional formal statements. The actual odd-head,
icosahedral, and full ambient filling/fixed-source gates remain explicit.
Neither carrier properness nor quotient or nonsplitting results settle
either main decision. Main A and Main B remain Open.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint32. Agents resume substantive research after capture,
before verification and saving, according to the recorded writer release.
Next review/checkpoint:2026-11-17 08:49:30 UTC.
'''
    destinations = [root / rel for rel in ('records/checkpoints.md', 'records/continuation_state.md')]
    old_values = [path.read_text() for path in destinations]
    assert all('## Checkpoint31: saved and verified' not in old for old in old_values)
    for path, old in zip(destinations, old_values):
        path.write_text(old + '\n' + record)
    print('Checkpoint31 archive, three native TAR restorations, actual64MiB stream, receipt and metadata agree.')
    print('Delivery record written', datetime.now(timezone.utc).isoformat())


if __name__ == '__main__':
    main()
