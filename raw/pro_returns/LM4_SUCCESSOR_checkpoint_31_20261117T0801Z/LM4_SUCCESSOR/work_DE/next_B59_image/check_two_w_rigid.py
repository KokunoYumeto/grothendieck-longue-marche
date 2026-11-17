"""Check whether the actual tetrahedral word with class-two image2w
already lies in the full rigid-seven kernel. Finite Burau nonidentity
is conclusive only in the negative direction.
"""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import BRAIDS,inverse
n=6;p=101;t=2
Id=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
def gen(i,neg=False):
 out=[list(row) for row in Id];j=i-1
 block=((0,1),(pow(t,-1,p),(t-1)*pow(t,-1,p)%p)) if neg else ((1-t,t),(1,0))
 for x in range(2):
  for y in range(2):out[j+x][j+y]=block[x][y]%p
 return tuple(tuple(row) for row in out)
G={i:gen(i) for i in range(1,n)};G.update({-i:gen(i,True) for i in range(1,n)})
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
word=[1,-2,3,5,-3,2,-1,-5]
value=ev(word,B)
print('All defining Burau braid relations and inverses:PASS')
print('Source word [e1 e2^-1 e3,e5]:',word)
print('Finite Burau image overF101 at t2:')
for row in value:print(row)
print('Image nonidentity:',value!=Id)
print('If nonidentity, the word is not in the full rigid-seven kernel; only its degree-two image vanishes.')
(HERE/'two_w_rigid_image.json').write_text(json.dumps({'word':word,'prime':p,'t':t,'matrix':value,'nonidentity':value!=Id},indent=2)+'\n')
