#!/usr/bin/env python3
"""Exactly one old-zero translate of the64 actual full node columns.
All old/deck indices stay distinct. No orbit-depth iteration is performed.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_paired_fox_data.json','symmetric_source_node_alignment.json',
       'symmetric_full_source_data.json']
raw={n:(P/n).read_bytes() for n in names}
D,S,T=[json.loads(raw[n]) for n in names]
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
beta=mp(D['retained_involution']);ret=D['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
meta={int(i):dict(r,retained_word=tuple(r['retained_word'])) for i,r in S['common_R_basis'].items()}
idx={(r['retained_word'],r['paired_slot']):i for i,r in meta.items()}
for i,r in D['finite_used_common_R_basis'].items():
    assert meta[int(i)]['retained_word']==tuple(r['retained_word'])
    assert meta[int(i)]['paired_slot']==r['paired_slot']
def bid(g,i):
    if (g,i) not in idx:
        j=max(meta,default=0)+1;idx[g,i]=j;meta[j]={'retained_word':g,'paired_slot':i}
    return idx[g,i]
def rw(w):
    g=();r=[]
    for x in w:
        i=abs(x);sgn=1 if x>0 else -1
        if i in hm:g=red(g+(sgn*hm[i],))
        else:
            a=i<12;n=bid(g if a else sub(g,beta),i if a else i-10)
            r.append(sgn*(2*n-1 if a else 2*n))
    assert not g
    return red(r)
def isA(x):return abs(x)%2==1
def rid(x):return (abs(x)+1)//2
def proj(w,a):return red((1 if x>0 else -1)*rid(x) for x in w if isA(x)==a)
def chain(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x)
        if isA(x):
            aa=red(a+(y,));av=a if y>0 else aa;bp=()
            for z in b:
                bn=red(bp+(z,));bv=bp if z>0 else bn
                add(out,(av,bv,abs(y),abs(z)),-(1 if y>0 else -1)*(1 if z>0 else -1));bp=bn
            a=aa
        else:b=red(b+(y,))
    assert not a and not b
    return dict(out)
def edges(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x);sgn=1 if y>0 else -1
        if isA(x):
            aa=red(a+(y,));add(out,('A',a if y>0 else aa,b,abs(y)),sgn);a=aa
        else:
            bb=red(b+(y,));add(out,('B',a,b if y>0 else bb,abs(y)),sgn);b=bb
    assert not a and not b
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        add(out,('A',a,b,i),n);add(out,('A',a,red(b+(j,)),i),-n)
        add(out,('B',red(a+(i,)),b,j),n);add(out,('B',a,b,j),-n)
    return dict(out)
def enc(c):return [{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':n} for (a,b,i,j),n in sorted(c.items())]
def dec(c):return {(tuple(x['A_vertex']),tuple(x['B_vertex']),x['A_generator'],x['B_generator']):x['coefficient'] for x in c}
A=mp(D['old_actions'][0]['geometric_push_paired']);F=mp(D['paired_involution'])
source0=next(r for r in T['old_source_generators'] if r['name']=='old_0')
assert not source0['h_paired'] and A==mp(source0['source_push_F21'])
assert all(sub(A[j],F)==sub(F[j],A) for j in range(1,22))
rows=[];start=time.monotonic()
for layer in (0,1):
    for row in D['node_columns']:
        r=tuple(row['paired_relator']);w=r if layer==0 else sub(r,A)
        kw=rw(w);c=chain(kw)
        assert boundary(c)==edges(kw)
        if layer==0:assert c==dec(row['fox_cells'])
        fc=chain(rw(sub(w,F)))
        assert fc=={(b,a,j,i):-n for (a,b,i,j),n in c.items()}
        rows.append({'column_label':[layer,row['loop_index'],row['local_node_index']],
                     'old_base_translate':'identity' if layer==0 else 'old0 geometric push',
                     'paired_relator':w,'fox_cells':enc(c),'F_fox_cells':enc(fc),
                     'full_edge_boundary_checked':True})
    print('PASS layer',layer,': all64 full chains, independent boundaries and literal F-images.',flush=True)
seeds=[]
for layer in (0,1):
    for j,row in enumerate(T['source_peripheral_generators']):
        h=tuple(row['positive_source_word_F21']);w=h if layer==0 else sub(h,A)
        kw=rw(w);a,b=proj(kw,True),proj(kw,False);assert a==b
        if layer==0:assert a==tuple(S['source_rows'][j]['actual_source_word_R'])
        seeds.append({'actual_source_word_R':a,'source_seed_index':j+1,'layer':layer,
                      'source_witness':'seed' if layer==0 else 'g_old0^-1 * seed * g_old0',
                      'actual_F21_word':w,'sheet':row['sheet'],'critical_index':row['critical_index']})
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in raw.items()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'node_columns':rows,'common_R_basis':meta,'source_rows':seeds,
     'complete_column_count':128,'complete_source_witness_count':16,
     'elapsed_seconds':time.monotonic()-start,
     'claims_excluded':['higher old0 iterates','full E-span','full orbit module','global kappa vanishing']}
(ROOT/'work_A/intrinsic_old0_128_columns.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact128 columns and16 actual source witnesses; R basis size',len(meta),
      'elapsed',round(out['elapsed_seconds'],6),flush=True)
