from pathlib import Path
from datetime import datetime, timezone
import csv, json

ROOT = Path(__file__).resolve().parent
PREFIX = 'MPL_68_033-056+162-1+162-6'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record(scan, tex, elements, doubts=(), sheet_kind='text'):
    page = ROOT/'pages'/f'{PREFIX}_68_scan{scan:03}.tex'
    if page.exists():
        raise RuntimeError(f'Already recorded: {scan}')
    page.write_text(tex.strip()+'\n', encoding='utf-8')
    inventory = ROOT/f'{PREFIX}_inventory.csv'
    exists = inventory.exists()
    with inventory.open('a', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        if not exists:
            w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,pos,anchor) in enumerate(elements,1):
            w.writerow(['68',scan,sheet_kind,f'{scan:03}-{i:02}',kind,pos,anchor,'yes'])
    with (ROOT/'doubts_rows.jsonl').open('a',encoding='utf-8') as f:
        for pos,reading,alternatives,confidence in doubts:
            f.write(json.dumps(dict(cote='68',scan=scan,position=pos,reading=reading,alternatives=alternatives,confidence=confidence),ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'68 scan {scan:03} done {utc()}\n')
    print(f'Saved 68 scan {scan:03}: {len(elements)} inventory elements, {len(doubts)} doubt entries.')
