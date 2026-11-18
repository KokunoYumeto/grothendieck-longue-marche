"""Append one personally read page's inventory and reading record; no OCR."""
from pathlib import Path
import csv, datetime, re
ROOT=Path(__file__).resolve().parents[1]
def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(scan, elements, sheet='text', remarks=''):
    p=ROOT/'pages'/f'MPL_57_133-179_57_scan{scan:03}.tex'
    assert p.exists() and f'\\scanpage{{{scan}}}' in p.read_text()
    with (ROOT/'MPL_57_133-179_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,words) in enumerate(elements,1):
            w.writerow([57,scan,sheet,f'{scan}.{i:02}',kind,position,words,'yes'])
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'57 scan {scan:03} done {now()}\n')
    if remarks:
        with (ROOT/'documentation'/'reading_record.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{remarks}\n')
