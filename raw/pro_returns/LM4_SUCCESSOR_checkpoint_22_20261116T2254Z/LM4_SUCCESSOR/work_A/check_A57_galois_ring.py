"""Exact coefficient and fixed-line certificate for A57, regenerated after recovery."""
from itertools import permutations,product
f=[3,1,2,1];g=[3,2,3,1]
fg=[0]*7
for i,a in enumerate(f):
 for j,b in enumerate(g):fg[i+j]=(fg[i+j]+a*b)%4
assert fg==[1]*7
def rmul(a,b):
 z=[0]*5
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%4
 for n in range(4,2,-1):
  c=z[n]
  for j in range(3):z[n-3+j]=(z[n-3+j]-c*f[j])%4
 return tuple(z[:3])
one=(1,0,0);root=(0,1,0);v=one;powers=[]
for j in range(1,8):v=rmul(v,root);powers.append(v)
assert powers[-1]==one and one not in powers[:-1]
assert all((sum((f[i]%2)*(a**i)for i in range(4))%2)for a in(0,1))
def comp(a,b):return tuple(a[b[i]]for i in range(len(a)))
def par(p):return sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))%2
Q=list(product(permutations(range(3)),[p for p in permutations(range(4))if par(p)==0]))
def qm(a,b):return(comp(a[0],b[0]),comp(a[1],b[1]))
s=((1,0,2),(1,0,3,2));unit=(tuple(range(3)),tuple(range(4)))
assert qm(s,s)==unit
cosets={frozenset((q,qm(q,s)))for q in Q}
fixed=sum(frozenset(qm(s,x)for x in c)==c for c in cosets)
assert len(Q)==72 and len(cosets)==36 and fixed==4
print('Hensel factor product:',fg)
print('Teichmuller generator successive powers:',powers)
print('Reduction is the irreducible cubic T^3+T+1 over F2: PASS')
print('S3 x A4 induced cosets:',len(cosets),'; s-fixed lines:',fixed,'; exchanged pairs:',(len(cosets)-fixed)//2)
print('Exact GR(4,3) and Bockstein fixed-line certificate: PASS')
