import sympy as s
z,h,b=s.symbols('z h b')
hx,hy,hz=s.symbols('hx hy hz')
F=hx**3+hy**3+hz**3-3*z*hx*hy*hz
W=hx+hy+z*hz
Xw=12*(z**3-1)*hz/W-9*z*z
Yw=36*(z**3-1)*(hx-hy)/W
Aw=-27*z*(z**3+8)
Bw=54*(z**6-20*z**3-8)
num=s.fraction(s.cancel(Yw**2-Xw**3-Aw*Xw-Bw))[0]
assert s.rem(num,F,hx)==0
H=s.det(s.hessian(F,(hx,hy,hz)))
assert s.rem(H-216*(1-z**3)*hx*hy*hz,F,hx)==0
print('Hesse cubic exact Weierstrass transformation and constant nine flexes verified.')
B=z**6-20*z**3-8
J=z**3*(z**3+8)**3/(64*(z**3-1)**3)
assert s.cancel(1-J+B**2/(64*(z**3-1)**3))==0
u=z*(z**3+8)/(4*(z**3-1))
v=-h**2/(4*b*(z**3-1))
num=s.fraction(s.cancel(u**3+b*v**3-1))[0]
assert s.rem(num,h**3-b*B,h)==0
assert s.gcd(B,s.diff(B,z))==1
print('J=z^3(z^3+8)^3/[64(z^3-1)^3]')
print('1-J=-(z^6-20z^3-8)^2/[64(z^3-1)^3]')
print('h^3=beta*(z^6-20z^3-8), u=z(z^3+8)/[4(z^3-1)], v=-h^2/[4beta(z^3-1)]')
print('Verified u^3+beta*v^3=1 exactly modulo the genus4 curve equation.')
print('The degree6 branch polynomial is squarefree; the threefold cover has six ramified finite points and three unramified points at infinity: genus4.')
for level,group_order,image_order,components in [(3,12,4,3),(4,24,24,1),(5,60,60,1),(7,168,168,1)]:
 inertia=(1,2,level//s.gcd(3,level))
 two_g_minus_two=sum(3*image_order*(1-s.Rational(1,e)) for e in inertia)
 genus=1+two_g_minus_two/2
 assert genus.is_Integer
 print('level,geometric group order,Fermat image order,components,inertias,pullback genus=',level,group_order,image_order,components,inertia,genus)

# The four exact projective modular groups and the Fermat subgroup images.
for modulus in (3,4,5,7):
 def canon(A):
  A=tuple(x%modulus for x in A)
  return min(A,tuple((-x)%modulus for x in A))
 ident=canon((1,0,0,1))
 def mul(A,B):
  a,b,c,d=A;e,f,g,h=B
  return canon((a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))
 def inv(A):
  a,b,c,d=A;return canon((d,-b,-c,a))
 def closure(gens):
  result={ident};todo=[ident]
  while todo:
   x=todo.pop()
   for gen in gens:
    y=mul(x,gen)
    if y not in result:result.add(y);todo.append(y)
  return result
 Smat=canon((0,-1,1,0));Tmat=canon((1,1,0,1))
 A=mul(Smat,Tmat);B=Smat;C=inv(mul(A,B))
 G=closure([A,B])
 comm=[mul(mul(mul(x,y),inv(x)),inv(y)) for x in G for y in G]
 derived=closure(comm)
 H=closure(list(derived)+[mul(mul(A,A),A),mul(mul(B,B),B)])
 def order(g):
  n=1;x=g
  while x!=ident:x=mul(x,g);n+=1
  return n
 cusp_generators=[]
 for peripheral in (A,B,C):
  cube=mul(mul(peripheral,peripheral),peripheral)
  cusp_generators += [mul(mul(x,cube),inv(x)) for x in G]
 I=closure(cusp_generators)
 assert I==H
 assert len(G)=={3:12,4:24,5:60,7:168}[modulus]
 assert len(H)=={3:4,4:24,5:60,7:168}[modulus]
 assert tuple(order(x) for x in (A,B,C))==(3,2,modulus)
 print('modular_level,G,derived,H,cusp_image,peripheral_orders=',modulus,len(G),len(derived),len(H),len(I),tuple(order(x) for x in (A,B,C)))
 if modulus==3:
  inertia={mul(mul(x,B),inv(x)) for x in G}
  assert len(inertia)==3 and ident not in inertia and inertia<=H
  assert all(order(x)==2 for x in inertia)
  print('X3: three distinct nonzero V4 cusp inertias; each nontrivial quadratic character branches at two cusps.')
 if modulus==4:
  assert len(derived)==12 and A in derived and B not in derived and C not in derived
  print('X4 sign is unramified at J=0 and ramified at J=1,infinity: kappa2(1-J), up to global constant.')

# Uniform local-three identity on the least cubic.
xx,yy,bb,zz=s.symbols('xx yy bb zz')
Epoly=yy*yy+yy-xx**3+1
def field_reduce(expr):
 num=s.fraction(s.cancel(expr))[0]
 num=s.rem(num,bb**3-3,bb)
 num=s.rem(num,zz**2+zz+1,zz)
 return s.rem(num,Epoly,yy)
slope=(1-yy)/(bb*zz-xx)
xnew=slope*slope-xx-bb*zz
ynew=-yy-1+slope*(xx-xnew)
gnew=(bb*bb*zz*zz*xnew-ynew-2)/(bb*bb*xnew-ynew-2)
assert field_reduce(gnew*(zz-yy)-(zz+2))==0
print('Exact uniform identity: g(Q+(b*zeta,1))=(zeta+2)/(zeta-y(Q)).')
print('At L_3, v(zeta+2)=3; rational Q has y not congruent1 modulo3 when integral, so the translated ratio has odd valuation.')
