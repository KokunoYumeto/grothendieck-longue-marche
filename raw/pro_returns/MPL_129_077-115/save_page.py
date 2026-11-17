"""Save manually read page text and its manually enumerated inventory.

No OCR or image-to-text processing is performed by this helper.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

ROOT = Path(__file__).resolve().parent

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save(scan, tex, elements, sheet_kind='text', doubts=(), notation=(), abbreviations=(), leads=''):
    page = ROOT/'pages'/f'MPL_129_077-115_129_scan{scan:03d}.tex'
    assert not page.exists(), f'Page already saved: {page}'
    assert f'\\scanpage{{{scan}}}' in tex
    page.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_129_077-115_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        for i,(kind,position,first) in enumerate(elements,1):
            writer.writerow(['129',scan,sheet_kind,f'{scan:03d}-{i:02d}',kind,position,first,'yes'])
    record={'scan':scan,'doubts':list(doubts),'notation':list(notation),'abbreviations':list(abbreviations)}
    with (ROOT/'reading_records.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps(record,ensure_ascii=False)+'\n')
    if leads:
        with (ROOT/'working_research_leads.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n{leads}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'129 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(tex)} characters, {len(elements)} inventory elements')

if __name__=='__main__':
    save(**json.load(sys.stdin))
