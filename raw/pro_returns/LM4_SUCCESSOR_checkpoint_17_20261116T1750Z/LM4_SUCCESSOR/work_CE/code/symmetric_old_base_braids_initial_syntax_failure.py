#!/usr/bin/env python3
"""The six retained q-base actions in the validated symmetric fiber marking.
Includes exact discriminant and pairwise divisor checks, with pole signs.
These actions transport the64 local columns; they are not additional
filled relations and no infinite relation-module computation is asserted.
"""
from pathlib import Path
import json,time,hashlib
import symmetric_node_braid as B
S,Q,I=B.S,B.Q,B.I
P=B.OUT;started=time.monotonic()
crit=json.loads((B.DE/'symmetric_critical_deformation.json').read_text())
disc=json.loads((P/'symmetric_old_discriminant_orders.json').read_text())
nodes=json.loads((P/'symmetric_node_words.json').read_text())
centers=[(d,Q(d['center'][0])+I*Q(d['center'][1])) for d in crit['centers']]
olds=[x for x in centers if x[0]['kind']=='old']
base=Q(1,100);hub=base+I*Q(13,1000);h=Q(1,1000)
plans=[]
for idx,(d,c) in enumerate(olds):
 corners=B.square_corners(c,h,hub);segments=list(zip([hub]+corners,corners))
 margins=[]
 for a,b in [(base,hub)]+segments:
  assert S.re(a)**2+S.im(a)**2<25 and S.re(b)**2+S.im(b)**2<25
  for e,v in centers:
   dd=B.dist2_segment(v,a,b)
   limit=Q(1,5000)**2 if e['kind']=='old' else Q(1,20000)**2
   assert dd>limit,('old-path critical margin',idx,e.get('name',e.get('key')),dd)
   margins.append(dd)
 plans.append({'index':idx,'name':d['name'],'center':d['center'],
  'corners':[[str(S.re(x)),str(S.im(x))] for x in corners],
  'minimum_all_center_distance_squared':str(min(margins))})
(P/'symmetric_old_base_path_plan.json').write_text(json.dumps({'base':['1/100','0'],
 'hub':['1/100','13/1000'],'square_halfside':'1/1000','plans':plans,
 'old_pole_margin_strictly_greater_than':'1/5000','max_abs_q_strictly_less_than':'5'},indent=2)+'\n')
print('PASS all six old-lasso path margins and isolated clusters.',flush=True)
cache={}
def segment(a,b):
 if (a,b) not in cache:
  rec=B.Segment(a,b).compute();cache[(a,b)]=rec
  print('segment',len(cache),'crossings',rec['crossing_count'],'elapsed',round(time.monotonic()-started,3),flush=True)
 return cache[(a,b)]
trunk=segment(base,hub);initial=trunk['initial_order'];assert initial==nodes['initial_order']
rows=[]
for idx,((d,c),orders) in enumerate(zip(olds,disc['rows'])):
 corners=B.square_corners(c,h,hub)
 records=[segment(a,b) for a,b in zip([hub]+corners,corners)]
 W=B.rmul(trunk['word'],records[0]['word'])
 local=B.rmul(*(r['word'] for r in records[1:]))
 beta=B.rmul(W,local,B.rinv(W))
 exponent=sum(1 if x>0 else -1 for x in beta)
 assert exponent==orders['discriminant_order'],('wrong discriminant exponent',idx,exponent,orders['discriminant_order'])
 perm=list(initial);link={}
 for g in beta:
  j=abs(g)-1;key=tuple(sorted(perm[j:j+2]));link[key]=link.get(key,0)+(1 if g>0 else -1)
  perm[j],perm[j+1]=perm[j+1],perm[j]
 expected=list(initial)
 if idx==0:expected=[20 if x==19 else19 if x==20 else x for x in initial]
 assert perm==expected,('wrong physical peripheral permutation',idx,perm,expected)
 for v in orders['rational_pair_orders']:
  assert link.get(tuple(v['labels']),0)==2*v['difference_order'],('rational pair order mismatch',idx,v)
 for i,o in enumerate(orders['rational_against_two_roots_orders']):
  assert link.get((i,19),0)+link.get((i,20),0)==2*o,('rational/root divisor mismatch',idx,i,o)
 assert link.get((19,20),0)==orders['square_root_pair_discriminant_order']
 A=B.art(beta);Ai=B.art(B.rinv(beta))
 for j in range(1,22):assert B.sub(A[j],Ai)==(j,)==B.sub(Ai[j],A)
 assert B.sub(tuple(range(1,22)),A)==tuple(range(1,22))
 rows.append({'index':idx,'name':d['name'],'center':d['center'],'word':beta,
  'forward_segments':records,'exponent':exponent,'physical_permutation':perm,
  'images':A,'inverse_images':Ai,
  'pair_crossing_sums':[{'labels':list(k),'sum':v} for k,v in sorted(link.items()) if v]})
 out={'scope':__doc__,'initial_order':initial,'labels':B.LABELS,
  'common_trunk':trunk,'loops':rows,'path_plan':plans,
  'far_basepoint':'projected coordinate 10^6; identical initial outer-half-plane marking to the nodal basepoint',
  'finite_puncture_bound':'|v|<75000 from |q|<5 and old-pole margin>1/5000',
  'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'crossing_engine_sha256':hashlib.sha256(Path(B.__file__).read_bytes()).hexdigest(),
  'elapsed_seconds':round(time.monotonic()-started,6)}
 (P/'symmetric_old_base_braids.partial.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('OLD LOOP',idx,d['name'],'PASS length',len(beta),'exponent',exponent,flush=True)
(P/'symmetric_old_base_braids.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
compact={k:v for k,v in out.items() if k not in ('common_trunk','loops')}
compact['common_trunk_word']=trunk['word']
compact['loops']=[{k:v for k,v in r.items() if k!='forward_segments'} for r in rows]
(P/'symmetric_old_base_words.json').write_text(json.dumps(compact,indent=2)+'\n')
print('PASS all six retained-base actions; elapsed',round(time.monotonic()-started,3),flush=True)
