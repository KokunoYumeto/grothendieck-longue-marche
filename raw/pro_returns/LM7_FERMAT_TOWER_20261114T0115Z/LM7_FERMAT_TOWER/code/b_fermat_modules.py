#!/usr/bin/env python3
"""Integral Fox-chain calculations for all-cusp-deleted Fermat curves.

The output gives an integral presentation of the compact homology module,
not merely its dimension: affine Z-basis, deck/S3 action matrices, and the
cuspidal relation matrix. All assertions are exact integer calculations.
"""
from pathlib import Path
import json
from itertools import product
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent

def inv(w): return [-a for a in w[::-1]]
def subst(w, images):
    out=[]
    for a in w: out += images[a] if a>0 else inv(images[-a])
    return out
def snf_values(A):
    S=smith_normal_form(A,domain=sp.ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]

def compute(n):
    V=list(product(range(n),repeat=2)); index={v:i for i,v in enumerate(V)}
    E=[(v,a) for v in V for a in (1,2)]; ei={e:i for i,e in enumerate(E)}
    def step(v,a):
        u=list(v); u[abs(a)-1]=(u[abs(a)-1]+(1 if a>0 else -1))%n
        return tuple(u)
    def path(v): return [1]*v[0]+[2]*v[1]
    tree={( (i,0),1) for i in range(n-1)}|{((i,j),2) for i in range(n) for j in range(n-1)}
    chords=[e for e in E if e not in tree]; cr=[ei[e] for e in chords]
    def chain(w,start=(0,0)):
        c=sp.zeros(2*n*n,1); v=start
        for a in w:
            u=step(v,a)
            c[ei[(v,a) if a>0 else (u,-a)]] += 1 if a>0 else -1
            v=u
        return c,v
    words=[path(v)+[a]+inv(path(step(v,a))) for v,a in chords]
    B=sp.Matrix.hstack(*(chain(w)[0] for w in words))
    r=len(words); assert r==n*n+1 and B[cr,:]==sp.eye(r)
    D=sp.zeros(n*n,2*n*n)
    for j,(v,a) in enumerate(E): D[index[step(v,a)],j]+=1; D[index[v],j]-=1
    assert D*B==sp.zeros(n*n,r) and D.rank()==n*n-1
    actions={}
    for name,g in [('x',(1,0)),('y',(0,1))]:
        P=sp.zeros(2*n*n)
        for j,(v,a) in enumerate(E): P[ei[(((v[0]+g[0])%n,(v[1]+g[1])%n),a)],j]=1
        T=(P*B)[cr,:]; assert B*T==P*B
        actions[name]=T
    # These based automorphisms induce the geometric S3 complement.
    # r^3 and (rs)^2 are inner by words in F', hence trivial on K_n^ab.
    for name,ims in [('r',{1:[1,2,-1],2:[-2,-1]}),('s',{1:[2],2:[1]})]:
        BB=sp.Matrix.hstack(*(chain(subst(w,ims))[0] for w in words))
        T=BB[cr,:]; assert B*T==BB
        actions[name]=T
    X,Y,R,S=(actions[q] for q in ['x','y','r','s']); I=sp.eye(r)
    assert X**n==Y**n==I and X*Y==Y*X
    assert R**3==S**2==(R*S)**2==I
    assert R*X==Y*R and R*Y==X**(n-1)*Y**(n-1)*R and S*X==Y*S
    cusp=[]
    for j in range(n): cusp.append(chain([1]*n,(0,j))[0][cr,:])
    for i in range(n): cusp.append(chain([2]*n,(i,0))[0][cr,:])
    for i in range(n): cusp.append(chain([1,2]*n,(i,0))[0][cr,:])
    C=sp.Matrix.hstack(*cusp); cv=snf_values(C)
    assert cv==[1]*(3*n-1)
    C0=C[:,:-1]
    for A in actions.values():
        coeff=C0.gauss_jordan_solve(A*C)[0]
        assert all(z.q==1 for z in coeff)
    c=chain([1,2,-1,-2])[0][cr,:]
    O=sp.Matrix.hstack(*(X**i*Y**j*c for i,j in V))
    assert R*c==c and S*c==-c
    assert O.rank()==n*n-1
    # Inclusion K_n -> F on abelianizations is exponent sum of basis words.
    Q=sp.Matrix([[sum(1 if a==k else -1 if a==-k else 0 for a in w) for w in words] for k in [1,2]])
    assert Q*O==sp.zeros(2,n*n)
    assert snf_values(Q)==[n,n]
    assert snf_values(C.row_join(O))==[1]*r
    # Compact module R_n/(S_x,S_y,P_n), P_n=sum_{0<=j<=i<n}x^i y^j.
    regx=sp.zeros(n*n); regy=sp.zeros(n*n)
    for j,(a,b) in enumerate(V):
        regx[index[((a+1)%n,b)],j]=1; regy[index[(a,(b+1)%n)],j]=1
    SX=sum((regx**a for a in range(n)),sp.zeros(n*n))
    SY=sum((regy**b for b in range(n)),sp.zeros(n*n))
    P=sum((regx**a*regy**b for a in range(n) for b in range(a+1)),sp.zeros(n*n))
    J=SX.row_join(SY).row_join(P)
    sj=snf_values(J)
    assert sj==[1]*(3*n-2)
    assert (n*n-len(sj))==(n-1)*(n-2)
    # Quotient-map compatibility: each proposed annihilator column maps into cusps.
    coeff=C0.gauss_jordan_solve(O*J)[0]
    assert all(z.q==1 for z in coeff)
    characters=[{'a':a,'b':b,'affine_multiplicity':2 if (a,b)==(0,0) else 1,
                 'compact_multiplicity':int(a!=0 and b!=0 and (a+b)%n!=0)} for a,b in V]
    return {'n':n,'genus':(n-1)*(n-2)//2,'cusps':3*n,'affine_rank':r,
            'compact_rank':(n-1)*(n-2),'cusp_rank':len(cv),'cusp_SNF':cv,
            'compact_annihilator_SNF':sj,'base_map_SNF':[n,n],
            'affine_basis_words':words,'chain_basis':B.tolist(),
            'actions':{k:v.tolist() for k,v in actions.items()},
            'cuspidal_relations':C.tolist(),'commutator_orbit_map':O.tolist(),
            'base_abelianization_map':Q.tolist(),'characters':characters,
            'verified':'integer Fox boundary; primitive cuspidal lattice; deck/S3 relations; cyclic compact presentation'}

def main():
    records=[]
    print('n genus cusps H1_affine H1_compact cusp_rank base_map_smith checks')
    for n in range(1,9):
        rec=compute(n); records.append(rec)
        print(n,rec['genus'],rec['cusps'],rec['affine_rank'],rec['compact_rank'],rec['cusp_rank'],[n,n],'PASS',flush=True)
    data={'convention':'U_n removes all 3n coordinate cusps; compact X_n:x^n+y^n=z^n',
          'coefficient_ring':'Z','records':records}
    (OUT/'b_fermat_modules.json').write_text(json.dumps(data,indent=2,default=int)+'\n')

if __name__=='__main__': main()
