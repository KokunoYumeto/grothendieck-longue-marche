"""Exact finite-permutation checks for research notes; never reads source images.

Conventions: permutations act on the left, composition p*q means p after q;
r = rho_s, s = sigma, t = r^{-1}*s = rho_f, so r*t*s = 1.
Faces are t-cycles, edges s-cycles, vertices r-cycles.  Fixed points of s are
allowed (the manuscript's q=1 half-edges).  All tests use only integer tuples.
"""
from itertools import permutations
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent.parent
def mul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):return tuple(p.index(i) for i in range(len(p)))
def ident(n):return tuple(range(n))
def cyc(p):
 out=[];seen=set()
 for i in range(len(p)):
  if i in seen:continue
  c=[];j=i
  while j not in seen:c.append(j);seen.add(j);j=p[j]
  out.append(tuple(c))
 return out
def typ(p):return tuple(sorted((len(c) for c in cyc(p)),reverse=True))
def conjugate(a,p):return mul(mul(a,p),inv(a))
def regular(partition):
 p=[]
 for length in partition:
  b=len(p);p+=list(range(b+1,b+length))+[b]
 return tuple(p)
def group(gens):
 e=ident(len(gens[0]));ans={e};todo=[e]
 while todo:
  a=todo.pop()
  for g in gens:
   b=mul(g,a)
   if b not in ans:ans.add(b);todo.append(b)
 return ans
def transitive(gens):
 ans={0};todo=[0]
 while todo:
  i=todo.pop()
  for p in gens:
   if p[i] not in ans:ans.add(p[i]);todo.append(p[i])
 return len(ans)==len(gens[0])
def preserves_each_cycle(a,p):
 return all({a[x] for x in c}==set(c) for c in cyc(p))
def info(r,s):
 n=len(r);e=ident(n);t=mul(inv(r),s)
 assert mul(mul(r,t),s)==e and mul(s,s)==e
 sym=list(permutations(range(n)))
 ap=[a for a in sym if mul(a,r)==mul(r,a) and mul(a,s)==mul(s,a)]
 am=[a for a in sym if conjugate(a,r)==inv(r) and conjugate(a,s)==s]
 kernel=[a for a in ap if all(preserves_each_cycle(a,p) for p in (r,s,t))]
 return {'r':r,'s':s,'t':t,'passport':[typ(r),typ(s),typ(t)],
         'transitive':transitive((r,s)),
         'Euler_characteristic':len(cyc(r))+len(cyc(s))+len(cyc(t))-n,
         'monodromy_order':len(group((r,s))),
         'oriented_automorphisms':ap,'orientation_reversing_isomorphisms':am,
         'full_automorphism_order':len(ap)+len(am),'pinning_kernel':kernel}
def passport_classes(p,q,f):
 n=sum(p);r=regular(p);e=ident(n);sym=list(permutations(range(n)))
 central=[a for a in sym if mul(a,r)==mul(r,a)]
 reps={}
 for s in sym:
  if mul(s,s)!=e or typ(s)!=q:continue
  t=mul(inv(r),s)
  if typ(t)!=f or not transitive((r,s)):continue
  key=min(conjugate(a,s) for a in central)
  reps[key]=s
 return [info(r,s) for s in sorted(reps)]
def main():
 frozen=json.loads((ROOT/'records/frozen_hashes.json').read_text())['sha256']
 before={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in frozen}
 assert before==frozen
 torus=info((1,2,3,0),(2,3,0,1))
 assert torus['Euler_characteristic']==0 and len(torus['pinning_kernel'])==2
 assert torus['monodromy_order']==4 and len(torus['oriented_automorphisms'])==4
 star=info((1,2,0),(0,1,2))
 assert star['monodromy_order']==3 and len(star['oriented_automorphisms'])==3
 assert star['full_automorphism_order']==6 and len(star['pinning_kernel'])==1
 loop=info((1,2,0),(1,0,2))
 assert loop['monodromy_order']==6 and len(loop['oriented_automorphisms'])==1
 assert loop['full_automorphism_order']==2
 chiral=passport_classes((4,1),(2,2,1),(4,1))
 assert len(chiral)==2 and all(x['full_automorphism_order']==1 for x in chiral)
 duplicate=passport_classes((6,),(2,2,1,1),(3,2,1))
 # This checks the repeated passport, not the identification of every drawing.
 out={'time':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
      'method':'exhaustive permutations for the specified passports, modulo simultaneous relabelling',
      'index_base':0,'torus':torus,'cubic_star':star,'cubic_loop_tail':loop,
      'degree5_chiral_passport':chiral,'degree6_repeated_passport':duplicate,
      'frozen_sha256':frozen}
 after={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in frozen}
 assert before==after
 out['source_hashes_unchanged']=True
 (ROOT/'records/maps_moduli_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'torus_pinned_kernel':len(torus['pinning_kernel']),
 'star_monodromy_full_aut':[star['monodromy_order'],star['full_automorphism_order']],
 'loop_monodromy_full_aut':[loop['monodromy_order'],loop['full_automorphism_order']],
 'degree5_oriented_classes':len(chiral),
 'degree6_repeated_passport_oriented_classes':len(duplicate),
 'degree6_full_automorphism_orders':[x['full_automorphism_order'] for x in duplicate],
 'source_hashes_unchanged':True},indent=2))
if __name__=='__main__':main()
