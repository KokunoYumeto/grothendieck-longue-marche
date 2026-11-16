#!/usr/bin/env python3
"""Independent literal/semantic replay of every actual node-face F2 entry."""
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'finite_even_node_F2.json';d=json.loads(path.read_text())
base=json.loads((P/'actual_full21_Fox.json').read_text());finite=json.loads((P/'finite_even_boundary32.json').read_text())
paired=json.loads((P/'symmetric_paired_fox_data.json').read_text());start=time.monotonic()
for name,h in d['input_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
T=base['retained_word_DAG']+finite['retained_word_DAG_append']+d['retained_word_DAG_append']
R=base['R_word_DAG']+finite['R_word_DAG_append']+d['R_word_DAG_append']
RG=base['common_R_generators']+finite['common_R_generators_append']+d['common_R_generators_append']
G=base['group_elements']+finite['group_elements_append']+d['group_elements_append']
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
def read(nodes,p):
 out=[]
 while p:p,x,n=nodes[p];out.append(x)
 return tuple(out[::-1])
@lru_cache(None)
def tw(i):return read(T,i)
@lru_cache(None)
def rw(i):return tuple((1 if x>0 else -1,(tw(RG[abs(x)][0]),RG[abs(x)][1])) for x in read(R,i))
@lru_cache(None)
def group(i):
 a,b,t=G[i];return rw(a),rw(b),tw(t)
beta={1:-1,2:4,3:5,4:2,5:3}
def bet(t):return tuple((1 if x>0 else -1)*beta[abs(x)] for x in t)
def shift(t,w):return tuple((s,(red((*t,*h)),i)) for s,(h,i) in w)
def mult(g,h):
 a,b,t=g;x,y,s=h
 return rr((*a,*shift(t,x))),rr((*b,*shift(bet(t),y))),red((*t,*s))
def fg(g):
 a,b,t=g;return b,a,bet(t)
ret={j:i+1 for i,j in enumerate(base['retained_paired_indices'])};one=((),(),())
def step(g,x):
 a,b,t=g;j=abs(x);s=1 if x>0 else -1
 if j in ret:return a,b,red((*t,s*ret[j]))
 if j<12:return rr((*a,(s,(t,j)))),b,t
 return a,rr((*b,(s,(bet(t),j-10)))),t
def add(d,k,n):
 d[k]+=n
 if not d[k]:del d[k]
def fox(w):
 c=defaultdict(int);g=one
 for x in w:
  h=step(g,x);add(c,(abs(x),g if x>0 else h),1 if x>0 else -1);g=h
 return dict(c),g
F={int(k):tuple(v) for k,v in paired['paired_involution'].items()}
def fw(w):return red(y for x in w for y in (F[abs(x)] if x>0 else inv(F[-x])))
def peel(w):
 while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
 return w
raw={(n['loop_index'],n['local_node_index']):n for n in paired['node_columns']}
phys={(n['loop_index'],frozenset(n['physical_labels'])):n for n in raw.values()}
def physical(i):return i+8 if i<11 else i-8
records={(r['sheet'],tuple(r['node_index'])):r for r in d['records']}
checks=[]
for key,r in records.items():
 sheet,ix=key;face=finite['faces'][r['face_index']];mate=finite['faces'][r['mate_face_index']]
 assert face['sheet']==mate['sheet']==sheet and tuple(face['node_index'])==ix
 expected=phys[ix[0],frozenset(physical(i) for i in raw[ix]['physical_labels'])]
 mi=(expected['loop_index'],expected['local_node_index'])
 assert tuple(mate['node_index'])==tuple(r['mate_index'])==mi
 en=1 if raw[ix]['physical_labels'][0]<11 else -1
 em=1 if expected['physical_labels'][0]<11 else -1
 assert r['A_first_orientation_signs']==[en,em] and r['raw_cell_sign']==-en*em
 sign=r['raw_cell_sign'];w=tuple(face['literal_F21_word']);v=tuple(mate['literal_F21_word']);h=tuple(r['literal_F21_conjugator'])
 assert fw(w)==red((*h,*(v if sign==1 else inv(v)),*inv(h)))
 core=peel(v)
 assert core and all(core!=core[:k]*(len(core)//k) for k in range(1,len(core)) if len(core)%k==0)
 fc,end=fox(fw(w));mc,mend=fox(v);hc,hg=fox(h)
 assert end==mend==one and group(r['coefficient_G_id'])==hg
 got={(j,group(g)):n for j,g,n in r['F_boundary21']}
 assert len(got)==len(r['F_boundary21']) and got==fc
 rhs=defaultdict(int)
 for (j,g),n in mc.items():add(rhs,(j,mult(hg,g)),sign*n)
 assert fc==dict(rhs)
 mr=records[sheet,mi];mh=tuple(mr['literal_F21_conjugator'])
 double=red((*fw(h),*mh));assert double==tuple(r['double_F_conjugator_F21'])
 assert fox(double)[1]==one and mult(fg(hg),group(mr['coefficient_G_id']))==one
 assert red((*double,*w,*inv(double)))==w
 checks.append({'sheet':sheet,'node_index':ix,'mate_index':mi,'raw_sign':sign,
                'literal_word_and_nonpower':True,'entire_full_boundary':True,'double_F_G_identity':True})
assert len(checks)==128
out={'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'method':'Independent semantic (retained head,slot) free-word coefficients; every physical mate recomputed from the actual labels.',
 'checks':checks,'counts':d['counts'],
 'geometric_scope':'Actual same-q whisker/local torus provenance separately proved. Literal conjugator uniqueness in G follows from the verified non-power centralizer; no arbitrary boundary lift.',
 'elapsed_seconds':time.monotonic()-start}
(H/'finite_node_F2_independent_review20.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all128 physical mates/raw signs, exact free words, non-power tests, entire21 boundaries and double-F coefficients')
print('COUNTS',d['counts'],'elapsed',round(out['elapsed_seconds'],3))
