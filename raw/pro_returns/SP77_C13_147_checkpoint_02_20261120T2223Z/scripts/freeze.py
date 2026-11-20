"""Freeze and verify the completed transcription without compiling TeX."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
W = Path(__file__).resolve().parents[1]
from manage import SCANS
paths = [W / 'pages' / f'147_scan{n:03d}.tex' for n in SCANS] + [W / 'SP77_C13_147_transcription.tex']
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest = W / 'transcription_sha256.tsv'
if sys.argv[1] == 'freeze':
    assert not manifest.exists(), 'Never silently replace a freeze manifest'
    for n in SCANS:
        r = json.loads((W / 'records' / f'147_scan{n:03d}.json').read_text())
        assert r.get('audit') and r.get('main_review'), f'incomplete page {n}'
    data = [(str(p.relative_to(W)), digest(p)) for p in paths]
    manifest.write_text('file\tsha256\n' + ''.join(f'{p}\t{h}\n' for p,h in data))
    with (W / 'progress.log').open('a') as f:
        f.write('transcription frozen ' + stamp() + '\n')
        for p,h in data: f.write(f'SHA-256 {p} {h}\n')
elif sys.argv[1] == 'verify':
    data = [line.split('\t') for line in manifest.read_text().splitlines()[1:]]
    assert [p for p,h in data] == [str(p.relative_to(W)) for p in paths]
    bad = [p for p,h in data if digest(W/p) != h]
    assert not bad, 'Frozen files changed: ' + repr(bad)
    with (W / 'progress.log').open('a') as f:
        f.write('frozen transcription hashes verified unchanged ' + stamp() + ': 24 page files and combined transcription\n')
else: raise ValueError('freeze or verify required')
print(sys.argv[1] + ' completed')
