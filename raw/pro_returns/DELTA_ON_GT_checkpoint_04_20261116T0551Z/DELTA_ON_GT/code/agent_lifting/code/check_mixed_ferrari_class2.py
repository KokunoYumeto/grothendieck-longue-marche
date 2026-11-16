"""Exact class-two boundary/compact mixed quotient and L action.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
Uses H=F3^3+F3^2 and Z=H_boundary tensor H_compact, with BCH.
"""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parents[1]
previous=json.loads((HERE/'records'/'mixed_ferrari_quotient.json').read_text())
HM=(3,5,6,7,7);ZM=(4,4,2,2,1,1)
V0=(0,)*5;Z0=(0,)*6;N0=(V0,Z0)
I=tuple(int(i==j)for i in range(5)for j in range(5))
def sign(b,ms):return tuple(1 if (b&m).bit_count()%2==0 else 2 for m in ms)
def bracket(v,w):return tuple((v[i]*w[3+j]-w[i]*v[3+j])%3 for i in range(3)for j in range(2))
def nm(n,m):
    v,z=n;w,t=m;b=bracket(v,w)
    return (tuple((v[i]+w[i])%3 for i in range(5)),tuple((z[i]+t[i]+2*b[i])%3 for i in range(6)))
def ni(n):return(tuple(-x%3 for x in n[0]),tuple(-x%3 for x in n[1]))
def da(b,n):return(tuple(x*s%3 for x,s in zip(n[0],sign(b,HM))),tuple(x*s%3 for x,s in zip(n[1],sign(b,ZM))))
def em(g,h):
    n,b=g;m,c=h
    return nm(n,da(b,m)),b^c
E0=(N0,0)
def ep(*gg):
    out=E0
    for g in gg:out=em(out,g)
    return out
def ei(g):return da(g[1],ni(g[0])),g[1]
t=(((V0,Z0),1),(((1,0,0,1,0),Z0),2),(((0,1,1,0,1),Z0),4))
assert all(em(g,g)==E0 for g in t)
aim=(ep(t[0],t[1],t[0]),t[0],t[2])
bim=(t[2],t[1],ep(t[2],t[0],t[2]))
xi1=em(t[1],t[0]);cim=tuple(ep(xi1,g,ei(xi1))for g in aim)

def mv(M,v):return tuple(sum(M[5*i+j]*v[j]for j in range(5))%3 for i in range(5))
def mz(M,z):
    return tuple(sum(M[5*i+k]*M[5*(3+j)+(3+l)]*z[2*k+l]
                     for k in range(3)for l in range(2))%3 for i in range(3)for j in range(2))
def act(M,n):return mv(M,n[0]),mz(M,n[1])
def mm(A,B):return tuple(sum(A[5*i+k]*B[5*k+j]for k in range(5))%3 for i in range(5)for j in range(5))
def mi(M):
    rows=[list(M[5*i:5*i+5])+[int(i==j)for j in range(5)]for i in range(5)]
    for j in range(5):
        k=next(k for k in range(j,5)if rows[k][j]);rows[j],rows[k]=rows[k],rows[j]
        u=rows[j][j];rows[j]=[u*x%3 for x in rows[j]]
        for k in range(5):
            if k!=j:
                u=rows[k][j];rows[k]=[(x-u*y)%3 for x,y in zip(rows[k],rows[j])]
    ans=tuple(x for row in rows for x in row[5:]);assert mm(M,ans)==I
    return ans
G0=(N0,I)
def gm(g,h):return nm(g[0],act(g[1],h[0])),mm(g[1],h[1])
def gi(g):
    M=mi(g[1]);return act(M,ni(g[0])),M
def gp(*gg):
    out=G0
    for g in gg:out=gm(out,g)
    return out
def power(g,n):
    if n<0:g=gi(g);n=-n
    out=G0
    while n:
        if n&1:out=gm(out,g)
        g=gm(g,g);n//=2
    return out
def conjugation(n,M,sigma,g):
    nn,b=g;return ep((n,0),(act(M,nn),sigma[b]),(ni(n),0))

gens=[];records=[]
for k,(label,images)in enumerate(zip(('a','b','c'),(aim,bim,cim))):
    old=previous[label+'_matrix_6x6']
    M=tuple(old[6*i+j]for i in range(5)for j in range(5))
    u=tuple(old[6*i+5]for i in range(5))
    sigma={int(a):b for a,b in previous['base_V_actions'][k].items()}
    residual=[]
    for inp,out in zip(t,images):
        got=conjugation((u,Z0),M,sigma,inp)
        assert got[1]==out[1] and got[0][0]==out[0][0]
        residual.append(tuple((out[0][1][j]-got[0][1][j])%3 for j in range(6)))
    z=[]
    for j in range(6):
        k0=next(k0 for k0 in range(3)if sign(sigma[t[k0][1]],ZM)[j]==2)
        z.append(2*residual[k0][j]%3)
    n=(u,tuple(z))
    assert all(conjugation(n,M,sigma,inp)==out for inp,out in zip(t,images))
    gens.append((n,M))
    records.append({'name':label,'translation_H':u,'translation_mixed_center':z,'linear_H_5x5':M})
a,b,c=gens
assert gp(a,b,a)==gp(b,a,b)
assert gp(b,c,b)==gp(c,b,c)
assert gm(a,c)==gm(c,a)
assert power(gp(a,b,c),4)==G0

def inner(g):
    n,b=g;sg=sign(b,HM)
    return n,tuple(sg[i] if i==j else 0 for i in range(5)for j in range(5))
assert power(gp(a,b,c),2)==inner(t[0])
assert gp(c,gi(a))==inner(xi1)
assert gp(a,b,a,gi(c),gi(b),gi(a))==inner(em(t[2],t[0]))
X=(power(a,2),power(b,2),power(c,2),power(gp(a,b,a),2),power(gp(c,b,c),2))
out={'coefficient_field':3,'H_dimension':5,'mixed_center_dimension':6,
     'C_quotient_order':8*3**11,'H_character_masks':HM,'center_character_masks':ZM,
     'representation':'(n,M) in N_BCH semidirect GL(H), n=(H5,center6), bracket B tensor P',
     'generators':records,
     'five_Xi':[{'H':g[0][0],'center':g[0][1],'M':g[1]}for g in X],
     'all_L_relators_exact':True,'C_involution_and_Ferrari_words_exact':True,
     'scope':'Actual L quotient, with exact nonlinear class-two cocycles. Only the L-stable central subspace wedge2(boundary)+wedge2(compact) was killed; the six mixed coordinates are retained.'}
(HERE/'records'/'mixed_ferrari_class2.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':print(json.dumps(out,indent=2))
