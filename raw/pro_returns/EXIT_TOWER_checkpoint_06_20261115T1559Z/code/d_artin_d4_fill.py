"""Exact conjugate-relator certificates in Gamma(1,3)=A(D4)/<Delta>.

The seven fixed relators are three braid relations, three commutations,
and Delta=(1234)^3. Positive simple-word conversions use a complete
Matsumoto graph, and each Garside transfer retains its actual relator
path. A certificate expands freely to word * normal_word^{-1}.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
import importlib.util,json,time
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('d4',P/'d_artin_d4.py')
D=importlib.util.module_from_spec(sp);sp.loader.exec_module(D)
cat,inv,red=D.cat,D.inv,D.red
RULES=[((i,4,i),(4,i,4)) for i in (1,2,3)]
RULES += [((i,j),(j,i)) for i,j in ((1,2),(1,3),(2,3))]
RELS=[cat(a,inv(b)) for a,b in RULES]+[D.DELTA]
def conjugate(c,S):return tuple((cat(c,p),j,e) for p,j,e in S)
def inverse(S):return tuple((p,j,-e) for p,j,e in reversed(S))
def expanded(S):
 out=[]
 for c,j,e in S:
  for x in c+(RELS[j] if e>0 else inv(RELS[j]))+inv(c):
   if out and out[-1]==-x:out.pop()
   else:out.append(x)
 return tuple(out)
def reduce_sequence(S):
 out=[]
 for x in S:
  if out and out[-1][:2]==x[:2] and out[-1][2]==-x[2]:out.pop()
  else:out.append(x)
 return tuple(out)
def simple_id(w):
 s=D.one
 for x in w:
  assert x>0
  s=D.mult[s][D.gen[x-1]]
 assert D.length[s]==len(w),(w,'not Coxeter-reduced')
 return s
TREES={}
def matsumoto_tree(s):
 if s in TREES:return TREES[s]
 root=D.reps[D.W[s]];parent={root:None};todo=deque([root])
 while todo:
  w=todo.popleft()
  for j,(a,b) in enumerate(RULES):
   for lhs,rhs,e in ((a,b,1),(b,a,-1)):
    m=len(lhs)
    for p in range(len(w)-m+1):
     if w[p:p+m]!=lhs:continue
     v=w[:p]+rhs+w[p+m:]
     if v not in parent:
      parent[v]=(w,p,j,e);todo.append(v)
 TREES[s]=parent
 return parent
@lru_cache(maxsize=100000)
def to_canonical(w):
 s=simple_id(w);parent=matsumoto_tree(s)
 assert w in parent,(s,w,'Matsumoto component missing')
 out=[]
 while parent[w] is not None:
  old,p,j,e=parent[w]
  out.append((w[:p],j,-e));w=old
 return tuple(out)
@lru_cache(maxsize=100000)
def simple_between(u,v):
 assert simple_id(u)==simple_id(v)
 C=reduce_sequence(to_canonical(u)+inverse(to_canonical(v)))
 assert expanded(C)==cat(u,inv(v))
 return C
def sw(s):return D.reps[D.W[s]]
DELTA_CERT=simple_between(sw(D.D),D.DELTA)+(((),6,1),)
NEG_CERT={}
for x in range(1,5):
 c=sw(D.complement[D.gen[x-1]])
 R=simple_between((x,)+c,D.DELTA)+(((),6,1),)
 C=conjugate((-x,),inverse(R))
 assert expanded(C)==cat((-x,),inv(c))
 NEG_CERT[x]=C
@lru_cache(maxsize=100000)
def normalize(w):
 w=red(w);positive=();out=[]
 for x in w:
  if x>0:positive+=(x,)
  else:
   out.extend(conjugate(positive,NEG_CERT[-x]))
   positive+=sw(D.complement[D.gen[-x-1]])
 factors=[D.gen[x-1] for x in positive]
 while True:
  # In the central quotient every literal Delta block may be deleted.
  if D.D in factors:
   k=factors.index(D.D);prefix=cat(*(sw(s) for s in factors[:k]))
   out.extend(conjugate(prefix,DELTA_CERT))
   del factors[k]
   continue
  change=False
  for k in range(len(factors)-1):
   a,b=factors[k:k+2];d=D.gcd[D.complement[a],b]
   if d==D.one:continue
   ap=D.mult[a][d];bp=D.mult[D.inverse[d]][b]
   A,B,DD,AP,BP=sw(a),sw(b),sw(d),sw(ap),sw(bp)
   step=conjugate(A,simple_between(B,DD+BP))+simple_between(A+DD,AP)
   assert expanded(step)==cat(A,B,inv(cat(AP,BP)))
   prefix=cat(*(sw(s) for s in factors[:k]))
   out.extend(conjugate(prefix,step))
   factors[k:k+2]=[s for s in (ap,bp) if s!=D.one]
   change=True
   break
  if not change:break
 nf=cat(*(sw(s) for s in factors));out=reduce_sequence(out)
 assert expanded(out)==cat(w,inv(nf)),('bad free certificate',w,nf)
 assert D.equal(w,nf)
 return nf,out
def fill(w):
 nf,C=normalize(tuple(w))
 assert not nf,('word not identity',w,nf)
 return C
if __name__=='__main__':
 started=time.time()
 sizes=[len(fill(r)) for r in RELS]
 samples=[(1,-2,4,-3,2,-4),D.DELTA+(1,)+inv(D.DELTA)+(-1,)]
 for w in samples:
  nf,C=normalize(w);assert expanded(C)==cat(w,inv(nf))
 out={'relators':RELS,'defining_certificate_sizes':sizes,
      'matsumoto_components':len(TREES),'matsumoto_vertices':sum(map(len,TREES.values())),
      'convention':'certificate expands freely to word times inverse normal word',
      'seconds':time.time()-started}
 (P/'d_artin_d4_fill.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out,flush=True)
