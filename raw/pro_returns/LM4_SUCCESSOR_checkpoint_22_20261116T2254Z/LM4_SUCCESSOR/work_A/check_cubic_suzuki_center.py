"""Exact invariant normalized bar H² for the 64-element cubic class-two group.
No classification theorem is used. This is a local next-layer probe only.
"""
from pathlib import Path
def mul8(a,b):
 r=0
 while b:
  if b&1:r^=a
  a<<=1
  if a&8:a^=11
  b>>=1
 return r
def pw(a,n):
 r=1
 while n:
  if n&1:r=mul8(r,a)
  a=mul8(a,a);n>>=1
 return r
G=[(a,z)for a in range(8)for z in range(8)];ix={g:i for i,g in enumerate(G)}
def op(g,h):
 a,z=g;b,w=h
 return(a^b,z^w^mul8(mul8(a,a),b))
M=[[ix[op(g,h)]for h in G]for g in G]
D=[ix[(mul8(2,a),mul8(pw(2,3),z))]for a,z in G]
assert all(D[M[i][j]]==M[D[i]][D[j]]for i in range(64)for j in range(64))
assert all(M[M[i][j]][k]==M[i][M[j][k]]for i in range(64)for j in range(64)for k in range(64))
seen=set();orbits=[]
for i in range(1,64):
 if i in seen:continue
 o=[];j=i
 while j not in o:o.append(j);j=D[j]
 assert len(o)==7;orbits.append(o);seen.update(o)
oi={j:i for i,o in enumerate(orbits)for j in o}
porbits=[];po={}
for i in range(1,64):
 for j in range(1,64):
  if (i,j)in po:continue
  o=[];a,b=i,j
  while(a,b)not in o:o.append((a,b));a,b=D[a],D[b]
  assert len(o)==7
  for p in o:po[p]=len(porbits)
  porbits.append(o)
def term(a,b):return 0 if not a or not b else 1<<po[a,b]
piv={}
def insert(v):
 while v:
  j=v.bit_length()-1
  if j in piv:v^=piv[j]
  else:piv[j]=v;return True
 return False
for o in orbits:
 a=o[0]
 for b in range(64):
  for c in range(64):
   insert(term(b,c)^term(M[a][b],c)^term(a,M[b][c])^term(a,b))
zdim=len(porbits)-len(piv)
# Invariant normalized coboundaries are computed on pair representatives.
bc=[]
for q in range(len(orbits)):
 v=0
 for j,o in enumerate(porbits):
  a,b=o[0];ab=M[a][b]
  x=int(oi[a]==q)^int(oi[b]==q)^int(ab!=0 and oi[ab]==q)
  v|=x<<j
 bc.append(v)
bp={}
for v in bc:
 assert all((v&r).bit_count()%2==0 for r in piv.values())
 while v:
  j=v.bit_length()-1
  if j in bp:v^=bp[j]
  else:bp[j]=v;break
print('Actual cubic group: order64; strict scalar7 automorphism; associativity PASS')
print('Invariant normalized1-/2-cochain dimensions:',len(orbits),len(porbits))
print('Cocycle equation rank:',len(piv),'Z2 dimension:',zdim,'B2 dimension:',len(bp))
print('H2(group,F2)^C7 dimension:',zdim-len(bp))
print('Local group only; no full source scalar identification or negative norm conclusion.')
