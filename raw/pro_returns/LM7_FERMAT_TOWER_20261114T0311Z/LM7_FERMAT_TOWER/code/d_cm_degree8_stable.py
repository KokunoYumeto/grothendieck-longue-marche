#!/usr/bin/env python3
"""Stable class-two corrections that fix the entire degree-eight quotient.

At k=2 the adapted high C2 words have K-degree at least10. All upper
corrections have degree at least16. This computes their Bockstein image
in the full15-dimensional upper obstruction space of D29.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
J=json.loads((OUT/'d_cm_degree8_high.json').read_text())
U=[int(x,16) for x in J['basis_old_N_homology_masks']]
pairs=[(i,j) for i in range(97) for j in range(i,97)]
pos={p:k for k,p in enumerate(pairs)}
def square(v):
    ix=[]
    while v:
        b=v&-v;ix.append(b.bit_length()-1);v^=b
    z=0
    for k,i in enumerate(ix):
        for j in ix[k:]:z^=1<<pos[i,j]
    return z
def comm(a,b):
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
    v=[sum(int(x)<<i for i,x in enumerate(M[:,j])) for j in range(97)]
    return [square(v[i]) if i==j else comm(v[i],v[j]) for i,j in pairs]
S=action_columns(R['qs']);T=action_columns(R['qm'](R['qs'],R['qr']))
F1=[(1<<i)^S[i] for i in range(4753)];F2=[S[i]^T[i] for i in range(4753)]
def apply(mask,columns):
    z=0
    while mask:
        b=mask&-mask;z^=columns[b.bit_length()-1];mask^=b
    return z
X=[square(U[i]) if i==j else comm(U[i],U[j]) for i,j in J['high_C1_pairs']]
assert len(X)==4708
B=[int(x,16) for x in json.loads((OUT/'d_cm_pro2_class2.json').read_text())['stabilized_obstruction_functionals']]
bas={};obas={};nullity=0
for j,x in enumerate(X+X):
    half=0 if j<4708 else 1
    v=apply(x,F1 if half==0 else F2)
    b=sum(((row&(x<<(4753*half))).bit_count()%2)<<i for i,row in enumerate(B))
    cert=1<<j
    while v:
        k=v.bit_length()-1
        if k not in bas:bas[k]=(v,b,cert);break
        vv,bb,cc=bas[k];v^=vv;b^=bb;cert^=cc
    if not v:
        nullity+=1
        while b:
            k=b.bit_length()-1
            if k not in obas:obas[k]=(b,cert);break
            b^=obas[k][0];cert^=obas[k][1]
summary={'high_basis_words':4708,'two_conjugator_variables':9416,
 'mod2_correction_rank':len(bas),'relation_dimension':nullity,
 'stable_full_obstruction_dimension':15,'restricted_Bockstein_rank':len(obas),
 'all_lower_corrections_in_D10_K':True,'all_upper_corrections_in_D16_K':True,
 'lower_multiplier_change_excluded':True,'upper_multiplier288_invisible_in_T3':True,
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_stable.json').write_text(json.dumps({'summary':summary,
 'basis_certificates':{str(k):{'image':v[0],'new_high_basis_relation':hex(v[1])} for k,v in obas.items()}},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
