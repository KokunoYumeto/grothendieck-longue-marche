"""Finite chamber groupoids, exact braid combing, and the five/six-point tables.
Integer braid words use sigma_i = i, sigma_i^{-1} = -i.
Lists record the multiplication/traversal order used by action().
No numerical braid or curve approximation is used.
"""
import itertools,json
from pathlib import Path

def red(w):
 s=[]
 for a in w:
  if s and s[-1]==-a:s.pop()
  else:s.append(a)
 return tuple(s)
def inv(w):return tuple(-a for a in reversed(w))
def subst(w,imgs):return red(a for k in w for a in (imgs[k-1] if k>0 else inv(imgs[-k-1])))
def action(n,w):
 imgs=tuple((i,) for i in range(1,n+1))
 for j in w:
  i=abs(j);gen=[(k,) for k in range(1,n+1)]
  if j>0:gen[i-1]=(i,i+1,-i);gen[i]=(i,)
  else:gen[i-1]=(i+1,);gen[i]=(-(i+1),i,i+1)
  imgs=tuple(subst(x,gen) for x in imgs)
 return imgs
def eq(n,u,v):return action(n,u)==action(n,v)
def A(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))
def full(n):return tuple(range(1,n))*n
def pw(w,k):return w*k if k>=0 else inv(w)*(-k)
def permutation(n,w):
 p=list(range(1,n+1))
 for x in w:i=abs(x)-1;p[i],p[i+1]=p[i+1],p[i]
 return tuple(p)
def transport(p):
 a=list(range(1,len(p)+1));w=[]
 for pos,lab in enumerate(p):
  j=a.index(lab)
  while j>pos:
   a[j-1],a[j]=a[j],a[j-1];w.append(j);j-=1
 assert tuple(a)==p
 return tuple(w)
def swap(p,i):
 q=list(p);q[i-1],q[i]=q[i],q[i-1];return tuple(q)
def delete_last(n,w):
 p=list(range(1,n+1));out=[]
 for x in w:
  i=abs(x)-1
  if n not in p[i:i+2]:out.append((1 if x>0 else -1)*(i+1-(p.index(n)<i)))
  p[i],p[i+1]=p[i+1],p[i]
 assert tuple(p)==tuple(range(1,n+1))
 return red(out)
def link12(n,w):
 p=list(range(1,n+1));count=0
 for x in w:
  i=abs(x)-1
  if set(p[i:i+2])=={1,2}:count+=1 if x>0 else -1
  p[i],p[i+1]=p[i+1],p[i]
 assert tuple(p)==tuple(range(1,n+1)) and count%2==0
 return count//2
def conjugator(v,k):
 i=0
 while len(v)>2*i+1 and v[i]==-v[-1-i]:i+=1
 assert len(v)==2*i+1 and v[i]==k,(v,k)
 return v[:i]
def comb(n,w):
 """Return a word in signed pairs (i,j), in ascending fibre stages."""
 assert permutation(n,w)==tuple(range(1,n+1))
 if n==2:
  k=sum(w)//2;assert sum(w)%2==0
  return [(1,2,1 if k>0 else -1)]*abs(k)
 base=delete_last(n,w)
 residual=inv(base)+w
 c=conjugator(action(n,residual)[-1],n)
 fibre=red(x for x in c if abs(x)!=n)
 out=comb(n-1,base)+[(abs(x),n,1 if x>0 else -1) for x in fibre]
 return out
def expand(word):return tuple(x for i,j,s in word for x in (A(i,j) if s>0 else inv(A(i,j))))
def normalized(n,w):
 k=link12(n,w)
 reduced=pw(full(n),-k)+w
 out=comb(n,reduced)
 assert all((i,j)!=(1,2) for i,j,s in out)
 assert eq(n,w,pw(full(n),k)+expand(out))
 return k,out

