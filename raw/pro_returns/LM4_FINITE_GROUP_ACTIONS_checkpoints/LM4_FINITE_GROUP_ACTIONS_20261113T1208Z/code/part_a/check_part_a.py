#!/usr/bin/env python3
"""Finite certificates for Part A. All calculations use exact finite arithmetic."""
from collections import deque
import json
from pathlib import Path

I = tuple(int(i == j) for i in range(4) for j in range(4))
def mat(p, entries):
    z=list(I)
    for i,j,v in entries: z[4*i+j]=(z[4*i+j]+v)%p
    return tuple(z)
def mul(a,b,p):
    return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4))%p
                 for i in range(4) for j in range(4))
def inv(a,p):
    # For a=1+N in UT_4, a^{-1}=1-N+N^2-N^3.
    N=tuple((a[i]-I[i])%p for i in range(16))
    N2=mul(N,N,p); N3=mul(N2,N,p)
    return tuple((I[i]-N[i]+N2[i]-N3[i])%p for i in range(16))
def comm(a,b,p): return mul(mul(mul(a,b,p),inv(a,p),p),inv(b,p),p)
def closure(gens,p):
    gs=tuple(gens)+tuple(inv(g,p) for g in gens)
    seen={I}; todo=deque([I])
    while todo:
        a=todo.popleft()
        for g in gs:
            z=mul(a,g,p)
            if z not in seen: seen.add(z); todo.append(z)
    return seen
def sparse(a):
    return {f'E{i+1}{j+1}':a[4*i+j] for i in range(4) for j in range(i+1,4) if a[4*i+j]}

def ut_case(p):
    x=mat(p,[(0,1,1),(1,2,1)])
    y=mat(p,[(2,3,1)])
    c=comm(x,y,p); d=mul(mul(x,c,p),inv(x,p),p)
    G=closure([x,y],p)
    D=closure([mul(mul(g,c,p),inv(g,p),p) for g in G],p)
    cyc=closure([c],p)
    assert c==mat(p,[(1,3,1)])
    assert d==mat(p,[(1,3,1),(0,3,1)])
    assert d not in cyc
    assert d in D and comm(c,d,p)==I
    assert all(comm(a,b,p)==I for a in D for b in D)
    # Genus-two relation: a1=x,b1=y,a2=y,b2=x.
    assert mul(comm(x,y,p),comm(y,x,p),p)==I
    Cx={g for g in G if comm(g,x,p)==I}
    return dict(p=p,group_order=len(G),derived_order=len(D),
                derived_abelian=True,c=sparse(c),x_c_x_inverse=sparse(d),
                conjugate_outside_cyclic=True,genus2_relation_verified=True,
                finite_centralizer_x_order=len(Cx))

def reduce_word(word):
    out=[]
    for a in word:
        if out and out[-1]==-a: out.pop()
        else: out.append(a)
    return tuple(out)
def subst(word,images):
    out=[]
    for a in word:
        im=images[abs(a)]
        out.extend(im if a>0 else tuple(-x for x in reversed(im)))
    return reduce_word(out)

def filling_case():
    k={1:(-2,),2:(-1,)}
    assert subst((1,2),k)==(-2,-1) # distinguished loop inverted
    assert subst(subst((1,),k),k)==(1,)
    assert subst(subst((2,),k),k)==(2,)
    def quotient_exp(w): return sum((1 if a==1 else -1 if a==-1 else -1 if a==2 else 1) for a in w)
    assert quotient_exp(k[1])==1 and quotient_exp(k[2])==-1
    return dict(kernel_automorphism={'x':'y^-1','y':'x^-1'},order=2,
                distinguished_xy_image='(xy)^-1',filled_x_exponent=1,
                filled_y_exponent=-1,nontrivial_source=True)

def abelian_examples():
    ans=[]
    for p in (2,3,5):
        v=[(1,0),(0,1),((-1)%p,(-1)%p)]
        assert tuple(sum(a[j] for a in v)%p for j in (0,1))==(0,0)
        ker=[(a,b,c) for a in range(p) for b in range(p) for c in range(p)
             if (a-c)%p==0 and (b-c)%p==0]
        assert len(ker)==p and set(ker)=={(k,k,k) for k in range(p)}
        ans.append(dict(p=p,relation_verified=True,orientation_kernel_size=p,
                        kernel='span(1,1,1)',central_witness=(1,0)))
    return ans

if __name__=='__main__':
    out=dict(unitriangular_certificates=[ut_case(p) for p in (2,3,5)],
             abelian_filling=filling_case(),weakened_presentation=abelian_examples(),
             interpretation='Finite certificates prove stated finite facts; finite centralizers alone do not prove an inverse-limit centralizer assertion.')
    print(json.dumps(out,indent=2))
