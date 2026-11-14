#!/usr/bin/env python3
"""Independent canonical verification of the fixed large-conductor witness.

This imports no C arithmetic, accelerator, or search/coset-index code.
The binary field is constructed by shift/XOR polynomial arithmetic. Divisor
relations use the earlier canonical coefficient-list Cantor implementation.
Cosets use a general integer Hermite lattice reduction, independently of the
search's tailored component normalization.
"""
from pathlib import Path
from math import gcd,isqrt,prod
import json,time,hashlib
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
from A_theta_F4_moduli_witnesses import pmul,peval
from A_theta_F4_remaining_Jacobian import Jacobian

ROOT=Path(__file__).parent

class IndependentField:
    def __init__(self,e,mod,gen):
        self.e=e;self.q=1<<e;self.mod=mod;self.logs=[-1]*self.q;self.exps=[];a=1
        for i in range(self.q-1):
            assert a and self.logs[a]==-1
            self.logs[a]=i;self.exps.append(a);a=self.rawmul(a,gen)
        assert a==1 and all(v>=0 for v in self.logs[1:])
        self.exps*=2
    def rawmul(self,a,b):
        r=0
        while b:
            if b&1:r^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return r
    def mul(self,a,b):return self.exps[self.logs[a]+self.logs[b]] if a and b else 0
    def inv(self,a):assert a;return self.exps[self.q-1-self.logs[a]]
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r

def prime(n):return n>=2 and all(n%p for p in range(2,isqrt(n)+1))

def mult_log(p):
    for g in range(2,p):
        d={};a=1
        while a not in d:d[a]=len(d);a=a*g%p
        if len(d)==p-1:
            assert a==1;return g,d
    raise AssertionError('no primitive generator')

def main():
    start=time.time();path=ROOT/'A_F4_large_theta_witness.json';raw=path.read_bytes();w=json.loads(raw)
    F=IndependentField(18,w['field_binary_modulus'],w['field_generator']);alpha=w['alpha'];assert F.mul(alpha,alpha)^alpha==1
    J=Jacobian(F,[1,1,1]);J.h=[alpha,1,1];J.f=pmul(J.h,[F.mul(alpha,alpha),1,1,1],F);J.T=(J.h,[])
    assert J.add(J.T,J.T)==J.zero
    def theta(x,y):
        h=peval(J.h,x,F);assert h
        Y=F.mul(h,y);D=J.check(([x,1],[Y] if Y else []));return J.add(D,J.T)
    G=theta(*w['theta_generator_point']);assert G==tuple(w['theta_generator_divisor'])
    n=w['odd_exponent'];ps=sorted(int(p) for p in w['odd_factorization']);assert all(prime(p) for p in ps) and prod(ps)==n
    assert J.times(G,n)==J.zero
    for p in ps:assert J.times(G,n//p)!=J.zero
    # Re-establish the full odd group exponent, without assuming a cyclic
    # Frobenius lattice or deducing rank from the group order alone.
    H=theta(*w['independent_seven_source']);H=J.times(H,4*n//7)
    assert H==tuple(w['independent_seven_divisor']) and J.times(H,7)==J.zero
    A=J.times(G,n//7);assert all(J.times(A,i)!=H for i in range(7))
    pi=sp.Matrix([[0,0,0,-16],[1,0,0,-8],[0,1,0,-1],[0,0,1,-2]])
    order=int((pi**9-sp.eye(4)).det());assert order==w['Jacobian_order']==4*7*n
    # Independent quotient-lattice computation for U_n/<2>.
    ml=[mult_log(p) for p in ps];phi=[p-1 for p in ps];v=[d[2] for _,d in ml]
    lattice=sp.diag(*phi).row_join(sp.Matrix(v));HNF=hermite_normal_form(lattice)
    assert HNF.shape==(4,4) and int(HNF.det())==w['primitive_orbit_count']==1296
    h=[[int(HNF[i,j]) for j in range(4)] for i in range(4)]
    def residue(a):
        a=list(a)
        for j in range(3,-1,-1):
            q=a[j]//h[j][j]
            for i in range(4):a[i]-=q*h[i][j]
        return tuple(a)
    assert residue(v)==(0,0,0,0)
    labels=set();count=0
    for z in w['witnesses']:
        i=z['index'];assert 0<i<n and gcd(i,n)==1
        label=residue([d[i%p] for p,(_,d) in zip(ps,ml)]);assert label not in labels;labels.add(label)
        point=theta(z['x'],z['y']);assert J.times(G,i)==point
        count+=1
        if count%256==0:print('verified',count,flush=True)
    assert len(labels)==1296
    out={'status':'PASS','fixed_witness_sha256':hashlib.sha256(raw).hexdigest(),
         'field_size':F.q,'binary_modulus':F.mod,'primitive_generator':w['field_generator'],
         'theta_generator_exact_order':n,'prime_factorization':ps,
         'independent_seven_rank_two':True,'exact_Jacobian_order':order,
         'independent_multiplicative_generators':[g for g,_ in ml],
         'independent_Hermite_lattice_basis':h,'lattice_index':int(HNF.det()),
         'exact_theta_multiple_relations_verified':count,'all_primitive_doubling_cosets_distinct_and_exhausted':True,
         'canonical_divisor_operations':J.add_count,'runtime_seconds':time.time()-start,
         'scope':'This verifies the positive geometric cover certificate; the section implication is A.C2.19/A.C2.20.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)

if __name__=='__main__':main()
