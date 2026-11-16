"""Exact Möbius and anti-Möbius audit for five-point configurations.
Requires SymPy. Every candidate is determined by the images of three marks.
No floating-point tolerance is used.
"""
import sympy as s
from itertools import permutations
from pathlib import Path
import json
I=s.I
inf=s.oo

def point(z):return s.Matrix([1,0]) if z==inf else s.Matrix([z,1])
def det(v,w):return s.expand(v[0]*w[1]-v[1]*w[0])
def simp(x):return s.simplify(s.expand_complex(x))
def normalizer(a,b,c):
 p,q,r=map(point,(a,b,c))
 A=det(r,p);B=det(r,q)
 return s.Matrix([[q[1]*A,-q[0]*A],[p[1]*B,-p[0]*B]])
def perm_order(p):
 q=tuple(range(len(p)))
 for k in range(1,121):
  q=tuple(p[q[j]] for j in range(len(p)))
  if q==tuple(range(len(p))):return k
 raise AssertionError

def automorphisms(K,anti=False):
 src=[s.conjugate(z) if z!=inf and anti else z for z in K]
 A=normalizer(*src[:3]);V=list(map(point,src));W=list(map(point,K))
 out=[]
 for tri in permutations(range(5),3):
  B=normalizer(*(K[j] for j in tri))
  M=B.adjugate()*A
  images=[]
  for v in V:
   w=M*v
   hits=[j for j,u in enumerate(W) if simp(det(w,u))==0]
   if len(hits)!=1:break
   images.append(hits[0])
  if len(images)==5:
   p=tuple(images)
   assert len(set(p))==5
   o=perm_order(p)
   if anti:o=s.ilcm(o,2)
   out.append({'permutation':p,'order':int(o)})
 return out

specs={
 'generic_C2': s.Integer(2),
 'C4_pyramid': I,
 'D3_bipyramid': I/s.sqrt(3),
 'D5_pentagon': s.sqrt(5)-2,
 'square_edge_added': 3-2*s.sqrt(2),
 'tetrahedron_axis_added': I*(2+s.sqrt(3)),
}
rows=[]
for name,t in specs.items():
 K=[inf,s.Integer(1),-s.Integer(1),t,-t]
 beta=s.simplify(t*t+1/(t*t))
 pos=automorphisms(K);neg=automorphisms(K,True)
 row={'name':name,'t':str(t),'beta':str(beta),'positive_order':len(pos),'extended_order':len(pos)+len(neg),'negative_orders':sorted({g['order'] for g in neg}),'negative_involution_fixed_marks':sorted(sum(a==b for a,b in enumerate(g['permutation'])) for g in neg if g['order']==2),'positive_permutations':pos,'negative_permutations':neg}
 rows.append(row)
 print({k:v for k,v in row.items() if not k.endswith('permutations')},flush=True)
assert [r['positive_order'] for r in rows]==[2,4,6,10,2,2]
assert [r['beta'] for r in rows]==['17/4','-2','-10/3','18','34','-14']
# A harmonic quadruple has these two beta values; an equianharmonic one has beta=-14.
l=s.symbols('l')
jnum=16*(l*l+14*l+1)**3
jden=l*(l-1)**4
harm=s.factor(jnum-1728*jden)
assert s.expand(harm-16*(l+1)**2*(l*l-34*l+1)**2)==0
print('harmonic polynomial:',harm,flush=True)
print('equianharmonic factor: lambda^2+14*lambda+1',flush=True)
Path(__file__).with_name('special_configurations.json').write_text(json.dumps(rows,indent=2))
print('PASS: all Möbius and anti-Möbius candidates checked exactly',flush=True)
