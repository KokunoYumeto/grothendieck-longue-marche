#!/usr/bin/env python3
"""Complete F64 theta-packet search on the actual key203 F4 model.

This seeks positive primitive-orbit coverage at mixed non-Artin conductors,
independently of the Hankel searches. General Cantor arithmetic is used on
Y^2+hY=hG, h=x^2+x+alpha and G=x^3+x^2+x+alpha^2.
The complete F64 theta set supplies all theta multiples on every F64-rational
cyclic subgroup, because the theta embedding is defined overF4 and injective.
"""
from pathlib import Path
import json,time
from A_theta_F4_moduli_witnesses import Base,pmul,peval
from A_theta_F4_remaining_Jacobian import Jacobian,orbits

def key(D):return tuple(D[0]),tuple(D[1])

def main():
    start=time.time();F=Base(6,67)
    alpha=next(a for a in range(2,64) if F.mul(a,a)^a^1==0);alpha2=F.mul(alpha,alpha)
    J=Jacobian(F,[1,1,1]);J.h=[alpha,1,1];J.f=pmul(J.h,[alpha2,1,1,1],F);J.T=(J.h,[])
    assert J.check(J.T) and J.add(J.T,J.T)==J.zero
    roots={}
    for y in range(64):roots.setdefault(F.mul(y,y)^y,[]).append(y)
    points=[];theta={key(J.T):{'infinity':True}};odd=[]
    for x in range(64):
        h=peval(J.h,x,F)
        if not h:raise AssertionError('the two finite branch points are not rational overF64')
        value=F.mul(peval([alpha2,1,1,1],x,F),F.inv(h))
        for y in roots.get(value,[]):
            Y=F.mul(h,y);D=J.check(([x,1],[Y] if Y else []));eta=J.add(D,J.T)
            assert J.theta(eta) and J.times(eta,6076)==J.zero
            point={'x':x,'y':y,'eta':eta};points.append(point);theta[key(eta)]=point
            if J.times(eta,1519)==J.zero:
                n=1519
                for p in [7,31]:
                    while n%p==0 and J.times(eta,n//p)==J.zero:n//=p
                assert n>1;point['exact_order']=n;odd.append(point)
    assert len(points)+1==91 and len(theta)==91
    covered=set();packets=[]
    for point in odd:
        if key(point['eta']) in covered:continue
        eta=point['eta'];n=point['exact_order'];cur=J.zero;hits=[];multiples={}
        for i in range(n):
            k=key(cur);multiples[k]=i
            if k in theta:hits.append(i);assert J.theta(cur)
            cur=J.add(cur,eta)
        assert cur==J.zero and len(multiples)==n
        covered.update(multiples);O=orbits(n);missing=[o for o in O if not set(o).intersection(hits)]
        x,y=point['x'],point['y'];returns=[]
        for power in range(1,4):
            x=F.pow(x,4);y=F.pow(y,4);h=peval(J.h,x,F);Y=F.mul(h,y)
            phi=J.add(J.check(([x,1],[Y] if Y else [])),J.T)
            if key(phi) in multiples:returns.append({'power':power,'scalar':multiples[key(phi)]})
        entry={'generator':point,'theta_multiples':hits,'primitive_doubling_orbits':O,
               'missing_primitive_orbits':missing,'criterion_satisfied':not missing,
               'scalar_Frobenius_returns':returns};packets.append(entry)
        print('order',n,'hits',hits,'missing',len(missing),flush=True)
    out={'status':'EXPLORATORY exact fullF64 theta enumeration','field_binary_modulus':67,
         'alpha':alpha,'C_F64_points':91,'J_F64_order':6076,'odd_theta_points':len(odd),
         'distinct_cyclic_packets':len(packets),'packets':packets,
         'some_positive_primitive_cover':any(p['criterion_satisfied'] for p in packets),
         'runtime_seconds':time.time()-start}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['some_positive_primitive_cover'],out['runtime_seconds'])

if __name__=='__main__':main()
