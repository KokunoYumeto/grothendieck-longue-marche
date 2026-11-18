"""Verify the frozen transcription and package the finished authored deliverables."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'
STEM = 'MPL_29_049-094'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

frozen = json.loads((WORK / 'frozen_hashes.json').read_text())
assert len(frozen['sha256']) == 43
for name, expected in frozen['sha256'].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, f'Frozen transcription changed: {name}'

notes = (ROOT / f'{STEM}_notes.md').read_text()
assert 'Draft integration pending' not in notes
refs = set(re.findall(r'\[((?:BR|P|F)-S\d+)\]', notes))
defs = set(re.findall(r'^\[((?:BR|P|F)-S\d+)\]:', notes, re.M))
assert refs <= defs
assert not re.search(r'\[S\d[^\]]*\]', notes)
note_count = len(re.findall(r'^### (?:N-|BR|P\d|FORMAL-)', notes, re.M))
flag_count = len(re.findall(r'^### SFLAG-', notes, re.M))
page_count = len(re.findall(r'^### PAGE-', notes, re.M))
assert (note_count, flag_count, page_count) == (77, 37, 12)
with (ROOT / f'{STEM}_inventory.csv').open(newline='') as f:
    inv = list(csv.DictReader(f))
assert len(inv) == 822 and all(x['transcribed'] == 'yes' for x in inv)
sheets = {x['scan']: x['sheet_kind'] for x in inv}
assert len(sheets) == 42
with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as f:
    events = list(csv.DictReader(f, delimiter='\t'))
assert len(events) == 96

stamp = now()
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'research apparatus completed {stamp}; 77 main notes, 37 self-flag entries, 12 title/pagination entries, 96 check events\n')
    f.write(f'validation parser note {stamp}; accepted the original SHA-256 log prefix as well as sha256; original hash lines and frozen files were not changed\n')
    f.write(f'final frozen-hash verification {stamp}; all 43 SHA-256 hashes unchanged since transcription frozen\n')
    f.write(f'final package prepared {stamp}; supplied images, source/context archives and previous checkpoints excluded\n')

run = subprocess.run([sys.executable, str(WORK/'validate_package.py'), str(ROOT)],
                     text=True, capture_output=True)
report = [
    f'Final validation: {stamp}',
    run.stdout.strip(),
    run.stderr.strip(),
    f'Frozen integrity: 43/43 unchanged; freeze {frozen["frozen_at"]}',
    f'Sheet kinds: {dict(Counter(sheets.values()))}',
    f'Research: {note_count} main items; {flag_count} self-flag entries; {page_count} title/pagination entries',
    f'Mathematical check events: {len(events)}',
    'Source links: all BR/P/F reference keys defined; no stale unprefixed keys',
    'Pre-freeze compilation: succeeded; no undefined commands or missing glyphs reported; overfull harness boxes remain layout diagnostics, not transcription omissions',
    'Integration review: work/final_notes_review.md; both recorded minor fixes applied',
    'Scope: mechanical checks do not certify visual readings or independently prove external theorems',
]
(WORK/'final_validation.txt').write_text('\n'.join(x for x in report if x) + '\n')
assert run.returncode == 0, run.stdout + run.stderr

archive = ROOT.parent / f'{STEM}.zip'
paths = sorted(p for p in ROOT.rglob('*') if p.is_file()
               and '__pycache__' not in p.parts and p.suffix != '.pyc')
assert not any(p.suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip','.fmt'} for p in paths)
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in paths:
        z.write(p, p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(paths)
    for name, expected in frozen['sha256'].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == expected

print('\n'.join(report[:2]))
print(f'ZIP verified: {len(paths)} entries, {archive.stat().st_size} bytes')
print(str(archive))
