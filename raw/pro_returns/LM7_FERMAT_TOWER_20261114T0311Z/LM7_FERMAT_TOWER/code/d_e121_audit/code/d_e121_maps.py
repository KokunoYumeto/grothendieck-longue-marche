#!/usr/bin/env python3
"""Independent exact E121 peer certificate, using Fraction and enumeration.

No author Python module is imported. Marked ideal maps are independently
verified by d_e121_ideals.gp. Author output objects supply the already certified
E119 lattice bases; all E121 literal maps below are reconstructed separately.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json, hashlib

BASE = Path(__file__).resolve().parent.parent
I = BASE / 'inputs'
def records(name):
    return [json.loads(s) for s in (I / (name+'.out')).read_text().splitlines()
            if s.startswith('{')]
def record(name, typ):
    found = [r for r in records(name) if r.get('type') == typ]
    assert len(found) == 1
    return found[0]
def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return list(map(list, zip(*a)))
def mm(a,b):
    bt = transpose(b)
    return [[sum(x*y for x,y in zip(r,c)) for c in bt] for r in a]
def mv(a,v): return tuple(sum(x*y for x,y in zip(r,v)) for r in a)
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(n,a): return [[n*x for x in r] for r in a]
def inverse(a):
    n=len(a); w=[[Q(x) for x in a[i]+eye(n)[i]] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if w[k][j])
        w[j],w[k]=w[k],w[j]; pivot=w[j][j]
        w[j]=[x/pivot for x in w[j]]
        for k in range(n):
            if k != j:
                c=w[k][j];w[k]=[x-c*y for x,y in zip(w[k],w[j])]
    assert [r[:n] for r in w] == eye(n)
    return [r[n:] for r in w]
def integers(a):
    assert all(Q(x).denominator == 1 for r in a for x in r)
    z=[[int(x) for x in r] for r in a]
    assert z == a
    return z
def reduced(m,mods):
    m=integers(m)
    return [[x%q for x in r] for r,q in zip(m,mods)]
def act(m,v,mods):
    w=mv(m,v)
    assert all(Q(x).denominator==1 for x in w)
    return tuple(int(x)%q for x,q in zip(w,mods))
def elements(mods): return list(product(*(range(q) for q in mods)))
def hreduce(v,H):
    v=list(v);n=len(v)
    for j in range(n-1,-1,-1):
        c=v[j]//H[j][j]
        v=[v[i]-c*H[i][j] for i in range(n)]
    assert all(0 <= v[j] < H[j][j] for j in range(n))
    return tuple(v)
def hgroup(H):
    assert all(H[i][j] == 0 for i in range(len(H)) for j in range(i))
    return elements([H[j][j] for j in range(len(H))])
def relation_map(A,H1,H2):
    integers(mm(inverse(H2),mm(A,H1)))
def matrix_zero(a,mods): assert reduced(a,mods)==[[0]*len(a[0]) for _ in mods]
def rational_json(a):
    z=[[str(Q(x)) for x in r] for r in a]
    assert [[Q(x) for x in r] for r in z] == a
    return z

br=record('e119_e53_genus_transition','next_genus_presentation')
lr=record('e119_e53_positional_genus_transition','positional_genus_transition')
fr=record('e53_order_nine_genus','cyclic_nine_genus')
author=json.loads((I/'e53_normalizer_module.json').read_text())
lattices={}
for name,r,mod,rho,ks,ds in [
    ('B',br,[9,3,3,3],3,'kernel_smith_left','kernel_smith_diagonal'),
    ('L',lr,[9,3],3,'kernel_smith_left','kernel_smith_diagonal'),
    ('nine',fr,[9,3,3],9,'kernel_Smith_left','kernel_Smith_diagonal')]:
    H,K,U,D=[r[k] for k in ['relation_HNF','kernel_lattice',ks,ds]]
    fw=mm(U,inverse(K)); bw=integers(mm(K,inverse(U)))
    assert mm(fw,bw)==eye(len(H))==mm(bw,fw)
    assert rational_json(fw)==author['exact_Gamma_forward_'+name]
    assert bw==author['exact_Gamma_inverse_'+name]
    universe=hgroup(H)
    kernel=[v for v in universe if sum(x*y for x,y in zip(v,r['restriction_row']))%rho==0]
    coords={}
    for v in kernel:
        full=integers([list(mv(fw,v))])[0]
        c=tuple(full[i]%mod[i] for i in range(len(mod)))
        assert c not in coords;coords[c]=v
        assert hreduce(mv(bw,list(c)+[0]*(len(H)-len(c))),H)==v
    assert set(coords)==set(elements(mod))
    lattices[name]=(H,K,U,D,fw,bw,kernel,mod)

HB,KB,UB,DB,fB,bB,kB,mB=lattices['B']
HL,KL,UL,DL,fL,bL,kL,mL=lattices['L']
HF,KF,UF,DF,fF,bF,kF,mF=lattices['nine']
assert [len(hgroup(H)) for H in [HB,HL,HF]] == [729,81,729]
assert list(map(len,[kB,kL,kF])) == [243,27,81]
RF=[[12,-3,-11],[0,1,0],[-2,0,1],[-1,0,1]]
PF=[[0,0,-1,1],[0,1,0,0],[0,0,-1,2]]
assert mm(PF,RF)==eye(3)
for v in kF:
    c=act(PF,v,[9,3,3]);assert hreduce(mv(RF,c),HF)==v

Cg=[[1,6,0],[1,1,0],[0,0,1]]
Ch=[[4,3,3],[2,1,0],[2,0,1]]
Xg=[[0,1,0],[0,0,2],[1,2,1],[0,1,1],[0,0,1],[0,2,1]]
Xh=[[2,0,2],[0,1,2],[2,2,2],[2,1,2],[1,2,0],[1,0,1]]
def genus_action(perm,C,X):
    A=[[0]*9 for _ in range(9)]
    for i,j in enumerate(perm): A[j-1][i]=1
    for i in range(6):
        for j in range(3): A[i][6+j]=-X[i][j]
    for i in range(3):
        for j in range(3): A[6+i][6+j]=C[i][j]
    return A
AG=genus_action([3,1,2,4,5,6],Cg,Xg)
AH=genus_action([2,3,1,6,4,5],Ch,Xh)
G=[[1,0,0,0],[2,0,1,2],[2,2,2,2],[0,0,0,1]]
H=[[4,3,6,0],[2,2,2,0],[0,1,0,0],[1,0,0,1]]
for n,A,C,X,M in [('g',AG,Cg,Xg,G),('h',AH,Ch,Xh,H)]:
    r=next(r for r in records('e53_normalizer_actions') if r.get('name')==n)
    assert A==r['genus_action'] and C==r['ideal_class_columns'] and X==r['principal_correction_characters']
    relation_map(A,HB,HB)
    raw=mm(fB,mm(A,bB));assert raw==r['coinvariant_Smith_action']
    assert reduced([row[:4] for row in raw[:4]],mB)==M
    for v in kB:
        c=act(fB,v,mB)
        assert act(fB,mv(A,v),mB)==act(M,c,mB)

NG=[[1,1,1,0,0,0,-1,0,-1],[0,0,0,1,1,1,-1,-2,-2],
    [0,0,0,0,0,0,0,6,3],[0,0,0,0,0,0,1,0,0]]
JG=[[1,0,-2,-1],[1,0,0,-2],[1,0,-2,0],[0,1,0,0],[0,1,0,-2],
    [0,1,0,-1],[0,0,3,6],[0,0,1,0],[0,0,2,0]]
PG=[[0,0,0,3,0,0,-2,-3,-4],[1,1,1,0,0,0,-2,-2,-2],
    [0,0,0,0,3,0,-1,-3,-7],[0,0,0,0,0,3,-3,-3,-1]]
assert NG==record('e53_horizontal_upper_norm','horizontal_genus_norm')['genus_norm']
assert JG==record('e53_horizontal_upper_extension','horizontal_genus_extension')['genus_extension']
assert PG==record('e53_cyclic_nine_comparison','cyclic_nine_actual_comparison')['genus_norm']
for A,H1,H2 in [(NG,HB,HL),(JG,HL,HB),(PG,HB,HF)]:relation_map(A,H1,H2)
integers(mm(inverse(HL),sub(mm(NG,JG),scale(3,eye(4)))))
integers(mm(inverse(HB),sub(mm(JG,NG),add(eye(9),add(AH,mm(AH,AH))))))
N=[[6,3,6,3],[2,0,0,0]]
J=[[3,0],[2,1],[2,1],[1,0]]
Pi=[[5,3,6,6],[1,1,2,1],[0,0,0,2]]
for A,source,target,literal in [(NG,'B','L',N),(JG,'L','B',J),(PG,'B','nine',Pi)]:
    Ls,Lt=lattices[source],lattices[target]
    raw=mm(Lt[4],mm(A,Ls[5]))
    assert reduced([r[:len(Ls[7])] for r in raw[:len(Lt[7])]],Lt[7])==literal
    for v in Ls[6]:
        c=act(Ls[4],v,Ls[7]);assert act(Lt[4],mv(A,v),Lt[7])==act(literal,c,Lt[7])

B=elements(mB);L=elements([9,9]);lower=elements([3,3])
Nh=[[1,0,6,6],[0,3,6,3]];Jh=[[0,3],[2,0],[2,0],[0,1]]
NB=[[0,0,0,2],[1,0,0,2]];JB=[[6,3],[0,0],[0,0],[0,0]]
NL=[[0,2],[2,0]];JL=[[0,6],[6,0]]
sigma=[[1,3],[0,1]];pL=[[6,1],[2,1]]
delta=(3,0,0,0)
for x in B:
    assert act(Jh,act(Nh,x,[9,9]),mB)==tuple((a+b+c)%q for a,b,c,q in zip(x,act(H,x,mB),act(H,act(H,x,mB),mB),mB))
    assert act(JB,act(NB,x,[3,3]),mB)==tuple(3*a%q for a,q in zip(x,mB))
    assert act(pL,act(Nh,x,[9,9]),mL)==act(N,x,mL)
    assert act(G,act(H,x,mB),mB)==act(H,act(G,x,mB),mB)
for a in L:
    assert act(Nh,act(Jh,a,mB),[9,9])==tuple(3*x%9 for x in a)
    assert act(Jh,a,mB)==act(J,act(pL,a,mL),mB)
    assert act(JL,act(NL,a,[3,3]),[9,9])==tuple(3*x%9 for x in a)
    for k in range(3):
        a2=((a[0]+3*k*a[1])%9,a[1])
        assert act(pL,a2,mL)==act(pL,a,mL) and act(Jh,a2,mB)==act(Jh,a,mB)
for b in lower:
    lifts=[a for a in L if act(NL,a,[3,3])==b]
    assert len(lifts)==9
    assert {tuple(3*x%9 for x in a) for a in lifts}=={act(JL,b,[9,9])}
gim={tuple((y-x)%q for x,y,q in zip(a,act(G,a,mB),mB)) for a in B}
him={tuple((y-x)%q for x,y,q in zip(a,act(H,a,mB),mB)) for a in B}
assert gim=={(0,0,0,0),(0,1,1,0),(0,2,2,0)} and len(him)==9
assert {a for a in B if act(Pi,a,[9,3,3])==(0,0,0)}==gim
fixedH={a for a in B if act(H,a,mB)==a}
fixedL={a for a in L if act(sigma,a,[9,9])==a}
assert fixedH=={(3*r,t,t,s) for r,t,s in product(range(3),repeat=3)}
assert {a for a in fixedH if (a[0]//3-a[3])%3==0}=={act(Jh,a,mB) for a in L}
assert fixedL=={(a,3*b) for a,b in product(range(9),range(3))}
assert {a for a in fixedL if a[0]%3==0}=={act(JL,a,[9,9]) for a in lower}
assert {act(JB,b,mB) for b in lower}=={(0,0,0,0),(3,0,0,0),(6,0,0,0)}
inertia=[0]*9;inertia[3]=1
boundary=tuple(x-y for x,y in zip(inertia,mv(AH,inertia)))
assert act(fB,boundary,mB)==delta and delta not in him
assert act(Nh,delta,[9,9])==(3,0)

# A different literal coordinate system for the actual order162 normal closure.
# (a,u): alpha2 maps to zeta9^a alpha2, zeta27 maps to zeta27^u.
U27=[u for u in range(27) if u%3]
group=list(product(range(9),U27));one=(0,1)
def mul(x,y):return ((x[0]+x[1]*y[0])%9,(x[1]*y[1])%27)
def power(x,n):
    v=one
    for _ in range(n):v=mul(v,x)
    return v
def inv(x):return ((-pow(x[1],-1,9)*x[0])%9,pow(x[1],-1,27))
for a,b in product(group,repeat=2):
    c=mul(a,b);assert c in group
    assert mul(c,inv(b))==a
kb={x for x in group if x[1]%9==1 and (3*x[0]+x[1]-1)%27==0}
kbar={x for x in group if x[1]%9==1 and (3*x[0]-x[1]+1)%27==0}
kb1={x for x in group if x[0]%3==0 and x[1]%9==1}
kl={x for x in group if (3*x[0]+x[1]-1)%27==0}
kl1={x for x in group if (3*x[0]+x[1]-1)%9==0}
cf={x for x in group if x[1]%9==1}
assert list(map(len,[kb,kbar,kb1,kl,kl1,cf]))==[3,3,9,9,27,27]
assert kb & kbar=={one} and {mul(a,b) for a in kb for b in kbar}==kb1
assert all(mul(a,b)==mul(b,a) for a,b in product(cf,repeat=2))
g=(1,1);h=(8,4)
assert mul(mul(h,g),inv(h))==power(g,4)
assert power(h,3)==(6,10) and kb=={power(h,3*i) for i in range(3)}
assert kl=={power(h,i) for i in range(9)}
psi=[[1,1,2,1]]
assert Counter(act(psi,x,[3])[0] for x in B)=={0:81,1:81,2:81}
for x in B:
    assert act(psi,act(G,x,mB),[3])==act(psi,x,[3])==act(psi,act(H,x,mB),[3])

out={'status':'PASS','implementation':'Independent Fraction matrix arithmetic, HNF coset enumeration, literal maps and different order162 group coordinates; author checker not imported',
     'genus_orders':[729,81,729],'restriction_kernel_orders':[243,27,81],
     'all_exact_forward_maps':{n:rational_json(v[4]) for n,v in lattices.items()},
     'full_class_orders':{'B2':len(B),'L2':len(L)},
     'normalizer_genus_elements_checked':2*len(kB),
     'genus_norm_transfer_quotient_elements_checked':len(kB)*2+len(kL),
     'lift_independent_vertical_extension':{'lower_elements':9,'lifts_per_element':9,'rule':'j_L(b)=3a for every N_L(a)=b'},
     'positive_connecting_class':list(delta),'normal_closure_all_products':len(group)**2,
     'normal_closure_subgroup_orders':{'B2':3,'conjugate_B2':3,'B1':9,'L2':9,'L1':27,'F':27},
     'unit_defect_orders':{'B_vertical':81,'L_vertical':3,'horizontal':3},
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
text=json.dumps(out,indent=2)+'\n'
(BASE/'code/d_e121_maps.json').write_text(text)
print(text,end='')
