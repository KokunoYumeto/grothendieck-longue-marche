from pathlib import Path
import sys,json,csv
sys.path.insert(0,str(Path(__file__).parent))
from record import ROOT,PREFIX,rebuild,log,now

def audit(scan,replacements=(),note='',extra=()):
    p=ROOT/'pages'/f'{PREFIX}_137_scan{scan:03d}.tex'
    s=p.read_text()
    for old,new in replacements:
        if old not in s: raise ValueError(f'Scan {scan}: old text not found: {old!r}')
        s=s.replace(old,new)
    if replacements:p.write_text(s)
    if extra:
        f=ROOT/(PREFIX+'_inventory.csv')
        with f.open(newline='') as h:r=list(csv.DictReader(h))
        sheet=next(x['sheet_kind'] for x in r if int(x['scan'])==scan)
        for item in extra:
            kind,pos,opening=item[:3]
            row=dict(cote='137',scan=f'{scan:03d}',sheet_kind=sheet,element='',kind=kind,position=pos,first_words_or_objects=opening,transcribed='yes')
            if len(item)>3:
                at=next(i for i,x in enumerate(r) if int(x['scan'])==scan and x['first_words_or_objects']==item[3])
                r.insert(at+1,row)
            else:r.append(row)
        r.sort(key=lambda x:int(x['scan']))
        counts={}
        for x in r:
            n=x['scan'];counts[n]=counts.get(n,0)+1;x['element']=f'{n}-{counts[n]:02d}'
        with f.open('w',newline='') as h:
            w=csv.DictWriter(h,fieldnames=r[0].keys());w.writeheader();w.writerows(r)
    with (ROOT/'support/audit_actions.jsonl').open('a') as h:h.write(json.dumps(dict(scan=scan,time=now(),replacements=replacements,note=note,extra=extra),ensure_ascii=False)+'\n')
    rebuild();log(f'scan {scan:03d} audited')
    print(f'Audited {scan:03d}; {len(replacements)} explicit replacements; {len(extra)} inventory additions.')
