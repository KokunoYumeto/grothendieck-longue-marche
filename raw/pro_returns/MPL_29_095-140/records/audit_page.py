"""Record the root reader's sequential visual audit; never performs OCR."""
import csv
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def replace(scan, old, new):
    for p in [ROOT/'pages'/f'MPL_29_095-140_29_scan{scan:03}.tex', ROOT/'records'/f'page{scan:03}.py']:
        s=p.read_text(encoding='utf-8')
        if old not in s:
            raise ValueError(f'Expected old text absent in {p.name}: {old!r}')
        p.write_text(s.replace(old,new),encoding='utf-8')

def add_doubt(scan, place, reading, alternative, confidence):
    vals=[29,scan,place,reading,alternative,confidence]
    with (ROOT/'MPL_29_095-140_doubts.md').open('a',encoding='utf-8') as f:
        f.write('| '+' | '.join(str(x).replace('|','\\|').replace('\n',' ') for x in vals)+' |\n')
    p=ROOT/'records'/f'{scan:03}.json'
    data=json.loads(p.read_text())
    data['doubts'].append([place,reading,alternative,confidence])
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def add_element(scan,kind,position,first):
    p=ROOT/'records'/f'{scan:03}.json'
    data=json.loads(p.read_text())
    data['elements'].append([kind,position,first])
    n=len(data['elements'])
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'MPL_29_095-140_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow([29,scan,data['sheet_kind'],f'{scan:03}-{n:02}',kind,position,first,'yes'])

def sheet_kind(scan,kind):
    p=ROOT/'records'/f'{scan:03}.json'
    data=json.loads(p.read_text())
    old=data['sheet_kind']
    data['sheet_kind']=kind
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    q=ROOT/'records'/f'page{scan:03}.py'
    s=q.read_text()
    if f"sheet_kind='{old}'" in s:
        q.write_text(s.replace(f"sheet_kind='{old}'",f"sheet_kind='{kind}'"))
    inventory=ROOT/'MPL_29_095-140_inventory.csv'
    with inventory.open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f)); fields=list(rows[0])
    for row in rows:
        if int(row['scan'])==scan: row['sheet_kind']=kind
    with inventory.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fields); w.writeheader(); w.writerows(rows)

def audited(scan,note):
    with (ROOT/'records'/'visual_audit.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## Scan {scan:03}\n\n{note}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03} audited {now()}\n')
    print(f'Visual audit saved: {scan:03}')
