"""All26 local normal forms and82 relation normal generators in one marking.

The82 count is minimal for the stated local types, not a claim that the
displayed generating set is globally minimal. The source-kernel normality
problem remains unresolved.
"""
from pathlib import Path
import json,itertools,hashlib
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'sum_pencil_braids.json').read_text())
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return mul(*(A[x] if x>0 else inv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,24)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,inv(a)),a) if x>0 else (b,mul(inv(b),a,b))
 return A
def Delta(start,size):return tuple(j for length in range(size-1,0,-1) for j in range(start,start+length))
def full(start,size):return tuple(range(start,start+size-1))*size
def comm(a,b):return mul(a,b,inv(a),inv(b))
def candidate(name,support):
 if name=='zero':sizes=[3];kind='full3'
 elif name.startswith('positive_'):sizes=[5];kind='five'
 elif name.startswith('negative_'):sizes=[3];kind='half3'
 elif name.startswith('half_'):sizes=[2,2];kind='nodes'
 elif name.startswith('pair_'):sizes=[3,3];kind='triples'
 else:raise AssertionError(name)
 if len(support)!=sum(sizes):return None
 blocks=[];at=0
 for size in sizes:
  block=support[at:at+size];at+=size
  if block!=list(range(block[0],block[0]+size)):return None
  blocks.append(block)
 if kind=='five':w=mul(Delta(blocks[0][0],5),Delta(blocks[0][0]+1,3))
 elif kind=='half3':w=Delta(blocks[0][0],3)
 else:w=mul(*(full(b[0],len(b)) for b in blocks))
 return kind,blocks,w

new={i:(i,) for i in range(1,24)};new[10]=(10,-14,-13,-12,-11)
old={i:(i,) for i in range(1,24)};old[10]=(10,11,12,13,14)
rows=[];allrels=[]
for row in D['loops']:
 local=mul(*(s['word'] for s in row['forward_segments'][1:]));found=None
 for cut in range(len(local)+1):
  prefix=local[:cut];rotated=mul(local[cut:],prefix);A=art(rotated)
  support=[i for i in range(1,24) if A[i]!=(i,)]
  cand=candidate(row['name'],support)
  if cand and A==art(cand[2]):found=(prefix,*cand);break
 assert found,('no supported local normal form after a prefix',row['name'],local)
 prefix,kind,blocks,standard=found
 W=mul(row['forward_segments'][0]['word'],prefix);A=art(W);Ai=art(inv(W))
 for i in range(1,24):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
 assert art(row['word'])==art(mul(W,standard,inv(W)))
 localrels=[]
 for block in blocks:
  ms=[(i,) for i in block]
  if kind=='five':
   R=mul(*ms[:4]);localrels.append(mul(ms[4],inv(ms[0])))
   localrels.extend(comm(R,ms[j]) for j in (1,2,3))
  elif kind=='half3':localrels.extend([mul(ms[2],inv(ms[0])),comm(ms[0],ms[1])])
  else:
   P=mul(*ms);localrels.extend(comm(P,m) for m in ms[:-1])
 rels=[sub(sub(r,A),new) for r in localrels]
 expected={'full3':2,'five':4,'half3':2,'nodes':2,'triples':4}[kind]
 assert len(rels)==expected
 # The displayed standard action is trivial modulo these local relations:
 # full twists centralize their boundary; half3 identifies the outer pair
 # and commutes the two component meridians; five gives Z times F3.
 rows.append({'name':row['name'],'kind':kind,'absorbed_local_prefix':prefix,
   'local_blocks':blocks,'standard_braid':standard,'whisker_with_prefix':W,
   'local_relators':localrels,'relators_special_source_basis':rels})
 allrels.extend({'origin':row['name'],'word':r} for r in rels)
 print(row['name'],'kind',kind,'prefix length',len(prefix),'blocks',blocks,'relations',len(rels),
       'lengths',[len(r) for r in rels],flush=True)
assert len(allrels)==82
out={'scope':__doc__,'free_generators':list(range(1,24)),
 'source_generators':[i for i in range(1,24) if i not in (11,12,13,14)],
 'source_boundary_generator':10,'deleted_U_indices':[1,2,6,9,15,18,22,23],
 'missing_retained_generators':[11,12,13,14],'old_to_special_basis':new,'special_to_old_basis':old,
 'local_data':rows,'relators':allrels,'listed_relation_count':82,
 'input_sha256':hashlib.sha256((HERE/'sum_pencil_braids.json').read_bytes()).hexdigest(),
 'completion_scope':'The same presentation defines the full profinite completion by closed normal closure. The actual image of the source completion kernel is used; its equality with the full deletion kernel is not proved.'}
(HERE/'sum_pencil_presentation.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all26 actual local normal forms, inverse whisker actions and82 based relation normal generators.')

if __name__=='__main__':pass
