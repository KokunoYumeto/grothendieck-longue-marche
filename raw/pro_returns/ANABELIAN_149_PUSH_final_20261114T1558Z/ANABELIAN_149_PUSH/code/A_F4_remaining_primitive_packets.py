#!/usr/bin/env python3
"""Exact primitive-orbit analysis of complete positive theta-n loci.

The coefficient field is F16=F2[w]/(w^4+w+1), and the curve has coefficients
(1,9,14). Each irreducible factor of a complete Hankel gcd gives a coordinate
field. We construct and verify its full norm witness, adjoin an AS root only
when necessary, and compute all multiples of the theta point by Cantor
composition. No enumeration of the extension field is required.

The actual F4 Frobenius on these normalized coordinates is
 (x,y) |-> (x^4+1,y^4+alpha), alpha=w^2+w=6.
Scalar returns are reported, but the full theta-multiple test is stronger.
This remains a candidate computation pending independent review.
"""
from pathlib import Path
import argparse,json,time
from math import gcd
from A_theta_F4_moduli_witnesses import Base,Tower,irreducible_factor,pdiv,witness
from A_theta_F4_remaining_Jacobian import Jacobian,orbits

ROOT=Path(__file__).parent

def finite_tower(base,f):
    F=Tower(base,f);F.e=base.e*F.d;F.q=1<<F.e
    return F

def as_root(F,delta):
    """Solve b^2+b=delta by binary elimination; return None if inconsistent."""
    pivots={}
    for i in range(F.e):
        a=1<<i;v=F.mul(a,a)^a;c=a
        while v:
            j=v.bit_length()-1
            if j not in pivots:pivots[j]=(v,c);break
            w,b=pivots[j];v^=w;c^=b
    v=delta;c=0
    while v:
        j=v.bit_length()-1
        if j not in pivots:return None
        w,b=pivots[j];v^=w;c^=b
    assert F.mul(c,c)^c==delta
    return c

def all_factors(f,base):
    result=[]
    while len(f)>1:
        factor=irreducible_factor(f,base);result.append(factor)
        while len(f)>=len(factor):
            q,r=pdiv(f,factor,base)
            if r:break
            f=q
    return result

def prime_divisors(n):
    result=[];p=2
    while p*p<=n:
        if n%p==0:
            result.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:result.append(n)
    return result

def key(D):return tuple(D[0]),tuple(D[1])

def analyze(test):
    started=time.time();base=Base(4,19);n=test['n'];results=[]
    for factor in all_factors(test['coordinate_polynomial_coefficients'],base):
        row={'moduli_key':'203','field_degree':4,'coefficients':[1,9,14]}
        local=dict(test);local['coordinate_polynomial_coefficients']=factor
        norm=witness(row,local,{4:base})
        F=finite_tower(base,factor);t=F.t;delta=norm['beta_relation_constant']
        beta=as_root(F,delta);extended=beta is None
        if extended:
            tr=0;a=delta
            for _ in range(F.e):tr^=a;a=F.mul(a,a)
            assert tr==1
            K=finite_tower(F,[delta,1,1]);beta=1<<F.e;F=K
        assert F.mul(beta,beta)^beta==delta
        J=Jacobian(F,[1,9,14]);eta=J.theta_point(t,beta)
        assert J.theta(eta) and J.times(eta,n)==J.zero
        order=n
        for p in prime_divisors(n):
            while order%p==0 and J.times(eta,order//p)==J.zero:order//=p
        assert order>1
        hits=[];multiples={};current=J.zero
        for i in range(order):
            multiples[key(current)]=i
            if J.theta(current):hits.append(i)
            current=J.add(current,eta)
        assert current==J.zero and len(multiples)==order
        O=orbits(order);missing=[o for o in O if not set(o).intersection(hits)]
        x,y=t,beta;returns=[]
        for power in range(1,F.e//2+1):
            x=F.pow(x,4)^1;y=F.pow(y,4)^6
            phi=J.theta_point(x,y);k=multiples.get(key(phi))
            if k is not None:
                assert gcd(k,order)==1 and k in hits
                returns.append({'frobenius_power':power,'scalar':k})
        assert returns[-1]=={'frobenius_power':F.e//2,'scalar':1}
        results.append({
            'coordinate_factor':factor,'coordinate_degree_over_F16':len(factor)-1,
            'AS_quadratic_extension_used':extended,'field_degree_over_F2':F.e,
            'coordinate_t':t,'beta':beta,'eta':eta,'exact_order':order,
            'theta_multiples':hits,'primitive_doubling_orbits':O,
            'missing_primitive_orbits':missing,'criterion_satisfied':not missing,
            'scalar_Frobenius_returns':returns,'norm_witness':norm,
            'Cantor_operations':J.add_count,
        })
        print('factor',factor,'order',order,'hits',hits,'missing',len(missing),flush=True)
    return {'n':n,'complete_coordinate_gcd_degree':test['coordinate_polynomial_degree'],
            'coordinate_factors_tested':len(results),'packets':results,
            'some_primitive_zero_cover':any(r['criterion_satisfied'] for r in results),
            'runtime_seconds':time.time()-started}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',default='A_theta_F4_remaining_73_89.json');args=parser.parse_args()
    data=json.loads((ROOT/args.source).read_text());results=[]
    for test in data['tests']:
        if test['theta_n_exists']:results.append(analyze(test))
    out={'status':'EXPLORATORY exact norm and divisor arithmetic','source':args.source,
         'results':results,'scope':'A positive criterion requires independent review. Empty primitive coverage concerns these complete conductor loci only.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
