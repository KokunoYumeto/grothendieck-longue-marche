from pathlib import Path
from datetime import datetime,timezone
import csv,json
ROOT=Path(__file__).resolve().parents[1]
def audit(n,replacements=(),doubts=(),notes=(),inventory_add=(),remove_doubts=()):
    p=ROOT/'pages'/f'MPL_57_089-132_57_scan{n:03d}.tex'
    t=p.read_text()
    for old,new in replacements:
        if old not in t: raise ValueError(f'scan {n}: replacement source absent: {old!r}')
        t=t.replace(old,new)
    if replacements:p.write_text(t)
    rp=ROOT/'records'/f'scan{n:03d}.json'
    r=json.loads(rp.read_text())
    r['doubts']=[d for d in r.get('doubts',[]) if d[1] not in remove_doubts]+list(doubts)
    utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    r['audit']={'utc':utc,'replacement_count':len(replacements),'notes':list(notes)}
    rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    if inventory_add:
        cp=ROOT/'MPL_57_089-132_inventory.csv'
        rows=list(csv.DictReader(cp.open()))
        ids=[int(x['element']) for x in rows if int(x['scan'])==n]
        kind_sheet=next(x['sheet_kind'] for x in rows if int(x['scan'])==n)
        with cp.open('a',newline='') as f:
            w=csv.writer(f)
            for i,(kind,pos,incipit) in enumerate(inventory_add,max(ids)+1):w.writerow([57,n,kind_sheet,i,kind,pos,incipit,'yes'])
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {utc}\n')
    print(f'Audited {n:03d}: {len(replacements)} text corrections; {len(doubts)} added doubts.')
