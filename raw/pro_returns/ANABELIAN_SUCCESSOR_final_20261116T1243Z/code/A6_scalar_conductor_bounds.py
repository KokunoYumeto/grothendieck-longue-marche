"""Exact finite certificate for scalar-Frobenius primitive-cover obstructions.

The mathematical cutoff n < 10*e**3 and the necessary inequality
M*(M+1) <= 2*(n-1), M=phi(n)/gcd(ord_n(2),e), are proved in the paper.
This program enumerates every remaining odd n, computes its order exactly,
and counts the union bound for torsion incidences in the explicit pencil.
It proves no claim about an individually selected pencil parameter.
"""
from array import array
from math import gcd
from pathlib import Path
import json,time

def main():
    start=time.monotonic()
    exponents=list(range(1,33))+[64]
    limit=10*max(exponents)**3
    phi=array('I',range(limit+1))
    spf=array('I',[0])*(limit+1)
    for prime in range(2,limit+1):
        if spf[prime]:
            continue
        for multiple in range(prime,limit+1,prime):
            phi[multiple]-=phi[multiple]//prime
            if spf[multiple]==0:
                spf[multiple]=prime
    def prime_factors(n):
        ans=[]
        while n>1:
            p=spf[n];ans.append(p)
            while n%p==0:n//=p
        return ans
    order_cache={}
    def order2(n):
        if n in order_cache:return order_cache[n]
        f=int(phi[n])
        for p in prime_factors(f):
            while f%p==0 and pow(2,f//p,n)==1:
                f//=p
        assert pow(2,f,n)==1
        assert all(pow(2,f//p,n)!=1 for p in prime_factors(f))
        order_cache[n]=f
        return f
    rows=[]
    for e in exponents:
        cutoff=10*e**3
        candidates=[]
        for n in range(3,cutoff,2):
            tot=int(phi[n])
            # M >= phi(n)/e; the square inequality is a safe fast filter.
            if tot*tot>2*e*e*(n-1):continue
            f=order2(n);d=gcd(f,e);m=tot//d
            if m*(m+1)<=2*(n-1):
                jordan=n**4
                for ell in prime_factors(n):
                    jordan=jordan//ell**4*(ell**4-1)
                candidates.append({'n':n,'phi':tot,'order_2':f,
                    'gcd_order_exponent':d,'M':m,
                    'exact_order_n_points_J4':jordan,
                    'bad_parameter_incidence_bound':jordan//m})
        bound=sum(x['n']**4-1 for x in candidates)
        refined=sum(x['bad_parameter_incidence_bound'] for x in candidates)
        field=4**e
        rows.append({'e':e,'q':field,'cutoff_exclusive':cutoff,
            'admissible_conductors':candidates,
            'number_admissible':len(candidates),
            'torsion_incidence_union_bound':bound,
            'singular_parameter_bound':5,
            'parameters_total':field+1,
            'smooth_good_parameter_lower_bound':max(0,field+1-5-bound),
            'proves_counterexample_existence':field+1>5+bound,
            'exact_order_multiplicity_union_bound':refined,
            'refined_good_parameter_lower_bound':max(0,field+1-5-refined),
            'refined_proves_counterexample_existence':field+1>5+refined})
    result={'method':'Exact totient/order inequality after the proved global cutoff',
        'does_not_select_an_individual_parameter':True,
        'rows':rows,'seconds':time.monotonic()-start}
    destination=Path(__file__).with_suffix('.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    for r in rows:
        print(json.dumps({k:v for k,v in r.items() if k!='admissible_conductors'}))
    print('saved',destination,'in',result['seconds'],'seconds')

if __name__=='__main__':main()
