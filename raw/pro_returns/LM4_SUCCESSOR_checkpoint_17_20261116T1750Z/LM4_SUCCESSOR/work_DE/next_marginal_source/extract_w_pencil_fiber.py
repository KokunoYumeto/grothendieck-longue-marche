"""Actual source-based w-pencil actions with source strand11, not the last strand."""
from pathlib import Path
import itertools,json,time
from weighted_stallings import multiply as mul,inverse as inv,substitute as sub,WeightedFold
P=Path(__file__).resolve().parent
d=json.loads((P/'w_pencil_words.json').read_text());n=13;mark=d['source_position']+1
assert mark==11
remain=[i for i in range(1,n+1) if i!=mark];ren={i:j+1 for j,i in enumerate(remain)}
def fill(w):return mul(tuple((ren[abs(x)] if x>0 else -ren[abs(x)]) for x in w if abs(x)!=mark))
def artin(word,n=n):
 a={i:(i,) for i in range(1,n+1)}
 for s in word:
  k=abs(s);v,w=a[k],a[k+1]
  a[k],a[k+1]=(mul(v,w,inv(v)),v) if s>0 else (w,mul(inv(w),v,w))
 return a

def comp(a,b):return {i:sub(w,a) for i,w in b.items()}
def push(A):
 w=A[mark];h=[]
 while len(w)>1:
  assert w[0]==-w[-1];h.append(w[0]);w=w[1:-1]
 assert w==(mark,)
 return fill(h)
def point_hom(A):return inv(push(A))
def based(A):
 q=push(A)
 return {ren[i]:mul(inv(q),fill(A[i]),q) for i in remain}
def pair(i,j):
 assert i<j
 return tuple(range(j-1,i,-1))+(i,i)+tuple(range(-i-1,-j,-1))
def deletion(word):
 state=list(range(1,n+1));out=[]
 for s in word:
  k=abs(s)-1
  if state[k]!=mark and state[k+1]!=mark:
   j=sum(x!=mark for x in state[:k])+1;out.append(j if s>0 else -j)
  state[k],state[k+1]=state[k+1],state[k]
 assert state==list(range(1,n+1))
 return mul(out)
def core(w):
 while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
 return w
standards={ren[j]:pair(min(j,mark),max(j,mark)) for j in remain}
SA={j:artin(w) for j,w in standards.items()};fw={j:point_hom(a) for j,a in SA.items()}
for j,w in standards.items():assert artin(deletion(w),12)=={i:(i,) for i in range(1,13)}
f=WeightedFold(list(fw.values()));inverse_basis={j:f.rewrite((j,)) for j in range(1,13)}
assert all(w is not None for w in inverse_basis.values())
for j in range(1,13):assert sub(inverse_basis[j],fw)==(j,) and sub(fw[j],inverse_basis)==(j,)
first,second=list(SA.values())[:2]
assert point_hom(comp(first,second))==mul(point_hom(first),point_hom(second))
print('General distinguished-strand inverse-conjugator homomorphism and both12-basis inverses: PASS',flush=True)
acts={};invs={};new={};started=time.monotonic();checks=0
for index,row in enumerate(d['loops']):
 beta=tuple(row['word']);A=artin(beta);Ai=artin(inv(beta))
 if row['kind'] in ['old','filled']:
  a=based(A);ai=based(Ai)
  for j in range(1,13):
   assert sub(a[j],ai)==(j,) and sub(ai[j],a)==(j,)
   assert len(core(a[j]))==1
   conj=comp(A,comp(SA[j],Ai));assert point_hom(conj)==sub(fw[j],a)
   checks+=1
  acts[index]=a;invs[index]=ai
  print(index,row['name'],'action lengths',[len(a[j]) for j in range(1,13)],'seconds',round(time.monotonic()-started,2),flush=True)
 else:
  assert artin(deletion(beta),12)=={i:(i,) for i in range(1,13)}
  w=point_hom(A);assert len(core(w))==1
  new[index]=w;print(index,row['name'],'core',core(w),'length',len(w),flush=True)
assert checks==132
labels=[x for x in d['initial_order'] if x!=12]
killed=[i+1 for i,x in enumerate(labels) if x in [2,3,4,5]]
missing=[i+1 for i,x in enumerate(labels) if x in [1,6,7]]
assert killed==[4,5,6,9] and missing==[8,10,12]
print('Actual constant-family killed indices',killed,'three retained directions',missing,flush=True)
# Source fiber words plus these three actual remaining meridians generate
# the entire generic fiber, if and only if these literal inverse words exist.
combined=list(new.values())+[(j,) for j in missing]
f=WeightedFold(combined,allow_relations=True)
back={j:f.rewrite((j,)) for j in range(1,13)}
print('All12 fiber generators recovered from13 source crossings plus3 retained meridians:',all(w is not None for w in back.values()),flush=True)
if all(w is not None for w in back.values()):
 for j,w in back.items():assert sub(w,{i+1:v for i,v in enumerate(combined)})==(j,)
out={'description':__doc__,'initial_order':d['initial_order'],'source_position':mark,'fiber_labels':labels,'standard_kernel_braids':standards,'standard_kernel_words':fw,'inverse_standard_basis':inverse_basis,'old_and_filled_actions':acts,'old_and_filled_inverse_actions':invs,'source_fiber_words':new,'constant_family_killed_indices':killed,'missing_retained_indices':missing,'fiber_generators_in_source_words_and_missing':back,'full_basis_conjugation_checks':checks,'convention':'Artin action is homomorphic under left substitution; the distinguished-meridian conjugator is anti on the strand-deletion kernel, so its inverse is the actual fiber homomorphism. All132 old/filled conjugation identities checked on a whole kernel basis.','scope':'Actual common source actions and words. Filled negative base loops impose their variation relations; no generic-fiber injection after filling or whole source normality is assumed.'}
(P/'w_pencil_fiber_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all actual w-pencil source/fiber comparisons; seconds',round(time.monotonic()-started,3),flush=True)
