"""Exact rational certificate for the weight-four obstruction in task B.3.P7.

The Lie algebra is embedded in the free associative algebra.  A degree-k
special derivation of L(x,y,z) is D(x_i)=[x_i,a_i], |a_i|=k,
and D(x+y+z)=0.  For k>1 this is a unique representative of an
outer special derivation of the four-punctured sphere (set a_4=0).
All ranks below are over Q; no finite-field rank heuristic is used.
"""
from itertools import product
from functools import lru_cache
from math import gcd,lcm
from pathlib import Path
import sympy as s

def add(a,b,scale=1):
    c=dict(a)
    for w,v in b.items():
        c[w]=c.get(w,0)+scale*v
        if not c[w]: del c[w]
    return c

def mul(a,b):
    c={}
    for u,x in a.items():
        for v,y in b.items():
            w=u+v;c[w]=c.get(w,0)+x*y
    return {w:v for w,v in c.items() if v}

def bracket(a,b): return add(mul(a,b),mul(b,a),-1)
def lyndon(w): return all(w<w[i:] for i in range(1,len(w)))
def lyndons(r,k): return [w for w in product(range(r),repeat=k) if lyndon(w)]

@lru_cache(None)
def lie(w):
    if len(w)==1:return {w:s.Integer(1)}
    for i in range(1,len(w)):
        if lyndon(w[i:]):return bracket(lie(w[:i]),lie(w[i:]))
    raise AssertionError(w)

def lname(w,letters="xyz"):
    if len(w)==1:return letters[w[0]]
    for i in range(1,len(w)):
        if lyndon(w[i:]):return "["+lname(w[:i],letters)+","+lname(w[i:],letters)+"]"

def coeffvec(p,words):return s.Matrix([p.get(w,0) for w in words])
def dvec(D,r,k):
    words=list(product(range(r),repeat=k+1))
    return s.Matrix.vstack(*(coeffvec(p,words) for p in D))

def apply_der(D,p):
    out={}
    for w,v in p.items():
        for i,j in enumerate(w):
            q={w[:i]+u+w[i+1:]:v*c for u,c in D[j].items()}
            out=add(out,q)
    return out

def dbracket(D,E):
    return tuple(add(apply_der(D,e),apply_der(E,d),-1) for d,e in zip(D,E))

def substitute(p,images):
    out={}
    for w,v in p.items():
        q={():v}
        for j in w:q=mul(q,images[j])
        out=add(out,q)
    return out

def primitive(v):
    den=lcm(*(int(a.q) for a in v))
    vals=[int(a*den) for a in v]
    g=gcd(*vals)
    vals=[a//g for a in vals]
    if next(a for a in vals if a)!=abs(next(a for a in vals if a)):
        vals=[-a for a in vals]
    return s.Matrix(vals)

def special_matrix(r,k):
    bs=lyndons(r,k);words=list(product(range(r),repeat=k+1))
    cols=[coeffvec(bracket(lie((i,)),lie(w)),words)
          for i in range(r) for w in bs]
    return bs,s.Matrix.hstack(*cols)

def main():
    for r in (2,3):
        print("Witt dimensions r =",r,":",
              [len(lyndons(r,k)) for k in range(1,6)])
    bs,M=special_matrix(3,4)
    ns=[primitive(v) for v in M.nullspace()]
    assert M.rank()==48 and len(ns)==6
    print("Four-punctured sphere, weight 4: variables",M.cols,
          "constraint rank",M.rank(),"outer special dimension",len(ns))
    _,M2=special_matrix(2,4)
    assert M2.rank()==6 and len(M2.nullspace())==0
    print("Three-punctured sphere, weight 4: variables",M2.cols,
          "constraint rank",M2.rank(),"outer special dimension",len(M2.nullspace()))
    x,y,z=[lie((i,)) for i in range(3)]
    a=(bracket(x,y),bracket(y,x),{})
    b=({},bracket(y,z),bracket(z,y))
    @lru_cache(None)
    def bword(w):
        if len(w)==1:return (a,b)[w[0]]
        for i in range(1,len(w)):
            if lyndon(w[i:]):return dbracket(bword(w[:i]),bword(w[i:]))
        raise AssertionError
    braid_words=lyndons(2,4)
    B=s.Matrix.hstack(*(dvec(bword(w),3,4) for w in braid_words))
    assert B.rank()==3
    print("Weight-4 braid subspace dimension:",B.rank())
    chosen=None
    for v in ns:
        aa=[]
        for i in range(3):
            q={}
            for j,w in enumerate(bs):q=add(q,lie(w),v[i*len(bs)+j])
            aa.append(q)
        D=tuple(bracket(lie((i,)),aa[i]) for i in range(3))
        V=dvec(D,3,4)
        if s.Matrix.hstack(B,V).rank()>3:
            chosen=(v,aa,D);break
    assert chosen is not None
    v,aa,D=chosen
    assert not add(add(D[0],D[1]),D[2])
    print("Explicit non-braid special derivation: D(x_i)=[x_i,a_i], a_4=0")
    for i in range(3):
        terms=[f"({v[i*len(bs)+j]})*{lname(w)}"
               for j,w in enumerate(bs) if v[i*len(bs)+j]]
        print("a_"+str(i+1)+" =", " + ".join(terms) or "0")
    print("Rank with candidate adjoined:",s.Matrix.hstack(B,dvec(D,3,4)).rank())
    # Forget x,y,z separately; the two retained generators are relabelled 0,1.
    for killed in range(3):
        keep=[i for i in range(3) if i!=killed]
        images=[{} for _ in range(3)]
        for j,i in enumerate(keep):images[i]=lie((j,))
        target=tuple(substitute(D[i],images) for i in keep)
        assert all(not q for q in target)
        print("Forget cusp",killed+1,": zero derivation")
    # Forget cusp 4: set z=-x-y.  The induced derivation is inner.
    images=[lie((0,)),lie((1,)),{(0,):-1,(1,):-1}]
    target=(substitute(D[0],images),substitute(D[1],images))
    bb=lyndons(2,4)
    I=s.Matrix.hstack(*(dvec(tuple(bracket(lie((i,)),lie(w)) for i in range(2)),2,4)
                        for w in bb))
    sol=I.gauss_jordan_solve(dvec(target,2,4))[0]
    assert I*sol==dvec(target,2,4)
    print("Forget cusp 4: inner, common tangential conjugator =",
          " + ".join(f"({sol[j]})*{lname(w,'xy')}" for j,w in enumerate(bb) if sol[j]) or "0")
    print("PASS: common kernel dimension 6 exceeds braid dimension 3.")

if __name__=="__main__":main()
