#!/usr/bin/env python3
"""Independent normalized bar-complex computation for the H3:C2 norm obstruction."""
from itertools import product

elts=list(product(range(3),repeat=3)); ident=(0,0,0)
def mul(g,h):
    a,b,c=g; A,B,C=h
    return ((a+A)%3,(b+B)%3,(c+C+a*B)%3)
def invol(g):
    a,b,c=g
    return ((-a)%3,(-b)%3,c)
assert all(invol(mul(g,h))==mul(invol(g),invol(h)) for g in elts for h in elts)
nonzero=[g for g in elts if g!=ident]
def orbit_key(g): return min(g,invol(g))
onekeys=sorted({orbit_key(g) for g in nonzero})
pairkeys=sorted({min((g,h),(invol(g),invol(h))) for g in nonzero for h in nonzero})
index={key:i for i,key in enumerate(pairkeys)}
def pindex(g,h):
    if g==ident or h==ident: return None
    return index[min((g,h),(invol(g),invol(h)))]

n=len(index); mask=(1<<n)-1
def plus(A,B):
    a,b=A; c,d=B
    az=mask^(a|b); bz=mask^(c|d)
    return ((az&c)|(a&bz)|(b&d),(az&d)|(b&bz)|(a&c))
def sparse(terms):
    counts={}
    for i,c in terms:
        if i is not None: counts[i]=(counts.get(i,0)+c)%3
    return (sum(1<<i for i,c in counts.items() if c==1),
            sum(1<<i for i,c in counts.items() if c==2))
def insert(row,basis):
    while row[0]|row[1]:
        pivot=((row[0]|row[1])&-(row[0]|row[1])).bit_length()-1
        coeff=1 if (row[0]>>pivot)&1 else 2
        if pivot not in basis:
            basis[pivot]=row if coeff==1 else (row[1],row[0])
            return
        base=basis[pivot]
        row=plus(row,(base[1],base[0]) if coeff==1 else base)

d2={}
for g,h,k in product(nonzero,repeat=3):
    insert(sparse([(pindex(h,k),1),(pindex(mul(g,h),k),-1),
                   (pindex(g,mul(h,k)),1),(pindex(g,h),-1)]),d2)
d1={}
for key in onekeys:
    terms=[]
    for pair,i in index.items():
        g,h=pair; gh=mul(g,h)
        value=int(orbit_key(h)==key)+int(orbit_key(g)==key)-int(gh!=ident and orbit_key(gh)==key)
        terms.append((i,value))
    insert(sparse(terms),d1)
assert len(onekeys)==14 and n==340
assert len(d1)==14 and len(d2)==326 and n-len(d2)-len(d1)==0
print('PASS: C2-invariant normalized bar complex: dim C1=14, dim C2=340')
print('PASS: rank d1=14, rank d2=326; H2(H3,F3)^C2=0')

G=[(g,e) for g in elts for e in range(2)]; eG=(ident,0)
def gmul(g,h):
    x,e=g; y,f=h
    return (mul(x,invol(y) if e else y),(e+f)%2)
def inv(g): return next(h for h in G if gmul(g,h)==eG and gmul(h,g)==eG)
def subgroup(gens):
    S={eG}; todo=[eG]
    while todo:
        g=todo.pop()
        for h in gens:
            v=gmul(g,h)
            if v not in S: S.add(v); todo.append(v)
    return S
def comm(g,h): return gmul(gmul(g, h),gmul(inv(g),inv(h)))
x=((1,0,0),0); y=((0,1,0),0); c=(ident,1)
assert len(subgroup([x,y,c]))==54
for inertia in (x,y,gmul(x,y)):
    I=subgroup([inertia])
    tau=next(g for g in G if g!=eG and gmul(g,g)==eG
             and gmul(gmul(g,inertia),g)==inv(inertia))
    H=subgroup([inertia,tau])
    derived=subgroup([comm(g,h) for g in H for h in H])
    assert len(H)==6 and len(derived)==3
    core=set(H)
    for g in G: core &= {gmul(gmul(g,h),inv(g)) for h in H}
    assert core=={eG}
print('PASS: order54 group; each boundary stabilizer is S3 with trivial core and index nine')
