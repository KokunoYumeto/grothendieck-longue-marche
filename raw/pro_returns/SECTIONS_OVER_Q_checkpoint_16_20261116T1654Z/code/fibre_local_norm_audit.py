"""Exact finite audit of the joint fourth-root norm question over Q_2.

This is a search for explicit witnesses, not a proof of universal constancy.
Every accepted local fourth power uses the exact Q_2 criterion v divisible
by four and unit congruent to 1 modulo 16.  The global root fields are
unchanged by the rational fourth-power multipliers used here.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
from pathlib import Path


def val2(a):
    a = F(a)
    assert a
    n,d = abs(a.numerator), a.denominator
    vn = (n & -n).bit_length()-1
    vd = (d & -d).bit_length()-1
    return vn-vd


def pow2(e):
    return F(2**e) if e>=0 else F(1,2**(-e))


def unitmod(a,mod):
    a=F(a)/pow2(val2(a))
    return (a.numerator*pow(a.denominator,-1,mod))%mod


def fourth(a):
    return bool(a) and val2(a)%4==0 and unitmod(a,16)==1


Gamma=list(product((1,3,5,7),(0,1)))
identity=(1,0)


def mul(s,t):
    return (s[0]*t[0]%8,s[1]^t[1])


def common_subgroup(rows):
    allowed=[]
    for u,epsilon5 in Gamma:
        epsilon2=((u*u-1)//8)%2
        ds=gcd(4,u-1)
        if any(all((((u-1)//2)*delta+a*k2+b*k5)%ds==0
                   for a,b,delta in rows)
               for k2 in range(epsilon2,4,2)
               for k5 in range(epsilon5,4,2)):
            allowed.append((u,epsilon5))
    H={identity}
    for s in allowed:
        H|={mul(h,s) for h in tuple(H)}
    return H


rows=list(product(range(4),range(4),range(2)))
all_witnesses=[]
cases=0
checks=0
for exponent in range(-4,5):
    for odd in range(1,16,2):
        x=pow2(exponent)*odd
        if x==1:
            continue
        sigma=(unitmod(x,8),val2(x)%2)
        if sigma==identity:
            continue
        cases+=1
        found={}
        for row in rows:
            a,b,delta=row
            base=F((-1)**delta*2**a*5**b)
            for e in range(-4,5):
                if row in found:
                    break
                for zodd in range(1,32,2):
                    z=pow2(e)*zodd
                    D=base*z**4
                    if D==1:
                        continue
                    y4=x+(1-x)*D
                    checks+=1
                    if fourth(y4):
                        found[row]=(D,y4,z)
                        break
        H=common_subgroup(tuple(found))
        if sigma not in H:
            subset=list(found)
            for row in tuple(subset):
                reduced=[r for r in subset if r!=row]
                if sigma not in common_subgroup(reduced):
                    subset=reduced
            witness=(x,sigma,subset,{r:found[r] for r in subset},H)
            all_witnesses.append(witness)
            print('EXPLICIT JOINT NORM WITNESS:',witness)
            break
    if all_witnesses:
        break

out=(f'Checked {cases} exact local Artin classes and {checks} rational fourth-power inputs.\n'
     +f'Number of explicit nonconstant joint-character witnesses: {len(all_witnesses)}.\n'
     +repr(all_witnesses)+'\n'
     +'Absence of a witness in this finite audit proves no universal assertion.\n')
Path(__file__).with_name('fibre_local_norm_audit_output.txt').write_text(out)
print(out,end='')
