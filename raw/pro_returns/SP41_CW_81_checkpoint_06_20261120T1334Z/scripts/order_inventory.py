"""Put inventory rows in physical top-to-bottom order using recorded coordinates only.

This never reads images or infers a reading. The saved index permutation is a
bijection between the original rows and the reordered rows; every field stays
identical. The multiset of exact row encodings is checked before writing.
"""
from pathlib import Path
import json,re,datetime,hashlib
w=Path(__file__).resolve().parents[1]
def box(pos):
 if isinstance(pos,list):return pos
 if isinstance(pos,dict):return pos['bbox']
 m=re.search(r'\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]',pos)
 if m:return list(map(int,m.groups()))
 m=re.search(r'x\s*(\d+)[–-](\d+)\s*,\s*y\s*(\d+)[–-](\d+)',pos)
 if m:
  x0,x1,y0,y1=map(int,m.groups());return [x0,y0,x1,y1]
 m=re.search(r'y\s*(\d+)[–-](\d+)',pos)
 if m:
  y0,y1=map(int,m.groups());return [None,y0,None,y1]
 raise ValueError('No explicit vertical coordinates in '+str(pos))
def encoded(rows):return sorted(json.dumps(r,ensure_ascii=False,sort_keys=True) for r in rows)
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (w/'pages').glob('*.tex')}
audit=[];prepared=[]
for p in sorted((w/'decisions').glob('scan*.json')):
 d=json.loads(p.read_text());old=d['inventory'];order=sorted(range(len(old)),key=lambda i:(box(old[i]['position'])[1],i))
 assert sorted(order)==list(range(len(old)))
 if order==list(range(len(old))):continue
 new=[old[i] for i in order]
 assert encoded(old)==encoded(new)
 audit.append({'scan':d['scan'],'new_to_old_zero_based':order,'old_to_new_zero_based':[order.index(i) for i in range(len(old))],'rows':len(old),'row_multiset_unchanged':True})
 d['inventory']=new;prepared.append((p,d))
# All positions and exact row permutations are checked before any write.
for p,d in prepared:p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (w/'pages').glob('*.tex')}
assert before==after
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ap=w/'validation/inventory_order_audit.json'
prior=json.loads(ap.read_text()) if ap.exists() else []
if audit:
 prior.append({'utc':now,'permutations':audit,'page_text_hashes_unchanged':True});ap.write_text(json.dumps(prior,ensure_ascii=False,indent=2))
 with (w/'progress.log').open('a') as f:f.write('inventory row order audit '+now+': coordinate-order permutations for scans '+','.join(str(x['scan']) for x in audit)+'; every row field and all page text hashes unchanged.\n')
print(json.dumps({'changed_scans':[x['scan'] for x in audit],'page_text_hashes_unchanged':True}))
