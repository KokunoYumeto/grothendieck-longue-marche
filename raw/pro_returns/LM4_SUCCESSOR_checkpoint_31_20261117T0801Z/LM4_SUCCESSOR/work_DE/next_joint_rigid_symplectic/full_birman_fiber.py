"""Actual last-moving-strand fiber on a certified free source subgroup."""
from pathlib import Path
import json,itertools,sys,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute,artin
j=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
initial=j['initial_order_labels'];keep={1,4,5,6,10,11};old=[x for x in initial if x in keep]
def delete(w,order,keep):
 a=list(order);out=[]
 for b in w:
  k=abs(b)-1
  if a[k] in keep and a[k+1] in keep:
   q=sum(x in keep for x in a[:k])+1;out.append(q if b>0 else -q)
  a[k],a[k+1]=a[k+1],a[k]
 assert a==list(order)
 return red(out)
tau=tuple(range(old.index(10)+1,6));new=old[:];x=new.pop(new.index(10));new.append(x)
braids={int(i)+1:mul(inv(tau),delete(w,initial,keep),tau) for i,w in j['C5'].items()}
h=(2,4,-2,-4)
letters=[1,-1,3,-3,5,-5,6,-6]
conj=[()]+[(x,) for x in letters]+[(x,y) for x in letters for y in letters if x!=-y]
records=[];start=time.time()
for g in conj:
 w=mul(g,h,inv(g));b=substitute(w,braids)
 forget=delete(b,range(6),set(range(5)))
 assert artin(forget,n=5)==tuple((i,) for i in range(1,6))
 A=artin(b,n=6);v=list(A[-1]);c=[]
 while len(v)>1:
  assert v[0]==-v[-1];c.append(v.pop(0));v.pop()
 assert v==[6]
 push=red(a for a in c if abs(a)!=6)
 records.append({'g':g,'source_word':w,'push':push})
 print('fiber conjugator',g,'word length',len(push),flush=True)

def fold(words):
 par=[0];edges=[]
 def vertex():par.append(len(par));return len(par)-1
 for w in words:
  v=0
  for i,a in enumerate(w):
   z=0 if i==len(w)-1 else vertex();edges.append((v,a,z));edges.append((z,-a,v));v=z
 def root(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 changed=True
 while changed:
  changed=False;seen={}
  for v,a,z in edges:
   v,z=root(v),root(z)
   if (v,a) in seen:
    y=root(seen[v,a])
    if y!=z:par[z]=y;changed=True
   else:seen[v,a]=z
 E={(root(v),a,root(z)) for v,a,z in edges};V={root(v) for v in range(len(par))}
 return {'rank':len(E)//2-len(V)+1,'vertices':len(V),'edges':len(E)//2}
for n in [9,len(records)]:print('SOURCE FREE RANK',n,'IMAGE',fold([x['push'] for x in records[:n]]),flush=True)
(HERE/'full_birman_fiber_certificate.json').write_text(json.dumps({'h':h,'old_order':old,'new_order':new,'tau':tau,'records':records,'rank':fold([x['push'] for x in records]),'elapsed':time.time()-start},indent=2)+'\n')
print('elapsed',time.time()-start,flush=True)
