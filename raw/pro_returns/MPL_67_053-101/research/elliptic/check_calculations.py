"""Exact arithmetic support; the general arguments are in proofs.md."""
from fractions import Fraction
from pathlib import Path
from datetime import datetime,timezone
import json

def matmul(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
I=[[1,0],[0,1]]
split=[[1,0],[0,-1]]
nonsplit=[[1,1],[0,-1]]
r=[[0,-1],[1,0]]
rinv=[[0,1],[-1,0]]
assert matmul(split,split)==I and matmul(nonsplit,nonsplit)==I
assert matmul(matmul(r,split),rinv)==[[-1,0],[0,1]]

def ring_add(x,y):return(x[0]+y[0],x[1]+y[1])
def ring_mul(x,y):
 a,b=x;c,d=y
 return(a*c-3*b*d,a*d+b*c+b*d)
def ring_neg(x):return(-x[0],-x[1])
def rmm(a,b):
 return [[ring_add(ring_mul(a[i][0],b[0][j]),ring_mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
zero=(0,0);one=(1,0);minus=(-1,0)
slopes=[(1,0),(0,1),(1,1)]
rmatrices=[]
for lam in slopes:
 a=[[one,zero],[ring_neg(lam),minus]]
 assert rmm(a,a)==[[one,zero],[zero,one]]
 rmatrices.append(a)
assert Fraction(1,4)+Fraction(11,16)==Fraction(15,16)<1
assert [(x[0]%2,x[1]%2) for x in [one,minus]]==[(1,0),(1,0)]
f4products={}
for x in slopes:
 for y in slopes:
  a,b=ring_mul(x,y)
  out=(a%2,b%2)
  assert out in slopes
  f4products[str((x,y))]=out
hexratio=4*Fraction(1)-4*Fraction(1,2)+1
assert hexratio==3
orbits={}
for n in [2,4,6]:
 o=[];remaining=set(range(n))
 while remaining:
  j=min(remaining);orb=sorted({(j+2*k)%n for k in range(n)});o.append(orb);remaining-=set(orb)
 assert len(o)==2
 orbits[n]={'rotation_conjugacy_orbits':o,'sigma_and_minus_sigma_conjugate':n//2 in o[0]}
result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'method':'exact rational/integer arithmetic; no handwriting or OCR input','hexagonal_quadratic_ratio':str(hexratio),'norm_euclidean_bound':'15/16','ring':'Z[w], w^2-w+3=0','ring_involutions':rmatrices,'residue_nonzero_slopes':slopes,'unit_image_in_F4':[(1,0)],'nonzero_slope_orbits':3,'total_split_plus_nonsplit_classes':4,'dihedral_checks':orbits,'H2_lattice_index_split':2,'H2_lattice_index_nonsplit':1,'limitations':'Class counts rely on the general triple-equivalence and unit-orbit proof in proofs.md; no external Lean certificate was executed.'}
Path(__file__).with_name('calculation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
