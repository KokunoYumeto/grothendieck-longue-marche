"""Freeze or verify the final transcription bytes; never compile TeX."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import sys

OUT = Path(__file__).resolve().parents[1]
ID = 'SP83_C13_148+149'
HASHES = OUT / 'transcription_hashes.tsv'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
if mode == 'freeze':
    if HASHES.exists():
        raise FileExistsError('A transcription freeze already exists')
    pages = (OUT / 'page_order.txt').read_text().splitlines()
    paths = [Path('pages') / (page + '.tex') for page in pages]
    paths.append(Path(ID + '_transcription.tex'))
    rows = [(str(p), digest(OUT / p)) for p in paths]
    with HASHES.open('w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['path', 'sha256'])
        writer.writerows(rows)
    with (OUT / 'progress.log').open('a') as f:
        f.write('transcription frozen ' + now() + '\n')
        for path, sha in rows:
            f.write(f'sha256 {sha} {path}\n')
    print(f'Frozen {len(rows)} transcription files')
elif mode == 'verify':
    with HASHES.open(newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    changed = [row['path'] for row in rows if digest(OUT / row['path']) != row['sha256']]
    if changed:
        raise RuntimeError('Frozen transcription changed: ' + ', '.join(changed))
    with (OUT / 'progress.log').open('a') as f:
        f.write(f'transcription hashes verified unchanged {now()}: {len(rows)} files\n')
    print(f'All {len(rows)} frozen hashes are unchanged')
else:
    raise ValueError('Use freeze or verify')
