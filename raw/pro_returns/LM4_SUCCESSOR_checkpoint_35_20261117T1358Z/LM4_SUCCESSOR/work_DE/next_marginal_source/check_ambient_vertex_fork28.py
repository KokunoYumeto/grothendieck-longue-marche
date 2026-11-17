#!/usr/bin/env python3
"""Literal all-word input to the vertex-tree fork; no subgroup enumeration."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_DE/next_marginal_source/annular_neck_reflection23.json'
d=json.loads(p.read_text())
eta={int(i):w for i,w in d['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return r
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red([x for w in ws for x in w])
def sub(w,mp):return mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w))
mp={1:[1],2:[5,4,-5],3:[2],4:[3],5:[5]}
z=sub(eta[1],mp)
gamma=[1,5,4,-5,-1,5];D=[2,3,-2]
w=mul(gamma,D,[-5,-2])
assert z==mul(gamma,[-4,-5,-1])
q=sub(sub([1,5,-1],eta),mp)
assert q==mul(w,[-5],inv(w))
assert len({(),tuple(D),(-4,)})==3
out={'status':'PASS','source':str(p.relative_to(ROOT)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'leaf_basis':['a','d','e','V4=f^-1Bf','f'],'eta_a':z,'gamma':gamma,'D':D,'w':w,'eta_ell':q,'three_distinct_leaf_directions':[[],D,[-4]],'scope':'Literal fork marking only. Uniform all-power tree immersion and off-core stabilizer arguments are proved in ambient_vertex_overlap28.md. No finite subgroup/coset census.'}
(ROOT/'work_DE/next_marginal_source/ambient_vertex_fork28.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact eta(a) branch, eta(ell) conjugator and three distinct leaf directions.')
print('eta(a)=gamma V4^-1 f^-1 a^-1; w=gamma (d e d^-1) f^-1 d^-1.')
