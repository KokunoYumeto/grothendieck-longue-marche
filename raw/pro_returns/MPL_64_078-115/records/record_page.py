from pathlib import Path
import csv, re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record_page(scan, text, elements, doubts=(), notation=(), abbreviations=(), sheet_kind='text'):
    path = ROOT/'pages'/f'MPL_64_078-115_64_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError('Page already recorded; make an explicit correction instead.')
    path.write_text(text.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_64_078-115_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        for j,(kind,position,first) in enumerate(elements,1):
            writer.writerow(['64',scan,sheet_kind,f'{scan:03d}-{j:02d}',kind,position,first,'yes'])
    with (ROOT/'MPL_64_078-115_doubts.md').open('a',encoding='utf-8') as f:
        for position,reading,alternative,confidence in doubts:
            vals=[str(x).replace('|',' / ').replace('\n',' ') for x in ['64',scan,position,reading,alternative,confidence]]
            f.write('| '+' | '.join(vals)+' |\n')
    for name,items in [('notation',notation),('abbreviations',abbreviations)]:
        if items:
            with (ROOT/'records'/f'{name}.tsv').open('a',encoding='utf-8') as f:
                for source,latex,note in items:
                    f.write(f'{scan}\t{source}\t{latex}\t{note}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'64 scan {scan:03d} done {utc()}\n')
    print(f'Page {scan:03d} saved; {len(elements)} inventoried elements.')
