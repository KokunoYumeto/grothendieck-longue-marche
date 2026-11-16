"""Create a new complete research checkpoint or final ZIP, without overwriting.

Run only at the requested hourly checkpoint or final-delivery time. Supplied
background, previous ZIPs and reproducible runtime/source-download caches
are outside the work tree or explicitly excluded. Mathematical sources,
programs, outputs, logs, reviews and QA records are all retained.
"""
import argparse, datetime, hashlib, json, zipfile
from pathlib import Path

W = Path(__file__).resolve().parents[1]

def include(p):
    rel = p.relative_to(W)
    if not p.is_file(): return False
    if '__pycache__' in rel.parts: return False
    if 'native' in rel.parts: return False  # reproducible local FLINT runtime
    if 'sources' in rel.parts or 'source_checks' in rel.parts: return False  # third-party article/page cache
    if p.suffix in {'.zip', '.pyc'}: return False
    if '_temporary' in p.name: return False  # reproducible third-party source scans
    if p.name.startswith('Katz1981_') and p.suffix in {'.png', '.pdf'}: return False
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--kind', choices=['checkpoint', 'final'], required=True)
    parser.add_argument('--utc', required=True, help='Observed clock time, not filesystem clock')
    args = parser.parse_args()
    out = Path(args.output).resolve()
    if out.exists(): raise SystemExit('Refusing to overwrite an existing archive')
    manifest = {'kind': args.kind, 'observed_utc': args.utc,
                'status': 'INCOMPLETE',
                'exclusions': ['supplied background and attachments', 'previous ZIPs',
                               'Python caches', 'temporary reproducible third-party source scans',
                               'Katz1981 PDF and source-page download cache',
                               'third-party article and source-page caches in sources/source_checks directories',
                               'reproducible local native dependency runtime'],
                'files': []}
    with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=8) as z:
        for p in sorted(W.rglob('*')):
            if not include(p): continue
            data = p.read_bytes(); rel = str(p.relative_to(W))
            z.writestr(rel, data)
            manifest['files'].append({'path': rel, 'bytes': len(data),
                                      'sha256': hashlib.sha256(data).hexdigest()})
        z.writestr('ARCHIVE_MANIFEST.json', json.dumps(manifest, indent=2) + '\n')
    with zipfile.ZipFile(out) as z:
        error = z.testzip()
        assert error is None, error
        assert 'ANABELIAN_SUCCESSOR_paper.tex' in z.namelist()
        assert 'ANABELIAN_SUCCESSOR_paper.pdf' in z.namelist()
        assert 'ANABELIAN_SUCCESSOR_report.md' in z.namelist()
    result = {'path': str(out), 'bytes': out.stat().st_size,
              'entries': len(manifest['files']) + 1,
              'sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
              'observed_utc': args.utc, 'zip_integrity': 'passed'}
    (W / 'notes' / (out.stem + '_manifest.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
