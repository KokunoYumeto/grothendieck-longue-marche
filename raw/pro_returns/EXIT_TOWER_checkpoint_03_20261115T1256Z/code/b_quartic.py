"""Exact five-point involution family and the 60 bipyramid-to-pyramid incidences.
The program verifies algebraic configurations and finite endpoint data.
It does not assign words to the other 1560 manuscript arrows.
"""
import itertools,json
from pathlib import Path
import sympy as S
I=S.I;oo=S.oo;r=S.symbols('r',positive=True)
def sim(x):return S.simplify(S.cancel(x))
def cr(z,a,b,c):
 if z==c:return oo
 if a==oo:return sim((b-c)/(z-c))
 if b==oo:return sim((z-a)/(z-c))
 if c==oo:return sim((z-a)/(b-a))
 if z==oo:return sim((b-c)/(b-a))
 return sim((z-a)*(b-c)/((z-c)*(b-a)))
P=tuple(itertools.permutations(range(5)));ident=tuple(range(5))
def comp(p,q):return tuple(p[q[j]] for j in range(5))
def autom(points):
 c=[cr(points[j],*points[:3]) for j in (3,4)]
 return tuple(p for p in P if all(sim(cr(points[p[j]],*(points[p[k]] for k in range(3)))-v)==0 for j,v in zip((3,4),c)))
# Labels 0,1,2 are equatorial; 3,4 are the two poles in the bipyramid.
# (z+1)/(z-1) sends them to infinity,-i/sqrt(3),i/sqrt(3),-1,1.
def family(t):return (oo,-I*t,I*t,-S.Integer(1),S.Integer(1))
bp=family(1/S.sqrt(3));qp=family(S.Integer(1));middle=family(S.Rational(3,4))
HB=autom(bp);HQ=autom(qp);HH=autom(middle)
assert len(HB)==6 and len(HQ)==4 and len(HH)==2
assert set(HB)&set(HQ)==set(HH)
def cosets(H):
 left=set(P);out=[];rep={}
 while left:
  g=min(left);c={comp(g,h) for h in H};k=len(out)
  out.append(sorted(c));left-=c
  for p in c:rep[p]=k
 return out,rep
B,br=cosets(HB);Q,qr=cosets(HQ);E,er=cosets(HH)
edges=[dict(index=j,source=br[c[0]],target=qr[c[0]],representative=c[0]) for j,c in enumerate(E)]
assert len(B)==20 and len(Q)==30 and len(E)==60
assert all(sum(e['source']==j for e in edges)==3 for j in range(20))
assert all(sum(e['target']==j for e in edges)==2 for j in range(30))
# The original coordinate transformation and the quartic parameter.
zeta=(-1+I*S.sqrt(3))/2
M=lambda z: S.Integer(1) if z==oo else (oo if z==1 else sim((z+1)/(z-1)))
orig=(S.Integer(1),zeta,zeta**2,S.Integer(0),oo)
assert all(x==y or sim(x-y)==0 for x,y in zip(tuple(M(x) for x in orig),bp))
mu=I*(r-1/r)
assert sim(mu.subs(r,1/S.sqrt(3))+2*I/S.sqrt(3))==0
assert mu.subs(r,1)==0
z,nu=S.symbols('z nu');f=z**4-nu*z**2+1
disc=S.factor(S.discriminant(f,z))
assert disc==16*(nu-2)**2*(nu+2)**2
assert S.factor(f.subs(nu,0))==z**4+1
print('Bipyramid, square-pyramid, interior holomorphic stabilizer orders:',len(HB),len(HQ),len(HH))
print('Exact family: infinity,-i*r,i*r,-1,1 ; 1/sqrt(3) <= r <= 1')
print('Quartic parameter: mu=i*(r-1/r); endpoints -2i/sqrt(3),0')
print('Quartic discriminant:',disc)
print('Finite f_B,s incidence: 20 source objects,30 targets,60 arrows; valencies3,2')
print('The parameter mu=0 is nonsingular and gives the square-pyramidal configuration.')
result=dict(scope='Explicit paths realizing the sixty f_B,s endpoints; no assertion identifying an unstated manuscript homotopy or the remaining arrows.',family=['infinity','-i*r','i*r','-1','1'],interval=['1/sqrt(3)','1'],mu='i*(r-1/r)',stabilizers=dict(bipyramid=HB,pyramid=HQ,interior=HH),source_objects=B,target_objects=Q,arrows=edges,counts=[20,30,60],discriminant=str(disc))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
