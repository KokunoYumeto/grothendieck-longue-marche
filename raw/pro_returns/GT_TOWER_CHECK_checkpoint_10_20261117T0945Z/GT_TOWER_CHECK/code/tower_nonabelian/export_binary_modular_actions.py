#!/usr/bin/env python3
"""Exact modular source actions and97-generator map to all eight target factors."""
from pathlib import Path
import json,time,numpy as np
H=Path(__file__).resolve().parent
src=(H/'build_binary_eight_source.py').read_text()
exec(compile(src.split('V=np.empty',1)[0],str(H/'export_prefix.py'),'exec'),globals())
kt=old['modular_table'];kg=old['modular_generators']
kinv=np.array([np.flatnonzero(row==0)[0] for row in kt])
kch=old['modular_chords'];kci={tuple(v):i for i,v in enumerate(kch)}
paths={0:()};queue=[0]
for q in queue:
 for j,g in enumerate(kg):
  p=int(kt[q,g])
  if p not in paths:paths[p]=paths[q]+(j+1,);queue.append(p)
kwds=[paths[int(q)]+(int(j)+1,)+inverse(paths[int(kt[q,kg[j]])]) for q,j in kch]
def krewrite(w):
 q=0;out=[]
 for a in w:
  if a>0:e=(q,a-1);q=int(kt[q,kg[a-1]]);sgn=1
  else:q=int(kt[q,kinv[kg[-a-1]]]);e=(q,-a-1);sgn=-1
  if e in kci:out.append(sgn*(kci[e]+1))
 return q,out
iiK,jjK=np.triu_indices(97,1)
def keval(w):
 v=np.zeros(97,dtype=np.int16);c=np.zeros(4656,dtype=np.uint8)
 for a in w:
  j=abs(a)-1;u=np.zeros(97,dtype=np.int16);u[j]=1 if a>0 else 3
  c^=(v[jjK]*u[iiK]%2).astype(np.uint8);v=(v+u)%4
 return v,c
acts={};actwords={}
for name,aut,power in [('s',((2,),(1,)),2),('r',((2,),(-2,-1)),3)]:
 vv=[];zz=[];ww=[]
 for w in kwds:
  q,u=krewrite(subst(w,aut));assert q==0
  a,b=keval(u);vv.append(a);zz.append(b);ww.append(u)
  check=w
  for _ in range(power):check=subst(check,aut)
  q,ch=krewrite(check);assert q==0
  assert all(np.array_equal(x,y) for x,y in zip(keval(ch),keval(krewrite(w)[1])))
 acts[name]=(np.array(vv),np.array(zz));actwords[name]=ww
KV=np.empty((97,8,102),dtype=np.int16);KZ=np.empty((97,8,5151),dtype=np.uint8)
for i,w in enumerate(kwds):
 for j,pair in enumerate(pairs):
  v,z=evaluate(schreier(subst(w*3,pair)))
  KV[i,j]=-v%4;KZ[i,j]=z^cross(v,v)
print('PASS standard97 modular source actions and literal eight-target two-primary maps',flush=True)
# Recheck the direct-map identity on every original J generator.
jsrc=np.load(H/'build_binary_eight_source.npz')
for i,w in enumerate(loops):
 q,u=krewrite(w);assert q==0
 v=np.zeros((8,102),dtype=np.int16);z=np.zeros((8,5151),dtype=np.uint8)
 for a in u:
  g=KV[abs(a)-1];h=g if a>0 else -g%4;c=KZ[abs(a)-1].copy()
  if a<0:c^=cross(g,g)
  z^=c;z^=cross(v,h);v=(v+h)%4
 ov=jsrc['source_raw_linear'][i];oz=jsrc['source_raw_central'][i]
 dv=(v-ov)%4;assert not np.any(dv[:,:100]) and not np.any(dv[:,100:]%2)
 dz=z^oz^cross(ov,ov)^cross(v,-ov%4)
 rel=np.concatenate((dv[:,100:]//2,dz),axis=1).astype(np.uint8)
 assert not np.any(reduce_z(rel))
print('PASS all289 literal source-to-target word comparisons in the standard K basis',flush=True)
np.savez_compressed(H/'export_binary_modular_actions.npz',source_s_linear=acts['s'][0],source_s_central=acts['s'][1],
 source_r_linear=acts['r'][0],source_r_central=acts['r'][1],target_raw_linear=KV,target_raw_central=KZ,
 modular_table=kt,modular_generators=kg,modular_chords=kch)
out={'scope':'Actual standard-basis source actions and target maps; no genuine-frame census assertion',
 'standard_modular_words':kwds,'modular_paths':[paths[i] for i in range(96)],
 'source_action_words':actwords,
 'target_map_formula':'k mod gamma3(K)K^4 maps to (iota_i(k^3))^(-1) in the eight target N2 groups',
 'map_reason':'K/J=C3 and the actual common source K/(J intersect gamma3(K)K^4) is C3 times K2; this formula projects to its two-primary factor',
 'all289_source_comparisons_passed':True,'all_assertions_passed':True}
(H/'export_binary_modular_actions.json').write_text(json.dumps(out,indent=2)+'\n')
