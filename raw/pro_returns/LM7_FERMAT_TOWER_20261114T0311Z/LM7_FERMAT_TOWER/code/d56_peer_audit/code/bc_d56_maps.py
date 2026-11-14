#!/usr/bin/env python3
"""Independent D56 finite-map and peripheral-kernel checks.

Reconstruct the finite groups with ROW matrices (the author records columns),
evaluate all 97 marked words, and recompute the same-action injection rather
than infer it from the three fixed-space dimensions.  No author program is
imported or executed.  Frozen coefficient arrays are explicit inputs.
"""
from pathlib import Path
from itertools import product
from collections import deque, Counter
import hashlib, json

HERE=Path(__file__).resolve().parent
INPUT=HERE.parent/'inputs'
def load(n): return json.loads((INPUT/(n+'.json')).read_text())
Q=load('d_arithmetic_correction_graph')
B=load('d_arithmetic_affine_base')
C=load('d_arithmetic_affine_action')
H=load('d_arithmetic_affine_homology')

def eye(n):return tuple(int(i==j) for i in range(n) for j in range(n))
def mm(A,B,n,p):
    return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%p
                 for i in range(n) for j in range(n))
def mv(A,x,p=3):
    n=len(x)
    return tuple(sum(A[n*i+j]*x[j] for j in range(n))%p for i in range(n))
def tr(cols):
    n=len(cols)
    return tuple(cols[j][i] for i in range(n) for j in range(n))
def add(x,y):return tuple((a+b)%3 for a,b in zip(x,y))
def neg(x):return tuple(-a%3 for a in x)
def rank3(rows,n=None):
    rows=[list(r) for r in rows]
    n=len(rows[0]) if n is None and rows else (n or 0)
    h=0
    for j in range(n):
        k=next((k for k in range(h,len(rows)) if rows[k][j]%3),None)
        if k is None:continue
        rows[h],rows[k]=rows[k],rows[h]
        u=pow(rows[h][j],-1,3);rows[h]=[x*u%3 for x in rows[h]]
        for k in range(len(rows)):
            if k!=h and rows[k][j]%3:
                a=rows[k][j];rows[k]=[(x-a*y)%3 for x,y in zip(rows[k],rows[h])]
        h+=1
    return h

# Reconstruct actual Q from literal SL2(Z/12) matrices, quotient by +/-I.
def qcanon(A):return min(A,tuple(-x%12 for x in A))
def qm(A,B):return qcanon(mm(A,B,2,12))
q0=eye(2);qs=(0,1,11,0);qr=(0,1,11,1)
S=(0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0)
R=(1,0,0,0,2,1,2,0,0,0,1,0,2,0,1,1)
I=eye(4);z=(0,0,0,0);v=(1,1,1,0)
assert tr(B['quotient_s_columns'])==S
assert tr(B['quotient_r_columns'])==R
assert tuple(B['affine_s_translation'])==z
assert tuple(B['affine_r_translation'])==v
qimage={q0:I};queue=deque([q0]);edge_count=0
while queue:
    q=queue.popleft()
    for a,A in [(qs,S),(qr,R)]:
        q1=qm(q,a);m=mm(qimage[q],A,4,3)
        if q1 in qimage:assert qimage[q1]==m
        else:qimage[q1]=m;queue.append(q1)
        edge_count+=1
qstates=[tuple(x) for x in Q['Q_states']]
assert len(qimage)==576 and set(qimage)==set(qstates)
qindex={q:i for i,q in enumerate(qstates)}
assert all(Q['right_s'][i]==qindex[qm(q,qs)] and
           Q['right_r'][i]==qindex[qm(q,qr)] for i,q in enumerate(qstates))
linear=list(dict.fromkeys(qimage.values()));assert len(linear)==48
saved_linear=[tr(x) for x in B['Q_linear_image_matrices']]
assert all(qimage[q]==saved_linear[B['Q_to_linear_image'][i]]
           for i,q in enumerate(qstates))
kernel={q for q,M in qimage.items() if M==I}
assert {qindex[q] for q in kernel}==set(B['Q_linear_kernel_states'])
qinv={q:next(h for h in kernel if qm(q,h)==q0) for q in kernel}
comm={qm(qm(qm(g,h),qinv[g]),qinv[h]) for g in kernel for h in kernel}
assert len(kernel)==12 and len(comm)==4 and all(qm(a,b) in comm for a in comm for b in comm)
assert all(qm(a,a)==q0 for a in comm)
assert {qindex[q] for q in comm}=={0,572,574,575}
assert qimage[qcanon((5,0,0,5))]==tuple(-x%3 for x in I)

# Literal affine source and its rank-four map on all marked N generators.
def am(a,b):
    x,A=a;y,B0=b
    return add(x,mv(A,y)),mm(A,B0,4,3)
def ap(a,n):
    out=(z,I)
    while n:
        if n&1:out=am(out,a)
        a=am(a,a);n//=2
    return out
s=(z,S);r=(v,R);t=am(s,r);r2=ap(r,2)
assert ap(s,2)==ap(r,3)==(z,I)
aff={(z,I)};queue=deque([(z,I)])
while queue:
    g=queue.popleft()
    for a in [s,r]:
        h=am(g,a)
        if h not in aff:aff.add(h);queue.append(h)
assert len(aff)==3888
phi=B['actual_quotient_covector_rows'];assert rank3(phi)==4
def evaluate(word):
    g=(z,I)
    for token in word:g=am(g,[s,r,r2][token])
    return g
for j,word in enumerate(B['all97_source_basis_words']):
    assert evaluate(word)==(tuple(row[j] for row in phi),I)
