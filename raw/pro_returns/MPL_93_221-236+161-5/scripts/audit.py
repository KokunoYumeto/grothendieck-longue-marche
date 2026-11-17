from pathlib import Path
import csv,json
from session import BASE,STEM,utc,refresh_doubts

def audit(cote,scan,replacements=(),doubts=(),note='No textual change after whole-page and half-page comparison.',add_elements=()):
    cote=str(cote)
    p=BASE/'pages'/f'{STEM}_{cote}_scan{scan:03d}.tex'
    s=p.read_text(encoding='utf-8')
    for old,new in replacements:
        if old not in s: raise ValueError(f'Exact old text missing on {cote}/{scan}: {old!r}')
        s=s.replace(old,new)
    if replacements:p.write_text(s,encoding='utf-8')
    if doubts:
        with (BASE/'records/doubts.jsonl').open('a',encoding='utf-8') as f:
            for d in doubts:f.write(json.dumps({'cote':cote,'scan':scan,'line':d[0],'reading':d[1],'alternatives':d[2],'confidence':d[3]},ensure_ascii=False)+'\n')
    if add_elements:
        inv=BASE/f'{STEM}_inventory.csv'
        rows=list(csv.DictReader(inv.open(encoding='utf-8')))
        page=[r for r in rows if r['cote']==cote and int(r['scan'])==scan]
        n=len(page)
        with inv.open('a',newline='',encoding='utf-8') as f:
            w=csv.writer(f)
            for i,(kind,pos,first) in enumerate(add_elements,n+1):w.writerow([cote,scan,page[0]['sheet_kind'],f'{cote}-{scan:03d}-{i:02d}',kind,pos,first,'yes'])
    t=utc()
    with (BASE/'records/audit_changes.md').open('a',encoding='utf-8') as f:f.write(f'\n## {cote} scan {scan:03d} — {t}\n\n{note}\n')
    with (BASE/'progress.log').open('a',encoding='utf-8') as f:f.write(f'{cote} scan {scan:03d} audited {t}\n')
    refresh_doubts()
    print(f'{cote} scan {scan:03d} audited {t}')
