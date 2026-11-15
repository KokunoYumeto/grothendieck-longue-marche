#!/usr/bin/env python3
"""Search a specified extraspecial 2-extension of Q75 for (A--I).

P has order 2^13 and minus type. Q75 acts on F16^3, and the
central bilinear cocycle is Tr_F16/F2(theta sum u_j v_j^4).
All automorphisms above (v,i)->(-v,i) are enumerated algebraically.
"""
import json
from pathlib import Path

def fm(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&16:a^=19
    return r
F=[[fm(a,b) for b in range(16)] for a in range(16)]
def fp(a,n):
    r=1
    while n:
        if n&1:r=F[r][a]
        a=F[a][a];n>>=1
    return r
four=[fp(a,4) for a in range(16)]
tr=[a^fp(a,2)^fp(a,4)^fp(a,8) for a in range(16)]
assert set(tr)=={0,1}
zeta=fp(2,3); roots=[fp(zeta,j) for j in range(5)]
theta=2;assert theta^four[theta]==1
def coords(u):return (u&15,(u>>4)&15,(u>>8)&15)
def pack(v):return v[0]|(v[1]<<4)|(v[2]<<8)
def fbil(u,v):return tr[F[theta][F[u&15][four[v&15]]^F[(u>>4)&15][four[(v>>4)&15]]^F[(u>>8)&15][four[(v>>8)&15]]]]
basis=[1<<i for i in range(12)]
row=[sum(fbil(u,v)<<j for j,v in enumerate(basis)) for u in range(4096)]
def bil(u,v):return (row[u]&v).bit_count()&1
quad=[bil(u,u) for u in range(4096)]
def t(v):return (-v[1]%5,(v[0]-v[1])%5)
def tp(v,n):
    for _ in range(n%3):v=t(v)
    return v
qs=[(a,b,i) for i in range(3) for b in range(5) for a in range(5)]
qi={v:i for i,v in enumerate(qs)}
def qm(q,r):
    a,b,i=q;c,d,j=r;c,d=tp((c,d),i)
    return ((a+c)%5,(b+d)%5,(i+j)%3)
qmul=[[qi[qm(q,r)] for r in qs] for q in qs]
qid=qi[(0,0,0)]
qinv=[next(j for j in range(75) if qmul[i][j]==qid) for i in range(75)]
qa=[qi[(-a%5,-b%5,i)] for a,b,i in qs]
def act_raw(q,u):
    a,b,i=q;v=coords(u);vv=tuple(v[(j-i)%3] for j in range(3))
    ls=[tp((a,b),-j)[0] for j in range(3)]
    return pack(tuple(F[roots[ls[j]]][vv[j]] for j in range(3)))
act=[[act_raw(q,u) for u in range(4096)] for q in qs]
for q in range(75):
    assert all(quad[act[q][u]]==quad[u] for u in range(4096))
    for u in basis:
        for v in basis:assert bil(act[q][u],act[q][v])==bil(u,v)
for q in range(75):
    for r in range(75):
        for u in basis:assert act[q][act[r][u]]==act[qmul[q][r]][u]

def enc(u,c,q):return q*8192+u+c*4096
def dec(g):q,p=divmod(g,8192);return p&4095,p>>12,q
one=enc(0,0,qid)
def mul(g,h):
    u,c,q=dec(g);v,d,r=dec(h);v=act[q][v]
    return enc(u^v,c^d^bil(u,v),qmul[q][r])
def inv(g):
    u,c,q=dec(g);qq=qinv[q]
    return enc(act[qq][u],c^quad[u],qq)
def power(g,n):
    r=one
    while n:
        if n&1:r=mul(r,g)
        g=mul(g,g);n>>=1
    return r
def conj(g,h):return mul(mul(g,h),inv(g))
Ls={a:[pack(tuple(F[a][four[v]] for v in coords(u))) for u in range(4096)] for a in roots}
def psi(g,a):
    u,c,q=dec(g);return enc(Ls[a][u],c^quad[u],qa[q])
def alpha(g,a,k):return conj(enc(k,0,qid),psi(g,a))

# The displayed semilinear maps are checked on every P element and
# every pair of its basis vectors; bilinearity handles all products.
for a in roots:
    for u in range(4096):assert Ls[a][Ls[a][u]]==u and quad[Ls[a][u]]==quad[u]
    for u in basis:
        for v in basis:
            assert bil(Ls[a][u],Ls[a][v])^bil(u,v)==quad[u^v]^quad[u]^quad[v]
    for q in range(75):
        for u in basis:assert Ls[a][act[q][u]]==act[qa[q]][Ls[a][u]]

qx=qi[(0,0,1)];qy=qi[(1,0,1)]
qf=qi[(3,4,0)];qh=qi[(4,3,0)]
x=enc(0,0,qx)
def rank(vs):
    b={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in b:v^=b[j]
            else:b[j]=v;break
    return len(b)


y=enc(264,0,qy);w=mul(x,y);w3=power(w,3)
print('y coords',coords(264),'w3',dec(w3),'Q(w3)',quad[dec(w3)[0]],'w order',[j for j in range(1,13) if power(w,j)==one])
for a in roots:
 for k in [kk for kk in range(4096) if act[qx][kk]==kk and Ls[a][kk]==kk]:
  pw=alpha(w,a,k);stat={}
  for u in range(4096):
   h=enc(u,0,qh)
   if conj(inv(h),w)==pw:
    nn=mul(h,alpha(h,a,k));v,c,q=dec(nn);stat[(v,c,q)]=stat.get((v,c,q),0)+2
  print('a,k',a,k,'norm distribution',stat)
