"""Freeze, or verify, the 25 audited page files and combined transcription."""
from pathlib import Path
import csv, datetime, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
mode = sys.argv[1]
order = (ROOT / 'page_order.txt').read_text().splitlines()
files = [ROOT / 'pages' / (page + '.tex') for page in order]
files.append(ROOT / 'SP92_C13_150+151_transcription.tex')
manifest = ROOT / 'TRANSCRIPTION_SHA256.tsv'
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if mode == 'freeze':
    assert not manifest.exists(), 'A frozen manifest already exists; do not silently refreeze.'
    assert len(order) == 25
    for page in order:
        record = json.loads((ROOT / 'records' / (page + '.json')).read_text())
        assert record.get('root_reviewed') and record.get('audited'), page
    rows = [{'file': str(path.relative_to(ROOT)), 'sha256': digest(path)} for path in files]
    with manifest.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['file', 'sha256'], delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(f'transcription frozen {now}\n')
        for row in rows:
            stream.write(f"SHA-256 {row['sha256']}  {row['file']}\n")
    print(json.dumps({'frozen_files': len(rows), 'utc': now}))
elif mode == 'verify':
    with manifest.open(newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    assert {row['file'] for row in rows} == {str(path.relative_to(ROOT)) for path in files}
    changed = [row['file'] for row in rows if digest(ROOT / row['file']) != row['sha256']]
    assert not changed, 'Frozen transcription changed: ' + ', '.join(changed)
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(f'Frozen SHA-256 verification {now}: all 25 page files and combined transcription unchanged.\n')
    print(json.dumps({'unchanged_files': len(rows), 'utc': now}))
else:
    raise SystemExit('Use freeze or verify.')
