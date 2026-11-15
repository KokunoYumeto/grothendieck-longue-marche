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

results=[]
for uy in [1,2,3,16,17,18,256,257,273]:
    y=enc(uy,0,qy);w=mul(x,y)
    y3=power(y,3);v3=dec(y3)[0]
    rr=rank([act[q][v3] for q in range(75)])
    if rr!=12:continue
    candidates=[]
    for a in roots:
        for k in range(4096):
            if act[qx][k]!=k or Ls[a][k]!=k:continue
            if alpha(x,a,k)!=x:continue
            candidates.append((a,k))
    solved=[];count_f=0;count_h=0;both=0;candidate_table=[]
    for a,k in candidates:
        py=alpha(y,a,k);pw=alpha(w,a,k)
        ff=[];hh=[]
        for u in range(4096):
            f=enc(u,0,qf)
            if conj(inv(f),y)==py and mul(f,alpha(f,a,k))==one:ff.append(u)
            h=enc(u,0,qh)
            if conj(inv(h),w)==pw and mul(h,alpha(h,a,k))==one:hh.append(u)
        count_f+=bool(ff);count_h+=bool(hh)
        candidate_table.append(dict(a=a,k=k,f_options=2*len(ff),h_options=2*len(hh)))
        if ff and hh:
            both+=1;solved.append(dict(a=a,k=k,f=ff[0],h=hh[0],f_options=2*len(ff),h_options=2*len(hh)))
    results.append(dict(y_vector=uy,normal_generation_rank=rr,candidate_involutions=len(candidates),
                        pass_f=count_f,pass_h=count_h,pass_both=both,solutions=solved,
                        candidate_table=candidate_table))
    print(json.dumps(results[-1]),flush=True)
out=dict(group_order=75*8192,field_polynomial='z^4+z+1',theta=theta,zeta5=zeta,
         representation_checks=True,results=results)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
