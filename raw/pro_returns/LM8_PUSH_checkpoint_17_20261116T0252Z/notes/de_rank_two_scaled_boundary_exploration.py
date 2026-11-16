from sympy import Matrix,eye,ZZ
from sympy.matrices.normalforms import smith_normal_form
import json
rows=[]
for r,N in [(0,1),(1,1),(0,2),(1,2),(2,2)]:
 n=5**N
 T=Matrix(n,n,lambda i,j:int(i==(j+1)%n))
 Pi=Matrix(n,n,lambda i,j:int(i==(2*j)%n))
 M=(eye(n)+T**(5**r))*(eye(n)+T)**3*Pi
 D=smith_normal_form(M-eye(n),domain=ZZ)
 vals=[];free=0
 for i in range(n):
  z=abs(int(D[i,i]));v=0
  if z==0:free+=1;continue
  while z%5==0:z//=5;v+=1
  if v:vals.append(v)
 rows.append({'r':r,'N':N,'dimension':n,'free_rank':free,'five_torsion_valuations':vals})
print(json.dumps(rows,indent=2))
