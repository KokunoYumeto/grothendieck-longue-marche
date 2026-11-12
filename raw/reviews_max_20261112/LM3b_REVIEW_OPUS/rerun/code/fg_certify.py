#!/usr/bin/env python3
"""Certify reduction ranks of rational candidate bases and regenerate C++ input."""
import json
from pathlib import Path
P=65521
folder=Path(__file__).resolve().parent
obj=json.loads((folder/'fg_candidates.json').read_text())
def rank(rows,p):
 rows=[[x%p for x in row] for row in rows];i=0
 for j in range(len(rows[0]) if rows else 0):
  k=next((k for k in range(i,len(rows)) if rows[k][j]),None)
  if k is None:continue
  rows[k],rows[i]=rows[i],rows[k];u=pow(rows[i][j],-1,p);rows[i]=[(u*x)%p for x in rows[i]]
  for k in range(i+1,len(rows)):
   if rows[k][j]:
    u=rows[k][j];rows[k]=[(a-u*b)%p for a,b in zip(rows[k],rows[i])]
  i+=1
  if i==len(rows):break
 return i
report=[]
with open(folder/'fg_pentagon_input.txt','w') as f:
 f.write('12\n')
 for n in range(1,13):
  z=obj[str(n)];a=z['kernel'];r=rank(a,P)
  assert r==len(a)
  report.append({'weight':n,'rational_basis_size':len(a),'reduction_rank':r})
  f.write(f"{n} {len(z['words'])} {len(a)}\n")
  f.write(' '.join(z['words'])+'\n')
  for row in a:f.write(' '.join(str(c%P) for c in row)+'\n')
(folder/'fg_certify_results.json').write_text(json.dumps({'prime':P,'ranks':report},indent=2))
print('All 12 rational bases retain full rank modulo',P)