for source,A in [('mod3_s_columns',S),('mod3_r_columns',R)]:
    for j,col in enumerate(Q[source]):
        left=tuple(sum(row[k]*col[k] for k in range(97))%3 for row in phi)
        right=mv(A,tuple(row[j] for row in phi))
        assert left==right

vecs=list(product(range(3),repeat=4))
lines=[x for x in vecs if any(x) and next(a for a in x if a)==1]
for x in lines:
    orbit={x};queue=deque([x])
    while queue:
        w=queue.popleft()
        for A in [S,R]:
            y=mv(A,w)
            if y not in orbit:orbit.add(y);queue.append(y)
    assert rank3(orbit)==4
assert len(lines)==40
im1R={add(x,neg(mv(R,x))) for x in vecs}
candidates=[a for a in vecs if mv(S,a)==neg(a) and add(a,neg(add(v,v))) in im1R]
assert candidates==[(2,1,2,1)]
a=(candidates[0],I);t6=ap(t,6)
assert t6==((0,2,1,0),tuple(-x%3 for x in I)) and ap(t,12)==(z,I)
assert all(ap(t,k)!=(z,I) for k in range(1,12))
assert am(am(t6,s),t6)==am(s,a)
assert am(am(t6,r),t6)==am((neg(a[0]),I),r)
actual={g:am(am(t6,g),t6) for g in aff}
for g in aff:
    assert actual[am(g,s)]==am(actual[g],am(s,a))
    assert actual[am(g,r)]==am(actual[g],am((neg(a[0]),I),r))

# Endomorphism field, checked as an algebra of matrices, without source code.
end=[tr(m) for m in C['module_endomorphism_field_matrices']]
assert len(set(end))==9 and I in end and (0,)*16 in end
for A in end:
    assert all(mm(A,X,4,3)==mm(X,A,4,3) for X in [S,R])
    assert all(tuple((x+y)%3 for x,y in zip(A,B0)) in end and mm(A,B0,4,3) in end for B0 in end)
    if any(A):assert any(mm(A,B0,4,3)==I for B0 in end)
equations=[]
for X in [S,R]:
    for i in range(4):
        for j in range(4):
            row=[0]*16
            for k in range(4):
                row[4*i+k]=(row[4*i+k]+X[4*k+j])%3
                row[4*k+j]=(row[4*k+j]-X[4*i+k])%3
            equations.append(row)
assert rank3(equations)==14

# Actual same-action map: verify kernel inclusion and independence of all600
# images, retaining the actual marked moving module and its basis maps.
def bits(name):return [int(x,16) for x in H[name]]
def act(cols,x):
    out=0
    while x:
        b=x&-x;out^=cols[b.bit_length()-1];x^=b
    return out
def rank2(cols):
    basis={}
    for x in cols:
        while x:
            j=x.bit_length()-1
            if j not in basis:basis[j]=x;break
            x^=basis[j]
    return len(basis)
HS=bits('homology_s_columns');HR=bits('homology_r_columns')
WS=bits('moving_s_columns');WR=bits('moving_r_columns');WT=bits('moving_t_columns')
WB=bits('moving_basis');NA=bits('A_norm_columns')
assert rank2(WB)==640 and rank2(NA)==9
assert all(act(NA,w)==0 for w in WB)
assert all(act(HS,w)==act(WB,WS[i]) and act(HR,w)==act(WB,WR[i]) for i,w in enumerate(WB))
assert all(WT[i]==act(WS,WR[i]) for i in range(640))
assert all(act(WS,c)==1<<i for i,c in enumerate(WS))
assert all(act(WR,act(WR,c))==1<<i for i,c in enumerate(WR))
f={k:[int(x,16) for x in val] for k,val in H['moving_fixed_bases'].items()}
for key,A0 in [('s',WS),('r',WR),('t',WT)]:
    assert all(act(A0,x)==x for x in f[key])
    assert rank2(f[key])==len(f[key])==640-rank2([a0^(1<<j) for j,a0 in enumerate(A0)])
L=[(1<<i)^WS[i] for i in range(640)]+[act(WS,(1<<i)^WR[i]) for i in range(640)]
Kcols=f['s']+[x<<640 for x in f['r']]+[x|(x<<640) for x in f['t']]
assert rank2(L)==640 and len(Kcols)==600 and rank2(Kcols)==600
assert all(act(L,x)==0 for x in Kcols)
assert 1280-rank2(L)-rank2(Kcols)==40
cusps=bits('all_cusp_columns');pair=bits('pairing_columns_mod2')
assert len(cusps)==324 and rank2(cusps)==323
assert all(act(pair,c)==0 for c in cusps) and rank2(pair)==326
assert rank2([act(NA,c) for c in cusps])==3
assert rank2([c^act(NA,c) for c in cusps])==320

out={'status':'PASS','scope':'Independent literal finite-map and actual same-action-kernel verification; root owns the full seven-stage rebuild.',
     'Q_order':576,'Q_marked_edge_checks':edge_count,'linear_image_order':48,
     'linear_kernel_order':12,'linear_kernel_commutator_order':4,
     'all97_word_images_checked':97,'module_equivariance_columns_checked':194,
     'affine_group_order':3888,'actual_parameter':list(a[0]),
     'actual_inner_action_marked_edge_checks':7776,'irreducible_lines_checked':40,
     'endomorphism_algebra_dimension':2,'endomorphism_algebra_order':9,
     'moving_rank':640,'fixed_dimensions':{k:len(x) for k,x in f.items()},
     'cusp_map_rank':640,'same_action_injection_rank':600,'derivation_quotient_dimension':40,
     'cusp_rank':323,'compact_rank':326,'moving_cusp_rank':320,
     'exterior_rank':640*639//2+640*9,'exterior_invariant_rank':40*8*8,
     'inputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(INPUT.glob('*.json'))}}
(HERE/'bc_d56_maps.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
