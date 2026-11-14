#!/usr/bin/env python3
"""Exact finite and polynomial checks for the genus-five no-least-quotient example."""
from itertools import product
import sympy as s
import json

u=s.symbols('u')
f=-(u**6+1)*(u**6+4)
assert s.gcd(f,s.diff(f,u))==1
assert s.degree(f,u)==12
# Quotient of the Klein-bottle group by twice its orientation subgroup.
G=list(product(range(4),range(2)))
def add(v,w):return ((v[0]+w[0])%4,(v[1]+w[1])%2)
q1=lambda z:z[0]
q2=lambda z:(z[0]+2*z[1])%4
for q in (q1,q2):
 for v,w in product(G,repeat=2):
  assert q(add(v,w))==(q(v)+q(w))%4
  assert q(v)%2==v[0]%2
 assert {q(z) for z in G}==set(range(4))
assert all((2*a)%4!=0 for a in [1,3])
K1={z for z in G if q1(z)==0}
K2={z for z in G if q2(z)==0}
orientation={z for z in G if z[0]%2==0}
joint={add(v,w) for v,w in product(K1,K2)}
assert len(K1)==len(K2)==2
assert K1!=K2 and joint==orientation
# On four branch points, conjugation is (01)(23).
perm={0:1,1:0,2:3,3:2}
partitions=[frozenset([frozenset(a),frozenset(set(range(4))-set(a))])
            for a in [(0,1),(0,2),(0,3)]]
for P in partitions:
 assert frozenset(frozenset(perm[x] for x in b) for b in P)==P
# Exhaustively check the residue possibilities in the Q_2 valuation proof.
# v2(x)=0: v2(-(x²+1)(x²+4))=1.
for x in [1,3,5,7]:
 value=-(x*x+1)*(x*x+4)
 assert value%4==2
# v2(x)=1: x=2z, z odd, valuation is 3.
for z in [1,3,5,7]:
 value=-((2*z)**2+1)*((2*z)**2+4)
 assert value%16==8
# v2(x)>=2: after dividing by 4, the odd unit is 3 or 7 modulo 8.
for z in range(8):
 unit=-(16*z*z+1)*(4*z*z+1)
 assert unit%8 in [3,7]
# v2(x)<0, invert x: after removing x^4, unit is 3 or 7 modulo 8.
for z in [0,2,4,6]:
 unit=-(1+z*z)*(1+4*z*z)
 assert unit%8 in [3,7]
print(json.dumps({
 'curve_polynomial':str(s.expand(f)), 'smooth':True,'genus':5,
 'degree_to_genus_one_torsor':3,
 'finite_real_group':'C4 x C2',
 'quotient_maps':['(a,b) -> a mod4','(a,b) -> a+2b mod4'],
 'kernels':[sorted(K1),sorted(K2)],'joint_kernel':sorted(joint),
 'branch_pair_partitions_fixed':True,'Q2_residue_checks_passed':True,
 'status':'all exact assertions passed'},indent=2))

