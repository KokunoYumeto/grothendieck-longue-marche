from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_93_092-134'
HEADER=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def finish(scan, text, elements, doubts=(), sheet='text'):
    path=ROOT/'pages'/f'{PREFIX}_93_scan{scan:03d}.tex'
    if path.exists(): raise RuntimeError(f'Page already exists: {scan}')
    path.write_text(text.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    new=not inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if new:w.writerow(HEADER)
        for i,(kind,pos,words) in enumerate(elements,1):w.writerow(['93',scan,sheet,f'{scan:03d}.{i:02d}',kind,pos,words,'yes'])
    with (ROOT/'documentation/doubts_rows.tsv').open('a',encoding='utf-8') as f:
        for line,reading,alternative,confidence in doubts:
            f.write('\t'.join(['93',str(scan),line,reading,alternative,confidence])+'\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'93 scan {scan:03d} done {now()}\n')
    print(f'Saved scan {scan:03d}: {len(text)} characters; {len(elements)} inventory elements; {len(doubts)} doubt entries. {now()}')
