from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_002-049'
HEADER = ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save(scan, text, elements, sheet_kind='text', observations=''):
    path=ROOT/'pages'/f'{PREFIX}_33_scan{scan:03d}.tex'
    if path.exists():
        raise ValueError(f'Already saved: {path}')
    expected=f'\\scanpage{{{scan}}}'
    assert expected in text
    path.write_text(text.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    new=not inv.exists()
    with inv.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if new: w.writerow(HEADER)
        for i,(kind,position,first) in enumerate(elements,1):
            w.writerow([33,scan,sheet_kind,f'{scan:03d}-{i:02d}',kind,position,first,'yes'])
    if observations:
        p=ROOT/'records'/'precontext_observations.md'
        p.parent.mkdir(exist_ok=True)
        with p.open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'33 scan {scan:03d} done {now()}\n')
    print(f'Saved scan {scan:03d}: {len(elements)} inventory elements, {len(text)} characters; {now()}')
