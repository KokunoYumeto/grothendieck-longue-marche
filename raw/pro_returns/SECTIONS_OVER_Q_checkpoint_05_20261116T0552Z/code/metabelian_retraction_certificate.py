"""Finite exact checks for A.71's complement torsor and arithmetic retraction.
Cases: S3 acted on by S3; A4 acted on by S4 (nontrivial quotient action).
"""
from itertools import permutations, product

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
    r=[0]*len(a)
    for i,j in enumerate(a): r[j]=i
    return tuple(r)
def conjugate(a,b): return compose(compose(a,b),inverse(a))
def sign(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def powers(g):
    one=tuple(range(len(g))); out=[one]; p=g
    while p!=one:
        out.append(p); p=compose(p,g)
    return out
def closure(gens, one):
    out={one}; todo=[one]
    while todo:
        a=todo.pop()
        for b in gens:
            c=compose(a,b)
            if c not in out: out.add(c); todo.append(c)
    return out

reports=[]
for name,degree,even_only,cyc in [
    ("S3 with inner S3 action",3,False,(1,0,2)),
    ("A4 with S4 action",4,True,(1,2,0,3)),
]:
    G=list(permutations(range(degree)))
    M=[a for a in G if not even_only or sign(a)==1]
    one=tuple(range(degree))
    comms=[compose(compose(compose(a,b),inverse(a)),inverse(b)) for a,b in product(M,repeat=2)]
    D=closure(comms,one)
    C=powers(cyc)
    assert len(D)*len(C)==len(M)
    assert all(compose(a,b)==compose(b,a) for a,b in product(D,repeat=2))
    ab={}
    for d,c in product(D,C):
        ab[compose(d,c)]=c
    assert len(ab)==len(M)
    delta={}
    for g in G:
        target={conjugate(g,c) for c in C}
        candidates=[d for d in D if {conjugate(d,c) for c in C}==target]
        assert len(candidates)==1
        delta[g]=candidates[0]
    cocycle_checks=0
    for g,h in product(G,repeat=2):
        assert delta[compose(g,h)]==compose(delta[g],conjugate(g,delta[h]))
        cocycle_checks+=1
    def actionC(g,c): return ab[conjugate(g,c)]
    def domain_mul(a,b):
        c,g=a; d,h=b
        return compose(c,actionC(g,d)),compose(g,h)
    def ambient_mul(a,b):
        m,g=a; n,h=b
        return compose(m,conjugate(g,n)),compose(g,h)
    def retract_section(a):
        c,g=a
        return compose(c,inverse(delta[g])),g
    elements=list(product(C,G))
    images={retract_section(a) for a in elements}
    assert len(images)==len(elements)
    for a in elements:
        m,g=retract_section(a)
        assert (ab[m],g)==a
    hom_checks=0
    for a,b in product(elements,repeat=2):
        assert retract_section(domain_mul(a,b))==ambient_mul(retract_section(a),retract_section(b))
        hom_checks+=1
    reports.append((name,len(M),len(D),len(C),len(G),cocycle_checks,hom_checks))
print("A.71 exact finite arithmetic retraction certificate")
for name,mo,do,co,go,cc,hc in reports:
    print(name)
    print(" orders M,D,C,G:",mo,do,co,go)
    print(" complement-cocycle identities:",cc)
    print(" arithmetic homomorphism identities:",hc)
print("All right-inverse and injectivity checks passed.")

