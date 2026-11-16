from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def write_page(scan, tex, elements, doubts=(), leads='', sheet_kind='text'):
    path = ROOT/'pages'/f'MPL_15_139-194_15_scan{scan:03d}.tex'
    if path.exists():
        raise FileExistsError(path)
    path.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_15_139-194_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,opening) in enumerate(elements,1):
            w.writerow([15,scan,sheet_kind,f'{scan}.{i:02d}',kind,position,opening,'yes'])
    d=ROOT/'MPL_15_139-194_doubts.md'
    text=d.read_text(encoding='utf-8')
    rows=''.join('| 15 | '+str(scan)+' | '+' | '.join(str(x).replace('|',' / ') for x in row)+' |\n' for row in doubts)
    text=text.replace('\n# Abbreviations\n','\n'+rows+'\n# Abbreviations\n')
    d.write_text(text,encoding='utf-8')
    if leads:
        with (ROOT/'research_leads_before_context.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{leads}\n')

def done(scan):
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'15 scan {scan:03d} done {now()}\n')

def audit(scan):
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03d} audited {now()}\n')