data={}
for n in (3,4,5):
 perms=list(itertools.permutations(range(1,n+1)));edges=[];rels=[]
 for p in perms:
  for i in range(1,n):
   q=swap(p,i);w=transport(p)+(i,)+inv(transport(q))
   k,pure=normalized(n,w)
   edges.append(dict(source=p,target=q,sigma=i,transported_braid=w,central_power=k,moduli_word=pure))
  for i,j in itertools.combinations(range(1,n),2):
   u=(i,j,i) if j==i+1 else (i,j)
   v=(j,i,j) if j==i+1 else (j,i)
   assert eq(n,u,v)
   q=p
   for h in u:q=swap(q,h)
   r=p
   for h in v:r=swap(r,h)
   assert q==r
   rels.append(dict(source=p,target=q,left=u,right=v,type='braid' if j==i+1 else 'commutation'))
 data[str(n+1)]=dict(objects=perms,arrows=edges,relations=rels,base_full_turn=full(n),counts=[len(perms),len(edges),len(rels),1])
 print('M0,%d chamber objects/arrows/rank-two relations/central relation:'%(n+1),data[str(n+1)]['counts'])
 print('  All %d transported generators exactly combed and verified.'%len(edges))

# Compact presentation tables: c(u,v)=v^-1 u^-1 v u.
def C(u,v):return inv(v)+inv(u)+v+u
def conj(u,v):return u+v+inv(u)
a,b,x,y,z=[(i,) for i in range(1,6)]
base_braids=[A(1,3),A(2,3),A(1,4),A(2,4),A(3,4)]
phi_a=[inv(z)+x+z,conj(C(x,z),y),C(x,z)+z]
phi_b=[x,inv(z)+y+z,C(y,z)+z]
base_rels=[]
for h,images in [(a,phi_a),(b,phi_b)]:
 for v,img in zip((x,y,z),images):
  rel=h+v+inv(h)+inv(img)
  assert action(4,subst(rel,base_braids))==tuple((i,) for i in range(1,5))
  base_rels.append(rel)
print('M0,5 compact braid relations verified:',len(base_rels))
p,q,r,s=[(i,) for i in range(1,5)]
acts=[
 [inv(r)+p+r,conj(C(p,r),q),C(p,r)+r,s],
 [p,inv(r)+q+r,C(q,r)+r,s],
 [inv(s)+p+s,conj(C(p,s),q),conj(C(p,s),r),C(p,s)+s],
 [p,inv(s)+q+s,conj(C(q,s),r),C(q,s)+s],
 [p,q,inv(s)+r+s,C(r,s)+s]]
fib=[A(i,5) for i in range(1,5)]
for h,imgs in zip(base_braids,acts):
 for v,img in zip(fib,imgs):assert eq(5,conj(h,v),subst(img,fib))
# Free-word action composition (inverse actions via mirrored inverse braid).
def mirror(w):return tuple(-x for x in w)
# The fibre action is the inverse-convention Artin action, verified above.
inverse_acts=[[red(k for k in conjugator(action(5,conj(inv(h),v))[-1],5) if abs(k)!=5) for v in fib] for h in base_braids]
for f,g in zip(acts,inverse_acts):
 for i in range(1,5):
  assert subst(subst((i,),f),g)==(i,)
  assert subst(subst((i,),g),f)==(i,)
def apply_base(w,v):
 # h1 h2 acts on v by phi_h1(phi_h2(v)), rightmost first.
 for t in reversed(w):v=subst(v,acts[t-1] if t>0 else inverse_acts[-t-1])
 return v
for rel in base_rels:
 for i in range(1,5):assert apply_base(rel,(i,))==(i,)
print('M0,6 compact relations verified:',len(base_rels)+20)
print('M0,6 base-relation actions on F4 verified:',len(base_rels)*4)
data['compact']=dict(M05_generators=['A13','A23','A14','A24','A34'],M05_braid_words=base_braids,M05_relators=base_rels,M06_new_generators=['A15','A25','A35','A45'],M06_fibre_braid_words=fib,M06_actions=acts,M06_inverse_actions=inverse_acts)
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(data,indent=2)+'\n')
