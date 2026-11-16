"""Exact first 3-adic lift of the B.62 quotient, retaining source H1.

For each actual source F_r, enumerate only its mod-3 image, lift a
Schreier transversal to matrices mod9, and evaluate every Schreier
generator in the elementary congruence kernel. The joint source
abelian map is retained integrally. Thus the constrained Lie image
is the actual image of ker(F_r -> mod3) intersect ker(source H1),
not an upper bound obtained by reducing an integral constraint mod3.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
start=time.monotonic();n=10;p=3;mod=9
words=json.loads((BASE/'next_B59_image/common_base_braid_words.json').read_text())
old=json.loads((BASE/'next_finite_symplectic/matrices.json').read_text())
J=np.array(old['integral_symplectic_form'],dtype=np.int64)
Ji=np.array(s.Matrix(J).inv(),dtype=np.int64)
eye=np.eye(n,dtype=np.int64)
braid={}
for j in range(1,11):
    B=np.eye(11,dtype=np.int64)
    B[j-1:j+1,j-1:j+1]=[[2,-1],[1,0]]
    R=(B[:10,:10]-B[10,:10])%mod
    assert np.array_equal(R.T@J@R%mod,J%mod)
    braid[j]=R;braid[-j]=Ji@R.T@J%mod
    assert np.array_equal(braid[j]@braid[-j]%mod,eye)

def norm(a):
    a=a%mod
    lead=next(int(x)%3 for x in a.flat if x%3)
    return a if lead==1 else -a%mod

def key(a):return (norm(a)%p).astype(np.int8).tobytes()
def inv(a):return Ji@a.T@J%mod
def evaluate(w):
    out=eye.copy()
    for j in w:out=out@braid[j]%mod
    return norm(out)

def rref(a):
    a=np.array(a,dtype=np.int64,copy=True)%p
    piv=[];r=0
    for j in range(a.shape[1]):
        hit=next((i for i in range(r,a.shape[0]) if a[i,j]),None)
        if hit is None:continue
        a[[r,hit]]=a[[hit,r]]
        a[r]=a[r]*int(a[r,j])%p
        f=a[:,j].copy();f[r]=0
        a=(a-f[:,None]*a[r])%p
        piv.append(j);r+=1
        if r==a.shape[0]:break
    return a,piv

def span(a):
    _,piv=rref(a)
    return np.asarray(a,dtype=np.int64)[:,piv]%p,piv

def nullspace(a):
    r,piv=rref(a);free=[j for j in range(r.shape[1]) if j not in piv]
    out=np.zeros((r.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        out[j,k]=1
        for i,c in enumerate(piv):out[c,k]=-r[i,j]%p
    assert not np.any(a@out%p)
    return out

cert0=json.loads((BASE/'next_finite_symplectic/abelian_detection_certificate.json').read_text())
B=np.array(cert0['kernel_basis'],dtype=np.int64)
assert np.array_equal(B[6:,:],np.eye(7,dtype=np.int64))
Q=np.hstack([np.eye(6,dtype=np.int64),-B[:6,:]])
assert not np.any(Q@B)
cyclic=json.loads((BASE/'next_B59_image/cyclic_bracket_span.json').read_text())
assert s.Matrix(cyclic['meridian_ambient_H1_columns']).rank()==6

def family(name,constraint,expected):
    src=sorted(words[name].items(),key=lambda item:int(item[0]))
    gens=[evaluate(w) for _,w in src];r=len(gens)
    reps=[eye.copy()];ab=[np.zeros(r,dtype=np.int64)];repwords=[[]]
    lookup={key(eye):0};todo=deque([0]);edges=[]
    while todo:
        i=todo.popleft()
        for j,g in enumerate(gens):
            product=norm(reps[i]@g)
            k=key(product)
            if k not in lookup:
                lookup[k]=len(reps);reps.append(product)
                vec=ab[i].copy();vec[j]+=1;ab.append(vec)
                repwords.append(repwords[i]+[j]);todo.append(lookup[k])
            edges.append((i,j,lookup[k]))
    assert len(reps)==expected
    print(name,'mod3 order',len(reps),'Schreier edges',len(edges),flush=True)
    repinv=[inv(a) for a in reps]
    lie=[];source=[]
    for i,j,k in edges:
        a=norm(reps[i]@gens[j]@repinv[k])
        assert np.array_equal(a%p,eye)
        X=((a-eye)%mod)//p
        assert not np.any((X.T@J+J@X)%p)
        lie.append(X.reshape(-1))
        v=ab[i]-ab[k];v=v.copy();v[j]+=1
        source.append(constraint@v)
    V=np.array(lie,dtype=np.int64).T
    U=np.array(source,dtype=np.int64).T
    # Exact integer HNF, not just the mod3 kernel of U: its index can
    # have a factor3 and omitting this step creates spurious directions.
    H=hermite_normal_form(s.Matrix(U))
    assert H.shape==(6,6) and H.det()!=0
    Ubar=H.inv()*s.Matrix(U)
    assert all(x.q==1 for x in Ubar)
    Ubar=np.array(Ubar,dtype=np.int64)
    _,piv=rref(Ubar)
    assert len(piv)==6
    C=s.Matrix(Ubar[:,piv]);d=int(C.det());adj=C.adjugate()
    assert d%3!=0
    free=[j for j in range(len(edges)) if j not in piv]
    E=np.array(adj*s.Matrix(Ubar[:,free]),dtype=np.int64)
    # Actual integral kernel words have powers d on edge free[j],
    # and -E[:,j] on the six pivot edges, in that fixed order.
    assert np.array_equal(d*Ubar[:,free]-Ubar[:,piv]@E,np.zeros((6,len(free)),dtype=np.int64))
    W=(d*V[:,free]-V[:,piv]@E)%p
    all_basis,all_selected=span(V)
    zero_basis,zero_selected=span(W)
    for z in zero_basis.T:
        X=z.reshape(n,n);assert not np.any((X.T@J+J@X)%p)
    print(name,'source lattice index',abs(int(H.det())),
          'full/constrained congruence dimensions',all_basis.shape[1],zero_basis.shape[1],flush=True)
    result={'name':name,'mod3_order':len(reps),
            'source_constraint':constraint.tolist(),
            'generator_keys':[int(k) for k,_ in src],
            'generator_mod9_matrices':[a.tolist() for a in gens],
            'section_source_words':repwords,'schreier_edges':edges,
            'source_HNF':[[int(x) for x in H.row(i)] for i in range(6)],
            'source_lattice_index':abs(int(H.det())),
            'source_pivot_edges':piv,'source_pivot_determinant':d,
            'source_pivot_adjugate':[[int(x) for x in adj.row(i)] for i in range(6)],
            'full_basis':all_basis.tolist(),'full_basis_edges':[edges[j] for j in all_selected],
            'constrained_basis':zero_basis.tolist(),
            'constrained_free_edges':[free[j] for j in zero_selected],
            'constrained_pivot_exponents':(-E[:,zero_selected]).tolist(),
            'constrained_free_exponent':d,
            'scope':'Exact mod9 congruence image of the source subgroup with zero integral ambient H1.'}
    (HERE/(name+'_lift.json')).write_text(json.dumps(result,indent=2)+'\n')
    np.savez_compressed(HERE/(name+'_schreier.npz'),lie=V,source=U,source_normalized=Ubar)
    return all_basis,zero_basis

T,T0=family('T',Q,144)
C,C0=family('C5',np.eye(6,dtype=np.int64),1440)
def intersection(A,B):
    N=nullspace(np.hstack([A,-B]))
    result=A@N[:A.shape[1],:]%p
    basis,selected=span(result)
    assert basis.shape[1]==N.shape[1]
    return basis,N[:,selected]

full,full_coordinates=intersection(T,C)
actual,actual_coordinates=intersection(T0,C0)
print('COMMON congruence Lie dimensions: full',full.shape[1],
      '; both source-H1 constrained',actual.shape[1],flush=True)
record={'prime':3,'modulus':9,'full_common_basis':full.tolist(),
        'full_common_coordinates':full_coordinates.tolist(),
        'constrained_common_basis':actual.tolist(),
        'constrained_common_coordinates':actual_coordinates.tolist(),
        'scope':'Allowed first lift of actual K after B62, from the two actual subgroup images and B58. Nonzero vectors are quotient-level compatible lifts only, not elements of K.'}
(HERE/'first_lift_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS exact first-lift calculation in',round(time.monotonic()-start,3),'seconds',flush=True)
