"""All cocycle and two/three-cycle residues in the actual Legendre images.

At even n the quotient is ker(PSL2(Z/n)->SL2(F2)), not SL2(Z/n).
We separately test whether the induced C2*C3 map descends to PSL2(Z/n).
No assertion that a solution lifts to profinite GT_0 is made.
"""
from pathlib import Path
from itertools import product
from math import gcd,lcm
from collections import Counter
import json,csv
from finite_groups import matmul,sl_elements

HERE=Path(__file__).resolve().parent

def level(n):
    canon=lambda a:min(a,tuple(-v%n for v in a))
    mul=lambda a,b:canon(matmul(a,b,n))
    inv=lambda a:canon((a[3],-a[1]%n,-a[2]%n,a[0]))
    e=canon((1%n,0,0,1%n))
    def power(a,k):
        if k<0:return power(inv(a),-k)
        b=e
        while k:
            if k&1:b=mul(b,a)
            a=mul(a,a);k//=2
        return b
    def order(a):
        b=a;k=1
        while b!=e:b=mul(b,a);k+=1
        return k
    S=canon((0,1%n,-1%n,0));R=canon((0,1%n,-1%n,1%n))
    y=power(mul(S,R),2);x=canon((1%n,0,2%n,1%n));z=inv(mul(x,y))
    rho=lambda a:mul(mul(R,a),inv(R))
    theta=lambda a:mul(mul(S,a),inv(S))
    def closure(gens):
        seen={e};todo=[e]
        for a in todo:
            for g in gens:
                b=mul(a,g)
                if b not in seen:seen.add(b);todo.append(b)
        return seen
    H=closure([x,y]);Q=sorted({canon(a) for a in sl_elements(n)})
    assert closure([S,R])==set(Q)
    assert rho(y)==x and rho(x)==z and theta(x)==y
    comm=mul(mul(mul(x,y),inv(x)),inv(y))
    der=closure({mul(mul(a,comm),inv(a)) for a in H})
    o=order(x)
    sols=[];cycles=[];map_tests={};outer_keys=set();first_fail=None
    # Once per quotient, precompute a breadth first spanning tree and both edges.
    idx={a:i for i,a in enumerate(Q)}
    edges=[(idx[mul(a,S)],idx[mul(a,R)]) for a in Q]
    def descends(Snew,Rnew):
        values={idx[e]:e};todo=[idx[e]]
        for i in todo:
            for j,g in zip(edges[i],[Snew,Rnew]):
                v=mul(values[i],g)
                if j in values:
                    if values[j]!=v:return False,None
                else:values[j]=v;todo.append(j)
        if len(set(values.values()))!=len(Q):return False,None
        return True,values
    for nu in range(o):
        mu=2*nu+1
        if gcd(mu,n)!=1:continue
        xnu=power(x,nu);xn=inv(xnu)
        for xi in sorted(H):
            eta=mul(xi,xn)
            if mul(eta,theta(eta))!=e:continue
            if mul(mul(xi,rho(xi)),rho(rho(xi)))!=e:continue
            Snew=mul(eta,S);Rnew=mul(xi,R)
            ok,values=descends(Snew,Rnew)
            sols.append((nu,xi,eta,ok))
            if ok:
                key=min((mul(mul(inv(h),Snew),h),mul(mul(inv(h),Rnew),h)) for h in Q)
                outer_keys.add(key)
            elif first_fail is None:first_fail=dict(nu=nu,mu=mu,xi=xi,eta=eta)
        for f in sorted(der):
            if mul(theta(f),f)!=e:continue
            # rho=omega^{-1}; Drinfeld f(z,x)=omega² f=rho f.
            val=e
            for a in [rho(f),power(z,nu),rho(rho(f)),power(y,nu),f,power(x,nu)]:val=mul(val,a)
            if val!=e:continue
            a=power(x,mu);b=mul(mul(inv(f),power(y,mu)),f)
            generates=(closure([a,b])==H)
            cycles.append(dict(nu=nu,mu=mu,f=f,generates=generates))
    # Gauge preserves each exact cocycle solution (including lambda).
    solset={(nu,xi,eta) for nu,xi,eta,ok in sols};unseen=set(solset);gauge=0
    while unseen:
        nu,xi,eta=min(unseen);orb=set()
        for a in range(o):
            left=power(y,a);right=power(x,-a)
            orb.add((nu,mul(mul(left,xi),right),mul(mul(left,eta),right)))
        assert orb<=solset
        unseen-=orb;gauge+=1
    summary=dict(n=n,PSL_order=len(Q),Legendre_image_order=len(H),derived_order=len(der),
                 loop_order=o,manuscript_residues=len(sols),gauge_orbits=gauge,
                 quotient_automorphism_residues=sum(ok for nu,xi,eta,ok in sols),
                 quotient_outer_images=len(outer_keys),cycle_residues=len(cycles),
                 generating_cycle_residues=sum(c['generates'] for c in cycles),
                 first_descent_failure=first_fail)
    detail=dict(summary=summary,manuscript_solutions=[dict(nu=a,xi=b,eta=c,descends=d) for a,b,c,d in sols],
                cycle_solutions=cycles)
    return summary,detail

def main():
    rows=[];details={}
    for n in [2,3,4,5,6,7,8,12,24]:
        a,b=level(n);rows.append(a);details[n]=b;print(json.dumps(a),flush=True)
    (HERE/'finite_matrix_cycles.json').write_text(json.dumps(details,indent=2)+'\n')
    with (HERE/'finite_matrix_cycles.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

if __name__=='__main__':main()
