#!/usr/bin/env python3
"""Produce fixed exact norm witnesses for all seven F2-conjugacy representatives.
The final norm verifier is a separate file and does not use this solver.
"""
from pathlib import Path
from math import comb
import json,time
import sympy as sp
from A_F4_rank_one_search import MODS,configure,polynomial_counts,orders,unit_info
from A_rank_one_arithmetic import Field,eta,times,ZERO
from A_F4_large_theta_canonical import IndependentField
from A_theta_F4_moduli_witnesses import trim,padd,pscale,pmul,peval

ROOT=Path(__file__).parent

def kernel(mat,F):
    a=[row[:] for row in mat];m=len(a);n=len(a[0]);piv=[];r=0
    for c in range(n):
        s=next((s for s in range(r,m) if a[s][c]),None)
        if s is None:continue
        a[r],a[s]=a[s],a[r];inv=F.inv(a[r][c]);a[r]=[F.mul(x,inv) for x in a[r]]
        for j in range(m):
            if j==r or not a[j][c]:continue
            v=a[j][c];a[j]=[x^F.mul(v,y) for x,y in zip(a[j],a[r])]
        piv.append(c);r+=1
    free=[c for c in range(n) if c not in piv];assert len(free)==1,(r,n)
    v=[0]*n;v[free[0]]=1
    for j,c in reversed(list(enumerate(piv))):
        v[c]=0
        for k in range(c+1,n):v[c]^=F.mul(a[j][k],v[k])
    for row in mat:
        val=0
        for x,y in zip(row,v):val^=F.mul(x,y)
        assert val==0
    return v,r

def norm_witness(rec):
    e=rec['field_degree_over_F2'];mod=rec['field_modulus'];gen=rec['field_generator']
    F=IndependentField(e,mod,gen);ac=rec['A'];bc=rec['B'];t,y=rec['point'];n=rec['exact_order'];d=(n-1)//2
    inverse=F.inv(t);ys=[y]
    assert F.mul(y,y)^y==F.mul(ac,F.pow(t,3))^F.mul(bc,t)^inverse
    for j in range(1,n):
        c=F.pow(inverse,j+1)
        if j<=3:c^=F.mul(ac,F.pow(t,3-j))
        if j==1:c^=bc
        if j%2==0:c^=F.mul(ys[j//2],ys[j//2])
        ys.append(c)
    basis=[]
    for k in range(d+1):basis.append([F.pow(t,k-j) if j<=k and comb(k,j)%2 else 0 for j in range(n)])
    for k in range(d-1):
        col=[]
        for j in range(n):
            v=0
            for r in range(min(k,j)+1):
                if comb(k,r)%2:v^=F.mul(F.pow(t,k-r),ys[j-r])
            col.append(v)
        basis.append(col)
    mat=[[col[j] for col in basis] for j in range(n)]
    v,rank=kernel(mat,F);A=v[:d+1];B=v[d+1:];assert B[0]
    iv=F.inv(B[0]);A=pscale(A,iv,F);B=pscale(B,iv,F)
    c=F.mul(A[-1],A[-1]);assert len(A)==d+1 and c
    norm=padd(pmul([0,1],padd(pmul(A,A,F),pmul(A,B,F)),F),pmul(pmul(B,B,F),[1,0,bc,0,ac],F))
    target=[F.mul(c,F.pow(t,n-j)) if comb(n,j)%2 else 0 for j in range(n+1)]
    assert norm==target
    assert peval(A,t,F)^F.mul(peval(B,t,F),y)==0
    assert peval(B,t,F) and peval(B,0,F)
    return {**rec,'numerator_A':A,'numerator_B':B,'norm_scalar':c,
            'denominator_power':d,'jet_matrix_shape':[n,n-1],'jet_rank':rank}

def main():
    start=time.time();counts=polynomial_counts();search=json.loads((ROOT/'A_F4_rank_one_search.json').read_text())
    given={tuple(r['F4_coefficients']):r['witness'] for r in search['curves'] if 'witness' in r}
    targets=[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(2,3)];answer=[]
    for key in targets:
        rec=given.get(key)
        if rec is None:
            for e in (2,4,6,8):
                F=Field(e,MODS[e]);A,B=configure(F,*key);N,Nc=orders(counts[key],e//2);odd=N
                while odd%2==0:odd//=2
                for x in range(1,F.q):
                    ok,y=F.point(x)
                    if ok!=1:continue
                    D=eta(x,y)
                    if times(D,odd).key()!=ZERO.key():continue
                    n=odd
                    for p in sp.factorint(n):
                        while n%p==0 and times(D,n//p).key()==ZERO.key():n//=p
                    if n==1:continue
                    ui=unit_info(n)
                    if ui['index_of_doubling_and_sign']!=1:continue
                    rec={'field_degree_over_F2':e,'field_modulus':MODS[e],
                         'field_generator':F.generator,'alpha':F.alpha,'A':A,'B':B,
                         'point':[x,y],'mumford_theta':D.lists(),'exact_order':n,
                         'Jacobian_order':N,'curve_count_expected':Nc,**ui};break
                if rec:break
        assert rec,key
        out=norm_witness(rec);out['F4_coefficients']=list(key);answer.append(out)
        print('NORM',key,'n',out['exact_order'],'field',2**out['field_degree_over_F2'],'A',out['numerator_A'],'B',out['numerator_B'],flush=True)
    out={'status':'FIXED positive norm witnesses, pending independent verification',
         'curve':'y²+y=A*x³+B*x+1/x; Y=x*y; Btheta=W0',
         'encoding':'Binary polynomial field; F4 symbols0,1,2=alpha,3=alpha²',
         'identity':'x(a²+a*b)+b²(A*x4+B*x2+1)=c*(x+t)^n; function(a+b*y)/x^((n−1)/2)',
         'witnesses':answer,'runtime_seconds':time.time()-start}
    (ROOT/'A_F4_rank_one_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
