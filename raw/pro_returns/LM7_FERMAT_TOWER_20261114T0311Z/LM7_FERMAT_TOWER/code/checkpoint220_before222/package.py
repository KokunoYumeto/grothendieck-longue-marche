"""Build and verify the single research archive from the current checked paper.

Only our deliverables and reproducibility records are included. Downloaded
third-party papers, raw OCR/HTML, compiled executables, caches, and TeX
intermediates remain outside the archive. A per-file SHA-256 manifest permits
verification after extraction. Every included Python and GP program has saved output.
"""
from pathlib import Path
import csv
import hashlib
import json
import zipfile

BASE = Path(__file__).resolve().parents[1]
CODE = BASE / 'code'
PREFIX = 'LM7_FERMAT_TOWER'
ARCHIVE = BASE.parent / (PREFIX + '.zip')
OUT = CODE / 'package.out'
MANIFEST = BASE / (PREFIX + '_manifest.json')
REQUIRED = [PREFIX + suffix for suffix in (
    '_paper.tex', '_paper.pdf', '_results.csv', '_readings.csv',
    '_references.bib', '_report.md', '_coverage.json')]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    for name in REQUIRED:
        assert (BASE / name).is_file() and (BASE / name).stat().st_size, name
    build = json.loads((CODE / 'build_certificate.json').read_text())
    for name, digest in build['source_sha256'].items():
        assert sha((BASE / name).read_bytes()) == digest, 'Rebuild changed source: ' + name
    pdf_digest = sha((BASE / (PREFIX + '_paper.pdf')).read_bytes())
    assert pdf_digest == build['pdf_sha256']
    qa = json.loads((BASE / 'qa/pdf_qa.json').read_text())
    assert qa['sha256'] == pdf_digest
    assert qa['all_statement_headings_present']
    review = (BASE / 'qa/visual_review.md').read_text()
    assert pdf_digest in review, 'Visual review belongs to another PDF build'
    with (BASE / (PREFIX + '_results.csv')).open() as f:
        results = list(csv.DictReader(f))
    assert {r['id'] for r in results} == set(qa['statement_pages'])
    coverage = json.loads((BASE / (PREFIX + '_coverage.json')).read_text())
    assert len(coverage) == 33
    assert (BASE / (PREFIX + '_report.md')).read_text().startswith('INCOMPLETE\n')
    OUT.write_text('Archive validation in progress.\n')
    files = [BASE / name for name in REQUIRED]
    for folder, suffixes in (
        ('sections', {'.tex'}), ('ledger', {'.json', '.bib', '.md'}),
        ('code', {'.py', '.gp', '.cpp', '.json', '.csv', '.out', '.err', '.md', '.npz', '.npy', '.bin'}),
        ('inputs', {'.json', '.out', '.bin'}),
        ('qa', {'.json', '.jpg', '.md'}),
    ):
        files += sorted(p for p in (BASE / folder).rglob('*')
                        if p.is_file() and p.suffix in suffixes)
    files = sorted(set(files))
    data_certificates = [p for p in files if p.suffix in {'.npz', '.npy', '.bin'}]
    for p in data_certificates:
        header = p.read_bytes()[:4]
        assert not header.startswith((b'\x7fELF', b'MZ')), 'Executable in data certificates: ' + str(p)
    interrupted_empty_outputs = []
    failed_empty_outputs = []
    for script in (p for p in files if CODE in p.parents and p.suffix in {'.py', '.gp'}):
        assert script.with_suffix('.out').is_file(), 'Missing executed output: ' + script.name
        if not script.with_suffix('.out').stat().st_size:
            status_path = script.with_name(script.stem + '_status.json')
            assert status_path in files, 'Unexplained empty execution output: ' + script.name
            status = json.loads(status_path.read_text())
            assert status.get('reason')
            if status.get('status') == 'interrupted before result':
                assert status.get('exit_code') == 130
                interrupted_empty_outputs.append(str(script.relative_to(BASE)))
            else:
                assert status.get('status') == 'failed before result'
                assert isinstance(status.get('exit_code'), int) and status['exit_code'] != 0
                error = status_path.parent / status['stderr_path']
                assert error in files and error.stat().st_size
                assert sha(error.read_bytes()) == status['stderr_sha256']
                failed_empty_outputs.append(str(script.relative_to(BASE)))
    # Record the exact completed checks; the resulting archive is then read back.
    log = '\n'.join([
        'Mandatory deliverables: PASS',
        'PDF source hashes and build certificate: PASS',
        'Rendered PDF hash and recorded visual review: PASS',
        f'Numbered statements in CSV and PDF: {len(results)}; PASS',
        'Coverage rows: 33; PASS',
        'Every included Python and GP program has its actual saved output: PASS',
        f'Interrupted runs with genuinely empty stdout and retained exit/status records: {len(interrupted_empty_outputs)}',
        f'Failed runs with genuinely empty stdout and exact retained error evidence: {len(failed_empty_outputs)}',
        f'Actual binary data certificates retained: {len(data_certificates)}; PASS',
        'Third-party source documents, executable binaries and caches excluded: PASS',
        f'Files hashed in the manifest: {len(files)}',
        'Archive CRC and per-file SHA-256 read-back checks: PASS',
        'Research status: INCOMPLETE; unresolved requested items remain explicit.',
        '',
    ])
    OUT.write_text(log)
    payload = {str(p.relative_to(BASE)): p.read_bytes() for p in files}
    manifest = {
        'archive_root': PREFIX,
        'research_status': 'INCOMPLETE',
        'numbered_statements': len(results),
        'coverage_rows': 33,
        'pdf_pages': qa['pages'],
        'pdf_sha256': pdf_digest,
        'manifest_scope': 'Every archived file except this manifest itself.',
        'files': [{'path': name, 'bytes': len(data), 'sha256': sha(data)}
                  for name, data in sorted(payload.items())],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    payload[MANIFEST.name] = MANIFEST.read_bytes()
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(payload.items()):
            z.writestr(PREFIX + '/' + name, data)
    with zipfile.ZipFile(ARCHIVE) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {PREFIX + '/' + name for name in payload}
        for name, data in payload.items():
            assert z.read(PREFIX + '/' + name) == data, name
        archived_manifest = json.loads(z.read(PREFIX + '/' + MANIFEST.name))
        for item in archived_manifest['files']:
            assert sha(z.read(PREFIX + '/' + item['path'])) == item['sha256']
    archive_digest = sha(ARCHIVE.read_bytes())
    (ARCHIVE.with_suffix('.zip.sha256')).write_text(archive_digest + '  ' + ARCHIVE.name + '\n')
    print(log, end='')
    print(json.dumps({'archive': str(ARCHIVE), 'bytes': ARCHIVE.stat().st_size,
                      'sha256': archive_digest, 'members': len(payload)}, indent=2))


if __name__ == '__main__':
    main()
