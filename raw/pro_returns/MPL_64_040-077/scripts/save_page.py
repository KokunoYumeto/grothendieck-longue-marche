from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]

def save_page(scan, tex, elements, doubts=(), observations=(), notation=()):
    path = ROOT / 'pages' / f'MPL_64_040-077_64_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Page {scan} already exists; edit explicitly instead.')
    if scan > 40 and not (ROOT / 'pages' / f'MPL_64_040-077_64_scan{scan-1:03d}.tex').exists():
        raise RuntimeError('Pages must be saved in sequence.')
    path.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT / 'MPL_64_040-077_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,item in enumerate(elements,1):
            kind,position,words,*sheet = item
            w.writerow(['64',f'{scan:03d}',sheet[0] if sheet else 'text',f'{scan:03d}.{i:02d}',kind,position,words,'yes'])
    dpath=ROOT / 'MPL_64_040-077_doubts.md'
    d=dpath.read_text(encoding='utf-8')
    esc=lambda s:str(s).replace('|',r'\|').replace('\n',' ')
    rows=''.join('| 64 | %03d | %s | `%s` | %s | %s |\n'%(scan,esc(pos),esc(reading),esc(alt),conf) for pos,reading,alt,conf in doubts)
    d=d.replace('\n# Abbreviations', '\n'+rows+'\n# Abbreviations')
    if notation:
        nr=''.join('| %s | `%s` | scan %03d: %s |\n'%(esc(sign),esc(latex),scan,esc(note)) for sign,latex,note in notation)
        d=d.replace('\n# Reading doubts','\n'+nr+'\n# Reading doubts')
    dpath.write_text(d,encoding='utf-8')
    if observations:
        with (ROOT/'observations_before_context.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n'+'\n\n'.join(observations)+'\n')
    combined='\n'.join(p.read_text(encoding='utf-8').rstrip() for p in sorted((ROOT/'pages').glob('*.tex')))+'\n'
    (ROOT/'MPL_64_040-077_transcription.tex').write_text(combined,encoding='utf-8')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'64 scan {scan:03d} done {now}\n')
    print(f'Saved scan {scan:03d}; {len(elements)} inventory elements; {len(doubts)} doubt rows. {now}')
