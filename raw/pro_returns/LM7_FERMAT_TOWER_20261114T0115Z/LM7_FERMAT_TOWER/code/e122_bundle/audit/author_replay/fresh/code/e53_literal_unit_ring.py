#!/usr/bin/env python3
"""Independent rational relative-ring checks of all twenty-two unit roots.

No PARI, number-field package, root-search output, or executable import is used.
The field is Q[b,z]/(z^6+z^3+1,b^9-53z^3).
"""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm
from functools import reduce,lru_cache
import hashlib,json
import sympy as S

R=Path(__file__).resolve().parents[1]
P=R/'inputs/e122_literal_unit_witnesses.json';D=json.loads(P.read_text())
@lru_cache(None)
def zp(k):
    k%=9
    if k<6:return ((k,1),)
    return ((k-3,-1),(k-6,-1))
TAB={}
for a in range(54):
    i,j=divmod(a,6)
    for b in range(54):
        k,l=divmod(b,6);ii=i+k;power=j+l;co=1
        if ii>=9:ii-=9;power+=3;co=53
        TAB[a,b]=tuple((6*ii+t,co*v) for t,v in zp(power))
class E:
    __slots__=('a','d')
    def __init__(self,a,d=1):
        a=tuple(int(x) for x in a);d=int(d)
        if d<0:a=tuple(-x for x in a);d=-d
        g=reduce(gcd,a,d)
        self.a=tuple(x//g for x in a);self.d=d//g
    @classmethod
    def rational(cls,q):
        q=Fraction(q);a=[0]*54;a[0]=q.numerator;return cls(a,q.denominator)
    @classmethod
    def coefficients(cls,v):
        v=list(map(Fraction,v));d=lcm(*(t.denominator for t in v))
        return cls([t.numerator*(d//t.denominator) for t in v],d)
    def __add__(self,o):
        g=gcd(self.d,o.d);u=o.d//g;v=self.d//g
        return E([u*x+v*y for x,y in zip(self.a,o.a)],self.d*u)
    def __neg__(self):return E([-x for x in self.a],self.d)
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        out=[0]*54
        aa=[(i,x) for i,x in enumerate(self.a) if x]
        bb=[(i,x) for i,x in enumerate(o.a) if x]
        for i,x in aa:
            for j,y in bb:
                xy=x*y
                for k,c in TAB[i,j]:out[k]+=c*xy
        return E(out,self.d*o.d)
    def __pow__(self,n):
        assert n>=0;out=ONE;base=self
        while n:
            if n&1:out=out*base
            n//=2
            if n:base=base*base
        return out
    def __eq__(self,o):return self.a==o.a and self.d==o.d
    def sigma(self,k):
        out=[0]*54
        for n,v in enumerate(self.a):
            if not v:continue
            i,j=divmod(n,6)
            for jj,c in zp(j+3*i*k):out[6*i+jj]+=c*v
        return E(out,self.d)
def mon(i,j):
    a=[0]*54;a[6*i+j]=1;return E(a)
ZERO=E([0]*54);ONE=E.rational(1);z=mon(0,1);b=mon(1,0)
assert z**6+z**3+ONE==ZERO and b**9==E.rational(53)*z**3
ell=z-b**3*z**8
def ev(co,x):
    out=ZERO
    for c in reversed(co):out=out*x+E.rational(c)
    return out
lower=[ev(co,ell) for co in D['lower_units']]
candidates=[ev(co,b*z**j) for co in D['upper_candidates'] for j in range(3)]
units=lower+candidates
roots=[E.coefficients(c) for c in D['roots']]
cube_checks=[];norm_checks=[]
for k,(v,ex) in enumerate(zip(roots,D['root_exponents'])):
    pos=ONE;neg=ONE
    for u,a in zip(units,ex):
        if a>0:pos=pos*u**a
        if a<0:neg=neg*u**(-a)
    assert v**3*neg==pos,('cube',k)
    cube_checks.append(k+1)
    nr=v*v.sigma(1)*v.sigma(2)
    assert nr.sigma(1)==nr,('norm-fixed',k)
    co=[row[k] for row in D['lower_norm_coordinates']]
    pos=E.rational(D['lower_norm_signs'][k]);neg=ONE
    for u,a in zip(lower,co):
        if a>0:pos=pos*u**a
        if a<0:neg=neg*u**(-a)
    assert nr*neg==pos,('norm',k)
    norm_checks.append(k+1)

def records(p):return [json.loads(x) for x in p.read_text().splitlines() if x.startswith('{')]
W=next(x for x in records(R/'code/e53_upper_witness_verify.out') if x['type']=='literal_unit_witness_verification')
C=S.Matrix(W['root_character_matrix']);L=S.Matrix(W['with_included_lower_characters'])[:,:15]
def independent_columns(M):
    rows={};selected=[]
    for j in range(M.cols):
        v=[int(x)%3 for x in M[:,j]]
        for p,w in sorted(rows.items()):
            a=v[p];v=[(x-a*y)%3 for x,y in zip(v,w)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is None:continue
        v=[pow(v[p],-1,3)*x%3 for x in v];rows[p]=v;selected.append(j)
    return selected
sel=independent_columns(L.row_join(C));extra=[j-15+1 for j in sel if j>=15]
assert len(sel)==5 and len(extra)==3
five=(L.row_join(C)).extract(range(5),sel)
assert int(five.det())%3!=0
NC=S.Matrix(D['lower_norm_coordinates']);selN=independent_columns(NC)
assert len(selN)==9
base=NC[:,selN];extra_rows=[]
for i in range(15):
    e=S.eye(15)[:,i]
    if len(independent_columns(base.row_join(e)))>base.cols:
        base=base.row_join(e);extra_rows.append(i)
assert base.cols==15 and len(extra_rows)==6
B=NC[:,selN].row_join(3*S.eye(15)[:,extra_rows]);BI=B.inv()
def v3(n):
    n=abs(int(n));assert n
    a=0
    while n%3==0:n//=3;a+=1
    return a
H=S.Matrix(D['norm_lattice_HNF'])
assert v3(B.det())==6 and abs(int(H.det()))==729
assert all(S.denom(x)%3 for x in H.inv()*B)
assert all(S.denom(x)%3 for x in BI*H)
assert B*BI==BI*B==S.eye(15)
def mod3(x):
    x=S.Rational(x);assert x.q%3
    return int(x.p*pow(int(x.q),-1,3))%3
Q=(3*BI[9:,:]).applyfunc(mod3);QI=S.eye(15)[:,extra_rows]
assert (Q*QI-S.eye(6)).applyfunc(lambda x:int(x)%3)==S.zeros(6,6)
assert (Q*NC).applyfunc(lambda x:int(x)%3)==S.zeros(6,22)
def qm(A):
    a=[[str(x) for x in A.row(i)] for i in range(A.rows)]
    assert S.Matrix([[S.Rational(x) for x in row] for row in a])==A
    return a
out={'status':'PASS','independent_exact_relative_cube_identities':cube_checks,
     'independent_exact_relative_norm_identities':norm_checks,
     'five_character_columns':sel,'three_new_root_indices':extra,
     'five_character_matrix_first_five_rows':qm(five),
     'five_character_determinant':int(five.det()),
     'norm_root_basis_indices':[j+1 for j in selN],
     'norm_included_lower_cube_indices':[j+1 for j in extra_rows],
     'norm_basis':qm(B),'norm_basis_inverse':qm(BI),
     'norm_basis_determinant':int(B.det()),'norm_lattice_index':729,
     'norm_congruence_matrix_mod_three':qm(Q),'norm_quotient_right_inverse':qm(QI),
     'norm_basis_to_HNF':qm(H.inv()*B),'HNF_to_norm_basis':qm(BI*H),
     'scope':'Independent rational relative-ring arithmetic. No imported executable or upper BNF. Candidate S-unit divisor support and local positive characters are separately verified by the GP source.',
     'input_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [P,R/'code/e53_upper_witness_verify.out']}}
text=json.dumps(out,indent=2)+'\n';(R/'code/e53_literal_unit_ring.json').write_text(text);print(text,end='')
