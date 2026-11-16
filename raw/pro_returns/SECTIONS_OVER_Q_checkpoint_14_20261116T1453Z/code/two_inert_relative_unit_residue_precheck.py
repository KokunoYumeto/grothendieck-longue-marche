"""Exact scalar-unit comparison, separate from the pending relative-unit search."""
for q in (11,59):
 r=next(x for x in range(q)if x**3%q==3)
 def mul(x,y):
  a,b=x;c,e=y
  return ((a*c-r*r*b*e)%q,(a*e+b*c-r*b*e)%q)
 def pw(x,k):
  z=(1,0)
  while k:
   if k&1:z=mul(z,x)
   x=mul(x,x);k//=2
  return z
 u=((-r*r-2)%q,(-r)%q)
 chi=pw(u,(q*q-1)//3);omega=(10,6)if q==11 else(58,6)
 lam=next(i for i in range(3)if pw(omega,i)==chi)
 assert lam==(1 if q==11 else 2)
 print(q,'U residue',u,'U character',chi,'exponent relative to beta2 character',lam)
print('PASS: scalar U has character column (1,2); no scalar power cancels beta2 column (1,1).')
