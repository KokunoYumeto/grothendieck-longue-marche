"""Bookkeeping for amendments decided by the primary reader during visual audit."""
from workflow import *
def amend(cote,scan,text,changes=(),insert_inventory=(),new_doubts=()):
    p=WORK/'pages'/f'{cote}_scan{scan}.tex'
    assert p.exists()
    p.write_text(text.rstrip()+'\n')
    cr=[];hr=[]
    for r0 in changes:
        r=dict(r0);r.update(cote=cote,scan=scan)
        r['scan_shows']='Second visual reading: '+r['scan_shows']
        cr.append({k:r.get(k,'') for k in HEADERS['changes_records.tsv']})
        if r['against_H']=='yes':
            hr.append(dict(zip(HEADERS[PREFIX+'_collation.tsv'],[cote,str(int(scan)-1),scan,r['place'],r['H'],r['C'],r['final'],r['scan_shows']+' Crop: '+r['crop'],r['kind'],r.get('marked_in_H','no'),r['confidence']])))
    add('changes_records.tsv',cr);add(PREFIX+'_collation.tsv',hr)
    rank={x:i for i,x in enumerate(ORDER)}
    for fn,c,s in [('changes_records.tsv','cote','scan'),(PREFIX+'_collation.tsv','folder','our_scan')]:
        write_rows(fn,sorted(readrows(fn),key=lambda r:rank[(r[c],r[s])]))
    name=PREFIX+'_inventory.csv';allrows=readrows(name)
    rows=[r for r in allrows if r['scan']==cote+'/'+scan]
    for after,r in sorted(insert_inventory,key=lambda x:x[0],reverse=True):
        r=dict(r);r.update(scan=cote+'/'+scan,element='',transcribed='yes')
        rows.insert(after,r)
    for i,r in enumerate(rows,1):r['element']=str(i)
    allrows=[r for r in allrows if r['scan']!=cote+'/'+scan]+rows
    write_rows(name,sorted(allrows,key=lambda r:rank[tuple(r['scan'].split('/'))]))
    add('remaining_doubts.tsv',list(new_doubts))
    log(f'second-reading amendment {cote}/{scan} {now()}: {len(changes)} difference rows; {len(insert_inventory)} inventory additions')
    rebuild()
