"""Validate and package the final deliverable; never write frozen TeX files."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import csv
import hashlib
import re
import zipfile

root = Path(__file__).resolve().parents[1]
prefix = 'MPL_15_170-194r'
order = [170,171,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194]
archive = root.parent / (prefix + '.zip')
assert not archive.exists(), 'Refusing to overwrite an existing final ZIP.'

frozen = []
for line in (root / 'records/frozen_sha256.txt').read_text().splitlines():
    digest, name = line.split(None, 1)
    path = root / name.strip()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, str(path)
    frozen.append((digest, name.strip()))
assert len(frozen) == 19

parts = [(root / 'pages' / f'{prefix}_15_scan{n:03d}.tex').read_text() for n in order]
combined = (root / (prefix + '_transcription.tex')).read_text()
assert combined == '\n'.join(s.rstrip() + '\n' for s in parts)
assert re.findall(r'\\scanpage\{(\d+)\}', combined) == [str(n) for n in order]
assert combined.startswith('\\cotefile{15}\n\\scanpage{170}')
assert '\\documentclass' not in combined and '\\includegraphics' not in combined

rows = list(csv.DictReader((root / (prefix + '_inventory.csv')).open()))
assert len(rows) == 282
assert all(r['transcribed'] == 'yes' and r['cote'] == '15' for r in rows)
assert set(int(r['scan']) for r in rows) == set(order)
doubts = (root / (prefix + '_doubts.md')).read_text()
indexed = collections.Counter(int(m.group(1)) for m in re.finditer(r'^\| 15 \| (\d+) \|', doubts, re.M))
assert all(indexed[n] == text.count('\\unsure{') for n, text in zip(order, parts))
assert sum(indexed.values()) == 146

notes = (root / (prefix + '_notes.md')).read_text()
assert len(re.findall(r'^### [A-Z]+\d{2} —', notes, re.M)) == 59
labels = re.findall(r'\*\*Kind:\*\* ([^.]+)\.', notes)
allowed = {'conjecture', 'unproved claim', 'unpursued implication', 'own idea',
           'reading question', 'self-flagged', 'withdrawn in the same text'}
assert len(labels) == 59 and set(labels) <= allowed
assert len(re.findall(r'^\| [UT]\d{2} —', notes, re.M)) == 21
assert not re.search(r'turn\d+(?:view|search)', notes)
assert notes.count(r'\(') == notes.count(r'\)')
table_columns = None
for line in notes.splitlines():
    if line.startswith('|'):
        columns = len(re.split(r'(?<!\\)\|', line)) - 2
        if table_columns is None:
            table_columns = columns
        else:
            assert columns == table_columns, (columns, table_columns, line)
    else:
        table_columns = None

stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root / 'records/validation.md').open('a') as f:
    f.write('\n# Delivery verification\n\n')
    f.write(f'- Verified {stamp}: all 19 frozen SHA-256 values unchanged.\n')
    f.write('- Combined text exactly equals the 18 frozen page fragments in the requested order.\n')
    f.write('- All 282 inventory elements remain marked yes; all 146 uncertainty occurrences are indexed, with per-page counts matching.\n')
    f.write('- Research: 59 main notes with allowed kinds and 21 standing-register entries; mathematical delimiters and Markdown table widths checked.\n')
    f.write('- Research review corrections concern only the notes; the transcription was not reopened for correction after context access.\n')
    f.write('- Final archive excludes input scans, contextual source files, inspection images, bytecode caches, and superseded research assembly drafts.\n')
    f.write('- The pre-freeze compilation limitation remains: structural checks are not a successful TeX compile.\n')

with (root / 'progress.log').open('a') as f:
    f.write(f'research completed {stamp}; 59 main notes and 21 standing-register entries; contextual and primary-source review complete within recorded limits.\n')
    f.write(f'frozen transcription hashes unchanged {stamp}; all 18 page files and combined transcription verified against the frozen SHA-256 list.\n')
    f.write(f'final ZIP prepared {stamp}; all required deliverables included; supplied scans/context excluded.\n')

canonical = [prefix + suffix for suffix in ['_transcription.tex', '_doubts.md', '_inventory.csv', '_notes.md']]
files = [root / name for name in canonical] + [root / 'progress.log']
files += [root / 'pages' / f'{prefix}_15_scan{n:03d}.tex' for n in order]
record_names = ['README.md', 'notation.md', 'abbreviations_and_legibility.md',
                'visual_audit.md', 'reading_observations.md', 'validation.md',
                'frozen_sha256.txt', 'research_review.md']
files += [root / 'records' / name for name in record_names]
files += sorted(p for p in (root / 'scripts').glob('*.py') if p.name != 'assemble_notes.py')
assert len(files) == len(set(files))
assert all(p.is_file() for p in files)
files = sorted(files, key=lambda p: p.relative_to(root).as_posix())
manifest = root / 'records/final_manifest.sha256'
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(root).as_posix() + '\n' for p in files))
files.append(manifest)
with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for path in files:
        z.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
    assert all(not name.startswith('/') and '..' not in Path(name).parts for name in z.namelist())
    assert not any(Path(name).suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip','.pyc'} for name in z.namelist())
    for digest, name in frozen:
        assert hashlib.sha256(z.read(name)).hexdigest() == digest
print(f'Final ZIP: {archive}')
print(f'Files: {len(files)}; bytes: {archive.stat().st_size}')
print(f'SHA-256: {hashlib.sha256(archive.read_bytes()).hexdigest()}')
print('ZIP CRC verified; all 19 frozen files verified inside the archive; all required deliverables present.')
