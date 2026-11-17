#!/usr/bin/env python3
"""Actual B100 cube sphere in the finite359-face model, with its F mate."""
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'actual_full21_Fox.json',P/'finite_even_boundary32.json',P/'finite_even_node_F2.json',P/'symmetric_full_source_data.json']
D,C,FN,source=[json.loads(p.read_text()) for p in paths];start=time.monotonic()
T=D['retained_word_DAG']+C['retained_word_DAG_append']+FN['retained_word_DAG_append']
R=D['R_word_DAG']+C['R_word_DAG_append']+FN['R_word_DAG_append']
RG=D['common_R_generators']+C['common_R_generators_append']+FN['common_R_generators_append']
GG=D['group_elements']+C['group_elements_append']+FN['group_elements_append']
retindices=(1,4,9,14,19);ret={x:i+1 for i,x in enumerate(retindices)}
beta={1:-1,2:4,3:5,4:2,5:3}
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def rr(w):
 a=[]
 for s,x in w:
  if a and a[-1]==(-s,x):a.pop()
  else:a.append((s,x))
 return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def bet(t):return tuple((1 if x>0 else -1)*beta[abs(x)] for x in t)
def read(nodes,p):
 out=[]
 while p:p,x,n=nodes[p];out.append(x)
 return tuple(out[::-1])
@lru_cache(None)
def rt(p):return read(T,p)
@lru_cache(None)
def rw(p):return tuple((1 if x>0 else -1,(rt(RG[abs(x)][0]),RG[abs(x)][1])) for x in read(R,p))
@lru_cache(None)
def dg(g):
 a,b,t=GG[g];return rw(a),rw(b),rt(t)
one=((),(),())
def step(g,x):
 a,b,t=g;j=abs(x);s=1 if x>0 else -1
 if j in ret:return a,b,red((*t,s*ret[j]))
 if j<12:return rr((*a,(s,(t,j)))),b,t
 return a,rr((*b,(s,(bet(t),j-10)))),t
def evaluate(w):
 g=one
 for x in w:g=step(g,x)
 return g
def shift(t,w):return tuple((s,(red((*t,*h)),i)) for s,(h,i) in w)
def gm(g,h):
 a,b,t=g;x,y,s=h
 return rr((*a,*shift(t,x))),rr((*b,*shift(bet(t),y))),red((*t,*s))
def fg(g):
 a,b,t=g;return b,a,bet(t)
def t_lift(t):return tuple((1 if x>0 else -1)*retindices[abs(x)-1] for x in t)
def lift(g):
 a,b,t=g;w=[]
 for family,r in [(0,a),(10,b)]:
  for s,(head,i) in r:
   h=t_lift(head if family==0 else bet(head));w.extend((*h,s*(i+family),*inv(h)))
 w.extend(t_lift(t));return red(w)
old=next(m for m in D['matrices'] if m['family']=='source' and m['name']=='old_0' and m['direction']=='push')
def sub(w,A):return red(y for x in w for y in(A[abs(x)-1] if x>0 else inv(tuple(A[-x-1]))))
@lru_cache(None)
def psi(g,n):
 assert n in (0,1,2)
 if n==0:return g
 return psi(evaluate(sub(lift(g),old['literal_F21_images'])),n-1)
def pm(x,y):
 g,n=x;h,m=y;return gm(g,psi(h,n)),n+m
def pf(x):return fg(x[0]),x[1]
def add(c,k,n):
 c[k]+=n
 if not c[k]:del c[k]
