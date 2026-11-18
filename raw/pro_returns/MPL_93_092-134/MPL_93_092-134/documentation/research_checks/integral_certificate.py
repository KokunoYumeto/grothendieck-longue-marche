"""Exact symbolic and finite checks for research notes D01-D11.
No manuscript image input; no transcription edits. This is not a Lean certificate.
"""
from itertools import product
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
out=[]
def emit(s):out.append(str(s)); print(s)
a,b,c,A,B,C=S.symbols('a b c A B C')
r1=A*a;r2=A*b+B*a*a;r3=A*c+2*B*a*b+C*a**3
certificate=S.expand(r2*r2-r1*r3-A*A*(b*b-a*c)-a**4*(B*B-A*C))
assert certificate==0
emit('Hasse composition numerator identity over Z: remainder = '+str(certificate))
emit('G = 12 G0: -2*(6*c)/a+3*(2*b/a)^2 - 12*(-c/a+(b/a)^2) = '+str(S.simplify(-12*c/a+12*b*b/a**2-12*(-c/a+(b/a)**2))))
for p,q in [(2,4),(3,9),(5,5),(7,7),(11,11)]:
 residues={d:comb(d,3)%p for d in range(3,q)}
 assert all(residues.values())
 emit(f'Linear induction coefficients binom(d,3) mod {p}, 3<=d<{q}: {residues}')
for p,q in [(2,4),(3,9),(5,5),(7,7)]:
 killed=[n for n in range(4*q+1) if all(comb(n,i)%p==0 for i in range(1,4))]
 assert killed==list(range(0,4*q+1,q))
 emit(f'Degrees <= {4*q} killed by Hasse derivatives 1,2,3 in F_{p}: {killed}')
# s=2t over F5, B=F5[t]/t5: homogeneous equation 2t(ct+d)=at+b.
sol=[];sl=[]
for aa,bb,cc,dd in product(range(5),repeat=4):
 if (bb%5,(aa-2*dd)%5,(2*cc)%5)==(0,0,0):
  det=(aa*dd-bb*cc)%5
  if det:sol.append((aa,bb,cc,dd,det))
  if det==1:sl.append((aa,bb,cc,dd))
assert len(sol)==4 and not sl
emit('s=2t/F5: invertible matrix solutions = '+str(sol))
emit('s=2t/F5: determinant-one solutions = '+str(sl))
# Exhaustive nilpotent-base check over A=F2[epsilon]/epsilon^2, all four alpha.
p=2;q=4
els=range(p*p)
def add(x,y):return (x%p+y%p)%p+p*((x//p+y//p)%p)
def neg(x):return (-x%p)%p+p*((-(x//p))%p)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 return (x%p*y%p)%p+p*((x%p*(y//p)+(x//p)*(y%p))%p)
def sc(n,x):
 return mul(n%p,x)
def padd(x,y):return tuple(add(xx,yy) for xx,yy in zip(x,y))
def psub(x,y):return tuple(sub(xx,yy) for xx,yy in zip(x,y))
def pmul(x,y,alpha):
 z=[0]*q
 for i,xx in enumerate(x):
  for j,yy in enumerate(y):
   k=i+j;v=mul(xx,yy)
   if k>=q:k-=q;v=mul(v,alpha)
   z[k]=add(z[k],v)
 return tuple(z)
def ppow(x,n,alpha):
 z=(1,0,0,0)
 while n:
  if n&1:z=pmul(z,x,alpha)
  x=pmul(x,x,alpha);n//=2
 return z
def unit(x,alpha):
 z=ppow(x,q,alpha)
 assert z[1:]==(0,0,0)
 return z[0]%p!=0
def hasse(x,i):
 return tuple(sc(comb(j+i,i),x[j+i]) if j+i<q else 0 for j in range(q))
zero=(0,0,0,0)
for alpha in els:
 matrices=[]
 for aa,bb,cc,dd in product(els,repeat=4):
  if sub(mul(aa,dd),mul(bb,cc))%p and unit((dd,cc,0,0),alpha):
   matrices.append((aa,bb,cc,dd))
 total=0
 for s in product(els,repeat=q):
  s1,s2,s3=(hasse(s,i) for i in range(1,4))
  if not unit(s1,alpha):continue
  if psub(pmul(s2,s2,alpha),pmul(s1,s3,alpha))!=zero:continue
  total+=1;matches=[]
  for aa,bb,cc,dd in matrices:
   if pmul(s,(dd,cc,0,0),alpha)==(bb,aa,0,0):matches.append((aa,bb,cc,dd))
  assert len(matches)==2,(alpha,s,matches)
 emit(f'A=F2[epsilon]/epsilon^2, alpha={alpha%2}+{alpha//2}epsilon: {total} etale solutions of N=0; each has exactly 2 invertible quadruples (one A^*-orbit).')
emit('Finite tests cover this named ring only; arbitrary-ring validity rests on the separate proof.')
emit('UTC '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'))
Path(__file__).with_suffix('.txt').write_text('\n'.join(out)+'\n')
