#!/usr/bin/env python3
"""Focused independent matrix/centralizer verification for the frozen D53 data."""
from pathlib import Path
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/"D53_EXPERIMENTS"
manifest=json.loads((SRC/"ledger/d_arithmetic_correction_space_manifest.json").read_text())
verified=0
for rec in manifest["files"]+manifest["runtime_inputs"]:
    p=SRC/rec["path"]
    assert hashlib.sha256(p.read_bytes()).hexdigest()==rec["sha256"]
    verified+=1
data=json.loads((SRC/"code/d_arithmetic_correction_graph.json").read_text())
cols_s=data["mod3_s_columns"];cols_r=data["mod3_r_columns"];n=97
def apply(cols,v):
    return [sum(c[i]*v[j] for j,c in enumerate(cols))%3 for i in range(n)]
def subid(cols):
    return [[(x-int(i==j))%3 for i,x in enumerate(c)] for j,c in enumerate(cols)]
def rank(cols):
    a=[[c[i]%3 for c in cols] for i in range(n)];k=0
    for j in range(len(cols)):
        p=next((i for i in range(k,n) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k];inv=pow(a[k][j],-1,3)
        a[k]=[x*inv%3 for x in a[k]]
        for i in range(n):
            if i!=k:
                q=a[i][j]
                a[i]=[(x-q*y)%3 for x,y in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k
Ns,Nr=subid(cols_s),subid(cols_r)
assert rank(Ns)==52 and rank(Nr)==63
assert rank([apply(Nr,c) for c in Nr])==29
for j in range(n):
    e=[int(i==j) for i in range(n)]
    assert apply(cols_s,cols_s[j])==e
    assert apply(cols_r,apply(cols_r,cols_r[j]))==e
central_checks=0;lifted={}
for name,cols in [("s",cols_s),("r",cols_r)]:
    D=[[(-x)%3 for x in c] for c in subid(cols)]
    dr=rank(D);ok=0
    for rec in data["complete_centralizer_lifting_equations"][name]:
        rhs=[(-x)%3 for x in rec["defect"]]
        correction=rec["correction"]
        if correction is None:
            assert rank(D+[rhs])==dr+1
        else:
            assert apply(D,correction)==rhs
            assert rank(D+[rhs])==dr;ok+=1
        central_checks+=1
    lifted[name]=ok
assert lifted=={"s":16,"r":3}
def canonical(a):return min(a,tuple(-x%12 for x in a))
def mul(a,b):
    x,y,z,w=a;p,q,r,s=b
    return canonical(((x*p+y*r)%12,(x*q+y*s)%12,
                      (z*p+w*r)%12,(z*q+w*s)%12))
states=[tuple(x) for x in data["Q_states"]]
I=canonical((1,0,0,1));S=canonical((0,1,11,0));R=canonical((0,11,1,11))
actual={canonical(x) for x in product(range(12),repeat=4)
        if (x[0]*x[3]-x[1]*x[2])%12==1}
assert set(states)==actual and len(actual)==576
assert sum(mul(g,S)==mul(S,g) for g in states)==16
assert sum(mul(g,R)==mul(R,g) for g in states)==18
t=mul(S,R);a=I;cyclic=[]
while True:
    cyclic.append(a);a=mul(a,t)
    if a==I:break
assert len(cyclic)==12
assert any(data["actual_cusp_t12_mod3_cycle"])
bound=80*3**95-4*3**45-4*3**34
assert bound==int(data["summary"]["actual_arithmetic_peripheral_correction_dimension_lower_bound"])
assert bound>0
finite=json.loads((SRC/"code/d_cm_same_action_obstruction.json").read_text())
word=json.loads((SRC/"code/d_cm_same_action_word.json").read_text())
assert finite["summary"]["pair_to_actual_derivation_kernel_dimension"]==102
assert finite["summary"]["actual_peripheral_homology_derivation_image_dimension"]==18
assert finite["summary"]["same_mod2_action_obstruction_correction_rank"]==4
assert word["new_homology_columns"]==finite["identical_homology_columns"]
assert word["selected_parameter_mask"]==finite["new_parameter_mask"]=="0x400000000000000000000002004840"
out={"status":"PASS","manifest_entries_verified":verified,"homology_dimension":97,
     "independent_ranks":[52,63,29],"complete_centralizer_equations":central_checks,
     "lifted_Q_centralizer_images":lifted,"Q_order":576,
     "positive_arithmetic_dimension_bound":str(bound),
     "finite_same_action_columns_identical":True,
     "scope":"Independent frozen matrix/centralizer and cross-certificate check; full program reconstruction is owned by root."}
(ROOT/"bc_d53_exact_graph.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
