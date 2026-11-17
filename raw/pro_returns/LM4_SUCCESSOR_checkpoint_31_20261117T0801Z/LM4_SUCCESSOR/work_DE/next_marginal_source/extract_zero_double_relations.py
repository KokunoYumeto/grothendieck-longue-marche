"""Literal common-based U/zero node relations, without a normality inference."""
from pathlib import Path
import hashlib,itertools,json
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'remaining_pencil_braids.json').read_text())
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def iv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return mul(*(A[x] if x>0 else iv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,21)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,iv(a)),a) if x>0 else (b,mul(iv(b),a,b))
 return A
def cy(w):
 j=0
 while len(w)-2*j>1 and w[j]==-w[-j-1]:j+=1
 return w[:j],w[j:len(w)-j]
new={i:(i,) for i in range(1,21)};new[10]=(10,-11)
U={1,2,6,9,12,15,19,20};rows=[]
for row in D['loops']:
 if not row['name'].startswith('zero_double_'):continue
 W=row['forward_segments'][0]['word'];A=art(W);Ai=art(iv(W))
 for i in range(1,21):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
 local=mul(*(v['word'] for v in row['forward_segments'][1:]));L=art(local)
 pos=[i for i in range(1,21) if L[i]!=(i,)];assert len(pos)==2 and pos[1]==pos[0]+1
 assert L==art((pos[0],pos[0]))
 meridians=[sub(A[i],new) for i in pos];peeled=[cy(w) for w in meridians]
 assert all(len(core)==1 and core[0]>0 for h,core in peeled)
 zi=next(j for j,(h,core) in enumerate(peeled) if core[0] in (7,14));ui=1-zi
 hz,z=peeled[zi];hu,v=peeled[ui];assert v[0] in U
 k=mul(iv(hz),hu)
 rows.append({'name':row['name'],'local_positions':pos,'meridians_special_basis':meridians,
   'zero_index':z[0],'U_index':v[0],'normalized_U_conjugator':k,
   'b_letters':sum(abs(x)==11 for x in k),
   'normalized_relation':'[zero_generator, k*U_generator*k^-1]=1'})
 print(row['name'],'zero',z[0],'U',v[0],'arc length',len(k),'b letters',rows[-1]['b_letters'],'arc',k,flush=True)
(HERE/'zero_double_relations.json').write_text(json.dumps({'scope':__doc__,
 'input_sha256':hashlib.sha256((HERE/'remaining_pencil_braids.json').read_bytes()).hexdigest(),'relations':rows},indent=2)+'\n')
print('PASS: all8 exact based node relations and inverse Artin transport checks.')
