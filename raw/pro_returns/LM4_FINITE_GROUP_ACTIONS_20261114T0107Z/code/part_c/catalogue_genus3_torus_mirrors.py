#!/usr/bin/env python3
"""All mixed genus-three actions with annulus or Mobius quotient.
Exact oriented index-two extensions plus NEC generating vectors;
source fusion by boundary rotations, core point pushes, interior braids,
annulus boundary interchange and global reversal, or Mobius slides.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
from collections import Counter
import json,csv,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from genus3_small_extensions import extensions,ROOT,Group
from catalogue_genus3_reflection_quotients import braid,braid_generators

def flatten(kind,state):
 x,q,refs=state
 return tuple(x)+(q,)+tuple(r for block in refs for r in block)

def unpack(kind,vec,l,ks):
 x=tuple(vec[:l]);q=vec[l];refs=[];i=l+1
 for k in ks:
  nr=max(1,k);refs.append(tuple(vec[i:i+nr]));i+=nr
 assert i==len(vec)
 return x,q,tuple(refs)

def boundaries(G,kind,x,q):
 X=G.prod(x)
 if kind=='annulus':return (q,G.inv[G.mul[X][q]])
 return (G.mul[G.inv[X]][G.inv[G.mul[q][q]]],)

def rotate_refs(G,rs,k,e):
 if k:return rs[1:]+(G.conj(e,rs[0]),)
 return rs

def reverse_refs(G,rs,k,e):
 if not k:return rs
 return (G.conj(e,rs[0]),)+tuple(reversed(rs[1:]))

def neighbours(G,kind,state,m,ks):
 x,q,rs=state;l=len(x);es=boundaries(G,kind,x,q)
 for word in braid_generators((m,)*l):
  xx=x;dec=(m,)*l
  for i,s in word:xx,dec=braid(G,xx,dec,i,s)
  yield xx,q,rs
 for j,k in enumerate(ks):
  if k:
   rr=list(rs);rr[j]=rotate_refs(G,rs[j],k,es[j]);yield x,q,tuple(rr)
 if kind=='annulus':
  if l:
   a=x[-1];e=q
   xx=x[:-1]+(G.conj(G.mul[a][e],a),)
   qq=G.conj(a,e)
   rr=(tuple(G.conj(a,r) for r in rs[0]),rs[1])
   yield xx,qq,rr
  if ks[0]==ks[1]:
   qq=G.conj(q,es[1])
   rr=(tuple(G.conj(q,r) for r in rs[1]),rs[0])
   yield x,qq,rr
  # Reflection of the planar fundamental region; every boundary is reversed.
  p=G.one;xx=[]
  for a in x:xx.append(G.conj(p,G.inv[a]));p=G.mul[p][a]
  qq=G.conj(p,G.inv[q])
  rr=[]
  for j in range(2):
   rr.append(tuple(G.conj(p,r) for r in reverse_refs(G,rs[j],ks[j],es[j])))
   p=G.mul[p][es[j]]
  yield tuple(xx),qq,tuple(rr)
 else:
  if l:
   a=x[-1];d=q
   aa=G.conj(G.mul[a][d],G.inv[a])
   dd=G.mul[a][d]
   transport=G.mul[G.inv[aa]][a]
   rr=(tuple(G.conj(transport,r) for r in rs[0]),)
   yield x[:-1]+(aa,),dd,rr
  X=G.prod(x)
  rr=(tuple(G.conj(X,r) for r in reverse_refs(G,rs[0],ks[0],es[0])),)
  yield tuple(G.inv[a] for a in reversed(x)),G.inv[q],rr

def all_states(G,ori,kind,m,l,ks):
 positive=[q for q in range(G.n) if ori[q]==1]
 negative=[q for q in range(G.n) if ori[q]==-1]
 neginv=[q for q in negative if G.orders[q]==2]
 xp=[q for q in positive if G.orders[q]==m]
 @lru_cache(None)
 def reflection_sequences(k,e):
  if not k:return [(q,) for q in neginv if G.conj(e,q)==q]
  out=[]
  for q in neginv:
   end=G.conj(e,q)
   def rec(part):
    if len(part)==k:
     if G.orders[G.mul[part[-1]][end]]==m:out.append(tuple(part))
     return
    for p in neginv:
     if G.orders[G.mul[part[-1]][p]]==m:rec(part+[p])
   rec([q])
  return out
 for x in product(xp,repeat=l):
  for q in positive if kind=='annulus' else negative:
   es=boundaries(G,kind,x,q)
   for refs in product(*(reflection_sequences(k,e) for k,e in zip(ks,es))):
    state=(x,q,tuple(refs));vec=flatten(kind,state)
    if len(G.subgroup(vec))==G.n:yield state

def main():
 acts=json.loads((ROOT/'research_data/actions-genus3.json').read_text())['actions']
 rows=[];certs=[]
 for ai in (3,5,7,8,12,17,18):
  act=acts[ai-1];ms=act['bd'];assert len(set(ms))==1;m=ms[0];r=len(ms)
  H=Group([tuple(x-1 for x in p) for p in act['autgreps'][0]])
  exts=extensions(H)
  signatures=[]
  for l in range(r//2+1):
   k=r-2*l
   signatures.append(('mobius',l,(k,)))
   for k1 in range(k//2+1):signatures.append(('annulus',l,(k1,k-k1)))
  for kind,l,ks in signatures:
   # Canonical generating-vector keys identify target-group automorphisms exactly.
   states={}
   for ei,ext in enumerate(exts):
    G=ext['group'];ori=ext['orientation']
    for st in all_states(G,ori,kind,m,l,ks):
     key=G.tuple_key(flatten(kind,st))
     if key not in states:states[key]=(ei,st)
   remaining=set(states);orbits=[]
   while remaining:
    first=min(remaining);orb={first};todo=[first]
    for key in todo:
     ei,st=states[key];G=exts[ei]['group']
     for nxt in neighbours(G,kind,st,m,ks):
      kk=G.tuple_key(flatten(kind,nxt))
      assert kk in states,(ai,kind,m,l,ks,ei,st,nxt)
      if kk not in orb:orb.add(kk);todo.append(kk)
    assert orb<=remaining;remaining-=orb;orbits.append(sorted(orb))
   print('O3.'+str(ai),kind,'cone',(m,)*l,'corners',ks,'target_normalized',len(states),'classes',len(orbits),flush=True)
   for orb in orbits:
    ei,st=states[orb[0]];ext=exts[ei];G=ext['group'];ori=ext['orientation'];x,q,refs=st
    es=boundaries(G,kind,x,q)
    cid=f'G3T_{len(rows)+1:03}'
    row={'class_id':cid,'positive_action':f'O3.{ai}','order':G.n,'positive_order':H.n,
     'quotient':kind,'cone_orders':','.join([str(m)]*l),
     'corner_counts':','.join(map(str,ks)),'corner_order':m,
     'extension_class':ei,'kernel_orbit_size':len(orb)}
    rec={'class_id':cid,'positive_action':ai,'kind':kind,'cone_orders':[m]*l,
     'corner_lists':[[m]*k for k in ks],
     'group_elements':G.el,'orientation':ori,'identity_id':G.one,
     'generator_vector':flatten(kind,st),'interior_cone_generators':x,
     'boundary_elements':es,'reflection_cycles':refs,
     'crosscap_generator':q if kind=='mobius' else None,
     'extension_class':ei,'extension_alpha':ext['alpha'],'extension_square':ext['square'],
     'kernel_orbit_keys':orb}
    rows.append(row);certs.append(rec)
 with (HERE/'type_3_0_torus_mirrors_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_torus_mirrors_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
 summary={'scope':'all mixed genus-three actions with annulus or Mobius quotient',
  'classes':len(rows),'by_positive_action':dict(Counter(r['positive_action'] for r in rows)),
  'by_quotient':dict(Counter(r['quotient'] for r in rows)),
  'by_order':dict(sorted(Counter(r['order'] for r in rows).items()))}
 (HERE/'catalogue_genus3_torus_mirrors_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
