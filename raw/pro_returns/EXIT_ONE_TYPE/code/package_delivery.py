#!/usr/bin/env python3
"""Create the complete research archive and its per-file SHA-256 manifest."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {'__pycache__', 'luatex-cache'}
ROOT_TRANSIENT_SUFFIXES = {'.aux', '.log', '.out', '.toc', '.blg', '.fls', '.fdb_latexmk'}


def deliverable_files():
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.name in {'MANIFEST.sha256', 'missfont.log'}:
            continue
        if path.parent == ROOT and path.suffix in ROOT_TRANSIENT_SUFFIXES:
            continue
        yield path


def main():
    required = ['EXIT_ONE_TYPE_paper.pdf', 'EXIT_ONE_TYPE_paper.tex',
                'EXIT_ONE_TYPE_results.csv', 'EXIT_ONE_TYPE_readings.csv',
                'EXIT_ONE_TYPE_references.bib', 'EXIT_ONE_TYPE_report.md']
    for name in required:
        if not (ROOT/name).is_file():
            raise RuntimeError('Missing required deliverable: '+name)
    files = list(deliverable_files())
    manifest = ROOT/'MANIFEST.sha256'
    lines = [hashlib.sha256(path.read_bytes()).hexdigest()+'  '+str(path.relative_to(ROOT))
             for path in files]
    manifest.write_text('\n'.join(lines)+'\n')
    archive = ROOT.parent/'EXIT_ONE_TYPE.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in [*files, manifest]:
            bundle.write(path, str(Path(ROOT.name)/path.relative_to(ROOT)))
    with zipfile.ZipFile(archive) as bundle:
        if corrupt := bundle.testzip():
            raise RuntimeError('Archive CRC failure: '+corrupt)
        names = bundle.namelist()
    print(json.dumps({'archive': str(archive), 'files': len(names),
                      'bytes': archive.stat().st_size,
                      'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                      'crc_check': 'passed', 'source_manifest_entries': len(files)}, indent=2))


if __name__ == '__main__':
    main()
