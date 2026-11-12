# Independent re-derivation of finite claims in LM3 (B.4, B.5/D.20, D.2, B.15), stdlib only.
from itertools import permutations
from fractions import Fraction
# --- F_8 = F_2[t]/(t^3+t+1), elements as 3-bit ints
def gmul(a,b):
    r=0
    for i in range(3):
        if (b>>i)&1: r^= a<<i
    for i in (4,3):
        if (r>>i)&1: r^= 0b1011<<(i-3)
    return r
def mmul(A,B):
    a,b,c,d=A; e,f,g,h=B
    return (gmul(a,e)^gmul(b,g), gmul(a,f)^gmul(b,h), gmul(c,e)^gmul(d,g), gmul(c,f)^gmul(d,h))
I=(1,0,0,1)
X=(1,2,0,1)   # [[1,t],[0,1]]
Y=(0,1,1,1)   # [[0,1],[1,1]]
def order(M):
    k,P=1,M
    while P!=I: P=mmul(P,M); k+=1
    return k
print("ord X",order(X),"ord Y",order(Y))
G={I}; frontier=[I]
while frontier:
    nf=[]
    for g in frontier:
        for s in (X,Y):
            h=mmul(g,s)
            if h not in G: G.add(h); nf.append(h)
    frontier=nf
det=lambda M: gmul(M[0],M[3])^gmul(M[1],M[2])
allSL=[(a,b,c,d) for a in range(8) for b in range(8) for c in range(8) for d in range(8) if det((a,b,c,d))==1]
print("generated",len(G),"|SL2(F8)|",len(allSL), "equal", G==set(allSL))
# simplicity: normal closure of every nonidentity element is everything
inv={g:next(h for h in G if mmul(g,h)==I) for g in G}
def normal_closure(x):
    N={I,x}; changed=True
    while changed:
        changed=False
        cur=list(N)
        for n in cur:
            for g in G:
                c=mmul(mmul(g,n),inv[g])
                if c not in N: N.add(c); changed=True
            for m in cur:
                p=mmul(n,m)
                if p not in N: N.add(p); changed=True
    return N
# check one representative per conjugacy class
seen=set(); simple=True
for x in G:
    if x==I or x in seen: continue
    cls={mmul(mmul(g,x),inv[g]) for g in G}; seen|=cls
    if len(normal_closure(x))!=len(G): simple=False
print("simple",simple)
# PSL2(F_p) orders near 504
print({p:p*(p*p-1)//2 for p in (5,7,11,13)})
# --- A5 from (12345),(123), perfectness
def pmul(p,q): return tuple(p[q[i]] for i in range(5))
a=(1,2,3,4,0); b=(1,2,0,3,4)
H={tuple(range(5))}; fr=[tuple(range(5))]
while fr:
    nf=[]
    for g in fr:
        for s in (a,b):
            h=pmul(g,s)
            if h not in H: H.add(h); nf.append(h)
    fr=nf
pinv=lambda p: tuple(sorted(range(5),key=lambda i:p[i]))
comm={pmul(pmul(x,y),pmul(pinv(x),pinv(y))) for x in H for y in H}
D={tuple(range(5))}; fr=list(comm)
D|=comm
changed=True
while changed:
    changed=False
    for x in list(D):
        for y in list(D):
            z=pmul(x,y)
            if z not in D: D.add(z); changed=True
print("A5 order",len(H),"derived",len(D))
# --- discriminant of t^3+pt+q: -4p^3-27q^2 with p=0,q=-2
print("disc t^3-2:", -4*0**3-27*(-2)**2)
# --- B.15 alpha: alpha_2=0, alpha_p=1 (p odd): CRT mod 2^k*3^k
for k in range(1,6):
    m2,m3=2**k,3**k
    r=next(x for x in range(m2*m3) if x%m2==0 and x%m3==1)
    print(k, m2*m3, r)
