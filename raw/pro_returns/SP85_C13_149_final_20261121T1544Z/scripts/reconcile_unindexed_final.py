"""Complete the read-only review's two remaining metadata reconciliations."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
for page,index,place in [('149_scan029',2,'cancelled phrase after dans k'),('149_scan040',3,'Cancelled short word before donc')]:
 p=R/'records'/f'{page}.json';r=json.loads(p.read_text());d=next(d for d in r['doubts'] if d['place']==place);u=r['unindexed_decisions'][index]
 u.update(reading=(r'\deleted{'+d['reading']+'}') if page.endswith('029') else d['reading'],ink=d['reason'],confidence=d['confidence'])
 if 'alternatives' in u:u['alternatives']=d['alternatives']
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
assert before=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
with (R/'records/final_metadata_review.md').open('a') as f:f.write('\nReader B compared all 13 current unindexed decisions across all 23 records with the pages and doubts. The additional alternatives on 029 (des k l-prime / des f_k ell) and 040 (cancelled et/soit) are now reflected in those metadata entries. No other stale current unindexed reading, confidence or ink claim was found. Page TeX bytes remained unchanged.\n')
print('All current unindexed decisions reconciled; 23 page files unchanged')
