#!/usr/bin/env python3
"""Riemann--Roch interpolation for explicit swapped cubic norms.

Search on C: y^2+y=(v^3+3)^3 for g=p5(v)+y and h=p3(v), with
Norm(g)=f_Q*(x-3)*Norm(h).  Every successful row is verified as a full
function-field polynomial identity; absence proves only this finite ansatz.
"""
from pathlib import Path
import json
import numpy as np
from bc_miller_norm import *

# Pick the first third of P whose x-3 value is a cube.  The supplied first
# third has inert fibre in this cover; the full list is checked explicitly.
Q=next(R for label,target,R in roots if label=='P' and (R[0]-3)**114==ONE)
a,_=miller3(Q)


def ix(c): return c.v[0]+7*c.v[1]+49*c.v[2]
def ff(i):
    i=int(i)
    return F((i%7,(i//7)%7,i//49))

inds=np.arange(343,dtype=np.int32)
left,right=inds[:,None],inds[None,:]
l=[left%7,(left//7)%7,left//49]
r=[right%7,(right//7)%7,right//49]
addtab=sum(((l[i]+r[i])%7)*(7**i) for i in range(3))
multab=(((l[0]*r[0]+2*(l[1]*r[2]+l[2]*r[1]))%7)
         +7*((l[0]*r[1]+l[1]*r[0]+2*l[2]*r[2])%7)
         +49*((l[0]*r[2]+l[1]*r[1]+l[2]*r[0])%7))
negtab=(-inds%7)+7*((-(inds//7))%7)+49*((-(inds//49))%7)
invtab=np.zeros(343,dtype=np.int32)
for i in range(1,343): invtab[i]=np.flatnonzero(multab[i]==1)[0]
def A(a,b): return addtab[a,b]
def N(a): return negtab[a]
def S(a,b): return A(a,N(b))
def M(a,b): return multab[a,b]
def D(a,b): return M(a,invtab[b])
def P(a,n):
    result=np.ones_like(a)
    for _ in range(n): result=M(result,a)
    return result
def vsum(*values):
    out=0
    for v in values: out=A(out,v)
    return out
def vpmul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(q): out[i+j]=A(out[i+j],M(c,d))
    return out
def vpadd(*polys):
    out=[0]*max(map(len,polys))
    for pol in polys:
        for i,c in enumerate(pol): out[i]=A(out[i],c)
    return out
def vscale(p,c): return [M(v,c) for v in p]


def affine_solve(rows,values,n):
    mat=[list(row)+[b] for row,b in zip(rows,values)]
    piv=[]
    rr=0
    for col in range(n):
        row=next((i for i in range(rr,len(mat)) if mat[i][col]),None)
        if row is None: continue
        mat[rr],mat[row]=mat[row],mat[rr]
        scale=mat[rr][col]
        mat[rr]=[v/scale for v in mat[rr]]
        for j in range(len(mat)):
            if j==rr: continue
            scale=mat[j][col]
            mat[j]=[v-scale*w for v,w in zip(mat[j],mat[rr])]
        piv.append(col)
        rr+=1
    assert all(any(row[:-1]) or not row[-1] for row in mat)
    particular=[Z]*n
    for i,col in enumerate(piv): particular[col]=mat[i][-1]
    basis=[]
    for free in (j for j in range(n) if j not in piv):
        vec=[Z]*n
        vec[free]=ONE
        for i,col in enumerate(piv): vec[col]=-mat[i][free]
        basis.append(vec)
    return particular,basis


def norm_polys(pcoeff,cy=1):
    """Vectorized exact norm of sum p_i v^i+cy*y, v^3=x-3; variable b=x-3."""
    u,p,q=pcoeff[0::3],pcoeff[1::3],pcoeff[2::3]
    up3=vpmul(vpmul(u,u),u)
    cpp=vpmul([6,6,2,1],vpadd(vscale(u,M(3,M(cy,cy))),[N(P(cy,3))]))
    pp3=[0]+vpmul(vpmul(p,p),p)
    qp3=[0,0]+vpmul(vpmul(q,q),q)
    mixed=[0]+vscale(vpmul(vpmul(u,p),q),4)
    normA=vpadd(up3,cpp,pp3,qp3,mixed)
    normB=vpadd(vscale(vpmul(u,u),M(3,cy)),vscale(u,N(M(3,M(cy,cy)))),
                vscale([0,6,2,1],P(cy,3)),[0]+vscale(vpmul(p,q),N(M(3,cy))))
    return normA,normB


def actual_norm(pcoeff,cy):
    u,p,q=tuple(pcoeff[0::3]),tuple(pcoeff[1::3]),tuple(pcoeff[2::3])
    ux,px,qx=(pshift(f,F(-3)) for f in (u,p,q))
    base=(ux,(cy,))
    cub=npow(base,3)
    other=padd(pmul(vertical(PC),ppow(px,3)),pmul(ppow(vertical(PC),2),ppow(qx,3)))
    minus=nscale(base,pmul((F(-3),),pmul(vertical(PC),pmul(px,qx))))
    return padd(padd(cub[0],other),minus[0]),padd(cub[1],minus[1])


root_values=[r for r in FIELD if r**3==Q[0]-3]
assert len(root_values) in (0,3)
minimal_num=tuple(pexact(p,vertical(times(2,Q))) for p in a[0])
NA,NB=(pshift(p,F(3)) for p in minimal_num)
na,nb=[ix(v) for v in NA],ix(NB[0])
parameter1,parameter2=np.meshgrid(inds,inds,indexing='ij')
parameter1,parameter2=parameter1.ravel(),parameter2.ravel()
records=[]
witnesses=[]
all_orders=[orders for orders in product(range(4),repeat=3) if sum(orders)==3] if root_values else [(1,1,1)]
for orders in all_orders:
    rows,values=[[ONE,Z,Z,Z,Z,Z]],[-QC[1]]
    if not root_values:
        bQ=Q[0]-3
        rows.extend([[ONE,Z,Z,bQ,Z,Z],[Z,ONE,Z,Z,bQ,Z],[Z,Z,ONE,Z,Z,bQ]])
        values.extend([-Q[1],Z,Z])
    for r,order in zip(root_values,orders):
        x,y=Q
        xp,xpp=3*r*r,3*r
        yp=3*x*x*xp/(2*y+1)
        ypp=(3*x*x*xpp+3*x*xp*xp-yp*yp)/(2*y+1)
        for j in range(order):
            rows.append([F(int(sp.binomial(k,j)))*r**(k-j) if k>=j else Z for k in range(6)])
            values.append(-[y,yp,ypp][j])
    particular,basis=affine_solve(rows,values,6)
    assert len(basis)==2
    pol=[vsum(ix(particular[j]),M(ix(basis[0][j]),parameter1),M(ix(basis[1][j]),parameter2)) for j in range(6)]
    normA,normB=norm_polys(pol)
    lhs=vscale(normA,nb)
    rhs=vpmul(na,normB)
    assert len(lhs)==len(rhs)
    good=np.ones(len(parameter1),dtype=bool)
    for v,w in zip(lhs,rhs): good &= v==w
    found=[]
    for index in np.flatnonzero(good):
        pg=tuple(ff(c[index]) for c in pol)
        actual=actual_norm(pg,ONE)
        rb=tuple(ff(D(c[index],nb)) if isinstance(c,np.ndarray) else ff(D(c,nb)) for c in normB)
        rx=pshift(rb,F(-3))
        assert actual==nscale(minimal_num,rx)
        # Search the exact rational-function norm denominator h=p3(v).
        hu1=pg[5]
        hu0s=[c for c in FIELD if c**3==rb[0]]
        assert hu1**3==rb[3]
        hs=[]
        for hu0 in hu0s:
            hp,hq=parameter1,parameter2
            eq1=vsum(ix(3*hu0*hu0*hu1),P(hp,3),N(M(M(3,ix(hu0)),M(hp,hq))))
            eq2=vsum(ix(3*hu0*hu1*hu1),P(hq,3),N(M(M(3,ix(hu1)),M(hp,hq))))
            for j in np.flatnonzero((eq1==ix(rb[1])) & (eq2==ix(rb[2]))):
                h=(hu0,ff(hp[j]),ff(hq[j]),hu1)
                normh=actual_norm(h,Z)
                assert normh==(rx,PZERO)
                hs.append(h)
        row={'orders_at_lifts_Q':orders,
             'numerator_p5':[list(c.v) for c in pg],
             'R3_b_coefficients':[list(c.v) for c in rb],
             'denominator_h3':[list(c.v) for c in hs[0]] if hs else None,
             'number_of_denominators_found':len(hs)}
        found.append(row)
        if hs:
            row['witness']='(p5(v)+y)/(v*h3(v)), v^3=x-3'
            row['exact_norm_is_a']=True
            witnesses.append(row)
    records.append({'orders':orders,'norm_candidates':len(found),'data':found})

out={'Q':encP(Q),'root_values_v_at_Q':[list(c.v) for c in root_values],
     'tested_rr_rows':len(all_orders)*343**2,'records':records,'witnesses':witnesses,
     'status':'PASS_EXACT_WITNESS' if witnesses else 'NO_WITNESS_IN_THIS_ANSATZ'}
data=json.dumps(out,indent=2)+'\n'
print(data,end='')
Path(__file__).with_suffix('.json').write_text(data)
