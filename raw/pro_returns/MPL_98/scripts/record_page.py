#!/usr/bin/env python3
"""Record a manually read page, its inventory, and explicit palaeographic doubts.
No OCR or image recognition is performed by this script.
Input JSON is supplied on stdin after visual comparison by the transcriber.
"""
import csv, datetime, json, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parents[1]
def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

data=json.load(sys.stdin)
n=data['scan']
path=BASE/'pages'/f'MPL_98_98_scan{n:03d}.tex'
if path.exists():
    raise SystemExit('Page exists; revise explicitly before freeze, do not overwrite silently.')
path.write_text(data['tex'].rstrip()+'\n',encoding='utf8')
with (BASE/'MPL_98_inventory.csv').open('a',encoding='utf8',newline='') as f:
    w=csv.writer(f)
    for k,row in enumerate(data['elements'],1):
        w.writerow(['98',n,data.get('sheet_kind','text'),k,*row,'yes'])
ledger=BASE/'research'/'page_records.jsonl'
with ledger.open('a',encoding='utf8') as f:
    f.write(json.dumps(data,ensure_ascii=False)+'\n')
with (BASE/'progress.log').open('a',encoding='utf8') as f:
    f.write(f'98 scan {n:03d} done {now()}\n')
print(f'Recorded scan {n:03d}: {len(data["elements"])} inventory elements.')
