from pathlib import Path
import csv,sys
sys.path.insert(0,str(Path(__file__).parent))
from workflow import ROOT,PREFIX,FIELDS,utc
from audit_tools import page

inv=ROOT/f'{PREFIX}_inventory.csv';rows=list(csv.DictReader(inv.open()))
ordering={
 '33-148-25':8.5,'33-150-27':16.5,'33-158-21':4.5,'33-158-22':19.5,
 '33-163-17':15.5,'33-165-13':8.5,'33-167-21':19.5,'33-170-19':12.5,
 '34-006-25':16.5,'34-011-11':5.2,'34-011-12':5.3,'34-015-17':14.5}
for r in rows:r['_order']=ordering.get(r['element'],int(r['element'].rsplit('-',1)[1]))
def add(c,s,kind,pos,words,order):
    group=[r for r in rows if r['cote']==str(c) and int(r['scan'])==s]
    rows.append(dict(cote=str(c),scan=f'{s:03d}',sheet_kind=group[0]['sheet_kind'],element='',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes',_order=order))
for s,num in [(4,'2'),(5,'3'),(6,'4'),(7,'5'),(8,'6'),(10,'9 | 8 (uncertain)'),(11,'9'),(12,'10'),(13,'11'),(14,'12'),(15,'13'),(16,'14')]:
    add(34,s,'text','top right, own page number',num,0.1)
add(33,153,'insertion','first proof display','arrow from F(U) and two superscript stars',11.5)
add(33,153,'insertion','second proof display','arrow from F(U)',14.5)
add(33,153,'insertion','triangle labels','phi and phi prime',19.5)
add(33,158,'deletion','upper line beside xi clause','et eta^0 in R^0 Gamma with empty argument',5.5)
add(33,161,'insertion','end of first paragraph','square brackets around EGA IV, § 10',4.5)
add(34,6,'deletion','lower cancelled block','entire roots-of-unity paragraph and its displays',18.5)
add(34,14,'deletion','within cancelled proof','et I prime t isomorphic I t, nested cancellation',17.5)
add(34,15,'insertion','lower above gap before à coefficients','de K; alternative state to cancellation',14.6)
add(34,16,'deletion','inside abandoned 3.16 paragraph','k prime / k, replaced by I prime',24.5)
add(34,17,'margin note','bottom left','16',99)
p=page(34,17);t=p.read_text();assert r'\margin{16}' not in t;p.write_text(t+'\\margin{16}\n')
rows.sort(key=lambda r:(int(r['cote']),int(r['scan']),r['_order']))
counts={}
with inv.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
    for r in rows:
        k=(r['cote'],r['scan']);counts[k]=counts.get(k,0)+1
        r['element']=f'{k[0]}-{k[1]}-{counts[k]:02d}'
        del r['_order'];w.writerow(r)
with (ROOT/'records/audit_observations.md').open('a') as f:
    f.write('\n## Final inventory and foliation reconciliation\n\nInventory elements added during the second audit were moved to their physical positions within their leaves and element IDs were renumbered. Twelve omitted standalone SGA 7 foliation inventory entries were added (their numbers were already in the page text). Individual proof-arrow and triangle-label insertions on 33/153, EGA brackets on 33/161 and nested cancellation blocks were made explicit. The clearly visible lower-left archive number 16 on 34/017 was added to the page text and inventory before freezing. This last correction changes no mathematical reading.\n')
with (ROOT/'progress.log').open('a') as f:f.write(f'final inventory reconciled: {len(rows)} elements on {len(counts)} leaves {utc()}\n')
print(len(rows),'inventory elements on',len(counts),'pages')
