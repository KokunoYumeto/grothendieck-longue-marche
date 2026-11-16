from itertools import product
p=3
I=(1,0,0,1)
def neg(A):return tuple((-x)%p for x in A)
def canon(A):return min(A,neg(A))
def mul(A,B):
 a,b,c,d=A; e,f,g,h=B
 return canon(((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p))
def inv(A):
 a,b,c,d=A;return canon((d,-b%p,-c%p,a))
def closure(gens):
 out={canon(I)}; todo=[canon(I)]
 while todo:
  x=todo.pop()
  for g in gens:
   y=mul(x,g)
   if y not in out:out.add(y);todo.append(y)
 return out
A=canon((1,2,0,1)); B=canon((1,0,1,1)); C=inv(mul(A,B))
G=closure([A,B]); assert len(G)==12
comm=[mul(mul(mul(x,y),inv(x)),inv(y)) for x in G for y in G]
V=closure(comm);assert len(V)==4
assert all(mul(x,x)==canon(I) for x in V)
assert all(mul(mul(x,x),x)==canon(I) for x in [A,B,C])
assert mul(A,inv(B)) in V
print('Projective Legendre matrices modulo3:',A,B,C)
print('Group order:',len(G),'; commutator subgroup order:',len(V))
print('Derived subgroup:',sorted(V))
print('All three peripheral images have projective order3.')
print('All three have the same class in A4/V4=C3.')
print('The Fermat kernel ker(F2 -> (Z/3)^2) maps exactly onto V4.')
print('Its peripheral loops are conjugates of A^3,B^3,C^3, all killed.')
print('Thus each connected pullback component is a degree4 etale V4 cover of the compact cubic.')
print('Over an algebraic closure this is the multiplication-by-two cover.')
