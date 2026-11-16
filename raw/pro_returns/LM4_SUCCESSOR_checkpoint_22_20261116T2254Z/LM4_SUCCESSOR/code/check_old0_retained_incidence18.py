#!/usr/bin/env python3
"""Exact retained-deck incidence overlap for the single actual old0 translate.

This compares full E augmentations, not full column equality. A collision
is classified against the already checked free-word conjugacy certificate;
no augmented equality is promoted to a full relation.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
paths=[ROOT/'work_A/intrinsic_old0_128_columns.json',ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',ROOT/'work_A/old_zero_node_orbit_identities.json']
raw=[p.read_bytes() for p in paths];D,P,W=[json.loads(b) for b in raw]
def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
beta={int(i):tuple(w) for i,w in P['retained_involution'].items()}
def F(w):return red(y for x in w for y in (beta[x] if x>0 else inv(beta[-x])))
meta={int(i):r for i,r in D['common_R_basis'].items()}
started=time.monotonic();aug=[]
for col in D['node_columns']:
 a=defaultdict(int)
 for t in col['fox_cells']:a[t['A_generator'],t['B_generator']]+=int(t['coefficient'])
 a={k:n for k,n in a.items() if n};assert len(a)==1
 (i,j),sign=next(iter(a.items()));assert abs(sign)==1
 ma,mb=meta[i],meta[j];g,h=tuple(ma['retained_word']),tuple(mb['retained_word'])
 row=(ma['paired_slot'],mb['paired_slot'],red(inv(F(g))+h))
 aug.append((row,g,sign))
assert len(aug)==128 and len({r[0] for r in aug[:64]})==64
cert={(r['loop_index'],r['local_node_index']):r for r in W['rows']}
rows=[];collisions=[]
for k in range(64):
 row,g,s=aug[k];row2,g2,s2=aug[k+64]
 label=P['node_columns'][k]['loop_index'],P['node_columns'][k]['local_node_index']
 assert row[:2]==row2[:2]
 same=row==row2;wit=cert[label]
 r={'node_index':label,'seed_row':row,'old0_row':row2,
   'same_retained_deck_incidence_orbit':same,'seed_unit':{'F5_word':g,'sign':s},
   'old0_unit':{'F5_word':g2,'sign':s2},
   'previous_exact_free_conjugacy':wit['conjugate']}
 if same:
  r['required_retained_deck_translate']=red(g2+inv(g));collisions.append(r)
 rows.append(r)
print('Single old0 incidence comparison:64 physical slot pairs; retained-deck collisions',len(collisions),flush=True)
for r in collisions:print('COLLISION',r['node_index'],'full free conjugacy',r['previous_exact_free_conjugacy'],'head',r['required_retained_deck_translate'],flush=True)
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(b).hexdigest() for p,b in zip(paths,raw)},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'rows':rows,'collision_count':len(collisions),
 'all_collisions_have_prior_full_conjugacy':all(r['previous_exact_free_conjugacy'] for r in collisions),
 'elapsed_seconds':time.monotonic()-started,
 'claims_excluded':['augmented collision implies full equality without witness','all old-base translates covered','global kappa vanishing']}
(ROOT/'records/old0_retained_incidence18.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact incidence comparison; seconds',round(out['elapsed_seconds'],4),flush=True)
