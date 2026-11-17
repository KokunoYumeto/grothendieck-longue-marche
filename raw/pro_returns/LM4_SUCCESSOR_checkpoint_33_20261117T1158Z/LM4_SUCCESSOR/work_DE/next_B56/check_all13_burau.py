"""Exact auxiliary matrix witness for the certified thirteen braid images.

This tests only an explicit representation. A nonidentity matrix certifies
nonidentity of a braid; an identity matrix alone is never used to do so.
"""
import json
from pathlib import Path
from membership_rigid7 import BRAIDS,multiply,inverse,substitute,balanced_commutator

HERE=Path(__file__).resolve().parent
n=6;p=101;t=2
Id=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
def gen(i,negative=False):
    out=[list(row) for row in Id];j=i-1
    block=((0,1),(pow(t,-1,p),(t-1)*pow(t,-1,p)%p)) if negative else ((1-t,t),(1,0))
    for x in range(2):
        for y in range(2):out[j+x][j+y]=block[x][y]%p
    return tuple(tuple(row) for row in out)
G={i:gen(i) for i in range(1,n)}
G.update({-i:gen(i,True) for i in range(1,n)})
for i in range(1,n):assert mm(G[i],G[-i])==Id
for i in range(1,n-1):assert mm(mm(G[i],G[i+1]),G[i])==mm(mm(G[i+1],G[i]),G[i+1])
for i in range(1,n):
    for j in range(1,n):
        if abs(i-j)>1:assert mm(G[i],G[j])==mm(G[j],G[i])
def ev(w,images):
    ans=Id
    for a in w:ans=mm(ans,images[a])
    return ans
B={i:ev(w,G) for i,w in BRAIDS.items()}
B.update({-i:ev(inverse(w),G) for i,w in BRAIDS.items()})
h=(6,11,-6,-5)
assert ev(h,B)==Id
raw=balanced_commutator([(i,) for i in range(1,15)])
images={i:(i,) for i in range(1,14)};images[14]=tuple(range(-13,0))
w=substitute(raw,images)
value=ev(w,B)
print('Unreduced Burau B6 representation over F101 at t=2: all defining braid relations PASS')
print('Certified h braid maps to identity matrix: PASS')
print('w matrix:')
for row in value:print(row)
print('w matrix nonidentity:',value!=Id)
noncommuting=[i for i in range(1,n) if mm(value,G[i])!=mm(G[i],value)]
assert value!=Id and noncommuting==list(range(1,n))
print('w matrix fails to commute with braid generators:',noncommuting)
print('w is a source commutator, so its braid exponent sum is0; a central braid image would be the identity.')
if value!=Id:print('PASS: this finite matrix certifies w is NOT in the rigid-seven kernel.')
else:print('INCONCLUSIVE: this representation supplies no nonidentity witness for w.')
if noncommuting:print('PASS: w also survives the finite braid image modulo the central full-twist image.')
(HERE/'all13_burau_witness.json').write_text(json.dumps({'prime':p,'t':t,'dimension':n,'w_matrix':value,'w_nonidentity':value!=Id,'noncommuting_generators':noncommuting},indent=2)+'\n')
