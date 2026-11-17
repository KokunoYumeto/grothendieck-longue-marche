"""Record a visually read page; never performs OCR or reads context/scans."""
from pathlib import Path
import csv, json, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record(scan, tex, elements, doubts=(), notes=(), sheet_kind='text', notation=()):
    path = ROOT / 'pages' / f'MPL_83_178-222_83_scan{scan:03}.tex'
    if path.exists():
        raise RuntimeError(f'Page already recorded: {scan}')
    path.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_83_178-222_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,incipit) in enumerate(elements,1):
            w.writerow([83,scan,sheet_kind,f'{scan}.{i:02}',kind,position,incipit,'yes'])
    rec={'scan':scan,'sheet_kind':sheet_kind,'doubts':doubts,'notes':notes,'notation':notation,'elements':elements}
    (ROOT/'records'/f'{scan:03}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'83 scan {scan:03} done {utc()}\n')
    print(f'Saved scan {scan}: {len(elements)} inventory elements; {len(doubts)} doubt notes')

if __name__=='__main__':
    record(**json.load(sys.stdin))
