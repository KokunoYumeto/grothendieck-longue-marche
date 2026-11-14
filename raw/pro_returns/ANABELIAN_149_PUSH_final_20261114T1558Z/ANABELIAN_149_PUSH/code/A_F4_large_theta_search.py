#!/usr/bin/env python3
"""Bounded positive primitive-cover search overF_(4^9), with explicit witnesses.

The actual odd exponent and rank-two seven-primary part are certified by
explicit independent torsion generators and the exact Frobenius group order.
All prime projections use tiny complete additive tables (largest order4519).
Primitive doubling cosets are normalized in product logarithm coordinates;
no traversal of the billion-element cyclic group is performed.
"""
from pathlib import Path
from math import gcd
import json,time,sympy as sp
from A_F4_large_theta import Field,Div,ZERO,add,neg,times,eta,HASH

ROOT=Path(__file__).parent
PRIMES=[7,31,2503,4519];ORDERS=[6,30,2502,4518]
M=2454499369

def key(D):return bytes(D)
Z=key(ZERO)

def table(G,p):
    cur=ZERO;d={}
    for i in range(p):d[key(cur)]=i;cur=add(cur,G)
    assert key(cur)==Z and len(d)==p
    return d

def multiplicative_logs(p):
    factors=list(sp.factorint(p-1))
    g=next(g for g in range(2,p) if all(pow(g,(p-1)//r,p)!=1 for r in factors))
    a=1;d={}
    for i in range(p-1):d[a]=i;a=a*g%p
    assert a==1 and len(d)==p-1
    return g,d

ML=[multiplicative_logs(p) for p in PRIMES]
V=[d[2] for _,d in ML]

def canonical_logs(values):
    a=list(values)
    period=1
    # Normalize first the2503, then4519, then31 component. The7 component
    # is already fixed by the remaining period. Each step subtracts an
    # exactly determined multiple of the doubling vector.
    for j in [2,3,1]:
        delta=period*V[j]%ORDERS[j];g=gcd(delta,ORDERS[j]);length=ORDERS[j]//g
        residue=a[j]%g;k=((a[j]-residue)//g)*pow(delta//g,-1,length)%length
        shift=period*k
        a=[(x-shift*v)%o for x,v,o in zip(a,V,ORDERS)]
        assert a[j]==residue
        period*=length
    assert period==1570005 and all(period*v%o==0 for v,o in zip(V,ORDERS))
    assert 0<=a[0]<6 and 0<=a[1]<6 and 0<=a[2]<2 and 0<=a[3]<18
    return (((a[0]*6+a[1])*2+a[2])*18+a[3])

CRT=[(M//p)*pow(M//p,-1,p) for p in PRIMES]
def crt(values):return sum(a*b for a,b in zip(values,CRT))%M

def main():
    start=time.time();F=Field(18,(1<<18)|(1<<7)|1)
    pi=sp.Matrix([[0,0,0,-16],[1,0,0,-8],[0,1,0,-1],[0,0,1,-2]])
    group_order=int((pi**9-sp.eye(4)).det());curve_count=F.q+1-int(sp.trace(pi**9))
    assert group_order==4*7*M==68725982332
    assert sp.factorint(group_order)=={2:2,7:2,31:1,2503:1,4519:1}
    labels=set()
    for a in range(6):
      for b in range(6):
       for c in range(2):
        for d in range(18):
         values=[a,b,c,d];label=canonical_logs(values);labels.add(label)
         assert canonical_logs([(x+v)%o for x,v,o in zip(values,V,ORDERS)])==label
    assert labels==set(range(1296))
    # Obtain a theta generator of exact orderM.
    for x in range(F.q):
        ok,y=F.point(x)
        if ok!=1:continue
        G=eta(x,y)
        if key(times(G,M))==Z and all(key(times(G,M//p))!=Z for p in PRIMES):
            Gpoint=[x,y];break
    else:raise AssertionError('no exactM theta generator')
    projections=[times(G,M//p) for p in PRIMES]
    small=[table(projections[i],p) for i,p in enumerate(PRIMES)]
    A=projections[0]
    # An independent order-seven point proves J(Fq)[7] has ranktwo; combined
    # with the exact group order this proves the odd exponent is exactlyM.
    for x in range(F.q):
        ok,y=F.point(x)
        if ok!=1:continue
        H=times(eta(x,y),4*M//7)
        if key(times(H,7))==Z and key(H) not in small[0]:Hpoint=[x,y];break
    else:raise AssertionError('no independent seven-primary direction')
    seven={}
    for i in range(7):
        for j in range(7):seven[key(add(times(A,i),times(H,j)))]=(i,j)
    assert len(seven)==49
    inv=pow(M//7,-1,7)
    generators=[add(G,times(H,r*inv%7)) for r in range(7)]
    generators.append(add(add(G,neg(times(A,inv))),times(H,inv)))
    for D in generators:assert key(times(D,M))==Z and all(key(times(D,M//p))!=Z for p in PRIMES)
    packets=[{} for _ in range(8)];odd_points=primitive_points=affine_pairs=0;positive=None
    print('INIT','G',Gpoint,'independent7',Hpoint,'field',F.generator,F.alpha,'curvecount',curve_count,flush=True)
    for x in range(F.q):
        ok,y=F.point(x)
        if ok!=1:continue
        affine_pairs+=1;D=eta(x,y)
        if key(times(D,M))!=Z:continue
        odd_points+=2
        comp=[times(D,M//p) for p in PRIMES]
        if any(key(t)==Z for t in comp):continue
        primitive_points+=2;u,v=seven[key(comp[0])]
        if u:direction=v*pow(u,-1,7)%7;j7=u
        else:direction=7;j7=v
        values=[j7]+[small[i][key(comp[i])] for i in range(1,4)]
        assert all(values)
        for sign in [1,-1]:
            scalars=[sign*a%p for a,p in zip(values,PRIMES)]
            logs=[d[a] for a,(_,d) in zip(scalars,ML)];label=canonical_logs(logs)
            if label not in packets[direction]:
                index=crt(scalars);assert gcd(index,M)==1
                packets[direction][label]={'x':x,'y':y if sign==1 else y^1,'index':index,'prime_components':scalars,'label':label}
        if len(packets[direction])==1296:positive=direction;break
        if x%4096<2:
            print('PROGRESS',x,odd_points,primitive_points,[len(d) for d in packets],time.time()-start,flush=True)
            (ROOT/'A_F4_large_theta_search_progress.json').write_text(json.dumps({'last_x':x,'odd_theta_points':odd_points,'primitive_theta_points':primitive_points,'coverage':[len(d) for d in packets],'elapsed_seconds':time.time()-start})+'\n')
    out={'status':'POSITIVE candidate' if positive is not None else 'COMPLETE bounded search; no saturated packet',
         'C_source_sha256':HASH,'field_binary_modulus':F.mod,'field_generator':F.generator,'alpha':F.alpha,
         'field_size':F.q,'actual_F4_Weil_polynomial_ascending':[16,8,1,2,1],
         'Jacobian_order':group_order,'odd_exponent':M,'odd_factorization':{str(p):1 for p in PRIMES},
         'theta_generator_point':Gpoint,'theta_generator_divisor':G.lists(),
         'independent_seven_point_source':Hpoint,'independent_seven_divisor':H.lists(),
         'primitive_doubling_period':1570005,'primitive_orbit_count':1296,
         'multiplicative_generators':[g for g,_ in ML],'doubling_log_vector':V,
         'processed_x_through':x,'odd_theta_points':odd_points,'primitive_theta_points':primitive_points,
         'coverage':[len(d) for d in packets],'positive_direction':positive,
         'cyclic_generators':[D.lists() for D in generators],
         'packets':[{str(k):v for k,v in d.items()} for d in packets],
         'runtime_seconds':time.time()-start}
    if positive is None:assert 1+2*affine_pairs==curve_count
    else:
        # Express the final witness set relative to an actual theta generator.
        first=next(iter(packets[positive].values()));theta_index=first['index'];theta_G=eta(first['x'],first['y'])
        assert key(times(generators[positive],theta_index))==key(theta_G)
        out['positive_theta_generator']=first;out['positive_theta_generator_divisor']=theta_G.lists()
        invindex=pow(theta_index,-1,M)
        for witness in packets[positive].values():witness['index_relative_to_theta_generator']=witness['index']*invindex%M
        out['packets']=[{str(k):v for k,v in d.items()} for d in packets]
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['status'],out['coverage'],'seconds',out['runtime_seconds'],flush=True)

if __name__=='__main__':main()
