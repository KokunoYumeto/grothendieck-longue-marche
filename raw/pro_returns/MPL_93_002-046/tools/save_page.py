from pathlib import Path
from datetime import datetime,timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_93_002-046'
FIELDS=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save_page(scan,text,sheet,items,doubts=()):
    path=ROOT/'pages'/f'{PREFIX}_93_scan{scan:03}.tex'
    if path.exists():raise RuntimeError(f'Already exists: {path}')
    text=text.strip()+'\n'
    assert f'\\scanpage{{{scan}}}' in text
    path.write_text(text,encoding='utf-8')
    inventory=ROOT/f'{PREFIX}_inventory.csv'
    exists=inventory.exists()
    with inventory.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if not exists:w.writerow(FIELDS)
        for i,(kind,position,words) in enumerate(items,1):w.writerow(['93',f'{scan:03}',sheet,f'{scan:03}.{i:02}',kind,position,words,'yes'])
    dp=ROOT/'doubt_records.csv';exists=dp.exists()
    with dp.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if not exists:w.writerow(['file','scan','location','reading','alternatives','confidence','reason'])
        for row in doubts:w.writerow(['93',f'{scan:03}',*row])
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'93 scan {scan:03} done {now()}\n')
    print(f'Saved scan {scan:03}: {len(text)} characters; {len(items)} inventory elements; {len(doubts)} doubts.')
