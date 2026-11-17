from pathlib import Path
from datetime import datetime,timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, changes=(), doubts=(), elements=(), note='Visual second reading completed by the primary transcriber.'):
    log=ROOT/'progress.log'
    marker=f'scan {scan:03} audited '
    if marker in log.read_text(): raise RuntimeError('Already audited')
    p=ROOT/'pages'/f'MPL_136_002-046_136_scan{scan:03}.tex'
    txt=p.read_text()
    for old,new in changes:
        if old not in txt: raise RuntimeError(f'Missing replacement: {old!r}')
        txt=txt.replace(old,new)
    if changes:p.write_text(txt)
    if doubts:
        with (ROOT/'MPL_136_002-046_doubts.md').open('a') as f:
            for line,reading,alternatives,conf in doubts:
                vals=['136',f'{scan:03}',line,reading,alternatives,conf]
                f.write('| '+' | '.join(str(v).replace('|',' / ').replace('\n',' ') for v in vals)+' |\n')
    if elements:
        inv=ROOT/'MPL_136_002-046_inventory.csv'
        rows=list(csv.DictReader(inv.open()))
        same=[r for r in rows if r['scan']==f'{scan:03}']
        with inv.open('a',newline='') as f:
            w=csv.writer(f)
            for i,(kind,pos,words) in enumerate(elements,len(same)+1):
                w.writerow(['136',f'{scan:03}',same[0]['sheet_kind'],f'{scan:03}-{i:02}',kind,pos,words,'yes'])
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with log.open('a') as f:
        f.write(f'{marker}{now}\n')
        f.write(f'audit detail {scan:03}: {note} Changes: {len(changes)}; additional doubts: {len(doubts)}; additional inventory elements: {len(elements)}.\n')
    print(f'Audited {scan:03}; {len(changes)} targeted corrections.')
