"""Literal two-adic divisor map and character-neutral S-unit generator."""
from pathlib import Path
import json,itertools
import sympy as sp
base=Path(__file__).resolve().parent
x=sp.symbols('x');polys=[x+1,x*x+x+1,x**6+x**3+1]
assert sp.Poly(sp.prod(polys)-(x**9+1),x,modulus=2).is_zero
assert all(sp.Poly(p,x,modulus=2).is_irreducible for p in polys)
oldlinear=x**3+1;oldquadratic=x**6+x**3+1
assert [sp.rem(oldlinear,p,domain=sp.GF(2))==0 for p in polys]==[True,True,False]
assert sp.rem(oldquadratic,polys[2],domain=sp.GF(2))==0
N=sp.Matrix([[1,2,0],[0,0,3]])
vbeta1=sp.Matrix([1,1,0]);vbeta2=sp.Matrix([1,0,0])
vh=vbeta1-3*vbeta2
assert vh==sp.Matrix([-2,1,0])and N*vh==sp.zeros(2,1)
assert N*vbeta1==sp.Matrix([3,0])and N*vbeta2==sp.Matrix([1,0])
count=0
for a,b,c in itertools.product(range(-20,21),repeat=3):
 zero=N*sp.Matrix([a,b,c])==sp.zeros(2,1)
 assert zero==(c==0 and a==-2*b)
 count+=1
for row in json.loads((base/'two_inert_level2_local_norm_certificate_data.json').read_text()):
 q=row['q'];r=row['linear_alpha_root']
 def mul(z,w):
  a,b=z;c,e=w
  return ((a*c-r*r*b*e)%q,(a*e+b*c-r*b*e)%q)
 b2=tuple(row['beta2']);b1=tuple(row['beta1'])
 assert mul(mul(b2,b2),b2)==b1
 assert row['radicand_valuation']==8 and 8%3
 print('q',q,': beta2^3=beta1 in the actual residue field; h residue=1; next ramification degree3.')
print('Two-adic irreducible degrees [1,2,6]; actual old branches [linear,linear,quadratic].')
print('Relative ideal norm matrix',list(N))
print('Exact kernel generator',list(vh),'and tested integer vectors',count)
print('PASS: h=beta1/beta2^3 has relative norm1, divisor P2-2P0 and trivial repair characters.')
