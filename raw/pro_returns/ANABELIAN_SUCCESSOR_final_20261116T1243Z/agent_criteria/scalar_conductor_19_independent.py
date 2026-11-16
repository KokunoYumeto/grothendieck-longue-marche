"""Independent trial-division verification of the e=19 A6 count.

This uses no imported parent/other-agent arithmetic or sieve. It enumerates
every odd n below the proved cutoff 10e^3, computes ord_n(2) by factoring
phi(n), and checks the exact Sidon necessary condition and Jordan count.
"""
from math import gcd
from collections import Counter
import json
from pathlib import Path

def prime_factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:
                n//=p
        p+=1
    if n>1:
        out.append(n)
    return out

def phi(n):
    out=n
    for p in prime_factors(n):
        out=out//p*(p-1)
    return out

def order_two(n):
    out=phi(n)
    for p in prime_factors(out):
        while out%p==0 and pow(2,out//p,n)==1:
            out//=p
    assert pow(2,out,n)==1
    assert all(pow(2,out//p,n)!=1 for p in prime_factors(out))
    return out

e=19
cutoff=10*e**3
allowed=[]
for n in range(3,cutoff,2):
    f=order_two(n)
    M=phi(n)//gcd(f,e)
    if M*(M+1)<=2*(n-1):
        j4=n**4
        for p in prime_factors(n):
            j4=j4//(p**4)*(p**4-1)
        scalar=pow(2,e,n)
        orbit={1}
        x=scalar
        while x!=1:
            orbit.add(x)
            x=x*scalar%n
        symmetric=orbit|{(-a)%n for a in orbit}|{0}
        diffs=Counter((a-b)%n for a in symmetric for b in symmetric if a!=b)
        max_multiplicity=max(diffs.values())
        allowed.append(dict(n=n,order_two=f,minimum_primitive_theta_points=M,
                            jordan_four=j4,parameter_upper_bound=j4//M,
                            minimal_symmetric_scalar_orbit_size=len(symmetric)-1,
                            maximum_nonzero_difference_multiplicity=max_multiplicity,
                            fails_necessary_local_Sidon_test=max_multiplicity>2))

bound=sum(row['parameter_upper_bound'] for row in allowed)
good=4**e-4-bound
assert [row['n'] for row in allowed]==[
    191,229,361,419,457,571,573,647,687,955,1083,1257,1371]
assert bound==214950173608
assert good==59927733332 and good>0
out=dict(status='all exact independent checks passed', e=e,
         field_size=4**e, proved_conductor_cutoff=cutoff,
         complete_admissible_conductor_list=allowed,
         sum_parameter_upper_bounds=bound,
         lower_bound_good_parameters=good,
         optional_local_Sidon_exclusions=[row['n'] for row in allowed
             if row['fails_necessary_local_Sidon_test']],
         scope='The incidence bound divides J_4(n) by M because a primitive-zero member requires at least M distinct points of exact order n; this does not count all members containing any n-torsion point.')
Path(__file__).with_name('scalar_conductor_19_independent_output.json').write_text(
    json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
