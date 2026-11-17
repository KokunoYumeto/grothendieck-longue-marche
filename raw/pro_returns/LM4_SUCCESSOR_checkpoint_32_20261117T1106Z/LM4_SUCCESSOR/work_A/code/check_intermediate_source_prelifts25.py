#!/usr/bin/env python3
"""Exact actual source map from the intermediate boundary amalgam.

The four prefix relations are used ONLY in the explicit final quotient
map. This code does not identify j K j with eta(K) inside M.
"""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
D=json.loads(src.read_text())

def red(w,cones):
    a=[]
    for x in w:
        if abs(x) in cones:x=abs(x)
        if a and (a[-1]==-x or x in cones and a[-1]==x):a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w,cones):return red((-x for x in reversed(w)),cones)
def mul(*ws,cones):return red((x for w in ws for x in w),cones)
def sub(w,A,cones):
    return red((y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x],cones))),cones)

# M uses common K labels1..5, adapted C=6, k=8 and j=10.
# There is no outer K/C/k identification inside M.
Mcones={6,10}
local={int(i):tuple(w) for i,w in D['local_Y_h_maps']['minus'].items()}
a=(1,);j=(10,)
regional=[]
for row in D['actual_six_source_words'][:4]:
    regional.append(mul(a,sub(row['raw_Y_word'],local,Mcones),inv(a,Mcones),cones=Mcones))
regional.append(mul(a,local[7],inv(a,Mcones),cones=Mcones))
prelifts=[mul(j,w,j,cones=Mcones) for w in regional]+[(8,)]

# This evaluation is the final mirror quotient map, where ALL five
# prefix inversion relations give the actual eta action.
eta={int(i):tuple(w) for i,w in D['eta_in_common_K'].items()}
mirror=dict(eta);mirror.update({6:(7,),7:(6,),8:(9,),9:(8,)})
target_cones={6,7}
for i in range(1,10):assert sub(mirror[i],mirror,target_cones)==(i,)
def final_map(w):
    current=();parity=0
    for x in w:
        if abs(x)==10:parity^=1;continue
        step=(x,) if not parity else sub((x,),mirror,target_cones)
        current=mul(current,step,cones=target_cones)
    return current,parity
for w,row in zip(prelifts,D['actual_six_source_words']):
    assert final_map(w)==(tuple(row['word']),0),row['name']

O={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
prefix={};w=()
for i in range(1,6):
    w=mul(w,O[i],cones=Mcones);prefix[i]=w
assert prefix[5]==(1,2,5,3,4)
remaining=[mul(j,prefix[i],j,prefix[i],cones=Mcones) for i in range(1,5)]
for w in remaining:assert final_map(w)==((),0)

# Universal inverse Nielsen change in the carrier F4*D_infinity.
# With abstract j=10, P_i=i, w_i=jP_i, the inverse is P_i=jw_i.
for i in range(1,5):
    assert red((10,10,i),{10})==(i,)
    assert red((10,10,i),{10})==(i,)

out={'status':'PASS_EXACT_INTERMEDIATE_SOURCE_QUOTIENT_MAP',
     'input_path':str(src.relative_to(ROOT)),
     'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'intermediate_generators':{'1':'a','2':'B','3':'d','4':'e','5':'f','6':'C','8':'k','10':'j'},
     'five_actual_inner_regional_words':regional,
     'six_source_prelifts_in_M':[{'name':row['name'],'word':w} for w,row in zip(prelifts,D['actual_six_source_words'])],
     'final_quotient_source_images':[row['word'] for row in D['actual_six_source_words']],
     'actual_prefixes':prefix,'four_remaining_relators':remaining,
     'source_comparisons':6,'mirror_inverse_checks':9,
     'scope':'The six words freely generate the discrete intermediate selected centralizer factor by the proof. Their map to the final actual words is checked using all prefix relations. No final source injectivity or completed carrier embedding is inferred.'}
(ROOT/'work_A/intermediate_source_prelifts25.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS nine inverse actual mirror substitutions')
print('PASS all six intermediate prelifts map LITERALLY to the stored actual source words')
print('PASS all four remaining exact prefix-square relators under the final quotient map')
print('Intermediate source lengths:',[len(w) for w in prelifts])
print('Final source lengths:',[len(row['word']) for row in D['actual_six_source_words']])
print('Scope: no early jKj=eta(K) substitution, no final source-freeness assertion')
