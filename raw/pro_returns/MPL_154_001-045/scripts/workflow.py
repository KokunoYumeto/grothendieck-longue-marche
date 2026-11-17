from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib, zipfile

ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_154_001-045'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save_page(n, tex, elements, doubts=(), observations='', sheet_kind='text'):
    path=ROOT/'pages'/f'{PREFIX}_154_scan{n:03d}.tex'
    if path.exists():
        raise FileExistsError(path)
    text=tex.strip()+'\n'
    assert f'\\scanpage{{{n}}}' in text
    path.write_text(text)
    with (ROOT/f'{PREFIX}_inventory.csv').open('a', newline='') as f:
        w=csv.writer(f)
        for i,(kind,position,incipit) in enumerate(elements,1):
            w.writerow(['154',f'{n:03d}',sheet_kind,f'{n:03d}.{i:02d}',kind,position,incipit,'yes'])
    if doubts:
        p=ROOT/f'{PREFIX}_doubts.md'
        s=p.read_text()
        rows=''.join('| 154 | '+str(n)+' | '+' | '.join(str(v).replace('|',' / ').replace('\n',' ') for v in d)+' |\n' for d in doubts)
        s=s.replace('\n# Abbreviations\n','\n'+rows+'\n# Abbreviations\n')
        p.write_text(s)
    if observations:
        with (ROOT/'records/reading_observations.md').open('a') as f:
            f.write(f'\n## Scan {n:03d}\n\n'+observations+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'154 scan {n:03d} whole and both halves read; immediate comparison and inventory completed {utc()}\n')
        f.write(f'154 scan {n:03d} done {utc()}\n')
    combine()
    print(f'Saved scan {n:03d}: {len(text)} characters, {len(elements)} inventory elements.')

def combine():
    pages=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text() for p in pages))

def checkpoint(number):
    dest=ROOT.parent/f'{PREFIX}_checkpoint_{number:02d}.zip'
    if dest.exists():
        raise FileExistsError(dest)
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                z.write(p,p.relative_to(ROOT))
    print(dest)

if __name__=='__main__':
    import sys
    if len(sys.argv)>1 and sys.argv[1]=='checkpoint': checkpoint(int(sys.argv[2]))
    else: combine()
