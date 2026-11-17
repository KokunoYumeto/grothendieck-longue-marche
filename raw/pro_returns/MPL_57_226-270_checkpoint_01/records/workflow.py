from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, hashlib, zipfile

BASE = Path(__file__).resolve().parents[1]
EXPECTED = [n for n in range(226,271) if n not in (232,247)]
def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(message):
    with (BASE/'progress.log').open('a',encoding='utf-8') as f:
        f.write(message+'\n')
def save_page(scan, tex, elements, doubts=(), observations='', sheet_kind='text'):
    path = BASE/'pages'/f'MPL_57_226-270_57_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError('Use a documented audit correction for an existing page')
    existing = [int(p.stem[-3:]) for p in (BASE/'pages').glob('*.tex')]
    if scan != next(n for n in EXPECTED if n not in existing):
        raise RuntimeError('Pages must be written in order')
    assert f'\\scanpage{{{scan}}}' in tex
    path.write_text(tex.strip()+'\n',encoding='utf-8')
    with (BASE/'MPL_57_226-270_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,incipit) in enumerate(elements,1):
            w.writerow(['57',scan,sheet_kind,f'{scan}.{i:02d}',kind,position,incipit,'yes'])
    with (BASE/'MPL_57_226-270_doubts.md').open('a',encoding='utf-8') as f:
        for place,reading,alternative,confidence in doubts:
            vals = [str(v).replace('|',' / ').replace('\n',' ') for v in ('57',scan,place,reading,alternative,confidence)]
            f.write('| '+' | '.join(vals)+' |\n')
    if observations:
        with (BASE/'records/pre_context_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{observations}\n')
    log(f'57 scan {scan:03d} done {now()}')
    combine()
    print(f'Saved scan {scan}; {len(existing)+1}/{len(EXPECTED)} pages; {len(elements)} inventory elements; {now()}')
def combine():
    pages=sorted((BASE/'pages').glob('*.tex'))
    (BASE/'MPL_57_226-270_transcription.tex').write_text('\n'.join(p.read_text(encoding='utf-8') for p in pages),encoding='utf-8')
def freeze():
    pages=sorted((BASE/'pages').glob('*.tex'))
    assert [int(p.stem[-3:]) for p in pages] == EXPECTED
    text=(BASE/'progress.log').read_text()
    assert all(f'scan {n:03d} audited ' in text for n in EXPECTED)
    combine()
    hashes={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[BASE/'MPL_57_226-270_transcription.tex']}
    (BASE/'records/frozen_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    for path,digest in hashes.items(): log(f'SHA-256 {digest} {path}')
    log(f'transcription frozen {now()}')
def check_frozen():
    hashes=json.loads((BASE/'records/frozen_hashes.json').read_text())
    for path,digest in hashes.items():
        assert hashlib.sha256((BASE/path).read_bytes()).hexdigest()==digest,path
    log(f'frozen hashes unchanged ({len(hashes)} files) {now()}')
    print('Frozen hashes unchanged')
def archive(path):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BASE.rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts and f.suffix != '.zip':
                z.write(f,f.relative_to(BASE))
    print(path)
