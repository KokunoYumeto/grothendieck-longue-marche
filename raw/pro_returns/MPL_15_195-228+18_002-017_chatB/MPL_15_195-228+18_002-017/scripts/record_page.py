from pathlib import Path
from datetime import datetime, timezone
import csv, json, re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_15_195-228+18_002-017'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save_page(cote,scan,text,elements,sheet_kind='text',observations=''):
    expected=json.loads((ROOT/'records/expected_pages.json').read_text())
    target={'cote':cote,'scan':scan}; idx=expected.index(target)
    for e in expected[:idx]:
        assert (ROOT/'pages'/f'{PREFIX}_{e["cote"]}_scan{e["scan"]:03d}.tex').exists(),e
    p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03d}.tex'
    assert not p.exists(),f'Page already exists: {p}'
    assert f'\\scanpage{{{scan}}}' in text
    if idx==0 or expected[idx-1]['cote']!=cote: assert f'\\cotefile{{{cote}}}' in text
    p.write_text(text.strip()+'\n',encoding='utf-8')
    rows=[]
    for n,(kind,position,first) in enumerate(elements,1):
        rows.append([cote,scan,sheet_kind,n,kind,position,first,'yes'])
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',newline='',encoding='utf-8') as f: csv.writer(f).writerows(rows)
    (ROOT/'records'/f'{cote}_scan{scan:03d}.json').write_text(json.dumps({'cote':cote,'scan':scan,'sheet_kind':sheet_kind,'elements':elements,'observations':observations,'first_read_and_line_review_completed':utc(),'images_inspected':['whole','a','b']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(f'{cote} scan {scan:03d} done {utc()}\n')
    print(f'Saved {cote} scan {scan:03d}: {len(text)} characters; {len(rows)} inventory elements at {utc()}')
