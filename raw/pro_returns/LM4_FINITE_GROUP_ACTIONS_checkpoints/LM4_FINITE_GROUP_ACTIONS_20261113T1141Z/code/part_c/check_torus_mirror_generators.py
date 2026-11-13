#!/usr/bin/env python3
"""Independent comparison with the complete one-cone source-automorphism
lists in Gromadzki--Szepietowski 2016, Lemmas 3.7 and 3.8.
"""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
from catalogue_genus3_torus_mirrors import Group,ROOT,extensions,all_states,flatten,neighbours

def primary(G,kind,st):
 x,q,rs=st;a=x[0]
 if kind=='annulus':
  yield (G.conj(G.inv[q],G.inv[a]),),G.inv[q],rs
  yield (G.conj(G.inv[q],a),),G.inv[G.mul[a][q]],(rs[1],rs[0])
 else:
  yield (G.inv[a],),G.conj(G.inv[a],G.inv[q]),rs
  u=G.inv[G.mul[q][a]]
  yield x,u,(tuple(G.conj(u,r) for r in rs[0]),)

def orbitset(states,exts,kind,m,ks,source):
 left=set(states);result=[]
 while left:
  first=min(left);orb={first};todo=[first]
  for key in todo:
   ei,st=states[key];G=exts[ei]['group']
   for nxt in source(G,kind,st):
    kk=G.tuple_key(flatten(kind,nxt));assert kk in states
    if kk not in orb:orb.add(kk);todo.append(kk)
  assert orb<=left;left-=orb;result.append(sorted(orb))
 return sorted(result)

def main():
 acts=json.loads((ROOT/'research_data/actions-genus3.json').read_text())['actions'];out=[]
 for ai in (3,5,7,8):
  act=acts[ai-1]
  if len(act['bd'])!=2:continue
  H=Group([tuple(x-1 for x in p) for p in act['autgreps'][0]]);exts=extensions(H);m=act['bd'][0]
  for kind in ('annulus','mobius'):
   ks=(0,0) if kind=='annulus' else (0,);states={}
   for ei,ext in enumerate(exts):
    G=ext['group']
    for st in all_states(G,ext['orientation'],kind,m,1,ks):
     key=G.tuple_key(flatten(kind,st));states.setdefault(key,(ei,st))
   p=orbitset(states,exts,kind,m,ks,primary)
   q=orbitset(states,exts,kind,m,ks,lambda G,kind,st:neighbours(G,kind,st,m,ks))
   assert p==q,(ai,kind,len(p),len(q))
   out.append({'positive_action':'O3.'+str(ai),'quotient':kind,'normalized_vectors':len(states),'orbits':len(p),'full_orbit_partitions_equal':True})
 (HERE/'check_torus_mirror_generators_output.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
