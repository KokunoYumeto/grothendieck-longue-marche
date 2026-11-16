from fractions import Fraction
import json

def choose(a,j):
 x=Fraction(1)
 for k in range(j): x*=Fraction(a-k,k+1)
 return x

def red(x):
 x=Fraction(x);return x.numerator*pow(x.denominator,-1,5)%5

def rank(A):
 A=[row[:] for row in A]; nr=len(A);nc=len(A[0]);r=0
 for j in range(nc):
  p=next((i for i in range(r,nr) if A[i][j]%5),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r]
  z=pow(A[r][j]%5,-1,5);A[r]=[(x*z)%5 for x in A[r]]
  for i in range(nr):
   if i!=r and A[i][j]%5:
    z=A[i][j];A[i]=[(a-z*b)%5 for a,b in zip(A[i],A[r])]
  r+=1
  if r==nr:break
 return r

def probe(d,a,b):
 N=5**d;m=N+2
 # alpha=N*a; beta=b. U2 modulo q=z^2((1+z)^N-1).
 alpha=N*a
 A=Fraction(-2*a); B=Fraction(a*(alpha+N))-Fraction(3*a*b,2)
 U=[2*choose(b,j) for j in range(m)];U[0]+=2
 for j in range(1,m):
  U[j]+=A*choose(N,j)
  if j>=2:U[j]+=B*choose(N,j-1)
 U=[red(x) for x in U]
 R=[[0]*m for _ in range(m)]
 for j in range(1,m+1):
  # (2z+z^2)^j
  for k in range(j,min(2*j,m)+1):
   coeff=red(choose(j,k-j))*pow(2,2*j-k,5)%5
   for i in range(k,m+1): R[i-1][j-1]=(R[i-1][j-1]+coeff*U[i-k])%5
 for i in range(m):R[i][i]=(R[i][i]-2)%5
 return {'d':d,'a':a,'b':b,'dim':m,'fixed_dimension_mod5':m-rank(R),'predicted_divisible_rank':d}
rows=[probe(d,a,b) for d in range(4) for a,b in [(1,1),(1,2),(2,1),(2,3)]]
print(json.dumps(rows,indent=2))
