"""Exact finite-field characters for changing the first norm seed."""
from fractions import Fraction as F
from pathlib import Path
import json
base=Path(__file__).resolve().parent
for q in (11,59):
 r=next(x for x in range(q)if x**3%q==3)
 def mul(x,y):
  a,b=x;c,e=y
  return ((a*c-r*r*b*e)%q,(a*e+b*c-r*b*e)%q)
 def pw(x,k):
  k%=q*q-1;z=(1,0)
  while k:
   if k&1:z=mul(z,x)
   x=mul(x,x);k//=2
  return z
 omega=(10,6)if q==11 else(58,6)
 achi=pw((0,1),(q*q-1)//3)
 exponent=next(i for i in range(3)if pw(omega,i)==achi)
 assert exponent
 correction=(-pow(exponent,-1,3))%3
 print('q',q,'alpha character',achi,'exponent',exponent,'required h_q exponent',correction)
 # rho2=pi^8*u_q, u_q=dprime^-8*alpha^-5.
 dp=649//q
 uq=mul((pow(dp,-8,q),0),pw((0,1),-5))
 # h_q has valuation3. Its unit residue is dprime^-4*alpha^-2*gamma_q^-3.
 gamma=((r*r+2)%q,(2+r)%q)if q==59 else(2,1)
 h_unit=mul(mul((pow(dp,-4,q),0),pw((0,1),-2)),pw(gamma,-3))
 stable=mul(pw(h_unit,(q*q-1)//3),pw(pw(uq,(q*q-1)//3),-2*3))
 assert stable==achi
 # The baseline beta2 unit has character omega, so this vanishes exactly.
 assert mul(omega,pw(stable,correction))==(1,0)
 print(' stable h_q character and corrected character PASS')
# Norm(a+b alpha+c alpha²)=a³+3b³+9c³-9abc.
for q,(a,b,c)in [(11,(2,1,0)),(59,(2,2,-1))]:
 assert a**3+3*b**3+9*c**3-9*a*b*c==q
 print('literal gamma norm',q,'PASS')
