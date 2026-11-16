from fractions import Fraction
from itertools import product

# A2: CRT compression of two signs. Idempotent is selected algebraically.
units=[1,5,7,11]
idem=[e for e in range(12) if e*e%12==e]
print('IDEMPOTENTS',idem)
for e in idem:
 u=(1-2*e)%12
 sols=[j for j in range(12) if 2*j%12==(1-u)%12]
 print('e,u,all half-solutions',e,u,sols)
assert [(1-2*e)%12 for e in idem]==[1,11,5,7]

# Actual W for parity one is noncentral in SL2(F3).
n=3
I=(1,0,0,1); S=(0,1,2,0); U=(1,1,0,1)
def mm(a,b):
 return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n for i in range(2) for j in range(2))
assert mm(S,U)!=mm(U,S)
print('S U',mm(S,U),'U S',mm(U,S))

# Exact truncated theta versus eta in t=q^(1/24).
N=10000
prod=[0]*(N+1);prod[1]=1
for k in range(1,N//24+1):
 shift=24*k
 for i in range(N,shift-1,-1): prod[i]-=prod[i-shift]
def theta(r):
 out=[0]*(N+1)
 for j in range(-101,102):
  if j%12==r and j*j<=N: out[j*j]+=1
 return out
th1=theta(1); th5=theta(5)
assert prod==[a-b for a,b in zip(th1,th5)]
print('ETA=theta1-theta5 verified through t^',N)
for a in units:
 image=[x-y for x,y in zip(theta(a%12),theta(5*a%12))]
 chi=1 if a in (1,11) else -1
 assert image==[chi*x for x in prod]
 print('u,eta eigenvalue',a,chi)

# Explicit pointed category: additive exponents of omega in Q/Z and c in Q/Z.
# Representatives 0,...,11; omega(a,b,c)=a floor((b+c)/12)/2.
M=12
def w(a,b,c): return Fraction(a*((b+c)//M),2)%1
def c(a,b): return Fraction(a*b,2*M)%1
for a,b,c0,d in product(range(M),repeat=4):
 # delta omega = 0: w(b,c,d)-w(a+b,c,d)+w(a,b+c,d)-w(a,b,c+d)+w(a,b,c)=0
 assert (w(b,c0,d)-w((a+b)%M,c0,d)+w(a,(b+c0)%M,d)-w(a,b,(c0+d)%M)+w(a,b,c0))%1==0
print('POINTED ASSOCIATOR pentagon verified for all 12^4 quadruples')
# All primitive 24th root powers preserve pentagon/hexagons by field automorphism.
for lam in (1,5,7,11,13,17,19,23):
 for a,b,c0 in product(range(M),repeat=3):
  # Hexagon equations in additive exponent convention.
  assert (lam*(c(a,(b+c0)%M)-c(a,b)-c(a,c0)-w(b,a,c0)+w(a,b,c0)+w(b,c0,a)))%1==0
  assert (lam*(c((a+b)%M,c0)-c(a,c0)-c(b,c0)+w(a,c0,b)-w(a,b,c0)-w(c0,a,b)))%1==0
print('POINTED HEXAGONS verified for all 8 multipliers modulo24 and all 12^3 triples')
print('DONE')