def terms(face):return {(row,(dg(g),sw)):n for row,g,sw,n in C['faces'][face]['boundary32']}
src={(f['source_index'],f['paired_generator']):i for i,f in enumerate(C['faces']) if f['type']=='source_rectangle'}
nodes={(f['sheet'],tuple(f['node_index'])):i for i,f in enumerate(C['faces']) if f['type']=='node'}
node=nodes[0,(6,3)];mate=nodes[0,(6,7)]
assert C['source_generators'][0]['name']=='old_0' and C['source_generators'][0]['far_base_word']==[1]
s0=next(x for x in source['old_source_generators'] if x['name']=='old_0')
assert s0['h_paired']==s0['k_paired']==[]
for j in [2,3,12,13]:assert old['literal_F21_images'][j-1]==[j]
a=evaluate((2,));q=evaluate((12,));b=evaluate((12,13,-12))
assert gm(a,b)==gm(b,a) and all(psi(g,1)==g for g in [a,q,b])
assert C['faces'][node]['literal_F21_word']==[2,12,13,-12,-2,12,-13,-12]
z=defaultdict(int)
add(z,(node,(one,1)),1);add(z,(node,(one,0)),-1)
# -(a-1)*((1-b)c_(u,p12)+q*c_(u,p13))+(b-1)c_(u,p2).
for ga,na in [(a,-1),(one,1)]:
 for gb,nb in [(one,1),(b,-1)]:add(z,(src[1,12],(gm(ga,gb),0)),na*nb)
 add(z,(src[1,13],(gm(ga,q),0)),na)
add(z,(src[1,2],(b,0)),1);add(z,(src[1,2],(one,0)),-1)
z=dict(z)
def d2(c):
 out=defaultdict(int)
 for (face,h),n in c.items():
  for (row,g),m in terms(face).items():
   assert g[1] in (0,1)
   add(out,(row,pm(h,g)),n*m)
 return dict(out)
assert not d2(z)
FM={r['face_index']:(r['mate_face_index'],dg(r['coefficient_G_id']),r['raw_cell_sign']) for r in FN['records']}
for r in C['source_face_F']:
 FM[src[r['source_index'],r['paired_generator']]]=(src[r['source_index'],r['target_paired_generator']],dg(r['coefficient_G_id']),r['sign'])
def F2(c):
 out=defaultdict(int)
 for (face,g),n in c.items():
  target,h,s=FM[face];add(out,(target,pm(pf(g),(h,0))),n*s)
 return dict(out)
fz=F2(z);assert not d2(fz) and F2(fz)==z
nr=next(r for r in FN['records'] if r['sheet']==0 and r['node_index']==[6,3])
h=tuple(nr['literal_F21_conjugator'])
assert h==(12,-14,-12) and nr['raw_cell_sign']==1 and nr['mate_index']==[6,7]
Fword=next(m for m in D['matrices'] if m['family']=='involution')['literal_F21_images']
assert sub(C['faces'][node]['literal_F21_word'],Fword)==red((*h,*C['faces'][mate]['literal_F21_word'],*inv(h)))
assert {i for (i,g) in z if C['faces'][i]['type']=='node'}=={node}
assert {i for (i,g) in fz if C['faces'][i]['type']=='node'}=={mate}
def enc(c):return [{'face_index':i,'G_lift_F21':lift(g),'u_power':n,'coefficient':v} for (i,(g,n)),v in sorted(c.items(),key=repr)]
out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'u_convention':'u=t^-1; t is literally source old_0, with empty actual fiber correction',
 'geometric_nullhomotopies':'The actual node face and the actual old0 mapping-cylinder word homotopies.',
 'a':[2],'b':[12,13,-12],'q':[12],'node_face':node,'mate_face':mate,
 'z':enc(z),'Fz':enc(fz),'both_complete_D2_zero':True,'F2_Fz_equals_z':True,
 'actual_node_F_conjugator':h,'actual_node_F_sign':1,
 'private_node_rows':[[6,3],[6,7]],
 'rank_proof':'Each private coefficient is u-1 up to a right group unit. u has infinite order by the old-base free quotient; finite support proves right multiplication by u-1 injective over the integral group ring, without a domain hypothesis.',
 'scope':'Actual nonzero spherical elements of Z2; free Lambda rank2 with F exchanging the chosen basis. Its own Tate groups vanish, with no claim on the rest of Z2 or kappa.',
 'elapsed_seconds':time.monotonic()-start}
(H/'actual_cube_sphere20.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual source t, node disk and cylinder words; full359-row z and Fz boundaries zero')
print('PASS F2(Fz)=z; distinct private node rows, literal h=[12,-14,-12]')
print('TERMS',len(z),len(fz),'elapsed',round(out['elapsed_seconds'],3))
