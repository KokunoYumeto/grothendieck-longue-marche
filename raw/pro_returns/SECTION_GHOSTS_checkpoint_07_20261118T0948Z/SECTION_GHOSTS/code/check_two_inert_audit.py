#!/usr/bin/env python3
"""Exact finite certificate for E.166--169, independent of old S-unit files.

Only Python's standard library is used.  Class-field, unit-rank, duality,
cohomological, and compactness arguments are supplied in the proof; this
program certifies the explicit identities and finite residue matrix.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

class QuadraticField:
    """F_q[z]/(z^2+z+1), with q prime and q=2 mod3."""
    def __init__(self, q): self.q = q
    def add(self, a, b): return ((a[0]+b[0]) % self.q, (a[1]+b[1]) % self.q)
    def neg(self, a): return (-a[0] % self.q, -a[1] % self.q)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def mul(self, a, b):
        q = self.q
        return ((a[0]*b[0]-a[1]*b[1]) % q,
                (a[0]*b[1]+a[1]*b[0]-a[1]*b[1]) % q)
    def pow(self, a, n):
        if n < 0:
            assert a != (0, 0)
            return self.pow(self.pow(a, self.q*self.q-2), -n)
        result = (1, 0)
        while n:
            if n & 1: result = self.mul(result, a)
            a = self.mul(a, a)
            n //= 2
        return result
    def div(self, a, b): return self.mul(a, self.pow(b, -1))
    def scale(self, a, n): return (a[0]*n % self.q, a[1]*n % self.q)
    def cubic_log(self, a):
        assert a != (0, 0)
        symbol = self.pow(a, (self.q*self.q-1)//3)
        return next(i for i in range(3) if self.pow((0, 1), i) == symbol)
    def g(self, q, a):
        if q == 2: return self.sub(a, (1, 0))
        if q == 11: return self.add(a, (2, 0))
        if q == 59: return self.sub(self.add((2, 0), self.scale(a, 2)), self.pow(a, 2))
        raise ValueError(q)

# Q[beta]/(beta^6+3).
def pad(a): return tuple(Fraction(x) for x in a) + (Fraction(0),)*(6-len(a))
def add(a, b): return tuple(x+y for x,y in zip(a,b))
def scale(a, n): return tuple(n*x for x in a)
def mul(a, b):
    out = [Fraction(0)]*11
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    for k in range(10, 5, -1): out[k-6] -= 3*out[k]
    return tuple(out[:6])
def power(a,n):
    out=pad([1])
    for _ in range(n):out=mul(out,a)
    return out

def determinant(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    answer=Fraction(1)
    for j in range(len(a)):
        pivot=next((i for i in range(j,len(a)) if a[i][j]),None)
        if pivot is None:return 0
        if pivot != j:a[pivot],a[j]=a[j],a[pivot];answer=-answer
        x=a[j][j];answer*=x
        for k in range(j,len(a)):a[j][k]/=x
        for i in range(j+1,len(a)):
            x=a[i][j]
            for k in range(j,len(a)):a[i][k]-=x*a[j][k]
    assert answer.denominator==1
    return int(answer)

beta=pad([0,1]);one=pad([1]);alpha=scale(power(beta,2),-1)
zeta=scale(add(power(beta,3),scale(one,-1)),Fraction(1,2))
delta=add(one,scale(zeta,2))
epsilon=add(add(one,beta),scale(mul(zeta,power(beta,2)),-1))
tau=lambda a:tuple((-1)**i*x for i,x in enumerate(a))
U=add(power(alpha,2),scale(one,-2))
assert power(beta,3)==delta
assert mul(power(beta,2),scale(one,-1))==alpha
assert add(add(power(zeta,2),zeta),one)==pad([0])
assert mul(epsilon,tau(epsilon))==U
# eta = -(beta^3+1)/2-beta^2-beta; avoid inversion.
eta=scale(add(add(add(scale(add(power(beta,3),one),Fraction(1,2)),power(beta,2)),beta),pad([0])),-1)
assert mul(eta,tau(epsilon))==epsilon
assert mul(eta,tau(eta))==one
# Relative norm of 1+beta-zeta beta².
rel_norm=add(add(one,delta),scale(power(delta,2),-1))
rel_norm=add(rel_norm,scale(mul(zeta,delta),3))
assert rel_norm==power(zeta,2)
# Pure cubic norm of a+b alpha+c alpha².
pure_norm=lambda a,b,c:a**3+3*b**3+9*c**3-9*a*b*c
norms={2:pure_norm(-1,1,0),11:pure_norm(2,1,0),59:pure_norm(2,2,-1),'U':pure_norm(-2,0,1)}
assert norms=={2:2,11:11,59:59,'U':1}

unit_checks=[]
for b in [3,19]:
    p=61;z=(b**3-1)*pow(2,-1,p)%p
    e=(1+b-z*b*b)%p
    te=(1-b-pow(z,2,p)*b*b)%p
    et=e*pow(te,-1,p)%p
    logs=[]
    for val in [z,et]:
        val=pow(val,(p-1)//3,p)
        logs.append(next(i for i in range(3) if pow(z,i,p)==val))
    assert (b**6+3)%p==0
    unit_checks.append({'beta':b,'zeta':z,'eta':et,'logs':logs})
assert [x['logs'] for x in unit_checks]==[[2,1],[2,0]]
assert determinant([x['logs'] for x in unit_checks])==-2

rows=[];residue_records=[]
for q,r in [(2,1),(11,-2),(59,49)]:
    f=QuadraticField(q);z=(0,1)
    for j in range(3):
        al=f.scale(f.pow(z,j),r)
        assert f.pow(al,3)==(3%q,0)
        be=f.div(f.pow(al,2),(1,2))
        eps=f.sub(f.add((1,0),be),f.mul(z,f.pow(be,2)))
        teps=f.sub(f.sub((1,0),be),f.mul(f.pow(z,2),f.pow(be,2)))
        et=f.div(eps,teps)
        bs=[(0,z),(0,et)]
        for p in [2,11,59]:
            gs=[f.g(p,f.mul(al,f.pow(z,i))) for i in range(3)]
            assert f.mul(f.mul(gs[0],gs[1]),gs[2])==(p%q,0)
            if p!=q:bs.append((0,f.div(gs[1],gs[2])))
            elif gs[1]==(0,0):bs.append((1,f.pow(f.mul(gs[0],f.pow(gs[2],2)),-1)))
            elif gs[2]==(0,0):bs.append((-1,f.mul(gs[0],f.pow(gs[1],2))))
            else:bs.append((0,f.div(gs[1],gs[2])))
        va=8 if q in (11,59) else 0
        au=f.scale(al,pow(649//q,8,q)) if va else f.scale(al,pow(649,8,q))
        row=[f.cubic_log(f.div(f.pow(au,vb),f.pow(bu,va))) for vb,bu in bs]
        u=f.sub(f.pow(al,2),(2,0))
        cup_u=f.cubic_log(f.pow(u,-va))
        rows.append(row)
        residue_records.append({'q':q,'j':j,'alpha':al,'A_unit':au,
             'valuations':[v for v,_ in bs],'rows':row,'U':u,'cup_A_U':cup_u})
expected=[[0,0,0,0,0],[0,0,2,0,0],[0,0,2,0,0],
          [1,2,0,1,0],[1,1,0,0,0],[1,1,0,0,0],
          [2,0,0,1,1],[2,1,0,1,2],[2,1,0,1,2]]
assert rows==expected
assert [r['cup_A_U'] for r in residue_records]==[0,0,0,0,2,1,0,1,2]
minor=[rows[i] for i in [1,3,4,6,7]]
assert determinant(minor)==-8

# The two integral module identities gw=chi²w+chi²aT and gT=chi³T,
# checked as actual coefficient identities at all a,chi modulo9.
action_checks=0
for n in [3,9,27]:
    inv2=pow(2,-1,n)
    for a in range(n):
        for chi in range(n):
            if chi%3==0:continue
            def act(v):
                c0,c1,c2=v
                return (chi*c0%n,(chi*a*c0+chi*chi*c1)%n,
                  (chi*(a*(a-1)//2)*c0+
                   (chi*chi*a+chi*chi*(chi-1)//2)*c1+chi**3*c2)%n)
            assert act((0,1,-inv2))==(0,chi*chi%n,(chi*chi*a-chi*chi*inv2)%n)
            assert act((0,0,1))==(0,0,chi**3%n)
            action_checks+=2
    m=n
    assert m%m==0 and (m*(m-1)//2)%m==0

payload={'status':'PASS','scope':'Finite identities and complete displayed residue certificate; proof supplies global arguments',
 'pure_cubic_norms':{str(k):v for k,v in norms.items()},'unit_independence':unit_checks,
 'cup_columns':['zeta','eta','r2','r11','r59'],'residues':residue_records,
 'selected_row_indices':[1,3,4,6,7],'minor_determinant':-8,'minor_mod3':1,
 'coefficient_identity_checks':action_checks,
 'residue_sizes':[4,121,3481],
 'residue_exponents':[[q-1,q*q-1] for q in [4,121,3481]]}
canonical=json.dumps(payload,sort_keys=True,default=str).encode()
payload['data_sha256']=hashlib.sha256(canonical).hexdigest()
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(payload,indent=2,sort_keys=True,default=str)+'\n')
print(json.dumps({'status':'PASS','minor_determinant':-8,'matrix_rank_mod3':5,
                 'coefficient_checks':action_checks,'data_sha256':payload['data_sha256']},sort_keys=True))
