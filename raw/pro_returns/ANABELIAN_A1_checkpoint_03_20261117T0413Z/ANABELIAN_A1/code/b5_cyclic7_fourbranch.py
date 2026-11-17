#!/usr/bin/env python3
"""Exact complete zeta polynomials of cyclic-seven four-branch targets over F8.
Models y^7=x*((x+1)/(x+lambda))^b, b=1,2,3, lambda in F8-{0,1}.
Counts every point over F8^m for m=1,...,6. New exploratory file.
"""
import json,time
from pathlib import Path
import sympy as sp
mods={3:11,6:67,9:529,12:4179,15:32771,18:262273}
def table(n,mod):
 q=1<<n;ex=[];lg=[-1]*q;x=1
 for i in range(q-1):
  assert lg[x]==-1,(n,mod,i)
  lg[x]=i;ex.append(x)
  x<<=1
  if x&q:x^=mod
 assert x==1
 return ex,lg
start=time.monotonic();counts={(b,j):[] for b in (1,2,3) for j in range(1,7)};embeddings=[]
for m in range(1,7):
 n=3*m;q=1<<n;ex,lg=table(n,mods[n]);period=q-1
 alphas=[ex[(period//7)*i] for i in range(1,7)]
 alpha=min(a for a in alphas if ex[(lg[a]*3)%period]^a^1==0)
 embeddings.append(dict(field_degree=n,modulus=mods[n],alpha=alpha))
 for j in range(1,7):
  lam=ex[(lg[alpha]*j)%period];cs=[0,0,0]
  for x in range(2,q):
   if x==lam:continue
   a=lg[x]%7;d=(lg[x^1]-lg[x^lam])%7
   for b in (1,2,3):
    if (a+b*d)%7==0:cs[b-1]+=1
  for b in (1,2,3):counts[b,j].append(4+7*cs[b-1])
 print('field',q,'seconds',time.monotonic()-start,'counts',{f'{b},{j}':counts[b,j][-1] for b,j in counts},flush=True)
T=sp.symbols('T');records=[]
for (b,j),Ns in counts.items():
 a=[1]
 for k in range(1,7):
  s=sum(a[k-i]*(Ns[i-1]-8**i-1) for i in range(1,k+1))
  assert s%k==0
  a.append(s//k)
 full=a+[8**(k-6)*a[12-k] for k in range(7,13)]
 ss=all(c%(2**((3*k+1)//2))==0 for k,c in enumerate(a) if k)
 poly=sum(c*T**i for i,c in enumerate(full))
 records.append(dict(b=b,lambda_exponent=j,counts=Ns,L_coefficients=full,
  supersingular=ss,factorization=str(sp.factor(poly))))
 print('record',json.dumps(records[-1]),flush=True)
out=dict(models='y^7=x*((x+1)/(x+lambda))^b over F8, alpha^3+alpha+1=0, lambda=alpha^j',embeddings=embeddings,records=records,seconds=time.monotonic()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
