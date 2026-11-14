#!/usr/bin/env python3
"""Finite-prime cubic residue certificate for the actual eight L2 units."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'inputs/e122_witnesses.json').read_text())
U=[[Q(x) for x in row] for row in D['upper_candidates'][:8]]
def rank(M):
 a=[[int(x)%3 for x in row] for row in M];k=0
 for j in range(9):
  i=next((i for i in range(k,len(a)) if a[i][j]),None)
  if i is None:continue
  a[k],a[i]=a[i],a[k]
  t=pow(a[k][j],-1,3);a[k]=[t*x%3 for x in a[k]]
  for i in range(len(a)):
   if i!=k:
    t=a[i][j];a[i]=[(x-t*y)%3 for x,y in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k
def inverse(M):
 n=len(M);a=[[x%3 for x in row]+[int(i==j) for j in range(n)] for i,row in enumerate(M)]
 for j in range(n):
  i=next(i for i in range(j,n) if a[i][j]);a[i],a[j]=a[j],a[i]
  t=pow(a[j][j],-1,3);a[j]=[t*x%3 for x in a[j]]
  for i in range(n):
   if i!=j:
    t=a[i][j];a[i]=[(x-t*y)%3 for x,y in zip(a[i],a[j])]
 assert all(a[i][:n]==[int(i==j) for j in range(n)] for i in range(n))
 return [row[n:] for row in a]
def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*len(s[p*p:n+1:p])
 return [p for p in range(n+1) if s[p]]
def evaluate(co,x,p):
 y=0
 for a in reversed(co):y=(y*x+a.numerator*pow(a.denominator,-1,p))%p
 return y
rows=[];selected=[];tested=0;bound=10000
for p in primes(bound):
 if p in (3,53) or p%3!=1:continue
 for b in range(1,p):
  b9=pow(b,9,p)
  if (b9*b9+53*b9+2809)%p:continue
  z=b9*pow(53,-1,p)%p
  assert (z*z+z+1)%p==0 and z!=1
  values=[z]+[evaluate(co,b,p) for co in U]
  assert all(values)
  ph=[pow(x,(p-1)//3,p) for x in values]
  log={pow(z,i,p):i for i in range(3)}
  rr=[log[x] for x in ph];tested+=1
  if rank(rows+[rr])>len(rows):
   rows.append(rr);selected.append({'prime':p,'beta_residue':b,'zeta_residue':z,'values':values,'cubic_powers':ph,'row':rr})
  if len(rows)==9:break
 if len(rows)==9:break
out={'status':'PASS' if len(rows)==9 else 'RANK_INCOMPLETE','rank':len(rows),'bound':bound,'prime_ideals_tested':tested,
 'selected_primes':selected,'residue_matrix':rows,'inverse_mod3':inverse(rows) if len(rows)==9 else None,
 'input_sha256':hashlib.sha256((R/'inputs/e122_witnesses.json').read_bytes()).hexdigest(),
 'scope':'The rows are actual maps at degree-one primes of the specified maximal order. Rank9 proves the literal mu3 plus eight ordinary units form a full basis after multiplication completion at3; no BNF class or regulator assertion is used.'}
if len(rows)==9:
 inv=out['inverse_mod3'];assert all(sum(rows[i][k]*inv[k][j] for k in range(9))%3==int(i==j) for i in range(9) for j in range(9))
s=json.dumps(out,indent=2)+'\n';(R/'code/e53_ordinary_saturation.json').write_text(s);print(s,end='')
