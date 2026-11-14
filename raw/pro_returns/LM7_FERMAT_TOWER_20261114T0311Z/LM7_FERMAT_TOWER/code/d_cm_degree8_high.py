#!/usr/bin/env python3
"""An exact Nielsen basis isolates all quadratic degree-eight C1 terms.

Nine N generators retain degree two. The other 88 are explicit Nielsen
products with no degree-two term. Exactly 4708 of their4753 square/commutator
words lie in D5(K), and thus form an abelian correction subgroup moduloD9.
This file tests the actual N-class-two correction rank of that subgroup.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
pairs=[(i,j) for i in range(97) for j in range(i,97)]
pos={p:k for k,p in enumerate(pairs)}
def square_bits(v):
 ix=[i for i in range(97) if (v>>i)&1];z=0
 for k,i in enumerate(ix):
  for j in ix[k:]:z^=1<<pos[i,j]
 return z
def wedge_bits(a,b):
 z=0
 while a:
  bit=a&-a;i=bit.bit_length()-1;bb=b
  while bb:
   bt=bb&-bb;j=bt.bit_length()-1
   if i!=j:z^=1<<pos[tuple(sorted((i,j)))]
   bb^=bt
  a^=bit
 return z
def action_columns(q):
 a=np.zeros_like(R['CN']);a[[R['ixQ'][R['qm'](q,x)] for x in R['Q']]]=R['CN']
 M=a[R['chN']]%2
 vv=[sum(int(x)<<i for i,x in enumerate(M[:,j])) for j in range(97)]
 return [square_bits(vv[i]) if i==j else wedge_bits(vv[i],vv[j]) for i,j in pairs]
S=action_columns(R['qs']);ST=action_columns(R['qm'](R['qs'],R['qr']))
columns=[(1<<i)^S[i] for i in range(4753)]+[S[i]^ST[i] for i in range(4753)]
ch={j:i for i,j in enumerate(R['chN'])};q=R['one'];v=0
for a in [0,1]*12:
 if a==0:q=R['qm'](q,R['qs'])
 else:
  qq=R['qm'](q,R['qr'])
  for j in (R['ixQ'][q],R['ixQ'][qq]):
   if j in ch:v^=1<<ch[j]
  q=qq
assert q==R['one'];c2=square_bits(v)
T={'pos':pos,'square_bits':square_bits,'columns':columns,'c2':c2,'bas':R['echelon'](columns+[c2])}
relindices=[R['Nwords'].index(w) for w in R['relwords']]
rb=R['echelon'](R['rel']);U=[];words=[];low=[]
for i in relindices:
    U.append(1<<i);words.append(R['Nwords'][i]);low.append(i)
for i,w in enumerate(R['Nwords']):
    if i in relindices:continue
    q,ww=R['collapse'](w);assert q==R['e']
    P=R['poly'](ww,2);assert not P[1].any()
    good,c,rem=R['solve'](R['bitpoly'](P[2]),rb);assert good and not rem
    v=1<<i;cor=[]
    for j,k in enumerate(relindices):
        if (c>>j)&1:v^=1<<k;cor+=R['Nwords'][k]
    nw=w+R['inverse'](cor)
    q,ww=R['collapse'](nw);P=R['poly'](ww,2)
    assert q==R['e'] and not P[1].any() and not P[2].any()
    U.append(v);words.append(nw)
assert len(U)==97 and len(R['echelon'](U))==97
for i in range(9):
    for j in range(i,9):
        a,b=R['rel'][i],R['rel'][j]
        leading=R['mulpoly'](a,a,2) if i==j else R['bracket'](a,2,b,2)
        assert leading
pos=T['pos']
def comm_bits(a,b):
    z=0
    while a:
        aa=a&-a;i=aa.bit_length()-1;bb=b
        while bb:
            bt=bb&-bb;j=bt.bit_length()-1
            if i!=j:z^=1<<pos[tuple(sorted((i,j)))]
            bb^=bt
        a^=aa
    return z
def apply(v,columns):
    z=0
    while v:
        bit=v&-v;z^=columns[bit.bit_length()-1];v^=bit
    return z
cols=[];labels=[]
for i in range(97):
    for j in range(i,97):
        if j<9:continue
        v=T['square_bits'](U[i]) if i==j else comm_bits(U[i],U[j])
        labels.append((i,j));cols.append(v)
assert len(cols)==4708
F=[apply(v,T['columns'][:4753]) for v in cols]+[apply(v,T['columns'][4753:]) for v in cols]
bas=R['echelon'](F)
withmult=R['echelon'](F+[T['c2']])
summary={'adapted_N_basis_rank':97,'degree2_basis_generators':9,
 'remaining_generators_in_D3_K':88,'C1_generators_in_D5_K':4708,
 'omitted_degree4_C1_generators':45,
 'restricted_cusp_map_rank':len(bas),'rank_with_multiplier':len(withmult),
 'full_original_rank_without_multiplier':len(R['echelon'](T['columns'])),
 'full_original_rank_with_multiplier':len(T['bas']),
 'C1_subgroup_abelian_mod_D9':True,
 'scope':'Exact subgroup and rank only; no degree-eight replacement is asserted.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_high.json').write_text(json.dumps({'summary':summary,
 'basis_old_N_homology_masks':[hex(v) for v in U],
 'actual_Nielsen_basis_B_words':words,'high_C1_pairs':labels},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
