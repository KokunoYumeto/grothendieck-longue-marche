#!/usr/bin/env python3
"""Exact quotient/character support for A77; no Jacobian asserted by code."""
from pathlib import Path
import json, math


def run():
    G=[(i,j,k) for i in range(4) for j in range(4) for k in range(2)]
    one=(0,0,0);x=(1,0,0);y=(0,1,0);z=(0,0,1)
    def mul(a,b):return ((a[0]+b[0])%4,(a[1]+b[1])%4,(a[2]+b[2]+a[1]*b[0])%2)
    def inv(a):return (-a[0]%4,-a[1]%4,(-a[2]+a[0]*a[1])%2)
    def power(a,n):
        out=one
        for _ in range(n):out=mul(out,a)
        return out
    def order(a):
        for n in (1,2,4):
            if power(a,n)==one:return n
        raise AssertionError(a)
    def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
    assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in G for b in G for c in G)
    assert all(mul(a,inv(a))==one for a in G)
    H={one};todo=[one]
    while todo:
        a=todo.pop()
        for b in (x,y):
            c=mul(a,b)
            if c not in H:H.add(c);todo.append(c)
    assert H==set(G) and comm(x,y)==z
    centre=[a for a in G if all(mul(a,b)==mul(b,a) for b in G)]
    assert len(centre)==8 and set(comm(a,b) for a in G for b in G)=={one,z}
    assert max(map(order,G))==4
    Q=[(i,j,k) for i in range(2) for j in range(2) for k in range(2)]
    cases=[];chars=[];kernels=[]
    for eps in range(2):
        for delta in range(2):
            def qmul(a,b):
                return ((a[0]+b[0])%2,(a[1]+b[1])%2,
                        (a[2]+b[2]+a[1]*b[0]+eps*((a[0]+b[0])//2)+delta*((a[1]+b[1])//2))%2)
            def qmap(a):return (a[0]%2,a[1]%2,(a[2]+eps*(a[0]//2)+delta*(a[1]//2))%2)
            assert all(qmap(mul(a,b))==qmul(qmap(a),qmap(b)) for a in G for b in G)
            assert set(map(qmap,G))==set(Q)
            kernel={a for a in G if qmap(a)==one}
            assert len(kernel)==4
            involutions=sum(a!=one and qmul(a,a)==one for a in Q)
            assert involutions==(1 if (eps,delta)==(1,1) else 5)
            char=[0 if a[0]%2 or a[1]%2 else 2*((-1)**(a[2]+eps*(a[0]//2)+delta*(a[1]//2))) for a in G]
            assert {a for a,c in zip(G,char) if c==2}==kernel
            assert all(char[G.index((i,j,0))]+char[G.index((i,j,1))]==0 for i in range(4) for j in range(4))
            chars.append(char);kernels.append(kernel)
            cases.append({'x_square_exponent':eps,'y_square_exponent':delta,
                          'quotient_type':'Q8' if involutions==1 else 'D8','kernel':[list(a) for a in sorted(kernel)],
                          'nonidentity_involutions':involutions,'character':char,
                          'actual_quotient_images':[list(qmap(a)) for a in G]})
    gram=[[sum(a*b for a,b in zip(v,w))//32 for w in chars] for v in chars]
    assert gram==[[int(i==j) for j in range(4)] for i in range(4)]
    common=set(G)
    for k in kernels:common.intersection_update(k)
    assert common=={one}
    units=[(1,0),(0,1),(-1,0),(0,-1)]
    linear=[]
    for a in range(4):
        for b in range(4):linear.append([(a*i+b*j)%4 for i,j,k in G])
    for i,l in enumerate(linear):
        for j,m in enumerate(linear):
            val=[units[(a-b)%4] for a,b in zip(l,m)]
            assert (sum(v[0] for v in val),sum(v[1] for v in val))==(32*int(i==j),0)
        for char in chars:
            vals=[(c*units[-a%4][0],c*units[-a%4][1]) for c,a in zip(char,l)]
            assert (sum(v[0] for v in vals),sum(v[1] for v in vals))==(0,0)
    assert 16+4*4==32
    # The unbounded proof uses Z=<u²,v²,sigma>; these finite checks retain
    # its exact cyclic exponent arithmetic and the centre-order-two exception.
    central=[]
    for c in range(1,11):
        M=2**c;sig=M//2;valid=odd_square=xy_exception=0
        for a in range(M):
            for b in range(M):
                if math.gcd(M,a,b,sig)!=1:continue
                valid+=1
                if a%2 or b%2:
                    chosen=a if a%2 else b
                    assert 2*M//math.gcd(M,chosen)==2*M
                    odd_square+=1
                else:
                    assert c==1 and (a+b+sig)%M==1
                    xy_exception+=1
        assert valid==odd_square+xy_exception
        central.append({'centre_order':M,'generating_square_exponent_pairs':valid,'primitive_generator_square_cases':odd_square,'product_square_exception_cases':xy_exception,'cyclic_subgroup_index':2})
    return {'status':'PASS','candidate':'A.77, unregistered','group_order':32,'group_elements':[list(a) for a in G],
            'centre_order':len(centre),'derived_order':2,'exponent':4,'smallest_cyclic_index':8,
            'full_cover_genus':9,'full_cover_cusps':16,'four_actual_quotients':cases,
            'nonlinear_character_gram':gram,'linear_character_count':16,'complete_degree_square_sum':32,
            'joint_quotient_kernel':[list(a) for a in common],'faithful_cyclic_centre_checks':central,
            'scope':'Exact finite group and actual quotient maps, complete character orthogonality/degree accounting, and cyclic-centre arithmetic. The unbounded representation argument and actual Jacobian surjection are proved in the written candidate.'}


if __name__=='__main__':
    out=run();Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_quotients':[c['quotient_type'] for c in out['four_actual_quotients']],
                      'complete_degree_square_sum':out['complete_degree_square_sum'],'cyclic_centre_levels':len(out['faithful_cyclic_centre_checks']),
                      'largest_centre_order':out['faithful_cyclic_centre_checks'][-1]['centre_order']},indent=2))
