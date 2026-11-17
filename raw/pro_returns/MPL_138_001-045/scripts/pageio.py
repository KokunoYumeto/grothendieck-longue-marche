from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save_page(scan, text, elements, *, kind='text', doubts=(), notation=(), leads=()):
    path = ROOT / 'pages' / f'MPL_138_001-045_138_scan{scan:03d}.tex'
    if path.exists():
        raise FileExistsError(path)
    path.write_text(text.strip()+'\n', encoding='utf8')
    with (ROOT/'MPL_138_001-045_inventory.csv').open('a', newline='', encoding='utf8') as f:
        writer=csv.writer(f)
        for i, (typ, pos, words) in enumerate(elements, 1):
            writer.writerow([138, scan, kind, f'{scan:03d}-{i:02d}',typ,pos,words,'yes'])
    with (ROOT/'records/doubts_rows.md').open('a', encoding='utf8') as f:
        for pos, reading, alternatives, confidence in doubts:
            cells=[138,f'{scan:03d}',pos,reading,alternatives,confidence]
            f.write('| '+' | '.join(str(x).replace('|',' / ') for x in cells)+' |\n')
    with (ROOT/'records/notation_rows.md').open('a', encoding='utf8') as f:
        for row in notation:
            f.write(f'- scan {scan:03d}: {row}\n')
    with (ROOT/'records/research_leads.md').open('a', encoding='utf8') as f:
        for row in leads:
            f.write(f'- scan {scan:03d}: {row}\n')
    with (ROOT/'progress.log').open('a', encoding='utf8') as f:
        f.write(f'138 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(text)} characters, {len(elements)} inventory elements at {utc()}')

