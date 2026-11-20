"""Manual second-reading support. This script does not inspect images or recognise text."""
import record as r
from pathlib import Path
import csv

def write_rows(name,rows,headers=None):
    if headers is None: headers=list(rows[0])
    with (r.W/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

def begin(n):
    r.N=n
    r.COUNTER=max([int(x['id'].split('-')[-1]) for x in r.read('CHANGES.tsv') if int(x['scan'])==n] or [0])
    return (r.W/f'pages/142_scan{n:03}.tex').read_text()

def log(place,before,after,evidence,confidence='high',view='page, second visual audit'):
    path=r.W/'AUDIT_CHANGES.tsv'
    if not path.exists():r.append(path.name,['scan','place','first_pass','audited_reading','evidence','view','confidence','date'])
    r.append(path.name,[r.N,place,before,after,evidence,view,confidence,r.now()])

def amend(identifier,**updates):
    rows=r.read('CHANGES.tsv')
    found=[x for x in rows if x['id']==identifier]
    assert len(found)==1
    row=found[0];old=row.copy();row.update(updates)
    log(row['place'],old['final'],row['final'],row['scan_shows'],row['confidence'])
    write_rows('CHANGES.tsv',rows)
    rebuild_collation()

def rebuild_collation():
    current=r.read('SP70_C13_142_collation.tsv')
    marked={(x['our_scan'],x['line']):x['marked_in_H'] for x in current}
    headers=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
    rows=[]
    for x in r.read('CHANGES.tsv'):
        if x['against_H']!='yes':continue
        n=int(x['scan'])
        vals=['142',n-1,n,x['place'],x['H'],x['C'],x['final'],x['scan_shows']+'; '+x['crop'],x['kind'],marked.get((str(n),x['place']),'no'),x['confidence']]
        rows.append(dict(zip(headers,vals)))
    write_rows('SP70_C13_142_collation.tsv',rows,headers)

def add(place,c,h,final,ink,**kwargs):
    r.change(place,c,h,final,ink,**kwargs)
    log(place,c,final,ink,kwargs.get('conf','high'))

def finish(t,note='All page elements reread against the image; no further change.'):
    (r.W/f'pages/142_scan{r.N:03}.tex').write_text(t)
    with (r.W/'AUDIT.md').open('a') as f:f.write(f'## Scan {r.N:03}\n\n{note}\n\n')
    with (r.W/'progress.log').open('a') as f:f.write(f'scan {r.N:03} audited {r.now()}\n')
    r.refresh()
