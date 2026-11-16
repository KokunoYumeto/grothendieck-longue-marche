"""Structural nilpotence gate for the exact rank129 Ferrari homology target.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json

ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'ferrari_rank129.npz');X=D['X'];n=129;I=np.eye(n,dtype=np.int16)
def mm(A,B):return A@B%3
def mp(*gg):
    M=I
    for g in gg:M=mm(M,g)
    return M
def power(M,k):
    out=I
    while k:
        if k&1:out=mm(out,M)
        M=mm(M,M);k//=2
    return out
def inv(M):
    rows=np.concatenate((M.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(rows[j:,j])[0]);rows[[j,k]]=rows[[k,j]]
        if rows[j,j]==2:rows[j]=2*rows[j]%3
        inds=np.flatnonzero(rows[:,j]);inds=inds[inds!=j]
        rows[inds]=(rows[inds]-rows[inds,j,None]*rows[j])%3
    return rows[:,n:]
def comm(g,h):return mp(g,h,inv(g),inv(h))
def order(g,bound=256):
    h=I
    for k in range(1,bound+1):
        h=mm(h,g)
        if np.array_equal(h,I):return k
    return None
def conj(g,h):return mp(g,h,inv(g))
reports=[]
for ii,jj in ((0,1),(2,3),(3,4)):
    g,h=X[ii],X[jj];z=inv(mm(g,h));c=comm(g,h)
    seeds=[('[[x,y],x[x,y]x^-1]',comm(c,conj(g,c))),
           ('[[x,y],y[x,y]y^-1]',comm(c,conj(h,c))),
           ('[[x^4,y^4],[y^4,z^4]]',comm(comm(power(g,4),power(h,4)),comm(power(h,4),power(z,4))))]
    data=[];witness=None
    for name,s in seeds:
        r=order(s);data.append({'word':name,'order_up_to256':r})
        if r and r%2==0:
            a=power(s,r//2);assert np.array_equal(power(a,2),I)
            for cname,u in [('x',g),('y',h),('xy',mm(g,h)),('xy^-1',mm(g,inv(h)))]:
                b=conj(u,a);q=order(mm(a,b))
                if q and q&(q-1):
                    witness={'source_second_derived_word':name,'word_order':r,
                             'involution_power':r//2,'conjugating_word':cname,
                             'two_involutions_product_order':q,
                             'non_two_part':q//(q&-q)}
                    break
        if witness:break
    reports.append({'pair':[ii+1,jj+1],'seed_orders':data,'second_derived_nonnilpotence_witness':witness})
print(json.dumps({'target_dimension':n,'pair_gate_reports':reports,
 'criterion':'In a finite nilpotent group all involutions lie in the same2-Sylow subgroup, so a product of two involutions has2-power order. Both displayed involutions lie in the second derived pair subgroup.',
 'scope':'Actual finite homology quotient and source words, no candidate GT lift.'},indent=2))
