#!/usr/bin/env python3
"""Fast independent exact certificate for the two-dimensional top H2 term.

Independent original action rows are eliminated from LOW pivots, whereas the
full exploration used HIGH pivots.  Two explicit invariant alternating forms
give the opposite rank inequality, checked on every original action matrix.
"""
from pathlib import Path
import hashlib,itertools,json,time
CODE=Path(__file__).resolve().parent;start=time.time()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';s=json.loads(source.read_text())
assert sha(source)=='95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88'
full=CODE/'pbc_two_top_module.json';r=json.loads(full.read_text());assert r['status']=='PASS'
assert r['source_sha256']==sha(source) and r['wedge_rank']==2554 and r['wedge_dimension']==2556
con={(i,j):w for i,j,w in s['conjugates']};d=72;pairs=list(itertools.combinations(range(d),2))
def idx(a,b):
    if a>b:a,b=b,a
    assert a<b
    return a*(2*d-a-1)//2+b-a-1
def wedge(a,b):
    v=0
    aa=[i for i in range(d) if a>>i&1];bb=[i for i in range(d) if b>>i&1]
    for i in aa:
        for j in bb:
            if i!=j:v^=1<<idx(i,j)
    return v
def rank_low(rows):
    B={}
    for v in rows:
        while v:
            p=(v&-v).bit_length()-1
            if p not in B:B[p]=v;break
            v^=B[p]
    return len(B)
M={}
for g in range(1,105):
    a=[]
    for i in range(105,177):
        w=con[i,g];assert all(k>=105 for k in w[::2])
        v=sum((e%2)<<(k-105) for k,e in zip(w[::2],w[1::2]));a.append(v)
    assert rank_low(a)==72
    assert [hex(v) for v in a]==r['all_action_matrices_hex'][str(g)]
    M[g]=a
ordinary=[M[g][i]^(1<<i) for g in range(87,105) for i in range(d)]
assert rank_low(ordinary)==72
selected=[]
for g,i,j in r['independent_original_wedge_row_labels']:
    selected.append(wedge(M[g][i-105],M[g][j-105])^(1<<idx(i-105,j-105)))
assert len(selected)==2554 and rank_low(selected)==2554
explore=CODE/'pbc_two_top_norm_wedge_exploration.json';e=json.loads(explore.read_text())
forms=[int(v,16) for v in e['invariant_alternating_forms_hex']]
assert len(forms)==2 and rank_low(forms)==2
mat=[]
for B in forms:
    rows=[0]*d
    for q,(i,j) in enumerate(pairs):
        if B>>q&1:rows[i]|=1<<j;rows[j]|=1<<i
    mat.append(rows)
    for g in range(1,105):
        for i in range(d):
            left=0
            for a in range(d):
                if M[g][i]>>a&1:left^=rows[a]
            for j in range(d):
                assert ((left&M[g][j]).bit_count()&1)==((rows[i]>>j)&1)
    assert all((wedge(1<<i,M[2][i])&B).bit_count()%2==0 for i in range(d))

# Optional, fully checked algebraic data for later target-bit computations:
# invariant quadratic refinements of each alternating form, when they exist.
quadratic=[]
for B in forms:
    def cross(v):
        return sum((B>>idx(i,j))&1 for i,j in pairs if (v>>i&1) and (v>>j&1))%2
    basis={};consistent=True
    for g in (1,2):
        for i in range(d):
            v=M[g][i]^(1<<i);rhs=cross(M[g][i])
            while v:
                p=v.bit_length()-1
                if p not in basis:basis[p]=(v,rhs);break
                w,b=basis[p];v^=w;rhs^=b
            if not v and rhs:consistent=False
    q=0
    if consistent:
        for p in sorted(basis):
            v,rhs=basis[p]
            if ((v&q).bit_count()&1)^rhs:q|=1<<p
        for g in range(1,105):
            for i in range(d):assert ((M[g][i]&q).bit_count()&1)^cross(M[g][i])==((q>>i)&1)
    quadratic.append(dict(exists=consistent,linear_part_hex=hex(q) if consistent else None,
                          equation_rank=len(basis),verified_all104_actions=consistent))

out=dict(status='PASS',source_sha256=sha(source),full_calculation_sha256=sha(full),
         checker_sha256=sha(__file__),module_dimension=72,
         normal_odd_subgroup_generators=list(range(87,105)),
         normal_odd_coinvariant_rank=72,normal_odd_coinvariant_dimension=0,
         independently_rechecked_original_wedge_rows=2554,
         independent_low_pivot_rank=2554,invariant_alternating_forms_hex=[hex(v) for v in forms],
         every_original_quotient_action_preserves_both_forms=True,
         forms_independent=True,wedge_coinvariant_dimension=2,
         every_norm_wedge_a_s_a_detects_zero=True,quadratic_refinements=quadratic,
         seconds=time.time()-start,
         scope='Exact original-action rank certificate. The splitting and H2 direct-sum conclusion are proved separately; no target-bit value is claimed.')
(CODE/'pbc_two_top_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
